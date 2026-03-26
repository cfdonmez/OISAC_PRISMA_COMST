# Section VIII-B Preflight QA

## Proof of scope/source
- "Axis-2 Challenge domains: standardization_interoperability, hardware_scalability_efficiency, channel_modeling_evaluation, security_privacy_reliability, deployment_convergence_roadmap."
- analysis/VIII_ev_v1/axis_definitions.md :: Axis-2 Challenge domains :: L4-L4

## Two-set audit summary

| Metric | S1 | S2 |
|---|---|---|
| artefact_status | FAIL[ARTIFACT_MISSING:analysis/VIII_ch_sub_v1_micro/VIII_PREFLIGHT.md] | OK |
| M1 keys not in K_bib | 0 | 0 |
| M1 keys not in K_allowed | 0 | 0 |
| M2 case_valid (>=1 resolved markdown path) | 0/4 | 4/4 |
| M3 dedup integrity | FAIL[NO_CASE_TABLE] | FAIL[OVERLAP:Case_3-Case_4 share O_ISAC_161] |
| M4 violated cases (contract_violations.csv) | 4 | 1 |
| M5 drop_rate | 1.00 | 0.00 |
| M5 scope_drift | 0.000 | 0.000 |

## Canonical decision rationale
- Chosen: S2
- Ordering used: B1 (valid_cases max -> scope_drift min -> drop_rate min -> dedup integrity max -> evidence_row_locators tie-break)
- Applied repair (within K_allowed intersect K_bib): Case_4 cite swap O_ISAC_161, O_ISAC_100 -> O_ISAC_134, O_ISAC_171.

## Cite-key existence summary
- K_allowed source: analysis/VIII_ev_v1/section8B_evidence.csv (unique keys=221)
- K_bib source: data/references.bib (unique keys=222)
- Canonical selected keys: 11
- Missing from K_bib: 0
- Outside K_allowed: 0
- Invalid keys: none

## Path-resolution method summary
- Primary index: analysis/man_v1/file_index.csv
- Fallback index: analysis/II_md_inv.csv
- Canonical key-hit counts: HIT_PRIMARY=0, HIT_FALLBACK=11, MISS=0
- Canonical case_valid: 4/4

## Readiness decision
- PASS
- Condition checks: 4 valid cases; all keys in K_allowed intersect K_bib; >=1 markdown path per case.
