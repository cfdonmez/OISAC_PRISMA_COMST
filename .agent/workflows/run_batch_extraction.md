---
description: How to run the Full Batch CoT Extraction (The Factory)
---

# 🏭 Workflow: Full Batch Extraction

This workflow explains how to process all 150+ papers using the **Chain-of-Thought Laboratory**.

## 💡 Prerequisite: "Cloud vs Local"
You **do NOT need a GPU** to run this locally. 
*   **Why?** We are using the **Groq API** (Cloud). The "thinking" happens on Groq's supercomputers, not your laptop.
*   **Your Computer's Role:** It just acts as a "Secretary" sending emails (prompts) and saving replies (JSON). A standard CPU is perfectly sufficient.

## 1. Setup Environment
Ensure your `GROQ_API_KEY` is set.
```powershell
$env:GROQ_API_KEY='gsk_...'
```

## 2. Locate the Factory Script
The script is located at:
`analysis/cot_laboratory/core/batch_runner.py`

## 3. Run the Production Line
Execute the script from the project root:

```powershell
python analysis/cot_laboratory/core/batch_runner.py
```

## 4. Monitor Progress
The script will:
1.  Scan `data/processed_markdowns/` for all `O_ISAC_*.md` files.
2.  Process them one by one.
3.  Save prompts and results in `analysis/cot_laboratory/logs/`.
4.  Print `[✅ SUCCESS]` or `[❌ FAILED]` for each paper.

## 5. Post-Process (Synthesis)
Once the batch is done, all JSONs will be in the `logs/` folder.
We will then run a separate script to merge these JSONs into a single `master_dataset.csv` or `Excel` for the survey.
