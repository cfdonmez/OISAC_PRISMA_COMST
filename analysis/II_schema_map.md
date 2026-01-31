# II Schema Map (Optional)

Source
- data/extraction_results_v4/extraction_v4_unified.json

Modality labels
- study_level.classification.oisac_medium_class
  - Example: [i].study_level.classification.oisac_medium_class (e.g., O_ISAC_001 = wireless_vlc)
- study_level.classification.carrier_band
- study_level.classification.operational_environment
- study_level.classification.link_topology
- study_level.classification.mobility_context

Communication metrics
- scenario_level[*].comm_metrics.data_rate_gbps
- scenario_level[*].comm_metrics.capacity_bps_hz
- scenario_level[*].comm_metrics.spectral_efficiency_bps_hz
- scenario_level[*].comm_metrics.snr_db
- scenario_level[*].comm_metrics.osnr_db

Sensing metrics
- scenario_level[*].sensing_metrics.range_resolution_m
- scenario_level[*].sensing_metrics.spatial_resolution_m
- scenario_level[*].sensing_metrics.range_accuracy_m
- scenario_level[*].sensing_metrics.localization_error_m
- scenario_level[*].sensing_metrics.crb_crlb_value
- scenario_level[*].sensing_metrics.crb_parameter
- scenario_level[*].sensing_metrics.sensing_bandwidth_hz
- scenario_level[*].sensing_metrics.sensing_task_type

Waveform / resource hints
- scenario_level[*].waveform.comm_symbol_rate_gbaud
- scenario_level[*].waveform.comm_modulation_order
- scenario_level[*].waveform.comm_waveform_family
- scenario_level[*].waveform.sensing_waveform_family
- scenario_level[*].waveform.resource_partition

Channel models
- scenario_level[*].channel_wireless.turbulence_model
- scenario_level[*].channel_wireless.pointing_error_model
- scenario_level[*].channel_wireless.ambient_light_model
- scenario_level[*].channel_wireless.path_loss_model

Receiver / detection plane
- scenario_level[*].receiver.rx_detection_type

Integration signals
- scenario_level[*].integration.hardware_sharing_mode
- scenario_level[*].integration.duplexing_mode

Quality assessment
- quality_assessment.tqaf_* (five dimensions)

Example record path (illustrative)
- O_ISAC_001: [0].scenario_level[0].sensing_metrics.range_resolution_m

