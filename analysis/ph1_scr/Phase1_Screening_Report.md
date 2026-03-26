# Phase 1 Screening Report: Title and Abstract

Status
- This file is an interim Phase 1 artifact kept for historical traceability.
- It is not the canonical source for final Section III PRISMA counts.
- Final manuscript numbers must be taken from:
  - `screening/prisma_flow_counts.csv`
  - `search/search_log.csv`
  - `search/dedup_log.csv`
  - `screening/excluded_fulltext_log.csv`
  - `screening/screening_log.csv` when finalized

Interpretation rule
- If a number in this report conflicts with the canonical Section III artifacts, treat this report as archived and non-authoritative.

Update note (2026-02-05)
- Final included corpus size is `N = 221` based on `data/proc_markdowns` inventory.
- The Phase 1 counts below reflect a title/abstract screening subset and remain pending reconciliation with the final PRISMA flow.

## 1. Overview

| Metric | Count | Percentage |
| :--- | :--- | :--- |
| **Total Records Screened** | **510** | 100% |
| **Included** | **158** | **31.0%** |
| Excluded | 352 | 69.0% |

## 2. Included Studies by Media (O-ISAC Domain)

This breakdown reflects the categorization of the **158** included studies.

| Domain (Category) | Count | Percentage of Included |
| :--- | :--- | :--- |
| **Wireless O-ISAC** | **105** | **66.5%** |
| **Cabled (Fiber) O-ISAC** | **53** | **33.5%** |

## 3. Exclusion Analysis

A total of **352** studies were excluded. The primary reasons are listed below:

| Exclusion Reason | Count | Percentage of Excluded |
| :--- | :--- | :--- |
| No optical carrier detected | 222 | 63.1% |
| Lacks clear sensation/comms keywords | 34 | 9.7% |
| No optical carrier detected; Likely RF/THz only | 29 | 8.2% |
| Pure communication | 28 | 8.0% |
| Pure sensing | 24 | 6.8% |
| Review/Survey article | 15 | 4.3% |

Note
- The dominant exclusion reason ("No optical carrier detected") supports the observation that the broad search query retrieved many RF/THz ISAC records unrelated to optical systems.

## 4. Recommendations for Phase 2

1. Proceed to retrieve PDFs for the **158** included records.
2. Prioritize the **105** wireless O-ISAC papers because they constitute the majority.
3. Re-check the **15** review/survey articles as snowballing candidates even if they remain excluded from the primary synthesis.
