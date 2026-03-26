# Section V-A Prompt Pack (Communication Metrics)

Purpose
- Provide the exact analysis-file map and a ready-to-run COMST-style prompt for drafting Section V-A.
- Keep Section V-A consistent with Section II governance and Section IV taxonomy labels.

## 1) Section V-A analysis files (required first)

1. `analysis/V_ev_v2/readiness_report.md`
   - Run-completeness gate. Confirm required files exist before drafting.
2. `analysis/V_ev_v2/section5A_evidence.csv`
   - Text anchors and concept evidence for trade-off and communication-objective language.
3. `analysis/V_ev_v2/s5b_met_gov.csv`
   - Governance status per paper (plane mixing, aliasing, CRQ eligibility).
4. `analysis/V_ev_v2/section5C_tradeoff_points.csv`
   - Main quantitative source for communication metrics (rate and quality fields).
5. `analysis/V_ev_v2/contract_violations.csv`
   - Limitation statements are mandatory; do not hide violation-heavy subsets.

## 2) Section V-A support files (recommended)

1. `analysis/V_ev_v2/s5c_trade_mnts.csv`
   - Qualitative context to explain quantitative trends.
2. `analysis/V_ev_v2/anchor_table.csv`
   - Claim traceability to paper-level anchors.
3. `analysis/II_met_gov.md`
   - Hard rule source for OSNR/SNR plane separation.
4. `analysis/II_sch_map.md`
   - Field semantics and extraction-path consistency.
5. `analysis/IV_ev_v2/axis_definitions.md`
6. `analysis/IV_ev_v2/mapping_rules.md`
   - Medium normalization and taxonomy alignment.
7. `writing_recipes/COMST_master_recipe.md`
8. `review_package/surv_write_guide.md`
   - COMST synthesis tone and trade-off narrative style.

## 3) Copy-paste prompt for Section V-A

```text
Task
Draft only Section V-A (Communication Metrics) for the O-ISAC survey in IEEE COMST tutorial style.

Pre-check (must do before writing)
1) Verify these files and report status as FOUND/MISSING:
   - analysis/V_ev_v2/readiness_report.md
   - analysis/V_ev_v2/section5A_evidence.csv
   - analysis/V_ev_v2/s5b_met_gov.csv
   - analysis/V_ev_v2/section5C_tradeoff_points.csv
   - analysis/V_ev_v2/contract_violations.csv
2) If any required file is missing, stop and output the missing paths.

Data-use contract for V-A
- Primary quantitative base: section5C_tradeoff_points.csv
- Governance filter/caveat base: s5b_met_gov.csv + contract_violations.csv
- Narrative anchor support: section5A_evidence.csv (+ s5c_trade_mnts.csv if needed)

Hard governance constraints
- Keep OSNR (optical plane) and SNR/ESNR (electrical plane) explicitly separated.
- Do not pool OSNR and SNR in one comparable numeric claim unless an explicit conversion model is stated.
- Do not use dz as a substitute for drmin.
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
  - "### V-A. Communication Metrics"
- Length target: 700-1000 words.
- Include at least one short takeaway sentence at the end:
  - "Lesson (V-A): ..."
- Mention Table V and Fig. 4 in-text as anchors for later integration.
- Keep every numeric claim traceable to the listed files.

Content expectations
1) Define communication-metric scope (rate/throughput plus quality indicators) without mixing planes.
2) Summarize metric availability/coverage and usable subset after governance filters.
3) Discuss medium-conditioned communication behavior only with explicit caveats.
4) Add a concise limitations paragraph using contract_violations.csv evidence.
```

