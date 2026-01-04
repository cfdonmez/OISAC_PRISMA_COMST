import json
import os
import shutil
from pathlib import Path
from tqdm import tqdm

# Configuration
# Use raw strings and ensure we can construct long paths
PROJECT_ROOT = Path(r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST")
MANIFEST_PATH = PROJECT_ROOT / "data/corpus_manifest.json"
SOURCE_ROOT = PROJECT_ROOT / "data/processed_markdowns_comstPrev"
TARGET_ROOT = PROJECT_ROOT / "data/corpus_standardized"

def make_long_path(path_str):
    """
    On Windows, prepend \\?\ to absolute path to handle >260 chars.
    """
    if os.name == 'nt':
        # Ensure it is absolute
        abs_path = os.path.abspath(path_str)
        if not abs_path.startswith("\\\\?\\"):
            return "\\\\?\\" + abs_path
    return path_str

def standardize_corpus():
    if not MANIFEST_PATH.exists():
        print("Manifest not found.")
        return

    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # Create target root
    TARGET_ROOT.mkdir(parents=True, exist_ok=True)
    
    print(f"Standardizing {len(manifest)} papers into {TARGET_ROOT}...")
    
    success_count = 0
    
    for entry in tqdm(manifest):
        paper_id = entry["paper_id"]
        
        # We construct the source folder path manually from SOURCE_ROOT and folder_name key
        # Using the manifest md_path is risky if it was truncated or if standard open() fails.
        
        raw_source_folder = SOURCE_ROOT / entry["folder_name"]
        
        # Use long path syntax for checking existence and globbing
        long_source_folder_str = make_long_path(str(raw_source_folder))
        
        # We need to operate with Path objects or strings. 
        # Path(long_source_folder_str).exists() might work depending on python version.
        # But os.listdir(long_source_folder_str) definitely works.
        
        if not os.path.exists(long_source_folder_str):
            print(f"Skipping {paper_id}: Source folder not found: {long_source_folder_str}")
            entry["qa_status"] = "missing_source"
            continue
            
        # Create Target Folder: data/corpus_standardized/COMST_XXX/
        target_folder = TARGET_ROOT / paper_id
        target_folder.mkdir(exist_ok=True)
        
        # New MD Path
        target_md_path = target_folder / f"{paper_id}.md"
        
        try:
            # Find MD file in source manually (glob on Path object might fail with long path)
            # Use os.scandir or os.listdir on the long path string
            items = os.listdir(long_source_folder_str)
            md_files = [f for f in items if f.endswith(".md")]
            
            if not md_files:
                 print(f"Skipping {paper_id}: No MD file in {entry['folder_name']}")
                 continue
                 
            source_md_filename = md_files[0]
            source_md_path_str = os.path.join(long_source_folder_str, source_md_filename)
            
            # Copy MD File
            shutil.copy2(source_md_path_str, str(target_md_path))
            
            # Copy specific allowed image assets
            allowed_exts = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
            for item in items:
                _, ext = os.path.splitext(item)
                if ext.lower() in allowed_exts:
                    src_img = os.path.join(long_source_folder_str, item)
                    dst_img = target_folder / item
                    shutil.copy2(src_img, str(dst_img))
            
            # Update Manifest
            entry["md_path"] = str(target_md_path.absolute())
            entry["status"] = "standardized"
            entry["qa_status"] = "ready_for_qa" # Reset status
            
            success_count += 1
            
        except Exception as e:
            print(f"Error processing {paper_id}: {e}")
            entry["notes"] = f"Standardization failed: {str(e)}"

    # Save Updated Manifest
    with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=4)
        
    print(f"Standardization Complete. {success_count}/{len(manifest)} papers processed.")
    print(f"Updated manifest saved to {MANIFEST_PATH}")

if __name__ == "__main__":
    standardize_corpus()
