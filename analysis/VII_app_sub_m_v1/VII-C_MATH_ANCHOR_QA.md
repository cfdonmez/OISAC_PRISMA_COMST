# VII-C MATH_ANCHOR QA

## PASS/FAIL Checklist
- Placeholder markers (`TODO`/`TBD`/`FIXME`): PASS.
- Intent compliance (Section VII applications/deployment framing): PASS.
- Scope lock (`automotive_transportation` from `VII-C_PREFLIGHT_QA_PATCH_v2.md`): PASS.
- Preflight cite-key pool lock (only `O_ISAC_003`, `O_ISAC_060`, `O_ISAC_055`, `O_ISAC_164` allowed): PASS.
- Bracket-safe math (no square-bracket math forms): PASS.
- Metric-plane separation (comm-plane vs sensing-plane explicitly labeled): PASS.
- Enabling-tech honesty (no ORIS/OPA/RIS phase variables introduced): PASS.
- No-ghost-parameter safety (no unsupported fixed distance/turbulence/NLoS constants in anchor): PASS.
- Word count gate for `VII-C_MATH_ANCHOR.md` (target 90-170): PASS (`90` words).

## Cite-Key Existence (`data/references.bib`)
- `O_ISAC_055`: YES (line `342`).
- `O_ISAC_164`: YES (line `1002`).

## Processed Markdown Validation Log

### Path Resolution Method
1. Attempted resolution via `analysis/man_v1/file_index.csv`.
2. Result: no key-level hits for `O_ISAC_055` and `O_ISAC_164`.
3. Fallback applied via `analysis/II_md_inv.csv`: YES.
4. Resolved paths used in this run:
   - `O_ISAC_055` -> `data/proc_markdowns/O_ISAC_055/O_ISAC_055.md`
   - `O_ISAC_164` -> `data/proc_markdowns/O_ISAC_164/O_ISAC_164.md`

### Opened-Section Log (this run)
- `O_ISAC_055` -> `data/proc_markdowns/O_ISAC_055/O_ISAC_055.md`
  - Abstract/Intro opened: lines `5`, `11-13`.
  - Methods/results opened: lines `65`, `96`, `144`, `161-169`, `212`, `226`.
  - Conclusion/limitations opened: line `234`.
  - D2 excerpt locators used: lines `96`, `65`.
- `O_ISAC_164` -> `data/proc_markdowns/O_ISAC_164/O_ISAC_164.md`
  - Abstract/Intro opened: lines `17`, `33`.
  - Methods/results opened: lines `55`, `236-256`, `266-269`, `410`.
  - Conclusion/limitations opened: lines `434-440`.
  - D2 excerpt locators used: lines `55`, `269`.

## Decision Trace (Option-1/Option-2)
- Candidate pool validated from RUN2+RUN3 includes comm-plane metrics (`BER`, `data rate`, `G_c`) and sensing-plane metrics (`CRB`, `RMSE`, `G_e`).
- Supported items used for anchor: achievable data rate and CRB (`O_ISAC_055`), joint communication+sensing objective (`O_ISAC_164`), vehicular driving context (`O_ISAC_164`), LoS regime (`O_ISAC_055`).
- Unsupported-for-anchor item: standalone range estimate value (`O_ISAC_060`) was excluded because it is not an explicit loss-bound metric.
- Selection: **Option-1 (joint trade-off)**, because both communication-plane and sensing-plane metrics are directly evidenced in processed markdowns.

## SHA256
- `analysis/VII_app_sub_v1_micro/VII-C_MATH_ANCHOR_DECISION.md`: `fa5d3d595b7366030578bc221e177b97d80d4bf58447cad3ce7caafd765af54b`
- `analysis/VII_app_sub_v1_micro/VII-C_MATH_ANCHOR.md`: `c7ea08ad1014a864547b9dada04f97b9d1d49a3ddd8001a714d76ab82d937894`
- `analysis/VII_app_sub_v1_micro/VII-C_MATH_ANCHOR_supp.md`: `25c224845a96e63beb14237b5c8a9a78bf9fde7d7a278270bd6b7295429e6a4d`
