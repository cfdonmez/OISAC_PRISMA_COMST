import json
import re
from pathlib import Path
from tqdm import tqdm

# Configuration
PROJECT_ROOT = Path(r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST")
DATA_DIR = PROJECT_ROOT / "data/corpus_standardized"
OUTPUT_JSON = PROJECT_ROOT / "analysis/phrasebank.json"

# NLTK removed to avoid dependencies. We will use a simple regex for sentence splitting.

# Target Sections for Extraction (from our Structure Analysis)
TARGET_SECTIONS = ["INTRODUCTION", "LITERATURE_REVIEW"]

# Heuristic Patterns for "High-Value" Academic Sentences
# We are looking for "function" sentences, not content sentences.
PATTERNS = {
    "timeline_trends": [
        r"^Recently,", r"^In recent years,", r"^Over the past decade,", 
        r"^With the rapid development of", r"^Due to the emergence of"
    ],
    "problem_statement": [
        r"Although.*, there is still", r"However,.*remains a challenge", 
        r"Despite these efforts,", r"One major issue is", r"The main challenge lies in"
    ],
    "gap_identification": [
        r"To the best of our knowledge,", r"Few studies have investigated", 
        r"There is a lack of", r"Existing surveys mainly focus on",
        r"However, these works do not", r"In contrast to [\[\(].*?[\]\)]"
    ],
    "contribution": [
        r"The main contributions of this (paper|article|survey) are", 
        r"In this (paper|article|survey), we", r"This paper presents a comprehensive",
        r"Our objective is to", r"We aim to provide"
    ],
    "paper_organization": [
        r"The remainder of this paper is organized as follows", 
        r"Section .* describes", r"In Section .*, we discuss"
    ]
}

def extract_phrases():
    if not DATA_DIR.exists():
        print("Standardized corpus not found.")
        return

    # Load previously mapped structure to know where sections are (optional, but we can just parse commonly mapped headers again or assume standard top-down)
    # For simplicity/robustness, let's re-scan the files but only look at the first 200 lines for Intro/Related Work cues if separate mapping is complex.
    # Actually, we already standardized files. Let's just iterate and hunt.
    
    papers = sorted(list(DATA_DIR.glob("COMST_*/COMST_*.md")))
    print(f"Mining phrases from {len(papers)} papers...")
    
    phrasebank = {cat: [] for cat in PATTERNS.keys()}
    
    for md_path in tqdm(papers):
        paper_id = md_path.stem
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                text = f.read()
                
            # Simple Cleaning
            # Remove Markdown images/links
            text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
            text = re.sub(r'<.*?>', '', text)
            
            # Sentence Tokenization (Regex approximation)
            # Split by .!? followed by whitespace or usage of [Ref] notation
            # This is a bit coarse but sufficient for extracting "Trends" sentences
            sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
            
            # Filter Logic
            for sent in sentences:
                sent_clean = sent.strip().replace('\n', ' ')
                if len(sent_clean) < 20 or len(sent_clean) > 500:
                    continue
                    
                # Check against patterns
                for category, regex_list in PATTERNS.items():
                    for pattern in regex_list:
                        if re.search(pattern, sent_clean, re.IGNORECASE):
                            # Found a match!
                            # Anonymize Citations (replace [1], [15-20] with [Ref])
                            sent_final = re.sub(r'\[[\d,\s-]+\]', '[Ref]', sent_clean)
                            
                            phrasebank[category].append({
                                "text": sent_final,
                                "source": paper_id,
                                "pattern": pattern
                            })
                            break # Avoid double counting same sentence
                            
        except Exception as e:
            print(f"Error processing {paper_id}: {e}")

    # Deduplicate and Sort
    print("\n=== Phrasebank Stats ===")
    for cat, items in phrasebank.items():
        # Remove exact duplicates
        unique_texts = {item["text"]: item for item in items}
        phrasebank[cat] = list(unique_texts.values())
        print(f"{cat}: {len(phrasebank[cat])} unique templates found.")
        
    # Save
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(phrasebank, f, indent=4)
        
    print(f"\nPhrasebank saved to {OUTPUT_JSON}")

if __name__ == "__main__":
    extract_phrases()
