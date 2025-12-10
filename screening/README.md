# 🕵️ Screening Operations Guide

This folder contains the logs and records for the **Study Selection Process** (PRISMA 2020).

## 📋 The Screening Workflow

### 1. Title & Abstract Screening (Phase 1)
**Goal:** Quickly eliminate irrelevant studies.

*   **Input:** Exported CSV/RIS files from databases (IEEE Xplore, Scopus).
*   **Action:** Read the Title and Abstract.
*   **Decision Criteria:**
    *   **Include:** Does it match "Optical ISAC" definition? (See `protocol/prisma_protocol.md` Section 4).
    *   **Exclude:** RF-only, Pure Sensing, Pure Comm, Thesis, etc.
*   **Logging:**
    *   Update `screening_log.csv` (or your Excel master list).
    *   Mark status: `Include` / `Exclude` / `Unsure`.

### 2. Full-Text Retrieval
**Goal:** Get the PDF for "Include" papers.
*   Download the PDF.
*   **Renaming Rule:** `O_ISAC_[ID].pdf` (e.g., `O_ISAC_045.pdf`).
*   **Save Location:** `data/retrieved_docs/`.

### 3. Files in this Directory
*   `screening_log.csv`: The master record of your screening decisions.
*   `excluded_fulltext_log.csv`: Specific reasons for excluding papers *after* reading the full text.
*   `prisma_flow_counts.csv`: Auto-generated numbers for the PRISMA diagram.
