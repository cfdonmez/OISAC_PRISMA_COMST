# II. TECHNICAL FUNDAMENTALS OF O-ISAC

> **Section intent (1 paragraph):** This section establishes the unified physical-layer foundations required to compare fiber-, FSO-, VLC-, and photonic-THz O-ISAC systems under a common measurement contract. We intentionally separate (i) propagation/channel models, (ii) transceiver/hardware abstractions, and (iii) sensing-performance definitions (resolution vs accuracy vs bounds), so that later taxonomy and trade-off synthesis are mathematically defensible.

---

## A. Unified O-ISAC System Model and Integration Paradigms

### A.1 Canonical Joint Waveform/Resource Model
Define a generic joint design variable set:
- waveform parameters (bandwidth, chirp rate, pilots, coding),
- optical front-end parameters (source type, modulation, detection),
- sensing task parameters (range/angle/velocity vs fiber spatial granularity).

**Generic baseband observation (complex coherent model):**
\[
\mathbf{y}(t)=\mathbf{H}(t;\boldsymbol{\theta})\mathbf{s}(t)+\mathbf{w}(t),
\]
where \(\boldsymbol{\theta}\) collects sensing parameters (delay/range, Doppler, AoA/AoD, vibration state, etc.).

**IM/DD observation (real nonnegative intensity constraint):**
\[
y(t)=\mathcal{R}\,\big(x(t)\ast h(t)\big)+n(t),\qquad x(t)\ge 0,
\]
where \(\mathcal{R}\) is responsivity and \(h(t)\) is the intensity channel impulse response.

> **Measurement-plane note:** declare where “SNR” is measured (electrical post-detection) vs “OSNR” (optical domain pre-detection), and why this matters for cross-modality comparisons.

### A.2 Integration Paradigms (Communication-centric / Sensing-centric / Joint Design)
Provide a unifying taxonomy of integration *mechanisms* (not modalities):
- shared waveform, shared hardware, shared spectrum/time, shared processing.
Define “integration depth” as an abstract variable \(d_{\text{int}}\in\{0,1/2,1\}\) matching your Table I scoring logic.

**Lesson (A):** A unified system model is the only way to make later “taxonomy” and “trade-off” claims falsifiable rather than narrative.

---

## B. Propagation and Channel Models Across Modalities

### B.1 Fiber Channel (Guided Medium)
State the linearized coherent comm model and (optionally) the NLSE abstraction:

**(i) Linear dispersive model:**
\[
\mathbf{y}(t)=\mathbf{G}_{\text{disp}}(t)\ast \mathbf{s}(t)+\mathbf{w}(t)
\]

**(ii) NLSE (conceptual, not fully expanded):**
\[
\frac{\partial A(z,t)}{\partial z}
= -\frac{\alpha}{2}A -j\frac{\beta_2}{2}\frac{\partial^2 A}{\partial t^2}
+ j\gamma |A|^2A + \eta(z,t).
\]

### B.2 FSO Channel (Atmosphere + Pointing)
Write the multiplicative fading + pointing error structure:
\[
y = h_{\text{turb}}\,h_{\text{point}}\,x + n,
\]
and specify candidate statistical models (lognormal / Gamma–Gamma) and when each is used.
Clarify the LoS dominance and when multipath is non-negligible (urban canyon, reflective surfaces).

### B.3 VLC Channel (Lambertian + Multipath + Ambient Light)
Lambertian DC gain \(H_0\) and impulse response form; include the illumination constraint:
\[
x(t)=x_{\text{DC}} + x_{\text{AC}}(t),\quad x_{\text{AC}}(t)\in[-x_{\text{DC}},\,\infty)
\]
Highlight shot noise / thermal noise and the ambient light term.

### B.4 Photonic-THz Bridging (Optical generation/distribution + THz wireless propagation)
Define the “bridging” as a *hybrid transceiver architecture*:
- optical carrier(s) used for generation/LO/distribution,
- RF/THz carrier used for wireless propagation.

**Lesson (B):** Channel models differ in their dominant impairments, but the *contract* for reporting comm/sensing performance must not.

---

## C. Transceiver and Hardware Abstractions (What is Common, What is Modality-Specific)

### C.1 Sources and Modulators
- LED/LD/VCSEL, external modulation (MZM, TFLN-MZM), direct modulation.
State which assumptions enable coherent vs IM/DD.

### C.2 Receivers and Detection
- IM/DD photodiodes, APD/SPAD, coherent receivers.
Add explicit “measurement plane” mapping:
- OSNR → coherent optical systems,
- electrical SNR → VLC/IM-DD post-detection.

### C.3 Beamforming/Wavefront Control Enablers
- OPA, ORIS/metasurfaces, PICs.
Define a generic array response for angle sensing/beam steering:
\[
\mathbf{a}(\phi)=\left[1,\,e^{j k d \sin\phi},\,\ldots,\,e^{j k d (N-1)\sin\phi}\right]^{\top}.
\]

**Lesson (C):** Hardware commonality exists at the abstraction level (source–modulator–channel–detector), not at the implementation level.

---

## D. Sensing Principles and the Metric Contract (Resolution vs Accuracy vs Bounds)

### D.1 Ranging/ToF/FMCW/LFM Fundamentals
State the *two-way ranging convention* explicitly.

**Bandwidth-limited two-way range resolution:**
\[
\Delta r_{\min}\triangleq \frac{v}{2B_{\mathrm{eff}}}
\]
with \(v=c\) in free space and \(v\approx c/n_g\) in guided media.

### D.2 Accuracy (Estimator-Dependent) and CRB/FIM Bounds
Define estimator RMSE:
\[
\sigma_r \triangleq \sqrt{\mathbb{E}\big[(\hat r-r)^2\big]}.
\]

Provide a canonical CRB form (delay estimation exemplar):
\[
\mathrm{var}(\hat\tau)\ge \frac{1}{8\pi^2 \beta^2\,\mathrm{SNR}}
\quad \Rightarrow \quad
\mathrm{var}(\hat r)\ge \left(\frac{v}{2}\right)^2\mathrm{var}(\hat\tau),
\]
where \(\beta\) is RMS bandwidth.

### D.3 Fiber Spatial Granularity (\(\Delta z\)) vs Wireless Range Resolution (\(\Delta r_{\min}\))
Make the separation explicit:
- \(\Delta z\): minimum resolvable segment / gauge length / sampling granularity in DAS/OTDR-type sensing.
- \(\Delta r_{\min}\): bandwidth-limited ranging resolution for ToF/FMCW-style tasks.

### D.4 Capacity–Resolution Quotient
Keep your contract consistent:
\[
\mathrm{CRQ}_{\Delta}\triangleq \frac{R}{\Delta r_{\min}}\quad [\mathrm{bps/m}].
\]
Add a one-sentence constraint: comparisons only on subset where \(\Delta r_{\min}\) exists.

**Lesson (D):** Without separating \(\Delta r_{\min}\), \(\sigma_r\), CRB/FIM, and \(\Delta z\), “resolution” becomes non-isomorphic and destroys cross-paper comparability.

---

## E. ISAC Coupling and Trade-off Foundations (Optimization View)

### E.1 Multiobjective Formulation
State a generic joint design problem:
\[
\max_{\mathbf{x}} \; R(\mathbf{x})
\quad \text{s.t.}\quad
\mathrm{CRB}_r(\mathbf{x})\le \epsilon,\;\; P(\mathbf{x})\le P_{\max},
\]
or equivalently a scalarized Lagrangian:
\[
\max_{\mathbf{x}}\; R(\mathbf{x})-\lambda\,\mathrm{CRB}_r(\mathbf{x}).
\]

### E.2 Coupling Mechanisms by Modality
Explain *why* coupling differs:
- IM/DD amplitude constraints,
- coherent phase access,
- fiber sensing probe interference with comm carriers,
- turbulence/ambient noise affecting both tasks.

### E.3 What This Enables Later (Bridge to Sections IV–V)
One paragraph mapping: Section II gives the *physics + metrics*; Section IV will categorize *architectures*; Section V will quantify *Pareto frontiers*.

**Lesson (E):** O-ISAC is not “two tasks in one box”; it is a constrained joint optimization where the constraints differ by modality and measurement plane.

---
