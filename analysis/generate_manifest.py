import os
import json
import re
from pathlib import Path
from tqdm import tqdm

# Configuration
MARKDOWN_ROOT = Path(r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns_comstPrev")
OUTPUT_MANIFEST = Path(r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\corpus_manifest.json")

def extract_metadata_from_md(md_path):
    """
    Attempts to extract metadata (Year, Real Title) from the first few lines of MD.
    """
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read(2000) # Read first 2000 chars
            
        # 1. Try to find Year (2018-2025)
        year_match = re.search(r'\b(20[12][0-9])\b', content)
        year = int(year_match.group(1)) if year_match else None
        
        # 2. Heuristic for Title (Usually the first H1 or first non-empty line)
        title = None
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('# '):
                title = line[2:].strip()
                break
            if not title and len(line) > 10 and not line.startswith('!['):
                title = line # Fallback to first text line
                
        return year, title
    except Exception as e:
        print(f"Error reading {md_path}: {e}")
        return None, None

def generate_manifest():
    if not MARKDOWN_ROOT.exists():
        print(f"Error: Directory {MARKDOWN_ROOT} not found.")
        return

    manifest = []
    
    # Get all subdirectories sorted alphabetically to ensure stable ID assignment
    subdirs = sorted([d for d in MARKDOWN_ROOT.iterdir() if d.is_dir()])
    
    print(f"Found {len(subdirs)} folders. Generating manifest...")
    
    for idx, folder in enumerate(tqdm(subdirs)):
        # Generate ID: COMST_001, COMST_002...
        paper_id = f"COMST_{idx+1:03d}"
        
        # Find the MD file (heuristic: ends with .md and likely matches folder name)
        md_files = list(folder.glob("*.md"))
        
        if not md_files:
            print(f"Warning: No MD file found in {folder.name}")
            continue
            
        # Pick the largest MD file if multiple (unlikely) or just the first
        md_file = md_files[0]
        
        # Extract metadata
        year, extracted_title = extract_metadata_from_md(md_file)
        
        # Use Folder Name as fallback Title if extraction fails
        final_title = extracted_title if extracted_title else folder.name
        
        entry = {
            "paper_id": paper_id,
            "title": final_title,
            "folder_name": folder.name,
            "year": year if year else "Unknown",
            "md_path": str(md_file.absolute()),
            "pdf_path_predicted": f"data/comstPrev/{folder.name}.pdf", # Prediction
            "status": "converted",
            "notes": ""
        }
        
        manifest.append(entry)
        
    # Save Manifest
    with open(OUTPUT_MANIFEST, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=4)
        
    print(f"Manifest saved to {OUTPUT_MANIFEST} with {len(manifest)} entries.")

if __name__ == "__main__":
    generate_manifest()
