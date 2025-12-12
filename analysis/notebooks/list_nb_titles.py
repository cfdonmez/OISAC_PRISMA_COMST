import json
import os

NOTEBOOK_PATH = r"g:\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\analysis\notebooks\CoT_Master_Pipeline.ipynb"

def list_titles():
    if not os.path.exists(NOTEBOOK_PATH):
        print("Notebook not found")
        return

    with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    for cell in nb['cells']:
        source = "".join(cell['source'])
        if "# @title" in source:
            print(source.split('\n')[0].strip())

if __name__ == "__main__":
    list_titles()
