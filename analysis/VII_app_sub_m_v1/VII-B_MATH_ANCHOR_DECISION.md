# VII-B Math Anchor Decision (Run4)

## Gate Verification (G0-G3)
- G0 PASS: `analysis/man_v1/section_intent_manifest.yaml` confirms `section_VII_intent: "Applications and Use Cases"`.
- G1 PASS: `analysis/man_v1/build_contract.md` and `analysis/man_v1/stylekit_paths.md` reviewed; referenced COMST recipe docs opened.
- G2 PASS: `analysis/VII_ev_v2/axis_definitions.md` confirms Axis-2 token `indoor_environments`; VII-B official title lock is `Indoor Environments`.
- G3 PASS: `analysis/VII_app_sub_v1_micro/VII-B_PREFLIGHT.md` / `_QA.md` checked; cite-key pool lock remains within `O_ISAC_011`, `O_ISAC_030`, `O_ISAC_108`, `O_ISAC_388`.

## Decision Memo (D1-D4)
1. Candidate pool from RUN2+RUN3 contains comm metrics `BER`, `throughput`; sensing metrics `RMSE`, `MSE`, `gesture accuracy`; deployment constraints `room geometry`, `user density`, `table-surface reflection`.
2. Processed markdown validation was completed for `O_ISAC_011`, `O_ISAC_030`, `O_ISAC_108`, `O_ISAC_388` using Abstract/Intro + methods/results + conclusion/limitations sections.
3. SUPPORTED comm items: `BER` (`O_ISAC_011`, `O_ISAC_108`, `O_ISAC_388`), `throughput` (`O_ISAC_030`).
4. SUPPORTED sensing items: `distance/position RMSE` (`O_ISAC_011`), `coordinate MSE` (`O_ISAC_108`), `gesture-recognition accuracy` (`O_ISAC_030`).
5. SUPPORTED deployment items: indoor room geometry (`O_ISAC_108`, `O_ISAC_388`), user-density effect (`O_ISAC_388`), reflection variability (`O_ISAC_030`).
6. UNSUPPORTED item: explicit sensing-plane metric for Scenario-4 study `O_ISAC_388` itself (no sensing KPI reported in that scenario text).
7. Option rule check: Option-1 is admissible because at least one comm-plane metric and one sensing-plane metric are both directly supported by excerpts without introducing non-evidenced variables.
8. Selection: **Option-1 (joint trade-off)** using BER-derived communication utility and position-MSE sensing loss for indoor deployment.

## Supported/Unsupported List (Auditable)
- `BER` -> SUPPORTED (`O_ISAC_108:233`, `O_ISAC_388:139`, `O_ISAC_011:145`)
- `MSE_pos` -> SUPPORTED (`O_ISAC_108:139-141`)
- `RMSE_pos` -> SUPPORTED (`O_ISAC_011:153`, `O_ISAC_011:165`)
- `throughput` -> SUPPORTED (`O_ISAC_030:292`)
- `gesture accuracy` -> SUPPORTED (`O_ISAC_030:214`)
- `room geometry` -> SUPPORTED (`O_ISAC_388:117`, `O_ISAC_108:43`)
- `user density effect` -> SUPPORTED (`O_ISAC_388:139`)
- `sensing KPI in O_ISAC_388 scenario` -> UNSUPPORTED (no explicit sensing metric statement in the scenario evidence chain)

## Cite Keys Used In This Run
- Validation set: `O_ISAC_011`, `O_ISAC_030`, `O_ISAC_108`, `O_ISAC_388`
- Anchor-writing set: `O_ISAC_108`, `O_ISAC_388`
