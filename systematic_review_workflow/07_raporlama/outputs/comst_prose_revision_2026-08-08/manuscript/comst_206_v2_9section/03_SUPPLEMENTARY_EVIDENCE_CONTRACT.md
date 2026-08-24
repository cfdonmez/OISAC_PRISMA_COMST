# Supplementary Evidence Contract

## Purpose

This contract defines how the nine-section O-ISAC survey exposes complete
study, report, and claim provenance without turning the prose into a catalogue.
The current main manuscript cites all 206 included studies in scientifically
matched prose or table contexts. Supplementary carriers preserve the fuller
study, report, claim, condition, appraisal, and source-location trace that
cannot be carried efficiently in the article.

Main-text citation visibility and supplementary traceability have distinct
jobs. Every included study is visible in the article, while ST-01 resolves all
227 eligible reports and the evidence supplements expose the governed row-level
records. A main-text citation must remain attached to a specific mechanism,
boundary, contrast, or synthesis statement; complete coverage does not
authorize unrelated citation dumping.

This file is a production contract. It does not itself materialize a journal
supplement, create a new evidence result, or authorize a claim that a pending
carrier has already been released.

## Status vocabulary

- **Materialized source projection:** an existing, checked artifact that can
  supply a planned journal carrier.
- **Materialized public source:** an existing sanitized file in the draft
  public-release package, covered by that package's checksum manifest.
- **Materialized journal candidate:** a publication-facing local artifact that
  has passed its declared row-count, schema, join, leakage, and workbook checks
  but has not yet been uploaded to a journal or public repository.
- **Future/pending journal carrier:** the publication-facing table, workbook,
  or archive has not yet been assembled and audited under its final label.
- **Authority:** an existing locked or frozen input from which a carrier may be
  derived. An authority is not automatically the publication artifact.

No future/pending carrier may be described in the manuscript as “available,”
“provided,” or “released” until its row-count, schema, leakage, checksum, and
cross-reference checks pass.

## Verified authority map

All paths below are workspace-relative and were verified to exist.

| Evidence layer | Verified authority | Role in supplement production |
| --- | --- | --- |
| Locked Phase D | `prisma2020Review/systematic_review_workflow/04_veri_cekme/outputs/phase_d_survey_ready_2026-08-04/OISAC_PHASE_D_SURVEY_READY_2026-08-04.xlsx` | Authoritative study, report, metric, tradeoff, governance, and provenance ledgers. Locked SHA-256: `c1b3b89789c6ed3e20da5a6283e480875c1913e21af88ff59ac747a6aa949348`. |
| Frozen Phase E | `prisma2020Review/systematic_review_workflow/05_kalite_kanit/phase_e_tqaf_normalization_crosswalk_2026-08-04.json` | Authoritative 206-row normalization crosswalk for modality, validation maturity, artifact status, and 6G relevance. Frozen SHA-256: `41d6f8f574bdd0d6eba04806b2930ade8fa1d3d56e28b083de3d56bb13e7d122`. |
| Phase E TQAF audit | `prisma2020Review/systematic_review_workflow/05_kalite_kanit/phase_e_tqaf_dimension_audit_2026-08-04.csv` and `prisma2020Review/systematic_review_workflow/05_kalite_kanit/phase_e_tqaf_summary_2026-08-04.md` | Dimension-level calculation audit and final study-level distributions. |
| Final Phase F | `prisma2020Review/systematic_review_workflow/06_sentez/outputs/phase_f_s1_s7_2026-08-04/PHASE_F_S1_S7_PUBLICATION_SUMMARY.md` | Canonical publication counts and denominator rules for S1 through S7. |
| Phase F metric map | `prisma2020Review/systematic_review_workflow/06_sentez/outputs/phase_f_s1_s7_2026-08-04/s3_metric_domains.csv` and `s3_metric_families.csv` in the same directory | Aggregated checks for the primary 4,779 metric records. |
| Phase F tradeoff map | `prisma2020Review/systematic_review_workflow/06_sentez/outputs/phase_f_s1_s7_2026-08-04/s4_tradeoff_families.csv` | Aggregated governed-family checks. The table contains all 404 ledger rows, including two absence-status audit sentinels. |
| Phase F derivation | `prisma2020Review/systematic_review_workflow/06_sentez/outputs/phase_f_s1_s7_2026-08-04/derive_phase_f_synthesis.py` | Deterministic family and category derivation used to regenerate and audit future row-level projections. |
| Sanitized public staging | `prisma2020Review/systematic_review_workflow/07_raporlama/outputs/public_release_v1_0_0_staging_2026-08-07/OISAC_PRISMA_206_v1.0.0_DRAFT/` | Existing public projections for studies, claims, metrics, tradeoffs, TQAF, and lineage. This remains a draft staging package, not a released DOI-bearing deposit. |
| Public checksum manifest | `prisma2020Review/systematic_review_workflow/07_raporlama/outputs/public_release_v1_0_0_staging_2026-08-07/OISAC_PRISMA_206_v1.0.0_DRAFT/SHA256SUMS.txt` | Integrity authority for the materialized public source files. |
| Related-synthesis audit | `prisma2020Review/systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/qa/SECTION2_RELATED_SYNTHESIS_SOURCE_AUDIT.md` | Bounded 38-source contextual synthesis register and the 24/14 full-length versus short/focused split. |
| Context bibliography | `prisma2020Review/systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/references_context_candidate.bib` | Citation-key resolution for Table I and the internal contextual-synthesis audit. It is not a substitute for the source-function audit. |
| Internal contextual-synthesis audit | `prisma2020Review/systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/supplements/related_synthesis/` | Internal CSV/XLSX audit of the bounded 38-source register. It is retained for provenance but is not cited as ST-RS1, packaged, or submitted as an annex. |
| Materialized Supplement S7 | `prisma2020Review/systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/supplements/s7/` | A 206-row join audit plus a 12-study maximum-tier carrier that identifies the six-study paired-function subset. |
| Materialized ST-01 | `prisma2020Review/systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/supplements/st01/` | Citation-linked 206-study inventory, filtered 227-report lineage, exact-key bibliography inclusion fragment, and checked workbook. |
| Materialized journal evidence carriers | `prisma2020Review/systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/supplements/evidence/` | Publication-facing local projections for 39 exclusions, 3,020 evidence rows, 4,779 metric rows, 404 governed and 402 substantive tradeoff rows, 206 TQAF rows, 115 evidence bodies, and 4,931 memberships. |
| Materialized reporting carrier | `prisma2020Review/systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/supplements/reporting/` | Executed search records, protocol and dated amendments, eight protocol deviations, 446-field dictionary, and conduct boundaries. |

The public staging directory is a derived projection. If it disagrees with the
locked Phase D workbook, frozen Phase E crosswalk, or final Phase F counts, the
upstream authority wins and the journal carrier must be regenerated.

## Coverage architecture

The citation and evidence layers have separate jobs:

1. **Main prose:** retain claim-matched visibility for all 206 studies while
   keeping every citation attached to a sentence-level mechanism, contrast,
   exception, or evidence boundary. Do not append citations merely to inflate
   local density.
2. **Main tables and figures:** summarize families, counts, and comparison
   contracts. They may use representative citations but must retain the stated
   denominator and nonclaim.
3. **ST-01:** expose all 206 retained studies and their 227 eligible-report
   lineage in a compact sanitized inventory.
4. **Internal positioning audit:** retain the 38-source source-function audit
   for provenance without presenting it as a reader-facing annex or mixing it
   into the 206-study technical denominator.
5. **Claim supplements:** expose the primary metric and governed tradeoff
   ledgers with source locators, condition gates, use classes, and conflicts.
6. **Appraisal supplements:** expose the 206-row public TQAF projection and the
   narrower evidence-for-both-functions view without turning appraisal into a
   study leaderboard.

This layered design solves evidence visibility through traceability rather
than citation stuffing.

## ST-01: 206-study sanitized inventory

### Status

- **Content projection:** materialized and QA-passed.
- **Journal label and packaging as ST-01:** materialized in CSV, TeX, and XLSX;
  citation, lineage, and reopened-workbook QA passed.
- **Public repository release:** pending.

The publication-facing package is:

`supplements/st01/`

Its hard-gate records are:

`qa/FINAL_PRISMA_ITEM17_QA.json` and
`qa/FINAL_PRISMA_ITEM17_WORKBOOK_QA.json`.

The QA records confirm 206 unique study rows, 206 resolved citation keys, 206
real row citations, 206 unique primary reports, and 227 eligible reports across
the lineages. They also confirm the frozen modality and maximum-validation
distributions, no duplicate study rows, no unresolved bibliography joins, and
no detected source-path leakage.

### Required columns

ST-01 must preserve the already audited compact schema:

- `study_cluster_id`;
- `primary_report_id` and `primary_screening_record_id`;
- title, year, and venue;
- canonical modality;
- maximum validation maturity;
- study survey-use status;
- eligible-report count and eligible-report lineage; and
- independent-human-review status.
- resolved citation key and row-level citation token.

Additional columns may be joined only from an existing sanitized public source
and only when they answer a declared reader question. The richer materialized
public source is:

`prisma2020Review/systematic_review_workflow/07_raporlama/outputs/public_release_v1_0_0_staging_2026-08-07/OISAC_PRISMA_206_v1.0.0_DRAFT/data/included_studies_206_public.csv`

The study-specific survey-use projection is:

`prisma2020Review/systematic_review_workflow/07_raporlama/outputs/public_release_v1_0_0_staging_2026-08-07/OISAC_PRISMA_206_v1.0.0_DRAFT/data/study_survey_use_206_public.csv`

### ST-01 allowlist

- One row per `study_cluster_id`.
- Exactly one designated primary report per study.
- All eligible companion reports through the existing lineage field.
- The frozen exclusive modality and maximum-validation values.
- `survey_ready` or `survey_ready_with_claim_restrictions` without converting
  the latter into study exclusion.
- `independent_human_status=not_documented` as currently recorded.
- Stable identifiers needed to join metrics, tradeoffs, TQAF, and citations.

### ST-01 denylist

- The superseded 221-study predecessor as an attrition parent.
- The 67 contextual records as primary technical studies.
- Report rows counted as independent studies.
- Restricted abstract snippets, local file paths, browser state, private notes,
  credentials, or unpublished contact details.
- “Independently human verified,” “dual reviewed,” or equivalent wording.
- A quality rank inferred from modality, validation tier, or claim restriction.

### ST-01 denominator gate

The publication carrier must assert:

- study rows = 206;
- unique study identifiers = 206;
- primary reports = 206;
- total eligible reports represented by lineage = 227;
- survey-ready studies = 175;
- studies with at least one claim restriction = 31; and
- independent human review documented = 0 of 206.
- resolved study citation keys and visible ST-01 row citations = 206 of 206.

The existing `report_lineage_232_public.csv` contains 232 lineage rows because
it also retains three outside-272 lineage-only rows and two excluded full-text
rows. ST-01 may use only the 227 rows whose `final_decision` is
`include_primary` when reporting eligible-report lineage.

## Internal contextual-synthesis audit

### Status

- **Bounded 38-source audit:** materialized and retained internally.
- **Reader-facing annex:** not used. The matrix is excluded from the submission
  package and is not referenced from Table I.

The internal audit contains 38 unique contextual syntheses: 24 full-length or
independently citable sources and 14 short or focused sources. Table I displays
the 24 full-length sources through six exclusive primary navigation families.
Overlapping scope, secondary reader tasks, chronology, source form, and lineage
remain available only for internal provenance checks.

Seven of the 38 were identified during the manuscript-stage bounded update and
were not present in the executed exports. They remain contextual only. The
dated amendment is
`prisma2020Review/systematic_review_workflow/01_protokol/05_contextual_synthesis_positioning_update_2026-08-13.md`.
It changes no primary review denominator and does not claim worldwide
exhaustiveness.

The internal carriers are
`supplements/related_synthesis/ST-RS1_CONTEXTUAL_SYNTHESES_38.csv` and
`supplements/related_synthesis/ST-RS1_CONTEXTUAL_SYNTHESES_38.xlsx`. Their
hard-gate records are `qa/FINAL_ST_RS1_CONTEXTUAL_SYNTHESIS_QA_2026-08-13.json`
and `qa/FINAL_ST_RS1_WORKBOOK_QA_2026-08-13.json`. These paths are not part of
the journal supplement allowlist.

### Required internal-audit fields

- resolved citation key;
- title, authors, year, venue, and persistent identifier as already verified;
- source form: full-length/independently citable or short/focused;
- captured in executed workflow versus manuscript-stage bounded addition;
- one primary reader-task family used by Table I;
- multilabel secondary reader-task and scope tags;
- optical medium or network scope;
- native evidence unit and comparison logic;
- relationship or lineage flag when related outputs are retained separately;
- inclusion rationale under the synthesis-function rule; and
- neutral boundary statement.

### Internal-audit gates

- rows = 38 and unique citation keys = 38;
- full-length/independently citable = 24;
- short/focused = 14;
- every Table I key appears exactly once among the 24 primary assignments;
- all 38 remain outside the 206-study technical denominator;
- no present-survey self-score, checkmarks, quality rank, or first/only claim;
- no DOI, publication date, or lineage is copied from memory when it is absent
  from the audited register and resolved bibliography; and
- any later source addition triggers a dated amendment and a new 38-source
  denominator statement rather than silent insertion.

## Primary metric evidence supplement

### Status

- **4,861-row sanitized metric ledger:** materialized public source.
- **4,779-row primary publication projection:** materialized journal candidate
  at `supplements/evidence/ST-19_PRIMARY_METRIC_RESULTS_4779.csv`; denominator,
  disposition, leakage, checksum, and workbook QA passed.
- **Public repository release:** pending.

The source ledger is:

`prisma2020Review/systematic_review_workflow/07_raporlama/outputs/public_release_v1_0_0_staging_2026-08-07/OISAC_PRISMA_206_v1.0.0_DRAFT/data/metric_results_4861_public.csv`

The materialized primary projection selects the 4,779 rows whose
`final_survey_use_class` is `eligible_quantitative`. The other 82 rows are 31
`context_only` records and 51 `quarantined_conflict` records; neither group may
enter primary numerical synthesis.

### Required metric fields

- metric and study identifiers;
- source report and source locator;
- condition-set and linked tradeoff identifiers where present;
- metric domain, family, source-reported name, and measurement plane;
- validation type and result representation;
- reported value, interval, uncertainty, unit, origin, and normalization status;
- scenario and baseline;
- comparability and admissibility classes;
- claim status, survey-use class, reason code, and conflict flag; and
- independent-human-review status and source-workbook hash.

### Metric allowlist

- Only `eligible_quantitative` rows in the 4,779-record primary carrier.
- Source-reported values and explicitly source-reported calculations.
- Existing normalized values only when the ledger preserves the formula and
  input identifiers.
- Narrow conditional comparison when all recorded task, definition, plane,
  scenario, operating-condition, baseline, and validation gates align.
- Descriptive use when comparison is not admissible.

### Metric denylist

- The 31 context-only or 51 quarantined metric records in primary tables,
  plots, extrema, averages, or prevalence statements.
- Curve digitization or graph-read values not already recorded as such.
- Newly derived performance values or silent unit conversions.
- Substitution of OSNR, electrical SNR, received power, launch power, gross
  rate, net rate, range resolution, estimator error, RMSE, or a bound for one
  another.
- Treating the 4,779 records as independent effects or a meta-analytic sample.
- A universal maximum-value leaderboard.

### Metric denominator and QA gates

- source ledger = 4,861;
- primary projection = 4,779;
- context only = 31;
- quarantined conflict = 51;
- 4,779 + 31 + 51 = 4,861;
- cross-study quantitative comparison allowed with conditions = 118;
- cross-study quantitative comparison not allowed = 4,661; and
- no unconditional `yes` category is created.

The 118 conditionally admissible rows remain separate condition-bound records;
they are not one pooled comparison set.

## Governed and substantive tradeoff lineage

### Status

- **404-row governed public ledger:** materialized public source.
- **404-row governed journal view:** materialized at
  `supplements/evidence/ST-19_GOVERNED_TRADEOFFS_404.csv`.
- **402-row substantive publication view:** materialized at
  `supplements/evidence/ST-19_SUBSTANTIVE_TRADEOFFS_402.csv`.
- **Public repository release:** pending.

The governed ledger is:

`prisma2020Review/systematic_review_workflow/07_raporlama/outputs/public_release_v1_0_0_staging_2026-08-07/OISAC_PRISMA_206_v1.0.0_DRAFT/data/tradeoff_evidence_404_public.csv`

All 404 rows remain visible for audit. Two rows have
`reported_status=absent`; they preserve explicit review coverage but do not
describe substantive tradeoff evidence. The substantive view therefore uses
`reported_status != absent` and contains 402 records.

### Required lineage views

1. **Governed view:** 404 rows from 169 studies, including the two absence
   sentinels and their locators, status, and reason codes.
2. **Substantive view:** 402 rows from 168 studies after excluding the two
   absence sentinels from scientific-family plots and mechanism totals.
3. **Use-class view:** 218 eligible-quantitative and 184
   eligible-qualitative substantive rows.
4. **Conditionality view:** 371 conditionally comparable and 31 descriptive
   substantive rows.

The row-level publication projection may add the deterministic Phase F family
only by rerunning the verified Phase F derivation and reconciling it to
`s4_tradeoff_families.csv`. Family totals reported directly from that canonical
aggregate describe all 404 governed rows. If the two absence rows are removed,
family totals and unique-study counts must be recalculated after filtering;
they must not be subtracted from an arbitrary fallback family.

### Tradeoff allowlist

- Explicit quantitative, explicit qualitative, partial, architecture,
  implementation, security, synergy, and other source-supported coupling rows.
- Absence rows in the governed audit view only.
- Within-study numerical relationships under their recorded conditions.
- Qualitative cross-study synthesis by causal mechanism when numerical
  compatibility is absent.

### Tradeoff denylist

- Calling all 404 rows substantive evidence.
- Plotting the two absence sentinels as tradeoff observations.
- Treating multiple rows from one study as independent experiments.
- Summing family-level unique-study counts across overlapping families.
- A universal Pareto frontier, common exchange rate, or pooled effect.
- Relabelling synergistic or non-antagonistic coupling as a strict loss without
  preserving its source status.

### Tradeoff denominator gate

- governed records/studies = 404/169;
- absence sentinels = 2;
- substantive records/studies = 402/168;
- eligible quantitative + eligible qualitative = 218 + 184 = 402;
- conditional + descriptive = 371 + 31 = 402; and
- the 404/169 and 402/168 statements must always be labelled separately.

## TQAF public projection

### Status

- **206-row sanitized TQAF projection:** materialized public source.
- **Journal TQAF carrier:** materialized at
  `supplements/evidence/ST-18_STUDY_LEVEL_TQAF_206.csv`; denominator,
  instrument-boundary, leakage, checksum, and workbook QA passed.
- **Evidence-body carriers:** materialized at
  `supplements/evidence/ST-22_EVIDENCE_BODY_CERTAINTY_115.csv` and
  `supplements/evidence/ST-22_EVIDENCE_BODY_MEMBERSHIP_4931.csv`.
- **Public repository release:** pending.

The materialized public projection is:

`prisma2020Review/systematic_review_workflow/07_raporlama/outputs/public_release_v1_0_0_staging_2026-08-07/OISAC_PRISMA_206_v1.0.0_DRAFT/data/study_level_tqaf_206_public.csv`

The separate 115-body projection is:

`prisma2020Review/systematic_review_workflow/07_raporlama/outputs/public_release_v1_0_0_staging_2026-08-07/OISAC_PRISMA_206_v1.0.0_DRAFT/data/evidence_body_certainty_115_public.csv`

The 115 evidence bodies are not extra studies and must not be merged into the
206-row study appraisal table.

The local journal-candidate versions and their shared workbook are under
`supplements/evidence/`. Their denominator and workbook gates are
`qa/JOURNAL_EVIDENCE_SUPPLEMENT_QA_2026-08-13.json` and
`qa/JOURNAL_EVIDENCE_WORKBOOK_QA_2026-08-13.json`.

### Required TQAF fields and gates

- one row per study identifier;
- eight final dimensions: technical relevance, metric clarity, reporting
  completeness, validation maturity, reproducibility, benchmark readiness,
  comparison admissibility, and limitation transparency;
- the separate overall evidence-contribution category;
- TQAF version and instrument-boundary statement;
- rows = 206 and unique study identifiers = 206; and
- overall contribution = 125 strong, 75 adequate, and 6 low.

The publication note must state that TQAF is deterministic, review-specific,
and nonvalidated. It is not conventional risk of bias, GRADE certainty, or a
measure of scientific worth. The overall evidence-contribution value is not a
ninth input dimension.

### TQAF denylist

- Modality or author rankings based on TQAF.
- Mean or total “quality scores” not defined by the instrument.
- Converting adequate or low categories into exclusion decisions.
- Treating evidence-body certainty as a study-level score.
- Calling the appraisal independent duplicate human assessment.
- Inferring that open artifacts caused stronger validation or performance.

## Supplement S7: evidence for both functions

### Status

- **Underlying 206-row inventory and TQAF sources:** materialized.
- **Publication-facing Supplement S7:** materialized as a bounded 12-study
  carrier plus a 206-row join audit. Existing sources do not expose relationship
  timing or separate function-specific locator mappings; those fields are
  explicit `NR`, not inferred.

“Supplement S7” is a manuscript supplement label for the paired-function
validation view. It must not be confused with the Phase F synthesis domain S7,
which classifies 6G relevance as 138 direct, 64 inferred, 1 weak, and 3 not
applicable.

The paired-function carrier is produced by joining:

- maximum validation tier from the checked ST-01 source projection; and
- the TQAF `validation_maturity` field from the materialized 206-row public
  TQAF projection.

The join key is the study cluster identifier (`study_cluster_id` in ST-01 and
`study_id` in the TQAF public projection). The verified relationship is:

- 12 studies have maximum validation tier 6, meaning field trial or deployment
  was the strongest observed setting; and
- 6 of those 12 have TQAF validation-maturity score 3, which requires field or
  deployment evidence for both communication and sensing.

The six score-3 studies are a subset of the 12 maximum-tier studies. The other
six are not failed or invalid studies; they do not satisfy this review-specific
paired-function rule at the field/deployment setting.

### Required Supplement S7 fields

- study identifier and primary report identifier;
- canonical modality;
- maximum validation tier and its definition;
- TQAF validation-maturity category;
- communication evidence setting;
- sensing evidence setting;
- concurrent, sequential, replayed, or offline relationship when explicitly
  recorded;
- source locator supporting the field/deployment classification;
- source locator supporting each function; and
- bounded interpretation note.

The materialized carrier populates the communication and sensing
field/deployment outcome flags directly from the audited TQAF input, and it
retains the combined record-level locator trace supporting the validation
assessment. The existing audited projection does not expose the
concurrent/sequential/replayed/offline relationship or a separate mapping from
trace locators to the communication and sensing functions. Those three fields
therefore remain explicit `NR` values and must not be reconstructed from memory
or inferred from a maximum-tier label.

The artifacts are `supplements/s7/S7_CANONICAL_JOIN_206.csv`,
`supplements/s7/S7_PAIRED_FUNCTION_VALIDATION_12.csv`, and
`supplements/s7/S7_PAIRED_FUNCTION_VALIDATION_12.xlsx`. Their QA records are
`qa/FINAL_SUPPLEMENT_S7_PAIRED_FUNCTION_QA_2026-08-13.json` and
`qa/FINAL_SUPPLEMENT_S7_WORKBOOK_QA_2026-08-13.json`.

### Supplement S7 gates

- joined study rows = 206 before filtering;
- maximum field/deployment tier = 12;
- paired-function TQAF score 3 = 6;
- score-3 identifiers are a strict subset of the 12 maximum-tier identifiers;
- no equivalence between maximum tier 6 and TQAF validation score 3;
- no equivalence between Supplement S7 and Phase F S7 6G relevance; and
- no statement that a component tested in the field validates the complete
  communication and sensing system.

## Exclusion, evidence-result, and reporting carriers

The following journal-candidate carriers are also materialized locally and
covered by explicit QA. They remain unpublished until a persistent release is
created.

- `supplements/evidence/ST-16B_EXCLUDED_REPORTS_39.csv` identifies all 39
  full-text exclusions with a DOI URL or full citation, one primary reason,
  and an audit note. The six contextual reports are not counted as exclusions.
- `supplements/evidence/ST-19_PRIMARY_EVIDENCE_RESULTS_3020.csv` preserves the
  3,020 primary qualitative evidence records. It is a claim-level carrier, not
  a study table or a set of independent effects.
- `supplements/reporting/search/` contains the executed six-source search
  records. The exact query-to-export link for two low-yield Taylor & Francis
  exports could not be reconstructed and is disclosed rather than invented.
- `supplements/reporting/protocol/` contains the initial protocol and dated
  amendments. `S_PROTOCOL_DEVIATIONS_2026-08-13.csv` records eight changes,
  their rationales, timing, and effects.
- `supplements/reporting/S_DATA_DICTIONARY_446.csv` provides the sanitized
  446-field extraction dictionary, while
  `S_REVIEW_CONDUCT_AND_REPORTING_BOUNDARIES.md` states the executed reviewer
  roles and the analyses that were not performed.

The evidence-carrier gates are recorded in
`qa/JOURNAL_EVIDENCE_SUPPLEMENT_QA_2026-08-13.json`; the reporting-carrier gate
is `qa/REPORTING_SUPPLEMENT_QA_2026-08-13.json`.

## Cross-carrier provenance rules

Every publication carrier must include or inherit the following provenance:

- investigator-supervised and claim-governed review workflow;
- routine independent duplicate human screening, extraction, appraisal, and
  adjudication were not documented across the corpus;
- `independent_human_status=not_documented` remains visible where present;
- no authors of included studies were contacted;
- artifact availability reflects source reporting at extraction time;
- links were not universally retested and artifacts were not executed under a
  common protocol;
- no graph values were digitized and no new performance values were derived by
  the review;
- contextual syntheses remain outside the 206-study primary denominator; and
- the public-release directory is draft staging until release metadata,
  licensing, and deposition are finalized.

Every exported carrier must be generated deterministically from a verified
authority, preserve stable identifiers, record its generation date and source
hashes, and be added to a checksum manifest. Manual spreadsheet editing is not
an acceptable final production path.

## Global allowlist

The supplements may contain:

- sanitized bibliographic identity and stable study/report/claim identifiers;
- source locators already present in governed ledgers;
- frozen categories and deterministic Phase F mappings;
- source-reported values, units, definitions, conditions, baselines, and
  validation settings;
- explicit claim-use, conflict, quarantine, and comparison gates;
- review-specific appraisal categories with their instrument boundary; and
- bounded review inferences clearly marked as such.

## Global denylist

The supplements must not contain or imply:

- local source paths, credentials, browser state, private correspondence, or
  restricted source text;
- invented filenames, DOIs, citations, source locators, or artifact links;
- unresolved source conflicts presented as resolved values;
- context-only or quarantined claims in primary numerical synthesis;
- independent-review language not supported by the provenance record;
- the 221-study predecessor as a parent denominator for the final 206;
- reports, claims, conflict events, evidence bodies, and studies treated as
  interchangeable units;
- causal effects, publication-bias conclusions, sensitivity results, or pooled
  estimates that were not performed; or
- a first, only, most comprehensive, universal, or platform-ranking claim.

## Denominator firewall

The following units must remain distinct in captions, notes, and joins:

| Unit | Canonical count | Permitted meaning | Prohibited substitution |
| --- | ---: | --- | --- |
| Contextual synthesis | 38 | Bounded prior-synthesis positioning set | Included technical study |
| Search record | 1,733 | Identified record | Report or study |
| Screened record | 1,259 | Title/abstract screening unit | Full-text report |
| Report sought | 330 | Unique full-text report sought | Included study |
| Report assessed | 272 | Full-text report assessed | Eligible report |
| Eligible report | 227 | Eligible reports before study consolidation | Unique study |
| Public lineage row | 232 | 227 eligible plus 3 outside-lineage and 2 excluded audit rows | Eligible-report denominator without filtering |
| Included study | 206 | Unique study cluster | Report, claim, or evidence body |
| Governed coding record | 8,306 | 3,041 evidence + 4,861 metric + 404 tradeoff records | Primary synthesis record |
| Primary coding record | 8,203 | 3,020 evidence + 4,779 metric + 404 tradeoff records | Independent effect |
| Context-only coding record | 31 | Contextual claim use only | Primary numerical evidence |
| Quarantined coding record | 72 | Unresolved conflict exclusion from primary synthesis | Study exclusion |
| Primary metric record | 4,779 | Condition-bound metric extraction row | Comparable effect or study |
| Governed tradeoff record | 404 from 169 studies | Full audit ledger including two absence rows | Substantive tradeoff universe |
| Substantive tradeoff record | 402 from 168 studies | Source-supported coupling relationship | Independent experiment or universal frontier |
| TQAF study row | 206 | One review-specific appraisal per study | Risk-of-bias grade or evidence body |
| Evidence body | 115 | Review-defined synthesis body | Study or claim count |
| Conflict audit event | 93 | Conflict-register event | Quarantined claim count |

Any caption or sentence that uses two of these units must name both units and
explain the mapping. Silent denominator switching is a blocking QA failure.

## Release and citation QA

Before any supplement is cited as available, run all of the following checks:

1. **Existence:** the publication artifact exists under its declared label.
2. **Authority:** every row resolves to the stated locked/frozen authority.
3. **Row counts:** all carrier-specific denominator assertions pass.
4. **Uniqueness:** identifiers are unique at the carrier's declared unit.
5. **Join integrity:** all foreign keys resolve and no join multiplies rows
   unintentionally.
6. **Disposition integrity:** context-only, quarantine, absence-sentinel, and
   restriction rules are preserved.
7. **Citation integrity:** every citation key resolves; no title-only or
   memory-based citation is inserted.
8. **Leakage:** no local path, restricted source text, credential, or private
   note is present.
9. **Checksum:** the final artifact is added to a checksum manifest after QA.
10. **Manuscript link:** each main-text supplement reference uses the final
    carrier label and makes no stronger availability claim than its status.
11. **Narrative audit:** the main prose still cites the most relevant source
    for each sentence; supplement coverage has not been used to excuse a
    citation-free technical claim.
12. **No stuffing:** citations are not added solely to maximize the number of
    primary studies named in prose.

## Acceptance criteria

The supplementary evidence layer is complete only when:

- ST-01 is packaged and reconciles 206 studies to 227 eligible reports;
- the internal positioning audit retains all 38 contextual syntheses outside
  the primary denominator without becoming a submitted annex;
- the metric carrier contains exactly 4,779 primary rows and excludes all 31
  context-only and 51 quarantined metric rows;
- the governed tradeoff carrier retains 404 rows and exposes a separately
  filtered 402-row substantive view;
- the TQAF public projection contains 206 unique study rows and preserves its
  nonvalidated review-specific boundary;
- Supplement S7 reconciles 12 maximum field/deployment studies with the 6-study
  evidence-for-both-functions subset without conflating it with Phase F S7;
- all materialized journal candidates pass provenance, denominator, identifier, leakage,
  checksum, and manuscript-link QA; and
- the survey's scientific claims remain readable and selectively cited rather
  than becoming a catalogue of 206 citation tokens.
