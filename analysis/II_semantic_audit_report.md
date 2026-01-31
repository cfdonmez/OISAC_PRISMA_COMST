# II Semantic Audit Report (Pre-Writing)

## 1) Executive summary
- Schema separability decision: PARTIALLY SEPARABLE (conservative rules required; do not compute counts when ambiguity remains).
- Top risks:
  1) Range and spatial resolution fields are co-populated in most records (range_resolution_m + spatial_resolution_m both present in 181 of 221 records), preventing deterministic separation.
  2) SNR plane fields are co-populated in most records (osnr_db + snr_db both present in 191 of 221 records), so measurement-plane attribution is often ambiguous without paper text.
  3) Hybrid/THz labeling requires carrier-band proxies; Photo-THz bucket is not a native modality label and must be treated as a conservative proxy.

Sample check summary (n=20):
- Resolution-type check: {'AMBIGUOUS': 19, 'PASS': 1} (keyword-based spot-check; most cases ambiguous in text or schema).
- SNR-plane check: {'AMBIGUOUS': 18, 'PASS': 1, 'N/A': 1} (plane typically not explicit in text).

## 2) Schema separability audit (Delta r_min vs Delta z)
Decision: PARTIALLY SEPARABLE

Deterministic fields (available but not sufficient alone):
- range_resolution_m vs spatial_resolution_m:
  - data/extraction_results_v4/extraction_v4_unified.json[*].scenario_level[*].sensing_metrics.range_resolution_m
  - data/extraction_results_v4/extraction_v4_unified.json[*].scenario_level[*].sensing_metrics.spatial_resolution_m
- Disambiguators:
  - data/extraction_results_v4/extraction_v4_unified.json[*].study_level.classification.oisac_medium_class
  - data/extraction_results_v4/extraction_v4_unified.json[*].scenario_level[*].sensing_metrics.sensing_task_type

Conservative separability rules (use only when all conditions hold):
- Delta r_min (wireless ranging): require range_resolution_m present AND sensing_task_type includes "ranging" (or ToF/FMCW equivalent) AND oisac_medium_class is not cabled_fibre.
- Delta z (fiber granularity): require spatial_resolution_m present AND oisac_medium_class == cabled_fibre OR sensing_task_type indicates fiber sensing (e.g., vibration, temperature, fault_localization).
- If both range_resolution_m and spatial_resolution_m are present in a record, treat as NOT SEPARABLE unless the sensing task type clearly indicates one category.

Concrete path examples (illustrative):
- O_ISAC_035 (FSO): data/extraction_results_v4/extraction_v4_unified.json[34].scenario_level[*].sensing_metrics.range_resolution_m
- O_ISAC_006 (Fiber): data/extraction_results_v4/extraction_v4_unified.json[5].scenario_level[*].sensing_metrics.spatial_resolution_m

## 3) Stratified sample check (JSON vs Markdown)
Method: 5 papers per bucket selected deterministically from schema labels; Markdown spot-check via keyword cues (range resolution vs spatial granularity; OSNR vs SNR).

| Bucket | Paper_ID | JSON path | Markdown path | JSON res fields | MD res cue | Res check | SNR fields | SNR check |
|---|---|---|---|---|---|---|---|---|
| Fiber | O_ISAC_006 | data/extraction_results_v4/extraction_v4_unified.json[5] | data/processed_markdowns/O_ISAC_006/O_ISAC_006/O_ISAC_006.md | both | spatial | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |
| Fiber | O_ISAC_007 | data/extraction_results_v4/extraction_v4_unified.json[6] | data/processed_markdowns/O_ISAC_007/O_ISAC_007/O_ISAC_007.md | both | none | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |
| Fiber | O_ISAC_010 | data/extraction_results_v4/extraction_v4_unified.json[9] | data/processed_markdowns/O_ISAC_010/O_ISAC_010/O_ISAC_010.md | ambiguous | none | AMBIGUOUS | osnr:False snr:True | PASS |
| Fiber | O_ISAC_013 | data/extraction_results_v4/extraction_v4_unified.json[12] | data/processed_markdowns/O_ISAC_013/O_ISAC_013/O_ISAC_013.md | ambiguous | both | AMBIGUOUS | osnr:False snr:False | N/A |
| Fiber | O_ISAC_014 | data/extraction_results_v4/extraction_v4_unified.json[13] | data/processed_markdowns/O_ISAC_014/O_ISAC_014/O_ISAC_014.md | both | none | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |
| FSO | O_ISAC_012 | data/extraction_results_v4/extraction_v4_unified.json[11] | data/processed_markdowns/O_ISAC_012/O_ISAC_012/O_ISAC_012.md | both | none | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |
| FSO | O_ISAC_023 | data/extraction_results_v4/extraction_v4_unified.json[22] | data/processed_markdowns/O_ISAC_023/O_ISAC_023/O_ISAC_023.md | both | range | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |
| FSO | O_ISAC_034 | data/extraction_results_v4/extraction_v4_unified.json[33] | data/processed_markdowns/O_ISAC_034/O_ISAC_034/O_ISAC_034.md | range | none | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |
| FSO | O_ISAC_035 | data/extraction_results_v4/extraction_v4_unified.json[34] | data/processed_markdowns/O_ISAC_035/O_ISAC_035/O_ISAC_035.md | range | range | PASS | osnr:True snr:True | AMBIGUOUS |
| FSO | O_ISAC_048 | data/extraction_results_v4/extraction_v4_unified.json[47] | data/processed_markdowns/O_ISAC_048/O_ISAC_048/O_ISAC_048.md | both | none | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |
| VLC | O_ISAC_001 | data/extraction_results_v4/extraction_v4_unified.json[0] | data/processed_markdowns/O_ISAC_001/O_ISAC_001/O_ISAC_001.md | both | spatial | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |
| VLC | O_ISAC_003 | data/extraction_results_v4/extraction_v4_unified.json[2] | data/processed_markdowns/O_ISAC_003/O_ISAC_003/O_ISAC_003.md | both | none | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |
| VLC | O_ISAC_009 | data/extraction_results_v4/extraction_v4_unified.json[8] | data/processed_markdowns/O_ISAC_009/O_ISAC_009/O_ISAC_009.md | both | none | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |
| VLC | O_ISAC_015 | data/extraction_results_v4/extraction_v4_unified.json[14] | data/processed_markdowns/O_ISAC_015/O_ISAC_015/O_ISAC_015.md | range | none | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |
| VLC | O_ISAC_022 | data/extraction_results_v4/extraction_v4_unified.json[21] | data/processed_markdowns/O_ISAC_022/O_ISAC_022/O_ISAC_022.md | both | none | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |
| Photo-THz | O_ISAC_002 | data/extraction_results_v4/extraction_v4_unified.json[1] | data/processed_markdowns/O_ISAC_002/O_ISAC_002/O_ISAC_002.md | both | range | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |
| Photo-THz | O_ISAC_016 | data/extraction_results_v4/extraction_v4_unified.json[15] | data/processed_markdowns/O_ISAC_016/O_ISAC_016/O_ISAC_016.md | both | range | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |
| Photo-THz | O_ISAC_026 | data/extraction_results_v4/extraction_v4_unified.json[25] | data/processed_markdowns/O_ISAC_026/O_ISAC_026/O_ISAC_026.md | both | range | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |
| Photo-THz | O_ISAC_029 | data/extraction_results_v4/extraction_v4_unified.json[28] | data/processed_markdowns/O_ISAC_029/O_ISAC_029/O_ISAC_029.md | both | range | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |
| Photo-THz | O_ISAC_043 | data/extraction_results_v4/extraction_v4_unified.json[42] | data/processed_markdowns/O_ISAC_043/O_ISAC_043/O_ISAC_043.md | both | range | AMBIGUOUS | osnr:True snr:True | AMBIGUOUS |

Legend:
- JSON res fields: range_only / spatial_only / both / ambiguous derived from presence of range_resolution_m and spatial_resolution_m in the record.
- MD res cue: range / spatial / both / none based on keyword cues in processed markdown.
- PASS = JSON and Markdown cues agree; AMBIGUOUS = insufficient or mixed evidence; N/A = no SNR fields in JSON.

## 4) Notation alignment audit (Section I)
Forbidden tokens check:
- Delta R / \Delta R count = 0 / 0
- sigma_R / \sigma_R count = 0 / 0

Alternative symbols check:
- Delta d / \Delta d count = 0 / 0
- sigma_d / \sigma_d count = 0 / 0

Recommendation:
- No alternative symbols detected; no equivalence statement required.

## 5) Measurement-plane governance check
- II_metric_governance.md already contains an explicit rule: OSNR and electrical SNR are separate planes and must not be mixed without an explicit mapping model.
- No additional insert is required.

## 6) Scope-leak guardrails for Section II
- Guardrail 1: Do not insert taxonomy tables or modality prevalence counts (reserved for Section IV).
- Guardrail 2: Do not report numeric Pareto frontiers or trade-off statistics (reserved for Section V).
- Guardrail 3: Do not drift into paper-by-paper enumeration; Section II must remain concept/physics-driven.
