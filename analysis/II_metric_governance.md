# II Metric Governance Layer (PRISMA-Consistent)

Purpose
- Provide a defensible, PRISMA-aligned metric contract for Section II that constrains later synthesis (Sections IV-V) without introducing new evidence claims.
- Enforce consistent definitions, units, measurement planes, modality applicability, and record-level inclusion rules.

Global governance rules
- Canonical definitions only; any nontrivial statement must be either theory-standard or supported later by extraction evidence.
- Do not compute or compare metrics across modalities without explicit measurement-plane notes.
- Do not mix fiber spatial granularity (Delta z) with wireless range resolution (Delta r_min).
- Do not introduce Delta R or sigma_R tokens; only Delta r_min, sigma_r, CRQ_Delta.

Metric A) Communication rate R
Definition + unit
- R: reported communication data rate, in bps (convert from Gbps when needed).
Normalization rule
- If data_rate_gbps present, convert to bps by * 1e9.
- If only spectral_efficiency_bps_hz is present, do not infer R unless a bandwidth field is explicitly given; otherwise leave R undefined.
Measurement plane
- R is reported under the measurement plane that matches the reported OSNR or electrical SNR; do not compare across planes without an explicit mapping note.
Modality applicability
- All modalities (fiber, FSO, VLC, photo-THz, hybrid).
Record-level inclusion rule
- Include a record as R-available if comm_metrics.data_rate_gbps or comm_metrics.capacity_bps_hz is numeric and >0.
Disambiguation rules
- Per-channel vs aggregate rate: if not specified, label as "reported rate" and do not compare with aggregate totals.
Edge case
- Fiber studies may report aggregate multi-core/WDM throughput; do not compare with single-link wireless rates without stating aggregation scope.
Schema mapping (candidate fields)
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].comm_metrics.data_rate_gbps
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].comm_metrics.capacity_bps_hz
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].comm_metrics.spectral_efficiency_bps_hz

Metric A2) Effective bandwidth B_eff
Definition + unit
- B_eff: effective (usable) bandwidth for sensing or ranging, in Hz.
Normalization rule
- Use sensing_metrics.sensing_bandwidth_hz if present; otherwise leave B_eff undefined (do not infer from symbol rate or modulation order in Section II).
Measurement plane
- B_eff is a signal property; must be tied to the plane where the measurement model is defined.
Modality applicability
- Wireless ranging and photo-THz; not required for fiber Delta z.
Record-level inclusion rule
- Include if sensing_metrics.sensing_bandwidth_hz is numeric and >0.
Disambiguation rules
- Do not substitute comm_symbol_rate_gbaud for B_eff unless explicitly stated by the source.
Edge case
- Some studies report allocated bandwidth but not effective bandwidth; treat as non-computable for Delta r_min in synthesis.
Schema mapping
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].sensing_metrics.sensing_bandwidth_hz

Metric B) Delta r_min (bandwidth-limited two-way range resolution)
Definition + unit
- Delta r_min = v / (2 B_eff); units: meters; v=c in free space, v=c/n_g in guided media.
Normalization rule
- Prefer explicit range_resolution_m when available; only compute from B_eff if the record explicitly supports two-way ranging.
Measurement plane
- Ranging resolution is defined at the sensing observation plane; do not conflate with estimator accuracy.
Modality applicability
- Wireless/FSO/VLC/photo-THz ranging tasks; not fiber spatial granularity.
Record-level inclusion rule
- Include if sensing_metrics.range_resolution_m is numeric AND (oisac_medium_class indicates wireless/photo-THz OR sensing_task_type indicates ranging/ToF/FMCW).
Disambiguation rules
- If only spatial_resolution_m is present in fiber or if task type is DAS/OTDR, treat as Delta z, not Delta r_min.
Do-not-compare warnings
- Do not compute CRQ_Delta when only Delta z is available.
Edge case
- Hybrid-labeled records may include photonic-THz bridging; require sensing_task_type or wireless carrier band to qualify as Delta r_min.
Schema mapping
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].sensing_metrics.range_resolution_m
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].sensing_metrics.sensing_task_type
- data/extraction_results_v4/extraction_v4_unified.json -> [i].study_level.classification.oisac_medium_class

Metric C) sigma_r (estimator-dependent accuracy)
Definition + unit
- sigma_r: estimator RMSE of range or localization error; units: meters.
Normalization rule
- Use range_accuracy_m or localization_error_m as reported; do not convert between 1D/2D/3D errors unless explicitly specified.
Measurement plane
- Estimator accuracy is post-processing; do not label as resolution.
Modality applicability
- All modalities with localization/ranging tasks.
Record-level inclusion rule
- Include if sensing_metrics.range_accuracy_m or sensing_metrics.localization_error_m is numeric and >0.
Disambiguation rules
- Do not treat accuracy as resolution; keep sigma_r distinct from Delta r_min.
Edge case
- VLC localization often reports 2D/3D error without dimensionality; keep as "reported accuracy".
Schema mapping
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].sensing_metrics.range_accuracy_m
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].sensing_metrics.localization_error_m

Metric D) CRB/FIM-derived bounds
Definition + unit
- CRB/CRLB on an estimated parameter; units depend on parameter (range in m or variance in m^2).
Normalization rule
- Use crb_crlb_value as reported; interpret using crb_parameter.
Measurement plane
- Requires explicit observation model; do not claim comparability across different estimators or planes.
Modality applicability
- Any modality where bounds are reported.
Record-level inclusion rule
- Include if crb_crlb_value is numeric and crb_parameter is provided.
Disambiguation rules
- If crb_parameter is not "range" or "delay", do not cast to range bound.
Edge case
- Some works report variance vs standard deviation; treat as reported, do not take square-root without explicit evidence.
Schema mapping
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].sensing_metrics.crb_crlb_value
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].sensing_metrics.crb_parameter

Metric E) Delta z (fiber spatial granularity / gauge length)
Definition + unit
- Delta z: minimum resolvable fiber segment or gauge length; units: meters.
Normalization rule
- Use spatial_resolution_m only when modality is fiber (cabled_fibre) or task type indicates DAS/OTDR.
Measurement plane
- Fiber sensing plane; not a ranging resolution metric.
Modality applicability
- Fiber/cabled only.
Record-level inclusion rule
- Include if spatial_resolution_m is numeric AND oisac_medium_class == cabled_fibre (or task type indicates DAS/OTDR).
Disambiguation rules
- If spatial_resolution_m appears in wireless, treat as "reported spatial resolution" and do not map to Delta z.
Do-not-compare warnings
- Do not use Delta z in CRQ_Delta or compare directly with Delta r_min.
Edge case
- Some fiber works report gauge length in text but not normalized; ensure units are meters before use.
Schema mapping
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].sensing_metrics.spatial_resolution_m
- data/extraction_results_v4/extraction_v4_unified.json -> [i].study_level.classification.oisac_medium_class

Metric F) Signal quality plane (OSNR vs electrical SNR)
Definition + unit
- OSNR: optical domain SNR prior to detection; SNR: electrical post-detection.
Normalization rule
- Treat osnr_db and snr_db as separate planes; never convert without explicit receiver model.
Measurement plane
- Must be stated wherever SNR is referenced; align with receiver detection type.
Modality applicability
- OSNR: coherent optical; SNR: IM/DD and post-detection systems.
Record-level inclusion rule
- Include osnr_db if numeric; include snr_db if numeric.
Disambiguation rules
- If both are present, record both planes; do not average or substitute.
Edge case
- Some records list OSNR but use IM/DD; flag as potentially inconsistent and avoid synthesis claims.
Schema mapping
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].comm_metrics.osnr_db
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].comm_metrics.snr_db
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].receiver.rx_detection_type

Metric G) Trade-off constructs (CRQ_Delta and Pareto set)
Definition + unit
- CRQ_Delta := R / Delta r_min (bps/m). Pareto frontier: nondominated set in (R, sensing-metric) space.
Normalization rule
- Compute CRQ_Delta only when both R and Delta r_min are available; never use Delta z as a surrogate.
Measurement plane
- Must inherit the measurement plane note used for R and Delta r_min.
Modality applicability
- Wireless/photo-THz entries with ranging; fiber excluded unless Delta r_min is explicitly reported.
Record-level inclusion rule
- Include for CRQ_Delta if R and range_resolution_m are numeric and satisfy Delta r_min criteria.
Disambiguation rules
- Do not compute CRQ_Delta from spatial_resolution_m.
Edge case
- Hybrid modality labels may hide photonic-THz cases; require explicit ranging task or range_resolution_m.
Schema mapping
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].comm_metrics.data_rate_gbps
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].sensing_metrics.range_resolution_m
- data/extraction_results_v4/extraction_v4_unified.json -> [i].scenario_level[*].tradeoff.*

