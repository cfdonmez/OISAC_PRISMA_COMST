# Phase G Verification Schema Preflight

Date: 2026-09-01  
Status: `PASS_SCHEMA_PREFLIGHT_ONLY`  
G1: `PENDING_NOT_LOCKED`  
G2: `NOT_RUN_NOT_PASS`

## Scope and non-claim

This preflight covers only the draft codebook, the two blank blind-review
forms, and the deterministic 12-row pilot-candidate manifest. It confirms
schema/provenance properties; it does not confirm any source value, locator,
report identity, PDF hash, comparison decision, or survey-use decision.

No AI output is counted as V1, V2, adjudication, or source verification.

## Input locks

| Input | Rows | SHA-256 | Result |
|---|---:|---|---|
| `governance/plan_snapshot/01_verification/full_118_verification_register.csv` | 118 | `77A91B8A34F5CA964D519F4E2759C8554759276D8BB683F4BDD14B5959A49B0B` | PASS |
| `evidence/inputs/ST-19_PRIMARY_METRIC_RESULTS_4779.csv` | 4,779 | `DAC20625EF18C97BAC289F6AA05C2E2A75172E14CC76745780DDEDF9B689C539` | PASS |
| `governance/plan_snapshot/01_verification/DOUBLE_HUMAN_VERIFICATION_PROTOCOL.md` | protocol | `4CC462003CB381120A0B08F476EC5405F6E9C249F3B3F24C55E2499B01ABED32` | PASS |

## Reviewer-form checks

| Check | Observed | Result |
|---|---:|---|
| V1 rows / unique IDs | 118 / 118 | PASS |
| V2 rows / unique IDs | 118 / 118 | PASS |
| Register unique IDs | 118 | PASS |
| V1/V2 set difference versus register | 0 / 0 | PASS |
| V1/V2 row-order differences versus register | 0 / 0 | PASS |
| Form schema | 81 columns: 39 frozen context + 42 human entry | PASS |
| V1/V2 header difference | 0 | PASS |
| Nonblank human-entry cells in V1 | 0 of 4,956 | PASS |
| Nonblank human-entry cells in V2 | 0 of 4,956 | PASS |
| ST-19 canonical-prefill mismatches | 0 of 4,130 compared cells | PASS |
| Register-prefill mismatches | 0 of 354 compared cells | PASS |
| Initial form byte/hash difference | none | PASS |

Both blank forms have SHA-256
`FA5F6CA9BA628EB6BAD1E946C7B6829354DCC33AD106324BBCB9A3049BECD81D`.
Their initial byte identity is intentional; file names and subsequent
human-controlled storage establish the assignments. Once review starts, the
files must remain isolated and are expected to diverge.

The canonical section includes source/report identity, locator, value,
unit/uncertainty, measurement plane, baseline, scenario, validation,
comparison, and survey-use context copied verbatim from the two permitted
inputs. Source title, DOI, companion relationship, opened-PDF hash, metric
definition, reviewed values, tasks/objectives, comparison rationale, use
decision, and lock/signature remain blank for independent human entry.

## Pilot-candidate checks

`PILOT_12_CANDIDATE_MANIFEST.csv` has SHA-256
`4592B376329BF0DFC687F3AB8BF17D5664072A2C78A1D04FFBD464CD8C489383`.

| Check | Observed | Result |
|---|---:|---|
| Rows / unique IDs / IDs outside 118 register | 12 / 12 / 0 | PASS |
| Status | 12 × `PILOT_CANDIDATE_REQUIRES_G1_APPROVAL` | PASS |
| Metric domains | communication 4; sensing 4; joint 4 | PASS |
| Result representations | scalar 6; range 2; threshold 2; mean_SD 1; curve 1 | PASS |
| Explicit reported uncertainty candidate | 1 (`mean_SD` with `SD`) | PASS |
| Locator-bearing rows | table 2; figure 9; equation 3 | PASS |
| Study clusters / source reports | 10 / 11 | PASS |
| Companion-family exercise | `P03-M004`/`SCR-00553` and `P03-M039`/`SCR-00083` share one canonical study-cluster ID | PASS AS CANDIDATE |

The selection uses deterministic `selection_modality_proxy` tags derived from
canonical condition/scenario/cluster text. These tags visibly span multiple
system families, but they are not an approved modality classification. The
protocol's “at least four modalities” condition therefore remains
`PENDING_G1_HUMAN_CONFIRMATION` and is not credited as passed here.

## Required-field and gate negative tests

All mutations below were performed in memory; no source or output file was
changed.

| Negative test | Injected invalid state | Observed rejection | Result |
|---|---|---|---|
| N01 missing row | one V1 ID removed | register/form set difference = 1 | PASS |
| N02 duplicate key | final V1 ID replaced by first ID | unique count fell from 118 to 117 | PASS |
| N03 contaminated blind issuance | one human-entry cell made nonblank | blank-at-issuance rule rejected the form | PASS |
| N04 false complete row | `COMPLETE_LOCKED` proposed on an untouched row | 17 required fields still blank; rejected | PASS |
| N05 unapproved pilot | current 12 candidate statuses evaluated against `PILOT_APPROVED_G1` | 12/12 rejected | PASS |
| N06 premature agreement | G2 agreement requested before reviewer entry | critical-field denominator = 0; no statistic/no PASS | PASS |

These tests establish fail-closed behavior for row identity, blindness,
required fields, G1 approval, and G2 agreement. They do not replace a
versioned validation script at release.

## Gate decision

- Schema preflight: `PASS`.
- G1 codebook/pilot approval: `PENDING`.
- Approved 12-row double-human pilot: not started.
- V1 completed rows: 0/118.
- V2 completed rows: 0/118.
- Critical-field agreement denominator: 0.
- G2: `NOT_RUN_NOT_PASS`.

G2 may be evaluated only after G1 locks the codebook and actual pilot
composition, two different humans independently complete the approved 12 rows,
all discrepancies are adjudicated, and exact agreement for
value/operator/range/unit/source locator is at least 90%.
