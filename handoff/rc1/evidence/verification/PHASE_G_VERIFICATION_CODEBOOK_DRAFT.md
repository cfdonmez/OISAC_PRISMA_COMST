# Phase G Verification Codebook

Status: `DRAFT_REQUIRES_G1_LOCK`

This codebook governs the two independent human-review forms for the 118
conditional-comparison candidates. It does not verify any source, authorize a
numeric manuscript claim, or pass G1/G2.

## 1. Frozen inputs

| Input | Rows / role | SHA-256 |
|---|---|---|
| `governance/plan_snapshot/01_verification/full_118_verification_register.csv` | 118-row Phase G candidate register | `77A91B8A34F5CA964D519F4E2759C8554759276D8BB683F4BDD14B5959A49B0B` |
| `evidence/inputs/ST-19_PRIMARY_METRIC_RESULTS_4779.csv` | 4,779-row canonical metric authority | `DAC20625EF18C97BAC289F6AA05C2E2A75172E14CC76745780DDEDF9B689C539` |
| `governance/plan_snapshot/01_verification/DOUBLE_HUMAN_VERIFICATION_PROTOCOL.md` | governing draft protocol | `4CC462003CB381120A0B08F476EC5405F6E9C249F3B3F24C55E2499B01ABED32` |

The join key is `register.metric_record_id =
ST-19.metric_record_id`; the review forms expose it as
`source_metric_record_id`. The register must contain exactly 118 unique keys,
and each key must match exactly one ST-19 row.

## 2. Blind-form invariant

`VERIFICATION_REVIEWER_V1_BLIND.csv` and
`VERIFICATION_REVIEWER_V2_BLIND.csv` have the same schema, row order, and
118-key set. At issuance, their bytes are identical. Columns 1--39 are frozen
navigation/context fields copied only from ST-19 or the register. Columns
40--81, beginning with `reviewer_code`, are human-entry fields and must be
blank at issuance.

V1 and V2 must be assigned to different humans and stored separately. Neither
reviewer may inspect the other form, progress, notes, or decisions before both
forms are `COMPLETE_LOCKED`. AI may prepare the blank forms and locate a source
for a human; AI is not V1, V2, or the adjudicator.

## 3. Canonical context columns

The `canonical_*` columns preserve ST-19 values verbatim: study/report/condition
identity, metric/task domain, measurement plane, validation type, result
representation, operator/value/bounds/uncertainty/unit, scenario, baseline,
comparison metadata, locators, survey-use metadata, human-status metadata, and
source-workbook hash. The three `register_*` columns preserve the register's
comparison flag and documented human-status fields.

These values are leads, not verified answers. Reviewers must consult the exact
source report and enter their own findings in the `reviewed_*` and decision
columns. A canonical blank must not be inferred or silently copied into a
reviewed field.

## 4. Human-entry fields

### Source identity

- `reviewer_code`, `review_date_utc`
- `reviewed_source_report_title`, `reviewed_source_report_doi`
- `reviewed_companion_relationship`, `reviewed_source_pdf_sha256`
- `source_pdf_opened`, `source_identity_decision`

`reviewed_source_pdf_sha256` is the hash of the file actually opened. DOI may
be `NR` if the source explicitly lacks one. Companion status is established
from the report packet, not guessed from a title.

### Locator and metric definition

- `reviewed_pdf_page`, `reviewed_section_heading`, `reviewed_table_id`,
  `reviewed_figure_id`, `reviewed_equation_id`
- `source_locator_decision`
- `reviewed_metric_name`, `reviewed_metric_definition`

Page is required for every retained numeric claim. Inapplicable table, figure,
or equation locators must be written as `NR`, not left blank at lock.

### Value, unit, and uncertainty

- `reviewed_comparison_operator`
- `reviewed_value_numeric`, `reviewed_value_low`, `reviewed_value_high`
- `reviewed_uncertainty_type`, `reviewed_uncertainty_value`
- `reviewed_unit_reported`

Transcribe source strings without conversion, rounding, sign repair, or graph
digitization. For a scalar, use `reviewed_value_numeric`; for a reported range,
use both low and high. An explicit threshold retains its operator. If the
source does not report uncertainty, use `NR`; if it cannot be resolved after
inspection, use `UNC`.

### Plane, tasks, conditions, and validation

- `reviewed_measurement_plane_code`, `reviewed_reference_point`
- `reviewed_communication_task`, `reviewed_sensing_task`,
  `reviewed_objective`
- `reviewed_scenario_summary`, `reviewed_geometry`,
  `reviewed_condition_set_id`
- `reviewed_baseline_comparator`, `reviewed_validation_type_code`,
  `reviewed_value_origin`

The reviewer records what the source supports. A missing baseline is `NR`; it
must not be synthesized from a nearby experiment. Allowed `reviewed_value_origin`
values are `reported`, `source_calculated`, `digitized`, `NR`, or `UNC`.
`digitized` cannot be retained under the current protocol without a separately
approved method amendment.

### Comparison and survey use

- `reviewed_comparison_group_id`
- `comparison_decision`, `comparison_decision_rationale`
- `survey_use_decision`, `verification_outcome`
- `reviewer_notes`, `reviewer_lock_status`,
  `reviewer_signature_or_form_hash`

Allowed values:

| Field | Controlled values |
|---|---|
| `source_pdf_opened` | `yes`, `no` |
| `source_identity_decision` | `match`, `mismatch`, `UNC` |
| `source_locator_decision` | `match`, `corrected`, `missing`, `UNC` |
| `comparison_decision` | `within_study_only`, `bounded_cross_study_candidate`, `non_poolable`, `reject_after_review`, `UNC` |
| `survey_use_decision` | `main_text`, `supplement_only`, `context_only`, `reject_after_review`, `UNC` |
| `verification_outcome` | `verified_as_reported`, `corrected_in_overlay`, `rejected_after_human_verification`, `supplement_only`, `UNC` |
| `reviewer_lock_status` | `DRAFT`, `COMPLETE_LOCKED` |

`bounded_cross_study_candidate` is not a pooling decision. It requires a
condition-complete group check after adjudication.

## 5. Missingness and completion

- Blank means "not yet reviewed" and is permitted only while the row/form is
  draft.
- `NR` means the opened source does not report the item.
- `UNC` means the reviewer could not resolve the item and a discrepancy must be
  adjudicated.
- Canonical `NR`, `NA`, or blank values remain verbatim in canonical columns;
  they do not pre-decide the reviewer entry.

A row may be `COMPLETE_LOCKED` only after source identity/hash, at least a page
locator, metric definition, operator/value representation, unit, uncertainty
status, plane/reference point, tasks/objective, scenario/geometry/condition,
baseline status, validation, value origin, comparison decision with rationale,
survey-use decision, verification outcome, reviewer identity/date, and
signature/hash are nonblank or explicitly `NR`/`UNC` as allowed.

## 6. Pilot and gates

`PILOT_12_CANDIDATE_MANIFEST.csv` is a deterministic candidate set, not an
approved pilot. `selection_modality_proxy` and `selection_diversity_roles` are
selection aids derived from canonical text/tokens; they are not canonical
modality adjudications. G1 must approve or replace the 12 rows and confirm the
actual modality and companion-report coverage before any review starts.

G2 remains closed until both humans independently complete the approved 12-row
pilot, all pilot discrepancies are adjudicated, and exact agreement for
value/operator/range/unit/source-locator critical fields is at least 90%.
Nothing in these blank forms constitutes human verification.
