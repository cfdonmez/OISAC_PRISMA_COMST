# IE Evidence Map (Audit Trail)

**Data scope:** data/extraction_results_v4/extraction_v4_unified.json joined with data/processed_markdowns/O_ISAC_* by Paper_ID (intersection size = 221).

| Contribution ID | Claim snippet | Supporting evidence (stat or citation keys) | JSON paths used | Notes |
|---|---|---|---|---|
| C1 | PRISMA evidence base and TQAF quality scoring | N=221 records; bibliographic year available for 219 records, with 210 in 2020-2025; TQAF complete (all five fields) for 208 studies; PRISMA citation [14] | study_level.bibliographic.year; quality_assessment.tqaf_modelling_fidelity / tqaf_validation_strength / tqaf_experimental_validity / tqaf_metric_completeness / tqaf_reproducibility | Query: count records; count non-null years; count years in [2020, 2025]; count records with all five tqaf_* fields present. |
| C2 | Cross-modality taxonomy coverage | Modality counts: fiber=46, FSO=19, VLC/visible-light/UV=26, photo-THz=1, hybrid=116 (remaining labels grouped as other) | study_level.classification.oisac_medium_class | Query: map oisac_medium_class via normalization table; count per normalized category. |
| C3 | Reporting contract and trade-off coverage using Delta r_min, sigma_r, CRQ_Delta | data_rate_gbps=217 papers; range_resolution_m (Delta r_min)=213; range_accuracy_m (sigma_r)=208; crb_crlb_value=171; both data_rate_gbps and range_resolution_m present in 213 papers (CRQ_Delta feasible) | scenario_level.comm_metrics.data_rate_gbps; scenario_level.sensing_metrics.range_resolution_m; scenario_level.sensing_metrics.range_accuracy_m; scenario_level.sensing_metrics.crb_crlb_value | Query: per paper, scan all scenarios; mark presence if any scenario has the field populated; count papers with both data_rate_gbps and range_resolution_m. |
| C4 | Enabler-centric synthesis (ORIS/OPA/ML) | machine_learning_used=53; ris_present (ORIS)=8; opa_present=7 | study_level.enabling_tech.machine_learning_used / ris_present / opa_present | Query: count papers where the field value is True/yes/1. |
| C5 | Cross-domain transfer map tied to applications | 15 application domains appear in >=2 modality classes; 8 domains in >=3; high-frequency domains: industrial_manufacturing=65, vehicular=60, indoor_positioning=56, 6g_networks=46 | study_level.application.application_domain + study_level.classification.oisac_medium_class | Query: for each application_domain, compute set of normalized modalities; count domains with >=2 and >=3 modalities; count application label frequencies (list entries counted once per record where present). |

**File globs used:**
- data/extraction_results_v4/extraction_v4_unified.json
- data/processed_markdowns/O_ISAC_*

**Normalization notes:**
- Modality mapping: cabled_fibre->fiber; wireless_fso->fso; wireless_vlc/vlc/visible_light/wireless_uv->vlc; terahertz->photo_thz; hybrid->hybrid; others grouped as other/retroreflective/rf.
- Presence tests treat any non-empty field value as reported, and any True/yes/1 value as positive for enabler tags.


## Risk Check Sampling (I-E)

### Risk Check 1: Delta r_min coverage ambiguity
**Extraction field used for counting resolution coverage:** scenario_level.sensing_metrics.range_resolution_m.

**Fiber (cabled) samples (range_resolution_m present):**
| Paper_ID | Observation in processed markdown | Path |
|---|---|---|
| O_ISAC_006 | Uses fiber-sensing spatial resolution language (DAS/DOFS) rather than bandwidth-limited ranging. | data/processed_markdowns/O_ISAC_006/O_ISAC_006/O_ISAC_006.md |
| O_ISAC_013 | Reports "sensing spatial resolution" in meters for DVS. | data/processed_markdowns/O_ISAC_013/O_ISAC_013/O_ISAC_013.md |
| O_ISAC_024 | Reports spatial resolution (1 m) for distributed sensing over fiber link. | data/processed_markdowns/O_ISAC_024/O_ISAC_024/O_ISAC_024.md |
| O_ISAC_046 | Reports 20-m spatial-resolution for DAS over multicore fiber. | data/processed_markdowns/O_ISAC_046/O_ISAC_046/O_ISAC_046.md |
| O_ISAC_033 | Reports spatial resolution (10 m) tied to chirped pulse bandwidth in DAS. | data/processed_markdowns/O_ISAC_033/O_ISAC_033/O_ISAC_033.md |

**Wireless/FSO/VLC/THz samples (range_resolution_m present):**
| Paper_ID | Observation in processed markdown | Path |
|---|---|---|
| O_ISAC_001 | Mentions high resolution in both range and Doppler via ambiguity function (VLC radar/ToF context). | data/processed_markdowns/O_ISAC_001/O_ISAC_001/O_ISAC_001.md |
| O_ISAC_003 | Provides delay resolution (0.2 ns), which maps to range resolution. | data/processed_markdowns/O_ISAC_003/O_ISAC_003/O_ISAC_003.md |
| O_ISAC_009 | Improves resolution of estimated CIRs for positioning (delay-domain resolution). | data/processed_markdowns/O_ISAC_009/O_ISAC_009/O_ISAC_009.md |
| O_ISAC_012 | Describes LiDAR as having greater resolution in optical sensing context. | data/processed_markdowns/O_ISAC_012/O_ISAC_012/O_ISAC_012.md |
| O_ISAC_115 | Explicit distance resolution (1 cm) tied to required bandwidth (>30 GHz). | data/processed_markdowns/O_ISAC_115/O_ISAC_115/O_ISAC_115.md |

**Finding:** Both meanings appear in the corpus: fiber papers use spatial granularity (Delta z) language, while wireless/FSO/VLC papers use range/delay resolution. I-E updated accordingly.

### Risk Check 2: Hybrid vs Photo-THz labeling
**Modality distribution from extraction JSON (normalized):** fiber=46, FSO=19, VLC=26, photo-THz=1, hybrid=116 (plus other/retroreflective/rf).

**Hybrid samples (10) and optical-THz bridging check:**
| Paper_ID | THz/photonic-THz bridging evidence | Path |
|---|---|---|
| O_ISAC_002 | Yes: photonic terahertz ISAC; fiber-optic link to THz wireless bridging. | data/processed_markdowns/O_ISAC_002/O_ISAC_002/O_ISAC_002.md |
| O_ISAC_004 | No THz bridging observed in sampled text. | data/processed_markdowns/O_ISAC_004/O_ISAC_004/O_ISAC_004.md |
| O_ISAC_005 | No (FSO + mmWave context; not photonic-THz bridging). | data/processed_markdowns/O_ISAC_005/O_ISAC_005/O_ISAC_005.md |
| O_ISAC_008 | No THz bridging observed (OPA/photonic components, no THz carrier). | data/processed_markdowns/O_ISAC_008/O_ISAC_008/O_ISAC_008.md |
| O_ISAC_011 | No THz bridging observed in sampled text. | data/processed_markdowns/O_ISAC_011/O_ISAC_011/O_ISAC_011.md |
| O_ISAC_016 | Yes: photonic sub-THz ISAC with fiber-THz-fiber architecture. | data/processed_markdowns/O_ISAC_016/O_ISAC_016/O_ISAC_016.md |
| O_ISAC_018 | No explicit THz bridging observed in sampled text. | data/processed_markdowns/O_ISAC_018/O_ISAC_018/O_ISAC_018.md |
| O_ISAC_021 | No THz bridging observed in sampled text (FSO-centric). | data/processed_markdowns/O_ISAC_021/O_ISAC_021/O_ISAC_021.md |
| O_ISAC_026 | Photonic mmWave fiber-wireless integration (W-band); not THz but optical-wireless bridging. | data/processed_markdowns/O_ISAC_026/O_ISAC_026/O_ISAC_026.md |
| O_ISAC_027 | No THz bridging observed (fiber sensing). | data/processed_markdowns/O_ISAC_027/O_ISAC_027/O_ISAC_027.md |

**Finding:** Multiple hybrid-labeled papers are photonic-THz/sub-THz bridging (e.g., O_ISAC_002, O_ISAC_016); I-E now notes that such studies can appear under hybrid depending on the extraction label ontology.

## PATCH2 Numeric Refinement (Contribution-3)

| Item | Value | JSON paths used | Counting logic |
|---|---:|---|---|
| N_rate_and_resType | 213 | scenario_level.comm_metrics.data_rate_gbps; scenario_level.sensing_metrics.range_resolution_m | Per paper: mark true if any scenario has data_rate_gbps and any scenario has range_resolution_m; count papers where both are true. |
| N_rate_and_Drmin | 160 | scenario_level.comm_metrics.data_rate_gbps; scenario_level.sensing_metrics.range_resolution_m; scenario_level.sensing_metrics.sensing_task_type | Per paper: require data_rate_gbps + range_resolution_m, and at least one scenario with sensing_task_type containing "ranging" (conservative proxy for bandwidth-limited Delta r_min). |
