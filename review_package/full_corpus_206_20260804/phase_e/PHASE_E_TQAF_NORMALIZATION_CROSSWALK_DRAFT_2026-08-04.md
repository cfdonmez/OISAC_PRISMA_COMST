# Phase-E TQAF normalization crosswalk draft — 2026-08-04

## Outcome

- Study rows: **206**; unique studies: **206**.
- Metric rows inspected: **4861**.
- Crosswalk unmapped values: **0**.
- QA status: **PASS**.
- Source workbook SHA-256: `e0ea51c332483f0e7150b25ecfae9a1b1c19232a74b1f484d1277fd8a46da55c`.

## Canonical study distributions

| Field | Distribution |
|---|---|
| Modality | photonic_THz=69; fiber=56; VLC_LiFi=38; FSO=31; hybrid_optical=9; other_optical=3 |
| Validation maturity max | 2=32; 3=18; 4=78; 5=66; 6=12 |
| 6G relevance | direct=138; inferred=64; not_applicable=3; weak=1 |
| Dataset availability | unavailable_or_NR=145; on_request=41; open=13; NA=7 |
| Code/model availability | unavailable_or_NR=197; on_request=7; NA=1; partial_components=1 |
| Repeatability | complete_or_substantial=106; partial=99; insufficient_or_NR=1 |
| Baseline | internal=132; external_or_common=61; none=13 |

## Deterministic contract

- Blank is mapped to `workflow_blank` only so crosswalk coverage can be audited; it is never silently assigned a scientific score.
- `NR` and `UNC` contribute 0; `NA` is excluded only from its applicable subindicator denominator.
- Multi-report clusters retain one study weight. Complementary evidence is unioned; contradictions remain visible.
- Validation maturity is mapped on split `|` tokens. Study-level maximum is a normalization output, not yet the final outcome-linked maturity score.
- Baselines are classified as `none=0`, `internal=0.5`, or `external_or_common=1`; the JSON preserves the raw text, metric-level baseline-row count, rule, and any review flag for every study.

## Workflow blanks requiring Phase-E handling

- Comparability blanks: **92 metric rows / 12 studies**.
- Admissibility blanks: **92 metric rows / 12 studies**.
- These rows must be resolved, explicitly coded not-applicable, or excluded as configuration/non-outcome rows before final TQAF scoring.

## Baseline rule-review flags

- Deterministic classifier review flags: **0**.
- None.

## Files and audit use

The companion JSON contains every raw distribution, every categorical/token crosswalk, the 206-row per-study normalization result, baseline classification evidence, workflow-blank study IDs, and the explicit unmapped QA result. It is a Phase-E draft and does not modify or overwrite the Phase-D workbook.
