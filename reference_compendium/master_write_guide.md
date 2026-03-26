# O-ISAC Survey: Master Writing Guide
**IEEE COMST-Compliant Writing Templates**

> **Purpose:** This master guide consolidates all micro-templates developed from the analysis of 76 COMST papers. Use this as your primary reference when drafting any section of the O-ISAC survey.

---

## 📚 Table of Contents
1. [Abstract Template](#1-abstract-template)
2. [Introduction Template](#2-introduction-template)
3. [Methodology Template](#3-methodology-template)
4. [Body Section Templates](#4-body-section-templates)
5. [Conclusion Template](#5-conclusion-template)
6. [Universal Writing Rules](#6-universal-writing-rules)

---

## 1. Abstract Template

### The "Golden Abstract Formula" (5 Blocks, ~200-250 words)

#### Block 1: The Contextual Hook [1-2 sentences]
**Goal:** Define the current phase of the technology or the demand.

**Premium Phrasing:**
- "The next phase of [X] technology is being characterized by..."
- "The ever-increasing demand for ubiquitous and differentiated services emphasizes the necessity of [X]..."
- "Recent advances in... have opened new opportunities..."
- "As [domain] continues to evolve..."

**O-ISAC Example:**
> "The next phase of 6G wireless communication is being characterized by the integration of sensing and communication (ISAC). While RF-based systems are nearing theoretical limits, **Optical ISAC (O-ISAC)** emerges as a transformative paradigm for ultra-high-speed and high-precision connectivity."

---

#### Block 2: The Bottleneck/Gap [1-2 sentences]
**Goal:** Explain why current solutions or surveys are insufficient.

**Premium Phrasing:**
- "However, the inherent [Complexity/Heterogeneity/Dynamics] of [X] constraint the materialization of these potentials..."
- "Existing surveys are either limited to or specific to particular topics and lack a comprehensive overview of..."
- "Despite recent progress, [problem] remains a critical challenge..."
- "To the best of our knowledge, no survey simultaneously covers..."

**O-ISAC Example:**
> "**However**, the O-ISAC research landscape remains fragmented across disjoint domains such as fiber sensing, VLP, and FSO ranging, which constraints the unified design of 6G networks."

---

#### Block 3: The Authority Claim [1 sentence]
**Goal:** Assert the paper's uniqueness and importance.

**Premium Phrasing:**
- "To understand the latest development and ultimately open new research niches on this significant topic, this survey is the **pioneer paper** to serve as a systematical and comprehensive overview..."
- "This is the **first-of-its-kind** survey to systematically review literature in both [A] and [B] scenarios."
- "We present the first systematic analysis of..."

**O-ISAC Example:**
> "To bridge this gap, this paper is the **pioneer work** to serve as a systematic and comprehensive overview of the entire O-ISAC ecosystem."

---

#### Block 4: Detailed Content Breakdown [2-3 sentences]
**Goal:** List the specific domains covered (PHY, MAC, Architecture, etc.).

**Premium Phrasing:**
- "We **start** with a profound discussion about..."
- "**Furthermore**, we make an in-depth literature overview across [A], [B], and [C]..."
- "**Moreover**, we analyze..."
- "**Finally**, we present..."

**O-ISAC Example:**
> "We start with a profound discussion of the physical layer fundamentals and hardware enablers. Furthermore, we provide a systematic review based on **PRISMA** guidelines, analyzing 221 recent studies to categorize multi-tier integration architectures."

---

#### Block 5: The Exit/Vision [1 sentence]
**Goal:** Reference the roadmap and future impact.

**Premium Phrasing:**
- "Finally, we outline research challenges and future directions focusing on [Trend]."
- "This work paves the way for..."
- "We conclude by identifying future research directions..."

**O-ISAC Example:**
> "**Finally**, we identify fundamental performance trade-offs and outline future research directions for achieving seamless optical convergence in the 6G era."

---

## 2. Introduction Template

### Structure (4,500 words, ~10% of manuscript)

#### A. Hook (Motivation)
**Choose one of three patterns:**

**Pattern A – 6G Vision Hook:**
> "As 6G networks evolve towards the *intelligence of everything*, **Optical Integrated Sensing and Communication (O‑ISAC)** emerges as a transformative paradigm that unifies perception, transmission, and processing on optical carriers. This integration addresses the spectrum scarcity and interference bottlenecks of traditional RF‑ISAC and enables ultra‑high data‑rate, low‑latency, and high‑resolution sensing for emerging verticals such as smart factories, autonomous vehicles, and holographic telepresence."

**Pattern B – Spectrum‑Crisis Hook:**
> "The explosive growth of mobile‑data traffic and high‑resolution sensing applications has created an unprecedented demand for spectrum resources. Optical carriers (fiber, VLC, LiFi, FSO) offer orders‑of‑magnitude larger bandwidths, making them the natural substrate for the next generation of joint sensing‑communication systems."

**Pattern C – Convergence Trend Hook:**
> "Recent standards (IEEE 802.11be, 3GPP NR‑ISAC, ITU‑6G) are converging on the idea that *sensing* and *communication* should share the same physical layer. O‑ISAC is the concrete realization of this trend, leveraging photonic components, wavelength‑division multiplexing, and coherent detection to achieve simultaneous high‑capacity data transfer and precise environmental awareness."

---

#### B. Overview of O‑ISAC (Technical Context)
- **Physical‑Layer Convergence**: shared waveform, shared hardware (laser/LED sources, photodetectors), joint spectrum allocation.
- **Key Enabling Technologies**: Photonic Integrated Circuits (PIC), Spatial‑Division Multiplexing (SDM), Optical Beamforming, Machine‑Learning‑assisted channel estimation.
- **Application Domains**: 6G wireless back‑haul, vehicular networks, indoor positioning, distributed acoustic sensing, quantum‑enhanced metrology.

**Example Sentence:**
> "With the continuous evolution of wireless networks, the integration of sensing and communication over optical carriers provides a unified solution for high‑throughput, low‑latency services."

---

#### C. Related Surveys (Gap Analysis)
**CRITICAL:** Every COMST introduction includes a *Comparison Table* (Table I) that explicitly lists existing surveys and highlights the missing dimensions.

| Survey | Year | Scope | O‑ISAC Coverage | Gap |
|--------|------|-------|----------------|-----|
| **[Ref A]** | 2020 | RF‑ISAC | No optical layer | Lacks optical‑domain taxonomy |
| **[Ref B]** | 2022 | 6G Vision | Broad 6G trends | No systematic O‑ISAC extraction |
| **[Ref C]** | 2023 | Photonic Communications | Focus on pure optics | No joint sensing‑communication analysis |
| **This Survey** | 2024 | **O‑ISAC (Optical)** | **Comprehensive** | – |

---

#### D. Contributions (Four‑fold List)
1. **A unified taxonomy** of O‑ISAC systems spanning fiber‑based, free‑space optical, and VLC/LiFi modalities.
2. **A systematic PRISMA‑compliant extraction** of 221 primary studies, including a 5‑dimensional TQAF quality assessment.
3. **Cross‑layer performance trade‑off analysis** (capacity vs. range resolution, power vs. latency) with visual taxonomy maps.
4. **Future‑roadmap** outlining research challenges (hardware integration, joint waveform design, AI‑driven adaptation) up to 2030.

---

#### E. Organization (Structure Map)
> "The remainder of this survey is organized as follows. Section II describes the PRISMA methodology and data extraction pipeline. Section III presents the unified O‑ISAC taxonomy. Section IV details the physical‑layer design space (waveforms, hardware, channel models). Section V conducts a quantitative trade‑off analysis across the extracted studies. Section VI identifies open research challenges and proposes a roadmap. Finally, Section VII concludes the paper."

**Include:** Fig. 2 – Survey organization diagram

---

#### F. Acronyms Table (Table II)
| Acronym | Definition |
|:---|:---|
| O‑ISAC | Optical Integrated Sensing and Communication |
| PRISMA | Preferred Reporting Items for Systematic Reviews and Meta‑Analyses |
| TQAF | Technical Quality Assessment Form |
| VLC | Visible Light Communication |
| FSO | Free-Space Optical |
| DAS | Distributed Acoustic Sensing |

---

### 📌 Critical Implementation Guidance for Introduction
1. **Maintain COMST‑style headings** (`I.`, `II.`, …) and lettered subsections (`A.`, `B.`, …).
2. **Every subsection must end with a concise "Lesson Learned" sentence** (e.g., *Lesson 1: Optical wavefront shaping is the key enabler for joint high‑rate sensing.*).
3. **Use the phrasebank** for consistent academic voice – e.g., "To the best of our knowledge…", "Despite significant progress…".
4. **All tables/figures must be referenced in the text** and have a caption that starts with an active verb (e.g., *Table I summarizes…*, *Fig. 2 illustrates…*).
5. **Word‑budget**: keep the Introduction around 3.5–4k words (≈10% of total manuscript).

---

## 3. Methodology Template

### 🛡️ Purpose: The "Shield"
Unlike the Introduction (which sells the "Why"), the Methodology section defends the "How".

**Key Insight:** Analysis of 25 COMST papers reveals that <5% use a formal PRISMA methodology.
- **Implication:** This section will be a major differentiator, proving that your survey is not just a "narrative review" but a scientifically rigorous "systematic review".

---

### 📋 PRISMA 2020 Checklist Alignment
This template covers **Items 5-15** of the PRISMA checklist.

| Item | Topic | Our Implementation |
|:---:|---|---|
| 5 | Eligibility Criteria | "Inclusion/Exclusion" Subsection |
| 6 | Information Sources | "Data Sources" (IEEE, WoS, etc.) |
| 7 | Search Strategy | "Search Strings" Boolean Logic |
| 8 | Selection Process | "Screening" (3-Phase Flow) |
| 10 | Data Items | "Taxonomy Definition" |
| 11 | Risk of Bias | "Quality Assessment" (TQAF) |

---

### 🏗️ Micro-Templates (Boilerplate)

#### 1. The Opening Statement (Standard of Rigor)
> "**Methods:** This systematic review was conducted in strict accordance with the **Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) 2020** guidelines [Ref]. To ensure reproducibility and minimize selection bias, a formal protocol was developed and registered prior to the literature search."

---

#### 2. Search Strategy (Item 6 & 7)
> "**Search Strategy:** We performed a comprehensive search across four major academic databases: **IEEE Xplore, Web of Science, ACM Digital Library, and Scopus**. The search covered the period from **January 2010 to December 2025**. We employed a multi-string Boolean search strategy combining keywords from two primary domains:
> - *Set A (Sensing):* ("Integrated Sensing and Communication" OR "ISAC" OR "Joint Radar and Communication") AND
> - *Set B (Optical):* ("Optical Wireless" OR "VLC" OR "LiFi" OR "FSO" OR "Fiber Sensing")."

---

#### 3. Eligibility Criteria (Item 5)
> "**Inclusion and Exclusion:** A study was included if it: (1) proposed a physical-layer integration of optical sensing and communication, (2) was published in a peer-reviewed journal or conference, and (3) provided quantitative performance metrics.
> 
> Conversely, studies were excluded if they: (1) focused solely on RF-based ISAC without an optical component, (2) were non-English publications, or (3) were abstract-only or review papers."

---

#### 4. Selection & Quality Assessment (Item 8 & 11)
> "**Study Selection:** The selection process followed a **three-phase screening workflow**: (1) Title/Abstract screening, (2) Full-text eligibility assessment, and (3) Quality appraisal.
> 
> To assess the methodological quality of the included studies, we developed a custom **Technical Quality Assessment Form (TQAF)** adapting the CASP checklist for engineering surveys. Each study was scored based on the clarity of its system model, the reproducibility of its simulation environment, and the completeness of its performance analysis."

**CRITICAL:** Include **Fig. 2: PRISMA Flow Diagram** showing the screening stages.

---

## 4. Body Section Templates

### 🎯 "Non-List" Writing Policy
**Never Do:** "Paper [1] did this. Paper [2] did that." (Annotated Bibliography style).
**Always Do:** Group papers by problem, methodology, or result axis.

---

### 🏗️ Template 1: Challenge-Based Synthesis
Use when explaining how a technical challenge was overcome (e.g., Non-linearity in fibers).

> "Managing **[Challenge Name]** is critical for joint sensing and communication in [System Type]. Early attempts primarily focused on [Category 1: e.g., Digital Compensation], where [Ref A, B] utilized [Technique]. However, these approaches often suffer from [Limitation]. To address this, a more recent trend involves [Category 2: e.g., All-optical Processing], as demonstrated by [Ref C], achieving [Result]. Table [X] provides a comprehensive comparison of these strategies based on complexity and accuracy."

---

### 🏗️ Template 2: Technology/Architecture Synthesis
Use when comparing different architectures (e.g., VLC vs FSO ISAC).

> "The architectural landscape of [Domain] O-ISAC is bifurcated into [Type 1] and [Type 2]. While [Type 1] architectures ([Ref 1, 2]) excel in [Metric A], they are inherently limited by [Metric B]. In contrast, [Type 2] designs ([Ref 3-5]) leverage [Key Component] to bridge this gap. Fig. [Y] illustrates the unified system model that encompasses both paradigms, highlighting the common hardware enablers such as [Component]."

---

### 📊 Visual Standards for Body Sections
Each major section (Fiber, Wireless, FSO) must include two visual elements:

1. **Unified System Model (Diagram):** A block diagram showing the common denominator of all reviewed papers.
2. **Summary Table (Comparison Table):**
   - **Columns:** Reference, Integration Level, Key Sensing Metric, Key Comm Metric, Implementation (Sim/Exp).
   - **Rows:** Use "cluster" rows for similar paper groups instead of individual papers.

---

### 🔑 Engineer's Perspective (Trade-off Analysis)
At the end of each major technology heading, include this pattern:

> "From an engineering perspective, the trade-off between [Metric 1] and [Metric 2] remains the primary optimization constraint. As visualized in the **Pareto Frontier (Fig. Z)**, increasing sensing resolution by [X]% typically incurs a [Y]% loss in spectral efficiency when using [Scheme Name]."

---

## 5. Conclusion Template

### The "Receipt" Formula (3 Blocks, ~150-250 words)

#### Block 1: The Restatement (The Goal) [1 sentence]
**Goal:** Re-affirm why the survey was conducted.

**Pattern:**
- "In this survey, we have presented the **first unified overview** of..."
- "This paper has explored the potentially promising methodologies in..."

**O-ISAC Example:**
> "In this article, we have presented the **first unified survey** on O-ISAC, bridging the technological gap between fiber-based sensing and optical wireless communication systems."

---

#### Block 2: The Summary (The Delivery) [2-3 sentences]
**Goal:** Recount the taxonomy, analysis, and challenges provided.

**Pattern:**
- "Specifically, we first established... Then, we proposed a **comprehensive taxonomy**... Furthermore, we analyzed..."

**O-ISAC Example:**
> "Specifically, we first established a fundamental understanding of optical channel models and hardware enablers. Then, we proposed a comprehensive **taxonomy** that categorizes O-ISAC into cabled and wireless domains, analyzing contributions from over 200 studies. Furthermore, we provided a **comparative analysis** of performance metrics, highlighting the trade-offs between sensing resolution and data rate."

---

#### Block 3: The Vision (The Exit) [1 sentence]
**Goal:** Final forward-looking statement.

**Pattern:**
- "Hopefully, this survey will serve as a foundational roadmap for researchers aiming to unlock..."
- "We envision that this work will enable..."

**O-ISAC Example:**
> "Hopefully, this survey will serve as a foundational roadmap for researchers aiming to unlock the full potential of the optical spectrum in the **6G** era, fostering a truly integrated sensing and communication ecosystem."

---

## 6. Universal Writing Rules

### ✅ COMST Golden Standards

#### 1. Structural Requirements
- **Headings:** Use Roman numerals for sections (`I.`, `II.`, `III.`) and capital letters for subsections (`A.`, `B.`, `C.`).
- **Figures:** 16-22 figures per survey (average: 18).
- **Tables:** 10-12 tables per survey.
- **Word Count:** 35,000-40,000 words total.

#### 2. Visual Requirements
- **Every figure/table MUST be referenced in text** before it appears.
- **Captions start with active verbs:** "Fig. 1 illustrates...", "Table II compares...", "Fig. 3 depicts...".
- **Include at least one "taxonomy diagram"** (sunburst, hierarchical tree, or Venn diagram).
- **Include PRISMA Flow Diagram** in Methodology section.

#### 3. Citation Style
- **Avoid citation lists:** Don't write "[1, 2, 3, 4, 5] proposed...".
- **Group by contribution:** "Several works [1-5] have addressed... Among these, [2, 4] specifically focused on...".
- **Use narrative citations:** "As demonstrated by Smith et al. [12], the integration of...".

#### 4. Academic Voice (Premium Phrasing)
- **Gap identification:** "To the best of our knowledge, no prior work has..."
- **Transition words:** "Furthermore,", "Moreover,", "In addition,", "Specifically,", "Finally,".
- **Authority claims:** "This is the first comprehensive survey to...", "We pioneer the...".
- **Limitations:** "However, these approaches suffer from...", "Despite recent progress...".

#### 5. Lesson-Learned Pattern
At the end of each major subsection, include a synthesizing sentence:
> "**Lesson 1:** Optical wavefront shaping is the key enabler for joint high-rate sensing."

#### 6. Acronym Management
- **First use:** "Optical Integrated Sensing and Communication (O-ISAC)".
- **Subsequent uses:** "O-ISAC".
- **Include acronym table** in Introduction (Table II).

#### 7. Reproducibility Requirements
- **All claims must be traceable** to either extracted data or cited references.
- **Quantitative statements require evidence:** "Increasing resolution by 20% incurs a 15% loss in data rate [Ref X]."
- **Include methodology details** sufficient for replication.

---

## 📋 Section-by-Section Checklist

### Before Writing Any Section:
- [ ] Identify the section type (Hook, Gap, Taxonomy, Trade-off, etc.)
- [ ] Select the appropriate template from this guide
- [ ] Gather all relevant extracted data and references
- [ ] Plan visual elements (figures/tables)

### While Writing:
- [ ] Follow the micro-template structure
- [ ] Use premium phrasing from the phrasebank
- [ ] Group papers thematically, not as lists
- [ ] Reference all figures/tables in text
- [ ] Include lesson-learned statements

### After Writing:
- [ ] Verify word count matches budget
- [ ] Check all acronyms are defined
- [ ] Ensure all citations are narrative-style
- [ ] Confirm all figures/tables have active-verb captions
- [ ] Cross-reference with COMST examples

---

## 🎯 Quick Reference: Section Word Budgets

| Section | Words | % | Key Template |
|---------|-------|---|--------------|
| Abstract | 200-250 | - | 5-Block Formula |
| I. Introduction | 4,500 | 12.5% | Hook → Gap → Contributions |
| II. Fundamentals | 5,000 | 13.9% | Tutorial-style |
| III. Methodology | 2,500 | 6.9% | PRISMA Shield |
| IV. Taxonomy | 8,000 | 22.2% | Architecture Synthesis |
| V. Performance | 4,000 | 11.1% | Trade-off Analysis |
| VI. Enabling Tech | 3,500 | 9.7% | Technology Synthesis |
| VII. Applications | 3,000 | 8.3% | Scenario-driven |
| VIII. Future | 4,500 | 12.5% | Challenge-based |
| IX. Conclusion | 500 | 1.4% | Receipt Formula |
| **Total** | **35,500** | **98.5%** | - |

---

## 📚 Related Resources

- **Phrasebank:** `memory-bank/phrasebank.json` (if available)
- **Survey Outline:** `memory-bank/surveyOutline.md`
- **Golden Model:** `memory-bank/goldenModel.md`
- **PRISMA Protocol:** `protocol/prisma_proto.md`
- **Extraction Schema:** Referenced in PRISMA protocol

---

> [!IMPORTANT]
> **This master guide is your single source of truth for writing.** Every sentence in your O-ISAC survey should be traceable to a template or pattern documented here. When in doubt, consult COMST examples and update this guide accordingly.

---

**Last Updated:** 2026-01-15  
**Version:** 1.0  
**Status:** Ready for production use
