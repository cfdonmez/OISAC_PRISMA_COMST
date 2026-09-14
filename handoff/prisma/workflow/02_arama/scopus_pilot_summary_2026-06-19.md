# Scopus Pilot Summary - 2026-06-19

Bu dosya Step 2B Scopus pilot search exportlarini ozetler. Bu kayitlar pilot search exportlaridir; final search execution, deduplication, screening veya PRISMA flow count olarak kullanilmayacaktir. Search freeze etiketi `planned search freeze date: June 30, 2026` olarak kalir.

## Canonical Raw Export Files

Canonical raw export klasoru:

- `systematic_review_workflow/02_arama/raw_exports/pilot_2026-06-19/`

| Search ID | Original file signal | Canonical file | Reported records | Exported rows | Column status | Prelim karar |
|---|---|---|---:|---:|---|---|
| SCO-PILOT-S1A | 40-row Scopus export | `SCO-PILOT-S1A_export_2026-06-19.csv` | 40 | 40 | adequate pilot metadata | keep candidate |
| SCO-PILOT-S1B | 60-row Scopus export | `SCO-PILOT-S1B_export_2026-06-19.csv` | 35 | 60 | metadata-light | keep candidate; verify mismatch |
| SCO-PILOT-S1F | 104-row Scopus export | `SCO-PILOT-S1F_export_2026-06-19.csv` | 103 | 104 | adequate pilot metadata | keep candidate; verify minor mismatch |

## Count QA Notes

- SCO-PILOT-S1A: reported records and exported rows match, 40 vs 40.
- SCO-PILOT-S1B: reported/export mismatch, 35 vs 60. Query/export settings must be verified before final search.
- SCO-PILOT-S1F: minor mismatch, 103 vs 104. This should be verified before final search.
- SCO-PILOT-S1B export is metadata-light; future final export should include Year, Source title, Document type, DOI, Abstract, Author keywords, Index keywords, and EID.

## Audit Notes

Extracted audit files are stored under:

- `systematic_review_workflow/02_arama/audits/pilot_2026-06-19/extracted/`

Relevant audit files:

- `scopus_pilot_export_audit_2026-06-19.csv`
- `scopus_pilot_unique_audit_2026-06-19.csv`
- `scopus_ieee_pilot_audit_summary_2026-06-19.md`

Audit summary reports Scopus total exported rows as 204 and Scopus unique records after DOI/title deduplication as 172. These are pilot audit diagnostics only and are not PRISMA flow counts.

## Corpus Handling Reminder

- Review/survey papers will be marked as contextual corpus and will not be counted as primary technical evidence.
- No included studies, screening counts, final search counts, or PRISMA flow counts are derived from these pilot exports.
- Legacy `included_studies_canonical.csv` will not be used as seed set or validation set in the formal PRISMA workflow.

## TODO

- Recover exact SCO-PILOT-S1A query string from chat log or Scopus database history.
- Recover exact SCO-PILOT-S1B query string from chat log or Scopus database history.
- Recover exact SCO-PILOT-S1F query string from chat log or Scopus database history.
- Verify SCO-PILOT-S1B reported/export mismatch before final search.
- Verify SCO-PILOT-S1F minor mismatch before final search.
