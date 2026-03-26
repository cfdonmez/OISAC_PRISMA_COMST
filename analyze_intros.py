

import os
import re

base_path = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\corpus_standardized"
papers = ["COMST_016", "COMST_017", "COMST_018", "COMST_019", "COMST_020"]
output_file = "analysis_output.txt"

def clean_text(text):
    return re.sub(r'<[^>]+>', '', text).strip()

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
        
        # 1. FIND INTRODUCTION
        # Allow any characters (like spans) between # and Introduction
        intro_match = re.search(r'^(#+).*Introduction', content, re.MULTILINE | re.IGNORECASE)
        if intro_match:
            out.write("FOUND: Introduction Header\n")
            start_idx = intro_match.end()
            hook_chunk = content[start_idx:start_idx+800]
            clean_hook = clean_text(hook_chunk)
            out.write(f"HOOK START: {clean_hook[:300]}...\n")
        else:
            out.write("MISSING: Introduction Header\n")

        # 2. FIND GAP TABLE
        table_match = re.search(r'Table\s+[IVX0-9]+.*(?:compar|existing|survey)', content, re.IGNORECASE)
        if table_match:
            out.write(f"FOUND: Gap Table Ref: '{table_match.group(0)}'\n")
        else:
            if "comparison" in content.lower() and "survey" in content.lower():
                 out.write("FOUND: Gap Textual Reference (exact table tag not found)\n")
            else:
                 out.write("MISSING: Gap Comparison Table\n")

        # 3. FIND CONTRIBUTION
        contrib_match = re.search(r'(?:contributions|objectives).{0,50}summarized', content, re.IGNORECASE | re.DOTALL)
        if contrib_match:
            out.write("FOUND: Contribution List Introducer\n")
            start_idx = contrib_match.end()
            contrib_chunk = content[start_idx:start_idx+300]
            clean_contrib = clean_text(contrib_chunk)
            out.write(f"CONTRIBUTION START: {clean_contrib[:200]}...\n")
        else:
             out.write("MISSING: Contribution List Introducer\n")
        
        out.write("\n")

