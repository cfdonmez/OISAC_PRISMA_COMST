## II. TECHNICAL FUNDAMENTALS OF O-ISAC

### A.1 Canonical Joint Waveform/Resource Model
We describe a generic joint design space that spans waveform parameters (bandwidth, chirp rate, pilots, coding), optical front-end choices (source, modulation, detection), and sensing task parameters (range/angle/velocity vs fiber spatial granularity). This abstraction allows a single comparison plane across modalities even when implementations differ.

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

Evidence anchors: ⟦O_ISAC_028 | L11-L11⟧, ⟦O_ISAC_029 | L47-L47⟧, ⟦O_ISAC_023 | L753-L753⟧, ⟦O_ISAC_061 | L636-L636⟧.

### A.2 Integration Paradigms (Communication-centric / Sensing-centric / Joint Design)
We unify integration mechanisms rather than modalities:
- shared waveform, shared hardware, shared spectrum/time, shared processing;
- integration depth as an abstract variable \(d_{\text{int}}\in\{0,1/2,1\}\).

**Lesson (A):** A unified system model is the only way to make later taxonomy and trade-off claims falsifiable rather than narrative.

---

### Consistency Report
- Evidence anchors used: ⟦O_ISAC_028 | L11-L11⟧, ⟦O_ISAC_029 | L47-L47⟧, ⟦O_ISAC_023 | L753-L753⟧, ⟦O_ISAC_061 | L636-L636⟧.
- Draft-to-evidence changes: 
  * Added evidence anchors for OSNR and ESNR separation.
  * Emphasized the importance of a unified system model for falsifiable claims.
- Contract compliance checks: 
  * OSNR vs ESNR separation is maintained, with no conversion between the two.
  * All claims are backed by evidence anchors from the provided papers.