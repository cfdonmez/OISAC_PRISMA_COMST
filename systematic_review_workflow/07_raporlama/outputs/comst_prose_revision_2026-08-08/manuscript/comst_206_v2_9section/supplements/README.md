# Electronic Supplementary Material

This directory contains the electronic evidence and reporting carriers that
support the 206-study O-ISAC survey. The materials are intended to accompany
the manuscript during peer review. They are not a public repository release
and have no persistent public DOI.

## Contents

### `st01/` -- included studies and report lineage

- `ST01_INCLUDED_STUDIES_206.csv` and `.xlsx`: citation linked characteristics
  for every included unique study;
- `ST01_ELIGIBLE_REPORT_LINEAGE_227.csv`: 206 primary reports and 21 eligible
  companion reports mapped to the same 206 study clusters;
- `ST01_COMPANION_REPORT_PROVENANCE_21.csv` and `.tex`: report-level evidence,
  metric, and tradeoff provenance for every companion report;
- `ST01_COMPANION_GUARDRAIL_METRICS_14.csv`: report-specific conditions that
  must remain attached to companion-derived metric claims;
- `ST01_SUPPLEMENT_DRIVER.pdf`: standalone review supplement whose 206 study
  rows cite all 227 eligible reports; and
- the TeX projections, 206-entry compatibility bibliography, combined
  227-entry bibliography, and explicit bibliography fragment are build
  carriers and are not separate evidence denominators.

### `evidence/` -- exclusions, governed claims, appraisal, and certainty

- 39 full text exclusions with one primary reason;
- 3,020 primary evidence records;
- 4,779 primary metric records;
- 404 governed tradeoff records and the 402-row substantive projection;
- eight-dimension TQAF records for 206 studies;
- 115 evidence body ratings and 4,931 study to body memberships;
- machine readable CSV carriers with package-level hashes and a packing list.

### `s7/` -- paired function validation boundary

The canonical 206-row join identifies 12 studies at the highest recorded field
or deployment tier. Six satisfy the narrower paired communication and sensing
validation gate. Missing function specific locators remain explicitly not
reported rather than inferred.

### `reporting/` -- search, protocol, and data dictionary

This package records the executed source searches, the initial protocol and
dated amendments, conduct and reporting boundaries, 446 dictionary fields,
and the deviation register. Two Taylor and Francis export rows retain an
unreconstructed query to export mapping; no query was invented.

The manuscript carrier names resolve to these exact local paths:

| Manuscript alias | Exact carrier path or paths |
|---|---|
| ST-01 | `st01/ST01_SUPPLEMENT_DRIVER.pdf`; source inventory `st01/ST01_INCLUDED_STUDIES_206.csv` and `st01/ST01_INCLUDED_STUDIES_206.xlsx`; report lineage `st01/ST01_ELIGIBLE_REPORT_LINEAGE_227.csv` |
| S-Search | `reporting/search/FINAL_SEARCH_EXECUTION_AND_STRATEGIES_FOR_REPORTING_2026-08-14.csv` and `reporting/search/FINAL_SEARCH_METHODS_AND_EXECUTION_FOR_REPORTING_2026-08-14.md` |
| S-Protocol | `reporting/protocol/protocol_initial_2026-06-17.md`; `reporting/protocol/protocol_amendment_actual_workflow_2026-08-04.md`; `reporting/protocol/protocol_registration_lineage_correction_2026-08-07.md`; `reporting/protocol/contextual_synthesis_positioning_update_2026-08-13.md`; `reporting/protocol/contextual_synthesis_reporting_disposition_2026-08-17.md`; `reporting/S_PROTOCOL_DEVIATIONS_2026-08-13.csv`; `reporting/S_REVIEW_CONDUCT_AND_REPORTING_BOUNDARIES.md` |
| S-Flow | `st01/ST01_ELIGIBLE_REPORT_LINEAGE_227.csv` |
| S-Studies | `st01/ST01_INCLUDED_STUDIES_206.csv` and `st01/ST01_INCLUDED_STUDIES_206.xlsx` |
| S-Data Dictionary | `reporting/S_DATA_DICTIONARY_446.csv` |
| S-Exclusions | `evidence/ST-16B_EXCLUDED_REPORTS_39_FOR_REPORTING.csv` |
| S-Appraisal | `evidence/ST-18_STUDY_LEVEL_TQAF_206.csv` |
| S-Evidence | `evidence/ST-19_PRIMARY_EVIDENCE_RESULTS_3020.csv`; `evidence/ST-19_PRIMARY_METRIC_RESULTS_4779.csv`; `evidence/ST-19_GOVERNED_TRADEOFFS_404.csv`; `evidence/ST-19_SUBSTANTIVE_TRADEOFFS_402.csv` |
| S-Bodies | `evidence/ST-22_EVIDENCE_BODY_CERTAINTY_115.csv` and `evidence/ST-22_EVIDENCE_BODY_MEMBERSHIP_4931.csv` |
| S7 | `s7/S7_CANONICAL_JOIN_206.csv`; `s7/S7_PAIRED_FUNCTION_VALIDATION_12.csv`; `s7/S7_PAIRED_FUNCTION_VALIDATION_12.xlsx` |

## Counting rules

- Reports and studies are different units: 227 eligible reports map to 206
  unique studies.
- The 221-study OSF snapshot is a retrospective predecessor state, not an
  attrition denominator.
- The governed tradeoff ledger contains 404 rows from 169 studies. Removing
  two explicit absence status audit rows yields 402 substantive rows from 168
  studies.
- Contextual syntheses are not primary technical evidence.

## Redistribution boundary

Publisher PDFs, publisher full text, restricted database exports, credentials,
private notes, internal actor identifiers, and raw internal tool artifacts are
not included. The supplied files contain derived review records and
bibliographic identifiers needed to interpret the survey.

`SUPPLEMENT_PACKING_LIST_2026-08-17.csv` enumerates the peer review files and
their roles. `SUPPLEMENT_SHA256_2026-08-17.txt` records their hashes. The clean
upload directory and ZIP archive are generated from that allowlist; QA previews
and workbook inspection traces are excluded from the upload archive.
