"""
Quick Test Script: Deep Extraction & Verification (CoT) for Single Paper
========================================================================
Run in Colab/Local after setup.
"""

import os
import asyncio
import json
from groq import Groq
from extraction_pipeline_v3 import extract_single_paper, Config, CheckpointManager

# Mock Semaphore
class MockSemaphore:
    async def __aenter__(self):
        pass
    async def __aexit__(self, exc_type, exc, tb):
        pass

async def test_single(paper_id="O_ISAC_029"):
    
    # Setup Config if not already valid
    if not os.path.exists(Config.MARKDOWN_DIR):
        print("Config.MARKDOWN_DIR does not exist. Adjusting paths...")
        # (Assuming we are in the correct relative path context or Config handles it)
        pass

    # Get API Key
    try:
        from google.colab import userdata
        api_key = userdata.get('GROQ_API_KEY')
    except:
        api_key = os.environ.get('GROQ_API_KEY')

    if not api_key:
        print("[Warning] GROQ_API_KEY not found. Please set it.")
        return

    # Init Client (Groq/OpenAI compatible)
    client = Groq(api_key=api_key)
    
    # Run Extraction
    print(f"\n[TEST] CoT Deep Extraction on: {paper_id}")
    
    # Locate folder (Phase 2 logic in extraction_pipeline_v3 expects folder path)
    # We essentially need to simulate passing the folder where the paper is.
    paper_folder = os.path.join(Config.MARKDOWN_DIR, paper_id)
    if not os.path.exists(paper_folder):
        print(f"[Error] Folder not found for {paper_id} at {paper_folder}")
        return

    # Run
    semaphore = MockSemaphore()
    data = await extract_single_paper(client, paper_id, Config.MARKDOWN_DIR, semaphore)
    
    if data:
        print("\n[Success] Extraction Success!")
        print(json.dumps(data, indent=2))
        
        # Save
        out_path = f"test_{paper_id}_CoT.json"
        with open(out_path, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"\n[Saved] to {out_path}")
    else:
        print("\n[Failed] Extraction Failed.")

if __name__ == "__main__":
    asyncio.run(test_single("O_ISAC_029"))
