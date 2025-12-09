import os
import sys
import json

# Add the project root to sys.path to allow imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.append(project_root)

from analysis.cot_laboratory.core.assembler import CoTAssembler

def main():
    # 1. Setup Paths
    paper_path = os.path.join(project_root, "data", "processed_markdowns", "O_ISAC_029", "O_ISAC_029", "O_ISAC_029.md")
    vis_path = os.path.join(project_root, "data", "processed_markdowns", "O_ISAC_029", "O_ISAC_029", "visual_analysis.txt")
    recipe_path = "analysis/cot_laboratory/recipes/experiment_v1_full_analysis.yaml"
    
    # 2. Read Paper Content
    print(f"[INFO] Reading Paper: {paper_path}...")
    try:
        with open(paper_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("[ERROR] Paper file not found!")
        return

    # 3. Read Visual Content (if exists)
    visual_content = None
    if os.path.exists(vis_path):
        with open(vis_path, "r", encoding="utf-8") as f:
            visual_content = f.read()
        print(f"[INFO] Found Visual Analysis Data ({len(visual_content)} chars)")
    else:
        print("[INFO] No Visual Analysis Data found.")

    # 4. Initialize Assembler
    print("[INFO] Initializing CoT Assembler...")
    try:
        assembler = CoTAssembler(project_root)
    except Exception as e:
         print(f"[ERROR] Init Failed: {str(e)}")
         return
    
    # 5. Run Extraction
    print("[INFO] Starting Extraction Run...")
    try:
        result = assembler.run_extraction(
            recipe_path, 
            content, 
            paper_id="O_ISAC_029",
            visual_content=visual_content
        )
    except Exception as e:
        print(f"[ERROR] Extraction Exception: {e}")
        return
    
    # 6. Show Results
    if result["status"] == "success":
        print("\n[SUCCESS] Extraction Successful!")
        print("-" * 50)
        
        # Show the Reasoning Trace first
        trace = result["parsed_output"].get("reasoning_trace", [])
        print("[RESULT] REASONING TRACE FOUND:")
        print(json.dumps(trace, indent=2, ensure_ascii=False))
        
        print("\n[RESULT] Study Data (Snippet):")
        study_level = result["parsed_output"].get("study_level", {})
        print(json.dumps(study_level, indent=2, ensure_ascii=False)[:700] + "...")
        
    else:
        print(f"\n[FAIL] Extraction Failed: {result.get('error_message')}")

if __name__ == "__main__":
    main()
