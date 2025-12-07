# Active Context

## Current Phase: Phase 2 (Full-Text Retrieval)
We have completed **Phase 1 (Screening)** and the **Schema Definition**.
We are now entered the **Retreival Phase**.

## Recent Accomplishments
*   **Infrastructure:** Established `memory-bank` and `AI_Co_Pilot_Workflow.md`.
*   **Schema:** Defined `analysis/oisac_extraction_schema.yaml` (v1.0) for structured meta-analysis.
*   **Target List:** `analysis/phase1_screening/included_studies_list.csv` contains the 158 papers to retrieve.

## Immediate Next Steps
1.  **Full-Text Retrieval (User Action):**
    *   The User needs to download PDFs for the 158 included studies using the DOIs in `included_studies_list.csv`.
    *   Store them in a local directory (e.g., `papers/`).
2.  **Pilot Extraction:**
    *   Once a few PDFs are available, we will pilot the `oisac_extraction_schema.yaml` on 3-5 papers to test if it "fits" the reality of the data.

## Active Files
*   `analysis/oisac_extraction_schema.yaml`: The form we must fill out.
*   `analysis/phase1_screening/included_studies_list.csv`: The checklist of papers.
