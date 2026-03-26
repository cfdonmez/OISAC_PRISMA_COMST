# Section V-B Prompt Pack (Sensing Metrics)

Purpose
- Provide the exact analysis-file map and a ready-to-run COMST-style prompt for drafting Section V-B.
- Keep Section V-B consistent with Section II metric governance and Section IV taxonomy labels.

## 1) Section V-B analysis files (required first)

1. `analysis/V_ev_v2/readiness_report.md`
   - Run-completeness gate. Confirm required files exist before drafting.
2. `analysis/V_ev_v2/section5C_tradeoff_points.csv`
   - Main quantitative source for sensing metrics and governance flags.
   - Core fields: `drmin_m`, `sigma_r_m`, `crb_value`, `dz_m`, `task_type`, `medium`, `governance_blocked`.
3. `analysis/V_ev_v2/s5b_met_gov.csv`
   - Governance status per paper (plane mixing, aliasing, CRQ eligibility).
   - Use to quantify usable vs blocked sensing evidence.
4. `analysis/V_ev_v2/s5c_trade_mnts.csv`
   - Textual support for quantitative sensing interpretation.
5. `analysis/V_ev_v2/contract_violations.csv`
   - Limitation statements are mandatory; do not hide violation-heavy subsets.

## 2) Section V-B support files (recommended)

1. `analysis/V_ev_v2/section5D_modality_slices.csv`
   - Medium-conditioned medians for sensing discussion (fiber vs wireless slices).
2. `analysis/V_ev_v2/section5A_evidence.csv`
   - Additional anchor support where sensing/trade-off language is explicit.
3. `analysis/V_ev_v2/anchor_table.csv`
   - Claim traceability to paper-level anchors.
4. `analysis/II_met_gov.md`
   - Hard rule source for plane and metric-role separation.
5. `analysis/II_sch_map.md`
   - Field semantics and extraction-path consistency.
6. `analysis/IV_ev_v2/axis_definitions.md`
7. `analysis/IV_ev_v2/mapping_rules.md`
   - Medium normalization and taxonomy alignment.
8. `writing_recipes/COMST_master_recipe.md`
9. `review_package/surv_write_guide.md`
   - COMST synthesis tone and trade-off narrative style.

## 3) Copy-paste prompt for Section V-B

```text
Task
Draft only Section V-B (Sensing Metrics) for the O-ISAC survey in IEEE COMST tutorial style.

Pre-check (must do before writing)
1) Verify these files and report status as FOUND/MISSING:
   - analysis/V_ev_v2/readiness_report.md
   - analysis/V_ev_v2/section5C_tradeoff_points.csv
   - analysis/V_ev_v2/s5b_met_gov.csv
   - analysis/V_ev_v2/s5c_trade_mnts.csv
   - analysis/V_ev_v2/contract_violations.csv
2) If any required file is missing, stop and output the missing paths.

Data-use contract for V-B
- Primary quantitative base: section5C_tradeoff_points.csv
- Governance filter/caveat base: s5b_met_gov.csv + contract_violations.csv
- Narrative anchor support: s5c_trade_mnts.csv (+ section5A_evidence.csv if needed)

Hard governance constraints
- Keep sensing roles explicitly separated:
  - drmin: physical resolution
  - sigma_r: estimator-level accuracy
  - CRB: bound-level context (auxiliary), not a direct replacement for measured accuracy
  - dz: spatial granularity and not a substitute for drmin
- Do not use dz as a substitute for drmin in any quantitative comparison.
- Keep OSNR (optical plane) and SNR/ESNR (electrical plane) separated when discussing sensing evidence quality.
- Any CRQ-related statement must be restricted to eligible records.

Cross-section consistency constraints
- Align terminology with:
  - analysis/II_met_gov.md
  - analysis/II_sch_map.md
  - analysis/IV_ev_v2/axis_definitions.md
  - analysis/IV_ev_v2/mapping_rules.md
- Use Section IV medium labels consistently (for example: hybrid, cabled_fibre, wireless_vlc, wireless_fso).

Writing style constraints (COMST)
- Synthesis-focused tutorial prose, not paper-by-paper list.
- Paragraph pattern: context -> quantitative finding -> comparative interpretation -> caveat.
- Use formal transitions (however, therefore, consequently, in contrast).
- Avoid raw schema/pipeline labels in manuscript prose.
- No unsupported superlatives.

Output format
- Return only manuscript-ready text for subsection:
  - "### V-B. Sensing Metrics"
- Length target: 700-1000 words.
- Include at least one short takeaway sentence at the end:
  - "Lesson (V-B): ..."
- Mention Table VI and Fig. 4 in-text as anchors for later integration.
- Keep every numeric claim traceable to the listed files.

Content expectations
1) Define sensing-metric scope with explicit role separation (drmin, sigma_r, CRB, dz).
2) Summarize metric availability/coverage and usable subset after governance filters.
3) Discuss medium-conditioned sensing behavior only with explicit comparability caveats.
4) Add a concise limitations paragraph using contract_violations.csv evidence.
```

