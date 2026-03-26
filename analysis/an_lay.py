import json
import re
from pathlib import Path
from tqdm import tqdm
import pandas as pd
import numpy as np

# Configuration
PROJECT_ROOT = Path(r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST")
DATA_DIR = PROJECT_ROOT / "data/corp_std"
OUTPUT_JSON = PROJECT_ROOT / "analysis/lay_stats.json"

# Reuse the map from structure extraction
SECTION_MAP = {
    r"intro|overview|background": "INTRODUCTION",
    r"related work|literature|state of the art|prior work|survey": "LITERATURE_REVIEW",
    r"system|architecture|framework|model|scenario": "SYSTEM_MODEL",
    r"problem|formulation|analysis|optimization|method|algorithm|scheme|mechanism|design": "TECHNICAL_SOLUTION",
    r"challenge|open issue|future|direction|opportunity|trend": "CHALLENGES_AND_FUTURE",
    r"conclusion|summary|remark": "CONCLUSION"
}

def normalize_header(header_text):
    text = header_text.lower().strip()
    text = re.sub(r'^[ivx0-9\.\-]+\s+', '', text)
    for pattern, tag in SECTION_MAP.items():
        if re.search(pattern, text):
            return tag
    return "OTHER"

def count_words(text):
    return len(text.split())

def analyze_layout():
    papers = sorted(list(DATA_DIR.glob("COMST_*/COMST_*.md")))
    print(f"Analyzing layout of {len(papers)} papers...")
    
    layout_data = []
    
    for md_path in tqdm(papers):
        paper_id = md_path.stem
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            current_section = "METADATA"
            section_buffers = {k: 0 for k in SECTION_MAP.values()}
            section_buffers["METADATA"] = 0
            section_buffers["OTHER"] = 0
            
            fig_count = 0
            table_count = 0 
            
            for line in lines:
                # Check for headers
                if line.lstrip().startswith('#'):
                    text = line.strip('#').strip()
                    if text:
                        # Determine if this starts a new major section
                        # We only switch context on H1/H2 roughly
                        # Heuristic: simple tag switch
                        tag = normalize_header(text)
                        if tag != "OTHER": 
                            current_section = tag
                            
                # Count Content
                word_count = count_words(line)
                section_buffers[current_section] += word_count
                
                # Count Visuals (Markdown heuristics)
                if line.strip().startswith("!"): # Image
                    fig_count += 1
                if line.strip().startswith("|") and "---" not in line: # Table row (naive)
                    # This overcounts rows, let's just count table CAPTIONS if possible
                    pass
            
            # Better specific counts via regex on full text for reliability
            full_text = "".join(lines)
            real_fig_count = len(re.findall(r'!\[.*?\]\(.*?\)', full_text))
            # Table count heuristic: "TABLE [IVX]" text
            real_table_count = len(re.findall(r'(?i)TABLE\s+[IVX]+', full_text))
            
            # Total words
            total_words = sum(section_buffers.values())
            
            layout_data.append({
                "paper_id": paper_id,
                "total_words": total_words,
                "figures": real_fig_count,
                "tables": real_table_count,
                "sections": section_buffers
            })
            
        except Exception as e:
            print(f"Error {paper_id}: {e}")

    # Aggregation
    df = pd.DataFrame(layout_data)
    
    stats = {
        "avg_total_words": int(df["total_words"].mean()),
        "avg_figures": int(df["figures"].mean()),
        "avg_tables": int(df["tables"].mean()),
        "section_avgs": {}
    }
    
    # Calculate average word count per section (excluding 0s to avoid skewing if section missing)
    section_df = pd.json_normalize(df["sections"])
    for col in section_df.columns:
        # Mean of non-zero entries
        non_zero = section_df[col][section_df[col] > 100]
        if not non_zero.empty:
            stats["section_avgs"][col] = int(non_zero.mean())
        else:
            stats["section_avgs"][col] = 0
            
    # Calculate % distribution
    total_avg = sum(stats["section_avgs"].values())
    if total_avg > 0:
        stats["section_pct"] = {k: round(v/total_avg*100, 1) for k,v in stats["section_avgs"].items()}
        
    print("\n=== Layout Statistics ===")
    print(f"Avg Length: {stats['avg_total_words']} words")
    print(f"Avg Visuals: {stats['avg_figures']} Figures, {stats['avg_tables']} Tables")
    print("\nSection Word Budgets:")
    for sec, count in stats["section_avgs"].items():
        print(f"{sec}: ~{count} words")
        
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=4)
        
    print(f"\nLayout stats saved to {OUTPUT_JSON}")

if __name__ == "__main__":
    analyze_layout()
