import json
import re
from pathlib import Path
from tqdm import tqdm
import pandas as pd
import collections

# Configuration
PROJECT_ROOT = Path(r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST")
DATA_DIR = PROJECT_ROOT / "data/corpus_standardized"
OUTPUT_JSON = PROJECT_ROOT / "analysis/corpus_structure.json"
OUTPUT_CSV = PROJECT_ROOT / "analysis/corpus_structure_summary.csv"

# Canonical Mapping Rules (Regex -> Canonical Tag)
SECTION_MAP = {
    r"intro|overview|background": "INTRODUCTION",
    r"related work|literature|state of the art|prior work|survey": "LITERATURE_REVIEW",
    r"system|architecture|framework|model|scenario": "SYSTEM_MODEL",
    r"problem|formulation|analysis|optimization|method|algorithm|scheme|mechanism|design": "TECHNICAL_SOLUTION",
    r"simulation|numerical|result|performance|experiment|evaluation": "PERFORMANCE_EVALUATION",
    r"challenge|open issue|future|direction|opportunity|trend": "CHALLENGES_AND_FUTURE",
    r"conclusion|summary|remark": "CONCLUSION",
    r"reference|bibliography": "REFERENCES",
    r"standard|standardization|regulation|3gpp|ieee": "STANDARDIZATION"
}

def normalize_header(header_text):
    """
    Maps a raw header text to a canonical tag using regex.
    Returns 'OTHER' if no match found.
    """
    text = header_text.lower().strip()
    # Remove numbering (e.g., "I. Introduction" -> "Introduction")
    text = re.sub(r'^[ivx0-9\.\-]+\s+', '', text)
    
    for pattern, tag in SECTION_MAP.items():
        if re.search(pattern, text):
            return tag
    return "OTHER"

def extract_structure():
    if not DATA_DIR.exists():
        print("Standardized corpus not found.")
        return

    papers = sorted(list(DATA_DIR.glob("COMST_*/COMST_*.md")))
    print(f"Analyzing structure of {len(papers)} papers...")
    
    corpus_data = []
    
    for md_path in tqdm(papers):
        paper_id = md_path.stem
        
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            headers = []
            structure_seq = []
            
            for line in lines:
                if line.lstrip().startswith('#'):
                    # Determine level (H1, H2, H3)
                    level = len(line) - len(line.lstrip('#'))
                    text = line.strip('#').strip()
                    
                    # We focus mainly on Top-Level (H1/H2) for the high-level skeleton
                    # Many papers use H1 for Title/Metadata and H2 for actual sections, or vice versa.
                    # Let's verify: usually "Introduction" is a top-level section.
                    if text:
                        tag = normalize_header(text)
                        
                        # Store detailed header info
                        headers.append({
                            "level": level,
                            "text": text,
                            "tag": tag
                        })
                        
                        # Build the sequence of "Main" sections (ignoring sub-sections if possible, or just filtering for distinct transitions)
                        # Heuristic: Only track transitions between different tags to avoid "Introduction -> Introduction" repetitions
                        if tag != "OTHER":
                            if not structure_seq or structure_seq[-1] != tag:
                                structure_seq.append(tag)

            corpus_data.append({
                "paper_id": paper_id,
                "header_count": len(headers),
                "structure_sequence": structure_seq,
                "raw_headers": [h["text"] for h in headers if h["level"] <= 2] # Sample top headers
            })
            
        except Exception as e:
            print(f"Error parsing {paper_id}: {e}")

    # Aggregation & Analysis
    
    # 1. Common Sequence Analysis (Transition Matrix proxy)
    # We can count how many papers contain each section type
    tag_counts = collections.defaultdict(int)
    for p in corpus_data:
        unique_tags = set(p["structure_sequence"])
        for t in unique_tags:
            tag_counts[t] += 1
            
    # 2. Average position (normalized)
    
    print("\n=== Corpus Structure Analysis ===")
    print("Section Frequency (in % of papers):")
    df_freq = pd.DataFrame.from_dict(tag_counts, orient='index', columns=['count'])
    df_freq['percentage'] = (df_freq['count'] / len(papers)) * 100
    print(df_freq.sort_values('percentage', ascending=False))
    
    # Save Data
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(corpus_data, f, indent=4)
        
    df_freq.to_csv(OUTPUT_CSV)
    print(f"\nStructure data saved to {OUTPUT_JSON}")

if __name__ == "__main__":
    extract_structure()
