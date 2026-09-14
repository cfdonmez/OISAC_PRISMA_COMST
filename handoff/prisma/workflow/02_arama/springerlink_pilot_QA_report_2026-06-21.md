# SpringerLink Pilot QA Report - 2026-06-21

Bu dosya, Step 2C-B SpringerLink supplementary platform pilot search ciktisinin kalite ve izlenebilirlik kontrolunu kaydeder. Bu kayitlar pilot/audit kayitlaridir; final search execution, formal screening karari veya PRISMA flow count olarak kullanilmayacaktir.

## Kapsam

- Platform: SpringerLink
- Source role: supplementary platform source
- Search date/export date: 2026-06-21
- Search freeze label: planned search freeze date: June 30, 2026
- Raw exported rows: 159
- Unique deduplicated records: 126
- Duplicate groups: 29

## PASS

- PASS - SpringerLink raw pilot CSV files for `SPR-PILOT-P1B` and `SPR-PILOT-P2A` through `SPR-PILOT-P2E` are present in the raw export folder.
- PASS - SpringerLink audit package was readable and the expected audit CSV/MD files were extracted to the audit folder.
- PASS - Query strings for `SPR-PILOT-P1B` and `SPR-PILOT-P2A` through `SPR-PILOT-P2E` are documented in `search_log.csv` and `01_arama_plani.md`.
- PASS - Pilot diagnostics are explicitly marked as not final PRISMA flow counts.
- PASS - `prisma_flow_counts.md` remains TBD-only for SpringerLink and other sources.

## WARNING

- WARNING - `SPR-PILOT-P1A` not present in uploaded ZIP.
- WARNING - `springer.zip` was not present in the raw export folder during local repo check; extracted CSV exports and the audit package are present.
- WARNING - SpringerLink author names are concatenated in export; usable for pilot logging but not ideal for final extraction.
- WARNING - Chapter records are present; chapters are not primary technical evidence under current protocol.
- WARNING - P1B includes non-O-ISAC false positives.
- WARNING - P2A/P2B/P2C include general ISAC/6G and non-optical records; title/abstract screening required.
- WARNING - SpringerLink pilot records must not be treated as included studies.

## FAIL

- FAIL - None identified for workflow logging. The remaining issues are warnings/TODOs, not evidence that pilot logging should be discarded.

## Query Decision Summary

Keep candidate:

- SPR-PILOT-P2C
- SPR-PILOT-P2D
- SPR-PILOT-P2E

Noisy / rescue only:

- SPR-PILOT-P1B
- SPR-PILOT-P2A
- SPR-PILOT-P2B

Missing / TODO:

- SPR-PILOT-P1A

## TODO

- Recover or confirm `SPR-PILOT-P1A` query/export if it exists outside the uploaded package.
- Preserve `SPR-PILOT-P2C`, `SPR-PILOT-P2D` and `SPR-PILOT-P2E` as useful focused candidates for final supplementary search design.
- Decide whether `SPR-PILOT-P1B`, `SPR-PILOT-P2A` and `SPR-PILOT-P2B` should remain rescue/sensitivity queries after overlap analysis.
- Check SpringerLink overlap against IEEE Xplore, Scopus and ScienceDirect pilot records before final supplementary search execution.
