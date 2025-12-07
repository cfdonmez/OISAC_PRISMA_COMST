# Active Context

## Current Phase: Phase 2 (Full-Text Retrieval & Pilot Extraction)
We have successfully completed **Phase 1 (Screening)** with **158 studies included**.
We are now in the **Retrieval Phase**, with concurrent Pilot Extraction.

## Recent Accomplishments
*   **Screening Complete:** 158 papers selected (`analysis/phase1_screening/included_studies_list.csv`).
*   **Retrieval Started:** 10/158 PDFs retrieved (`data/retrieved_docs`).
*   **Pilot Processing:** 10 retrieved papers have been processed into markdown (`data/processed_markdowns`).
*   **Extraction Pilot:** Initial extraction results generated (`data/extraction_results`).

## Immediate Next Steps
1.  **Full-Text Retrieval (Action Required):**
    *   Download remaining 148 PDFs for the included studies.
    *   Naming convention: `O_ISAC_XXX.pdf`.
    *   Store in `data/retrieved_docs`.
2.  **Extraction Verification:**
    *   Review `data/extraction_results` to ensure `oisac_extraction_schema.yaml` is capturing necessary data.
    *   Refine schema if needed.
3.  **Scale Extraction:**
    *   Once retrieval is substantial, run batch extraction.

## Active Files
*   `analysis/phase1_screening/included_studies_list.csv`: The master list of 158 included papers.
*   `data/retrieved_docs/`: Repository for PDF files.
*   `data/processed_markdowns/`: Intermediate processed files for AI analysis.
*   `analysis/oisac_extraction_schema.yaml`: The data extraction schema.
