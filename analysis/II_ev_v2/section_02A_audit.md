### II-A Writing Recipe Audit (Not for manuscript)
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
