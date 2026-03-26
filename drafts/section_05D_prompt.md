# Section V-D Prompt Pack (Comparative Analysis: Fiber vs Wireless)

Purpose
- Provide the exact analysis-file map and a ready-to-run COMST-style prompt for drafting Section V-D.
- Keep Section V-D consistent with Section II metric governance and Section IV taxonomy labels.

## 1) Section V-D analysis files (required first)

1. `analysis/V_ev_v2/readiness_report.md`
   - Run-completeness gate. Confirm required files exist before drafting.
2. `analysis/V_ev_v2/section5D_modality_slices.csv`
   - Primary comparative source for medium-conditioned summaries.
   - Core fields: `medium`, `n_points`, `n_unique_papers`, `median_r_bps`, `median_drmin_m`, `median_sigma_r_m`, `median_crq`, `p90_crq`.
3. `analysis/V_ev_v2/section5C_tradeoff_points.csv`
   - Scenario-level detail behind the medium slices.
   - Use to verify coverage limits, sparse media, and governed subsets.
4. `analysis/V_ev_v2/s5b_met_gov.csv`
   - Governance status per paper (plane mixing, aliasing, CRQ eligibility).
   - Use to quantify medium-comparison reliability.
5. `analysis/V_ev_v2/contract_violations.csv`
   - Limitation statements are mandatory; do not hide violation-heavy subsets.

## 2) Section V-D support files (recommended)

1. `analysis/V_ev_v2/section5E_summary_table.csv`
2. `analysis/V_ev_v2/section5E_pareto_points.csv`
   - Frontier context to avoid overclaiming from cross-medium medians.
3. `analysis/V_ev_v2/s5c_trade_mnts.csv`
   - Narrative support for medium-specific trade-off interpretation.
4. `analysis/V_ev_v2/anchor_table.csv`
   - Claim traceability to paper-level anchors.
5. `analysis/II_met_gov.md`
   - Hard rule source for plane and metric-role separation.
6. `analysis/II_sch_map.md`
   - Field semantics and extraction-path consistency.
7. `analysis/IV_ev_v2/axis_definitions.md`
8. `analysis/IV_ev_v2/mapping_rules.md`
   - Medium normalization and taxonomy alignment.
9. `writing_recipes/COMST_master_recipe.md`
10. `review_package/surv_write_guide.md`
   - COMST synthesis tone and trade-off narrative style.

## 3) Copy-paste prompt for Section V-D

```text
Task
Draft only Section V-D (Comparative Analysis: Fiber vs Wireless) for the O-ISAC survey in IEEE COMST tutorial style.

Pre-check (must do before writing)
1) Verify these files and report status as FOUND/MISSING:
   - analysis/V_ev_v2/readiness_report.md
   - analysis/V_ev_v2/section5D_modality_slices.csv
   - analysis/V_ev_v2/section5C_tradeoff_points.csv
   - analysis/V_ev_v2/s5b_met_gov.csv
   - analysis/V_ev_v2/contract_violations.csv
2) If any required file is missing, stop and output the missing paths.

Data-use contract for V-D
- Primary comparative base: section5D_modality_slices.csv
- Scenario-level support and caveat base: section5C_tradeoff_points.csv
- Governance caveat base: s5b_met_gov.csv + contract_violations.csv
- Optional frontier context: section5E_summary_table.csv + section5E_pareto_points.csv

Hard governance constraints
- Keep OSNR (optical plane) and SNR/ESNR (electrical plane) explicitly separated.
- Keep drmin (resolution) and sigma_r (accuracy) explicitly separated.
- Do not use dz as a substitute for drmin.
- CRQ claims must be restricted to CRQ-eligible records.
- Do not rank media as universally superior when sample sizes are sparse.
- Distinguish clearly:
  - medium slices computed from governed subset
  - singleton or low-support media anchors

Cross-section consistency constraints
- Align terminology with:
  - analysis/II_met_gov.md
  - analysis/II_sch_map.md
  - analysis/IV_ev_v2/axis_definitions.md
  - analysis/IV_ev_v2/mapping_rules.md
- Use Section IV medium labels consistently (for example: hybrid, cabled_fibre, wireless_vlc, wireless_fso).
- Keep section-level scope explicit: scenario-level governed records, not raw corpus-level study counts.

Writing style constraints (COMST)
- Synthesis-focused tutorial prose, not paper-by-paper list.
- Paragraph pattern: context -> quantitative finding -> comparative interpretation -> caveat.
- Use formal transitions (however, therefore, consequently, in contrast).
- Avoid raw schema/pipeline labels in manuscript prose.
- No unsupported superlatives.

Output format
- Return only manuscript-ready text for subsection:
  - "### V-D. Comparative Analysis: Fiber vs Wireless"
- Length target: 700-1000 words.
- Include at least one short takeaway sentence at the end:
  - "Lesson (V-D): ..."
- Mention Table VII in-text as the primary comparative anchor.
- If figure references are used, keep them consistent with global numbering decisions in the manuscript.
- Keep every numeric claim traceable to the listed files.

Content expectations
1) Define the comparison protocol (what is compared and under which governance filters).
2) Compare medium slices using sample-size-aware interpretation (n_points, n_unique_papers, medians).
3) Explain where cross-medium comparison is defensible and where it is not (sparse slices, missing metrics).
4) Relate comparative findings to integration/coupling implications without introducing new metric definitions.
5) Add a concise limitations paragraph using contract_violations.csv evidence.
```

