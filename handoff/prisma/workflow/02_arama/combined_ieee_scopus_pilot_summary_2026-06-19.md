# Combined IEEE + Scopus Pilot Summary - 2026-06-19

Bu dosya Step 2B IEEE + Scopus pilot search export paketini ozetler. Bu pilot counts final PRISMA flow counts degildir. PRISMA flow count dosyasi TBD kalmalidir.

## Candidate Pilot Package

Candidate pilot package:

| Search ID | Source | Pilot date | Reported/raw records | Exported rows | Canonical file | Prelim karar |
|---|---|---|---:|---:|---|---|
| IEEE-PILOT-S1A | IEEE Xplore | 2026-06-18 | 31 | 31 | `raw_exports/pilot_2026-06-19/IEEE-PILOT-S1A_export_2026-06-18.csv` | keep candidate |
| IEEE-PILOT-S1B-R2 | IEEE Xplore | 2026-06-18 | 239 | 239 | `raw_exports/pilot_2026-06-19/IEEE-PILOT-S1B-R2_export_2026-06-18.csv` | keep candidate |
| IEEE-PILOT-S1F-R2 | IEEE Xplore | 2026-06-19 | 45 | 45 | `raw_exports/pilot_2026-06-19/IEEE-PILOT-S1F-R2_export_2026-06-19.csv` | keep candidate; replaces S1F-R1 |
| SCO-PILOT-S1A | Scopus | 2026-06-19 | 40 | 40 | `raw_exports/pilot_2026-06-19/SCO-PILOT-S1A_export_2026-06-19.csv` | keep candidate |
| SCO-PILOT-S1B | Scopus | 2026-06-19 | 35 | 60 | `raw_exports/pilot_2026-06-19/SCO-PILOT-S1B_export_2026-06-19.csv` | keep candidate; verify mismatch |
| SCO-PILOT-S1F | Scopus | 2026-06-19 | 103 | 104 | `raw_exports/pilot_2026-06-19/SCO-PILOT-S1F_export_2026-06-19.csv` | keep candidate; verify minor mismatch |

## Rejected or Replaced IEEE Pilot Records

These pilot records remain documented in `search_log.csv` but are not part of the current candidate pilot package:

| Search ID | Pilot count | Status |
|---|---:|---|
| IEEE-PILOT-S1B | 1195 | too broad; rejected |
| IEEE-PILOT-S1B-R1 | 780 | too broad; rejected |
| IEEE-PILOT-S1C-R1 | >1000 | too broad; rejected/refinement needed |
| IEEE-PILOT-S1D-R1 | 1000 | too broad; rejected/refinement needed |
| IEEE-PILOT-S1E-R1 | >3000 | too broad; rejected/refinement needed |
| IEEE-PILOT-S1F-R1 | 110 | valuable but noisy; replaced by S1F-R2 |

## Audit Summary

Audit package:

- `systematic_review_workflow/02_arama/audits/pilot_2026-06-19/pilot_audit_files_for_agent_2026-06-19.zip`
- `systematic_review_workflow/02_arama/audits/pilot_2026-06-19/extracted/`

Key pilot audit diagnostics:

| Metric | Pilot audit value | Interpretation |
|---|---:|---|
| Scopus total exported rows | 204 | Pilot export diagnostic only |
| Scopus unique records after DOI/title dedup | 172 | Pilot dedup diagnostic only |
| Combined IEEE + Scopus candidate rows | 519 | Pilot export diagnostic only |
| Combined IEEE + Scopus unique records | 327 | Pilot dedup diagnostic only |
| IEEE-only unique records | 155 | Shows IEEE-specific contribution in pilot set |
| Scopus-only unique records | 78 | Shows Scopus complementary records beyond IEEE |
| Records appearing in both sources | 94 | Pilot overlap diagnostic |

These audit diagnostics are not final PRISMA counts and must not be entered into `03_secim/prisma_flow_counts.md`.

## QA Warnings

- SCO-PILOT-S1B has reported/export mismatch: 35 vs 60.
- SCO-PILOT-S1F has minor mismatch: 103 vs 104.
- SCO-PILOT-S1B export is metadata-light; future final export should include Year, Source title, Document type, DOI, Abstract, Author keywords, Index keywords, and EID.
- IEEE-PILOT-S1A, IEEE-PILOT-S1B-R2 and IEEE-PILOT-S1F-R2 exact query strings were recovered from chat log and added to `search_log.csv`.
- Scopus exact query strings are still pending and must be recovered from Scopus database history or user confirmation.

## Corpus Handling Reminder

- Pilot exports do not create included studies.
- Pilot exports do not create screening counts.
- Review/survey papers will be marked as contextual corpus and will not be counted as primary technical evidence.
- Legacy `included_studies_canonical.csv` remains outside the formal PRISMA workflow and will not be used as seed set or validation set.

## Next Actions

1. Recover exact query strings for SCO-PILOT-S1A, SCO-PILOT-S1B and SCO-PILOT-S1F.
2. Verify SCO-PILOT-S1B and SCO-PILOT-S1F count mismatches.
3. Inspect candidate pilot package before final core source search.
4. Start supplementary platform pilots after core package QA.
