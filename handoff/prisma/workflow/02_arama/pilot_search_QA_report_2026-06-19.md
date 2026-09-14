# Pilot Search QA Report - 2026-06-19

Bu QA raporu Step 2B IEEE + Scopus pilot search export duzenlemesini kontrol eder. Pilot search counts final PRISMA flow counts degildir.

## PASS

| Check | Status | Evidence |
|---|---|---|
| Canonical raw export folder exists | PASS | `systematic_review_workflow/02_arama/raw_exports/pilot_2026-06-19/` |
| Audit folder exists | PASS | `systematic_review_workflow/02_arama/audits/pilot_2026-06-19/` |
| Audit zip moved out of IEEE Xplore raw root | PASS | `audits/pilot_2026-06-19/pilot_audit_files_for_agent_2026-06-19.zip` |
| Audit zip extracted | PASS | `audits/pilot_2026-06-19/extracted/` |
| Scopus raw exports separated from IEEE Xplore raw root | PASS | No `scopus_export_*.csv` remains under `raw_exports/ieee_xplore/` root. |
| CSV files parse | PASS | Six canonical raw export CSV files were readable. |
| Raw/exported row counts recorded | PASS | Counts recorded in `search_log.csv`, Scopus summary, and combined summary. |
| Pilot/final distinction is explicit | PASS | Summaries and search log state pilot counts are not final PRISMA flow counts. |
| PRISMA flow counts unchanged | PASS | `03_secim/prisma_flow_counts.md` remains TBD. |
| Query string placeholder has TODO | PASS | Scopus candidate rows use `query_string_pending_from_scopus_history_or_user_confirmation`; TODOs added. |
| ScienceDirect package copied into workflow | PASS | Package copied under `audits/pilot_2026-06-19/sciencedirect/`; CSVs copied under `raw_exports/pilot_2026-06-19/sciencedirect/`. |
| ScienceDirect CSV files parse | PASS | Four ScienceDirect pilot CSV files were readable. |
| ScienceDirect pilot rows logged | PASS | SD-PILOT-P1, P2A, P2B, P2C, P2D, P2E, P3 and P4 added to `search_log.csv`. |

## Raw Export Row Counts

| Search ID | Canonical file | Parsed rows | Expected/exported rows | Status |
|---|---|---:|---:|---|
| IEEE-PILOT-S1A | `IEEE-PILOT-S1A_export_2026-06-18.csv` | 31 | 31 | PASS |
| IEEE-PILOT-S1B-R2 | `IEEE-PILOT-S1B-R2_export_2026-06-18.csv` | 239 | 239 | PASS |
| IEEE-PILOT-S1F-R2 | `IEEE-PILOT-S1F-R2_export_2026-06-19.csv` | 45 | 45 | PASS |
| SCO-PILOT-S1A | `SCO-PILOT-S1A_export_2026-06-19.csv` | 40 | 40 | PASS |
| SCO-PILOT-S1B | `SCO-PILOT-S1B_export_2026-06-19.csv` | 60 | 60 | PASS with count warning |
| SCO-PILOT-S1F | `SCO-PILOT-S1F_export_2026-06-19.csv` | 104 | 104 | PASS with count warning |

## ScienceDirect Pilot Row Counts

| Search ID | Parsed rows | Unique within query | Status |
|---|---:|---:|---|
| SD-PILOT-P1 | 9 | 9 | PASS with query warning |
| SD-PILOT-P2A | 59 | 59 | PASS |
| SD-PILOT-P2B | 67 | 67 | PASS |
| SD-PILOT-P2C | 89 | 89 | PASS |
| SD-PILOT-P2D | 5 | 5 | PASS |
| SD-PILOT-P2E | 10 | 10 | PASS |
| SD-PILOT-P3 | 11 | 11 | PASS with query warning |
| SD-PILOT-P4 | 100 | 100 | PASS with query warning |

ScienceDirect aggregate audit diagnostics: 350 all parsed rows and 172 unique records after DOI/title deduplication. These are pilot audit diagnostics only and are not PRISMA flow counts.

## WARNING

| Warning | Detail | Required action |
|---|---|---|
| Original file names differed from canonical names | IEEE and Scopus source files were mapped by row count and content signal, then stored with canonical names. | Keep canonical files as working raw export references. |
| SCO-PILOT-S1B count mismatch | Reported records = 35; exported rows = 60. | Must be resolved before final search. |
| SCO-PILOT-S1F count mismatch | Reported records = 103; exported rows = 104. | Must be resolved before final search. |
| SCO-PILOT-S1B metadata-light export | Missing final-export fields such as Year, Source title, Document type, and EID. | Future final export should include Year, Source title, Document type, DOI, Abstract, Author keywords, Index keywords, and EID. |
| Scopus exact query strings still pending | SCO-PILOT-S1A, SCO-PILOT-S1B and SCO-PILOT-S1F exact query strings require Scopus history or user confirmation. | Recover from Scopus database history or user confirmation; do not reconstruct from memory. |
| ScienceDirect exact query strings pending | SD-PILOT-P1, SD-PILOT-P3 and SD-PILOT-P4 exact UI query strings were not independently verified. | Recover from ScienceDirect history or user confirmation; do not reconstruct from memory. |
| ScienceDirect automated labels are not screening decisions | Package labels such as `primary_candidate_not_screened` are audit/readiness labels only. | Do not convert labels into included/excluded studies or PRISMA flow counts. |
| ZIP path separator portability | Future handoff zip path entries should use portable `/` separators where possible. | Prefer forward-slash entry names in generated handoff packages. |

## FAIL

No FAIL items identified in this QA pass.

## Non-PRISMA Count Reminder

The following audit diagnostics must not be copied into PRISMA flow counts:

- Scopus exported rows: 204.
- Scopus unique records after DOI/title deduplication: 172.
- Combined IEEE + Scopus candidate rows: 519.
- Combined IEEE + Scopus unique records: 327.
- ScienceDirect all parsed pilot rows: 350.
- ScienceDirect unique pilot records after DOI/title deduplication: 172.

These are pilot audit diagnostics only. Formal PRISMA counts remain TBD until final search execution, deduplication, and screening are completed.
