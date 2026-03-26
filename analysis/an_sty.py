import json
import re
from pathlib import Path
from tqdm import tqdm
import collections
import statistics

# Configuration
PROJECT_ROOT = Path(r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST")
DATA_DIR = PROJECT_ROOT / "data/corp_std"
OUTPUT_REPORT = PROJECT_ROOT / "analysis/stylo_rpt.json"

# Heuristic patterns for visual classification
VISUAL_KEYWORDS = {
    "Taxonomy": ["taxonomy", "classification", "category", "hierarchy", "branch"],
    "System Model": ["system model", "scenario", "architecture", "framework", "schematic", "overview"],
    "Simulation/Graph": ["performance", "result", "simulation", "vs", "versus", "ber", "throughput", "capacity", "rate"],
    "Process/Flow": ["flowchart", "process", "workflow", "sequence", "protocol", "step"],
}

def analyze_citations(text):
    """
    Extracts 4-digit years from lines that look like references.
    Heuristic: Lines starting with [X] or similar in a Reference section.
    """
    years = []
    # Find Reference Section
    ref_match = re.search(r'(?i)REFERENCES\s*\n(.*?)$', text, re.DOTALL)
    if not ref_match: 
        # Fallback: Scan absolute bottom 20% of file
        lines = text.split('\n')
        ref_text = "\n".join(lines[-int(len(lines)*0.2):])
    else:
        ref_text = ref_match.group(1)
        
    # Find years (1990-2029)
    # Simple regex finding 4 digit numbers
    # We filter out line numbers/page numbers by context if possible, 
    # but raw year distribution is usually robust enough given the volume.
    candidates = re.findall(r'\b(19[9][0-9]|20[0-2][0-9])\b', ref_text)
    years = [int(y) for y in candidates]
    return years

def analyze_visuals(text):
    """
    Classifies figures based on caption text.
    """
    visual_counts = collections.Counter()
    # Find Captions: Fig. X, Figure X
    captions = re.findall(r'(?:Fig\.|Figure)\s*\d+[:\.]\s*(.*?)(?=\n|$)', text, re.IGNORECASE)
    
    for cap in captions:
        classified = False
        cap_lower = cap.lower()
        for cat, keywords in VISUAL_KEYWORDS.items():
            if any(k in cap_lower for k in keywords):
                visual_counts[cat] += 1
                classified = True
                break
        if not classified:
            visual_counts["Other"] += 1
            
    return visual_counts

def analyze_paragraphs(text):
    """
    Extracts paragraph stats: Length (sentences), Topic Sentences.
    """
    # Simple Paragraph Split: Double Newline
    paragraphs = re.split(r'\n\s*\n', text)
    valid_paras = []
    topic_sentences = []
    
    for p in paragraphs:
        clean_p = p.strip()
        # Filter out short blurbs, headers, metadata
        if len(clean_p.split()) > 40: # Assume body paragraph has > 40 words
            valid_paras.append(clean_p)
            # Extact first sentence
            match = re.search(r'^(.*?)[\.\?!]', clean_p)
            if match:
                topic_sentences.append(match.group(1))
    
    lengths = [len(p.split()) for p in valid_paras]
    return lengths, topic_sentences

def analyze_style():
    papers = sorted(list(DATA_DIR.glob("COMST_*/COMST_*.md")))
    print(f"Deep analyzing {len(papers)} papers...")
    
    all_citation_years = []
    visual_agg = collections.Counter()
    para_lengths = []
    sample_topic_sentences = []
    
    for md_path in tqdm(papers):
        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                text = f.read()
                
            # 1. Citations
            years = analyze_citations(text)
            all_citation_years.extend(years)
            
            # 2. Visuals
            v_counts = analyze_visuals(text)
            visual_agg.update(v_counts)
            
            # 3. Paragraphs
            p_lens, t_sents = analyze_paragraphs(text)
            para_lengths.extend(p_lens)
            if t_sents: 
                # Keep a few samples
                sample_topic_sentences.extend(t_sents[:2]) 
                
        except Exception as e:
            pass

    # Synthesis
    report = {}
    
    # Citation Freshness
    if all_citation_years:
        current_year = 2024 # Approx
        fresh_count = sum(1 for y in all_citation_years if y >= current_year - 5)
        report["citation_freshness"] = {
            "total_citations_analyzed": len(all_citation_years),
            "median_year": int(statistics.median(all_citation_years)),
            "fresh_percentage": round(fresh_count / len(all_citation_years) * 100, 1)
        }
        
    # Visual Taxonomy
    total_visuals = sum(visual_agg.values())
    report["visual_taxonomy"] = {k: round(v/total_visuals*100, 1) for k,v in visual_agg.most_common()}
    
    # Paragraph Dynamics
    if para_lengths:
        report["paragraph_stats"] = {
            "avg_words": int(statistics.mean(para_lengths)),
            "median_words": int(statistics.median(para_lengths)),
            "std_dev": int(statistics.stdev(para_lengths))
        }
    
    report["topic_sentence_samples"] = sample_topic_sentences[:20]

    with open(OUTPUT_REPORT, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4)
        
    print("\n=== Stylometric Analysis ===")
    print(f"Citation Freshness: {report.get('citation_freshness', {}).get('fresh_percentage', 0)}% (Last 5 Years)")
    print("Visual Types:")
    for k,v in report.get("visual_taxonomy", {}).items():
        print(f"  {k}: {v}%")
    print(f"Avg Paragraph Length: {report.get('paragraph_stats', {}).get('avg_words', 0)} words")
    
    print(f"\nReport saved to {OUTPUT_REPORT}")

if __name__ == "__main__":
    analyze_style()
