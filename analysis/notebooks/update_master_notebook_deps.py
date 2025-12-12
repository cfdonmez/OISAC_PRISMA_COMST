import json
import os

NOTEBOOK_PATH = r"g:\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\analysis\notebooks\CoT_Master_Pipeline.ipynb"

def update_notebook():
    if not os.path.exists(NOTEBOOK_PATH):
        print(f"[ERROR] Notebook not found at {NOTEBOOK_PATH}")
        return

    try:
        with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except Exception as e:
        print(f"[ERROR] Error reading notebook: {e}")
        return

    updated_deps = False
    updated_secrets = False

    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = cell['source']
            source_str = "".join(source)

            # Update 1.1 Install Dependencies
            if "# @title 1.1 Install Dependencies" in source_str:
                if "google-generativeai" not in source_str:
                    new_source = []
                    added = False
                    for line in source:
                        new_source.append(line)
                        if "!pip install groq" in line and not added:
                            new_source.append("!pip install -q -U google-generativeai\n")
                            added = True
                    if not added: 
                         new_source.append("!pip install -q -U google-generativeai\n")
                    
                    cell['source'] = new_source
                    updated_deps = True
                    print("[OK] Added google-generativeai dependency")

            # Update 1.3 Load API Key
            if "# @title 1.3 Load API Key" in source_str:
                if "GOOGLE_API_KEY" not in source_str:
                    new_source = []
                    for line in source:
                        new_source.append(line)
                        if "os.environ[\"GROQ_API_KEY\"]" in line:
                            new_source.append("    os.environ[\"GOOGLE_API_KEY\"] = userdata.get('GOOGLE_API_KEY')\n")
                        if "print(f\"🔑 GROQ Key:" in line:
                             new_source.append("    print(f\"🔑 GOOGLE Key: {'Set' if os.environ.get('GOOGLE_API_KEY') else 'Not Set'}\")\n")
                    
                    cell['source'] = new_source
                    updated_secrets = True
                    print("[OK] Added GOOGLE_API_KEY loading logic")

    if updated_deps or updated_secrets:
        try:
            with open(NOTEBOOK_PATH, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=None)
            print("[INFO] Notebook updated successfully.")
        except Exception as e:
            print(f"[ERROR] Error saving notebook: {e}")
    else:
        print("[INFO] Notebook already up to date.")

if __name__ == "__main__":
    update_notebook()
