# Active Context

## Current Phase: Pilot Extraction v2.0 Complete ✅
Pilot successfully validated Schema v2.0 extraction on 3 papers with 0 errors.

## Latest Results (2025-12-07 23:28)
*   **Papers Processed:** 3 (O_ISAC_001, O_ISAC_002, O_ISAC_003)
*   **Experiments Extracted:** 5 (multi-scenario detection working)
*   **CSV Columns:** 51 (comprehensive PRISMA Section 9 alignment)
*   **Key Success:** `isac_waveform_relationship` and `coupling_mode` correctly extracted

## Extraction Quality Summary
| Metric | Value |
|--------|-------|
| `single_dual_function` | 3/5 experiments |
| `resource_division` | 3/5 experiments |
| Evidence Snippets | ✅ Captured |
| Source Pointers | ✅ Captured |

## Output Files
*   `data/extraction_results_v2/extraction_v2_full.json` (17.7 KB)
*   `data/extraction_results_v2/study_level_v2.csv`
*   `data/extraction_results_v2/experiment_level_v2.csv`

## Immediate Next Steps
1.  **Full Extraction** - Run `run_extraction_pipeline_v2()` on all 9 papers
2.  **Fix O_ISAC_009** - Markdown not generated
3.  **Continue PDF Retrieval** - 147 papers remaining

## Excluded Studies
| Track_ID | Reason | Code |
|----------|--------|------|
| O_ISAC_007 | Pure sensing, no communication | EXC-PURE-SENSING |

## Active Files
*   `analysis/oisac_extraction_schema_v2.yaml`: Comprehensive schema
*   `analysis/notebooks/PRISMA_Extraction_v2_Colab.ipynb`: Extraction notebook
*   `data/extraction_results_v2/`: Pilot output directory
