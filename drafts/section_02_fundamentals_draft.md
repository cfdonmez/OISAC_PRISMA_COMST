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

---

﻿## B. Propagation and Channel Models Across Modalities
This subsection abstracts each modality's propagation as an operator/channel mapping consistent with the observation models in Section II-A, while emphasizing that dominant impairments differ across media. The measurement-plane contract remains binding: channel modeling does not justify OSNR-to-SNR conversion, and plane separation is preserved throughout (Metric Governance).

### B.1 Fiber Channel (Guided Medium)
Design rationale: A guided fiber link is well captured by a linear dispersive baseband model for coherent communication, with a nonlinear wave equation as a conceptual extension when power or length scales demand it. This separation provides a minimal, modality-consistent abstraction while allowing later sections to specialize the impairment regime.

A linear dispersive baseline is
\[
\mathbf{y}(t)=\mathbf{G}_{\text{disp}}(t)\ast \mathbf{s}(t)+\mathbf{w}(t),
\]
where \(\mathbf{s}(t)\) is the transmitted baseband signal, \(\mathbf{G}_{\text{disp}}(t)\) is the dispersive impulse response, and \(\mathbf{w}(t)\) is additive noise. As a conceptual extension, the nonlinear Schrodinger equation (NLSE) captures loss, dispersion, and Kerr nonlinearity:
\[
\frac{\partial A(z,t)}{\partial z}= -\frac{\alpha}{2}A - j\frac{\beta_2}{2}\frac{\partial^2 A}{\partial t^2} + j\gamma|A|^2A + \eta(z,t),
\]
where \(A(z,t)\) is the optical field envelope, \(\alpha\) is attenuation, \(\beta_2\) is group-velocity dispersion, and \(\gamma\) is the nonlinear coefficient. For sensing, the effective channel is the distributed backscatter/impulse response along the fiber, whereas the communication view typically emphasizes the forward transmission path. Fiber sensing spatial granularity is reported as \(\Delta z\) (gauge/segment length), not \(\Delta r_{\min}\) (Metric Governance).

Evidence alignment: This subsection presents theory-standard channel abstractions and does not assert paper-specific modeling choices; hence no evidence anchors are invoked here.

### B.2 FSO Channel (Atmosphere + Pointing)
Design rationale: Free-space optical channels are dominated by multiplicative impairments (turbulence and pointing) and path attenuation, which are naturally expressed in an IM/DD-friendly intensity model. This abstraction keeps the optical nonnegativity constraint explicit while isolating the dominant propagation factors.

A compact IM/DD-friendly form is
\[
y = h_{\text{turb}}\,h_{\text{point}}\,x + n,\qquad x\ge 0,
\]
where \(x\) is the transmitted optical intensity, \(h_{\text{turb}}\) captures turbulence-induced fading, \(h_{\text{point}}\) captures pointing/misalignment loss, and \(n\) is additive noise. A standard attenuation factor is the Beer-Lambert law,
\[
h_{\text{att}}=\exp(-\kappa d),
\]
with \(\kappa\) as the extinction coefficient and \(d\) the propagation distance. Turbulence statistics are commonly represented by lognormal or Gamma-Gamma distributions as theory-standard options.

Evidence alignment: Representative FSO works compute atmospheric loss using Beer-Lambert attenuation in their channel modeling and simulation setup [O_ISAC_035], [O_ISAC_034]. <!-- evidence: ⟦O_ISAC_035 | ### II. SYSTEM MODEL AND METHODOLOGY > # B. FSO Channel | L75-L79 | strength_final=strong | claim_tag=attenuation_beer_lambert | context-verified=YES⟧; ⟦O_ISAC_034 | # IV. NUMERICAL RESULTS | L205-L205 | strength_final=strong | claim_tag=attenuation_beer_lambert | context-verified=YES⟧ -->

### B.3 VLC Channel (Lambertian + Multipath + Ambient Light)
Design rationale: VLC channels are geometry-driven and are naturally modeled by Lambertian emission with an intensity impulse response that captures both direct and reflected paths. This abstraction preserves IM/DD constraints while enabling later sections to compare sensing and communication performance under common channel primitives.

A compact representation uses an intensity impulse response \(h(t)\) with a Lambertian DC gain for the LoS path, while NLoS reflections are captured by additional impulse-response components. Multipath/NLoS effects are thus expressed through \(h(t)\) rather than an equivalent complex baseband model. Shot noise, thermal noise, and ambient-light-induced noise are standard components in VLC receiver models.

Evidence alignment: Representative VLC/OWC works model the channel impulse response as a sum of LOS and NLOS components, explicitly framing multipath via LoS/NLoS impulse-response components [O_ISAC_022], [O_ISAC_039]. <!-- evidence: ⟦O_ISAC_022 | ## <span id="page-3-0"></span>D. The Optical Wireless Channel | L136-L136 | strength_final=strong | claim_tag=multipath_nlos_impulse_response | context-verified=YES⟧; ⟦O_ISAC_039 | # 2 VISIBLE LIGHT INTEGRATED POSITIONING AND COMMUNICATION FRAMEWORK > ## 2.1 System Model of Indoor Visible Light Positioning and Communication | L67-L71 | strength_final=strong | claim_tag=multipath_nlos_impulse_response | context-verified=YES⟧ -->

### B.4 Photonic-THz Bridging (Optical Generation/Distribution + THz Propagation)
Design rationale: Photonic-THz links are hybrid by construction: optical carriers are used for signal generation, distribution, and local-oscillator delivery, while the wireless propagation occurs in the THz band. A split-channel abstraction therefore cleanly separates optical-domain impairments from THz wireless propagation effects.

We treat the link as an optical generation/distribution stage feeding a THz wireless channel, which enables consistent modeling of end-to-end performance without conflating measurement planes. In representative photonic-THz links, laser-induced phase noise and frequency offset are treated as dominant impairments that shape performance and system design choices.

Evidence alignment: Photonic-THz works explicitly discuss laser-induced phase noise and frequency-offset effects in their experimental or system-performance analyses [O_ISAC_044], [O_ISAC_077]. <!-- evidence: ⟦O_ISAC_044 | #### I. INTRODUCTION | L41-L41 | strength_final=strong | claim_tag=phase_noise_freq_offset | context-verified=YES⟧; ⟦O_ISAC_077 | ### III. PHOTONIC THZ ISAC LINK > #### A. Experimental Setup | L58-L58 | strength_final=strong | claim_tag=phase_noise_freq_offset | context-verified=YES⟧ -->

**Lesson (B):** Channel models differ in dominant impairments, but the reporting contract and measurement-plane separation remain invariant across modalities.

---

﻿## C. Transceiver and Hardware Abstractions (What is Common, What is Modality-Specific)

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

---

﻿## D. Sensing Principles and the Metric Contract (Resolution vs Accuracy vs Bounds)
Design rationale: Section II-D establishes the minimal, modality-agnostic metric contract needed to compare sensing performance across O-ISAC systems without aliasing “resolution” and “accuracy.” The intent is to separate physics-limited resolution, estimator-dependent accuracy, and bounds so that later taxonomy and trade-off synthesis remain defensible.

### D.1 Ranging/ToF/FMCW/LFM Fundamentals
Design rationale: A two-way ranging convention provides a common physical baseline for ToF/FMCW/LFM systems and anchors all subsequent resolution metrics to bandwidth rather than estimator choice.

We adopt a two-way ranging convention with round-trip delay. The bandwidth-limited two-way range resolution is
\[
\Delta r_{\min} := \frac{v}{2B_{\text{eff}}},
\]
with \(v=c\) in free space and \(v\approx c/n_g\) in guided media. Here \(B_{\text{eff}}\) denotes the effective bandwidth of the sensing waveform as seen through the receiver processing chain. A compact bridge holds for ranging tasks: \(\tau=2r/v\) links time delay to \(\Delta r_{\min}\), whereas fiber DAS reports spatial granularity via \(\Delta z\) (gauge/segment length), not \(\Delta r_{\min}\) (Metric Governance).

Evidence alignment: Representative photonic ranging works explicitly express bandwidth-limited resolution in the form \(c/2B\), consistent with \(\Delta r_{\min}=v/(2B_{\text{eff}})\) under the two-way convention [O_ISAC_026], [O_ISAC_034]. <!-- evidence: ⟦O_ISAC_026 | Jianyang Shi > I. INTRODUCTION | L74-L84 | strength_final=strong | meaning_final=bandwidth_limited_range_resolution | context_verified=YES⟧; ⟦O_ISAC_034 | <span id="page-0-1"></span>I. INTRODUCTION > <span id="page-1-3"></span>*B. Signal Structure* > B. Sensing Metrics | L145-L155 | strength_final=strong | meaning_final=bandwidth_limited_range_resolution | context_verified=YES⟧ -->

### D.2 Accuracy (Estimator-Dependent) and CRB/FIM Bounds
Design rationale: Accuracy depends on the estimator and noise model, so it must be separated from physics-limited resolution. A canonical CRB exemplar provides a theory-standard lower bound without assuming a specific measurement plane.

Estimator-dependent accuracy is defined by the RMSE
\[
\sigma_r := \sqrt{\mathbb{E}\big[(\hat r-r)^2\big]}.
\]
A canonical CRB form for delay estimation is
\[
\mathrm{var}(\hat\tau) \ge \frac{1}{8\pi^2\beta^2\,\mathrm{SNR}} \quad \Rightarrow \quad \mathrm{var}(\hat r) \ge \left(\frac{v}{2}\right)^2 \mathrm{var}(\hat\tau),
\]
where \(\beta\) is the RMS bandwidth. The SNR in this bound is a theory-standard abstract SNR unless a specific plane is explicitly defined by a source.

Evidence alignment: This subsection introduces theory-standard definitions and does not assert literature-specific usage; hence no evidence anchors are invoked here.

### D.3 Fiber Spatial Granularity (\(\Delta z\)) vs Wireless Range Resolution (\(\Delta r_{\min}\))
Design rationale: Fiber sensing resolves spatial granularity along the fiber, whereas wireless ranging resolves time-of-flight. Treating these as interchangeable destroys comparability across modalities.

We explicitly separate the two: \(\Delta z\) denotes the minimum resolvable segment/gauge length in DAS/OTDR-type fiber sensing, while \(\Delta r_{\min}\) is the bandwidth-limited range resolution for ToF/FMCW-style tasks. **Comparability warning:** \(\Delta z\) must not be substituted into \(\mathrm{CRQ}_\Delta\); only \(\Delta r_{\min}\) is admissible.

Evidence alignment: Representative fiber sensing works report spatial resolution along the fiber (gauge/segment length) in meters, which aligns with \(\Delta z\) rather than \(\Delta r_{\min}\) [O_ISAC_006], [O_ISAC_013]. <!-- evidence: ⟦O_ISAC_006 | *A. Solution based on multiplexing technology* | L79-L95 | strength_final=strong | meaning_final=delta_z_spatial_granularity | context_verified=YES⟧; ⟦O_ISAC_013 | Single-Ended > 100-km Distributed Vibration Sensor Based on OFDR Using Pearson Correlation Coefficient | L3-L19 | strength_final=strong | meaning_final=delta_z_spatial_granularity | context_verified=YES⟧ -->

### D.4 Capacity–Resolution Quotient
Design rationale: A compact scalar measure is needed to compare joint communication–sensing operating points without collapsing non-isomorphic metrics. The contract therefore defines a single admissible quotient based on \(\Delta r_{\min}\).

We define the capacity–resolution quotient as
\[
\mathrm{CRQ}_{\Delta} := \frac{R}{\Delta r_{\min}} \quad [\mathrm{bps/m}].
\]
Comparisons are only valid on the subset where \(\Delta r_{\min}\) exists and is defensible; \(\Delta z\) is not a proxy. This contract enables cross-architecture Pareto analysis in Sections IV–V without metric aliasing.

Evidence alignment: This subsection specifies a governance-level construct; no literature-usage claims are asserted.

**Lesson (D):** Without explicit separation of \(\Delta r_{\min}\), \(\sigma_r\)/CRB, and \(\Delta z\), “resolution” becomes non-isomorphic and cross-study comparability collapses.

---

## E. ISAC Coupling and Trade-off Foundations (Optimization View)

### E.1 Multiobjective Formulation
Design rationale. We cast O-ISAC co-design as a multiobjective program over a shared design vector $\mathbf{x}$ that collects waveform/resource parameters, optical front-end knobs, sensing-task parameters, and processing knobs, so that communication performance and sensing fidelity are optimized on the same degrees of freedom. Let $f_c(\mathbf{x})$ denote a communication objective (e.g., rate/BER/outage) and $f_s(\mathbf{x})$ denote a sensing objective (e.g., resolution/accuracy/bound), with feasibility $\mathbf{x}\in\mathcal{X}$ capturing nonnegativity, power/bandwidth, and hardware limits. A point $\mathbf{x}^*$ is Pareto-optimal if no other feasible design improves one objective without degrading the other; scalarizations such as $\max_{\mathbf{x}\in\mathcal{X}} f_c(\mathbf{x})-\lambda f_s(\mathbf{x})$ provide convenient operating points but do not exhaust the Pareto set.

Evidence alignment. Representative FSO O-ISAC works explicitly maximize spectral efficiency subject to sensing-precision (Fisher-information) constraints via power allocation, yielding a constrained trade-off formulation. [O_ISAC_048] <!-- evidence: ⟦O_ISAC_048 | # I. INTRODUCTION > ## C. Clipping Noise Statistics > #### III. OPTIMAL POWER ALLOCATION FOR DCO-OFDM | L124-L132 | strength_final=strong | context_verified=YES⟧ -->
Other works formulate joint power-allocation problems for communication-centric and sensing-centric scenarios and solve them with block-coordinate-descent algorithms, explicitly positioning the comm-sensing trade-off within the optimization. [O_ISAC_023] <!-- evidence: ⟦O_ISAC_023 | # Free-Space Optical Integrated Sensing and Communication Based on DCO-OFDM: Performance Metrics and Resource Allocation | L5-L5 | strength_final=strong | context_verified=YES⟧ -->

### E.2 Coupling Mechanisms by Modality
Design rationale. Coupling is most stable when categorized by mechanism rather than modality: resource coupling (power/bandwidth/time), waveform coupling (shared modulation and signaling), hardware coupling (shared optical/electrical front-ends), algorithmic coupling (joint inference/control), and propagation/environment coupling (shared impairments). These mechanisms manifest differently across modalities (e.g., IM/DD nonnegativity, coherent phase access, fiber probe interactions, turbulence/ambient light), but the coupling logic is invariant.

Evidence alignment. In UAV-aided mixed FSO-RF O-ISAC, end-to-end throughput is optimized under FSO backhaul capacity while jointly tuning antenna beamwidth and bandwidth, illustrating explicit resource coupling. [O_ISAC_005] <!-- evidence: ⟦O_ISAC_005 | # III. PROBLEM FORMULATION AND RESOURCE ALLOCATION > #### A. Problem Formulation | L116-L122 | strength_final=strong | context_verified=YES⟧ -->
In DCO-OFDM FSO-ISAC, power allocation is optimized to maximize spectral efficiency subject to Fisher-information constraints, providing a second resource-coupling exemplar. [O_ISAC_048] <!-- evidence: ⟦O_ISAC_048 | # I. INTRODUCTION > ## C. Clipping Noise Statistics > #### III. OPTIMAL POWER ALLOCATION FOR DCO-OFDM | L124-L132 | strength_final=strong | context_verified=YES⟧ -->
Photonic THz O-ISAC explicitly notes that waveform modulation, transmit power, and bandwidth must balance sensing and communication requirements, making waveform design intrinsically coupled. [O_ISAC_002] <!-- evidence: ⟦O_ISAC_002 | # **2. Photonic THz ISAC Waveform Design** | L17-L17 | strength_final=strong | context_verified=YES⟧ -->
VLC CE-OFDM experiments report a trade-off between modulation index and EVM, providing a second waveform-level coupling example. [O_ISAC_001] <!-- evidence: ⟦O_ISAC_001 | # Modulation Strategies for Robust Optical Wireless Communications and Sensing in 6G > ## B. VLC CE-OFDM Receiver > ### III. VLC CE-OFDM PERFORMANCE ASSESSMENT | L97-L97 | strength_final=strong | context_verified=YES⟧ -->
Fiber systems integrate sensing and telecommunication on the same optical-fiber infrastructure, establishing hardware coupling by construction. [O_ISAC_004] <!-- evidence: ⟦O_ISAC_004 | # Adiabatic-tapered few-mode-fiber-based system for integrating optical fiber sensing and telecommunication > ### I. INTRODUCTION | L13-L13 | strength_final=strong | context_verified=YES⟧ -->
Microwave-photonics full-duplex systems reuse the optical carrier over a single fiber for bidirectional transmission, providing a second hardware-coupling anchor. [O_ISAC_019] <!-- evidence: ⟦O_ISAC_019 | # Full-duplex Integrated Sensing and Communication System Based on Microwave Photonics | L31-L31 | strength_final=strong | context_verified=YES⟧ -->
Algorithmic coupling appears when joint objectives are solved via explicit co-optimization, such as BCD-based joint power allocation in FSO-ISAC. [O_ISAC_023] <!-- evidence: ⟦O_ISAC_023 | # Free-Space Optical Integrated Sensing and Communication Based on DCO-OFDM: Performance Metrics and Resource Allocation | L5-L5 | strength_final=strong | context_verified=YES⟧ -->
Algorithmic coupling also arises in RL-based controllers that iteratively adjust beamwidth and bandwidth to optimize coupled performance. [O_ISAC_005] <!-- evidence: ⟦O_ISAC_005 | # III. PROBLEM FORMULATION AND RESOURCE ALLOCATION > #### B. Resource Optimization using Reinforcement Learning | L134-L136 | strength_final=strong | context_verified=YES⟧ -->
Propagation/environment coupling is exemplified when weather-driven backscatter is used as sensing feedback that conditions link operation. [O_ISAC_005] <!-- evidence: ⟦O_ISAC_005 | # Integrated Sensing and Communication for UAV Trajectory Optimization in Mixed FSO-RF Networks in Dynamic Weather Conditions | L5-L5 | strength_final=strong | context_verified=YES⟧ -->

### E.3 What This Enables Later (Bridge to Sections IV-V)
Design rationale. The optimization view provides a common language to map architectures to coupling families, define operating points, and align evaluation protocols with the metric contract (Section II-D). This lets later sections compare designs on consistent objectives without re-interpreting metrics across modalities.

Evidence alignment. Because representative O-ISAC studies already instantiate coupling-aware optimization (e.g., spectral-efficiency maximization under sensing-precision constraints), Sections IV-V can map architectures to objective forms and trade-off surfaces without redefining the problem. [O_ISAC_048] <!-- evidence: ⟦O_ISAC_048 | # I. INTRODUCTION > ## C. Clipping Noise Statistics > #### III. OPTIMAL POWER ALLOCATION FOR DCO-OFDM | L124-L132 | strength_final=strong | context_verified=YES⟧ -->
Resource-coupled optimization under backhaul limits further motivates taxonomy-to-trade-off alignment in the later synthesis. [O_ISAC_005] <!-- evidence: ⟦O_ISAC_005 | # III. PROBLEM FORMULATION AND RESOURCE ALLOCATION > #### A. Problem Formulation | L116-L122 | strength_final=strong | context_verified=YES⟧ -->

**Lesson (E):** O-ISAC is a constrained multiobjective design problem; without explicit coupling families and objective forms, cross-architecture comparisons devolve into metric aliasing.

---
