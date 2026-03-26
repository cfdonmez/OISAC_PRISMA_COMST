# Section V-C Prompt Pack (Sensing-Communication Trade-off)

Purpose
- Provide the exact analysis-file map and a ready-to-run COMST-style prompt for drafting Section V-C.
- Keep Section V-C consistent with Section II metric governance and Section IV taxonomy labels.

## 1) Section V-C analysis files (required first)

1. `analysis/V_ev_v2/readiness_report.md`
   - Run-completeness gate. Confirm required files exist before drafting.
2. `analysis/V_ev_v2/section5C_tradeoff_points.csv`
   - Main quantitative source for trade-off operating points.
   - Core fields: `r_bps`, `drmin_m`, `sigma_r_m`, `tradeoff_type`, `coupling_mode`, `medium`, `crq_*`, governance flags.
3. `analysis/V_ev_v2/s5c_trade_mnts.csv`
   - Text anchors for trade-off language and optimization narratives.
4. `analysis/V_ev_v2/section5E_summary_table.csv`
   - Top-level trade-off summary counts (`n_total_points`, `n_valid_crq_points`, `n_pareto_points`, `max_crq`, `median_crq`).
5. `analysis/V_ev_v2/section5E_pareto_points.csv`
   - Pareto/nondominated operating points for frontier interpretation.
6. `analysis/V_ev_v2/s5b_met_gov.csv`
   - Governance status per paper (plane mixing, aliasing, CRQ eligibility).
7. `analysis/V_ev_v2/contract_violations.csv`
   - Limitation statements are mandatory; do not hide violation-heavy subsets.

## 2) Section V-C support files (recommended)

1. `analysis/V_ev_v2/section5E_summary.json`
   - Machine-readable mirror of the summary table for consistency checks.
2. `analysis/V_ev_v2/section5A_evidence.csv`
   - Additional anchor support for trade-off wording.
3. `analysis/V_ev_v2/section5D_modality_slices.csv`
   - Medium-conditioned context for trade-off caveats.
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

## 3) Copy-paste prompt for Section V-C

```text
Task
Draft only Section V-C (Sensing-Communication Trade-off) for the O-ISAC survey in IEEE COMST tutorial style.

Pre-check (must do before writing)
1) Verify these files and report status as FOUND/MISSING:
   - analysis/V_ev_v2/readiness_report.md
   - analysis/V_ev_v2/section5C_tradeoff_points.csv
   - analysis/V_ev_v2/s5c_trade_mnts.csv
   - analysis/V_ev_v2/section5E_summary_table.csv
   - analysis/V_ev_v2/section5E_pareto_points.csv
   - analysis/V_ev_v2/s5b_met_gov.csv
   - analysis/V_ev_v2/contract_violations.csv
2) If any required file is missing, stop and output the missing paths.

Data-use contract for V-C
- Primary quantitative base: section5C_tradeoff_points.csv
- Textual trade-off anchors: s5c_trade_mnts.csv
- Frontier and summary base: section5E_summary_table.csv + section5E_pareto_points.csv (+ section5E_summary.json if needed)
- Governance caveat base: s5b_met_gov.csv + contract_violations.csv

Hard governance constraints
- Keep OSNR (optical plane) and SNR/ESNR (electrical plane) explicitly separated.
- Keep drmin (resolution) and sigma_r (accuracy) explicitly separated.
- Do not use dz as a substitute for drmin.
- CRQ claims must be restricted to CRQ-eligible records.
- Distinguish clearly:
  - total points
  - CRQ-candidate points
  - CRQ-valid points
  - Pareto points
- Do not overgeneralize from sparse Pareto sets.

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
  - "### V-C. Sensing-Communication Trade-off"
- Length target: 800-1200 words.
- Include at least one short takeaway sentence at the end:
  - "Lesson (V-C): ..."
- Mention Fig. 4 and Fig. 5 in-text as anchors for later integration.
- Keep every numeric claim traceable to the listed files.

Content expectations
1) Define trade-off dimensions (for example rate-vs-resolution and rate-vs-accuracy) and coupling modes.
2) Summarize quantitative operating-region evidence after governance filtering.
3) Interpret CRQ and Pareto results with explicit sample-size caveats.
4) Integrate qualitative evidence from trade-off mentions (DIRECT/INDIRECT/NONE patterns).
5) Add a concise limitations paragraph using contract_violations.csv evidence.
```

