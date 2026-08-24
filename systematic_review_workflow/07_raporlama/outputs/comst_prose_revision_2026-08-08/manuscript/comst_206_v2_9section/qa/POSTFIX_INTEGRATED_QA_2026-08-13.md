# Post-fix Integrated QA — 2026-08-13

Status: `PASS_NONVISUAL_CLOSEOUT_FIGURES_ONLY`

PASS means the compiled local manuscript, direct-citation bibliography, eight live tables, standalone 206-study supplement, and other materialized supplements satisfy the tested nonvisual gates. Figures 1-8 and their post-insertion page-budget check remain; portal attestations and a public persistent release are external actions.

## Tested gates

| Gate | Status | Observed | Expected |
| --- | --- | --- | --- |
| section_files | PASS | `["00_ABSTRACT.tex", "01_INTRODUCTION.tex", "02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex", "03_REVIEW_METHOD_AND_EVIDENCE_BASE.tex", "04_OPTICAL_PLATFORMS_AND_INTEGRATION_ARCHITECTURES.tex", "05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex", "06_VALIDATION_REPRODUCIBILITY_AND_BENCHMARK_READINESS.tex", "07_ENABLING_TECHNOLOGIES_APPLICATIONS_AND_6G.tex", "08_DISCUSSION_ROADMAP_AND_LIMITATIONS.tex", "09_CONCLUSION.tex"]` | `["00_ABSTRACT.tex", "01_INTRODUCTION.tex", "02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex", "03_REVIEW_METHOD_AND_EVIDENCE_BASE.tex", "04_OPTICAL_PLATFORMS_AND_INTEGRATION_ARCHITECTURES.tex", "05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex", "06_VALIDATION_REPRODUCIBILITY_AND_BENCHMARK_READINESS.tex", "07_ENABLING_TECHNOLOGIES_APPLICATIONS_AND_6G.tex", "08_DISCUSSION_ROADMAP_AND_LIMITATIONS.tex", "09_CONCLUSION.tex"]` |
| main_section_count | PASS | `9` | `9` |
| abstract_word_limit | PASS | `225` | `"150-250"` |
| tqaf_canonical_name | PASS | `"Assessment"` | `"Technical Quality Assessment Framework"` |
| study_bibliography | PASS | `{"entries": 206, "unique": 206}` | `206` |
| duplicate_bib_keys | PASS | `[]` | `[]` |
| section_citations_resolve | PASS | `[]` | `[]` |
| duplicate_labels | PASS | `[]` | `[]` |
| cross_references_resolve | PASS | `[]` | `[]` |
| brace_balance | PASS | `[]` | `[]` |
| environment_balance | PASS | `[]` | `[]` |
| item17_st01 | PASS | `{"rows": 206, "studies": 206, "keys": 206, "row_citations": 206}` | `{"rows": 206, "studies": 206, "keys": 206, "row_citations": 206}` |
| explicit_bibliography_inclusion | PASS | `{"keys": 206, "unique": 206, "wildcard": false}` | `{"keys": 206, "unique": 206, "wildcard": false}` |
| eligible_report_lineage | PASS | `{"rows": 227, "reports": 227, "studies": 206}` | `{"rows": 227, "reports": 227, "studies": 206}` |
| excluded_reports | PASS | `{"rows": 39, "unique": 39}` | `{"rows": 39, "unique": 39}` |
| primary_evidence | PASS | `{"rows": 3020, "unique": 3020}` | `{"rows": 3020, "unique": 3020}` |
| primary_metrics | PASS | `{"rows": 4779, "unique": 4779}` | `{"rows": 4779, "unique": 4779}` |
| governed_tradeoffs | PASS | `{"rows": 404, "unique": 404}` | `{"rows": 404, "unique": 404}` |
| substantive_tradeoffs | PASS | `{"rows": 402, "unique": 402}` | `{"rows": 402, "unique": 402}` |
| study_tqaf | PASS | `{"rows": 206, "unique": 206}` | `{"rows": 206, "unique": 206}` |
| evidence_bodies | PASS | `{"rows": 115, "unique": 115}` | `{"rows": 115, "unique": 115}` |
| evidence_memberships | PASS | `{"rows": 4931, "unique": "not_applicable"}` | `{"rows": 4931, "unique": "not_applicable"}` |
| contextual_syntheses | PASS | `{"rows": 38, "unique": 38}` | `{"rows": 38, "unique": 38}` |
| s7_join | PASS | `{"rows": 206, "unique": 206}` | `{"rows": 206, "unique": 206}` |
| s7_field_subset | PASS | `{"rows": 12, "unique": 12}` | `{"rows": 12, "unique": 12}` |
| tradeoff_lineage | PASS | `{"governed_studies": 169, "substantive_studies": 168, "governed_absent": 2, "substantive_absent": 0}` | `{"governed_studies": 169, "substantive_studies": 168, "governed_absent": 2, "substantive_absent": 0}` |
| s7_paired_subset | PASS | `6` | `6` |
| standalone_item17_integration | PASS | `{"study_table": "present", "bibliography": "present", "forced_main_bibliography": "absent"}` | `{"study_table": "present", "bibliography": "present", "forced_main_bibliography": "absent"}` |
| active_state_not_stale | PASS | `{"item17_open": false, "st01_pending": false, "metric_pending": false, "tradeoff_pending": false, "tqaf_pending": false, "unregistered": false, "tqaf_wrong_name": false}` | `{"item17_open": false, "st01_pending": false, "metric_pending": false, "tradeoff_pending": false, "tqaf_pending": false, "unregistered": false, "tqaf_wrong_name": false}` |
| novelty_overclaim | PASS | `[]` | `[]` |
| live_visual_truth | PASS | `{"table_environments": 9, "logical_tables": 8, "figures": 0}` | `{"table_environments": 9, "logical_tables": 8, "figures": 0}` |
| required_component_qa | PASS | `["FINAL_PRISMA_ITEM17_QA.json", "FINAL_PRISMA_ITEM17_WORKBOOK_QA.json", "JOURNAL_EVIDENCE_SUPPLEMENT_QA_2026-08-13.json", "JOURNAL_EVIDENCE_WORKBOOK_QA_2026-08-13.json", "REPORTING_SUPPLEMENT_QA_2026-08-13.json", "FINAL_ST_RS1_CONTEXTUAL_SYNTHESIS_QA_2026-08-13.json", "FINAL_ST_RS1_WORKBOOK_QA_2026-08-13.json", "FINAL_SUPPLEMENT_S7_PAIRED_FUNCTION_QA_2026-08-13.json", "FINAL_SUPPLEMENT_S7_WORKBOOK_QA_2026-08-13.json", "MANUSCRIPT_CLAIM_REAUDIT_2026-08-13.json", "FRONT_MATTER_RELEASE_REAUDIT_2026-08-13.json"]` | `["FINAL_PRISMA_ITEM17_QA.json", "FINAL_PRISMA_ITEM17_WORKBOOK_QA.json", "JOURNAL_EVIDENCE_SUPPLEMENT_QA_2026-08-13.json", "JOURNAL_EVIDENCE_WORKBOOK_QA_2026-08-13.json", "REPORTING_SUPPLEMENT_QA_2026-08-13.json", "FINAL_ST_RS1_CONTEXTUAL_SYNTHESIS_QA_2026-08-13.json", "FINAL_ST_RS1_WORKBOOK_QA_2026-08-13.json", "FINAL_SUPPLEMENT_S7_PAIRED_FUNCTION_QA_2026-08-13.json", "FINAL_SUPPLEMENT_S7_WORKBOOK_QA_2026-08-13.json", "MANUSCRIPT_CLAIM_REAUDIT_2026-08-13.json", "FRONT_MATTER_RELEASE_REAUDIT_2026-08-13.json"]` |

## Remaining gates

- Production, insertion, and rendered inspection of Figures 1-8.
- Post-figure verification against the 30-page COMST submission limit.
- Author portal attestations and final upload actions.
- Optional public repository release, persistent URL, and archive DOI.

The pre-fix PRISMA and architecture reports remain historical snapshots. Their
old 76/206 citation-coverage and pending-supplement observations must not be
used as the current candidate state. `MANUSCRIPT_STRUCTURE.json` and the root
README now point to this post-fix gate and the post-fix PRISMA matrix.
