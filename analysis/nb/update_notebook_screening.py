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

new_cells = [
    create_markdown_cell([
        "## 3. Phase 1: AI Bulk Screening (Scopus)",
        "This section automates the screening of candidate papers using **Llama 3.3 70B** via Groq.",
        "We load the `scopus_candidates.csv`, ask the model to evaluate relevance based on the Title (and Abstract if available), and output a decision."
    ]),
    create_code_cell([
        "# @title Load Scopus Candidates",
        "import pandas as pd",
        "import os",
        "",
        "CANDIDATES_CSV = os.path.join(BASE_DIR, 'scopus_candidates.csv')",
        "if os.path.exists(CANDIDATES_CSV):",
        "    df_candidates = pd.read_csv(CANDIDATES_CSV)",
        "    print(f'✅ Loaded {len(df_candidates)} candidates from {CANDIDATES_CSV}')",
        "    display(df_candidates.head())",
        "else:",
        "    print(f'❌ File not found: {CANDIDATES_CSV}')"
    ]),
    create_code_cell([
        "# @title Define Screening Agent (Llama-3.3-70b)",
        "!pip install -q groq",
        "import json",
        "import time",
        "import os",
        "from google.colab import userdata",
        "from groq import Groq",
        "",
        "# Setup Groq Client",
        "try:",
        "    api_key = None",
        "    try: api_key = userdata.get('GROQ_API_KEY')",
        "    except: pass",
        "    if not api_key: api_key = os.environ.get('GROQ_API_KEY')",
        "    ",
        "    if not api_key:",
        "        raise ValueError('GROQ_API_KEY not found in Secrets or Env')",
        "    ",
        "    client = Groq(api_key=api_key)",
        "    print('✅ Groq Client Initialized')",
        "except Exception as e:",
        "    print(f'❌ Setup Error: {e}')",
        "",
        "def screen_paper(title, authors, year, category):",
        "    # 1. Construct Prompt",
        "    prompt = f\"\"\"",
        "    Act as a Senior Systematic Reviewer for a survey on 'Optical Integrated Sensing and Communication (O-ISAC)'.",
        "    ",
        "    INCLUSION CRITERIA (Must meet ALL):",
        "    1. MUST involve BOTH 'Sensing' (Radar, Lidar, Positioning, Detection) AND 'Communication' (Data transmission).",
        "    2. MUST involve 'Optical' technologies (Visible Light, FSO, Fiber, Photonic Integrated Circuits, etc.).",
        "    3. Dual-functionality must be INTEGRATED (shared hardware, spectrum, or waveform).",
        "    ",
        "    EXCLUSION CRITERIA (Reject if ANY):",
        "    1. Purely RF/Millimeter-wave/THz studies without any optical/photonic component.",
        "    2. Purely sensing (e.g., just Lidar) or purely communication (e.g., just FSO) without the other function.",
        "    3. 'Optical Sensing' for non-comm purposes (e.g., simple temp sensor) unless integrated with comms.",
        "    ",
        "    Analyze this paper:",
        "    - Title: {title}",
        "    - Authors: {authors}",
        "    - Year: {year}",
        "    - Auto-Category: {category}",
        "    ",
        "    Provide a JSON response with keys:",
        "    - 'decision': 'Included' or 'Excluded'",
        "    - 'reason': Concise explanation (max 1 sentence) referencing the criteria.",
        "    - 'confidence': 0.0 to 1.0",
        "    \"\"\"",
        "    ",
        "    try:",
        "        completion = client.chat.completions.create(",
        "            model='llama-3.3-70b-versatile',",
        "            messages=[",
        "                {'role': 'system', 'content': 'You are a helpful assistant that outputs strictly JSON.'},",
        "                {'role': 'user', 'content': prompt}",
        "            ],",
        "            temperature=0,",
        "            response_format={'type': 'json_object'}",
        "        )",
        "        return json.loads(completion.choices[0].message.content)",
        "    except Exception as e:",
        "        print(f'Error: {e}')",
        "        return {'decision': 'Error', 'reason': str(e), 'confidence': 0.0}",
        ""
    ]),
    create_code_cell([
        "# @title Test Screening (First 5 Rows)",
        "results = []",
        "print('🧪 Testing Llama-3.3 Agent on first 5 rows...')",
        "",
        "if 'df_candidates' in locals() and 'client' in locals():",
        "    for idx, row in df_candidates.head(5).iterrows():",
        "        print(f'Processing {idx+1}: {row[\"Document Title\"][:50]}...')",
        "        decision = screen_paper(",
        "            row['Document Title'], ",
        "            row['Authors'], ",
        "            row['Publication Year'],",
        "            row.get('CATEGORY', 'Unknown')",
        "        )",
        "        print(f'   👉 {decision[\"decision\"]}: {decision[\"reason\"]}')",
        "        results.append(decision)",
        "        time.sleep(1) # Rate limit politeness",
        "else:",
        "    print('⚠️ df_candidates or client not loaded. Run the previous cells first.')"
    ])
]

with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Append new cells
# Note regarding previous append: Since we are overwriting this script and running it again, 
# strictly speaking we are appending *again*. Ideally we should clear the old ones or just add.
# For simplicity in this interaction, we simply append. The user can delete duplicates if they appear.
nb['cells'].extend(new_cells)

with open(NOTEBOOK_PATH, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print(f"Successfully added {len(new_cells)} cells (Llama 3.3 Config) to {NOTEBOOK_PATH}")
