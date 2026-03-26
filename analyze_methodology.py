
import os
import re

base_path = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\corpus_standardized"
# Analyze a mix of papers (recent and older) to catch trends
papers = [f"COMST_{i:03d}" for i in range(1, 21)] + [f"COMST_{i:03d}" for i in range(60, 65)]
output_file = "analysis_methodology_output.txt"

def clean_text(text):
    text = re.sub(r'<[^>]+>', '', text)
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
        
        # 1. Check for "PRISMA" mention (Case insensitive)
        if "prisma" in content.lower():
            out.write("PRISMA MENTIONED: YES\n")
        else:
            out.write("PRISMA MENTIONED: NO\n")
            
        # 2. Look for "Methodology", "Search Strategy", "Data Collection" headers
        # Regex for headers like "II. METHODOLOGY", "III. SEARCH STRATEGY", "SURVEY SCOPE"
        header_pattern = r'(?:#+\s*|\b)(?:II\.|III\.|IV\.)?\s*(METHODOLOGY|SURVEY SCOPE|SEARCH STRATEGY|DATA COLLECTION|REVIEW PROCESS)(.*?)(?:#+\s*(?:II\.|III\.|IV\.)|$)'
        match = re.search(header_pattern, content, re.DOTALL | re.IGNORECASE)
        
        if match:
            title = match.group(1)
            text = clean_text(match.group(2))
            out.write(f"SECTION FOUND: {title}\n")
            out.write(f"CONTENT PREVIEW: {text[:400]}...\n")
        else:
            out.write("SECTION FOUND: None explicit (Likely integrated in Intro or Scope)\n")
            
        out.write("\n")
