# Section VIII-B Preflight QA Patch

## Dedup integrity (post-repair recompute)

| Pair | Shared keys | Jaccard |
|---|---|---|
| Case_1 vs Case_2 | none | 0.000 |
| Case_1 vs Case_3 | none | 0.000 |
| Case_1 vs Case_4 | none | 0.000 |
| Case_2 vs Case_3 | none | 0.000 |
| Case_2 vs Case_4 | none | 0.000 |
| Case_3 vs Case_4 | none | 0.000 |

- Dedup status: PASS

## Motif-diversity lock

| case_id | motif signature |
|---|---|
| Case_1 | transceiver_sharing;rf_hardware_simplification;cost_reduction |
| Case_2 | power_budget;signal_chain_amplification;edge_latency |
| Case_3 | integration_level_tradeoff;baseband_processing_complexity;path_loss_constraints |
| Case_4 | flops_scaling;beam_steering_granularity;latency_dataset_size |

- Distinct motif signatures across 4 cases: 4
- Diversity rule (>=3 if available): PASS

## Cite-key re-verification

- Allowed set source: analysis/VIII_ev_v1/section8B_evidence.csv
- Bibliography source: data/references.bib
- Selected keys total: 11
- Missing from allowed set: 0
- Missing from bibliography: 0
- Invalid keys list: none

## Contract-violation recheck

- Source: analysis/VIII_ev_v1/contract_violations.csv (section=8B)
- Violating selected keys: 0
- violations_flag per case: FALSE, FALSE, FALSE, FALSE

## Markdown path resolution + real-file verification

- Resolution policy: file_index.csv primary, II_markdown_inventory.csv fallback
- HIT_PRIMARY: 0
- HIT_FALLBACK: 11
- MISS: 0
- Duplicate-key path verification:
  - O_ISAC_035 -> selected existing file: C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_035\O_ISAC_035.md
  - O_ISAC_093 -> selected existing file: C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_093\O_ISAC_093.md

## Readiness

- Status: PASS
- Checks: 4 valid cases; all keys in section8B allowed set and references.bib; >=1 resolved markdown path per case; dedup PASS; motif-diversity PASS.
