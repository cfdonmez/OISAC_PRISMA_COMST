import json
import os

NOTEBOOK_PATH = r"g:\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\analysis\notebooks\CoT_Master_Pipeline.ipynb"

def update_notebook_text():
    if not os.path.exists(NOTEBOOK_PATH):
        print(f"[ERROR] Notebook not found at {NOTEBOOK_PATH}")
        return

    try:
        with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except Exception as e:
        print(f"[ERROR] Error reading notebook: {e}")
        return

    updated_count = 0

    replacements = {
        "BLIP + DePlot": "Gemini 1.5 Flash (Batched)",
        "BLIP": "Gemini 1.5 Flash",
        "DePlot": "Gemini 1.5 Flash",
        "transformers torch pillow": "google-generativeai pillow",
        "Phase 2: Visual Analysis (using BLIP and DePlot models)": "Phase 2: Visual Analysis (using Gemini 1.5 Flash)",
        "Phase 2: Visual Analysis (BLIP + DePlot)": "Phase 2: Visual Analysis (Gemini 1.5 Flash)"
    }

    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            source = cell['source']
            new_source = []
            cell_updated = False
            
            for line in source:
                new_line = line
                for old, new in replacements.items():
                    if old in new_line:
                        new_line = new_line.replace(old, new)
                        cell_updated = True
                new_source.append(new_line)
            
            if cell_updated:
                cell['source'] = new_source
                updated_count += 1

    if updated_count > 0:
        try:
            with open(NOTEBOOK_PATH, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=None)
            print(f"[INFO] Updated {updated_count} markdown cells manually.")
        except Exception as e:
            print(f"[ERROR] Error saving notebook: {e}")
    else:
        print("[INFO] No text updates needed.")

if __name__ == "__main__":
    update_notebook_text()
