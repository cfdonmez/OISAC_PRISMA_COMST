# II High-Confidence QA

Fields used (must exist in analysis/II_schema_map.md):
- study_level.classification.oisac_medium_class
- study_level.classification.carrier_band
- scenario_level.sensing_metrics.sensing_task_type
- scenario_level.sensing_metrics.range_resolution_m
- scenario_level.sensing_metrics.spatial_resolution_m
- scenario_level.comm_metrics.data_rate_gbps
- scenario_level.comm_metrics.capacity_bps_hz
- scenario_level.comm_metrics.spectral_efficiency_bps_hz
- scenario_level.comm_metrics.snr_db
- scenario_level.comm_metrics.osnr_db

Manual verification list:
- O_ISAC_023: ESNR: # <span id="page-11-1"></span><span id="page-11-0"></span>D. Robustness to Channel Variations :: respectively. Subsequently, Fig. 9 illustrates the sensing RMSE w.r.t. different electrical SNRs, i.e., $\mathbb{E}(|H_s x^+(n)|^2)/\mathbb{E}(|w_s(n)|^2)$ . The sensing performance deteriorates due to the stronger atmospheric
- O_ISAC_061: ESNR: #### <span id="page-11-3"></span>*C. Practical C&S Performance Metrics* :: <span id="page-12-1"></span>Fig. 11. BER for communication w.r.t. electrical SNR under different constraints on light-field SINR.
- O_ISAC_100: ESNR: # <span id="page-11-0"></span>*B. Communication Performance Metrics* :: BER and normalized MSE of DCO and ACO components w.r.t. electrical SNR for communication, i.e., SNRe,c = Pe/ (N∆fNc), are displayed separately in Fig. [7.](#page-12-1)
- O_ISAC_132: OSNR: ## *A. Antenna Polarization Diversity for High-Speed Polarization Multiplexing Wireless Signal Delivery at W-band* :: Fig. 3. (a) The relationship between BER and OSNR of 128 Gbit/s signal after 2 m wireless with and without fiber transmission. (b) The relationship

Limitations:
- Co-occurrence of range_resolution_m and spatial_resolution_m forces AMBIGUOUS unless manual evidence resolves semantics.
- OSNR and SNR often co-occur; plane attribution remains AMBIGUOUS without explicit plane cues.
- DRMIN_DEFENSIBLE requires ranging task + non-fiber modality; many records lack explicit task typing.