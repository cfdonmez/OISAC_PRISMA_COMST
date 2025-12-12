import json
import os
import sys

# Force UTF-8 for stdout
sys.stdout.reconfigure(encoding='utf-8')

NOTEBOOK_PATH = r"g:\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\analysis\notebooks\CoT_Master_Pipeline.ipynb"

def list_titles():
    if not os.path.exists(NOTEBOOK_PATH):
        print("Notebook not found")
        return

    try:
        with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except Exception as e:
        print(f"Error reading notebook: {e}")
        return

    for cell in nb['cells']:
        source = "".join(cell['source'])
        if "# @title" in source:
            title = source.split('\n')[0].strip()
            print(title)

if __name__ == "__main__":
    list_titles()
