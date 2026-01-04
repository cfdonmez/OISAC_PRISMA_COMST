import json
import re
from pathlib import Path
from tqdm import tqdm
import collections

# Configuration
PROJECT_ROOT = Path(r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST")
DATA_DIR = PROJECT_ROOT / "data/corpus_standardized"
OUTPUT_REPORT = PROJECT_ROOT / "analysis/gap_methodology_report.csv"

# Keywords that suggest a table is comparing surveys
# "Table I: Comparison of existing surveys..."
GAP_TABLE_KEYWORDS = ["comparison", "existing", "survey", "related work", "prior", "literature", "summary"]

def is_gap_table(caption_text, table_content):
    """
    Heuristic to decide if a table is a 'Gap Analysis' table.
    1. Caption contains magic words.
    2. Table content has column usually named "Ref" or "Year" and "Focus".
    """
    text = caption_text.lower()
    if any(k in text for k in GAP_TABLE_KEYWORDS):
        return True
    
    # Check headers directly
    if table_content and "|" in table_content[0]:
        headers = [h.strip().lower() for h in table_content[0].split("|")]
        if "ref" in headers or "reference" in headers or "year" in headers:
            # If it also has "contributions" or "focus" or "limitations", it's likely a gap table
            if any(k in headers for k in ["contributions", "contribution", "focus", "scope", "limitations", "drawbacks", "challenges", "covered"]):
                return True
                
    return False

def extract_gap_methods():
    papers = sorted(list(DATA_DIR.glob("COMST_*/COMST_*.md")))
    print(f"Hunting for Gap Tables in {len(papers)} papers...")
    
    extracted_tables = []
    
    for md_path in tqdm(papers):
        paper_id = md_path.stem
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            # Naive Markdown Table Parser
            # Look for lines starting with |
            
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                
                # Check for Figure/Table Caption format typically found in Marker output
                # e.g. "Table I: Comparison..." or just text before table
                # We often scan backwards a few lines from a table to find caption
                
                if line.startswith("|") and "---" in lines[i+1]:
                    # Found a table start
                    # Look back for caption (heuristic: last non-empty line)
                    caption = "Unknown"
                    for k in range(1, 5):
                        if i-k >= 0 and lines[i-k].strip():
                            caption = lines[i-k].strip()
                            break
                            
                    # Extract Headers
                    header_line = line
                    headers = [h.strip() for h in header_line.split("|") if h.strip()]
                    
                    if is_gap_table(caption, [header_line]):
                        extracted_tables.append({
                            "paper_id": paper_id,
                            "caption": caption,
                            "columns": headers
                        })
                        
                    # Skip table body
                    while i < len(lines) and lines[i].strip().startswith("|"):
                        i += 1
                else:
                    i += 1
                    
        except Exception as e:
            pass

    # Analysis
    # Count frequency of column names
    col_counter = collections.Counter()
    for t in extracted_tables:
        for c in t["columns"]:
            # Normalize column name
            c_norm = c.lower().replace('.', '')
            col_counter[c_norm] += 1
            
    print(f"\nFound {len(extracted_tables)} Gap/Comparison Tables.")
    print("Top 20 Comparison Dimensions (Columns):")
    for col, count in col_counter.most_common(20):
        print(f"{col}: {count}")
        
    # Save raw data to see exact column names
    import pandas as pd
    df = pd.DataFrame(extracted_tables)
    df.to_csv(OUTPUT_REPORT, index=False)
    print(f"\nGap Methodology data saved to {OUTPUT_REPORT}")

if __name__ == "__main__":
    extract_gap_methods()
