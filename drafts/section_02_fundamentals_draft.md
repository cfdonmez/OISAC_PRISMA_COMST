# II. TECHNICAL FUNDAMENTALS OF O-ISAC

> **Section intent:** This section establishes unified physical-layer foundations for comparing fiber-, FSO-, VLC-, and photonic-THz O-ISAC systems under a common measurement contract. We separate (i) propagation/channel models, (ii) transceiver/hardware abstractions, and (iii) sensing-performance definitions (resolution vs accuracy vs bounds) so that later taxonomy and trade-off synthesis are mathematically defensible.

---

## A. Unified O-ISAC System Model and Integration Paradigms

### A.1 Canonical Joint Waveform/Resource Model
We describe a generic joint design space that spans waveform parameters (bandwidth, chirp rate, pilots, coding), optical front-end choices (source, modulation, detection), and sensing task parameters (range/angle/velocity vs fiber spatial granularity). This abstraction allows a single comparison plane across modalities even when implementations differ.

**Generic baseband observation (complex coherent model):**

\[
\mathbf{y}(t)=\mathbf{H}(t;\boldsymbol{\theta})\mathbf{s}(t)+\mathbf{w}(t),
\]

where \(\boldsymbol{\theta}\) collects sensing parameters (delay/range, Doppler, AoA/AoD, vibration state, etc.).

**IM/DD observation (real, nonnegative intensity constraint):**

\[
y(t)=\mathcal{R}\,\big(x(t)\ast h(t)\big)+n(t),\qquad x(t)\ge 0,
\]

where \(\mathcal{R}\) is responsivity and \(h(t)\) is the intensity channel impulse response.

**Measurement-plane note:** we explicitly separate OSNR (optical domain, pre-detection) from electrical SNR (post-detection/receiver output). These are not interchangeable and must be reported on their own planes to preserve cross-modality comparability.

Evidence anchors (OSNR/ESNR plane separation): O_ISAC_028 (L11-L11), O_ISAC_029 (L47-L47), O_ISAC_023 (L753-L753), O_ISAC_061 (L636-L636).

### A.2 Integration Paradigms (Communication-centric / Sensing-centric / Joint Design)
We unify integration mechanisms rather than modalities:
- shared waveform, shared hardware, shared spectrum/time, shared processing;
- integration depth as an abstract variable \(d_{\text{int}}\in\{0,1/2,1\}\).

**Lesson (A):** A unified system model is the only way to make later taxonomy and trade-off claims falsifiable rather than narrative.

---

## B. Propagation and Channel Models Across Modalities

### B.1 Fiber Channel (Guided Medium)
We use a linear dispersive comm model for the baseline and the NLSE as a conceptual extension:

**(i) Linear dispersive model:**
\[
\mathbf{y}(t)=\mathbf{G}_{\text{disp}}(t)\ast \mathbf{s}(t)+\mathbf{w}(t)
\]

**(ii) NLSE (conceptual):**
\[
\frac{\partial A(z,t)}{\partial z}
= -\frac{\alpha}{2}A -j\frac{\beta_2}{2}\frac{\partial^2 A}{\partial t^2}
+ j\gamma |A|^2A + \eta(z,t).
\]

### B.2 FSO Channel (Atmosphere + Pointing)
We model multiplicative fading and pointing:
\[
y = h_{\text{turb}}\,h_{\text{point}}\,x + n,
\]
with lognormal / Gamma–Gamma turbulence models depending on regime, and explicit pointing-error terms. LoS dominates in many deployments, but multipath can matter in reflective or urban canyon scenarios.

### B.3 VLC Channel (Lambertian + Multipath + Ambient Light)
We use Lambertian DC gain and impulse response formulations, with illumination and nonnegativity constraints:
\[
x(t)=x_{\text{DC}} + x_{\text{AC}}(t),\quad x_{\text{AC}}(t)\in[-x_{\text{DC}},\,\infty).
\]
Shot noise, thermal noise, and ambient light terms explicitly shape receiver SNR in IM/DD VLC.

### B.4 Photonic-THz Bridging (Optical Generation/Distribution + THz Propagation)
We treat photonic-THz as a hybrid transceiver architecture: optical carriers for generation/LO/distribution, and RF/THz carriers for wireless propagation. This separation allows a consistent report of comm/sensing metrics despite heterogeneous front-ends.

**Lesson (B):** Channel models differ in dominant impairments, but the reporting contract for comm/sensing performance must not.

---

## C. Transceiver and Hardware Abstractions (What is Common, What is Modality-Specific)

### C.1 Sources and Modulators
Common abstraction: source → modulator → channel → detector. Implementations vary (LED/LD/VCSEL, MZM, TFLN-MZM, direct modulation), but the model remains consistent. Coherent access vs IM/DD is determined by source and receiver architecture.

### C.2 Receivers and Detection
We separate detection planes and map metrics accordingly:
- OSNR for coherent optical systems (optical plane),
- electrical SNR for IM/DD systems (receiver output plane).

Evidence anchors (plane separation): O_ISAC_028 (L11-L11), O_ISAC_029 (L47-L47), O_ISAC_023 (L753-L753), O_ISAC_061 (L636-L636).

### C.3 Beamforming/Wavefront Control Enablers
Hardware enablers (OPA, ORIS/metasurfaces, PICs) support beam steering and angle sensing. A generic array response is
\[
\mathbf{a}(\phi)=\left[1,\,e^{j k d \sin\phi},\,\ldots,\,e^{j k d (N-1)\sin\phi}\right]^{\top}.
\]

**Lesson (C):** Hardware commonality exists at the abstraction level, not the implementation level.

---

## D. Sensing Principles and the Metric Contract (Resolution vs Accuracy vs Bounds)

### D.1 Ranging/ToF/FMCW/LFM Fundamentals
We adopt a *two-way ranging convention* and define bandwidth-limited range resolution:

\[
\Delta r_{\min}\triangleq \frac{v}{2B_{\mathrm{eff}}}
\]

with \(v=c\) in free space and \(v\approx c/n_g\) in guided media.

Evidence anchors (\(\Delta r_{\min}\)): O_ISAC_026 (L74-L84), O_ISAC_034 (L145-L155), O_ISAC_043 (L21-L31), O_ISAC_044 (L119-L129).

### D.2 Accuracy (Estimator-Dependent) and CRB/FIM Bounds
Accuracy is estimator-dependent and typically reported via RMSE:
\[
\sigma_r \triangleq \sqrt{\mathbb{E}\big[(\hat r-r)^2\big]}.
\]

A canonical CRB form (delay estimation exemplar) is
\[
\mathrm{var}(\hat\tau)\ge \frac{1}{8\pi^2 \beta^2\,\mathrm{SNR}}
\quad \Rightarrow \quad
\mathrm{var}(\hat r)\ge \left(\frac{v}{2}\right)^2\mathrm{var}(\hat\tau),
\]
where \(\beta\) is RMS bandwidth.

### D.3 Fiber Spatial Granularity (\(\Delta z\)) vs Wireless Range Resolution (\(\Delta r_{\min}\))
We explicitly separate the two:
- \(\Delta z\): minimum resolvable segment / gauge length / sampling granularity in DAS/OTDR-type sensing,
- \(\Delta r_{\min}\): bandwidth-limited ranging resolution for ToF/FMCW-style tasks.

Evidence anchors (\(\Delta z\)): O_ISAC_006 (L79-L95), O_ISAC_013 (L3-L19), O_ISAC_018 (L146-L162), O_ISAC_024 (L3-L19).

### D.4 Capacity–Resolution Quotient
We keep the contract consistent:

\[
\mathrm{CRQ}_{\Delta}\triangleq \frac{R}{\Delta r_{\min}}\quad [\mathrm{bps/m}].
\]

Comparisons are only valid on the subset where \(\Delta r_{\min}\) is defensible.

**Lesson (D):** Without separating \(\Delta r_{\min}\), \(\sigma_r\), CRB/FIM, and \(\Delta z\), “resolution” becomes non-isomorphic and destroys cross-paper comparability.

---

## E. ISAC Coupling and Trade-off Foundations (Optimization View)

### E.1 Multiobjective Formulation
We state a generic joint design problem:
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
Coupling differs by modality:
- IM/DD amplitude constraints,
- coherent phase access,
- fiber sensing probe interference with comm carriers,
- turbulence/ambient noise affecting both tasks.

### E.3 What This Enables Later (Bridge to Sections IV–V)
Section II provides the physics and metric contract; Section IV will categorize architectures, and Section V will quantify Pareto frontiers.

**Lesson (E):** O-ISAC is not “two tasks in one box”; it is a constrained joint optimization where the constraints differ by modality and measurement plane.

---
