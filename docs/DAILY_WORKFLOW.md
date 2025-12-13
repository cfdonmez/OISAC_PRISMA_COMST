# 🔄 Daily "Living" Workflow for O-ISAC Review

This document outlines the **Daily Routine** to maintain the "Living Systematic Review" status. Until the manuscript is finalized, these steps should be performed regularly (e.g., every morning).

## 🌅 Morning Routine: Data Ingestion

### 1. Living Search (Sürekli Arama)
**Goal:** Catch new publications immediately.
*   **Action:** Check defined search alerts (Google Scholar, IEEE Xplore).
*   **Query:** Use the "Block A + Block B" simplified string from `protocol/prisma_protocol.md`.
*   **If New Hits Found:**
    1.  Add bibliographic details to `search/search_log.csv`.
    2.  Assign a temporary ID (e.g., `O_ISAC_NEW_YYYYMMDD_XX`).

### 2. Living Screening (Sürekli Eleme)
**Goal:** Filter new hits instantly.
*   **Input:** New entries in `search_log.csv`.
*   **Process:**
    1.  **Title/Abstract Check:** Does it meet `protocol` Section 4 criteria?
    2.  **Decision:** Update `screening/screening_log.csv` with `Include` or `Exclude`.
    3.  **If Included:** Immediately flag for PDF collection.

### 3. PDF Collection (Anlık Toplama)
**Goal:** Prevent backlog accumulation.
*   **Action:** Download PDF for any new `Include` items.
*   **Naming:** Rename to `O_ISAC_[ID].pdf`.
*   **Storage:** Save to `data/retrieved_docs/`.

---

## 🏭 The Factory: Batch Extraction (Optimization)

*Note: This section describes the integrated "Structural + Reasoning" pipeline.*

### 4. Integrated Extraction & Backbone Update
**Goal:** Turn PDF into Manuscript Skeleton.
*   **Trigger:** When new PDFs land in `data/retrieved_docs/`.
*   **Process:**
    1.  **Run Pipeline:** Execute `analysis/notebooks/CoT_Master_Pipeline.ipynb`.
    2.  **Output:** Generates `extraction_results_v4/` (Unified JSON).
    3.  **Backbone Sync:** The results automatically update the `manuscript/skeleton/` (TBD) files, linking findings to specific report sections.

---

## 🤖 Nightly: Agentic Research

### 5. Deep Research
**Goal:** Synthesis and Hypothesis Generation.
*   **Action:** The Deep Research Agent analyzes the day's new findings against the existing `activeContext`.
*   **Output:** Updates `analysis/deep_research/insights_log.md` with new gaps or trends identified.

---
**Last Updated:** 2025-12-13
