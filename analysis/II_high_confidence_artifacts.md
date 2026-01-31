Resolved input paths:
- c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\drafts\section_01_introduction.md
- c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\analysis\II_metric_governance.md
- c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\analysis\II_schema_map.md
- c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\analysis\II_semantic_audit_report.md
- c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\analysis\II_semantic_audit_artifacts.md
- c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\extraction_results_v4\extraction_v4_unified.json
- c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_023\O_ISAC_023\O_ISAC_023.md
- c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_061\O_ISAC_061\O_ISAC_061.md
- c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_100\O_ISAC_100\O_ISAC_100.md
- c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_132\O_ISAC_132\O_ISAC_132.md

Extraction source used:
- c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\extraction_results_v4\extraction_v4_unified.json

Commands/search patterns used:
- rg --files -g "II_metric_governance.md" -g "II_schema_map.md" -g "II_semantic_audit_report.md" -g "II_semantic_audit_artifacts.md"

Field mappings used:
- oisac_modality_label := study_level.classification.oisac_medium_class
- carrier_band_label := study_level.classification.carrier_band
- has_rate := comm_metrics.data_rate_gbps present
- has_spectral_efficiency := comm_metrics.capacity_bps_hz or spectral_efficiency_bps_hz present
- has_range_resolution_field := sensing_metrics.range_resolution_m present
- has_spatial_resolution_field := sensing_metrics.spatial_resolution_m present
- osnr_db/snr_db for plane labeling