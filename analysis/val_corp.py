import json
import os
import re
from pathlib import Path
from tqdm import tqdm
import pandas as pd

# Configuration
MANIFEST_PATH = Path(r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\corp_man.json")
OUTPUT_REPORT = Path(r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\analysis\corpus_fidelity_report.csv")

# Weights (Adjustable)
W_TEXT = 0.3
W_STRUCT = 0.3
W_FIG = 0.2
W_BIB = 0.2

# Expected Structural Elements (Canonical Headings)
CANONICAL_SECTIONS = [
    r"introduction|overview",
    r"related work|literature review|state of the art",
    r"system model|architecture|framework",
    r"challenges|open issues|future directions|opportunities",
    r"conclusion"
]

def calculate_fidelity(md_path):
    """
    Calculates the fidelity score for a single MD file.
    """
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Text Score (r_text)
        # Heuristic: A full survey should be at least 20k chars (~3-4k words minimum). 
        # Cap at 1.0 for >50k chars.
        char_count = len(content)
        r_text = min(1.0, char_count / 50000.0)
        
        # 2. Structure Score (r_struct)
        # Check against canonical headers
        headers_found = 0
        md_lower = content.lower()
        # Find headers marked with ## or #
        # We search specifically in lines starting with #
        header_lines = [line.lower() for line in content.split('\n') if line.strip().startswith('#')]
        header_text = "\n".join(header_lines)
        
        for pattern in CANONICAL_SECTIONS:
            if re.search(pattern, header_text):
                headers_found += 1
                
        r_struct = headers_found / len(CANONICAL_SECTIONS)
        
        # 3. Figure Score (r_fig)
        # Count image tags used in MD
        fig_count = len(re.findall(r'!\[.*?\]\(.*?\)', content))
        # Heuristic: Expect at least 5 figures for a score of 1.0
        r_fig = min(1.0, fig_count / 5.0)
        
        # 4. Bibliography Score (r_bib)
        # Look for "References" at the end
        r_bib = 1.0 if re.search(r'^#+\s*reference', header_text, re.MULTILINE) else 0.0
        
        # Composite Score
        score = (W_TEXT * r_text) + (W_STRUCT * r_struct) + (W_FIG * r_fig) + (W_BIB * r_bib)
        
        return {
            "score": round(score, 2),
            "char_count": char_count,
            "headers_found": headers_found,
            "fig_count": fig_count,
            "has_bib": bool(r_bib),
            "r_text": round(r_text, 2),
            "r_struct": round(r_struct, 2),
            "r_fig": round(r_fig, 2),
            "r_bib": r_bib
        }
        
    except Exception as e:
        print(f"Error processing {md_path}: {e}")
        return None

def validate_corpus():
    if not MANIFEST_PATH.exists():
        print("Manifest not found.")
        return

    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        manifest = json.load(f)
        
    results = []
    
    print(f"Validating {len(manifest)} papers...")
    
    for entry in tqdm(manifest):
        md_path = entry.get("md_path")
        if not md_path or not os.path.exists(md_path):
            entry["qa_status"] = "missing_file"
            entry["fidelity_score"] = 0
            results.append({**entry, **{"score": 0, "notes": "File not found"}})
            continue
            
        metrics = calculate_fidelity(md_path)
        
        if metrics:
            # Update entry status based on score
            # Threshold > 0.70 -> OK, else FIX
            status = "qa_ok" if metrics["score"] >= 0.70 else "qa_fix"
            
            row = {
                "paper_id": entry["paper_id"],
                "fidelity_score": metrics["score"],
                "qa_status": status,
                "title": entry["title"],
                **metrics, # flatten metrics
                "md_path": md_path
            }
            results.append(row)
            
    # Save Report
    df = pd.DataFrame(results)
    df.to_csv(OUTPUT_REPORT, index=False)
    
    # Summary
    print("\n=== Corpus Fidelity Report ===")
    print(f"Total Papers: {len(df)}")
    if not df.empty:
        print(f"Passed (Score >= 0.7): {len(df[df['fidelity_score'] >= 0.7])}")
        print(f"Failed (Score < 0.7): {len(df[df['fidelity_score'] < 0.7])}")
        print(f"Average Score: {df['fidelity_score'].mean():.2f}")
        print(f"Report saved to: {OUTPUT_REPORT}")
    else:
        print("No results generated.")

if __name__ == "__main__":
    validate_corpus()
