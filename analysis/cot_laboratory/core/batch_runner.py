import os
import sys
import glob
import time
from typing import List

# Setup project root for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
sys.path.append(project_root)

from analysis.cot_laboratory.core.assembler import CoTAssembler

class CoTFactory:
    """
    The Factory Line Manager.
    Iterates through the data warehouse (processed_markdowns) 
    and feeds papers into the Engine (Assembler).
    """
    
    def __init__(self, project_root: str):
        self.project_root = project_root
        self.assembler = CoTAssembler(project_root)
        print(f"[FACTORY] Initialized at {project_root}")

    def get_pending_papers(self) -> List[str]:
        """
        Scans for papers that haven't been processed yet.
        Returns a list of folder paths.
        """
        data_dir = os.path.join(self.project_root, "data", "processed_markdowns")
        # Pattern: data/processed_markdowns/O_ISAC_XXX/O_ISAC_XXX/O_ISAC_XXX.md
        # Or simpler: Just find all .md files in that tree that match O_ISAC_*.md
        
        print("[FACTORY] Scanning for papers...")
        # Recursive glob to valid papers
        search_pattern = os.path.join(data_dir, "**", "O_ISAC_*.md")
        all_candidates = glob.glob(search_pattern, recursive=True)
        
        print(f"[FACTORY] Found {len(all_candidates)} markdown files candidates.")
        return all_candidates

    def run_batch(self, recipe_path: str):
        """
        Main production loop.
        """
        papers = self.get_pending_papers()
        total = len(papers)
        
        print(f"🏭 STARTING BATCH PRODUCTION: {total} Papers")
        print(f"📜 Recipe: {recipe_path}")
        print("="*60)
        
        success_count = 0
        fail_count = 0
        
        for index, paper_path in enumerate(papers):
            # Extract ID from filename (O_ISAC_029.md -> O_ISAC_029)
            filename = os.path.basename(paper_path)
            paper_id = os.path.splitext(filename)[0]
            
            print(f"\n[{index+1}/{total}] Processing {paper_id}...")
            
            try:
                # Read Content
                with open(paper_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if empty
                if not content.strip():
                    print(f"⚠️ SKIPPING {paper_id}: File is empty.")
                    fail_count += 1
                    continue

                # Check for Visual Analysis Data (DePlot/BLIP output)
                paper_dir = os.path.dirname(paper_path)
                visual_path = os.path.join(paper_dir, "visual_analysis.txt")
                visual_content = None
                
                if os.path.exists(visual_path):
                    with open(visual_path, 'r', encoding='utf-8') as vf:
                        visual_content = vf.read()
                    print(f"   🖼️ Found Visual Analysis Data ({len(visual_content)} chars)")

                # Run Assembly & Extraction
                result = self.assembler.run_extraction(
                    recipe_path, 
                    content, 
                    paper_id=paper_id, 
                    visual_content=visual_content
                )
                
                if result.get("status") == "success":
                    print(f"✅ SUCCESS: {paper_id}")
                    success_count += 1
                else:
                    print(f"❌ FAILED: {paper_id} - {result.get('error_message')}")
                    fail_count += 1
                    
                # Nap to be polite to API rate limits
                time.sleep(1) 
                
            except Exception as e:
                print(f"💥 CRITICAL ERROR on {paper_id}: {str(e)}")
                fail_count += 1
        
        print("="*60)
        print(f"🏁 BATCH COMPLETE.")
        print(f"✅ Success: {success_count}")
        print(f"❌ Failed:  {fail_count}")

if __name__ == "__main__":
    # Ensure API Key is present
    if not os.getenv("GROQ_API_KEY"):
         print("❌ ERROR: GROQ_API_KEY not set. Please set it before running the factory.")
         sys.exit(1)

    factory = CoTFactory(project_root)
    # Default Recipe
    recipe = "analysis/cot_laboratory/recipes/experiment_v1_full_analysis.yaml"
    factory.run_batch(recipe)
