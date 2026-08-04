# Phase-E TQAF deterministic draft — 2026-08-04

- Source workbook: `OISAC_PHASE_D_SURVEY_READY_2026-08-04.xlsx`
- Locked source SHA-256: `c1b3b89789c6ed3e20da5a6283e480875c1913e21af88ff59ac747a6aa949348`
- Method: `phase_e_tqaf_deterministic_v1.0_2026-08-04`
- Study rows: 206 (one row per unique study cluster).
- Evidence bodies: 115 across S1–S7.
- Body-normalization audit rows: 7951; fallback memberships S3 communication=2, S3 sensing=2, S6 technology=19, S6 application=15.
- Quarantined claims: 72 in 31 studies; type-specific caps applied.
- Legacy blank resolution: 92 comparability and 92 admissibility blanks explicitly mapped to `insufficient_information_due_legacy_extraction`.
- QA: **PASS** (43/43 checks).

## Deterministic scoring method

Eight study-level dimensions use the protocol-locked 0–3 scale (0 insufficient, 1 weak/incomplete, 2 adequate, 3 strong/benchmark-ready). Composite indicators use fixed thresholds: <0.25=0, 0.25–<0.50=1, 0.50–<0.80=2, >=0.80=3. Overall contribution uses the arithmetic mean of the eight final dimension scores (<0.75=0, <1.50=1, <2.25=2, otherwise 3), followed by source-conflict and core-relevance caps.

Metric clarity requires both communication and sensing outcome rows and evaluates source reporting, family/definition, measurement plane, validation/scenario context, operational value/unit, and unresolved conflict status. Validation score 3 requires field/deployment evidence for both functions. Reproducibility score 3 requires complete/substantial parameters and open data or code/model. Benchmark score 3 requires an external/common baseline, an open artifact, direct admissibility, adequate validation/reproducibility, and no quarantined claim. Comparison score 3 requires directly comparable/admissible outcomes in both domains.

Quarantined metric/tradeoff claims cap comparison admissibility at 1; affected quantitative dimensions are capped at 2; any quarantined claim caps overall contribution at 2. Quarantined records remain in the audit trace and are excluded from evidence-body claim aggregation.

## Score distributions

```json
{
  "technical_relevance": {
    "1": 15,
    "2": 68,
    "3": 123
  },
  "metric_clarity": {
    "1": 31,
    "2": 7,
    "3": 168
  },
  "reporting_completeness": {
    "2": 10,
    "3": 196
  },
  "validation_maturity": {
    "1": 32,
    "2": 168,
    "3": 6
  },
  "reproducibility": {
    "1": 4,
    "2": 199,
    "3": 3
  },
  "benchmark_readiness": {
    "1": 48,
    "2": 158
  },
  "comparison_admissibility": {
    "1": 192,
    "2": 10,
    "3": 4
  },
  "limitation_transparency": {
    "1": 9,
    "2": 44,
    "3": 153
  },
  "overall_evidence_contribution": {
    "1": 6,
    "2": 75,
    "3": 125
  }
}
```

## Outputs

- `risk_of_bias_PHASE_E_DRAFT_2026-08-04.csv`
- `certainty_grade_PHASE_E_DRAFT_2026-08-04.csv`
- `synthesis_matrix_PHASE_E_DRAFT_2026-08-04.csv`
- `phase_e_tqaf_dimension_audit_2026-08-04.csv`
- `phase_e_tqaf_body_normalization_audit_2026-08-04.csv`
- `phase_e_tqaf_resolved_legacy_metric_rows_2026-08-04.csv`
- `phase_e_tqaf_QA_2026-08-04.json`
- `phase_e_tqaf_summary_2026-08-04.md`

These are temporary Phase-E drafts. No canonical workbook or canonical CSV was modified.
