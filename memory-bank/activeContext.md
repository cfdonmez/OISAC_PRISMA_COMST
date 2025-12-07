# Active Context

## Current Phase: Phase 2 (Full-Text Retrieval & Pilot Extraction)
We have successfully completed **Phase 1 (Screening)** with **158 studies included**.
We are now in the **Retrieval Phase**, with concurrent Pilot Extraction using **Schema v2.0**.

## Recent Accomplishments
*   **Screening Complete:** 158 papers selected (`analysis/phase1_screening/included_studies_list.csv`).
*   **Retrieval Started:** 10/158 PDFs retrieved (`data/retrieved_docs`).
*   **Pilot Processing:** 10 retrieved papers have been processed into markdown (`data/processed_markdowns`).
*   **Schema v2.0 Created:** Comprehensive extraction schema aligned with PRISMA Protocol Section 9 (`analysis/oisac_extraction_schema_v2.yaml`).
*   **Extraction Script v2.0:** Updated Colab script with enhanced LLM prompt (`analysis/notebooks/prisma_extraction_v2.py`).

## Schema v2.0 Key Improvements
*   **68 fields** (vs. ~15 in v1.0)
*   **Study-Level + Scenario-Level** structure
*   **isac_waveform_relationship**: Critical for taxonomy
*   **Tradeoff characterization**: coupling_mode, tradeoff_type, control parameters
*   **Full channel models**: Fiber (backscatter types) + Wireless (turbulence models)
*   **Quality Assessment (TQAF)**: 5-dimension scoring

## Immediate Next Steps
1.  **Re-run Pilot Extraction** with v2.0 schema on existing 10 papers.
2.  **Validate Extraction Quality** - check for NR rates and consistency.
3.  **Continue PDF Retrieval** - 148 papers remaining.
4.  **Scale Extraction** once validation complete.

## Active Files
*   `analysis/oisac_extraction_schema_v2.yaml`: **NEW** comprehensive schema
*   `analysis/notebooks/prisma_extraction_v2.py`: **NEW** extraction script
*   `analysis/phase1_screening/included_studies_list.csv`: Master paper list
*   `data/retrieved_docs/`: PDF repository
*   `data/processed_markdowns/`: Processed markdown files
