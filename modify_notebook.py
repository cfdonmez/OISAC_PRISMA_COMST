import json
import os

NOTEBOOK_PATH = r"analysis/notebooks/CoT_Pipeline_comstPrev.ipynb"

# Cell 1.2 is already correct in the notebook (defines paths), but we keep it here for reference/completeness if needed.
# We are primarily focusing on fixing 2.1 and 4.1 where the overrides happen.

cell_2_1_new = [
    "# @title 2.1 Import & Status Check\n",
    "import extraction_pipeline_v3 as v3\n",
    "from extraction_pipeline_v3 import Config\n",
    "import importlib\n",
    "import glob\n",
    "\n",
    "# FORCE RELOAD V3\n",
    "importlib.reload(v3)\n",
    "\n",
    "# --- OVERRIDE FOR COMST PREV ---\n",
    "# CRITICAL FIX: Modify the Config object ON THE RELOADED MODULE\n",
    "v3.Config.PDF_DIR = PDF_DIR\n",
    "v3.Config.MARKDOWN_DIR = MARKDOWN_DIR\n",
    "v3.Config.OUTPUT_DIR = os.path.join(PROJECT_ROOT, \"data/extraction_results_comstPrev_v3\")\n",
    "v3.Config.CHECKPOINT_FILE = os.path.join(v3.Config.OUTPUT_DIR, \"checkpoint.json\")\n",
    "\n",
    "print(f\"🔧 Config Overridden for ComstPrev:\")\n",
    "print(f\"   Input: {v3.Config.PDF_DIR}\")\n",
    "print(f\"   Output: {v3.Config.OUTPUT_DIR}\")\n",
    "\n",
    "# Initialize\n",
    "v3.Config.init_dirs()\n",
    "checkpoint = v3.CheckpointManager(v3.Config.CHECKPOINT_FILE)\n",
    "\n",
    "# Show status\n",
    "processed_count = len(checkpoint.data.get('processed', {}))\n",
    "pdf_count = len(glob.glob(os.path.join(v3.Config.PDF_DIR, '*.pdf')))\n",
    "\n",
    "print(f\"📊 PDF Durumu: {pdf_count} toplam, {processed_count} işlenmiş.\")"
]

cell_4_1_new = [
    "# @title 4.1 Import V4 Engine\n",
    "import extraction_pipeline_v4 as v4\n",
    "from extraction_pipeline_v4 import ConfigV4\n",
    "import importlib\n",
    "\n",
    "importlib.reload(v4)\n",
    "\n",
    "# --- OVERRIDE FOR COMST PREV ---\n",
    "# CRITICAL FIX: Modify the Config object ON THE RELOADED MODULE\n",
    "v4.ConfigV4.OUTPUT_DIR = OUTPUT_DIR_V4\n",
    "\n",
    "# Init V4 environment\n",
    "v4.ConfigV4.init_dirs()\n",
    "v4_checkpoint = v4.CheckpointManager(os.path.join(v4.ConfigV4.OUTPUT_DIR, \"checkpoint_v4.json\"))\n",
    "\n",
    "print(\"✅ V4 Engine (Factory) Hazır!\")\n",
    "print(f\"📂 V4 Çıktı Hedefi: {v4.ConfigV4.OUTPUT_DIR}\")"
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
    
    if "# @title 2.1" in first_line:
        print("Found Cell 2.1 - Applying Fix")
        cell['source'] = cell_2_1_new
        cells_modified += 1
        
    if "# @title 4.1" in first_line:
        print("Found Cell 4.1 - Applying Fix")
        cell['source'] = cell_4_1_new
        cells_modified += 1

print(f"Total cells modified: {cells_modified}")

with open(NOTEBOOK_PATH, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook saved successfully.")
