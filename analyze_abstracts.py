
import os
import re

base_path = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\corpus_standardized"
papers = [f"COMST_{i:03d}" for i in range(60, 71)]
output_file = "analysis_abstracts_output.txt"

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove citation brackets like [1], [15]
    text = re.sub(r'\[\d+\]', '', text)
    # Remove extra whitespace
    return ' '.join(text.split())

with open(output_file, 'w', encoding='utf-8') as out:
    for paper_id in papers:
        file_path = os.path.join(base_path, paper_id, f"{paper_id}.md")
        if not os.path.exists(file_path):
            out.write(f"MISSING: {file_path}\n")
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            out.write(f"ERROR reading {file_path}: {e}\n")
            continue
            
        out.write(f"--- ANALYZING {paper_id} ---\n")
        
        # Strategy: Look for "Abstract" (case insensitive) and take text until "Index Terms" or "Introduction"
        # In standardized markdown, Abstract is often marked with 'Abstract-' or '**Abstract**'
        
        # Regex to capture abstract content
        # Matches "Abstract" followed by content, stopping before "Index Terms" or "I. Introduction"
        match = re.search(r'(?:Abstract|ABSTRACT)(?:—|-|\.|:)?\s*(.*?)\s*(?:Index Terms|INDEX TERMS|I\.\s*Introduction|1\.\s*Introduction|#+\s*I\.)', content, re.DOTALL | re.IGNORECASE)
        
        if match:
            raw_abstract = match.group(1)
            cleaned_abstract = clean_text(raw_abstract)
            word_count = len(cleaned_abstract.split())
            
            # Split into sentences (naive split by period)
            sentences = [s.strip() for s in cleaned_abstract.split('.') if len(s.strip()) > 10]
            
            out.write(f"WORD COUNT: {word_count}\n")
            if sentences:
                out.write(f"FIRST SENTENCE (Context): {sentences[0]}.\n")
                if len(sentences) > 1:
                    out.write(f"LAST SENTENCE (Impact/Result): {sentences[-1]}.\n")
            
            out.write(f"FULL TEXT: {cleaned_abstract[:300]}...\n") # Preview
        else:
            out.write("MISSING: Could not locate Abstract block.\n")
            # fallback: look for text between authors and Introduction? 
            # often difficult without clearer markers.
            
        out.write("\n")
