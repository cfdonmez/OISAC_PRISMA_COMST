## C. Transceiver and Hardware Abstractions (What is Common, What is Modality-Specific)

### C.1 Sources and Modulators
Design rationale: Transceiver abstraction begins at the optical source and modulation interface, because these elements determine whether the system operates coherently or under IM/DD constraints and set the effective bandwidth and waveform interface used by sensing/communication co-design. A compact source–modulator view also supports cross-modality comparison without over-committing to device-specific implementations.

Evidence alignment: Representative photonic-THz hardware chains explicitly modulate external cavity laser (ECL) light using an IQ modulator composed of MZMs, reflecting a coherent source–modulator stack [O_ISAC_029]. <!-- evidence: ⟦O_ISAC_029 | # THz Integrated Sensing and Communication With Full-Photonic Direct LFM Reception and De-Chirping for D-Band Fiber-Wireless Network > ### <span id="page-2-2"></span>II. PRINCIPLE | L100-L100 | strength_final=strong | plane_final=OPTICAL_PLANE | context-verified=YES⟧ -->
In contrast, IM/DD-oriented VLC transmitter chains can be realized by adding a DC bias to an electrical waveform and using it to modulate a laser diode (LD), which enforces a nonnegative optical intensity interface [O_ISAC_001]. <!-- evidence: ⟦O_ISAC_001 | # Modulation Strategies for Robust Optical Wireless Communications and Sensing in 6G > #### II. VLC SYSTEM EMPLOYING CE-OFDM > #### A. VLC CE-OFDM Transmitter | L70-L70 | strength_final=strong | plane_final=OPTICAL_PLANE | context-verified=YES⟧ -->

### C.2 Receivers and Detection
Design rationale: Receiver architecture determines the measurement plane and, therefore, which signal-quality metrics are meaningful. Coherent receivers with an optical LO recover complex field information, whereas IM/DD receivers implement square-law detection and operate on optical intensity, mapping observations to the electrical plane.

We restate the measurement-plane contract for receiver design: 
\[
\pi(m)\in\{\text{OPTICAL\_PLANE},\;\text{ELECTRICAL\_PLANE},\;\text{AMBIGUOUS}\},
\]
where OSNR is an optical-plane metric and electrical SNR/ESNR is a post-detection electrical-plane metric; OSNR-to-SNR conversion is prohibited without an explicit receiver model, and generic “SNR” without plane cues remains AMBIGUOUS (Metric Governance). At the receiver interface, ranging metrics reflect bandwidth-limited sensing tasks via \(\Delta r_{\min}=v/(2B_{\text{eff}})\), whereas fiber systems report spatial granularity via \(\Delta z\) (gauge/segment length), not \(\Delta r_{\min}\) (Metric Governance).

Evidence alignment: Representative optical-plane reporting explicitly uses OSNR (optical signal-to-noise ratio) [O_ISAC_028], [O_ISAC_029]. <!-- evidence: ⟦O_ISAC_028 | # Performance Improvement for Symmetric Carrierassisted Differential Detection Receiver by Pairwise Coding | L11-L11 | strength_final=strong | plane_final=OPTICAL_PLANE | context-verified=YES⟧; ⟦O_ISAC_029 | # THz Integrated Sensing and Communication With Full-Photonic Direct LFM Reception and De-Chirping for D-Band Fiber-Wireless Network > ## <span id="page-0-1"></span>I. INTRODUCTION | L47-L47 | strength_final=strong | plane_final=OPTICAL_PLANE | context-verified=YES⟧ -->
Electrical SNR is explicitly reported in post-detection performance analysis [O_ISAC_061], [O_ISAC_023], consistent with the electrical-plane interpretation of IM/DD receivers. <!-- evidence: ⟦O_ISAC_061 | # *A. Convergence of BCD Algorithm* > #### *B. Optimal Beampattern and C&S Tradeoff* > #### <span id="page-11-3"></span>*C. Practical C&S Performance Metrics* | L638-L642 | strength_final=strong | plane_final=ELECTRICAL_PLANE | context-verified=YES⟧; ⟦O_ISAC_023 | # Free-Space Optical Integrated Sensing and Communication Based on DCO-OFDM: Performance Metrics and Resource Allocation > ## *C. Computational Complexity and Scalability* > ### <span id="page-11-1"></span><span id="page-11-0"></span>D. Robustness to Channel Variations | L751-L755 | strength_final=strong | plane_final=ELECTRICAL_PLANE | context-verified=YES⟧ -->
Hardware-level receiver implementations in photonic-THz systems explicitly describe PD/BPD-based O/E conversion after photonic down-conversion [O_ISAC_029], while VLC receivers detect optical signals with a photodiode and convert them to electrical waveforms [O_ISAC_001]. <!-- evidence: ⟦O_ISAC_029 | # THz Integrated Sensing and Communication With Full-Photonic Direct LFM Reception and De-Chirping for D-Band Fiber-Wireless Network > ### <span id="page-2-2"></span>II. PRINCIPLE | L157-L157 | strength_final=strong | plane_final=ELECTRICAL_PLANE | context-verified=YES⟧; ⟦O_ISAC_001 | # Modulation Strategies for Robust Optical Wireless Communications and Sensing in 6G > ## B. VLC CE-OFDM Receiver | L74-L74 | strength_final=strong | plane_final=ELECTRICAL_PLANE | context-verified=YES⟧ -->

### C.3 Beamforming/Wavefront Control Enablers
Design rationale: Spatial control elements (e.g., OPA, optical RIS/metasurfaces, and integrated photonics) are treated as front-end enablers that shape beam directionality and angular sensitivity while remaining compatible with the source–modulator–channel–detector abstraction. A generic array response for angle sensing/beam steering can be written as
\[
\mathbf{a}(\phi)=\left[1,\;e^{j k d \sin\phi},\;\ldots,\;e^{j k d (N-1)\sin\phi}\right]^{\top}.
\]

Evidence alignment: This subsection provides theory-standard enabler abstractions; the current II-C evidence layer does not include dedicated, context-verified anchors for OPA/optical-RIS usage, so no paper-specific adoption claims are asserted here.

**Lesson (C):** Hardware commonality exists at the abstraction level (source–modulator–channel–detector), not at the implementation level.
