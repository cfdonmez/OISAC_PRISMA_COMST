import json
import re
from pathlib import Path
from tqdm import tqdm
import collections

# Configuration
PROJECT_ROOT = Path(r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST")
DATA_DIR = PROJECT_ROOT / "data/corpus_standardized"
OUTPUT_REPORT = PROJECT_ROOT / "analysis/rhetoric_report.json"

# Common research verbs to search for manually since we don't have POS tagger
RESEARCH_VERBS = ["summarizes", "compares", "lists", "provides", "presents", "shows", "illustrates", "surveys", "reviews", "classifies", "outlines", "give", "discusses", "highlight", "focuses"]

def get_verbs_near_table(text):
    """
    Finds verbs used in sentences that cite a table (e.g. "Table I summarizes...")
    Using regex instead of NLTK.
    """
    # Regex to find sentences appearing to cite a table
    citations = re.findall(r'([^.]*?Table\s+[IVX0-9]+[^.]*\.)', text, re.IGNORECASE)
    
    verbs = []
    for sent in citations:
        sent_lower = sent.lower()
        if "table" in sent_lower:
            # Check for our list of verbs
            for v in RESEARCH_VERBS:
                # Naive check: is the verb in the sentence?
                # To be slightly smarter, check if it usually follows "Table"
                if re.search(fr'\b{v}\b', sent_lower):
                    verbs.append(v)
            
    return verbs

def analyze_transitions(text):
    """
    Analyzes the last sentences of paragraphs to see how they transition.
    """
    paragraphs = re.split(r'\n\s*\n', text)
    transitions = []
    
    for p in paragraphs:
        clean_p = p.strip()
        if len(clean_p.split()) > 40: # Valid paragraph
            # Get last sentence
            sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', clean_p)
            if sentences:
                last_sent = sentences[-1].strip()
                # Check for cohesive devices
                first_word = last_sent.split(' ')[0].lower().strip(',')
                if first_word in ["thus", "therefore", "consequently", "hence", "finally", "however", "summary", "in"]:
                    transitions.append(last_sent)
                    
    return transitions

def analyze_rhetoric():
    papers = sorted(list(DATA_DIR.glob("COMST_*/COMST_*.md")))
    print(f"Analyzing rhetorical patterns in {len(papers)} papers (Scope Check: YES, all of them)...")
    
    table_verbs = collections.Counter()
    transition_starters = collections.Counter()
    
    for md_path in tqdm(papers):
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                text = f.read()
            
            # 1. Table Consistency Verbs
            verbs = get_verbs_near_table(text)
            table_verbs.update(verbs)
            
            # 2. Transition Patterns
            trans_sents = analyze_transitions(text)
            for s in trans_sents:
                first_word = s.split(' ')[0].lower().rstrip(',')
                transition_starters[first_word] += 1
                
        except Exception as e:
            pass
            
    # Synthesis
    print("\n=== Rhetorical Analysis Results ===")
    
    print("\nTop Verbs used with Tables (How they refer):")
    common_verbs = table_verbs.most_common(15)
    for v, c in common_verbs:
        print(f"{v}: {c}")
        
    print("\nTop Transition Starters (How they end paragraphs):")
    common_trans = transition_starters.most_common(10)
    for w, c in common_trans:
        print(f"{w}: {c}")
        
    # Save Report
    results = {
        "table_verbs": common_verbs,
        "transition_starters": common_trans
    }
    with open(OUTPUT_REPORT, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4)
        
    print(f"\nRhetoric report saved to {OUTPUT_REPORT}")

if __name__ == "__main__":
    analyze_rhetoric()
