# IE Implementation Plan

## 1) Constraints extracted (from guides)
- COMST_master_recipe.md: keep Introduction lean, provide contribution bullets and organization map; formal COMST tone; avoid overlong intro.
- master_writing_guide.md: COMST-style headings (Roman numerals + lettered subsections); every subsection ends with a Lesson statement; quantitative claims must be traceable to extracted data; no marketing language.
- introduction_templates.md: contributions list in I-D/E with compact structure; include a Lesson sentence at the end of the subsection.
- methodology_template.md: PRISMA 2020 emphasis; include TQAF quality assessment when claiming systematic rigor.
- body_section_templates.md: avoid annotated-bibliography style; synthesize by axes (relevant for contribution phrasing).
- abstract_templates.md: consistent academic voice and transition markers; keep claims precise.
- surveyOutline.md: section map (II Fundamentals, III Methodology, IV Taxonomy, V Performance, VI Enablers, VII Applications, VIII Challenges) used for contribution-to-section mapping.
- systemPatterns.md: use O_ISAC_XXX IDs and extraction_results_v4 outputs as authoritative evidence sources.
- goldenModel.md: enforce gap-selling logic and evidence traceability; avoid legacy script-derived claims.

## 2) Data fields found in extraction_results_v4
Source: data/extraction_results_v4/extraction_v4_unified.json (221 records) joined with data/processed_markdowns/O_ISAC_* by Paper_ID.
- study_level.bibliographic.year
- study_level.classification.oisac_medium_class
- study_level.application.application_domain
- study_level.evidence.evidence_type, validation_baselines_present, reproducibility_artifacts
- study_level.enabling_tech.ris_present, opa_present, machine_learning_used
- scenario_level.integration.hardware_sharing_mode
- scenario_level.waveform.isac_waveform_relationship
- scenario_level.comm_metrics.data_rate_gbps
- scenario_level.sensing_metrics.range_resolution_m, range_accuracy_m, crb_crlb_value
- quality_assessment.tqaf_* (five dimensions)

## 3) Statistics to compute (and how)
- Corpus size (N): count records in extraction_v4_unified.json after intersection with processed_markdowns by Paper_ID.
- Year coverage: count non-null bibliographic.year; count within 2020-2025; report both.
- Modality distribution: count oisac_medium_class values; normalize to fiber/FSO/VLC/photo-THz/hybrid (+ other) via mapping table.
- Reporting coverage for metric contract: per-paper presence of data_rate_gbps, range_resolution_m (Delta r_min), range_accuracy_m (sigma_r), crb_crlb_value; count papers with both data_rate_gbps and range_resolution_m to justify CRQ_Delta.
- Enabler frequencies: count papers where ris_present, opa_present, machine_learning_used are True.
- Cross-domain transfer via applications: for each application_domain, compute unique normalized modality set; count domains with >=2 and >=3 modalities; report top-frequency application domains.
- TQAF availability: count papers with all five tqaf_* fields populated.

## 4) Rewrite outline for I-E (gap/section mapping)
1) PRISMA evidence base + TQAF scoring (Gap 2) -> Section III
2) Unified taxonomy with modality coverage counts (Gap 1) -> Section IV
3) Reporting contract + trade-off synthesis using Delta r_min, sigma_r, CRQ_Delta coverage stats (Gap 3) -> Section V
4) Enabling-technology synthesis with ORIS/OPA/ML frequencies (Gap 5) -> Section VI
5) Cross-domain transfer map via modality-application matrix (Gap 4) -> Section VII

## 5) Edit operations
- File: drafts/section_01_introduction.md
- Anchor: replace content under heading "## E. Contributions of This Survey" up to (but not including) "## F. Organization of This Paper".
- Preserve: citation keys (e.g., [14]), metric symbols Delta r_min, sigma_r, CRQ_Delta, and the Lesson 2 statement.
