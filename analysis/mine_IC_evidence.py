
import os
import json
import csv
import re
import glob
from collections import defaultdict, Counter

# --- Configuration ---
CORPUS_DIR = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns"
EXTRACTIONS_DIR = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\extraction_results_v4"
OUTPUT_DIR = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\analysis"

# Definition of Terms and Keywords
TERMINOLOGY_TERMS = [
    "ISAC-OF", "fiber-ISAC", "photonic ISAC", "optical ISAC", "RO-ISAC",
    "distributed acoustic sensing", "LiDAR", "FSO", "VLC", "Photo-THz", "LiFi"
]

METRIC_TERMS = [
    r"\\Delta R", "range resolution", "RMSE", r"\\sigma_R", "CRB", "FIM", "Cramér-Rao",
    "localization error", "sensing accuracy", "capacity-resolution", "Pareto", "trade-off"
]

# Modality Keywords
MODALITY_KEYWORDS = {
    "Fiber": ["fiber", "optical fiber", "DAS", "φ-OTDR", "DSCM", "cabled"],
    "FSO": ["free-space optical", "FSO", "atmospheric", "turbulence"],
    "VLC": ["visible light", "VLC", "LiFi", "illumination", "LED"],
    "Photo-THz": ["photonic terahertz", "photo-THz", "terahertz", "THz", "300 GHz"],
    "RO-ISAC": ["retroreflective", "corner cube", "modulating retroreflector"]
}

# C4: Weak Tech Transfer / Fragmentation Keywords
TRANSFER_GAP_KEYWORDS = [
    "limit", "gap", "lack", "missing", "challenge", "unexplored", "separate", 
    "independently", "transfer", "borrow", "cross-domain", "silo", "fragment", 
    "incompatible", "diverse", "heterogeneous", "unified framework"
]

# --- Helper Functions ---

def clean_text(text):
    """Remove newlines and extra spaces."""
    if not text: return ""
    return " ".join(text.split()).strip()

def smart_truncate(text, center_idx, window_words=15):
    """Return a ~30 word excerpt centered on index."""
    # Find start/end word boundaries
    words = text.split()
    
    # Map char index to word index (approximate)
    # This is expensive if done naively. Let's do a sliding window check?
    # Simpler: just take characters +/- 150 chars, then strip to nearest space.
    
    start_char = max(0, center_idx - 150)
    end_char = min(len(text), center_idx + 150)
    
    raw_slice = text[start_char:end_char]
    
    # Try to center the keyword if possible
    # But strictly, let's just use the 30 words rule on the raw slice
    
    # Tokenize the slice
    slice_tokens = raw_slice.split()
    
    # We want ~30 words. If the slice is huge, we might have too many.
    # We don't know exactly where the keyword is in the slice tokens relative to start.
    
    # fallback: regex word finder
    # 1. Find the term in the text to ensure we focus on it.
    # (The caller passes center_idx).
    
    subtext = text[max(0, center_idx - 200) : min(len(text), center_idx + 200)]
    # This subtext contains the keyword roughly in middle.
    
    sub_words = subtext.split()
    mid_point = len(sub_words) // 2
    
    start_w = max(0, mid_point - window_words)
    end_w = min(len(sub_words), mid_point + window_words)
    
    excerpt = " ".join(sub_words[start_w:end_w])
    return f"...{excerpt}..."

def parse_markdown_metadata(full_text):
    """Extract Year and Title from MD content if JSON missing."""
    meta = {"year": "20XX", "title": "Unknown Title"}
    
    # 1. Look for Year
    # Common formats: "IEEE ... 2024", "Vol. 40, 2022", "Date of Publication: ... 2023"
    year_pats = [
        r"202[0-5]",
        r"© (202[0-5])",
        r"Vol\.\s*\d+,\s*No\.\s*\d+,\s*.*(202\d)"
    ]
    
    for pat in year_pats:
        m = re.search(pat, full_text[:2000]) # Check first 2k chars
        if m:
            # if group captured
            if m.groups():
                meta["year"] = m.group(1)
            else:
                meta["year"] = m.group(0)
            break
            
    # 2. Look for Title
    # Often first line or # Title
    lines = full_text.split('\n')
    for line in lines[:20]:
        line = line.strip()
        if line.startswith("# "):
            meta["title"] = line[2:].strip()
            break
        if len(line) > 20 and "IEEE" not in line and "http" not in line:
            # Heuristic: First long line might be title
            if meta["title"] == "Unknown Title":
                meta["title"] = line
                
    return meta

def get_modality(text, title, json_modality=None):
    if json_modality and json_modality not in ["Unknown", "Other"]:
        return json_modality
    
    text_lower = (text + " " + title).lower()
    counts = Counter()
    for mod, keywords in MODALITY_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in text_lower:
                counts[mod] += 1
    
    if not counts:
        return "Other"
    return counts.most_common(1)[0][0]

def get_location_label(text, char_idx):
    """Find the nearest preceding header."""
    # Search backwards from char_idx for a line starting with #
    # This is inefficient for large files repeated calls.
    # Better: Scan file lines once, build a map of (start_char, end_char) -> Header.
    pass # Implemented inside main loop for efficiency

# --- Main Logic ---

def main():
    print("Starting Evidence Mining (v2 - Patch Run)...")
    
    # 1. Load Extractions (JSON)
    metadata_map = {}
    json_files = glob.glob(os.path.join(EXTRACTIONS_DIR, "*.json"))
    for jf in json_files:
        try:
            with open(jf, 'r', encoding='utf-8') as f:
                data = json.load(f)
                pid = data.get("paper_id", os.path.basename(jf).replace(".json", ""))
                metadata_map[pid] = data
        except:
            pass

    # 2. Scan Corpus
    evidence_rows = []
    
    # Compile regexes
    metric_regexes = [re.compile(p, re.IGNORECASE) for p in METRIC_TERMS]
    term_regexes = [re.compile(re.escape(t), re.IGNORECASE) for t in TERMINOLOGY_TERMS]
    c4_regexes = [re.compile(r"\b" + re.escape(w) + r"\b", re.IGNORECASE) for w in TRANSFER_GAP_KEYWORDS]
    
    paper_dirs = glob.glob(os.path.join(CORPUS_DIR, "O_ISAC_*"))
    
    for p_dir in paper_dirs:
        pid = os.path.basename(p_dir)
        md_path = os.path.join(p_dir, f"{pid}.md")
        
        if not os.path.exists(md_path):
            continue
            
        with open(md_path, 'r', encoding='utf-8') as f:
            full_text = f.read()
            
        # Refined Metadata
        json_meta = metadata_map.get(pid, {})
        
        # Title/Year logic
        parsed_meta = parse_markdown_metadata(full_text)
        
        title = json_meta.get("title") or parsed_meta["title"]
        year = json_meta.get("year") 
        if not year or str(year) == "20XX":
            year = parsed_meta["year"]
        
        modality = get_modality(full_text, title, json_meta.get("modality"))
        
        # Build Section Map
        # list of (start_idx, header_name)
        section_map = []
        for m in re.finditer(r"^#+\s+(.*)", full_text, re.MULTILINE):
            section_map.append((m.start(), m.group(1).strip()))
        section_map.append((len(full_text), "EOF")) 
        
        def find_section(idx):
            current = "Introduction/Body" # Default
            for i in range(len(section_map)-1):
                if section_map[i][0] <= idx < section_map[i+1][0]:
                    current = section_map[i][1]
                    break
            return current

        # Claim Mining
        
        # C1: Terminology
        # Logic: Usage of multiple terms OR explicit definitions
        # Scan for terms
        for t_re in term_regexes:
            for m in t_re.finditer(full_text):
                # FILTER: Only log if it looks like a definition or explicit usage?
                # For v2, we want Explicit inconsistency. 
                # Heuristic: "called", "known as", "termed" nearby?
                # Or just basic usage if it's one of the fragmented terms like "ISAC-OF"
                term_str = m.group(0)
                
                # Check for "aka" context
                window = full_text[max(0, m.start()-50):min(len(full_text), m.end()+50)].lower()
                is_explicit = any(x in window for x in ["called", "known as", "termed", "referred", "defined"])
                
                if is_explicit or term_str in ["ISAC-OF", "RO-ISAC", "photonic ISAC"]:
                    excerpt = smart_truncate(full_text, m.start(), 15)
                    evidence_rows.append({
                        "claim_id": "C1",
                        "claim_short": "Terminology Inconsistency",
                        "paper_id": pid,
                        "year": year,
                        "title": title,
                        "modality": modality,
                        "evidence_type": "Other", # Infer
                        "where_in_paper": find_section(m.start()),
                        "supporting_excerpt": clean_text(excerpt),
                        "why_it_supports": f"Explicit/Distinct usage of '{term_str}'",
                        "metric_terms": "",
                        "terminology_terms": term_str,
                        "cross_domain_note": "",
                        "confidence": 0.9 if is_explicit else 0.7,
                        "source_path": md_path,
                        "source_locator": f"Section: {find_section(m.start())}"
                    })
                    break # One per term per paper to avoid spam

        # C2: Metrics
        # Logic: Definitions of metrics
        for m_re in metric_regexes:
            for m in m_re.finditer(full_text):
                # Search for definition context: "=" or "defined" or "denotes"
                window = full_text[max(0, m.start()-50):min(len(full_text), m.end()+100)]
                is_def = "=" in window or "defined" in window or "expressed" in window
                
                if is_def:
                    excerpt = smart_truncate(full_text, m.start(), 20)
                    evidence_rows.append({
                        "claim_id": "C2",
                        "claim_short": "Metric Definition/Usage",
                        "paper_id": pid,
                        "year": year,
                        "title": title,
                        "modality": modality,
                        "evidence_type": "Other",
                        "where_in_paper": find_section(m.start()),
                        "supporting_excerpt": clean_text(excerpt),
                        "why_it_supports": f"Defines/Uses metric '{m.group(0)}'",
                        "metric_terms": m.group(0),
                        "terminology_terms": "",
                        "cross_domain_note": "",
                        "confidence": 0.85,
                        "source_path": md_path,
                        "source_locator": f"Section: {find_section(m.start())}"
                    })
                    break # One per metric per paper

        # C4: Cross-Domain Tech Transfer Gap
        # Logic: Keyword "gap"/"challenge" appearing in Introduction or Conclusion, 
        # OR appearing near "future work"
        # AND mentioning other modalities?
        
        # Scan for GAP keywords
        for gap_re in c4_regexes:
            for m in gap_re.finditer(full_text):
                section = find_section(m.start())
                
                # Boost if in Intro/Conclusion
                is_strategic = any(x in section.lower() for x in ["intro", "conclusion", "future", "discussion"])
                
                if is_strategic:
                    excerpt = smart_truncate(full_text, m.start(), 25)
                    
                    # Logic: Does excerpt mention another modality or "standard"?
                    excerpt_lower = excerpt.lower()
                    has_cross = "standard" in excerpt_lower or "framework" in excerpt_lower or "unified" in excerpt_lower
                    # Or mentions other modalities
                    other_mods = [mod for mod, kws in MODALITY_KEYWORDS.items() if mod != modality and any(k.lower() in excerpt_lower for k in kws)]
                    
                    if has_cross or other_mods:
                        evidence_rows.append({
                            "claim_id": "C4",
                            "claim_short": "Cross-Domain Gap/Transfer",
                            "paper_id": pid,
                            "year": year,
                            "title": title,
                            "modality": modality,
                            "evidence_type": "Survey" if "Survey" in title or "Review" in title else "Other",
                            "where_in_paper": section,
                            "supporting_excerpt": clean_text(excerpt),
                            "why_it_supports": f"Discusses '{m.group(0)}' in strategic section '{section}'",
                            "metric_terms": "",
                            "terminology_terms": "",
                            "cross_domain_note": f"Mentions {other_mods} or standardization",
                            "confidence": 0.9,
                            "source_path": md_path,
                            "source_locator": f"Section: {section}"
                        })

    # Deduplicate and Sort
    # Priority: Higher confidence, then Year desc
    
    unique_rows = []
    seen = set()
    
    # Sort by claim, then confidence desc
    evidence_rows.sort(key=lambda x: (x['claim_id'], -x['confidence']))
    
    for row in evidence_rows:
        # Key: Paper + Claim. (We only want the BEST evidence for a claim from a paper)
        k = (row['paper_id'], row['claim_id'])
        if k not in seen:
            seen.add(k)
            unique_rows.append(row)
            
    # Write to CSV v2
    csv_path = os.path.join(OUTPUT_DIR, "IC_evidence_claims_v2.csv")
    headers = [
        "claim_id", "claim_short", "paper_id", "year", "title", "modality",
        "evidence_type", "where_in_paper", "supporting_excerpt", "why_it_supports",
        "metric_terms", "terminology_terms", "cross_domain_note", "confidence",
        "source_path", "source_locator"
    ]
    
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(unique_rows)
        
    print(f"Wrote {len(unique_rows)} rows to {csv_path}")
    
    # Verify C4 count
    c4_count = len([x for x in unique_rows if x['claim_id'] == 'C4'])
    print(f"C4 Items Found: {c4_count}")

    # Gen Summary v2
    summary_path = os.path.join(OUTPUT_DIR, "IC_evidence_summary_v2.md")
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write("# Evidence Summary v2 (Patch Run)\n\n")
        f.write(f"Total Evidence Items: {len(unique_rows)}\n")
        f.write(f"C4 (Gap/Transfer) Items: {c4_count}\n\n")
        
        # Breakdown
        counts = Counter([x['claim_id'] for x in unique_rows])
        for k,v in counts.items():
            f.write(f"- {k}: {v}\n")

if __name__ == "__main__":
    main()
