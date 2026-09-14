# Phase G Verification Codebook — Locked Application Record

Status: `LOCKED_SOURCE_VERIFICATION__G6_G7_APPROVED__RC1_TECHNICAL_QA_PASS__HUMAN_RELEASE_SIGNOFF_PENDING`

Date: `2026-09-01`

This record applies the frozen draft codebook without modifying that historical
G0 artefact. It records the human source-verification interpretation used for
the completed 118-record review.

## Human-review scope

- Two independent anonymous human reviewers examined 118 records each.
- The 16 source reports were opened and checked for identity and SHA-256.
- Reviewers checked source locator, metric definition, operator/value or range,
  uncertainty status, reported unit, measurement plane, task, condition,
  comparator role, validation setting, and value origin.
- Missing source information was retained as `NR`; unresolved information would
  have been retained as `UNC`.
- All 118 rows were approved as `verified_as_reported`; there were zero
  corrections, rejections, discrepancies, or adjudication decisions.

## Locked interpretation of analysis fields

The frozen draft requires `comparison_decision` and `survey_use_decision` at
row lock. For source verification these two fields use `analysis_pending`.
This value means the source is verified while method grouping and manuscript
use remain separate decisions. It is neither missing data nor a manuscript-use
approval.

G6 subsequently approved `within_study_only` and `non_poolable` roles under the
documented group contracts. G7 approved `main_text`, `context_only`, and
`supplement_only` carriers in the superseding analysis lock. The original
reviewer-form value remains unchanged so that source verification is not
mistaken for a later method or manuscript-use decision.

## Chronology declaration

The analog review preceded the formal digital G1/pilot lock. The sequence was
not backdated. On 2026-09-01, the two independent reviewer records and the
third human author/controller confirmation were transcribed and the sequence
deviation was recorded explicitly.

## Completion evidence

- `VERIFICATION_REVIEWER_V1_BLIND.csv`: 118/118 `COMPLETE_LOCKED`.
- `VERIFICATION_REVIEWER_V2_BLIND.csv`: 118/118 `COMPLETE_LOCKED`.
- `PILOT_12_HUMAN_RESULT_2026-09-01.csv`: 100% critical-field agreement.
- `VERIFIED_118_LOCK.csv/.json`: 118/118 `verified_as_reported`, with the G7
  analysis-lock version explicitly superseding the historical source-only
  lock by hash.
- `REPORT_PDF_HASHES.sha256`: 16/16 source reports verified.

No numeric manuscript claim is authorized by this record.
