# VII-F MATH_ANCHOR QA

## PASS/FAIL Checklist
- Placeholder markers scan: PASS (none found).
- Intent discipline (applications and use-case synthesis only): PASS.
- Bracket-safe math (no square-bracket math tokens): PASS.
- Enabling-tech honesty (no unsupported ORIS or OPA or RIS phase variables): PASS.
- Numeric-claim safety: PASS.
  All numeric values in D0-D2 are backed by explicit artifact rows or JSON key paths in D2.

## Anchor Family and Compliance
- Selected family: Anchor-B.
- Decision rule compliance: PASS.
  Anchor-A was feasible, Anchor-B was feasible, and Anchor-B was selected due to VII-F cross-domain framing with concrete artifact references.

## Cite-Key Existence
- Anchor equation terms use summary artifacts only, so cite-key dependence in D1 and D2 is not required.
- Cite-keys referenced in D0 feasibility check:
  - `O_ISAC_011`: FOUND in `data/references.bib`
  - `O_ISAC_108`: FOUND in `data/references.bib`

## Validation Log (Anchor-B artifact rows)
- `s7f_macro_med_cov.csv` rows 2-6 used for macro coverage weights.
- `s7f_micro_dom_cnts.csv` rows 2-5 used for micro coverage weights.
- `section7F_paper_macro_map.csv` row 1 schema and rows 12, 108, 143, 164, 173, 191 used for incidence mapping sanity checks.
- `section7F_transfer_map.csv` rows 3, 15, 25, 32, 36 and rows 13, 23, 30, 39 and rows 2, 14, 24, 31, 35 and rows 9, 20, 27, 34, 37 used for transfer-penalty construction.
- `section7F_summary.json` key paths `$.n_total_papers` and `$.n_unique_micro_domains` used for global cardinality support.

## SHA256
- `analysis/VII_app_sub_v1_micro/VII-F_MATH_ANCHOR_DECISION.md`
  - `87c923d9a35fcd04456f148e73bdd85f350330b77ab036bba7a01ed3ade04097`
- `analysis/VII_app_sub_v1_micro/VII-F_MATH_ANCHOR.md`
  - `49215e23342d9bc2abe710260c5a3c062945658cffdfc0139e8b8c8a70ebd828`
- `analysis/VII_app_sub_v1_micro/VII-F_MATH_ANCHOR_supp.md`
  - `0cd0538b749941ab0c946e8e76a62d85ad7124b04a1d2caac58c54aa3bbb9757`
