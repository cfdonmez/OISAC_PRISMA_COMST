#!/usr/bin/env python3
"""
mine_ID_surveys_v2_3_1.py - Repair Tier-2 Evidence Quality

Fixes v2.3 locator compliance from 3/44 to 100% for CORE set.
Curates 12-20 CORE feeders with balanced subdomains.
"""

import json
import csv
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Configuration
BASE_DIR = Path(r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST")
CORPUS_DIR = BASE_DIR / "data" / "processed_markdowns"
V23_DIR = BASE_DIR / "analysis" / "ID_v2_3" / "run_20260120_010054"

TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_DIR = BASE_DIR / "analysis" / "ID_v2_3_1" / f"run_{TIMESTAMP}"

# Target CORE counts per subdomain
CORE_TARGETS = {
    'VLC_positioning': 5,
    'DFOS_DAS': 4,
    'FSO_channel': 4,
    'Optical_transmission': 4,
    'O-ISAC': 2,  # Tier-1
}

# Excluded sections
EXCLUDED_PATTERNS = [
    r'(?i)acknowledg', r'(?i)funding', r'(?i)reference', r'(?i)author',
    r'(?i)appendix', r'(?i)biograph', r'(?i)conflict'
]

def load_markdown(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return ""

def parse_headings_with_lines(content):
    """Parse headings with line numbers."""
    lines = content.split('\n')
    headings = []
    for i, line in enumerate(lines, 1):
        match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
        if match:
            level = len(match.group(1))
            title = re.sub(r'[*`<>]', '', match.group(2)).strip()[:60]
            headings.append({'level': level, 'title': title, 'line': i})
    return headings, lines

def get_heading_path(headings, line_num):
    """Get heading path for a line number."""
    path_parts = []
    for h in headings:
        if h['line'] <= line_num:
            while path_parts and path_parts[-1][0] >= h['level']:
                path_parts.pop()
            path_parts.append((h['level'], h['title']))
        else:
            break
    path = ' > '.join([p[1] for p in path_parts]) if path_parts else "Document"
    return path[:80]

def is_excluded(heading_path):
    for p in EXCLUDED_PATTERNS:
        if re.search(p, heading_path):
            return True
    return False

def is_intro_section(heading_path, line_num):
    """Check if in Abstract/Introduction."""
    lower = heading_path.lower()
    if 'abstract' in lower or 'introduction' in lower or 'overview' in lower:
        return True
    if line_num < 80:  # Early in document
        return True
    return False

def is_conclusion_section(heading_path):
    """Check if in Conclusion/Future/Challenges."""
    lower = heading_path.lower()
    return any(w in lower for w in ['conclusion', 'future', 'challenge', 'discussion', 'summary', 'outlook'])

def extract_scope_with_locator(content, headings):
    """Extract scope excerpt with locator from Abstract/Intro."""
    patterns = [
        r'(?i)(this\s+(survey|review|paper|work)\s+(?:provides|presents|reviews|summarizes|investigates|proposes)[^.]{10,120}\.)',
        r'(?i)(we\s+(review|provide|present|summarize|investigate)\s+[^.]{10,120}\.)',
        r'(?i)(the\s+(?:main|primary)\s+(?:focus|objective|goal|contribution)[^.]{10,100}\.)',
        r'(?i)(this\s+(?:article|study)\s+(?:addresses|focuses|examines)[^.]{10,100}\.)',
    ]
    
    # Search in first 8000 chars
    intro = content[:8000]
    
    for pattern in patterns:
        match = re.search(pattern, intro)
        if match:
            found_pos = match.start()
            line_num = content[:found_pos].count('\n') + 1
            heading = get_heading_path(headings, line_num)
            
            if is_intro_section(heading, line_num) and not is_excluded(heading):
                excerpt = match.group(0).strip()
                words = excerpt.split()[:25]
                locator = f"{heading} (L{line_num})"
                return ' '.join(words), locator
    
    # Fallback: first substantive sentence in intro
    intro_patterns = [
        r'(?i)^([A-Z][^.]{30,150}(?:communication|sensing|optical|fiber|vlc|fso)[^.]*\.)',
    ]
    for pattern in intro_patterns:
        match = re.search(pattern, intro, re.MULTILINE)
        if match:
            found_pos = match.start()
            line_num = content[:found_pos].count('\n') + 1
            heading = get_heading_path(headings, line_num)
            if not is_excluded(heading):
                excerpt = match.group(1).strip()
                words = excerpt.split()[:25]
                return ' '.join(words), f"{heading} (L{line_num})"
    
    return "", ""

def extract_limitations_with_locator(content, headings):
    """Extract limitations excerpt with locator from Conclusion/Future."""
    patterns = [
        r'(?i)(future\s+(?:work|research|direction|study)[^.]{10,100}\.)',
        r'(?i)((?:remain|open)\s+(?:challenge|issue|problem)[^.]{10,100}\.)',
        r'(?i)(however,\s+[^.]*(?:limitation|not\s+address|not\s+consider|beyond\s+scope)[^.]*\.)',
        r'(?i)((?:do|did|does)\s+not\s+(?:address|consider|cover)[^.]{10,80}\.)',
        r'(?i)(further\s+(?:investigation|research|study)\s+[^.]{10,80}\.)',
    ]
    
    # Search in last 40% of document
    start_pos = int(len(content) * 0.6)
    end_content = content[start_pos:]
    
    for pattern in patterns:
        match = re.search(pattern, end_content)
        if match:
            abs_pos = start_pos + match.start()
            line_num = content[:abs_pos].count('\n') + 1
            heading = get_heading_path(headings, line_num)
            
            if is_conclusion_section(heading) and not is_excluded(heading):
                excerpt = match.group(0).strip()
                words = excerpt.split()[:25]
                locator = f"{heading} (L{line_num})"
                return ' '.join(words), locator
    
    return "", ""

def compute_feeder_strength(content, headings, scope, limit):
    """Compute feeder strength score 0-10."""
    score = 0
    
    # Has explicit scope language (+3)
    if scope:
        score += 3
    
    # Has explicit limitation language (+3)
    if limit:
        score += 3
    
    # Breadth: count of distinct section headings (+0-2)
    section_count = len([h for h in headings if h['level'] <= 2])
    if section_count >= 10:
        score += 2
    elif section_count >= 5:
        score += 1
    
    # Has taxonomy/classification section (+2)
    for h in headings:
        if any(w in h['title'].lower() for w in ['taxonomy', 'classification', 'categorization']):
            score += 2
            break
    
    return min(score, 10)

def load_v23_catalog():
    """Load v2.3 catalog."""
    catalog = []
    path = V23_DIR / "ID_related_catalog_v2_3.csv"
    if path.exists():
        with open(path, 'r', encoding='utf-8') as f:
            for row in csv.DictReader(f):
                catalog.append(row)
    return catalog

def pass1_parse_and_extract(catalog):
    """PASS 1-2: Parse markdowns and extract evidence with locators."""
    print("\n" + "="*60)
    print("PASS 1-2: Parsing and Extracting Evidence")
    print("="*60)
    
    updated = []
    
    for entry in catalog:
        paper_id = entry['paper_id']
        tier = entry.get('tier', '2')
        
        # Tier-1: keep as-is (already has good locators)
        if tier == '1':
            entry['feeder_strength'] = 10
            entry['is_core'] = 1
            updated.append(entry)
            continue
        
        # Tier-2: re-extract with locators
        md_path = Path(entry.get('source_path', ''))
        if not md_path.exists():
            md_path = CORPUS_DIR / paper_id / f"{paper_id}.md"
        
        content = load_markdown(md_path)
        if not content:
            entry['feeder_strength'] = 0
            entry['is_core'] = 0
            updated.append(entry)
            continue
        
        headings, lines = parse_headings_with_lines(content)
        
        # Extract evidence
        scope, scope_loc = extract_scope_with_locator(content, headings)
        limit, limit_loc = extract_limitations_with_locator(content, headings)
        
        # Update entry
        entry['scope_excerpt'] = scope.replace('\n', ' ')[:150] if scope else ''
        entry['scope_locator'] = scope_loc if scope else ''
        entry['limitations_excerpt'] = limit.replace('\n', ' ')[:150] if limit else ''
        entry['limitations_locator'] = limit_loc if limit else ''
        
        # Compute strength
        strength = compute_feeder_strength(content, headings, scope, limit)
        entry['feeder_strength'] = strength
        entry['is_core'] = 0  # Will be set in PASS 3
        
        updated.append(entry)
    
    # Stats
    tier2 = [e for e in updated if e.get('tier') == '2']
    with_scope = sum(1 for e in tier2 if e.get('scope_locator'))
    with_limit = sum(1 for e in tier2 if e.get('limitations_locator'))
    
    print(f"  Tier-2 papers: {len(tier2)}")
    print(f"  With scope locator: {with_scope}")
    print(f"  With limitations locator: {with_limit}")
    
    return updated

def pass3_curate_core(catalog):
    """PASS 3: Curate CORE feeder set."""
    print("\n" + "="*60)
    print("PASS 3: Curating CORE Feeder Set")
    print("="*60)
    
    # Group by subdomain
    by_subdomain = defaultdict(list)
    for entry in catalog:
        if entry.get('tier') == '1':
            by_subdomain['O-ISAC'].append(entry)
        else:
            sd = entry.get('subdomain_label', 'General')
            by_subdomain[sd].append(entry)
    
    # For each subdomain, select top N by strength (with locators)
    core_set = []
    for subdomain, target in CORE_TARGETS.items():
        candidates = by_subdomain.get(subdomain, [])
        
        # Filter: must have at least scope_locator
        valid = [c for c in candidates if c.get('scope_locator') or c.get('tier') == '1']
        
        # Sort by strength
        valid.sort(key=lambda x: int(x.get('feeder_strength', 0)), reverse=True)
        
        # Select top N
        selected = valid[:target]
        for s in selected:
            s['is_core'] = 1
        
        core_set.extend(selected)
        print(f"  {subdomain}: {len(selected)}/{target} (from {len(candidates)} candidates)")
    
    # Update is_core in full catalog
    core_ids = {c['paper_id'] for c in core_set}
    for entry in catalog:
        if entry['paper_id'] in core_ids:
            entry['is_core'] = 1
    
    print(f"  Total CORE: {len(core_set)}")
    return catalog, core_set

def write_outputs(catalog, core_set):
    """Write all outputs."""
    print("\n" + "="*60)
    print(f"Writing Outputs to {OUTPUT_DIR}")
    print("="*60)
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Updated catalog
    fields = ['paper_id', 'year', 'title', 'tier', 'subdomain_label', 'modality_coverage',
              'scope_excerpt', 'scope_locator', 'limitations_excerpt', 'limitations_locator',
              'source_path', 'confidence', 'feeder_strength', 'is_core']
    
    with open(OUTPUT_DIR / "ID_related_catalog_v2_3_1.csv", 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        w.writerows(catalog)
    
    # 2. Core feeders
    with open(OUTPUT_DIR / "ID_core_feeders_v2_3_1.csv", 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader()
        w.writerows(core_set)
    
    # 3. Gap summary
    write_gap_summary(catalog, core_set)
    
    # 4. Outline skeleton
    write_outline(catalog, core_set)
    
    # 5. QA report
    write_qa_report(catalog, core_set)
    
    print("  All outputs written")

def write_gap_summary(catalog, core_set):
    """Write gap summary with locator-backed claims."""
    tier1 = [c for c in core_set if c.get('tier') == '1']
    tier2 = [c for c in core_set if c.get('tier') == '2']
    
    # Group Tier-2 by subdomain
    by_sd = defaultdict(list)
    for c in tier2:
        by_sd[c.get('subdomain_label', 'General')].append(c)
    
    lines = [
        "# Section I-D Gap Summary (v2.3.1)",
        f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**CORE Set:** {len(core_set)} papers",
        f"- Tier-1: {len(tier1)}",
        f"- Tier-2: {len(tier2)}",
        "\n---\n",
        "## CORE Papers by Subdomain",
    ]
    
    for sd, papers in sorted(by_sd.items()):
        lines.append(f"\n### {sd} ({len(papers)} papers)")
        for p in papers:
            lines.append(f"- [{p['paper_id']}] {p.get('title', '')[:50]}")
    
    lines.extend([
        "\n---\n",
        "## Evidence-Backed Claims",
        "",
        "### Tier-1 Claims (True O-ISAC)",
        "",
    ])
    
    # Tier-1 claims
    for t in tier1[:2]:
        lines.append(f"**Claim: O-ISAC survey {t['paper_id']} provides state-of-art coverage**")
        if t.get('scope_locator'):
            lines.append(f"- Evidence: \"{t.get('scope_excerpt', '')[:80]}...\"")
            lines.append(f"- Locator: {t.get('scope_locator')}")
        lines.append("")
    
    lines.extend([
        "### Tier-2 Claims (Feeder Surveys)",
        "",
    ])
    
    # VLC claim
    vlc_papers = by_sd.get('VLC_positioning', [])[:3]
    if vlc_papers:
        lines.append("**Claim: VLC positioning surveys exist but lack communication integration**")
        lines.append(f"- Papers: {', '.join([p['paper_id'] for p in vlc_papers])}")
        for p in vlc_papers[:1]:
            if p.get('limitations_locator'):
                lines.append(f"- Evidence: \"{p.get('limitations_excerpt', '')[:80]}...\"")
                lines.append(f"- Locator: {p.get('limitations_locator')}")
        lines.append("")
    
    # DFOS claim
    dfos_papers = by_sd.get('DFOS_DAS', [])[:3]
    if dfos_papers:
        lines.append("**Claim: DFOS/DAS reviews focus on sensing without simultaneous data transmission**")
        lines.append(f"- Papers: {', '.join([p['paper_id'] for p in dfos_papers])}")
        for p in dfos_papers[:1]:
            if p.get('scope_locator'):
                lines.append(f"- Evidence: \"{p.get('scope_excerpt', '')[:80]}...\"")
                lines.append(f"- Locator: {p.get('scope_locator')}")
        lines.append("")
    
    # FSO claim
    fso_papers = by_sd.get('FSO_channel', [])[:3]
    if fso_papers:
        lines.append("**Claim: FSO channel modeling surveys address turbulence but not ISAC integration**")
        lines.append(f"- Papers: {', '.join([p['paper_id'] for p in fso_papers])}")
        for p in fso_papers[:1]:
            if p.get('scope_locator'):
                lines.append(f"- Evidence: \"{p.get('scope_excerpt', '')[:80]}...\"")
                lines.append(f"- Locator: {p.get('scope_locator')}")
        lines.append("")
    
    with open(OUTPUT_DIR / "ID_gap_summary_v2_3_1.md", 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def write_outline(catalog, core_set):
    """Write outline with evidence hooks."""
    tier1 = [c for c in core_set if c.get('tier') == '1']
    tier2 = [c for c in core_set if c.get('tier') == '2']
    
    by_sd = defaultdict(list)
    for c in tier2:
        by_sd[c.get('subdomain_label', 'General')].append(c)
    
    vlc_ids = [p['paper_id'] for p in by_sd.get('VLC_positioning', [])[:4]]
    dfos_ids = [p['paper_id'] for p in by_sd.get('DFOS_DAS', [])[:3]]
    fso_ids = [p['paper_id'] for p in by_sd.get('FSO_channel', [])[:3]]
    opt_ids = [p['paper_id'] for p in by_sd.get('Optical_transmission', [])[:3]]
    tier1_ids = [p['paper_id'] for p in tier1]
    
    lines = [
        "# Section I-D Outline Skeleton (v2.3.1)",
        "\n> CORE set citations with evidence hooks.\n",
        "---\n",
        "## Para 1: RF-ISAC Survey Landscape",
        "- Narrative only (no corpus citations)",
        "- Acknowledge RF-domain surveys, note optical gap",
        "",
        "## Para 2: VLC and Indoor Optical Surveys",
        f"**CORE cite:** {', '.join(vlc_ids)}",
        "",
        "**Evidence hooks:**",
    ]
    
    # Add VLC evidence hooks
    for p in by_sd.get('VLC_positioning', [])[:2]:
        if p.get('scope_locator'):
            lines.append(f"- [{p['paper_id']}] \"{p.get('scope_excerpt', '')[:60]}...\" ({p.get('scope_locator')})")
    
    lines.extend([
        "",
        "## Para 3: Fiber/DFOS and FSO Surveys",
        f"**DFOS cite:** {', '.join(dfos_ids)}",
        f"**FSO cite:** {', '.join(fso_ids)}",
        "",
        "**Evidence hooks:**",
    ])
    
    for p in by_sd.get('DFOS_DAS', [])[:1]:
        if p.get('scope_locator'):
            lines.append(f"- [{p['paper_id']}] \"{p.get('scope_excerpt', '')[:60]}...\" ({p.get('scope_locator')})")
    for p in by_sd.get('FSO_channel', [])[:1]:
        if p.get('scope_locator'):
            lines.append(f"- [{p['paper_id']}] \"{p.get('scope_excerpt', '')[:60]}...\" ({p.get('scope_locator')})")
    
    lines.extend([
        "",
        "## Para 4: True O-ISAC Surveys (Tier-1)",
        f"**CORE cite:** {', '.join(tier1_ids)}",
        "",
        "**Evidence hooks:**",
    ])
    
    for p in tier1:
        if p.get('scope_locator'):
            lines.append(f"- [{p['paper_id']}] \"{p.get('scope_excerpt', '')[:60]}...\" ({p.get('scope_locator')})")
    
    lines.extend([
        "",
        "## Para 5: Gap Synthesis",
        "- Bridge to G1-G7 gaps",
        "- Emphasize G3 (cross-modal) and G7 (systematic methodology)",
        "",
        "## Para 6: Table III Narration",
        "- Open: \"Table III summarizes existing surveys...\"",
        f"- Tier-1: {', '.join(tier1_ids)}",
        "- Highlight 'This Survey' row",
    ])
    
    with open(OUTPUT_DIR / "ID_outline_skeleton_v2_3_1.md", 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def write_qa_report(catalog, core_set):
    """Write QA report."""
    tier2_all = [c for c in catalog if c.get('tier') == '2']
    tier2_core = [c for c in core_set if c.get('tier') == '2']
    
    # Locator compliance
    all_with_loc = sum(1 for c in tier2_all if c.get('scope_locator'))
    core_with_loc = sum(1 for c in tier2_core if c.get('scope_locator'))
    
    # By subdomain
    core_by_sd = defaultdict(int)
    for c in core_set:
        core_by_sd[c.get('subdomain_label', 'Unknown')] += 1
    
    lines = [
        "QA Report v2.3.1",
        "="*40,
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        f"CORE set total: {len(core_set)}",
        f"  - Tier-1: {len([c for c in core_set if c.get('tier') == '1'])}",
        f"  - Tier-2: {len(tier2_core)}",
        "",
        "Tier-2 Locator Compliance:",
        f"  - All Tier-2: {all_with_loc}/{len(tier2_all)} ({all_with_loc/max(len(tier2_all),1)*100:.0f}%)",
        f"  - CORE Tier-2: {core_with_loc}/{len(tier2_core)} ({core_with_loc/max(len(tier2_core),1)*100:.0f}%)",
        "",
        "CORE counts by subdomain:",
    ]
    for sd, cnt in sorted(core_by_sd.items()):
        lines.append(f"  - {sd}: {cnt}")
    
    with open(OUTPUT_DIR / "QA_report_v2_3_1.txt", 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def main():
    print("="*60)
    print("Section I-D Evidence Mining v2.3.1 Repair")
    print(f"Timestamp: {TIMESTAMP}")
    print("="*60)
    
    # Load v2.3 catalog
    print("\nLoading v2.3 catalog...")
    catalog = load_v23_catalog()
    print(f"  Loaded {len(catalog)} papers")
    
    # PASS 1-2: Parse and extract
    catalog = pass1_parse_and_extract(catalog)
    
    # PASS 3: Curate CORE
    catalog, core_set = pass3_curate_core(catalog)
    
    # Write outputs
    write_outputs(catalog, core_set)
    
    print("\n" + "="*60)
    print("COMPLETE")
    print(f"Output: {OUTPUT_DIR}")
    print("="*60)

if __name__ == "__main__":
    main()
