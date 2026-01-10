
import os
import re

base_path = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\corpus_standardized"
# Deep analysis of 2 high-quality COMST papers
papers = ["COMST_014", "COMST_060"]
output_file = "analysis_body_deep_output.txt"

def clean_text(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\[\d+\]', '', text)
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
            
        out.write(f"{'='*60}\n")
        out.write(f"DEEP ANALYSIS: {paper_id}\n")
        out.write(f"{'='*60}\n\n")
        
        # --- FUNDAMENTALS SECTION ANALYSIS ---
        out.write("--- FUNDAMENTALS / BACKGROUND SECTION ---\n")
        # Look for "PRELIMINARIES", "FUNDAMENTALS", "BACKGROUND", "SYSTEM MODEL"
        fund_match = re.search(r'(?:#+\s*|\b)(?:II\.|III\.)?\s*(PRELIMINARIES|FUNDAMENTALS|BACKGROUND|SYSTEM MODEL)(.*?)(?:(?:#+\s*)(?:II\.|III\.|IV\.))', content, re.DOTALL | re.IGNORECASE)
        if fund_match:
            fund_title = fund_match.group(1)
            fund_content = clean_text(fund_match.group(2))
            out.write(f"SECTION TITLE: {fund_title}\n")
            out.write(f"WORD COUNT: {len(fund_content.split())}\n")
            # First sentences
            sentences = [s.strip() for s in fund_content.split('.') if len(s.strip()) > 10]
            if sentences:
                out.write(f"OPENING: {sentences[0]}.\n")
            out.write(f"PREVIEW: {fund_content[:500]}...\n\n")
        else:
            out.write("FUNDAMENTALS SECTION: Not found with standard headers.\n\n")
        
        # --- CHALLENGES / FUTURE SECTION ANALYSIS ---
        out.write("--- CHALLENGES / FUTURE SECTION ---\n")
        chall_match = re.search(r'(?:#+\s*|\b)(?:VI\.|VII\.|VIII\.)?\s*(CHALLENGES|FUTURE|OPEN ISSUES)(.*?)(?:(?:#+\s*)(?:CONCLUSION|REFERENCES|ACKNOWLEDGMENT))', content, re.DOTALL | re.IGNORECASE)
        if chall_match:
            chall_title = chall_match.group(1)
            chall_content = clean_text(chall_match.group(2))
            out.write(f"SECTION TITLE: {chall_title}\n")
            out.write(f"WORD COUNT: {len(chall_content.split())}\n")
            sentences = [s.strip() for s in chall_content.split('.') if len(s.strip()) > 10]
            if sentences:
                out.write(f"OPENING: {sentences[0]}.\n")
                if len(sentences) > 1:
                    out.write(f"CLOSING: {sentences[-1]}.\n")
            out.write(f"PREVIEW: {chall_content[:500]}...\n\n")
        else:
            out.write("CHALLENGES SECTION: Not found with standard headers.\n\n")
            
        # --- SUBSECTION STRUCTURE ---
        out.write("--- SUBSECTION ANALYSIS ---\n")
        # Find all A., B., C., D. subsections
        subsections = re.findall(r'(?:####\s*)?([A-G])\.\s+([A-Z][a-zA-Z\s\-/,]+)', content)
        out.write(f"MAJOR SUBSECTIONS (A-G): {len(subsections)}\n")
        for sub in subsections[:10]:  # First 10
            out.write(f"  {sub[0]}. {sub[1].strip()[:50]}\n")
        
        # --- TABLE ANALYSIS ---
        out.write("\n--- TABLE USAGE ---\n")
        # Find table captions
        table_captions = re.findall(r'(?:TABLE|Table)\s+([IVX]+|\d+)[:\.]?\s*([^\n|]+)', content)
        out.write(f"TABLES FOUND: {len(table_captions)}\n")
        for tc in table_captions[:5]:  # First 5
            out.write(f"  Table {tc[0]}: {tc[1].strip()[:60]}\n")
            
        # --- FIGURE ANALYSIS ---
        out.write("\n--- FIGURE USAGE ---\n")
        fig_captions = re.findall(r'(?:Fig\.|Figure)\s+(\d+)[:\.]?\s*([^\n]+)', content)
        out.write(f"FIGURES FOUND: {len(fig_captions)}\n")
        for fc in fig_captions[:5]:  # First 5
            out.write(f"  Fig {fc[0]}: {fc[1].strip()[:60]}\n")
        
        out.write("\n\n")
        
print("Analysis complete. Check analysis_body_deep_output.txt")
