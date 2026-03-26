
import os
import re

base_path = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\corpus_standardized"
papers = ["COMST_030", "COMST_035", "COMST_040", "COMST_045", "COMST_050"]
output_file = "analysis_conclusions_output.txt"

def clean_text(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\[\d+\]', '', text)
    return ' '.join(text.split())

with open(output_file, 'w', encoding='utf-8') as out:
    for paper_id in papers:
        file_path = os.path.join(base_path, paper_id, f"{paper_id}.md")
        if not os.path.exists(file_path):
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            continue
            
        out.write(f"--- ANALYZING {paper_id} ---\n")
        
        # Strategy: Find "CONCLUSION" header and take text until end or References
        # Regex: Header followed by text, stopping at "REFERENCES" or "ACKNOWLEDGMENT" or end of file
        match = re.search(r'(?:#+\s*|\b)(?:VI\.|VII\.|VIII\.|IX\.|X\.|XI\.)?\s*CONCLUSIONS?(?:\s+AND\s+FUTURE\s+WORK)?(.*?)(?:(?:#+\s*)?REFERENCES|ACKNOWLEDGMENT|APPENDIX)', content, re.DOTALL | re.IGNORECASE)
        
        if match:
            raw_text = match.group(1)
            cleaned = clean_text(raw_text)
            sentences = [s.strip() for s in cleaned.split('.') if len(s.strip()) > 10]
            
            out.write(f"WORD COUNT: {len(cleaned.split())}\n")
            if sentences:
                out.write(f"OPENING: {sentences[0]}.\n")
                out.write(f"CLOSING: {sentences[-1]}.\n")
            
            # Check for "In this paper/article/survey"
            if "research directions" in cleaned.lower() or "future" in cleaned.lower():
                out.write("CONTAINS FUTURE WORK: Yes\n")
            else:
                out.write("CONTAINS FUTURE WORK: No (Likely separate section)\n")
                
            out.write(f"PREVIEW: {cleaned[:300]}...\n")
        else:
            out.write("MISSING: Could not locate Conclusion block.\n")
            
        out.write("\n")
