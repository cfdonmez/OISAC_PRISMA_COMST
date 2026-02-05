# II. TECHNICAL FUNDAMENTALS OF O-ISAC

## A. Unified O-ISAC System Model and Integration Paradigms

### A.1 Canonical Joint Waveform/Resource Model
Design rationale: We define a joint design variable set that spans waveform parameters (bandwidth, chirp rate, pilot structure, coding), optical front-end parameters (source, modulation, detection), and sensing-task parameters (range/angle/velocity versus fiber spatial granularity). This compact variable set supports cross-modality comparisons without erasing the physical constraints that distinguish coherent and IM/DD architectures.

**Generic baseband observation (complex coherent model):**
\[
\mathbf{y}(t)=\mathbf{H}(t;\boldsymbol{\theta})\mathbf{s}(t)+\mathbf{w}(t),
\]
where \(\mathbf{y}(t)\) is the received complex baseband observation, \(\mathbf{s}(t)\) is the transmitted complex baseband waveform, \(\mathbf{H}(t;\boldsymbol{\theta})\) is a parametric operator embedding sensing parameters \(\boldsymbol{\theta}\) (e.g., delay, Doppler, angle), and \(\mathbf{w}(t)\) is receiver noise.

**IM/DD observation (real, nonnegative intensity constraint):**
\[
y(t)=\mathcal{R}\,\big(x(t)\ast h(t)\big)+n(t),\qquad x(t)\ge 0,
\]
where \(y(t)\) is the electrical observation after direct detection, \(x(t)\) is the transmitted optical intensity waveform, \(h(t)\) is the intensity channel impulse response, \(\mathcal{R}\) is photodetector responsivity, and \(n(t)\) is additive electrical noise. Here \(x(t)\) denotes the modulated optical intensity (post square-law abstraction), not the optical field amplitude; the nonnegativity constraint follows.

**Measurement-plane contract.** We map each reported metric \(m\) to a measurement plane via
\[
\pi(m)\in\{\text{OPTICAL\_PLANE},\;\text{ELECTRICAL\_PLANE},\;\text{AMBIGUOUS}\},
\]
where OPTICAL\_PLANE refers to pre-detection optical field/power (\(E(t)\), \(P(t)=|E(t)|^2\ge 0\)) and ELECTRICAL\_PLANE refers to post-detection electrical baseband observations. OSNR and electrical SNR must be reported on their native planes, and OSNR-to-SNR conversion is prohibited unless a source provides an explicit receiver model (Metric Governance). Generic "SNR" without an optical/electrical cue remains AMBIGUOUS and is not used to justify plane separation (Metric Governance). For ranging tasks, the delay-to-range relation \(\tau=2r/v\) underpins \(\Delta r_{\min}=v/(2B_{\text{eff}})\), whereas fiber DAS reports spatial granularity via \(\Delta z\) (gauge/segment length) rather than \(\Delta r_{\min}\) (Metric Governance).

Evidence alignment: Representative works explicitly report OSNR in the optical plane (e.g., "optical signal-to-noise ratio (O-SNR)/(OSNR)") [O_ISAC_056], [O_ISAC_080]. <!-- evidence: ⟦O_ISAC_056 | # Optical ISAC: Fundamental Performance Limits and Transceiver Design | L7-L11 | strength_final=strong | plane_final=OPTICAL_PLANE⟧; ⟦O_ISAC_080 | # Integrated Communication and In-band Spectrum Polarization-Based Sensing via Fraction-Division Non-Orthogonal Multiple Access | L5-L9 | strength_final=strong | plane_final=OPTICAL_PLANE⟧ -->
Electrical SNR is explicitly reported as a post-detection (electrical) quantity for communication performance [O_ISAC_061], [O_ISAC_023]. <!-- evidence: ⟦O_ISAC_061 | # *A. Convergence of BCD Algorithm* > #### *B. Optimal Beampattern and C&S Tradeoff* > #### <span id="page-11-3"></span>*C. Practical C&S Performance Metrics* | L638-L642 | strength_final=strong | plane_final=ELECTRICAL_PLANE⟧; ⟦O_ISAC_023 | # Free-Space Optical Integrated Sensing and Communication Based on DCO-OFDM: Performance Metrics and Resource Allocation > ## *C. Computational Complexity and Scalability* > ### <span id="page-11-1"></span><span id="page-11-0"></span>D. Robustness to Channel Variations | L751-L755 | strength_final=strong | plane_final=ELECTRICAL_PLANE⟧ -->

### A.2 Integration Paradigms (Communication-centric / Sensing-centric / Joint Design)
Design rationale: To avoid modality-locked taxonomies, we classify integration by mechanisms: shared waveform, shared hardware, shared time/frequency resources, and shared processing. This mechanism-first view aligns heterogeneous implementations under a single abstraction while keeping the physical constraints of each modality intact.

**Communication-centric:** The primary objective is communication performance while sensing is constrained to operate within communication-driven resource limits. A minimal objective-form exemplar is: maximize \(R\) subject to \(J_{\text{sense}}(\boldsymbol{\theta})\le \varepsilon\).

**Sensing-centric:** The primary objective is sensing fidelity while communication is constrained to meet a minimum service level. A minimal objective-form exemplar is: minimize \(J_{\text{sense}}(\boldsymbol{\theta})\) subject to \(R\ge R_0\) (and/or BER \(\le \beta\)).

**Joint design:** Communication and sensing are co-optimized via explicit multi-objective trade-offs with an operating-point interpretation. A minimal objective-form exemplar is: minimize \([J_{\text{sense}}(\boldsymbol{\theta}),\; -R]\) (Pareto) or minimize \(\alpha J_{\text{sense}}(\boldsymbol{\theta})-(1-\alpha)R\), where \(R\) denotes throughput and \(J_{\text{sense}}\) denotes a sensing loss (e.g., estimation MSE or a ranging-error proxy).

Paradigm-to-mechanism bridge:
- Communication-centric -> shared processing / shared resources -> sensing piggybacks on communication signaling.
- Sensing-centric -> shared waveform / shared hardware -> communication is embedded under sensing-driven constraints.
- Joint design -> shared waveform + shared processing -> explicit co-optimization couples both objectives.

We define an integration depth variable
\[
d_{\text{int}}\in\{0,\;1/2,\;1\},
\]
where \(d_{\text{int}}=0\) corresponds to coexistence, \(d_{\text{int}}=1/2\) to partial sharing/cooperation, and \(d_{\text{int}}=1\) to full co-design. This abstraction provides the axis used later to align taxonomy and trade-off synthesis without rewriting modality-specific models.

Evidence alignment: A.2 introduces a survey-internal taxonomy for organizing later sections; no paper-specific performance claims are asserted here, and thus no additional evidence anchors are required.

**Lesson (A):** A unified system model combined with explicit measurement-plane mapping is necessary to make later taxonomy and trade-off statements falsifiable rather than narrative.
