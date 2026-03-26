# VII-C Math Anchor Decision (Run4)

## Gate Verification (G0-G3)
- G0 PASS: `analysis/man_v1/section_intent_manifest.yaml` confirms `section_VII_intent: "Applications and Use Cases"`.
- G1 PASS: `analysis/man_v1/build_contract.md` and `analysis/man_v1/stylekit_paths.md` reviewed; referenced COMST recipe docs opened.
- G2 PASS: `analysis/VII_app_sub_v1_micro/VII-C_PREFLIGHT.md` and `analysis/VII_app_sub_v1_micro/VII-C_PREFLIGHT_QA_PATCH_v2.md` confirm VII-C scope lock to `automotive_transportation`.
- G3 PASS: prior VII-C runs were reviewed; cite-key pool remains bound to preflight shortlist (`O_ISAC_003`, `O_ISAC_060`, `O_ISAC_055`, `O_ISAC_164`).

## Decision Procedure Trace (D1-D4)
1. Candidate pool from RUN2+RUN3: comm metrics `{BER, transmission rate, achievable data rate, normalized communication gain}`; sensing metrics `{CRB, RMSE, normalized sensing gain, received-power ratio, RMS DS}`; deployment constraints `{vehicular mobility, LoS/NLoS, weather/turbulence, link geometry}`.
2. SUPPORTED in processed markdowns opened this run: achievable data rate and BER (`O_ISAC_055:96`), CRB (`O_ISAC_055:96,144`), normalized gains and explicit joint objective (`O_ISAC_164:255,269`), driving V2V/V2I context (`O_ISAC_164:55`), LoS optical-link assumption (`O_ISAC_055:65`).
3. UNSUPPORTED or excluded from anchor: point ranging estimate `100.011 m` (`O_ISAC_060:197`) is not an explicit sensing error-bound metric; fixed numeric distances and turbulence constants are omitted from `s` to satisfy no-ghost-parameter safety.
4. Option admissibility check: at least one comm-plane metric and one sensing-plane metric are both directly supported; therefore Option-1 is admissible.
5. Selection: **Option-1 (joint trade-off)**.
6. Chosen anchor mapping: `R_comm` uses achievable data rate evidence; `J_sense` uses ToF-CRB evidence; scenario vector `s` keeps only evidenced vehicular mobility and LoS visibility terms.
7. Anchor cite-key set (locked): `O_ISAC_055`, `O_ISAC_164`.
