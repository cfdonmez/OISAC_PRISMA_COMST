# Introduction Micro-templates & Analysis

## Standard COMST Introduction Structure
Most COMST introductions follow a structured sequence using lettered subsections (e.g., A, B, C, D).

### I. INTRODUCTION (Main Heading)
A. **Motivation** (The Hook + Societal/Technical Problem Statement)
B. **Related Works / Survey Comparisons** (The Gap Statement + Detailed Comparison Table)
C. **Key Contributions** (Numbered or Bulleted List)
D. **Structure of the Survey** (Structure Description + Organization Figure Reference)
*(Note: Some papers add an "E. Notations" or "E. List of Abbreviations" here, though Abbreviations often appear as Table I/II near the start.)*

---

## Detailed Component Templates

### 1. The Hook (Paragraphs 1-2)

**Pattern A: The "Evolution" Hook** (Historical)
- *Structure:* "Since the birth of [Field]..." or "With the continuous evolution of [Broad Field]..."
- *Example:* "Since the birth of quantum mechanics, humankind has developed..." (COMST_008)

**Pattern B: The "Societal/Trend" Hook** (Proliferation)
- *Structure:* "Today's world has become increasingly [Adjective]..." or "[Field] has seen a growing trend..."
- *Example:* "Vehicles have seen a growing trend in the utilization of sensors..." (COMST_010)

**Pattern C: The "Metric/KPI" Hook** (Standardization Driven)
> [!TIP]
> Use this for 6G or standard-centric topics.
- *Structure:* Reference to "6G visions", "IMT-2030", or specific KPIs (e.g., latency, reliability).
- *Example:* "Next-generation wireless (6G) promises a revolutionary leap... requiring seamless integration of sensing and communication." (COMST_015)

---

### 2. The Detailed Motivation (New Pattern)
Found in more recent/complex surveys (e.g., COMST_015).

- **Pattern: "The Shortage Checklist"**
  - *Intro:* "Existing paradigms fall short in [X] due to the following reasons:"
  - *Bullets:*
    - "Low Resource Utilization: [Explanation]"
    - "Mismatch between Module Goals: [Explanation]"
    - "Ignoring Tight Coupling: [Explanation]"

---

### 3. The Gap & Literature Comparison

**Pattern A: The "PRISMA-Style" Comparison**
- *Phrasing:* "While several surveys have explored [Topic X], they often lack [Feature Y]. To address this gap..."
- *Example:* "Table I compares this work with existing surveys in terms of [Criteria]..."

**Pattern B: The "Exhaustive Comparison Table"**
Every COMST survey must justify itself against existing literature using a comparison table.

| Reference | Year | [Criteria 1] | [Criteria 2] | [Features] | Focus Area | Limitations |
|-----------|------|--------------|--------------|------------|------------|-------------|
| [Ref A]   | 2020 | ✅           | ❌           | Partial    | [Topic A]  | No 6G focus |
| [Ref B]   | 2022 | ❌           | ✅           | ✅         | [Topic B]  | No O-ISAC   |
| **O-ISAC**| 2024 | ✅           | ✅           | ✅         | **Unified**| **Ours**    |

---

### 4. The Contribution (The "Fourfold" List)

- *Intro:* "The key contributions of this survey paper can be summarized as follows:"
- *Common Bullets:*
    - **Taxonomy:** "We provide a comprehensive and multi-dimensional **taxonomy** of [Topic]..."
    - **Comparative Analysis:** "We present a detailed **comparative analysis** of [Technologies]..."
    - **Architecture/Framework:** "We propose a unified **framework/system model** for [X]..."
    - **Future Directions:** "We identify **open issues** and propose **short-term and long-term research directions**."

---

### 5. The Organization (The Structure Map)

- *Structure:* Section-by-section breakdown + Explicit reference to a "Structure Figure".
- *Template:* "The overall structure of this survey, together with the relations between different sections, is presented in **Fig. 2**. Section II... Section III... Finally, Section IX concludes the paper."

### 6. The Acronyms Table (Standard Table I/II)
- Every COMST survey includes a dedicated table for acronyms, usually placed within Section I or II.
- **Template:**
| Acronym | Definition |
| :--- | :--- |
| 6G | Sixth Generation |
| ISAC | Integrated Sensing and Communication |
| ... | ... |

---

### 7. The Notations Section (Specialized Pattern)
Found in mathematically heavy surveys (e.g., COMST_027).
- **Subsection:** `E. Notations` (placed after Organization).
- **Template:** "Throughout this paper, scalars are denoted by... vectors by boldface lowercase... matrices by boldface uppercase... The expectation operator is denoted by $E[\cdot]$."

---

### 8. The "Lessons Learned" Pattern (Internal Section Summaries)
Observed in COMST_028, 029, 030 as a recurring "closing" for major technical sections.
- **Sub-subsection:** `E/F. Lessons Learned` or `Summary and Lessons Learned`.
- **Purpose:** Synthesize findings before moving to the next section.
- **Content:** Bullet points highlighting limitations, key takeaways, and specific open problems for that sub-domain.

---

## Writing Phraseology & Approaches

### 1. Critical Academic Moves (The "COMST" Voice)
Use these specific phrases to bridge the gap between "what exists" and "why your survey is needed."

- **The "Best of Our Knowledge" Move:**
  - *Phrase:* "To the best of our knowledge, this survey is the first to provide a comprehensive treatment of [X] from the perspective of [Y]."
  - *Approach:* Use this in Section I-C (Contributions) to assert authority.

- **The "Despite Efforts" Move:**
  - *Phrase:* "Despite significant research efforts in [Topic], a unified understanding of [Specific Problem] remains elusive."
  - *Approach:* Use this to transition from Background to Motivation.

- **The "Shortcoming" Move:**
  - *Phrase:* "A major shortcoming of existing literature is the lack of a systematic taxonomy/framework that addresses [Problem]."
  - *Approach:* Link this directly to your Comparison Table findings.

- **The "Forward-Looking" Move:**
  - *Phrase:* "We not only summarize the state-of-the-art but also provide a critical analysis of open issues that will shape the [Field] landscape toward 2030."

- **The "Contrastive Comparison" Move (Section B):**
  - *Phrases:* "Unlike [Ref 5], which focuses on [X]... we extend the scope to [Y]." or "In contrast to previous tutorials that primarily address [Z], this work treats [Topic] as a unified [Concept]."
  - *Approach:* Use these to explicitly reference rows in your comparison table.

- **The "Structural Roadmapping" Move (Section D):**
  - *Phrases:* "To guide the reader through this multifaceted subject, the remainder of this survey is structured as follows..." or "As depicted in the organization map in Fig. 1..."

### 2. Structural Connectors (The Flow)
Use these to link the lettered subsections seamlessly:

- **From A (Motivation) to B (Related Work):**
  - "Given these challenges, it is imperative to examine how existing literature has addressed [Topic]. To this end, Table I provides a comprehensive comparison..."
- **From B (Related Work) to C (Contributions):**
  - "Motivated by the identified gaps in existing surveys, particularly the lack of [X], this paper provides a unified treatment of [Y]."
- **From C (Contributions) to D (Organization):**
  - "The remainder of this survey is organized to systematically present these contributions, starting with the fundamental models in Section II."

### 2. Logical Approaches for Survey Drafting
- **Broad-to-Narrow:** Always start with the global trend (e.g., 6G, IoT) before diving into the specific sub-topic (e.g., O-ISAC).
- **The "Synergy" Argument:** For ISAC papers, emphasize that integration is not just "sharing resources" but "achieving mutual gain/synergy."
- **Visual-Text Interlock:** Never include a figure or table without at least one dedicated paragraph explaining how to read it.

---

## Micro-Templates for O-ISAC

### Template Set 1: Introduction Start (The Hook)
> **Option A (The 6G Vision):**
> "As 6G networks evolve towards the 'intelligence of everything,' **Optical ISAC (O-ISAC)** emerges as a transformative paradigm. By integrating information perception, transmission, and processing using optical resources, O-ISAC overcomes the spectrum scarcity and interference bottlenecks of traditional RF-ISAC..."

### Template Set 2: The Contribution Statement
> "To the best of our knowledge, this is the most comprehensive survey bridging the gap between fiber-based and wireless-based optical sensing-communication integration. Our contributions are fourfold: (i) a novel taxonomy..., (ii) a detailed comparison..., (iii) a systematic review of signal designs, and (iv) a roadmap for future 6G integration."

---

## Methodology & Analysis Findings
- **Analyzed Papers:** COMST_001 to COMST_030.
- **Validation Status:** 🏁 Fully Validated.
- **Key Trend (2023-2024):** 
    - **Multi-Level Comparisons:** Modern papers don't just compare with other surveys once; they include "Recent Literature" tables for *each* major contribution section (Sections III, IV, V...).
    - **Acronym Tables:** 100% presence in the first 2-4 pages.
    - **Organization Figures:** Always present (e.g., "Fig. 1/2. Organization of the survey").
    - **Systematic Structure:** Moving from a long introduction to a very technical "Preliminaries/System Model" (Section II) containing a **Taxonomy Map**.
    - **Lessons Learned:** High frequency in newer papers (at the end of each major section).
