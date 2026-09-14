# Supplement source index

Checked: 14 September 2026.

[methods.md](methods.md) is the V3 supplementary methods narrative. This index identifies the existing source files behind its aliases. The frozen source files have now been copied into this worktree for transfer. This is not a claim that they have been uploaded to OSF.

The frozen source package is [submission_supplement_final_v10_2026-08-17](v10). Paths below are relative to that package unless a worktree link is explicitly supplied. The original source package was read only; the portable `v10/` copy retains its file bytes and manifests. Its [packing list](v10/SUPPLEMENT_PACKING_LIST_2026-08-17.csv) and [SHA-256 manifest](v10/SUPPLEMENT_SHA256_2026-08-17.txt) identify the frozen files.

## S-Search

The [search methods record](v10/reporting/search/FINAL_SEARCH_METHODS_AND_EXECUTION_FOR_REPORTING_2026-08-14.md) and [19-run strategy table](v10/reporting/search/FINAL_SEARCH_EXECUTION_AND_STRATEGIES_FOR_REPORTING_2026-08-14.csv) correspond to:

- `reporting/search/FINAL_SEARCH_METHODS_AND_EXECUTION_FOR_REPORTING_2026-08-14.md`
- `reporting/search/FINAL_SEARCH_EXECUTION_AND_STRATEGIES_FOR_REPORTING_2026-08-14.csv`

They contain source queries, limits, execution dates, exported counts, and reconstruction limits. Restricted raw database exports are not included in this package.

## S-Protocol

The [protocol folder](v10/reporting/protocol) contains:

- `reporting/protocol/protocol_initial_2026-06-17.md`: initial internal protocol; dated amendments supersede its planned wording where conduct changed.
- `reporting/protocol/protocol_amendment_actual_workflow_2026-08-04.md`: executed investigator and AI roles, extraction restrictions, and departures from planned reviewer independence.
- `reporting/protocol/protocol_registration_lineage_correction_2026-08-07.md`: retrospective registration and the distinction between the earlier 221-study state and final 206-study corpus.
- `reporting/protocol/contextual_synthesis_positioning_update_2026-08-13.md`: bounded addition of seven contextual syntheses.
- `reporting/protocol/contextual_synthesis_reporting_disposition_2026-08-17.md`: subsequent disposition of contextual reporting materials, with no primary denominator change.

Two further files complete this alias:

- [reporting/S_PROTOCOL_DEVIATIONS_2026-08-13.csv](v10/reporting/S_PROTOCOL_DEVIATIONS_2026-08-13.csv): eight material departures or lineage corrections.
- [reporting/S_REVIEW_CONDUCT_AND_REPORTING_BOUNDARIES.md](v10/reporting/S_REVIEW_CONDUCT_AND_REPORTING_BOUNDARIES.md): executed conduct, TQAF rules, synthesis-group rating rules, and nonperformed procedures.

The initial protocol, historical amendments, and this V3 narrative serve different purposes. Earlier plans for prospective registration, duplicate review, or other unperformed procedures must be read with the executed-workflow and lineage corrections.

## ST-01

The [standalone ST-01 supplement](v10/st01/ST01_SUPPLEMENT_DRIVER.pdf) is supported by:

- `st01/ST01_INCLUDED_STUDIES_206.csv` and `.xlsx`: one entry for each of 206 studies.
- [st01/ST01_ELIGIBLE_REPORT_LINEAGE_227.csv](v10/st01/ST01_ELIGIBLE_REPORT_LINEAGE_227.csv): one entry for each of 227 eligible reports.
- `st01/ST01_COMPANION_REPORT_PROVENANCE_21.csv` and `.tex`: source provenance for 21 companion reports.
- `st01/ST01_COMPANION_GUARDRAIL_METRICS_14.csv`: report-specific conditions for 14 companion-derived metric records.
- `st01/ST01_REFERENCES_227.bib`: bibliography for all eligible reports.

The [ST-01 README](v10/st01/README.md) identifies the corresponding TeX and bibliography build files.

## S-Data Dictionary

[reporting/S_DATA_DICTIONARY_446.csv](v10/reporting/S_DATA_DICTIONARY_446.csv) contains 446 field and code entries, including definitions and missing-data rules.

## S-Evidence

The source files are:

- [evidence/ST-19_PRIMARY_EVIDENCE_RESULTS_3020.csv](v10/evidence/ST-19_PRIMARY_EVIDENCE_RESULTS_3020.csv): 3,020 primary evidence items.
- [evidence/ST-19_PRIMARY_METRIC_RESULTS_4779.csv](v10/evidence/ST-19_PRIMARY_METRIC_RESULTS_4779.csv): 4,779 primary metric records.
- [evidence/ST-19_GOVERNED_TRADEOFFS_404.csv](v10/evidence/ST-19_GOVERNED_TRADEOFFS_404.csv): 404 tradeoff records, including two absence records.
- [evidence/ST-19_SUBSTANTIVE_TRADEOFFS_402.csv](v10/evidence/ST-19_SUBSTANTIVE_TRADEOFFS_402.csv): the 402 substantive relationships from that tradeoff table.

A portable worktree copy of the [4,779-record metric table](../evidence/inputs/ST-19_PRIMARY_METRIC_RESULTS_4779.csv) is already present. Its column order and every parsed cell match the frozen source, checked across all 4,779 rows on 14 September 2026. The file hashes differ, so byte-for-byte identity is not claimed:

- Frozen source SHA-256: `DAC20625EF18C97BAC289F6AA05C2E2A75172E14CC76745780DDEDF9B689C539`
- Worktree copy SHA-256: `EFD34C2A0512EA5E4CC58A3FDCAE0DEEA9D3F76FA4AA51BE95E69B4ECEDBCCD8`

The 8,306-record full-register total is documented in the actual-workflow amendment. S-Evidence contains the 8,203 primary records; it does not include the 31 contextual and 72 conflicted records as additional primary data.

## S-Appraisal

[evidence/ST-18_STUDY_LEVEL_TQAF_206.csv](v10/evidence/ST-18_STUDY_LEVEL_TQAF_206.csv) supplies eight TQAF dimensions and separate overall evidence contribution for each of 206 studies. The scoring and interpretation rules are in the conduct-and-reporting record listed under S-Protocol.

## S-Bodies

- [evidence/ST-22_EVIDENCE_BODY_CERTAINTY_115.csv](v10/evidence/ST-22_EVIDENCE_BODY_CERTAINTY_115.csv): 115 synthesis-group summaries; 111 are marked substantive for survey conclusions and four are not.
- [evidence/ST-22_EVIDENCE_BODY_MEMBERSHIP_4931.csv](v10/evidence/ST-22_EVIDENCE_BODY_MEMBERSHIP_4931.csv): 4,931 study-to-group membership links.

The conduct-and-reporting record under S-Protocol describes the review-specific group appraisal rules. File names containing “certainty” do not denote GRADE ratings.

## S-Exclusions

[evidence/ST-16B_EXCLUDED_REPORTS_39_FOR_REPORTING.csv](v10/evidence/ST-16B_EXCLUDED_REPORTS_39_FOR_REPORTING.csv) identifies the 39 full-text exclusions and one primary reason per report. It is not a complete ledger of all title/abstract decisions, unretrieved reports, or contextual dispositions. The six contextual full-text reports remain separate from these exclusions in the selection flow.

## Reporting checklist

The frozen v10 package and its packing list contain no completed PRISMA reporting checklist. The [current reporting-location map](../governance/review.md#reporting-location-map) identifies the revised manuscript and supplement destinations. That map is a project record; it is not a submitted checklist or a claim of full PRISMA checklist completion. Earlier section, figure, and page references in source snapshots must not be treated as current V3 locations.

## Packaging status

The two Markdown files in this folder are new V3 materials. The complete frozen v10 package is now included under `v10/` for GitHub transfer, with its original packing list and SHA-256 manifest. All carrier links above resolve inside this repository. The transfer provenance and per-file hashes are recorded in [handoff/files.json](../handoff/files.json). This packaging action does not update OSF. The existing `evidence/inputs/OISAC_COMST_OVERLEAF_CORE_2026-08-25.zip` remains a separate manuscript baseline.

The final manuscript and OSF archive update are to be completed together under the author's 14 September 2026 plan. Packaging must include the chosen supporting carriers and the revised methods narrative, resolve final archive links, and check version consistency. This change performed no OSF download, upload, publication, or registration edit. The scientific methods narrative retains the retrospective registration history independently of the later archive update.
