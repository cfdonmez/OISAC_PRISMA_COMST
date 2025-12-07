# Project Status Snapshot

**Date:** 2025-12-07
**Current Phase:** Phase 2 - Retrieval & Pilot Extraction

## 🚦 Phase Summary

| Phase | Status | Progress | Notes |
| :--- | :--- | :--- | :--- |
| **0. Preparation** | ✅ Completed | Protocol defined | `protocol/prisma_protocol.md` |
| **1. Search** | ✅ Completed | Sources identified | `search/` |
| **2. Screening** | ✅ Completed | 157 Studies Included | `analysis/phase1_screening/included_studies_list.csv` |
| **3. Retrieval** | 🟡 In Progress | 10/157 PDFs Retrieved | `data/retrieved_docs/` |
| **4. Extraction** | 🟡 Pilot | Schema v2.0 ready | `analysis/oisac_extraction_schema_v2.yaml` |
| **5. Synthesis** | 🔴 Pending | - | - |

## 📊 Detailed Metrics

*   **Total Included Studies:** 157 (1 excluded at full-text: O_ISAC_007)

*   **PDFs Retrieved:** 10 (Target: 158)
    *   Stored in: `data/retrieved_docs/`
    *   Current IDs: `O_ISAC_001` - `O_ISAC_010`
*   **Processed for Analysis:** 10
    *   Markdown conversions in: `data/processed_markdowns/`

## 🛠 Active Tasks
1.  **Retrieve remaining 148 PDFs.**
2.  **Verify extraction quality** on the first 10 papers (`data/extraction_results`).
3.  **Update Extraction Schema** if pilot results show missing fields.
