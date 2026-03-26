
import os
import re

base_path = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\corpus_standardized"
# Select 10 papers for taxonomy analysis (mix of recent and established)
papers = [f"COMST_{i:03d}" for i in [1, 5, 10, 14, 15, 20, 60, 62, 65, 70]]
output_file = "analysis_taxonomy_output.txt"

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
        
        # 1. Find section headers that look like taxonomy/classification
        # Common patterns: "TAXONOMY", "CLASSIFICATION", "CATEGORIZATION", or numbered sections III, IV, V
        taxonomy_headers = re.findall(r'(?:#+\s*|\b)(?:II\.|III\.|IV\.|V\.)\s*([A-Z][A-Z\s,/-]+)', content)
        if taxonomy_headers:
            out.write(f"MAIN SECTION HEADERS: {taxonomy_headers[:5]}\n")
        
        # 2. Count subsection depth (A., B., C. or 1., 2., 3.)
        subsections = re.findall(r'(?:####\s*)?([A-D]\.|[1-4]\.)\s+([A-Z][a-zA-Z\s-]+)', content)
        out.write(f"SUBSECTION COUNT: {len(subsections)}\n")
        if subsections:
            out.write(f"SUBSECTION SAMPLES: {subsections[:5]}\n")
        
        # 3. Count tables in the document
        tables = re.findall(r'TABLE\s+[IVX]+|Table\s+\d+|\|.*\|.*\|', content)
        out.write(f"TABLE MENTIONS: {len(tables)}\n")
        
        # 4. Check for taxonomy diagram mentions
        if "taxonomy" in content.lower() or "classification" in content.lower():
            out.write("TAXONOMY/CLASSIFICATION MENTIONED: Yes\n")
        else:
            out.write("TAXONOMY/CLASSIFICATION MENTIONED: No\n")
            
        # 5. Find opening sentence pattern of main body section
        # Look for "In this section" or "This section presents"
        section_openers = re.findall(r'(?:In this section|This section (?:presents|provides|discusses|introduces))[^.]+\.', content)
        if section_openers:
            out.write(f"SECTION OPENER PATTERN: {section_openers[0][:150]}...\n")
        
        out.write("\n")
