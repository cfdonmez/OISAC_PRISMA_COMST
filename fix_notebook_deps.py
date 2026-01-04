import json
import os

NOTEBOOK_PATH = r"analysis/notebooks/CoT_Pipeline_comstPrev.ipynb"

# Define the new cell contents for 1.1
cell_1_1_new = [
    "# @title 1.1 Install Dependencies\n",
    "# Phase 1 & 2 dependencies\n",
    "print('🔄 Cleaning up and installing marker-pdf...')\n",
    "!pip uninstall -y marker marker-pdf numpy -q\n",
    "# Pin numpy to <2.0 because Numba/Marker often fail with 2.0+\n",
    "!pip install \"numpy<2.0\" -q\n",
    "!pip install marker-pdf --upgrade --force-reinstall -q\n",
    "!pip install transformers torch pillow -q\n",
    "\n",
    "# Phase 3 & V4 Engine dependencies\n",
    "!pip install groq nest_asyncio pandas pyyaml -q\n",
    "!pip install -q -U google-generativeai\n",
    "\n",
    "print(\"✅ Tüm bağımlılıklar yüklendi! Lütfen Runtime > Restart Session yapmayı unutmayın.\")"
]

# Load Notebook
with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells_modified = 0

for cell in nb['cells']:
    if cell['cell_type'] != 'code':
        continue
    
    src = cell.get('source', [])
    if not src: continue
    
    first_line = src[0]
    
    if "# @title 1.1" in first_line:
        print("Found Cell 1.1 - Applying dependency fix...")
        cell['source'] = cell_1_1_new
        cells_modified += 1

print(f"Total cells modified: {cells_modified}")

with open(NOTEBOOK_PATH, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook saved successfully.")
