import json
import re
from pathlib import Path
from tqdm import tqdm
import collections
import string

# Configuration
PROJECT_ROOT = Path(r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST")
DATA_DIR = PROJECT_ROOT / "data/corp_std"
OUTPUT_REPORT = PROJECT_ROOT / "analysis/gap_rpt.json"

STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by", 
    "from", "up", "down", "is", "are", "was", "were", "be", "been", "has", "have", "had", 
    "it", "this", "that", "these", "those", "which", "who", "what", "where", "when", "why",
    "how", "can", "could", "will", "would", "should", "may", "might", "must", "survey", 
    "comprehensive", "review", "overview", "tutorial", "paper", "article", "based", "using",
    "proposed", "propose", "approach", "method", "system", "network", "communication", 
    "analysis", "performance", "wireless", "challenges", "issues", "future", "directions",
    "applications", "technologies", "enabled", "driven", "towards", "state-of-the-art",
    "recent", "advances", "perspective", "communications", "networks", "systems", "study"
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text) # Keep hyphens for things like multi-modal
    return text

def get_ngrams(text, n=2):
    tokens = [t for t in clean_text(text).split() if t not in STOP_WORDS and len(t) > 2]
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]

def extract_abstract(md_path):
    """
    Heuristic to extract abstract: text between 'Abstract' header and 'Introduction'.
    Or just the first big blob of text.
    """
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            text = f.read()
            
        # Try finding "Abstract" header
        # Many converted MDs might not have a clean # Abstract header, 
        # but often have the text "Abstract" at the start.
        match = re.search(r'(?i)(?:abstract|summary)\s*[:\-\n]+(.*?)(?=\n#|\nI\.|Introduction)', text, re.DOTALL)
        if match:
            return match.group(1).strip()
            
        # Fallback: Read first 20 lines (metadata usually)
        # Taking title is safer for now if abstract parsing is flaky.
        return "" 
    except:
        return ""

def analyze_gaps():
    papers = sorted(list(DATA_DIR.glob("COMST_*/COMST_*.md")))
    print(f"Analyzing content of {len(papers)} papers...")
    
    titles = []
    abstracts = []
    
    # 1. Load Data
    for md_path in tqdm(papers):
        # We assume the file content starts with the Title (H1)
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip().strip('#').strip()
                if len(first_line) > 10:
                    titles.append(first_line)
                    
            abs_text = extract_abstract(md_path)
            if abs_text:
                abstracts.append(abs_text)
                
        except Exception as e:
            pass

    # 2. NGram Analysis
    bigram_counts = collections.Counter()
    trigram_counts = collections.Counter()
    
    # Weight Titles more than abstracts (x3)
    for title in titles:
        for _ in range(3):
            bigram_counts.update(get_ngrams(title, 2))
            trigram_counts.update(get_ngrams(title, 3))
            
    for abs_text in abstracts:
        bigram_counts.update(get_ngrams(abs_text, 2))
        trigram_counts.update(get_ngrams(abs_text, 3))
        
    # 3. Define "Red Ocean" (Saturated)
    red_ocean = bigram_counts.most_common(20)
    
    print("\n=== RED OCEAN (Saturated Topics) ===")
    for term, count in red_ocean:
        print(f"{term}: {count}")
        
    # 4. Define "Blue Ocean" (Potential Gaps)
    # Strategy: Look for terms that appear but are low frequency (1-3 times) in this elite set
    # meaningful keywords that are NOT in the top list.
    # This requires manual interpretation, but we can list the "Tail".
    
    results = {
        "status": "success",
        "red_ocean": red_ocean,
        "trigrams": trigram_counts.most_common(20),
        "titles_analyzed": len(titles)
    }
    
    with open(OUTPUT_REPORT, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4)
        
    print(f"\nGap analysis saved to {OUTPUT_REPORT}")

if __name__ == "__main__":
    analyze_gaps()
