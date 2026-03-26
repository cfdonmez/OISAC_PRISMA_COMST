### II-B Writing Recipe Audit (Not for manuscript)
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
