# 🏭 O-ISAC Systematic Review: Daily Workflow Model (SOP)

This document defines the **Standard Operating Procedure (SOP)** for the daily execution of the Optical ISAC systematic review. It integrates **PRISMA 2020 compliance**, **Literature Search**, and the **AI-Powered Extraction Factory**.

---

## 🌅 Morning Cycle: Research & Screening (The Filter)
**Goal:** Feed the pipeline with high-quality, relevant studies while maintaining PRISMA compliance.

### 1.1 PRISMA Check & Strategy Adjustment
*   **Reference:** `protocol/PRISMA_2020_Checklist.md` (Items 5-8: Search Strategy, Selection)
*   **Action:**
    *   Review the **Search Strategy** in `prisma_protocol.md` (Section 6).
    *   Select the target database for the day (e.g., IEEE Xplore, Scopus).
    *   *Decision:* Are we searching for "Cabled" (Fiber) or "Wireless" (FSO/VLC) today?

### 1.2 Database Search & Export
*   **Action:** Run the query on the target database.
*   **Output:** Export results as `.csv` or `.ris`.
*   **Log:** Update `analysis/search_logs/search_log.csv` with the query date, string, and hit count.

### 1.3 Screening (Title/Abstract)
*   **Criteria:** Refer to `prisma_protocol.md` (Section 4: Eligibility).
*   **Action:** Quickly scan titles and abstracts.
    *   ✅ **Include:** Download PDF -> Save to `data/retrieved_docs/[Paper_ID].pdf`.
    *   ❌ **Exclude:** Log reason (e.g., "Radio Frequency only", "No sensing metrics").

---

## ☀️ Afternoon Cycle: The Extraction Factory (The Engine)
**Goal:** Convert raw PDFs into structured, high-fidelity JSON data using Llama 4 Vision.

### 2.1 The Master Notebook
*   **Notebook:** `analysis/notebooks/OISAC_Extraction_Pipeline_v3.ipynb`
*   **Role:** The single control panel for the entire extraction factory.
*   **Action:** Open in Colab, Mount Drive, and Run All.

### 2.2 Phase 1: Pre-Processing (Smart Repair)
*   **Goal:** Convert PDF to Markdown & Extract Images.
*   **Command (in Notebook):**
    ```python
    # Phase 1 only (fixes missing images)
    run_full_pipeline(skip_phase1=False, skip_phase2=True)
    ```

### 2.3 Phase 2: Vision & Extraction
*   **Goal:** Multi-modal analysis (Text + Vision).
*   **Command (in Notebook):**
    ```python
    # Full Run (Phase 1 checks, then Phase 2 & 3)
    run_full_pipeline()
    ```
*   **Process:**
    1.  **Vision Analysis:** Model "sees" the extracted images (Block Diagrams, Result Plots).
    2.  **Reasoning:** Model connects visual evidence with paper text.
    3.  **Extraction:** Outputs JSON in strict accordance with `schema_v2.yaml`.
*   **Auto-Constraint:** The system forces `step_0_visual_inspection` to ensuring the model "looked" at the data.

---

## 🌙 Evening Cycle: QC & Synthesis (The Product)
**Goal:** Verify quality, track progress, and update the "Big Picture".

### 3.1 Quality Control (TQAF Review)
*   **Action:** Check the generated logs in `analysis/cot_laboratory/logs/`.
*   **Audit:**
    *   Did a run fail? (Check `status: failed`).
    *   Is `tqaf_modelling_fidelity` < 1? (Flag for manual review).
    *   Are mandatory fields (Data Rate, Sensing Range) present?

### 3.2 Metrics & Flow Diagram Update
*   **Action:** Update `analysis/prisma_metrics.json` with new counts.
    *   `records_identified`: + New search hits.
    *   `records_screened`: + Screened count.
    *   `studies_included`: + Extracted PDFs.
*   **Visualize:** Run `python analysis/generate_prisma_flow.py` to see the updated PRISMA Flow Diagram.

### 3.3 Commit & Sync
*   **Action:** Push changes to GitHub.
    *   `git add data/retrieved_docs/`
    *   `git commit -m "Daily routine: Processed X new papers"`

---

## 🛠️ Operational Dashboard

| Phase | Input | Tool / Script | Output |
| :--- | :--- | :--- | :--- |
| **Research** | Database (IEEE/Web) | Manual / Browser | `data/retrieved_docs/*.pdf` |
| **Prep** | PDFs | `extraction_pipeline_v3.py` (Phase 1) | Images (`.jpg`) + Markdown (`.md`) |
| **Extract** | Images + Text | `CoT_Vision_Factory.ipynb` | `logs/*_RESULT.json` |
| **Verify** | JSON Logs | `schema_validator.py` (Planned) | Validated Data |
| **Report** | Validated Data | `generate_prisma_flow.py` | PRISMA Flow Chart |
