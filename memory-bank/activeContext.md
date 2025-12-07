# Active Context

## Current Phase: Phase 2 (Preparation)
We have completed **Phase 1 (Title/Abstract Screening)** and are preparing for **Phase 2 (Full-Text Eligibility)** and **Data Extraction**.

## Recent Accomplishments
*   **Phase 1 Screening Analysis:**
    *   Analyzed `IEEE_511_OISAC_Results_Screened.csv`.
    *   **Included:** 158 studies (31.0%).
    *   **Excluded:** 352 studies.
    *   **Observation:** Significant number of RF-only papers were correctly excluded.
    *   **Report:** Generated `analysis/phase1_screening/Phase1_Screening_Report.md`.
*   **Infrastructure:**
    *   Created `included_studies_list.csv` for retrieval.
    *   Established this `memory-bank`.

## Immediate Next Steps
1.  **Develop Data Extraction Schema:**
    *   Translate Protocol Section 9 into a `oisac_extraction_schema.yaml` file.
    *   This schema will define the "Columns" for our final dataset (e.g., `wavelength_nm`, `data_rate_bps`, `sensing_resolution_m`).
2.  **Full-Text Retrieval Strategy:**
    *   User to retrieve PDFs based on `included_studies_list.csv`.

## Active Files
*   `protocol/prisma_protocol.md`: The rulebook.
*   `analysis/phase1_screening/included_studies_list.csv`: The worklist for the user.
