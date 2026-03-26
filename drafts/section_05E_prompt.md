# Section V-E Prompt Pack (Pareto Interpretation and Design Implications)

Purpose
- Provide the exact analysis-file map and a ready-to-run COMST-style prompt for drafting Section V-E.
- Keep Section V-E consistent with Section II metric governance and Section IV taxonomy labels.

## 1) Section V-E analysis files (required first)

1. `analysis/V_ev_v2/readiness_report.md`
   - Run-completeness gate. Confirm required files exist before drafting.
2. `analysis/V_ev_v2/section5E_pareto_points.csv`
   - Primary source for nondominated frontier points.
   - Core fields: `medium`, `task_type`, `coupling_mode`, `r_bps`, `drmin_m`, `sigma_r_m`, `crq_delta_bps_per_m`.
3. `analysis/V_ev_v2/section5E_summary_table.csv`
   - Top-level frontier summary (`n_total_points`, `n_valid_crq_points`, `n_pareto_points`, `max_crq`, `median_crq`).
4. `analysis/V_ev_v2/section5E_summary.json`
   - Machine-readable mirror of summary values for consistency checks.
5. `analysis/V_ev_v2/section5C_tradeoff_points.csv`
   - Baseline operating cloud to contextualize Pareto sparsity and representativeness.
6. `analysis/V_ev_v2/s5b_met_gov.csv`
   - Governance status per paper (plane mixing, aliasing, CRQ eligibility).
7. `analysis/V_ev_v2/contract_violations.csv`
   - Limitation statements are mandatory; do not hide violation-heavy subsets.

## 2) Section V-E support files (recommended)

1. `analysis/V_ev_v2/section5D_modality_slices.csv`
   - Medium-conditioned summary context for design implications.
2. `analysis/V_ev_v2/s5c_trade_mnts.csv`
   - Narrative support for trade-off and optimization language.
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

## 3) Copy-paste prompt for Section V-E

```text
Task
Draft only Section V-E (Pareto Interpretation and Design Implications) for the O-ISAC survey in IEEE COMST tutorial style.

Pre-check (must do before writing)
1) Verify these files and report status as FOUND/MISSING:
   - analysis/V_ev_v2/readiness_report.md
   - analysis/V_ev_v2/section5E_pareto_points.csv
   - analysis/V_ev_v2/section5E_summary_table.csv
   - analysis/V_ev_v2/section5E_summary.json
   - analysis/V_ev_v2/section5C_tradeoff_points.csv
   - analysis/V_ev_v2/s5b_met_gov.csv
   - analysis/V_ev_v2/contract_violations.csv
2) If any required file is missing, stop and output the missing paths.

Data-use contract for V-E
- Primary frontier base: section5E_pareto_points.csv
- Frontier summary base: section5E_summary_table.csv + section5E_summary.json
- Baseline operating-region context: section5C_tradeoff_points.csv
- Governance caveat base: s5b_met_gov.csv + contract_violations.csv
- Optional medium context: section5D_modality_slices.csv

Hard governance constraints
- Keep OSNR (optical plane) and SNR/ESNR (electrical plane) explicitly separated.
- Keep drmin (resolution) and sigma_r (accuracy) explicitly separated.
- Do not use dz as a substitute for drmin.
- CRQ claims must be restricted to CRQ-eligible records.
- Distinguish clearly:
  - total trade-off points
  - CRQ-candidate points
  - CRQ-valid points
  - Pareto points
- Do not generalize frontier behavior beyond its sample support.
- Treat sparse Pareto sets as illustrative evidence, not population-stable envelopes.

Cross-section consistency constraints
- Align terminology with:
  - analysis/II_met_gov.md
  - analysis/II_sch_map.md
  - analysis/IV_ev_v2/axis_definitions.md
  - analysis/IV_ev_v2/mapping_rules.md
- Use Section IV medium labels consistently (for example: hybrid, cabled_fibre, wireless_vlc, wireless_fso).
- Keep scope explicit: scenario-level governed records, not raw corpus-level study counts.

Writing style constraints (COMST)
- Synthesis-focused tutorial prose, not paper-by-paper list.
- Paragraph pattern: context -> quantitative finding -> comparative interpretation -> caveat.
- Use formal transitions (however, therefore, consequently, in contrast).
- Avoid raw schema/pipeline labels in manuscript prose.
- No unsupported superlatives.

Output format
- Return only manuscript-ready text for subsection:
  - "### V-E. Pareto Interpretation and Design Implications"
- Length target: 600-900 words.
- Include at least one short takeaway sentence at the end:
  - "Lesson (V-E): ..."
- Mention Fig. 5 in-text as the primary frontier anchor.
- Keep every numeric claim traceable to the listed files.

Content expectations
1) Define the Pareto interpretation protocol (frontier vs governed cloud vs raw cloud).
2) Quantify frontier sparsity and representativeness gap using summary counts.
3) Interpret medium and coupling composition of Pareto points with sample-size caveats.
4) Translate frontier observations into design implications without introducing new metric definitions.
5) Add a concise limitations paragraph using contract_violations.csv evidence.
```

