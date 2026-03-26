# I. INTRODUCTION (O‑ISAC Survey)

## A. Hook (Motivation)
> **Pattern A – 6G Vision Hook**: "As 6G networks evolve towards the *intelligence of everything*, **Optical Integrated Sensing and Communication (O‑ISAC)** emerges as a transformative paradigm that unifies perception, transmission, and processing on optical carriers. This integration addresses the spectrum scarcity and interference bottlenecks of traditional RF‑ISAC and enables ultra‑high data‑rate, low‑latency, and high‑resolution sensing for emerging verticals such as smart factories, autonomous vehicles, and holographic telepresence."

> **Pattern B – Spectrum‑Crisis Hook**: "The explosive growth of mobile‑data traffic and high‑resolution sensing applications has created an unprecedented demand for spectrum resources. Optical carriers (fiber, VLC, LiFi, FSO) offer orders‑of‑magnitude larger bandwidths, making them the natural substrate for the next generation of joint sensing‑communication systems."

> **Pattern C – Convergence Trend Hook**: "Recent standards (IEEE 802.11be, 3GPP NR‑ISAC, ITU‑6G) are converging on the idea that *sensing* and *communication* should share the same physical layer. O‑ISAC is the concrete realization of this trend, leveraging photonic components, wavelength‑division multiplexing, and coherent detection to achieve simultaneous high‑capacity data transfer and precise environmental awareness."

*Choose one of the above hooks (or combine) and replace the placeholder text with your specific motivation.*

## B. Overview of O‑ISAC (Technical Context)
- **Physical‑Layer Convergence**: shared waveform, shared hardware (laser/LED sources, photodetectors), joint spectrum allocation.
- **Key Enabling Technologies**: Photonic Integrated Circuits (PIC), Spatial‑Division Multiplexing (SDM), Optical Beamforming, Machine‑Learning‑assisted channel estimation.
- **Application Domains**: 6G wireless back‑haul, vehicular networks, indoor positioning, distributed acoustic sensing, quantum‑enhanced metrology.

> *Example from COMST_001*: "With the continuous evolution of wireless networks, the integration of sensing and communication over optical carriers provides a unified solution for high‑throughput, low‑latency services."

## C. Related Surveys (Gap Analysis)
| Survey | Year | Scope | O‑ISAC Coverage | Gap |
|--------|------|-------|----------------|-----|
| **[Ref A]** | 2020 | RF‑ISAC | No optical layer | Lacks optical‑domain taxonomy |
| **[Ref B]** | 2022 | 6G Vision | Broad 6G trends | No systematic O‑ISAC extraction |
| **[Ref C]** | 2023 | Photonic Communications | Focus on pure optics | No joint sensing‑communication analysis |
| **This Survey** | 2024 | **O‑ISAC (Optical)** | **Comprehensive** | – |

*The table must be populated with actual references from your literature search (see `search/search_strings.md`).*  
**Critical Note**: Every COMST introduction includes a *Comparison Table* (Table I) that explicitly lists existing surveys and highlights the missing dimensions. Replicate this pattern.

## D. Contributions (Four‑fold List)
1. **A unified taxonomy** of O‑ISAC systems spanning fiber‑based, free‑space optical, and VLC/LiFi modalities.
2. **A systematic PRISMA‑compliant extraction** of 221 primary studies, including a 5‑dimensional TQAF quality assessment.
3. **Cross‑layer performance trade‑off analysis** (capacity vs. range resolution, power vs. latency) with visual taxonomy maps.
4. **Future‑roadmap** outlining research challenges (hardware integration, joint waveform design, AI‑driven adaptation) up to 2030.

*Adapt the wording to match your actual contributions; keep the “four‑fold” structure.*

## E. Organization (Structure Map)
> "The remainder of this survey is organized as follows. Section II describes the PRISMA methodology and data extraction pipeline. Section III presents the unified O‑ISAC taxonomy. Section IV details the physical‑layer design space (waveforms, hardware, channel models). Section V conducts a quantitative trade‑off analysis across the extracted studies. Section VI identifies open research challenges and proposes a roadmap. Finally, Section VII concludes the paper."

*Include a Figure 2 placeholder (e.g., `Fig. 2 – Survey organization diagram`).*

## F. Acronyms Table (Table II)
| Acronym | Definition |
|:---|:---|
| O‑ISAC | Optical Integrated Sensing and Communication |
| PRISMA | Preferred Reporting Items for Systematic Reviews and Meta‑Analyses |
| TQAF | Technical Quality Assessment Form |
| ... | ... |

*Populate with all domain‑specific abbreviations used throughout the manuscript.*

---

### 📌 Critical Implementation Guidance
1. **Maintain COMST‑style headings** (`I.`, `II.`, …) and lettered subsections (`A.`, `B.`, …).
2. **Every subsection must end with a concise “Lesson Learned” sentence** (e.g., *Lesson 1: Optical wavefront shaping is the key enabler for joint high‑rate sensing.*).
3. **Use the phrasebank** (`memory-bank/phrasebank.json`) for consistent academic voice – e.g., “To the best of our knowledge…”, “Despite significant progress…”.
4. **All tables/figures must be referenced in the text** and have a caption that starts with an active verb (e.g., *Table I summarizes…*, *Fig. 2 illustrates…*).
5. **Word‑budget**: keep the Introduction around 3.5–4 k words (≈10 % of total manuscript).

---

*This template is ready to be copied into `memory-bank/introduction_templates.md`. Fill the placeholders with your specific data, figures, and references.*
