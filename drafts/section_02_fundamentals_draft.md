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

Evidence alignment: Representative studies report BER against OSNR (explicitly optical signal-to-noise ratio) for coherent optical links [O_ISAC_132], [O_ISAC_076].
Representative studies separately report electrical SNR after photodetection for BER/RMSE evaluation [O_ISAC_061], [O_ISAC_100], [O_ISAC_023]. Consistent with the governance contract, we keep these as different measurement planes and do not infer one from the other without an explicit receiver/noise model.

### A.2 Integration Paradigms (Communication-centric / Sensing-centric / Joint Design)
Design rationale: For cross-modality synthesis, we classify integration by mechanism (shared waveform, shared hardware, shared time/frequency resources, shared processing) rather than by medium. This mechanism-first lens keeps fiber/FSO/VLC/photonic-THz cases comparable while preserving their physical constraints.

**Communication-centric:** Communication performance is primary; sensing operates under communication-driven resource limits. A minimal exemplar is maximize \(R\) subject to \(J_{\text{sense}}(\boldsymbol{\theta})\le \varepsilon\).

**Sensing-centric:** Sensing fidelity is primary; communication is constrained to satisfy a service floor. A minimal exemplar is minimize \(J_{\text{sense}}(\boldsymbol{\theta})\) subject to \(R\ge R_0\) (and/or BER \(\le \beta\)).

**Joint design:** Communication and sensing are co-optimized as explicit multi-objective trade-offs. A minimal exemplar is minimize \([J_{\text{sense}}(\boldsymbol{\theta}),\; -R]\) (Pareto) or minimize \(\alpha J_{\text{sense}}(\boldsymbol{\theta})-(1-\alpha)R\), where \(R\) is throughput and \(J_{\text{sense}}\) is a sensing loss (e.g., estimation MSE or a ranging-error proxy).

These three paradigms denote operating intent (not mutually exclusive hardware classes); one architecture may move between them by changing constraints or operating point.

Paradigm-to-mechanism bridge:
- Communication-centric -> shared processing / shared resources -> sensing piggybacks on communication signaling.
- Sensing-centric -> shared waveform / shared hardware -> communication is embedded under sensing-driven constraints.
- Joint design -> shared waveform + shared processing -> explicit co-optimization couples both objectives.

We define an integration depth variable
\[
d_{\text{int}}\in\{0,\;1/2,\;1\},
\]
where \(d_{\text{int}}=0\) corresponds to coexistence, \(d_{\text{int}}=1/2\) to partial sharing/cooperation, and \(d_{\text{int}}=1\) to full co-design. This internal axis is used later to align taxonomy and trade-off synthesis without rewriting modality-specific models.

Evidence alignment: A.2 defines a review-internal synthesis scaffold for later sections; it does not claim prevalence or superiority of any paradigm in this subsection, so no paper-specific performance claim is asserted here.

**Fig. II-1** consolidates this system abstraction into a single review-facing view. It preserves a common source-modulator-waveform-channel-observation-output chain, separates coherent and IM/DD observation paths, and keeps integration paradigms as an interpretive side axis rather than as modality labels.

![Fig. II-1. Unified O-ISAC system abstraction across modalities. The figure summarizes a common source-modulator-waveform-channel-observation-output chain while retaining a modality-conditioned channel layer (fiber, FSO, VLC/LiFi, and photonic-THz bridging), coherent versus IM/DD observation paths, and an integration-depth side panel spanning communication-centric, sensing-centric, and joint-design operating intents.](fig_ii_1.png)

**Lesson (A):** A unified system model combined with explicit measurement-plane mapping is necessary to make later taxonomy and trade-off statements falsifiable rather than narrative.

---

## B. Propagation and Channel Models Across Modalities
This subsection defines a modality-aware channel layer for O-ISAC. The aim is not to rank modalities, but to expose dominant propagation impairments under a common operator view. The measurement-plane contract from Section II-A remains binding: channel modeling does not justify OSNR-to-SNR conversion, and optical/electrical plane separation is preserved.

### B.1 Fiber Channel (Guided Medium)
Design rationale: Fiber links are naturally represented by a linear dispersive baseband model in most communication analyses, with nonlinear wave dynamics added when launch power and distance require it.

A baseline model is
\[
\mathbf{y}(t)=\mathbf{G}_{\text{disp}}(t)\ast \mathbf{s}(t)+\mathbf{w}(t),
\]
where \(\mathbf{G}_{\text{disp}}(t)\) captures chromatic-dispersion-dominated propagation.

For nonlinear regimes, a conceptual NLSE form is
\[
\frac{\partial A(z,t)}{\partial z}= -\frac{\alpha}{2}A - j\frac{\beta_2}{2}\frac{\partial^2 A}{\partial t^2} + j\gamma|A|^2A + \eta(z,t),
\]
where \(A(z,t)\) is the optical field envelope, \(\alpha\) is attenuation, \(\beta_2\) is group-velocity dispersion, and \(\gamma\) is the nonlinear coefficient. For sensing tasks, fiber reports spatial granularity via \(\Delta z\) (gauge/segment length), not wireless-style \(\Delta r_{\min}\) (Metric Governance).

Evidence alignment: This part is theory-standard modeling; no paper-specific prevalence claim is asserted here.

### B.2 FSO Channel (Atmosphere + Pointing)
Design rationale: FSO propagation is dominated by multiplicative effects (turbulence and misalignment/pointing) plus path attenuation.

A compact IM/DD-friendly form is
\[
y = h_{\text{turb}}\,h_{\text{point}}\,h_{\text{att}}\,x + n,\qquad x\ge 0,
\]
with
\[
h_{\text{att}}=\exp(-\kappa d),
\]
where \(d\) is propagation distance and \(\kappa\) is the extinction coefficient. Turbulence statistics are typically modeled with log-normal or Gamma-Gamma families depending on regime assumptions.

Evidence alignment: Representative studies explicitly model Beer-Lambert attenuation and pointing/turbulence effects in FSO channel setup and analysis [O_ISAC_035], [O_ISAC_005].

### B.3 VLC Channel (Lambertian + LoS/NLoS Impulse Response)
Design rationale: VLC behavior is geometry-driven and typically represented by an intensity impulse response under Lambertian emission assumptions.

A generic representation is
\[
h(t)=h_{\text{LOS}}(t)+h_{\text{NLOS}}(t),
\]
where LoS and reflected components are separated in the CIR. Shot noise, thermal noise, and ambient-light-induced noise are included according to receiver setup.

Evidence alignment: Representative VLC/OWC studies model LoS/NLoS decomposition and Lambertian emission within impulse-response channel formulations [O_ISAC_039], [O_ISAC_022].

### B.4 Photonic-THz Bridging (Optical Generation/Distribution + THz Propagation)
Design rationale: Photonic-THz O-ISAC is inherently a two-stage channel chain: optical-domain generation/distribution followed by THz wireless propagation.

We therefore model this link as a split channel: an optical stage (carrier generation/distribution and optical front-end impairments) plus a THz stage (wireless propagation with multipath/frequency-selective effects). This split avoids plane conflation and keeps impairment attribution explicit.

Evidence alignment: Representative photonics-assisted mmWave/THz studies discuss multipath and frequency-selective channel effects in fiber-wireless settings [O_ISAC_241], [O_ISAC_077].

**Lesson (B):** Channel models are modality-specific in dominant impairments, but the reporting contract (plane separation plus metric governance) is modality-invariant.

---

## C. Transceiver and Hardware Abstractions (What is Common, What is Modality-Specific)
This subsection defines a hardware abstraction layer that stays valid across fiber/FSO/VLC/photonic-THz implementations. The focus is architectural role (source/modulator, receiver/detection, wavefront control), not device-level ranking.

### C.1 Sources and Modulators
Design rationale: The source-modulator stack determines whether operation is coherent or IM/DD and sets the feasible waveform interface for joint communication-sensing design.

Evidence alignment: Representative photonic-THz chains use ECL-driven MZM/IQ-modulator front-ends consistent with coherent operation [O_ISAC_029]. IM/DD-oriented VLC implementations use LED/LD intensity modulation with nonnegative optical intensity constraints [O_ISAC_001].

### C.2 Receivers and Detection
Design rationale: Receiver architecture defines the observation plane and therefore the admissible signal-quality interpretation.

We restate the measurement-plane contract for receiver-side interpretation:
\[
\pi(m)\in\{\text{OPTICAL\_PLANE},\;\text{ELECTRICAL\_PLANE},\;\text{AMBIGUOUS}\},
\]
where OSNR is optical-plane and electrical SNR/ESNR is post-detection electrical-plane; OSNR-to-SNR conversion is prohibited without an explicit receiver/noise model (Metric Governance).

Evidence alignment: Coherent receiver implementations explicitly use optical-hybrid/balanced-photodetector style detection chains [O_ISAC_028], [O_ISAC_029]. IM/DD receiver implementations explicitly use photodiode-based direct detection and O/E conversion [O_ISAC_001], [O_ISAC_023].

### C.3 Beamforming/Wavefront Control Enablers
Design rationale: Spatial-control elements (especially OPA-class front ends) are treated as enablers that shape beam directionality and angular observability while remaining compatible with the source-modulator-channel-detector abstraction.

A generic array response model for steering/sensing is
\[
\mathbf{a}(\phi)=\left[1,\;e^{jkd\sin\phi},\;\ldots,\;e^{jkd(N-1)\sin\phi}\right]^{\top}.
\]

Evidence alignment: Representative OW-ISAC studies explicitly use OPA-based beamforming front ends and discuss their role in joint communication-sensing operation [O_ISAC_061], [O_ISAC_091].

Table II-1 compacts the modality-aware channel and transceiver abstractions introduced across Sections II-B and II-C. Its purpose is not to rank modalities, but to preserve a common comparison scaffold while making each modality's native sensing abstraction and reporting constraints explicit.

### Table II-1: Modality-Aware Channel and Transceiver Abstraction Summary

| Modality | Channel abstraction | Signaling / detection view | Dominant impairment family | Native sensing abstraction | Governance guard |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Fiber (cabled) | Guided dispersive link; NLSE-style extension in nonlinear regimes | Typically coherent, field-aware observation | Dispersion, Kerr nonlinearity, PMD, phase noise | \(\Delta z\) for DAS/OTDR-like spatial granularity | Do not relabel \(\Delta z\) as wireless \(\Delta r_{\min}\) |
| FSO | Multiplicative atmosphere-plus-pointing link with path attenuation | IM/DD or coherent depending receiver chain | Turbulence, pointing error, attenuation | Delay/range estimation under two-way ranging convention | Keep optical-plane and electrical-plane reporting distinct |
| VLC / LiFi | Lambertian LoS/NLoS CIR with geometry-driven gain | IM/DD with nonnegative intensity waveform | Ambient light, shot/thermal noise, geometry | Positioning/ranging from CIR structure or intensity observations | Do not import coherent-field assumptions into IM/DD interpretations |
| Photonic-THz bridge | Split chain: optical generation/distribution + THz propagation | Bridged optical front-end plus THz wireless observation | Optical front-end impairments plus frequency-selective THz propagation | Delay/range/angle inference over a two-stage chain | Keep optical generation stage and THz propagation stage conceptually separated |

**Lesson (C):** Hardware commonality is abstraction-level (source-modulator-receiver-wavefront control), while implementations remain modality-specific.

---

## D. Sensing Principles and the Metric Contract (Resolution vs Accuracy vs Bounds)
Design rationale: Section II-D defines the metric contract that keeps sensing comparisons valid across O-ISAC modalities. The key separation is between physics-limited resolution, estimator-dependent accuracy, and bound-based limits.

### D.1 Ranging/ToF/FMCW/LFM Fundamentals
Design rationale: A two-way ranging convention provides a shared physical baseline for ToF/FMCW/LFM sensing and ties resolution to effective bandwidth instead of estimator choice.

We adopt the two-way delay model with
\[
\Delta r_{\min} := \frac{v}{2B_{\text{eff}}},
\]
where \(v=c\) in free space and \(v\approx c/n_g\) in guided media. For ranging tasks, \(\tau=2r/v\) links delay and range. Fiber DAS/OTDR records are mapped to \(\Delta z\) (gauge/segment length), not \(\Delta r_{\min}\) (Metric Governance).

Evidence alignment: Representative photonic ranging studies report bandwidth-limited resolution forms consistent with \(c/(2B)\) under the two-way convention [O_ISAC_026], [O_ISAC_034].

### D.2 Accuracy (Estimator-Dependent) and CRB/FIM Bounds
Design rationale: Accuracy is estimator- and noise-model-dependent, so it must remain distinct from bandwidth-limited resolution.

Estimator-dependent accuracy is defined as
\[
\sigma_r := \sqrt{\mathbb{E}[(\hat r-r)^2]},
\]
while a canonical delay-bound form is
\[
\mathrm{var}(\hat\tau) \ge \frac{1}{8\pi^2\beta^2\,\mathrm{SNR}} \Rightarrow \mathrm{var}(\hat r) \ge \left(\frac{v}{2}\right)^2\mathrm{var}(\hat\tau).
\]
Here SNR is an abstract estimator-plane quantity unless a source explicitly fixes the measurement plane; this expression does not permit OSNR/electrical-SNR substitution (Metric Governance).

Evidence alignment: This subsection states theory-standard definitions and bound forms; no paper-specific prevalence claim is asserted.

### D.3 Fiber Spatial Granularity (\(\Delta z\)) vs Wireless Range Resolution (\(\Delta r_{\min}\))
Design rationale: Fiber spatial granularity and wireless range resolution are not interchangeable metrics.

We enforce the mapping rule: in DAS/OTDR-like fiber contexts, spatial/distance granularity maps to \(\Delta z\); in bandwidth-limited ToF/FMCW ranging contexts, resolution maps to \(\Delta r_{\min}\). **Comparability warning:** \(\Delta z\) must not be substituted into \(\mathrm{CRQ}_{\Delta}\).

Evidence alignment: Representative fiber sensing works report meter-scale spatial granularity aligned with \(\Delta z\) rather than \(\Delta r_{\min}\) [O_ISAC_006], [O_ISAC_013].

### D.4 Capacity-Resolution Quotient
Design rationale: A compact cross-architecture indicator is useful only under strict admissibility constraints.

We define
\[
\mathrm{CRQ}_{\Delta} := \frac{R}{\Delta r_{\min}} \quad [\mathrm{bps/m}].
\]
\(\mathrm{CRQ}_{\Delta}\) is computed only when both \(R\) and \(\Delta r_{\min}\) are available from the same scenario record and the measurement-plane note is explicit. If only \(\Delta z\) (or generic spatial_resolution_m) is available, \(\mathrm{CRQ}_{\Delta}\) remains undefined.

Evidence alignment: This is a governance-level construct used to control later synthesis; no prevalence claim is asserted in Section II-D.

Table II-2 summarizes the metric contract used throughout this review. It states each metric's role, native scope or measurement plane, and the substitutions that remain inadmissible during cross-study comparison.

### Table II-2: Metric Contract and Comparability Guard Summary

| Quantity | Role | Native scope / plane | Admissible use | Forbidden substitution / warning |
| :--- | :--- | :--- | :--- | :--- |
| \(\Delta r_{\min}\) | Bandwidth-limited resolution | Two-way ranging physics | Use as resolution term; combine with \(R\) for \(\mathrm{CRQ}_{\Delta}\) only when both come from the same scenario | Do not treat as \(\sigma_r\) or \(\Delta z\) |
| \(\sigma_r\) | Estimator-dependent accuracy | Estimator/noise-model dependent | Report as accuracy or RMSE-style sensing fidelity | Do not relabel as physics-limited resolution |
| CRB / FIM | Bound-type metric | Model-based lower bound context | Use to contextualize attainable estimator accuracy | Do not report as measured accuracy or as \(\Delta r_{\min}\) |
| \(\Delta z\) | Fiber spatial granularity | Guided sensing / DAS-OTDR contexts | Use for gauge/segment-length style fiber reporting | Do not substitute into \(\mathrm{CRQ}_{\Delta}\) or wireless ranging comparisons |
| \(R\) | Communication throughput / rate | Communication objective | Use directly as rate objective; pair with \(\Delta r_{\min}\) only under matched scenario records | Not a sensing metric and not a quality-plane surrogate |
| \(\mathrm{CRQ}_{\Delta}\) | Derived joint indicator | Same-scenario derived quantity | Compute only from explicit \(R\) and \(\Delta r_{\min}\) | Undefined if only \(\Delta z\) or ambiguous resolution fields are available |
| OSNR | Optical-plane quality metric | Pre-detection optical plane | Compare within explicit optical-plane reporting | Do not convert to electrical SNR without an explicit receiver/noise model |
| SNR / ESNR | Electrical-plane quality metric | Post-detection electrical plane | Compare only within fixed electrical-plane contexts | Do not merge with OSNR as if they were interchangeable |
| Ambiguous SNR | Unresolved quality label | Plane unspecified | Flag as ambiguous and exclude from plane-sensitive synthesis | Cannot justify plane separation or cross-plane conversion |

**Fig. II-2** visualizes the metric-governance contract used throughout this review. Specifically, it shows the admissible chain from effective bandwidth to \(\Delta r_{\min}\), from delay/time-of-flight to range, and from matched \(R\) plus \(\Delta r_{\min}\) to \(\mathrm{CRQ}_{\Delta}\); it also keeps CRB/FIM as contextual support for estimator accuracy rather than as a substitute for \(\sigma_r\), preserves \(\Delta z\) as fiber-only spatial granularity, and enforces explicit separation between optical-plane and electrical-plane quality metrics.

![Fig. II-2. Metric contract and admissible comparison map for O-ISAC. The figure visualizes the admissible chain from effective bandwidth to bandwidth-limited resolution \(\Delta r_{\min}\), from delay/time-of-flight to range, and from matched \(R\) plus \(\Delta r_{\min}\) to the derived indicator \(\mathrm{CRQ}_{\Delta}\). It keeps estimator-level accuracy \(\sigma_r\), bound-type metrics (CRB/FIM), fiber spatial granularity \(\Delta z\), and plane-specific quality metrics (OSNR versus SNR/ESNR) explicitly separated. Green links denote admissible relations, dashed gray links denote contextual support, and blocked red links denote forbidden substitutions or cross-plane conversions without an explicit receiver/noise model.](fig_ii_2.png)

**Lesson (D):** Without explicit separation of \(\Delta r_{\min}\), \(\sigma_r\)/CRB, and \(\Delta z\), resolution becomes non-isomorphic and cross-study comparisons become non-defensible.

---

## E. ISAC Coupling and Trade-off Foundations (Optimization View)

### E.1 Multiobjective Formulation
Design rationale. We cast O-ISAC co-design as a multiobjective program over a shared design vector $\mathbf{x}$ that collects waveform/resource parameters, optical front-end knobs, sensing-task parameters, and processing knobs, so that communication performance and sensing fidelity are optimized on the same degrees of freedom. Let $f_c(\mathbf{x})$ denote a communication objective (e.g., rate/BER/outage) and $f_s(\mathbf{x})$ denote a sensing objective (e.g., resolution/accuracy/bound), with feasibility $\mathbf{x}\in\mathcal{X}$ capturing nonnegativity, power/bandwidth, and hardware limits. A point $\mathbf{x}^*$ is Pareto-optimal if no other feasible design improves one objective without degrading the other; scalarizations such as $\max_{\mathbf{x}\in\mathcal{X}} f_c(\mathbf{x})-\lambda f_s(\mathbf{x})$ provide convenient operating points but do not exhaust the Pareto set.

Evidence alignment. Representative FSO O-ISAC works explicitly maximize spectral efficiency subject to sensing-precision (Fisher-information) constraints via power allocation, yielding a constrained trade-off formulation. [O_ISAC_048] <!-- evidence: ⟦O_ISAC_048 | # I. INTRODUCTION > ## C. Clipping Noise Statistics > #### III. OPTIMAL POWER ALLOCATION FOR DCO-OFDM | L124-L132 | strength_final=strong | context_verified=YES⟧ -->
Other works formulate joint power-allocation problems for communication-centric and sensing-centric scenarios and solve them with block-coordinate-descent algorithms, explicitly positioning the comm-sensing trade-off within the optimization. [O_ISAC_023] <!-- evidence: ⟦O_ISAC_023 | # Free-Space Optical Integrated Sensing and Communication Based on DCO-OFDM: Performance Metrics and Resource Allocation | L5-L5 | strength_final=strong | context_verified=YES⟧ -->

### E.2 Coupling Mechanisms by Modality
Design rationale. Coupling is most stable when categorized by mechanism rather than modality: resource coupling (power/bandwidth/time), waveform coupling (shared modulation and signaling), hardware coupling (shared optical/electrical front-ends), algorithmic coupling (joint inference/control), and propagation/environment coupling (shared impairments). These mechanisms manifest differently across modalities (e.g., IM/DD nonnegativity, coherent phase access, fiber probe interactions, turbulence/ambient light), but the coupling logic is invariant.

Evidence alignment. Resource coupling is explicit in DCO-OFDM FSO-ISAC studies where communication and sensing objectives are jointly controlled through constrained power allocation [O_ISAC_048], [O_ISAC_023].
Waveform-level coupling is directly shown through waveform-parameter tuning (e.g., power-split control) [O_ISAC_075] and further supported by modulation-index trade-off discussions [O_ISAC_001].
Algorithmic coupling is explicit in optimization pipelines using block-coordinate decomposition and weighted-sum scalarization to tune trade-off operating points under joint constraints [O_ISAC_023], [O_ISAC_052].
Hardware and propagation couplings are retained as synthesis categories in this section; we do not assert cross-corpus prevalence claims for those categories here.

### E.3 What This Enables Later (Bridge to Sections IV-V)
Design rationale. The optimization view provides a common language to map architectures to coupling families, define operating points, and align evaluation protocols with the metric contract (Section II-D). This lets later sections compare designs on consistent objectives without re-interpreting metrics across modalities.

Evidence alignment. Because representative O-ISAC studies already instantiate coupling-aware optimization and explicit trade-off curves (e.g., spectral-efficiency versus sensing-precision under constrained power allocation), Sections IV-V can map architectures to objective forms and admissible operating regions without redefining the metric contract [O_ISAC_048], [O_ISAC_023], [O_ISAC_052].

**Lesson (E):** O-ISAC is a constrained multiobjective design problem; without explicit coupling families and objective forms, cross-architecture comparisons devolve into metric aliasing.
