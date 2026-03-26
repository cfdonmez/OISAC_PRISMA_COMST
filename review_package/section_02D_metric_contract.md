## D. Sensing Principles and the Metric Contract (Resolution vs Accuracy vs Bounds)
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
