import csv
import os
from collections import defaultdict

INPUT_CSV = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\analysis\IC_evidence_claims_v2.csv"
OUTPUT_CSV = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\analysis\IC_term_metric_conflicts_v2.csv"

# Concept Mappings
TERM_GROUPS = {
    "fiber_isac": ["ISAC-OF", "photonic ISAC", "fiber-ISAC", "optical ISAC"],
    "retro_isac": ["RO-ISAC", "retroreflective optical ISAC", "MRR-ISAC"],
    "vlc_isac": ["VLC", "LiFi", "visible light communication", "optical wireless ISAC"]
}

METRIC_GROUPS = {
    "ranging_accuracy": ["RMSE", "CRB", "FIM", "localization error", "sensing accuracy"],
    "ranging_resolution": ["range resolution", "\\Delta R", "\\Delta r", "\\sigma_R"],
    "tradeoffs": ["trade-off", "capacity-resolution", "Pareto"]
}

def clean_term(t):
    return t.strip().replace("\\", "").lower()

def main():
    print("Synthesizing Conflicts...")
    
    # 1. Load Evidence
    evidence = []
    with open(INPUT_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        evidence = list(reader)
        
    conflicts = []
    
    # 2. Terminology Conflicts (Fragmentation)
    # Strategy: Find papers using different terms for the SAME concept
    
    # Invert mapping: Term -> Concept
    term_to_concept = {}
    for concept, terms in TERM_GROUPS.items():
        for t in terms:
            term_to_concept[t.lower()] = concept
            
    # Group evidence by Concept
    concept_evidence = defaultdict(list)
    
    for row in evidence:
        if row['claim_id'] == 'C1' and row['terminology_terms']:
            t_raw = row['terminology_terms']
            # Try exact match first
            found_concept = None
            for t_key in term_to_concept:
                if t_key in t_raw.lower():
                    found_concept = term_to_concept[t_key]
                    break
            
            if found_concept:
                concept_evidence[found_concept].append(row)
                
    # Generate Pairs
    for concept, rows in concept_evidence.items():
        # Group by the specific variant used
        variant_groups = defaultdict(list)
        for r in rows:
            variant_groups[r['terminology_terms']].append(r)
            
        variants = list(variant_groups.keys())
        if len(variants) > 1:
            # We have a conflict! Simple pairwise check
            # Best pair: Most frequent A vs Most frequent B
            sorted_vars = sorted(variants, key=lambda v: len(variant_groups[v]), reverse=True)
            vA = sorted_vars[0]
            vB = sorted_vars[1]
            
            rowA = variant_groups[vA][0]
            rowB = variant_groups[vB][0]
            
            conflicts.append({
                "conflict_type": "Terminology Fragmentation",
                "concept": concept,
                "variant_A": vA,
                "variant_B": vB,
                "paper_A_id": rowA['paper_id'],
                "paper_B_id": rowB['paper_id'],
                "excerpts_A": rowA['supporting_excerpt'],
                "excerpts_B": rowB['supporting_excerpt'],
                "analysis": f"Papers use different terms ('{vA}' vs '{vB}') for essentially the same {concept} concept, hindering searchability.",
                "normalization_proposal": f"Standardize to '{concept.replace('_', ' ').upper()}'",
                "confidence": 0.95
            })

    # 3. Metric Conflicts (Incomparability)
    # Strategy: Papers assessing "Ranging" using RMSE vs Resolution vs CRB
    
    # Invert Metric Mapping
    metric_to_concept = {}
    for concept, terms in METRIC_GROUPS.items():
        for t in terms:
            metric_to_concept[t.lower()] = concept

    metric_evidence = defaultdict(list)
    for row in evidence:
        if row['claim_id'] == 'C2' and row['metric_terms']:
            m_raw = row['metric_terms']
            found_concept = None
            for m_key in metric_to_concept:
                if m_key in m_raw.lower():
                    found_concept = metric_to_concept[m_key]
                    break
            if found_concept:
                metric_evidence[found_concept].append(row)
                
    for concept, rows in metric_evidence.items():
        # Check for heterogeneity
        used_metrics = set([r['metric_terms'] for r in rows])
        if len(used_metrics) > 1:
            # Pick two distinct examples
            m_list = list(used_metrics)
            mA = m_list[0]
            mB = m_list[1]
            
            rA = next(r for r in rows if r['metric_terms'] == mA)
            rB = next(r for r in rows if r['metric_terms'] == mB)
            
            conflicts.append({
                "conflict_type": "Metric Inconsistency",
                "concept": concept,
                "variant_A": mA,
                "variant_B": mB,
                "paper_A_id": rA['paper_id'],
                "paper_B_id": rB['paper_id'],
                "excerpts_A": rA['supporting_excerpt'],
                "excerpts_B": rB['supporting_excerpt'],
                "analysis": f"Inconsistent evaluation of {concept}: One uses '{mA}', another uses '{mB}'. Makes direct comparison impossible.",
                "normalization_proposal": "Report both Resolution (physical limit) and RMSE (statistical performance).",
                "confidence": 0.9
            })

    # Write Output
    headers = [
        "conflict_type", "concept", "variant_A", "variant_B", "paper_A_id",
        "paper_B_id", "excerpts_A", "excerpts_B", "analysis", "normalization_proposal", "confidence"
    ]
    
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(conflicts)
        
    print(f"Synthesized {len(conflicts)} conflicts to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
