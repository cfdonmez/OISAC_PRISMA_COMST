import json
import os

NOTEBOOK_PATH = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\analysis\notebooks\Deep_Research_Agent_Lab.ipynb"

def create_code_cell(source_lines):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in source_lines]
    }

def create_markdown_cell(source_lines):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in source_lines]
    }

# Cells to Append
new_cells = [
    create_markdown_cell([
        "## 4. Phase 3: Extraction (O-ISAC Pipeline)",
        "This section processes the `extraction_queue.csv` (newly included studies) to generate the final dataset.",
        "Steps:",
        "1. Install Dependencies (Marker for PDF->MD).",
        "2. Convert PDFs to Markdown.",
        "3. Run Deep Extraction with Schema v2.1."
    ]),
    create_code_cell([
        "# @title 1. Install Extraction Dependencies",
        "!pip install -q marker-pdf",
        "!pip install -q groq",
        "print('✅ Dependencies installed.')"
    ]),
    create_code_cell([
        "# @title 2. PDF to Markdown Conversion (Marker)",
        "import os",
        "import glob",
        "import subprocess",
        "from tqdm.notebook import tqdm",
        "",
        "PDF_DIR = os.path.join(BASE_DIR, 'data/retrieved_docs')",
        "MARKDOWN_DIR = os.path.join(BASE_DIR, 'data/processed_markdowns')",
        "os.makedirs(MARKDOWN_DIR, exist_ok=True)",
        "",
        "# Filter for papers in the queue",
        "import pandas as pd",
        "QUEUE_FILE = os.path.join(BASE_DIR, 'analysis/phase2_extraction/extraction_queue.csv')",
        "if os.path.exists(QUEUE_FILE):",
        "    queue_df = pd.read_csv(QUEUE_FILE)",
        "    target_mode = True",
        "    target_ids = set(queue_df['Track_ID'].astype(str).str.strip())",
        "    print(f'🎯 Targeting {len(target_ids)} papers from Queue.')",
        "else:",
        "    target_mode = False",
        "    print('⚠️ Queue file not found. Processing ALL PDFs in retrieved_docs.')",
        "",
        "pdf_files = glob.glob(os.path.join(PDF_DIR, '*.pdf'))",
        "to_process = []",
        "",
        "for pdf_path in pdf_files:",
        "    pid = os.path.splitext(os.path.basename(pdf_path))[0]",
        "    # Check if needs processing",
        "    # 1. Is it in target list? (if mode is on)",
        "    if target_mode and pid not in target_ids: continue",
        "    ",
        "    # 2. output exists?",
        "    out_dir = os.path.join(MARKDOWN_DIR, pid)",
        "    if not os.path.exists(out_dir):",
        "         to_process.append(pdf_path)",
        "",
        "print(f'📋 Found {len(to_process)} PDFs to convert.')",
        "",
        "for pdf_path in tqdm(to_process):",
        "    pid = os.path.splitext(os.path.basename(pdf_path))[0]",
        "    out_dir = os.path.join(MARKDOWN_DIR, pid)",
        "    ",
        "    cmd = [",
        "        'marker_single', pdf_path,",
        "        '--output_dir', out_dir,",
        "        '--paginate_output'",
        "    ]",
        "    # Run silently",
        "    try:",
        "       subprocess.run(cmd, check=True, capture_output=True)",
        "    except subprocess.CalledProcessError as e:",
        "       print(f'❌ Error converting {pid}: {e}')"
    ]),
    create_markdown_cell([
        "### 3. Run LLM Extraction (Deep Extraction)",
        "Loads the Markdown, feeds it to Llama 3.3 / Gemini, and fills the Schema."
    ]),
    create_code_cell([
        "# @title Load Schema & Prompt",
        "SCHEMA_FILE = os.path.join(BASE_DIR, 'analysis/oisac_extraction_schema_v2.yaml')",
        "if os.path.exists(SCHEMA_FILE):",
        "    with open(SCHEMA_FILE, 'r') as f:",
        "        offset = f.read()",
        "        print('✅ Schema Loaded')",
        "else:",
        "    print('❌ Schema file not found!')"
        "",
        "SYSTEM_PROMPT = '''You are a Senior Technical Editor.''' # (Simplified for brevity in injection, relying on definition in cell above or reloading from file)",
        "# Ideally we load the extraction prompt from file too or define it here.",
        "# Let's define the Schema injection logic here for simplicity.",
        "pass"
    ]),
    create_code_cell([
        "# @title 🚀 Execute Batch Extraction Agent",
        "import json",
        "import time",
        "from groq import Groq",
        "from google.colab import userdata",
        "",
        "# Setup Groq",
        "try:",
        "    client = Groq(api_key=userdata.get('GROQ_API_KEY'))",
        "except:",
        "    client = Groq(api_key=os.environ.get('GROQ_API_KEY'))",
        "",
        "RESULTS_FILE = os.path.join(BASE_DIR, 'analysis/phase2_extraction/extraction_dataset.csv')",
        "# Logic to read markdown, prompt LLM, save row to CSV",
        "# ... (Simplified placeholder for the full logic found in pipeline_v3)",
        "print('⚠️  NOTE: Ensure you have copied the full extraction logic from extraction_pipeline_v3.py if this cell is not enough.')"
    ])
]

# Load Notebook
with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Append cells
nb['cells'].extend(new_cells)

# Save
with open(NOTEBOOK_PATH, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)

print(f"✅ Notebook updated with {len(new_cells)} new cells!")
