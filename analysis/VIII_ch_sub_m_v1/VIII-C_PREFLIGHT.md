# Section VIII-C Preflight

**Subsection Axis Label:** channel_modeling_evaluation
**Scope Keywords (axis-locked):** channel_modeling_evaluation; turbulence_pointing_blockage; nlos_geometry_intermittency; metric_alignment_comm_vs_sensing; benchmark_reproducibility

## Selection Plan

1. Gate lock: `section_VIII_intent == Open Challenges and Research Roadmap`; axis lock `channel_modeling_evaluation`.
2. Candidate pool: `section8C_evidence.csv` rows with `strength=DIRECT` and `challenge_domain=channel_modeling_evaluation`.
3. Diversity lock: 4 cases, non-duplicate cite-key sets, >=3 distinct motif signatures.
4. Evidence contract checks per key: `references.bib` existence, markdown path resolution (`file_index.csv` else `II_markdown_inventory.csv`), `contract_violations.csv` flag and plan.

## 4-Case Shortlist

| case_id/title | motif_signature | cite_keys | evidence_row_locators | markdown_paths | violations_flag | note |
|---|---|---|---|---|---|---|
| Case_1: weather-aware atmospheric channel sensing | turbulence_pointing_blockage | O_ISAC_005 | section8C_evidence.csv:R16 | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_005\O_ISAC_005.md [HIT_FALLBACK] | N | NONE |
| Case_2: LOS/NLOS multipath remodeling for model robustness | nlos_geometry_intermittency | O_ISAC_050 | section8C_evidence.csv:R81 | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_050\O_ISAC_050.md [HIT_FALLBACK] | N | NONE |
| Case_3: BER-capacity distance coupling in channel evaluation | metric_alignment_comm_vs_sensing | O_ISAC_381 | section8C_evidence.csv:R402 | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_381\O_ISAC_381.md [HIT_FALLBACK] | N | NONE |
| Case_4: benchmark/measurement-campaign consistency | benchmark_reproducibility | O_ISAC_327 | section8C_evidence.csv:R380 | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_327\O_ISAC_327.md [HIT_FALLBACK] | N | NONE |
