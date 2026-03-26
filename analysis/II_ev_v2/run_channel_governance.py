import os
import glob
import re
import csv
import sys
from collections import Counter

# =============================================================================
# CONSTANTS & PATTERNS
# =============================================================================

OUTPUT_DIR = r"analysis/II_ev_v2"
EVIDENCE_CSV = os.path.join(OUTPUT_DIR, "section2B_evidence.csv")
GOVERNANCE_DOC = os.path.join("analysis", "II_channel_governance.md")
PATCH_NOTES = os.path.join(OUTPUT_DIR, "patch_notes_for_writing_2B.md")

# Ensure output dir exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Regex patterns for Channel Models (II-B Scope)
# We strictly classify them into "Families".

PATTERNS = {
    "attenuation_beer_lambert": [
        r"(?i)Beer[-–]Lambert",
        r"(?i)Beer.?s\s+law",
        r"(?i)extinction\s+coefficient",
        r"(?i)attenuation\s+coefficient",
        r"(?i)atmospheric\s+loss",
        r"h_\{?atm\}?",
        r"H_\{?atm\}?",
        r"(?i)exp\(\s*-\s*sigma\s*L\s*\)"
    ],
    "turbulence_gamma_gamma": [
        r"(?i)Gamma[-–]Gamma",
        r"(?i)\bGG\b\s+distribution",
        r"(?i)\bGG\b\s+fading",
        r"(?i)\bGG\b\s+turbulence"
    ],
    "turbulence_log_normal": [
        r"(?i)Log[-–]normal",
        r"(?i)Lognormal",
        r"(?i)\bLN\b\s+distribution",
        r"(?i)weak\s+turbulence"
    ],
    "turbulence_malaga": [
        r"(?i)Málaga",
        r"(?i)Malaga",
        r"(?i)M[-–]distribution"
    ],
    "turbulence_general": [
        r"(?i)scintillation\s+index",
        r"(?i)Rytov\s+variance",
        r"(?i)refractive\s+index\s+structure\s+parameter",
        r"C_n\^2",
        r"C_\{?n\}?\^2",
        r"(?i)turbulence\s+fading",
        r"h_\{?tur\}?",
        r"H_\{?tur\}?"
    ],
    "pointing_error": [
        r"(?i)pointing\s+error",
        r"(?i)beam\s+wander",
        r"(?i)misalignment\s+loss",
        r"(?i)misalignment\s+fading",
        r"(?i)boresight",
        r"(?i)jitter",
        r"h_\{?p\}?",
        r"H_\{?p\}?"
    ],
    "multipath_nlos": [
        r"(?i)multipath",
        r"(?i)non[-–]line[-–]of[-–]sight",
        r"(?i)\bNLoS\b",
        r"(?i)diffuse\s+reflection",
        r"(?i)specular\s+reflection",
        r"(?i)Lambertian",
        r"(?i)impulse\s+response"
    ],
    "noise_regime": [
        r"(?i)shot\s+noise",
        r"(?i)thermal\s+noise",
        r"(?i)ambient\s+light",
        r"(?i)background\s+radiation",
        r"(?i)phase\s+noise"
    ]
}

HEADING_RE = re.compile(r"^#+\s+(.*)")

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def find_root():
    # Heuristic: verify we are in a repo by checking for 'analysis' or 'data' folder
    # In this environment, we are likely at root.
    if os.path.exists("data") and os.path.exists("analysis"):
        return "."
    # Walk up
    cur = os.getcwd()
    while True:
        if os.path.exists(os.path.join(cur, "data")):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            raise Exception("Cannot find repo root (looked for 'data' folder)")
        cur = parent

def load_processed_markdowns(root_dir):
    search_path = os.path.join(root_dir, "data", "processed_markdowns")
    if not os.path.exists(search_path):
        print(f"Warning: {search_path} does not exist. Trying generic search.")
        search_path = root_dir
        
    files = glob.glob(os.path.join(search_path, "**", "*.md"), recursive=True)
    # Filter for O_ISAC or COMST only
    files = [f for f in files if "O_ISAC" in f or "COMST" in f]
    return list(set(files))

def parse_heading_map(lines):
    # Returns list mapping line_idx -> heading_path
    map_ = []
    stack = []
    
    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            text = m.group(1).strip()
            level = 0
            while line[level] == '#':
                level += 1
            
            # Adjust stack
            while len(stack) >= level:
                stack.pop()
            stack.append(text)
        
        path = " > ".join(stack) if stack else "Root"
        map_.append(path)
    return map_

def check_patterns(text, line_idx, patterns_dict):
    # Returns (model_tag, match_text)
    for tag, regexes in patterns_dict.items():
        for r in regexes:
            m = re.search(r, text)
            if m:
                return tag, m.group(0)
    return None, None

def determine_strength(match_text, context_window):
    # Heuristic strength; 
    # Strong: definitions "H =", "where x is..."
    # Medium: Specific references
    # Weak: passing mentions
    
    combined = " ".join(context_window)
    lower_comb = combined.lower()
    
    if "=" in match_text or "defined as" in lower_comb or "where" in lower_comb:
        return "strong"
    if len(match_text) > 5: # specific term
        return "medium"
    return "weak"

def determine_domain(text_window):
    # Heuristic domain detection in context
    txt = " ".join(text_window).lower()
    if "fiber" in txt or "smf" in txt:
        return "Fiber"
    if "fso" in txt or "free space" in txt or "atmospheric" in txt:
        return "FSO"
    if "vlc" in txt or "visible light" in txt or "led" in txt:
        return "VLC"
    if "uwoc" in txt or "underwater" in txt:
        return "UWOC"
    return "Ambiguous"

# =============================================================================
# MAIN MINING LOGIC
# =============================================================================

def mine_evidence(files):
    evidence_rows = []
    
    print(f"Scanning {len(files)} files...")
    
    for fpath in files:
        fname = os.path.basename(fpath)
        pid = fname.replace(".md", "")
        
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except:
            continue
            
        heading_map = parse_heading_map(lines)
        
        # Scan lines
        for i, line in enumerate(lines):
            line = line.strip()
            if not line: continue
            
            tag, match = check_patterns(line, i, PATTERNS)
            if tag:
                # Context Window (±5 lines for heuristic)
                start = max(0, i - 5)
                end = min(len(lines), i + 6)
                context = [l.strip() for l in lines[start:end]]
                
                strength = determine_strength(match, context)
                domain = determine_domain(context)
                heading = heading_map[i]
                
                # Check for "References" section blockage
                if "reference" in heading.lower() or "bibliography" in heading.lower():
                    continue

                # Quote cleaning
                quote = line
                if len(quote.split()) > 25:
                    # Snip around match
                    idx_match = quote.find(match)
                    start_q = max(0, idx_match - 50)
                    end_q = min(len(quote), idx_match + 50)
                    quote = "..." + quote[start_q:end_q] + "..."

                row = {
                    "paper_id": pid,
                    "channel_factor": tag,
                    "model_tag": tag, # Redundant but useful
                    "domain": domain,
                    "strength": strength,
                    "quote": quote,
                    "heading_path": heading,
                    "line_start": i + 1,
                    "line_end": i + 1, # Single line hit
                    "rationale": f"Matched pattern '{match}' in context.",
                    "context_verified": False # Regex only
                }
                
                evidence_rows.append(row)
                
    return evidence_rows

# =============================================================================
# ARTIFACT GENERATION
# =============================================================================

def generate_governance_doc(evidence_rows):
    # D2: II_channel_governance.md
    
    # Analyze stats
    tags = [r['model_tag'] for r in evidence_rows]
    counts = Counter(tags)
    
    content = f"""# Section II-B: Channel Model Governance
    
## 1. Symbol Conventions
- **Atmospheric Loss**: Prefer $h_{{atm}}$ or $L_{{atm}}$.
- **Turbulence**: Prefer $h_{{tur}}$ or $h_{{turb}}$.
- **Pointing Error**: Prefer $h_{{p}}$.
- **Structure Parameter**: $C_n^2$ (avoid conflating with scintillation index $\sigma_I^2$).

## 2. Do-Not-Conflate Rules
- **Gamma-Gamma vs Log-Normal**: Verify turbulence regime. Log-Normal is weak turbulence ($<1$ km or low $C_n^2$), Gamma-Gamma covers weak-to-strong.
- **Path Loss includes Pointing?**: Explicitly check if geometric loss $h_{{geo}}$ includes pointing error $h_{{p}}$.
- **Attenuation vs Fading**: Attenuation is deterministic (Beer-Lambert); Fading is stochastic (Turbulence).

## 3. Detected Usage Statistics (from Corpus)
"""
    for tag, count in counts.most_common():
        content += f"- **{tag}**: {count} occurrences\n"
        
    with open(GOVERNANCE_DOC, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {GOVERNANCE_DOC}")

def generate_patch_notes(evidence_rows):
    # D4: patch_notes.md
    # Filter for 'strong' evidence
    strong_rows = [r for r in evidence_rows if r['strength'] == 'strong']
    
    # If not enough strong, use medium
    if len(strong_rows) < 10:
        strong_rows.extend([r for r in evidence_rows if r['strength'] == 'medium'])
    
    # Distinct papers
    seen_papers = set()
    selected = []
    for r in strong_rows:
        if r['paper_id'] not in seen_papers:
            selected.append(r)
            seen_papers.add(r['paper_id'])
        if len(selected) >= 25: break
        
    content = "# Patch Notes for Section II-B (Channel Models)\n\n"
    
    for r in selected:
        content += f"- **{r['paper_id']} ({r['model_tag']})**: Evidence suggests using {r['model_tag'].replace('_', ' ')} model. Locator: `[{r['heading_path']} | L{r['line_start']}]`. Quote: \"{r['quote']}\"\n"
        
    with open(PATCH_NOTES, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {PATCH_NOTES}")

def export_csv(evidence_rows):
    if not evidence_rows:
        print("No evidence to export.")
        return
        
    keys = evidence_rows[0].keys()
    with open(EVIDENCE_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(evidence_rows)
    print(f"Generated {EVIDENCE_CSV} ({len(evidence_rows)} rows)")

def print_qc(evidence_rows):
    print("\n=== QC SUMMARY ===")
    print(f"Total Lines of Evidence: {len(evidence_rows)}")
    tags = Counter([r['model_tag'] for r in evidence_rows])
    print("Tag Distribution:")
    for t, c in tags.items():
        print(f"  {t}: {c}")
        
    ambiguous = [r for r in evidence_rows if r['domain'] == 'Ambiguous']
    print(f"Ambiguous Domain cases: {len(ambiguous)}")

# =============================================================================
# RUNNER
# =============================================================================

def main():
    root = find_root()
    files = load_processed_markdowns(root)
    
    if not files:
        print("FAIL: No processed markdown files found.")
        return
        
    evidence = mine_evidence(files)
    
    export_csv(evidence)
    generate_governance_doc(evidence)
    generate_patch_notes(evidence)
    print_qc(evidence)

if __name__ == "__main__":
    main()
