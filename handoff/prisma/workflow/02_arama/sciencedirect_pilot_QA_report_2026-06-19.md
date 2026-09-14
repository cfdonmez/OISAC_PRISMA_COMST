# ScienceDirect Pilot QA Report - 2026-06-19

Bu dosya, Step 2C-A ScienceDirect supplementary platform pilot search ciktisinin kalite ve izlenebilirlik kontrolunu kaydeder. Bu kayitlar pilot/audit kayitlaridir; final search execution, formal screening karari veya PRISMA flow count olarak kullanilmayacaktir.

## Kapsam

- Platform: ScienceDirect
- Source role: supplementary platform source
- Search date: 2026-06-19
- Search freeze label: planned search freeze date: June 30, 2026
- Raw/audit status checked locally: 2026-06-21

## PASS

- PASS - ScienceDirect supplementary platform pilot rows are represented in `search_log.csv` as `SD-PILOT-P1`, `SD-PILOT-P2A`, `SD-PILOT-P2B`, `SD-PILOT-P2C`, `SD-PILOT-P2D`, `SD-PILOT-P2E`, `SD-PILOT-P3`, and `SD-PILOT-P4`.
- PASS - Query strings for `SD-PILOT-P1` and `SD-PILOT-P2A` through `SD-PILOT-P2E` are documented in `search_log.csv` and `01_arama_plani.md`.
- PASS - `SD-PILOT-P3` and `SD-PILOT-P4` are not reconstructed; their query strings remain `query_string_pending_from_sciencedirect_raw_txt`.
- PASS - Pilot diagnostics are explicitly marked as not final PRISMA flow counts.
- PASS - `prisma_flow_counts.md` remains TBD-only for ScienceDirect and other sources.

## WARNING

- WARNING - ScienceDirect interface limited Boolean connectors; original P2 was split into smaller exact and modality-specific subqueries.
- WARNING - ScienceDirect txt exports were converted to structured CSV by ChatGPT; CSVs are derived audit files, not raw exports.
- WARNING - ScienceDirect results include useful O-ISAC records but also broad 6G, pure sensing, pure communication, and contextual review noise.
- WARNING - Expected raw txt folder `systematic_review_workflow/02_arama/raw_exports/sciencedirect/pilot_2026-06-19/` is not present in this local repo check.
- WARNING - Expected audit folder `systematic_review_workflow/02_arama/audits/sciencedirect/pilot_2026-06-19/` is not present in this local repo check; existing ScienceDirect derived files are under the Step 2 pilot folder structure.
- WARNING - Several OneDrive-backed ScienceDirect summary/audit files could be listed but not opened during local readback; this appears consistent with cloud-placeholder behavior and should be verified on the machine where the files are fully hydrated.

## FAIL

- FAIL - None identified for workflow logging. The remaining issues are warnings/TODOs, not evidence that pilot logging should be discarded.

## Local File Placement Observed

Existing derived ScienceDirect CSV files were observed under:

```text
systematic_review_workflow/02_arama/raw_exports/pilot_2026-06-19/sciencedirect/
```

Existing ScienceDirect audit ZIP was observed under:

```text
systematic_review_workflow/02_arama/audits/pilot_2026-06-19/sciencedirect/
```

## Pilot Count Guardrail

- Total raw rows: 350.
- Unique deduplicated records: 172.
- These values are pilot audit diagnostics only.
- These values must not be copied into PRISMA flow counts.

## TODO

- Recover or place the eight user-provided raw ScienceDirect txt exports if available.
- Confirm exact raw-txt query strings for `SD-PILOT-P3` and `SD-PILOT-P4`.
- Check ScienceDirect overlap against IEEE Xplore and Scopus pilot records before final supplementary search design.
- Decide whether `SD-PILOT-P3` and `SD-PILOT-P4` remain rescue/sensitivity queries or are dropped before final search execution.
