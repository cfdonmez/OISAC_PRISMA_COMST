### II-C Writing Recipe Audit (Not for manuscript)
R-1 Structure compliance: PASS - Headings match template (C, C.1, C.2, C.3) and end with Lesson (C).
R-2 Hardware coverage: PASS - Transmitter chain (sources/modulators) addressed; receiver chain (coherent vs IM/DD) addressed; spatial/beamforming enablers addressed; fiber sensing granularity noted via Delta z without conflating with Delta r_min.
R-3 Metric governance compliance: PASS - pi(metric) mapping stated; OSNR vs electrical SNR separation stated; no OSNR->SNR conversion implied; no forbidden tokens introduced.
R-4 Evidence compliance: PASS - All literature-usage claims anchored; plane-separation claims use >=2 strong anchors per plane; context verification logged per anchor.
R-5 Section I stylistic alignment: PASS - Citation style [O_ISAC_XXX] and tone consistent with Section I/II-A/II-B.

Resolved input paths used:
- drafts/section_01_introduction.md
- reference_compendium/section_02_fundamentals_template.md (resolved from missing drafts/section_02_fundamentals_template.md)
- drafts/section_02_methodology.md
- drafts/section_02_fundamentals_draft.md
- drafts/section_02A_fundamentals.md
- analysis/II_metric_governance.md
- analysis/II_evidence_v2/patch_notes_for_writing.md
- analysis/II_evidence_v2/section2C_evidence_LLM.csv
- analysis/II_evidence_v2/Transceiver_Hardware_Governance_Lab.ipynb
- analysis/II_schema_map.md (not used)

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
