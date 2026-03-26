VII-B Integration QA

Gate checks:
- G0 PASS: `analysis/man_v1/section_intent_manifest.yaml` confirms Section VII intent is `Applications and Use Cases`.
- G1 PASS: `analysis/man_v1/build_contract.md` and `analysis/man_v1/stylekit_paths.md` reviewed; referenced COMST recipe docs opened.
- G2 PASS: `analysis/VII_ev_v2/axis_definitions.md` confirms VII-B scope token `indoor_environments` and official title `Indoor Environments`.
- G3 PASS: `analysis/VII_app_sub_v1_micro/VII-B_PREFLIGHT.md` and `_QA.md` reviewed; cite-key pool remains preflight-locked.

Integration notes:
- Source parts merged in required order: Context -> Scenarios 1-2 -> Scenarios 3-4 -> Math anchor -> Takeaways.
- No new cite keys introduced; D1 keys are exactly the micro-part pool.
- Supplement merged across all run supplements with de-duplication by identical excerpt string and grouped usage mapping.

Checklist (PASS/FAIL):
- Placeholder markers scan: PASS (0 in D1 and D2).
- Intent discipline (applications/deployment only): PASS.
- Metric-plane separation (explicit sensing plane vs communication plane): PASS.
- ORIS canon (non-canonical RIS term variants absent): PASS.
- Bracket-safe math (no square-bracket tokens inside LaTeX blocks): PASS.
- Word count for D1: PASS (`715` words; target `520-780` used because no VII-B-specific subsection budget was found in stylekit files).

Cite-key integrity in D1:
- `O_ISAC_011`: present in `data/references.bib` (line `78`).
- `O_ISAC_030`: present in `data/references.bib` (line `192`).
- `O_ISAC_108`: present in `data/references.bib` (line `664`).
- `O_ISAC_388`: present in `data/references.bib` (line `1350`).
- New keys beyond micro-parts: none.

Patch-A confirmation (terminology safety):
- Before (micro math anchor, <=2 lines):  
  "including waveform selection, LED radiation and power-allocation settings, and phase-level adaptation policy ..."
- After (integrated D1, <=2 lines):  
  "u denotes indoor control variables such as resource allocation and waveform adaptation policy ..."

Patch-B confirmation (objective canonicalization):
- Before (micro math anchor, <=2 lines):  
  `\max_{u}\ \alpha\,R_{\mathrm{comm}}(u;s)\;-\;(1-\alpha)\,J_{\mathrm{sense}}(u;s)`  
  `R_{\mathrm{comm}}(u;s) = -\mathrm{BER}(u;s)`
- After (integrated D1, <=2 lines):  
  `\min_{u}\ \alpha\,\mathrm{BER}(u;s) + (1-\alpha)\,\mathrm{MSE}_{\mathrm{pos}}(u;s)`  
  `s=(g_{\mathrm{room}},\rho_{\mathrm{user}})`

SHA256:
- D1 `analysis/VII_app_sub_v1/VII-B.md`: `4148d55aa63dd58e5e963792410560d0874eb76cba0bfe4e5bbf0dbf7d3348f5`
- D2 `analysis/VII_app_sub_v1/VII-B_supp.md`: `7c76c8d3aa9c4fd8ae56df88f158c4eeb33334630d957bea46936b119d276a45`
