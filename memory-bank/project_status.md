# Project Status Snapshot

**Date:** 2025-12-07 23:28
**Current Phase:** Phase 2 - Pilot Extraction v2.0 Complete ✅

## 🚦 Phase Summary

| Phase | Status | Progress | Notes |
| :--- | :--- | :--- | :--- |
| **0. Preparation** | ✅ Completed | Protocol defined | `protocol/prisma_protocol.md` |
| **1. Search** | ✅ Completed | Sources identified | `search/` |
| **2. Screening** | ✅ Completed | 157 Studies Included | `analysis/phase1_screening/included_studies_list.csv` |
| **3. Retrieval** | 🟡 In Progress | 10/157 PDFs Retrieved | `data/retrieved_docs/` |
| **4. Extraction** | ✅ Pilot Success | 3 papers, 5 experiments | `data/extraction_results_v2/` |
| **5. Synthesis** | 🔴 Pending | - | - |

## 📊 Pilot Extraction v2.0 Results

| Metric | Value |
|--------|-------|
| Papers Processed | 3 (O_ISAC_001, O_ISAC_002, O_ISAC_003) |
| Experiments Extracted | 5 |
| CSV Columns | 51 |
| Errors | 0 |
| Model | llama-3.3-70b-versatile |

### Key Taxonomy Findings
| Field | single_dual_function | resource_division | NR |
|-------|---------------------|-------------------|-----|
| ISAC_Relationship | 3 | - | 2 |
| Coupling_Mode | - | 3 | 2 |

## 📈 Detailed Metrics

*   **Total Included Studies:** 157 (1 excluded at full-text: O_ISAC_007)
*   **PDFs Retrieved:** 10 (Target: 157)
*   **Processed for Analysis:** 9 (O_ISAC_009 missing markdown)

## 🛠 Next Steps
1.  **Run Full Extraction** - Execute on all 9 papers (no limit)
2.  **Fix O_ISAC_009** - Regenerate markdown
3.  **Continue PDF Retrieval** - 147 papers remaining
