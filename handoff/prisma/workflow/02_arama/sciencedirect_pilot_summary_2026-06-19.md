# ScienceDirect Pilot Summary - 2026-06-19

Bu dosya ScienceDirect supplementary platform pilot CSV paketini ozetler. Bu kayitlar pilot search/audit kayitlaridir; final search execution, deduplication, screening veya PRISMA flow count olarak kullanilmayacaktir. Search freeze etiketi `planned search freeze date: June 30, 2026` olarak kalir.

## Package Placement

Original package copied into the workflow audit area:

- `systematic_review_workflow/02_arama/audits/pilot_2026-06-19/sciencedirect/sciencedirect_pilot_csv_package_2026-06-19.zip`

Extracted/working CSV files copied into:

- `systematic_review_workflow/02_arama/raw_exports/pilot_2026-06-19/sciencedirect/`
- `systematic_review_workflow/02_arama/audits/pilot_2026-06-19/sciencedirect/extracted/`

## CSV Files

| File | Parsed rows | Role |
|---|---:|---|
| `sciencedirect_pilot_query_summary_2026-06-19.csv` | 9 | Query-level pilot summary, including aggregate row. |
| `sciencedirect_pilot_all_rows_2026-06-19.csv` | 350 | All parsed pilot rows across ScienceDirect pilot queries. |
| `sciencedirect_pilot_records_clean_2026-06-19.csv` | 350 | Cleaned all-row pilot records. |
| `sciencedirect_pilot_unique_records_2026-06-19.csv` | 172 | DOI/title-deduplicated pilot diagnostic set. |

The 350 all-row count and 172 unique-record count are pilot audit diagnostics only and must not be entered into PRISMA flow counts.

## Query-Level Pilot Counts

| Search ID | Input file | Parsed rows | Unique within query | Query status | Search log status |
|---|---|---:|---:|---|---|
| SD-PILOT-P1 | `SD-PILOT-P1.txt` | 9 | 9 | exact UI query pending; described as original exact O-ISAC phrase export | Added with placeholder |
| SD-PILOT-P2A | `SD-PILOT-P2A.txt` | 59 | 59 | query text available in package | Added |
| SD-PILOT-P2B | `SD-PILOT-P2B.txt` | 67 | 67 | query text available in package | Added |
| SD-PILOT-P2C | `SD-PILOT-P2C.txt` | 89 | 89 | query text available in package | Added |
| SD-PILOT-P2D | `SD-PILOT-P2D.txt` | 5 | 5 | query text available in package | Added |
| SD-PILOT-P2E | `SD-PILOT-P2E.txt` | 10 | 10 | query text available in package | Added |
| SD-PILOT-P3 | `SD-PILOT-P3.txt` | 11 | 11 | exact UI query pending; optional/tight export | Added with placeholder |
| SD-PILOT-P4 | `SD-PILOT-P4.txt` | 100 | 100 | exact UI query pending; optional/modality export | Added with placeholder |

Aggregate row in package:

| Aggregate ID | Parsed rows | Unique records | Note |
|---|---:|---:|---|
| ALL_SD_PILOT | 350 | 172 | Audit diagnostic only; not logged as a separate search query. |

## Query String Status

The following ScienceDirect query strings were available in the package and were entered into `search_log.csv`:

- SD-PILOT-P2A
- SD-PILOT-P2B
- SD-PILOT-P2C
- SD-PILOT-P2D
- SD-PILOT-P2E

The following exact ScienceDirect UI query strings were not independently verified and remain pending:

- SD-PILOT-P1
- SD-PILOT-P3
- SD-PILOT-P4

Their `search_log.csv` search string is:

```text
query_string_pending_from_sciencedirect_history_or_user_confirmation
```

## Preliminary Relevance Labels

The package includes automated labels such as `primary_candidate_not_screened`, `contextual_candidate_not_screened`, `unclear_full_text_needed_not_screened`, and `likely_noise_or_out_of_scope_not_screened`. These are search-readiness/audit labels only. They are not screening decisions and must not be used as included studies, excluded studies, or PRISMA flow counts.

## Corpus Handling Reminder

- Review/survey records will be marked as contextual corpus where applicable.
- Contextual records will not be counted as primary technical evidence.
- ScienceDirect remains a supplementary platform source, not a core primary database.
- Formal PRISMA counts remain TBD until final search execution, deduplication, and screening are complete.

## TODO

- Recover or confirm exact ScienceDirect UI query strings for SD-PILOT-P1, SD-PILOT-P3, and SD-PILOT-P4.
- Decide whether SD-PILOT-P3 and SD-PILOT-P4 should remain supplementary rescue/sensitivity queries or be dropped before final supplementary search.
- Compare ScienceDirect unique pilot records against IEEE + Scopus candidate set during later deduplication planning.
