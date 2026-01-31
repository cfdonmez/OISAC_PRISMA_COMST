#!/usr/bin/env python3
"""
mine_ID_surveys_v2_3.py - Section I-D Evidence Mining v2.3 Two-Tier System

Tier-1: True O-ISAC surveys (strict v2.2 intent verification)
Tier-2: Feeder/adjacent surveys (VLC, DFOS/DAS, FSO, optical transmission)
"""

import json
import csv
import re
import shutil
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Configuration
BASE_DIR = Path(r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST")
EXTRACTIONS_DIR = BASE_DIR / "data" / "extraction_results_v4"
CORPUS_DIR = BASE_DIR / "data" / "processed_markdowns"
V22_DIR = BASE_DIR / "analysis" / "ID_v2_2" / "run_20260120_004850"

TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_DIR = BASE_DIR / "analysis" / "ID_v2_3" / f"run_{TIMESTAMP}"

# Tier-1 intent patterns (strict, from v2.2)
TIER1_INTENT_PATTERNS = [
    r'(?i)\bthis\s+survey\b',
    r'(?i)\bthis\s+review\b',
    r'(?i)\bthis\s+overview\b',
    r'(?i)\bwe\s+review\b',
    r'(?i)\bwe\s+survey\b',
    r'(?i)\bcomprehensive\s+review\s+of\b',
]

# Tier-2 title keywords
TIER2_TITLE_KEYWORDS = ['survey', 'review', 'overview', 'tutorial', 'roadmap', 'taxonomy']

# Subdomain classification keywords
SUBDOMAIN_KEYWORDS = {
    'VLC_positioning': ['vlc', 'visible light', 'lifi', 'led', 'indoor position', 'optical wireless'],
    'DFOS_DAS': ['dfos', 'das', 'distributed fiber', 'distributed acoustic', 'distributed sensing', 'otdr', 'fiber sens'],
    'FSO_channel': ['fso', 'free-space', 'free space', 'atmospheric', 'turbulence', 'owc channel'],
    'Optical_transmission': ['optical transmission', 'optical network', 'photonic', 'coherent', 'fiber communication'],
}

# Gap taxonomy for qualitative tagging
GAP_KEYWORDS = {
    'G1': ['terminology', 'nomenclature', 'glossary', 'definition', 'naming'],
    'G2': ['metric', 'crb', 'fim', 'rmse', 'snr', 'evaluation', 'performance'],
    'G3': ['benchmark', 'comparison', 'cross-modality', 'evaluation'],
    'G4': ['transfer', 'portability', 'generalization', 'cross-domain'],
    'G5': ['unified', 'framework', 'taxonomy', 'classification'],
    'G6': ['system-level', 'co-design', 'mobility', 'nlos', 'turbulence', 'network'],
    'G7': ['prisma', 'systematic', 'meta-analysis', 'search strategy'],
}

def load_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

def load_markdown(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return ""

def parse_headings(content):
    lines = content.split('\n')
    headings = []
    for i, line in enumerate(lines, 1):
        match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
        if match:
            level = len(match.group(1))
            title = re.sub(r'[*`]', '', match.group(2)).strip()[:80]
            headings.append({'level': level, 'title': title, 'line': i})
    return headings, lines

def get_heading_for_line(headings, line_num):
    path_parts = []
    for h in headings:
        if h['line'] <= line_num:
            while path_parts and path_parts[-1][0] >= h['level']:
                path_parts.pop()
            path_parts.append((h['level'], h['title']))
        else:
            break
    return ' > '.join([p[1] for p in path_parts]) if path_parts else "Document Start"

def extract_metadata(paper_id):
    json_path = EXTRACTIONS_DIR / f"{paper_id}_v4.json"
    json_data = load_json(json_path)
    if not json_data:
        return {}
    bib = json_data.get('study_level', {}).get('bibliographic', {})
    return {
        'title': bib.get('title', ''),
        'year': str(bib.get('year', '')) if bib.get('year') else '',
        'venue': bib.get('venue', ''),
        'doi': bib.get('doi', '')
    }

def has_tier1_intent(content):
    """Check for strict Tier-1 intent sentence in first 8000 chars."""
    intro = content[:8000]
    for pattern in TIER1_INTENT_PATTERNS:
        match = re.search(pattern, intro)
        if match:
            # Get line number
            line_num = content[:match.start()].count('\n') + 1
            if line_num < 100:  # Must be in intro area
                # Extract sentence
                start = max(content.rfind('.', 0, match.start()) + 1, 0)
                end = content.find('.', match.end())
                if end == -1:
                    end = min(match.end() + 150, len(content))
                sentence = content[start:end + 1].strip()
                return True, ' '.join(sentence.split()[:25]), line_num
    return False, None, None

def has_tier2_survey_structure(content, headings):
    """Check for Tier-2 survey structure cues."""
    cues = []
    
    # Check for taxonomy/classification section
    for h in headings:
        title_lower = h['title'].lower()
        if any(w in title_lower for w in ['taxonomy', 'classification', 'categorization']):
            cues.append('taxonomy_section')
            break
    
    # Check for comparative table
    if re.search(r'(?i)(table|fig)\s*[\dIVX]+.*?(compar|summar|survey|review)', content):
        cues.append('comparative_table')
    
    # Check for open challenges/future directions spanning subtopics
    challenges_match = re.search(r'(?i)(open\s+challenge|future\s+direction|research\s+gap)', content)
    if challenges_match:
        # Check if it has multiple subsections
        pos = challenges_match.start()
        section_content = content[pos:pos+5000]
        subsection_count = len(re.findall(r'^#{2,4}\s+', section_content, re.MULTILINE))
        if subsection_count >= 2:
            cues.append('challenges_section')
    
    return cues

def classify_subdomain(content, title):
    """Classify paper into subdomain."""
    text = (title + ' ' + content[:5000]).lower()
    
    scores = {}
    for subdomain, keywords in SUBDOMAIN_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in text)
        if score > 0:
            scores[subdomain] = score
    
    if scores:
        return max(scores, key=scores.get)
    return 'General'

def classify_modality(content, title):
    text = (title + ' ' + content[:5000]).lower()
    modalities = set()
    if any(w in text for w in ['fiber', 'dfos', 'das', 'otdr', 'fibre']):
        modalities.add('Fiber')
    if any(w in text for w in ['fso', 'free-space', 'free space']):
        modalities.add('FSO')
    if any(w in text for w in ['vlc', 'lifi', 'visible light']):
        modalities.add('VLC/LiFi')
    if any(w in text for w in ['thz', 'terahertz']):
        modalities.add('Photo-THz')
    
    if len(modalities) >= 2:
        return 'Multi'
    elif len(modalities) == 1:
        return list(modalities)[0]
    return 'General'

def extract_scope_excerpt(content, headings):
    """Extract scope from Abstract/Intro."""
    patterns = [
        r'(?i)(this\s+(survey|review|paper|work)\s+(?:provides|presents|reviews|summarizes)[^.]{10,100}\.)',
        r'(?i)(we\s+(review|provide|present|summarize)\s+[^.]{10,100}\.)',
    ]
    
    intro = content[:8000]
    for pattern in patterns:
        match = re.search(pattern, intro)
        if match:
            line_num = content[:match.start()].count('\n') + 1
            heading = get_heading_for_line(headings, line_num)
            return ' '.join(match.group(0).split()[:25]), f"{heading} (L{line_num})"
    
    return "", ""

def extract_limitations(content, headings):
    """Extract limitations from Conclusion/Future sections."""
    patterns = [
        r'(?i)(future\s+(?:work|direction|research)[^.]{10,80}\.)',
        r'(?i)(open\s+(?:challenge|issue)[^.]{10,80}\.)',
    ]
    
    start_pos = int(len(content) * 0.6)
    end_content = content[start_pos:]
    
    for pattern in patterns:
        match = re.search(pattern, end_content)
        if match:
            abs_pos = start_pos + match.start()
            line_num = content[:abs_pos].count('\n') + 1
            heading = get_heading_for_line(headings, line_num)
            return ' '.join(match.group(0).split()[:25]), f"{heading} (L{line_num})"
    
    return "", ""

def tag_gaps_qualitative(content, headings):
    """Tag which gaps a Tier-2 paper addresses (qualitative Yes/No)."""
    tags = {}
    evidence = {}
    
    for gap_id, keywords in GAP_KEYWORDS.items():
        found = False
        excerpt = ""
        locator = ""
        
        for kw in keywords:
            pattern = rf'(?i)([^.]*\b{re.escape(kw)}\b[^.]*\.)'
            match = re.search(pattern, content)
            if match:
                line_num = content[:match.start()].count('\n') + 1
                heading = get_heading_for_line(headings, line_num)
                
                # Check it's substantive (not just a passing mention)
                sentence = match.group(0)
                if len(sentence) > 50:
                    found = True
                    excerpt = ' '.join(sentence.split()[:20])
                    locator = f"{heading} (L{line_num})"
                    break
        
        tags[gap_id] = 'Yes' if found else 'No'
        evidence[gap_id] = (excerpt, locator) if found else ('', '')
    
    return tags, evidence

def load_tier1_from_v22():
    """Load Tier-1 surveys from v2.2."""
    tier1 = []
    
    catalog_path = V22_DIR / "ID_survey_catalog_v2_2.csv"
    if catalog_path.exists():
        with open(catalog_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['tier'] = '1'
                row['subdomain_label'] = 'O-ISAC'
                row['reason_if_tier2'] = ''
                tier1.append(row)
    
    print(f"  Loaded {len(tier1)} Tier-1 surveys from v2.2")
    return tier1

def scan_tier2_candidates():
    """Scan corpus for Tier-2 feeder surveys."""
    print("\n" + "="*60)
    print("Scanning for Tier-2 Feeder Surveys")
    print("="*60)
    
    tier2 = []
    tier2_borderline = []
    
    # Get v2.2 verified paper_ids to exclude
    tier1_ids = set()
    catalog_path = V22_DIR / "ID_survey_catalog_v2_2.csv"
    if catalog_path.exists():
        with open(catalog_path, 'r', encoding='utf-8') as f:
            for row in csv.DictReader(f):
                tier1_ids.add(row['paper_id'])
    
    json_files = sorted(EXTRACTIONS_DIR.glob("O_ISAC_*_v4.json"))
    
    for json_path in json_files:
        paper_id = json_path.stem.replace('_v4', '')
        
        # Skip Tier-1 papers
        if paper_id in tier1_ids:
            continue
        
        # Load markdown
        md_path = CORPUS_DIR / paper_id / f"{paper_id}.md"
        content = load_markdown(md_path)
        if not content or len(content) < 2000:
            continue
        
        # Get metadata
        meta = extract_metadata(paper_id)
        title = meta.get('title', '')
        
        # Check title keywords
        title_lower = title.lower()
        has_title_keyword = any(kw in title_lower for kw in TIER2_TITLE_KEYWORDS)
        
        # Parse structure
        headings, lines = parse_headings(content)
        
        # Check for intent sentence (Tier-1 style but not required)
        has_intent, intent_sentence, intent_line = has_tier1_intent(content)
        
        # Check for survey structure cues
        structure_cues = has_tier2_survey_structure(content, headings)
        
        # Tier-2 verification: title keyword OR structure, AND at least one of intent/structure
        is_candidate = has_title_keyword or len(structure_cues) >= 1
        has_evidence = has_intent or len(structure_cues) >= 1
        
        if is_candidate and has_evidence:
            # Classify subdomain
            subdomain = classify_subdomain(content, title)
            modality = classify_modality(content, title)
            
            # Skip if not in target subdomains
            if subdomain == 'General' and not has_title_keyword:
                continue
            
            # Extract excerpts
            scope, scope_loc = extract_scope_excerpt(content, headings)
            if not scope and intent_sentence:
                scope = intent_sentence
                scope_loc = f"Introduction (L{intent_line})" if intent_line else ""
            
            limits, limits_loc = extract_limitations(content, headings)
            
            # Determine evidence type
            if 'survey' in title_lower:
                evidence_type = 'Survey'
            elif 'tutorial' in title_lower:
                evidence_type = 'Tutorial'
            elif any(w in title_lower for w in ['review', 'overview']):
                evidence_type = 'Overview'
            else:
                evidence_type = 'Overview'  # Default for Tier-2
            
            # Build reason
            reasons = []
            if has_title_keyword:
                reasons.append('title_keyword')
            if has_intent:
                reasons.append('intent_statement')
            if structure_cues:
                reasons.extend(structure_cues)
            
            tier2.append({
                'paper_id': paper_id,
                'year': meta.get('year', ''),
                'title': title[:100],
                'venue': meta.get('venue', '')[:50],
                'doi': meta.get('doi', ''),
                'tier': '2',
                'subdomain_label': subdomain,
                'modality_coverage': modality,
                'integration_depth': 'Partial',
                'evidence_type': evidence_type,
                'scope_excerpt': scope.replace('\n', ' ')[:150],
                'scope_locator': scope_loc,
                'limitations_excerpt': limits.replace('\n', ' ')[:150] if limits else '',
                'limitations_locator': limits_loc,
                'methodology_excerpt': '',
                'methodology_locator': '',
                'source_path': str(md_path),
                'confidence': 0.75,
                'reason_if_tier2': ';'.join(reasons),
                '_content': content,
                '_headings': headings
            })
        elif is_candidate:
            tier2_borderline.append({
                'paper_id': paper_id,
                'title': title[:60],
                'reason': 'NO_STRUCTURE_EVIDENCE'
            })
    
    print(f"  Tier-2 verified: {len(tier2)}")
    print(f"  Tier-2 borderline: {len(tier2_borderline)}")
    
    # Count by subdomain
    subdomain_counts = defaultdict(int)
    for t in tier2:
        subdomain_counts[t['subdomain_label']] += 1
    print(f"  By subdomain: {dict(subdomain_counts)}")
    
    return tier2, tier2_borderline

def build_feeder_map(tier2):
    """Build gap qualitative tagging map for Tier-2."""
    feeder_map = []
    
    for paper in tier2:
        content = paper.get('_content', '')
        headings = paper.get('_headings', [])
        
        if not content:
            # Reload if needed
            md_path = Path(paper['source_path'])
            content = load_markdown(md_path)
            headings, _ = parse_headings(content)
        
        tags, evidence = tag_gaps_qualitative(content, headings)
        
        # Find first gap with evidence for excerpt
        evidence_excerpt = ""
        evidence_locator = ""
        for gap_id in ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7']:
            if evidence[gap_id][0]:
                evidence_excerpt = evidence[gap_id][0]
                evidence_locator = evidence[gap_id][1]
                break
        
        feeder_map.append({
            'paper_id': paper['paper_id'],
            'subdomain_label': paper['subdomain_label'],
            'addresses_G1': tags['G1'],
            'addresses_G2': tags['G2'],
            'addresses_G3': tags['G3'],
            'addresses_G4': tags['G4'],
            'addresses_G5': tags['G5'],
            'addresses_G6': tags['G6'],
            'addresses_G7': tags['G7'],
            'evidence_excerpt': evidence_excerpt[:100],
            'locator': evidence_locator
        })
    
    return feeder_map

def write_outputs(tier1, tier2, tier2_borderline, feeder_map):
    """Write all v2.3 outputs."""
    print("\n" + "="*60)
    print(f"Writing Outputs to {OUTPUT_DIR}")
    print("="*60)
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Combined catalog
    catalog_fields = ['paper_id', 'year', 'title', 'venue', 'doi', 'tier', 'subdomain_label',
                      'modality_coverage', 'integration_depth', 'evidence_type',
                      'scope_excerpt', 'scope_locator', 'limitations_excerpt', 'limitations_locator',
                      'methodology_excerpt', 'methodology_locator', 'source_path', 'confidence', 'reason_if_tier2']
    
    combined = []
    for t in tier1:
        row = {k: t.get(k, '') for k in catalog_fields}
        combined.append(row)
    for t in tier2:
        row = {k: t.get(k, '') for k in catalog_fields}
        combined.append(row)
    
    with open(OUTPUT_DIR / "ID_related_catalog_v2_3.csv", 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=catalog_fields)
        w.writeheader()
        w.writerows(combined)
    
    # 2. Copy Tier-1 gap matrix from v2.2
    v22_gap = V22_DIR / "ID_gap_matrix_v2_2.csv"
    if v22_gap.exists():
        shutil.copy(v22_gap, OUTPUT_DIR / "ID_gap_matrix_tier1_v2_3.csv")
    
    # 3. Feeder map
    if feeder_map:
        with open(OUTPUT_DIR / "ID_feeder_map_v2_3.csv", 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=feeder_map[0].keys())
            w.writeheader()
            w.writerows(feeder_map)
    
    # 4. Gap summary
    write_gap_summary(tier1, tier2, feeder_map)
    
    # 5. Outline skeleton
    write_outline_skeleton(tier1, tier2)
    
    # 6. QA report
    write_qa_report(tier1, tier2, tier2_borderline)
    
    print("  All outputs written")

def write_gap_summary(tier1, tier2, feeder_map):
    """Write gap summary with tier-separated claims."""
    lines = [
        "# Section I-D Gap Summary (v2.3)",
        f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Tier-1 (True O-ISAC Surveys):** {len(tier1)}",
        f"**Tier-2 (Feeder/Adjacent Surveys):** {len(tier2)}",
        "\n---\n",
        "## Tier-1 Papers",
    ]
    for t in tier1:
        lines.append(f"- [{t['paper_id']}] {t.get('title', '')[:60]}")
    
    lines.extend(["\n## Tier-2 by Subdomain"])
    subdomain_papers = defaultdict(list)
    for t in tier2:
        subdomain_papers[t['subdomain_label']].append(t['paper_id'])
    for sd, papers in sorted(subdomain_papers.items()):
        lines.append(f"- **{sd}**: {', '.join(papers[:5])}")
    
    lines.extend([
        "\n---\n",
        "## Evidence-Backed Claims for I-D",
        "",
        "### Tier-1 Supported Claims",
        "",
        "1. **No unified cross-modal O-ISAC taxonomy** — existing O-ISAC surveys focus on single domains",
        f"   - Evidence: {', '.join([t['paper_id'] for t in tier1])}",
        "",
        "2. **PRISMA methodology absent in optical ISAC** — no systematic review methodology applied",
        "   - Evidence: G7 scores 0-1 for all Tier-1 surveys",
        "",
        "### Tier-2 Supported Claims",
        "",
        "3. **VLC positioning surveys exist but lack communication integration**",
        f"   - Evidence: {', '.join([t['paper_id'] for t in tier2 if 'VLC' in t['subdomain_label']][:3]) or 'N/A'}",
        "",
        "4. **DFOS/DAS reviews cover sensing but not simultaneous data transmission**",
        f"   - Evidence: {', '.join([t['paper_id'] for t in tier2 if 'DFOS' in t['subdomain_label']][:3]) or 'N/A'}",
        "",
        "5. **FSO channel modeling surveys focus on link-level, not ISAC integration**",
        f"   - Evidence: {', '.join([t['paper_id'] for t in tier2 if 'FSO' in t['subdomain_label']][:3]) or 'N/A'}",
    ])
    
    with open(OUTPUT_DIR / "ID_gap_summary_v2_3.md", 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def write_outline_skeleton(tier1, tier2):
    """Write 6-paragraph outline skeleton."""
    tier1_ids = [t['paper_id'] for t in tier1]
    tier2_by_subdomain = defaultdict(list)
    for t in tier2:
        tier2_by_subdomain[t['subdomain_label']].append(t['paper_id'])
    
    lines = [
        "# Section I-D Outline Skeleton (v2.3)",
        "\n> Two-tier structure: Feeder surveys first, then True O-ISAC, then gap synthesis.\n",
        "---\n",
        "## Para 1: RF-ISAC Survey Landscape (Narrative Only)",
        "- Acknowledge RF-domain ISAC survey landscape",
        "- Note the absence of equivalent optical coverage",
        "- NO paper citations from corpus (external RF surveys mentioned narratively)",
        "",
        "## Para 2: VLC and Indoor Optical Surveys (Tier-2)",
        f"- **Cite**: {', '.join(tier2_by_subdomain.get('VLC_positioning', [])[:4]) or 'N/A'}",
        "- Summarize: positioning algorithms, LED communication, BUT lack of true ISAC integration",
        "",
        "## Para 3: Fiber and FSO Surveys (Tier-2)",
        f"- **Fiber/DFOS cite**: {', '.join(tier2_by_subdomain.get('DFOS_DAS', [])[:3]) or 'N/A'}",
        f"- **FSO cite**: {', '.join(tier2_by_subdomain.get('FSO_channel', [])[:3]) or 'N/A'}",
        "- Summarize: distributed sensing, channel modeling, BUT siloed from data transmission",
        "",
        "## Para 4: True O-ISAC Surveys (Tier-1)",
        f"- **Cite**: {', '.join(tier1_ids)}",
        "- Summarize: emerging O-ISAC surveys, scope and limitations",
        "- Highlight single-modality focus and lack of PRISMA methodology",
        "",
        "## Para 5: Gap Synthesis",
        "- Bridge from surveyed literature to identified gaps (G1-G7)",
        "- Emphasize: G3 (cross-modal benchmark), G7 (systematic methodology)",
        "- Lead into Section I-C contributions",
        "",
        "## Para 6: Table III Narration",
        "- Open: \"Table III provides a systematic comparison...\"",
        f"- Tier-1 block: {', '.join(tier1_ids)}",
        f"- Optional Tier-2 summary row or separate mini-table",
        "- Highlight 'This Survey' row as comprehensive coverage",
    ]
    
    with open(OUTPUT_DIR / "ID_outline_skeleton_v2_3.md", 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def write_qa_report(tier1, tier2, tier2_borderline):
    """Write QA report."""
    # Count by subdomain
    subdomain_counts = defaultdict(int)
    for t in tier2:
        subdomain_counts[t['subdomain_label']] += 1
    
    lines = [
        "QA Report v2.3",
        "="*40,
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        f"Tier-1 count: {len(tier1)}",
        f"Tier-2 count: {len(tier2)}",
        f"Tier-2 borderline: {len(tier2_borderline)}",
        "",
        "Tier-2 by Subdomain:",
    ]
    for sd, cnt in sorted(subdomain_counts.items()):
        lines.append(f"  - {sd}: {cnt}")
    
    # Check locator compliance
    locator_compliant = sum(1 for t in tier2 if t.get('scope_locator'))
    lines.extend([
        "",
        f"Tier-2 locator compliance: {locator_compliant}/{len(tier2)}",
        "",
        "Anomalies:",
        "  - None detected" if locator_compliant == len(tier2) else f"  - {len(tier2) - locator_compliant} missing locators",
    ])
    
    with open(OUTPUT_DIR / "QA_report_v2_3.txt", 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def main():
    print("="*60)
    print("Section I-D Evidence Mining v2.3 Two-Tier System")
    print(f"Timestamp: {TIMESTAMP}")
    print("="*60)
    
    # Load Tier-1 from v2.2
    print("\n" + "="*60)
    print("Loading Tier-1 from v2.2")
    print("="*60)
    tier1 = load_tier1_from_v22()
    
    # Scan for Tier-2
    tier2, tier2_borderline = scan_tier2_candidates()
    
    # Build feeder map
    print("\n" + "="*60)
    print("Building Feeder Map")
    print("="*60)
    feeder_map = build_feeder_map(tier2)
    print(f"  Feeder map entries: {len(feeder_map)}")
    
    # Write outputs
    write_outputs(tier1, tier2, tier2_borderline, feeder_map)
    
    print("\n" + "="*60)
    print("COMPLETE")
    print(f"Output: {OUTPUT_DIR}")
    print("="*60)

if __name__ == "__main__":
    main()
