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

new_cells = [
    create_code_cell([
        "# @title 🚀 Phase 2: RUN FULL BATCH (226 Items)",
        "import csv",
        "from tqdm.notebook import tqdm",
        "",
        "OUTPUT_FILE = os.path.join(BASE_DIR, 'analysis/phase1_screening/ai_screening_decisions_scopus.csv')",
        "",
        "print(f'🚀 Starting Bulk Screening for {len(df_candidates)} papers using Llama 3.3...')",
        "",
        "# Initialize Output File (Write Header)",
        "with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:",
        "    writer = csv.writer(f)",
        "    writer.writerow(['Track_ID', 'Title', 'Decision', 'Reason', 'Confidence'])",
        "",
        "included_count = 0",
        "",
        "for idx, row in tqdm(df_candidates.iterrows(), total=len(df_candidates)):",
        "    track_id = row.get('Track_ID', f'TEMP_{idx}')",
        "    title = row['Document Title']",
        "    ",
        "    # Run Screening Agent",
        "    try:",
        "        decision_data = screen_paper(",
        "            title, ",
        "            row['Authors'], ",
        "            row['Publication Year'],",
        "            row.get('CATEGORY', 'Unknown')",
        "        )",
        "        ",
        "        # Visual Feedback for Included items",
        "        if decision_data['decision'] == 'Included':",
        "            print(f'✅ [INCLUDED] {title[:60]}...')",
        "            included_count += 1",
        "        else:",
        "            # Optional: Print excluded too if verbose, but keeping it clean",
        "            pass",
        "            ",
        "        # Save Result Immediately",
        "        with open(OUTPUT_FILE, 'a', newline='', encoding='utf-8') as f:",
        "            writer = csv.writer(f)",
        "            writer.writerow([",
        "                track_id, ",
        "                title, ",
        "                decision_data['decision'], ",
        "                decision_data['reason'], ",
        "                decision_data.get('confidence', 0.0)",
        "            ])",
        "            ",
        "    except Exception as e:",
        "        print(f'❌ Error on {track_id}: {e}')",
        "    ",
        "    # Rate limit politeness (Groq is fast)",
        "    time.sleep(0.2)",
        "",
        "print('='*40)",
        "print(f'🏁 Batch Complete! Results saved to: {OUTPUT_FILE}')",
        "print(f'📊 Total Included Candidates: {included_count} / {len(df_candidates)}')"
    ])
]

with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Append new cells
nb['cells'].extend(new_cells)

with open(NOTEBOOK_PATH, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print(f"Successfully added Full Batch Run cell to {NOTEBOOK_PATH}")
