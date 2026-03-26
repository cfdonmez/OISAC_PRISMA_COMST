### II-D Writing Recipe Audit (Not for manuscript)
R-1 Structure compliance: PASS - Headings match II-D structure (D, D.1–D.4, Lesson (D)).
R-2 Required equations present: PASS - Delta r_min = v/(2 B_eff) with v=c and v≈c/n_g; sigma_r RMSE; CRB delay exemplar + range mapping with beta defined; CRQ_Delta = R/Delta r_min.
R-3 Governance compliance: PASS - No forbidden tokens; no OSNR->SNR conversion implied; Delta z not substituted into CRQ_Delta; explicit warning present.
R-4 Evidence compliance: PASS - All literature-usage claims anchored; context verification logged for each anchor; no unanchored prevalence claims.
R-5 Section I stylistic alignment: PASS - Citation tokens [O_ISAC_XXX] used correctly; tone and Markdown consistent.

Resolved input paths used:
- drafts/section_01_introduction.md
- review_package/section_02_fundamentals_template.md
- review_package/section_02_methodology.md
- drafts/section_02_fundamentals_draft.md
- analysis/II_met_gov.md
- review_package/patch_notes_for_writing.md
- analysis/II_ev_v2/section2D_evidence_LLM.csv (consulted; not used due to missing locators)
- analysis/II_sch_map.md (not used)

Evidence anchors used (deduplicated):
- O_ISAC_026 | Jianyang Shi > I. INTRODUCTION | L74-L84 | strength_final=strong | meaning_final=bandwidth_limited_range_resolution | context_verified=YES
- O_ISAC_034 | <span id="page-0-1"></span>I. INTRODUCTION > <span id="page-1-3"></span>*B. Signal Structure* > B. Sensing Metrics | L145-L155 | strength_final=strong | meaning_final=bandwidth_limited_range_resolution | context_verified=YES
- O_ISAC_006 | *A. Solution based on multiplexing technology* | L79-L95 | strength_final=strong | meaning_final=delta_z_spatial_granularity | context_verified=YES
- O_ISAC_013 | Single-Ended > 100-km Distributed Vibration Sensor Based on OFDR Using Pearson Correlation Coefficient | L3-L19 | strength_final=strong | meaning_final=delta_z_spatial_granularity | context_verified=YES

Claims weakened/removed due to missing/ambiguous evidence:
- No literature-usage claims for CRB/FIM prevalence or specific estimator choices; treated as theory-standard definitions.

Corrections to evidence labels (strength/meaning):
- None. Anchors remain consistent with context windows.
