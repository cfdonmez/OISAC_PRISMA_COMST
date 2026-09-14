# Wiley Online Library Pilot QA Report - 2026-06-21

Bu dosya, Step 2C-C Wiley Online Library supplementary platform pilot search ciktisinin kalite ve izlenebilirlik kontrolunu kaydeder. Bu kayitlar pilot/audit kayitlaridir; final search execution, formal screening karari veya PRISMA flow count olarak kullanilmayacaktir.

## Kapsam

- Platform: Wiley Online Library
- Source role: supplementary platform source
- Search/export date: 2026-06-21
- Search freeze label: planned search freeze date: June 30, 2026
- Raw exported rows: 57
- Unique deduplicated records: 49
- Duplicate groups: 7

## PASS

- PASS - Wiley raw pilot files `wiley.zip` and `wly_pilot_p1a.txt` through `wly_pilot_p2e.txt` are present in the raw export folder.
- PASS - Wiley audit package and expected audit CSV/MD files are present in the audit folder.
- PASS - Query strings for `WLY-PILOT-P1A`, `WLY-PILOT-P1B`, and `WLY-PILOT-P2A` through `WLY-PILOT-P2E` are documented in `search_log.csv` and `01_arama_plani.md`.
- PASS - Pilot diagnostics are explicitly marked as not final PRISMA flow counts.
- PASS - `prisma_flow_counts.md` remains TBD-only for Wiley and other sources.

## WARNING

- WARNING - WLY-PILOT-P1A appears to return a likely false positive despite an exact-phrase-style query.
- WARNING - WLY-PILOT-P1B includes false positives but also retrieves a strong self-powered optical O-ISAC record.
- WARNING - WLY-PILOT-P2B is mostly VLC/IRS communication noise and should remain rescue-only unless VLC/LiFi coverage is weak.
- WARNING - WLY-PILOT-P2C is mixed and requires title/abstract screening.
- WARNING - Review/chapter/contextual records must not be treated as primary technical evidence.
- WARNING - Wiley pilot records must not be treated as included studies.

## FAIL

- FAIL - None identified for workflow logging. The remaining issues are warnings/TODOs, not evidence that pilot logging should be discarded.

## Query Decision Summary

Keep candidate:

- WLY-PILOT-P2D
- WLY-PILOT-P2E

Keep as supplementary/rescue candidate with screening:

- WLY-PILOT-P1B
- WLY-PILOT-P2A
- WLY-PILOT-P2C

Rescue only / noisy:

- WLY-PILOT-P2B

Likely drop or deprioritize:

- WLY-PILOT-P1A

## TODO

- Check Wiley overlap against IEEE Xplore, Scopus, ScienceDirect and SpringerLink pilot records before final supplementary search execution.
- Decide whether WLY-PILOT-P1B, WLY-PILOT-P2A and WLY-PILOT-P2C remain rescue/sensitivity queries after overlap analysis.
- Keep WLY-PILOT-P2D and WLY-PILOT-P2E as focused candidate queries for final supplementary search design.
- Keep WLY-PILOT-P2B rescue-only unless final VLC/LiFi coverage is weak.
