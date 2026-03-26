# COMST_review_bundle_03_audits.md

## review_package/section_02A_audit.md

﻿### II-A Writing Recipe Audit (Not for manuscript)
R-1 Structure compliance: PASS - Headings include II, A, A.1, A.2, and Lesson (A).
R-2 Model inclusion: PASS - Coherent model present with symbols defined; IM/DD model present with x(t) >= 0 and responsivity R defined; IM/DD intensity-clarification sentence included.
R-2b Paradigm coverage: PASS - Communication-centric, sensing-centric, and joint design explicitly defined; objective-form exemplars included; paradigm-to-mechanism bridge bullets present.
R-3 Metric governance compliance: PASS - OSNR vs electrical SNR separation stated; no OSNR->SNR conversion claim; bridge sentence present (tau=2r/v -> Delta r_min; fiber uses Delta z); no forbidden tokens introduced.
R-4 Evidence compliance: PASS - All literature-usage claims are anchored; >=2 strong anchors per plane; context-window verification performed for each anchor.
R-5 Section I stylistic alignment: PASS - Citation style [O_ISAC_XXX] and COMST tone preserved.

Evidence anchors used (deduplicated):
- O_ISAC_056 | # Optical ISAC: Fundamental Performance Limits and Transceiver Design | L7-L11 | strength_final=strong | plane_final=OPTICAL_PLANE | context-verified=YES
- O_ISAC_080 | # Integrated Communication and In-band Spectrum Polarization-Based Sensing via Fraction-Division Non-Orthogonal Multiple Access | L5-L9 | strength_final=strong | plane_final=OPTICAL_PLANE | context-verified=YES
- O_ISAC_061 | # *A. Convergence of BCD Algorithm* > #### *B. Optimal Beampattern and C&S Tradeoff* > #### <span id="page-11-3"></span>*C. Practical C&S Performance Metrics* | L638-L642 | strength_final=strong | plane_final=ELECTRICAL_PLANE | context-verified=YES
- O_ISAC_023 | # Free-Space Optical Integrated Sensing and Communication Based on DCO-OFDM: Performance Metrics and Resource Allocation > ## *C. Computational Complexity and Scalability* > ### <span id="page-11-1"></span><span id="page-11-0"></span>D. Robustness to Channel Variations | L751-L755 | strength_final=strong | plane_final=ELECTRICAL_PLANE | context-verified=YES

Claims weakened/removed due to missing or ambiguous evidence:
- No OSNR->SNR conversion or plane inference from generic "SNR"; generic SNR remains AMBIGUOUS per governance.
- Avoided prevalence claims (e.g., "most studies") about SNR reporting practices.

Corrections to evidence labels (strength/plane):
- None. All used anchors remain consistent with surrounding context.

Resolved input paths used:
- drafts/section_01_introduction.md
- drafts/section_02_methodology.md
- reference_compendium/s02_fund_tpl.md (resolved from missing drafts/section_02_fundamentals_template.md)
- drafts/section_02_fundamentals_draft.md
- analysis/II_met_gov.md
- analysis/II_ev_v2/patch_notes_for_writing.md
- analysis/II_ev_v2/section2A_evidence.csv
- analysis/II_sch_map.md (not used)


## review_package/section_02B_audit.md

﻿### II-B Writing Recipe Audit (Not for manuscript)
R-1 Structure compliance: PASS - Headings include B, B.1, B.2, B.3, B.4, and Lesson (B).
R-2 Channel model inclusion: PASS - B.1 includes linear dispersive model and conceptual NLSE; B.2 includes multiplicative fading/pointing + Beer-Lambert attenuation; B.3 includes Lambertian/impulse-response framing + noise note; B.4 includes optical-vs-THz separation and impairment note (evidence-backed).
R-3 Metric governance compliance: PASS - No forbidden tokens introduced; no OSNR->SNR conversion implied; Delta r_min vs Delta z separation stated in B.1.
R-4 Evidence compliance: PASS - All representative-works claims anchored; Beer-Lambert anchors >=2 strong; multipath/NLoS anchors >=2 strong; photonic-THz noise-regime anchors >=2 strong; context verification logged for each anchor.
R-5 Section I stylistic alignment: PASS - Citation style [O_ISAC_XXX] and tone consistent with Section I/II-A.

Resolved input paths used:
- drafts/section_01_introduction.md
- reference_compendium/s02_fund_tpl.md
- drafts/section_02_methodology.md
- drafts/section_02A_fundamentals.md
- drafts/section_02_fundamentals_draft.md
- analysis/II_met_gov.md
- analysis/II_ev_v2/patch_notes_for_writing_2B.md
- analysis/II_ev_v2/section2B_evidence.csv
- analysis/II_ev_v2/section2B_evidence_LLM.csv (consulted as candidate-only)

Evidence anchors used (deduplicated):
- O_ISAC_035 | ### II. SYSTEM MODEL AND METHODOLOGY > # B. FSO Channel | L75-L79 | strength_final=strong | claim_tag=attenuation_beer_lambert | context-verified=YES
- O_ISAC_034 | # IV. NUMERICAL RESULTS | L205-L205 | strength_final=strong | claim_tag=attenuation_beer_lambert | context-verified=YES
- O_ISAC_022 | ## <span id="page-3-0"></span>D. The Optical Wireless Channel | L136-L136 | strength_final=strong | claim_tag=multipath_nlos_impulse_response | context-verified=YES
- O_ISAC_039 | # 2 VISIBLE LIGHT INTEGRATED POSITIONING AND COMMUNICATION FRAMEWORK > ## 2.1 System Model of Indoor Visible Light Positioning and Communication | L67-L71 | strength_final=strong | claim_tag=multipath_nlos_impulse_response | context-verified=YES
- O_ISAC_044 | #### I. INTRODUCTION | L41-L41 | strength_final=strong | claim_tag=phase_noise_freq_offset | context-verified=YES
- O_ISAC_077 | ### III. PHOTONIC THZ ISAC LINK > #### A. Experimental Setup | L58-L58 | strength_final=strong | claim_tag=phase_noise_freq_offset | context-verified=YES

Claims weakened/removed due to missing/ambiguous evidence:
- Avoided claims about specific turbulence distributions adopted by representative works; treated lognormal/Gamma-Gamma as theory-standard options.
- Avoided any plane-conversion statements (OSNR->SNR) and any prevalence language.

Corrections to evidence labels (strength/claim_tag):
- O_ISAC_035: reclassified from patch-notes claim_tag=multipath_nlos to claim_tag=attenuation_beer_lambert based on explicit "exponential Beers-Lambert Law" statement (context-verified).
- O_ISAC_034: patch-notes locator pointed to L92; corrected to L205 where Beer-Lambert Law is explicitly stated (context-verified).


## review_package/section_02C_audit.md

﻿### II-C Writing Recipe Audit (Not for manuscript)
R-1 Structure compliance: PASS - Headings match template (C, C.1, C.2, C.3) and end with Lesson (C).
R-2 Hardware coverage: PASS - Transmitter chain (sources/modulators) addressed; receiver chain (coherent vs IM/DD) addressed; spatial/beamforming enablers addressed; fiber sensing granularity noted via Delta z without conflating with Delta r_min.
R-3 Metric governance compliance: PASS - pi(metric) mapping stated; OSNR vs electrical SNR separation stated; no OSNR->SNR conversion implied; no forbidden tokens introduced.
R-4 Evidence compliance: PASS - All literature-usage claims anchored; plane-separation claims use >=2 strong anchors per plane; context verification logged per anchor.
R-5 Section I stylistic alignment: PASS - Citation style [O_ISAC_XXX] and tone consistent with Section I/II-A/II-B.

Resolved input paths used:
- drafts/section_01_introduction.md
- reference_compendium/s02_fund_tpl.md (resolved from missing drafts/section_02_fundamentals_template.md)
- drafts/section_02_methodology.md
- drafts/section_02_fundamentals_draft.md
- drafts/section_02A_fundamentals.md
- analysis/II_met_gov.md
- analysis/II_ev_v2/patch_notes_for_writing.md
- analysis/II_ev_v2/section2C_evidence_LLM.csv
- analysis/II_ev_v2/Transceiver_Hardware_Governance_Lab.ipynb
- analysis/II_sch_map.md (not used)

Evidence anchors used (deduplicated):
- O_ISAC_029 | # THz Integrated Sensing and Communication With Full-Photonic Direct LFM Reception and De-Chirping for D-Band Fiber-Wireless Network > ### <span id="page-2-2"></span>II. PRINCIPLE | L100-L100 | strength_final=strong | plane_final=OPTICAL_PLANE | context-verified=YES
- O_ISAC_001 | # Modulation Strategies for Robust Optical Wireless Communications and Sensing in 6G > #### II. VLC SYSTEM EMPLOYING CE-OFDM > #### A. VLC CE-OFDM Transmitter | L70-L70 | strength_final=strong | plane_final=OPTICAL_PLANE | context-verified=YES
- O_ISAC_028 | # Performance Improvement for Symmetric Carrierassisted Differential Detection Receiver by Pairwise Coding | L11-L11 | strength_final=strong | plane_final=OPTICAL_PLANE | context-verified=YES
- O_ISAC_029 | # THz Integrated Sensing and Communication With Full-Photonic Direct LFM Reception and De-Chirping for D-Band Fiber-Wireless Network > ## <span id="page-0-1"></span>I. INTRODUCTION | L47-L47 | strength_final=strong | plane_final=OPTICAL_PLANE | context-verified=YES
- O_ISAC_061 | # *A. Convergence of BCD Algorithm* > #### *B. Optimal Beampattern and C&S Tradeoff* > #### <span id="page-11-3"></span>*C. Practical C&S Performance Metrics* | L638-L642 | strength_final=strong | plane_final=ELECTRICAL_PLANE | context-verified=YES
- O_ISAC_023 | # Free-Space Optical Integrated Sensing and Communication Based on DCO-OFDM: Performance Metrics and Resource Allocation > ## *C. Computational Complexity and Scalability* > ### <span id="page-11-1"></span><span id="page-11-0"></span>D. Robustness to Channel Variations | L751-L755 | strength_final=strong | plane_final=ELECTRICAL_PLANE | context-verified=YES
- O_ISAC_029 | # THz Integrated Sensing and Communication With Full-Photonic Direct LFM Reception and De-Chirping for D-Band Fiber-Wireless Network > ### <span id="page-2-2"></span>II. PRINCIPLE | L157-L157 | strength_final=strong | plane_final=ELECTRICAL_PLANE | context-verified=YES
- O_ISAC_001 | # Modulation Strategies for Robust Optical Wireless Communications and Sensing in 6G > ## B. VLC CE-OFDM Receiver | L74-L74 | strength_final=strong | plane_final=ELECTRICAL_PLANE | context-verified=YES

Claims weakened/removed due to missing/ambiguous evidence:
- No paper-specific adoption claims for OPA/optical RIS/metasurfaces; treated as theory-standard enablers only.

Corrections to evidence labels (strength/plane):
- O_ISAC_029 (L47) uses the phrase "optical signal-to-noise ratio (SNR)" rather than the OSNR acronym; retained as OPTICAL_PLANE with strength_final=strong due to explicit optical-plane wording.


## review_package/section_02D_audit.md

﻿### II-D Writing Recipe Audit (Not for manuscript)
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


## review_package/section_02E_writing_audit.md

### II-E Writing Recipe Audit (Not for manuscript)
R-1 Structure compliance: PASS
R-2 Governance compliance (metric + tradeoff): PASS
R-3 Evidence compliance (every literature claim anchored): PASS
R-4 Context verification coverage (anchors with context_verified=YES): PASS
R-5 Style alignment with Section I: PASS

Evidence anchors used (deduplicated list)
- O_ISAC_048 | # I. INTRODUCTION > ## C. Clipping Noise Statistics > #### III. OPTIMAL POWER ALLOCATION FOR DCO-OFDM | L124-L132 | strength_final=strong | context_verified=YES
- O_ISAC_023 | # Free-Space Optical Integrated Sensing and Communication Based on DCO-OFDM: Performance Metrics and Resource Allocation | L5-L5 | strength_final=strong | context_verified=YES
- O_ISAC_005 | # III. PROBLEM FORMULATION AND RESOURCE ALLOCATION > #### A. Problem Formulation | L116-L122 | strength_final=strong | context_verified=YES
- O_ISAC_005 | # III. PROBLEM FORMULATION AND RESOURCE ALLOCATION > #### B. Resource Optimization using Reinforcement Learning | L134-L136 | strength_final=strong | context_verified=YES
- O_ISAC_005 | # Integrated Sensing and Communication for UAV Trajectory Optimization in Mixed FSO-RF Networks in Dynamic Weather Conditions | L5-L5 | strength_final=strong | context_verified=YES
- O_ISAC_002 | # **2. Photonic THz ISAC Waveform Design** | L17-L17 | strength_final=strong | context_verified=YES
- O_ISAC_001 | # Modulation Strategies for Robust Optical Wireless Communications and Sensing in 6G > ## B. VLC CE-OFDM Receiver > ### III. VLC CE-OFDM PERFORMANCE ASSESSMENT | L97-L97 | strength_final=strong | context_verified=YES
- O_ISAC_004 | # Adiabatic-tapered few-mode-fiber-based system for integrating optical fiber sensing and telecommunication > ### I. INTRODUCTION | L13-L13 | strength_final=strong | context_verified=YES
- O_ISAC_019 | # Full-duplex Integrated Sensing and Communication System Based on Microwave Photonics | L31-L31 | strength_final=strong | context_verified=YES

Corrections to evidence labels (if any)
- None. LLM CSV labels were treated as candidate-only; strength_final assigned after context verification.

Claims weakened/removed (if any)
- None.

Resolved paths used for inputs
- drafts/section_01_introduction.md
- drafts/section_02_methodology.md
- review_package/section_02_fundamentals_template.md (drafts/section_02_fundamentals_template.md not found)
- drafts/section_02_fundamentals_draft.md (patched only in Section II-E)
- analysis/II_met_gov.md
- analysis/II_trade_gov_2E.md
- analysis/II_sch_map.md (not required for drafting)
- analysis/II_ev_v2/patch_notes_for_writing_2E.md
- analysis/II_ev_v2/section2E_evidence_LLM.csv (primary candidate list)
- data/proc_markdowns/O_ISAC_048/O_ISAC_048.md
- data/proc_markdowns/O_ISAC_023/O_ISAC_023.md
- data/proc_markdowns/O_ISAC_005/O_ISAC_005.md
- data/proc_markdowns/O_ISAC_002/O_ISAC_002.md
- data/proc_markdowns/O_ISAC_001/O_ISAC_001.md
- data/proc_markdowns/O_ISAC_004/O_ISAC_004.md
- data/proc_markdowns/O_ISAC_019/O_ISAC_019.md

Evidence source note
- analysis/II_ev_v2/section2E_evidence.csv not found; anchors were selected from section2E_evidence_LLM.csv and verified directly in the markdown corpus with ?15-line context checks.

