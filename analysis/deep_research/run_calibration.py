import os
import glob
import json
import time

try:
    import google.generativeai as genai
    from google.colab import userdata
except ImportError:
    # Fallback for local testing if outside Colab
    pass

# CONFIG
PAPER_ID = "O_ISAC_029"
PDF_MARKDOWN_DIR = r"../../data/processed_markdowns"  # Relative path adjustment needed likely
SYSTEM_PROMPT_PATH = r"analysis/deep_research/config/system_prompt.md"
OUTPUT_DIR = r"analysis/deep_research/output"

def load_text(paper_id):
    # Try multiple base paths to accommodate different execution contexts (Colab root, module dir, etc.)
    base_paths = [
        "data/processed_markdowns",  # Run from project root (Notebook default)
        "../../data/processed_markdowns", # Run from analysis/deep_research/
        "/content/drive/MyDrive/AKU_WorkSpace/survey_fdgit/OISAC_PRISMA_COMST/data/processed_markdowns", # Colab Absolute
        r"g:\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns" # Local Absolute
    ]
    
    files = []
    for base in base_paths:
        search_path = os.path.join(base, paper_id, "**", "*.md")
        found = glob.glob(search_path, recursive=True)
        if found:
            files = found
            print(f"✅ Found paper text in: {base}")
            break
    
    if not files:
        raise FileNotFoundError(f"Markdown for {paper_id} not found. Checked paths: {base_paths}")
    
    with open(files[0], 'r', encoding='utf-8') as f:
        return f.read()

def load_system_prompt():
    prompt_path = os.path.abspath(SYSTEM_PROMPT_PATH)
    if not os.path.exists(prompt_path):
         # Helper for when running from various CWDs
         prompt_path = r"g:\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\analysis\deep_research\config\system_prompt.md"
    
    with open(prompt_path, 'r', encoding='utf-8') as f:
        return f.read()

def run_research_agent():
    print(f"🕵️‍♂️ Deep Research Agent - Calibration Mode: {PAPER_ID}")
    
    # 1. Setup API
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        try:
            api_key = userdata.get('GOOGLE_API_KEY')
        except:
            print("❌ GOOGLE_API_KEY not found in env.")
            return

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash') # Use the newly migrated model
    
    # 2. Load Content
    try:
        paper_text = load_text(PAPER_ID)
        system_role = load_system_prompt()
        print(f"✅ Loaded Paper Text ({len(paper_text)} chars)")
        print(f"✅ Loaded System Role")
    except Exception as e:
        print(f"❌ Error loading files: {e}")
        return

    # 3. Construct Prompt
    # Combining System Role implied as instruction for this interaction
    full_prompt = f"""{system_role}

---
TARGET TEXT TO ANALYZE:
{paper_text[:100000]} 

(Text truncated to 100k chars for safety, though Gemini context is larger)
---

Generate the Evidence Package now.
"""
    
    # 4. Generate
    print("⏳ Agent Thinking...")
    try:
        response = model.generate_content(full_prompt)
        output_text = response.text
        print("✅ Analysis Complete.")
    except Exception as e:
        print(f"❌ API Error: {e}")
        return

    # 5. Save Evidence Package
    output_filename = f"{PAPER_ID}_DeepResearch_Evidence.md"
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    # Handle abs path if needed
    if not os.path.exists(os.path.dirname(output_path)):
         output_path = os.path.join(r"g:\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST", output_path)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_text)
    
    print(f"💾 Evidence Package saved to: {output_path}")

if __name__ == "__main__":
    run_research_agent()
