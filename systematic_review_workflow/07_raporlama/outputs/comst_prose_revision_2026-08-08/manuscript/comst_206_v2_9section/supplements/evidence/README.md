# O-ISAC Journal Evidence Supplements

Generated: 2026-08-13  
Status: materialized and denominator-QA-passed manuscript carriers; not a public repository release.

These files preserve the study-level and claim-level evidence required for transparent reporting without turning the survey prose into a catalogue. They were deterministically filtered from the already sanitized public staging projections. No publisher PDF, restricted database export, local path, credential, or long source-derived passage is included.

## Files

- `ST-16B_EXCLUDED_REPORTS_39_FOR_REPORTING.csv` (39 rows):
  publication-facing PRISMA Item 16b projection. Every assessed full-text
  exclusion is identified by DOI URL or full citation and has one primary
  reason. The internal source file additionally retains review-team notes that
  are not required for interpretation and are not redistributed.
- `ST-19_PRIMARY_EVIDENCE_RESULTS_3020.csv` (3,020 rows): PRISMA Item 19 support: 3,020 primary qualitative evidence records.
- `ST-19_PRIMARY_METRIC_RESULTS_4779.csv` (4,779 rows): PRISMA Item 19 support: 4,779 primary quantitative metric records.
- `ST-19_GOVERNED_TRADEOFFS_404.csv` (404 rows): Governed tradeoff ledger: 404 rows, including two explicit absence audit sentinels.
- `ST-19_SUBSTANTIVE_TRADEOFFS_402.csv` (402 rows): Scientific tradeoff view: 402 source-supported rows after excluding two absence sentinels.
- `ST-18_STUDY_LEVEL_TQAF_206.csv` (206 rows): Review-specific eight-dimension TQAF projection; not a conventional risk-of-bias tool.
- `ST-22_EVIDENCE_BODY_CERTAINTY_115.csv` (115 rows): Review-defined certainty summaries for 115 evidence bodies.
- `ST-22_EVIDENCE_BODY_MEMBERSHIP_4931.csv` (4,931 rows): Membership links connecting studies to the 115 review-defined evidence bodies.

## Boundaries

- The evidence and metric tables preserve source-reported values and existing governed classifications; they do not add graph digitization, imputed values, pooled effects, or a universal platform ranking.
- The 404-row tradeoff file is the complete governed audit view. The 402-row file is the scientific view after removal of two rows whose `reported_status` is `absent`.
- The TQAF table reports a deterministic, nonvalidated, review-specific technical appraisal. It must not be labelled risk of bias or GRADE.
- Evidence bodies are review-defined synthesis units, not additional studies.
- Study citations and 227-report lineage are materialized separately under ST-01.
- A manuscript may cite these files as supplementary material after final package naming and journal upload, but it must not call them publicly available until a repository release exists.

The package-level packing list and SHA-256 file enumerate the redistributed
files and provide their integrity gates. The dated internal evidence manifest
and combined QA workbook remain in the local audit archive rather than the
peer-review upload.
