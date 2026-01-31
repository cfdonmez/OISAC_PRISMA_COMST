#!/usr/bin/env python3
"""
Evidence Gold Set v3.2 - COMST-grade distillation
Validates C3, applies authority scoring, produces 50-80 gold items for I-C
"""
import os
import csv
import re
import glob
from collections import Counter, defaultdict

# --- Configuration ---
CORPUS_DIR = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns"
EXTRACTIONS_DIR = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\extraction_results_v4"
OUTPUT_DIR = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\analysis"
EVIDENCE_V3_1 = os.path.join(OUTPUT_DIR, "IC_evidence_claims_v3_1.csv")
CONFLICTS_V3_1 = os.path.join(OUTPUT_DIR, "IC_term_metric_conflicts_v3_1.csv")

# --- C3 Strict Cue Words ---
C3_CUES = [
    r"fragmentation", r"fragmented", r"silo", r"siloed", r"disparate",
    r"scattered\s+literature", r"hard\s+to\s+compare", r"not\s+directly\s+comparable",
    r"lack\s+of\s+unified\s+benchmark", r"no\s+benchmark", r"standardization\s+needed",
    r"taxonomy\s+needed", r"lack\s+of\s+unified\s+framework", r"interoperability\s+lacking",
    r"separated?\s+communities", r"comprehensive\s+survey\s+lacking",
    r"independently\s+developed", r"heterogeneous", r"cross[-\s]?domain\s+gap",
    r"limited\s+cross", r"lack\s+of\s+common", r"no\s+common", r"separately",
    r"different\s+paradigms", r"isolated", r"without\s+unified", r"no\s+unified",
]

# I-C Anchor Terms for relevance scoring
IC_ANCHORS = [
    r"fragmentation", r"terminology", r"metrics?", r"transfer", r"unified\s+framework",
    r"benchmark", r"taxonomy", r"standardization", r"inconsistent", r"silo",
    r"aliasing", r"nomenclature", r"cross[-\s]?domain", r"interoperability",
]

# Authority keywords
OVERVIEW_KEYWORDS = [r"\boverview\b", r"\broadmap\b", r"\binvited\b", r"\bperspective\b", 
                     r"\bvision\b", r"\bchallenges\s+and\s+future\b", r"\bfuture\s+directions\b",
                     r"\bstate[-\s]of[-\s]the[-\s]art\b"]

# --- Helper Functions ---

def sanitize_html(text):
    """Remove HTML/XML tags and normalize whitespace."""
    if not text:
        return ""
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def truncate_excerpt(text, max_words=22):
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]) + "..."

def has_c3_cue(text):
    """Check if text contains any strict C3 cue word."""
    text_lower = text.lower()
    for cue in C3_CUES:
        if re.search(cue, text_lower, re.IGNORECASE):
            return True
    return False

def compute_relevance_score(row):
    """Compute I-C relevance based on anchor term overlap."""
    text = (row.get("supporting_excerpt", "") + " " + 
            row.get("why_it_supports", "") + " " + 
            row.get("cross_domain_note", "")).lower()
    
    matches = 0
    for anchor in IC_ANCHORS:
        if re.search(anchor, text, re.IGNORECASE):
            matches += 1
    
    return min(1.0, matches / 5.0)  # 5+ anchors = 1.0

def classify_authority(row):
    """Classify authority_class and compute authority_score."""
    etype = row.get("evidence_type", "").lower()
    title = row.get("title", "").lower()
    excerpt = row.get("supporting_excerpt", "").lower()
    
    # Determine authority_class
    if etype == "standard":
        auth_class = "Standard"
        base_score = 1.0
    elif etype == "survey":
        auth_class = "Survey"
        base_score = 0.9
    elif etype == "tutorial":
        auth_class = "Tutorial"
        base_score = 0.85
    else:
        # Check for overview-like papers
        is_overview = False
        for pat in OVERVIEW_KEYWORDS:
            if re.search(pat, title) or re.search(pat, excerpt):
                is_overview = True
                break
        
        if is_overview:
            auth_class = "Overview"
            base_score = 0.85
        else:
            auth_class = "Research"
            base_score = 0.6
    
    # Explicitness bonus
    explicitness_bonus = 0
    if re.search(r"\bneed\b|\black\b|\bfragment|\bnot\s+comparable|\bstandardization\b", excerpt):
        explicitness_bonus = 0.2
    
    authority_score = min(1.0, base_score + explicitness_bonus)
    
    return auth_class, authority_score

def get_subpoint_tag(row):
    """Assign subpoint_tag based on claim and content."""
    claim = row.get("claim_id", "")
    excerpt = row.get("supporting_excerpt", "").lower()
    terms = row.get("terminology_terms", "").lower()
    metrics = row.get("metric_terms", "").lower()
    
    if claim == "C1":
        if "alias" in excerpt or "also known" in excerpt:
            return "aliasing"
        elif "ambiguous" in excerpt:
            return "ambiguous naming"
        else:
            return "inconsistent labels"
    elif claim == "C2":
        if "rmse" in metrics or "crb" in metrics or "fim" in metrics:
            return "bounds(CRB/FIM)"
        elif "resolution" in metrics:
            return "resolution-vs-RMSE"
        elif "snr" in metrics or "osnr" in metrics:
            return "SNR-OSNR mismatch"
        else:
            return "reporting format"
    elif claim == "C3":
        if "silo" in excerpt:
            return "siloing"
        elif "benchmark" in excerpt:
            return "lack-of-benchmark"
        elif "standard" in excerpt:
            return "standardization-needed"
        else:
            return "non-comparability"
    elif claim == "C4":
        if "transfer" in excerpt:
            return "missing transfer"
        elif "interoperability" in excerpt:
            return "interoperability gap"
        else:
            return "cross-modality mismatch"
    elif claim == "C5":
        if "taxonomy" in excerpt:
            return "taxonomy need"
        elif "benchmark" in excerpt:
            return "benchmark suite need"
        else:
            return "unified PHY need"
    return "general"


def main():
    print("=" * 60)
    print("Evidence Gold Set v3.2 Distillation")
    print("=" * 60)
    
    # --- Load v3.1 evidence ---
    evidence = []
    with open(EVIDENCE_V3_1, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for key in row:
                if isinstance(row[key], str):
                    row[key] = sanitize_html(row[key])
            evidence.append(row)
    
    print(f"Loaded {len(evidence)} evidence items from v3.1")
    
    # --- C3 Validation and Audit ---
    c3_audit = []
    valid_evidence = []
    c3_dropped = 0
    c3_relabeled = 0
    
    for row in evidence:
        if row.get("claim_id") == "C3":
            old_excerpt = row.get("supporting_excerpt", "")
            has_cue = has_c3_cue(old_excerpt)
            
            audit_entry = {
                "paper_id": row.get("paper_id", ""),
                "old_excerpt": old_excerpt[:100],
                "new_excerpt": "",
                "kept_or_dropped": "",
                "new_claim_if_relabelled": "",
                "reason": "",
                "source_locator": row.get("source_locator", "")
            }
            
            if has_cue:
                # Valid C3, keep it
                row["supporting_excerpt"] = truncate_excerpt(old_excerpt, 22)
                audit_entry["new_excerpt"] = row["supporting_excerpt"]
                audit_entry["kept_or_dropped"] = "KEPT"
                audit_entry["reason"] = "Contains valid C3 cue word"
                valid_evidence.append(row)
            else:
                # Check if it fits another claim
                excerpt_lower = old_excerpt.lower()
                
                if "independently" in excerpt_lower or "separately" in excerpt_lower:
                    # This could still be C3-adjacent, check for heterogeneous
                    if "heterogeneous" in excerpt_lower or "gap" in excerpt_lower:
                        row["supporting_excerpt"] = truncate_excerpt(old_excerpt, 22)
                        audit_entry["new_excerpt"] = row["supporting_excerpt"]
                        audit_entry["kept_or_dropped"] = "KEPT"
                        audit_entry["reason"] = "Contains implicit fragmentation cue (independently/heterogeneous)"
                        valid_evidence.append(row)
                    else:
                        # Relabel to C4 (transfer gap) or drop
                        if "transfer" in excerpt_lower or "cross" in excerpt_lower:
                            row["claim_id"] = "C4"
                            row["claim_short"] = "Cross-domain gap (relabeled)"
                            row["supporting_excerpt"] = truncate_excerpt(old_excerpt, 22)
                            audit_entry["new_excerpt"] = row["supporting_excerpt"]
                            audit_entry["kept_or_dropped"] = "RELABELED"
                            audit_entry["new_claim_if_relabelled"] = "C4"
                            audit_entry["reason"] = "No explicit C3 cue, relabeled to C4"
                            valid_evidence.append(row)
                            c3_relabeled += 1
                        else:
                            audit_entry["kept_or_dropped"] = "DROPPED"
                            audit_entry["reason"] = "No valid C3 cue, not suitable for relabeling"
                            c3_dropped += 1
                else:
                    # Check for other potential claims
                    if "metric" in excerpt_lower or "snr" in excerpt_lower or "rmse" in excerpt_lower:
                        row["claim_id"] = "C2"
                        row["claim_short"] = "Metric usage (relabeled)"
                        row["supporting_excerpt"] = truncate_excerpt(old_excerpt, 22)
                        audit_entry["new_excerpt"] = row["supporting_excerpt"]
                        audit_entry["kept_or_dropped"] = "RELABELED"
                        audit_entry["new_claim_if_relabelled"] = "C2"
                        audit_entry["reason"] = "Contains metric-related content"
                        valid_evidence.append(row)
                        c3_relabeled += 1
                    elif "framework" in excerpt_lower or "benchmark" in excerpt_lower:
                        row["claim_id"] = "C5"
                        row["claim_short"] = "Framework need (relabeled)"
                        row["supporting_excerpt"] = truncate_excerpt(old_excerpt, 22)
                        audit_entry["new_excerpt"] = row["supporting_excerpt"]
                        audit_entry["kept_or_dropped"] = "RELABELED"
                        audit_entry["new_claim_if_relabelled"] = "C5"
                        audit_entry["reason"] = "Contains framework/benchmark content"
                        valid_evidence.append(row)
                        c3_relabeled += 1
                    else:
                        audit_entry["kept_or_dropped"] = "DROPPED"
                        audit_entry["reason"] = "No valid C3 cue, no suitable relabel target"
                        c3_dropped += 1
            
            c3_audit.append(audit_entry)
        else:
            # Non-C3 items: just truncate excerpt
            row["supporting_excerpt"] = truncate_excerpt(row.get("supporting_excerpt", ""), 22)
            valid_evidence.append(row)
    
    print(f"\nC3 Audit: {c3_dropped} dropped, {c3_relabeled} relabeled, {len([a for a in c3_audit if a['kept_or_dropped']=='KEPT'])} kept")
    
    # --- Apply authority classification and scoring ---
    for row in valid_evidence:
        auth_class, auth_score = classify_authority(row)
        row["authority_class"] = auth_class
        row["authority_score"] = auth_score
        row["relevance_score"] = compute_relevance_score(row)
        row["subpoint_tag"] = get_subpoint_tag(row)
    
    # --- Build Gold Set ---
    # Sort by combined score
    for row in valid_evidence:
        row["combined_score"] = float(row["authority_score"]) + float(row["relevance_score"])
    
    valid_evidence.sort(key=lambda x: x["combined_score"], reverse=True)
    
    # Select gold set with constraints
    gold_set = []
    claim_counts = Counter()
    mod_counts = Counter()
    auth_counts = Counter()
    paper_claim_seen = set()
    
    # First pass: ensure minimum per claim
    for claim in ["C1", "C2", "C3", "C4", "C5"]:
        claim_items = [r for r in valid_evidence if r["claim_id"] == claim]
        for row in claim_items:
            key = (row["paper_id"], row["claim_id"])
            if key not in paper_claim_seen:
                if claim_counts[claim] < 12:  # Target 10-12 per claim
                    paper_claim_seen.add(key)
                    gold_set.append(row)
                    claim_counts[claim] += 1
                    mod_counts[row.get("modality", "Other")] += 1
                    auth_counts[row.get("authority_class", "Research")] += 1
    
    # Second pass: fill to 50-80 with highest combined scores
    for row in valid_evidence:
        if len(gold_set) >= 75:
            break
        key = (row["paper_id"], row["claim_id"])
        if key not in paper_claim_seen:
            # Check modality balance
            modality = row.get("modality", "Other")
            if mod_counts[modality] / max(len(gold_set), 1) < 0.40:
                paper_claim_seen.add(key)
                gold_set.append(row)
                claim_counts[row["claim_id"]] += 1
                mod_counts[modality] += 1
                auth_counts[row.get("authority_class", "Research")] += 1
    
    print(f"\nGold set size: {len(gold_set)}")
    print(f"Claim distribution: {dict(claim_counts)}")
    print(f"Authority distribution: {dict(auth_counts)}")
    print(f"Modality distribution: {dict(mod_counts)}")
    
    # --- Write Gold Set CSV ---
    gold_path = os.path.join(OUTPUT_DIR, "IC_evidence_gold_v3_2.csv")
    gold_headers = [
        "claim_id", "subpoint_tag", "paper_id", "year", "title", "venue", "doi",
        "modality", "evidence_type", "authority_class", "authority_score", "relevance_score",
        "where_in_paper", "supporting_excerpt", "why_it_supports", "metric_terms",
        "terminology_terms", "cross_domain_note", "confidence", "source_path", "source_locator"
    ]
    
    with open(gold_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=gold_headers, quoting=csv.QUOTE_ALL, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(gold_set)
    
    print(f"Wrote {len(gold_set)} gold items to {gold_path}")
    
    # --- Write C3 Audit ---
    audit_path = os.path.join(OUTPUT_DIR, "IC_C3_audit_v3_2.csv")
    audit_headers = ["paper_id", "old_excerpt", "new_excerpt", "kept_or_dropped", 
                     "new_claim_if_relabelled", "reason", "source_locator"]
    
    with open(audit_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=audit_headers, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(c3_audit)
    
    print(f"Wrote {len(c3_audit)} C3 audit entries to {audit_path}")
    
    # --- Load and select conflicts ---
    conflicts = []
    with open(CONFLICTS_V3_1, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for key in row:
                if isinstance(row[key], str):
                    row[key] = sanitize_html(row[key])
            conflicts.append(row)
    
    # Rank conflicts by authority + relevance
    for c in conflicts:
        # Compute simple relevance for conflicts
        text = (c.get("concept", "") + " " + c.get("analysis", "")).lower()
        relevance = 0
        for anchor in IC_ANCHORS:
            if re.search(anchor, text):
                relevance += 0.2
        relevance = min(1.0, relevance)
        c["relevance_score"] = relevance
        c["combined_score"] = float(c.get("confidence", 0.8)) + relevance
    
    conflicts.sort(key=lambda x: x["combined_score"], reverse=True)
    gold_conflicts = conflicts[:20]
    
    conflicts_path = os.path.join(OUTPUT_DIR, "IC_conflicts_gold_v3_2.csv")
    with open(conflicts_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(gold_conflicts[0].keys()) if gold_conflicts else [], 
                                quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(gold_conflicts)
    
    print(f"Wrote {len(gold_conflicts)} gold conflicts to {conflicts_path}")
    
    # --- Generate I-C Skeleton ---
    skeleton_path = os.path.join(OUTPUT_DIR, "IC_I-C_skeleton_v3_2.md")
    
    with open(skeleton_path, 'w', encoding='utf-8') as f:
        f.write("# Section I-C: The Fragmentation Challenge (Writing Skeleton)\n\n")
        f.write("*Generated from gold evidence set v3.2*\n\n")
        
        # C1 paragraph
        c1_items = [r for r in gold_set if r["claim_id"] == "C1"][:5]
        f.write("## C1: Terminology Inconsistency\n\n")
        f.write("The O-ISAC field suffers from inconsistent terminology, with terms such as ")
        f.write("\"optical ISAC,\" \"photonic ISAC,\" \"O-ISAC,\" and \"ISAC-OF\" used interchangeably ")
        f.write("across different modality communities.\n\n")
        f.write("**Supporting evidence:**\n")
        for item in c1_items:
            f.write(f"- [{item['paper_id']}] {item['title'][:60]}... — \"{item['supporting_excerpt'][:50]}...\"\n")
        f.write("\n")
        
        # C2 paragraph
        c2_items = [r for r in gold_set if r["claim_id"] == "C2"][:5]
        f.write("## C2: Non-Standardized Metrics\n\n")
        f.write("Sensing performance is reported using diverse metrics (RMSE, CRB, FIM, range resolution) ")
        f.write("with inconsistent definitions, making cross-study comparison challenging.\n\n")
        f.write("**Supporting evidence:**\n")
        for item in c2_items:
            f.write(f"- [{item['paper_id']}] {item['title'][:60]}... — uses {item.get('metric_terms', 'various metrics')}\n")
        f.write("\n")
        
        # C3 paragraph
        c3_items = [r for r in gold_set if r["claim_id"] == "C3"][:5]
        f.write("## C3: Sub-Domain Fragmentation\n\n")
        f.write("Research in fiber, FSO, VLC, and Photo-THz sensing has evolved largely in isolation, ")
        f.write("with limited cross-citation and no unified evaluation framework.\n\n")
        f.write("**Supporting evidence:**\n")
        for item in c3_items:
            f.write(f"- [{item['paper_id']}] {item['title'][:60]}... — \"{item['supporting_excerpt'][:50]}...\"\n")
        f.write("\n")
        
        # C4 paragraph
        c4_items = [r for r in gold_set if r["claim_id"] == "C4"][:5]
        f.write("## C4: Weak Cross-Domain Technology Transfer\n\n")
        f.write("Despite shared physical-layer challenges, technology transfer between O-ISAC sub-domains ")
        f.write("remains limited due to incompatible hardware paradigms and evaluation methodologies.\n\n")
        f.write("**Supporting evidence:**\n")
        for item in c4_items:
            f.write(f"- [{item['paper_id']}] {item['title'][:60]}... — {item.get('cross_domain_note', 'transfer gap')}\n")
        f.write("\n")
        
        # C5 paragraph
        c5_items = [r for r in gold_set if r["claim_id"] == "C5"][:5]
        f.write("## C5: Missing Unifying Framework\n\n")
        f.write("No comprehensive taxonomy, benchmark suite, or unified PHY-layer framework exists ")
        f.write("to enable systematic comparison across O-ISAC modalities.\n\n")
        f.write("**Supporting evidence:**\n")
        for item in c5_items:
            f.write(f"- [{item['paper_id']}] {item['title'][:60]}... — \"{item['supporting_excerpt'][:50]}...\"\n")
        f.write("\n")
        
        # Normalization proposal
        f.write("---\n\n")
        f.write("## Minimal Normalization Proposal\n\n")
        f.write("To enable cross-modality comparison, we propose:\n")
        f.write("1. **Ranging accuracy**: Report both RMSE (absolute) and CRB/FIM (theoretical bound) at specified SNR.\n")
        f.write("2. **Resolution**: Standardize Δr definition as 3-dB bandwidth-based for all modalities.\n")
        f.write("3. **SNR**: Distinguish electrical vs. optical SNR; report both when applicable.\n")
        f.write("4. **Benchmark scenarios**: Define indoor/outdoor, static/mobile reference scenarios.\n")
        f.write("5. **Unified taxonomy**: Adopt consistent O-ISAC terminology across modalities.\n")
    
    print(f"Wrote I-C skeleton to {skeleton_path}")
    
    # --- QA Report ---
    qa_path = os.path.join(OUTPUT_DIR, "IC_QA_report_v3_2.txt")
    
    auth_high = sum(1 for r in gold_set if r.get("authority_class") in ["Standard", "Survey", "Tutorial", "Overview"])
    
    with open(qa_path, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("IC Evidence Gold Set v3.2 - QA Report\n")
        f.write("=" * 60 + "\n\n")
        
        f.write("## Gold Set Statistics\n")
        f.write(f"Total gold items: {len(gold_set)} (target: 50-80) {'✓' if 50 <= len(gold_set) <= 80 else '✗'}\n\n")
        
        f.write("## Claim Distribution\n")
        for c in ["C1", "C2", "C3", "C4", "C5"]:
            cnt = claim_counts.get(c, 0)
            f.write(f"  {c}: {cnt} (target: ≥10) {'✓' if cnt >= 10 else '✗'}\n")
        
        f.write(f"\n## Authority Distribution\n")
        for auth in ["Standard", "Survey", "Tutorial", "Overview", "Research"]:
            f.write(f"  {auth}: {auth_counts.get(auth, 0)}\n")
        f.write(f"\nHigh-authority items (Standard/Survey/Tutorial/Overview): {auth_high} (target: ≥12) {'✓' if auth_high >= 12 else '✗'}\n")
        
        f.write(f"\n## Modality Distribution\n")
        total = len(gold_set)
        for mod, cnt in mod_counts.most_common():
            pct = (cnt / total * 100) if total else 0
            f.write(f"  {mod}: {cnt} ({pct:.1f}%) {'✗ >40%' if pct > 40 else '✓'}\n")
        
        f.write(f"\nModalities covered: {len(mod_counts)} (target: ≥4) {'✓' if len(mod_counts) >= 4 else '✗'}\n")
        
        f.write(f"\n## C3 Audit Summary\n")
        f.write(f"Original C3 items: {len(c3_audit)}\n")
        f.write(f"Kept: {len([a for a in c3_audit if a['kept_or_dropped']=='KEPT'])}\n")
        f.write(f"Relabeled: {c3_relabeled}\n")
        f.write(f"Dropped: {c3_dropped}\n")
        
        f.write(f"\n## Conflicts\n")
        f.write(f"Gold conflicts: {len(gold_conflicts)}\n")
    
    print(f"Wrote QA report to {qa_path}")
    print("\n" + "=" * 60)
    print("Gold Set v3.2 Distillation Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
