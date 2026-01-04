# COMST Survey Writing Model: The Blueprint 🧬

**Generated from 76 IEEE COMST Papers via Reverse Engineering**

This document serves as the "Writing Model" for your survey. It combines the canonical **Structure** (Skeleton) derived from statistical analysis of headings with a **Phrasebank** (Language) of real sentence templates extracted from the corpus.

---

## Part 1: The "Golden" Structure 🏗️

Analysis of 76 files reveals the standard flow of a successful COMST survey. 

### Standard Outline Flow
1.  **Introduction** (100% frequency)
    *   *Goal:* Define scope, importance, and contributions.
2.  **Related Work / Literature Review** (85% frequency)
    *   *Goal:* Critique existing surveys and define the gap.
3.  **System Model / Fundamentals** (83% frequency)
    *   *Goal:* Explain technical basics (e.g., Signal model, Architecture).
4.  **Technical Taxonomy / Solutions** (71% frequency)
    *   *Goal:* The "Meat" of the survey. Categorize and discuss solutions.
5.  **Challenges & Future Directions** (93% frequency)
    *   *Goal:* Speculate on open issues (Security, AI, 6G).
6.  **Conclusion** (100% frequency)

---

## Part 2: Academic Phrasebank (The "Skin") 🗣️

Use these templates to write like a native COMST author. **Do not copy exact text**, but use these structures.

### A. Setting the Scene (Trends & Importance)
*Use in Introduction - Paragraph 1*

*   "Recently, [Topic] has emerged as a promising technology for..."
*   "With the rapid development of [Technology], [Topic] has attracted significant attention."
*   "In recent years, the integration of [X] and [Y] has become a key enabler for..."
*   "Due to the emergence of [Standard/Requirement], traditional methods are no longer sufficient."
*   "Over the past decade, [Field] has witnessed a paradigm shift towards..."

### B. Defining the Problem (The "Hook")
*Use in Introduction - Paragraph 2 or 3*

*   "Although extensive research has been conducted on [X], there is still a lack of..."
*   "However, [Problem] remains a challenge due to..."
*   "One major issue is that existing solutions often neglect [Factor]."
*   "Despite these efforts, realizing [Goal] in practical scenarios is difficult."
*   "The main challenge lies in balancing [Trade-off A] and [Trade-off B]."

### C. Identifying the Gap (Why this survey?)
*Use in Related Work / Introduction*

*   "To the best of our knowledge, no existing survey comprehensively covers [Topic] considering [Constraint]."
*   "Existing surveys mainly focus on [Aspect A], ignoring [Aspect B]."
*   "Few studies have investigated the joint optimization of [X] and [Y]."
*   "In contrast to [Ref], which focuses on [X], our work provides a holistic view of..."
*   "However, these works do not provide a systematic classification of..."

### D. Stating Contributions (The "Promise")
*Use at end of Introduction*

*   "The main contributions of this survey are visualized in Fig. [X] and summarized as follows:"
*   "In this survey, we provide a comprehensive review of [Topic], focusing on [Focus]."
*   "Our objective is to provide a tutorial-style overview of..."
*   "We aim to bridge the gap between [Field A] and [Field B] by..."
*   "This paper presents a comprehensive taxonomy of [Topic] based on [Criteria]."

### E. Structuring the Paper (The "Map")
*Use at very end of Introduction*

*   "The remainder of this paper is organized as follows. Section II presents..."
*   "Section [X] describes the system model, while Section [Y] discusses..."
*   "In Section [Z], we discuss open challenges and future directions."

---

## Part 3: Writing Strategy Recommendations 💡

1.  **Don't Over-Simulate:** Only 31% of papers have a explicit "Performance Evaluation" section. Focus more on **Taxonomy** and **Qualitative Comparison** (Tables) than generating new simulation plots.
2.  **Visuals Matter:** successful papers average **18 figures** and **5 tables**. Ensure you have a "Taxonomy Diagram" early on.
3.  **Future is Key:** The "Challenges" section is present in 93% of papers. Dedicate significant space to this (not just 1 page).

---

## Part 4: The Art of the Gap (Buying Your Ticket) 🎟️

Every successful COMST paper must justify "Why another survey?". The analysis shows a standard methodology for this.

### 1. The "Yes, But..." Rhetoric
Don't trash previous work. Praise it, then limit it.
*   **Template:** "While [Ref] provides an excellent overview of [Topic X], it primarily focuses on [Old Standard] and neglects [New Trend]."
*   **Template:** "Although [Ref] discusses [Aspect A], it treats [Aspect B] as a black box."
*   **Template:** "Table I summarizes existing surveys. As observed, most works date back to [Year] or earlier, failing to capture the recent advances in [Generative AI/Semantics]."

### 2. The "Comparison Table" (Mandatory Ticket)
You **must** Include a "Comparison with Existing Surveys" table (usually Table I or II).

**Standard Table Template:**

| Ref. | Year | Scope / Focus | Contributions | Disadvantages / Limitations |
| :--- | :--- | :--- | :--- | :--- |
| [1] | 2021 | 5G Fundamentals | Overview of basic 5G NR architecture. | Lacks discussion on 6G and AI integration. |
| [2] | 2022 | Generic AI in 6G | Survey of ML algorithms for optimization. | Focuses only on physical layer; ignores semantic comms. |
| [3] | 2023 | Partial ISAC | Review of joint radar-comm prototypes. | Limited to hardware aspects; no security discussion. |
| **Ours**| **2026**| **Holistic Model** | **1) First survey on GenAI + Semantics<br>2) Full protocol stack analysis<br>3) Gap analysis of 76 papers** | **N/A (Comprehensive)** |

### 3. Winning Arguments (From our Gap Analysis)
Use these "Killer Differentiators" in your *Limitations* column (these are the things existing papers miss):
*   **"Lacks Security/Privacy discussion"** (Used in 14% of gap tables)
*   **"Narrow Focus (PHY only)"** (Common critique)
*   **"Outdated Standards"** (If paper is >3 years old)
*   **"No Implementation/Testbed review"** (If they are purely theoretical)

---

## Part 5: Physical Constraints (The "Budget") 📏

Based on the average of 76 published papers:

*   **Total Word Count:** ~36,000 words (This is huge! COMST papers are book-length).
*   **Visual Density:** 
    *   **Figures:** 19 per paper (Aim for 1 figure every ~1500 words).
    *   **Tables:** 12 per paper (Aim for 1 table every ~2500 words).

**Section Word Budgets (Target Lengths):**
1.  **Introduction:** ~4,300 words (Create a strong, extensive setup).
2.  **Related Work:** ~4,400 words (Don't skimp here; prove you read everything).
3.  **Core Technical Sections:** ~20,000 words (The "Meat").
4.  **Challenges & Future:** ~3,000 words.
5.  **Conclusion:** ~500 words.

---
**Next Steps:**
Use this document as your stylesheet. Copy the specific templates for your Introduction immediately.

---

## Part 6: Advanced Stylometrics (The "Soul") 🎨

Deep analysis of the corpus reveals the subtle "texture" of a top-tier paper.

### 1. Citation Freshness (The "Recency Test")
*   **Target:** **61%** of your references should be from the last 5 years (2020-2025).
*   **Action:** If your bibliography has 200 references, ensure at least **120** are recent. Old references risk the "Outdated" critique.

### 2. Visual Taxonomy (What to Draw?)
Don't just add random charts. The distribution of figure types in successful papers is:
*   **System Model / Scenario (20%):** Mandatory early in the paper. Show the "World" (e.g., Use Case Diagram).
*   **Performance Graphs (13%):** Only if you have simulations.
*   **Taxonomy/Hierarchy (4%):** Critical for the contribution section.
*   **Other (Flowcharts/Block):** The rest.

### 3. Paragraph Dynamics (Flow)
*   **Average Length:** 173 words (approx. 5-7 sentences).
*   **Topic Sentences:** Start paragraphs with strong, declarative definitions.
    *   *Bad:* "We can see that X is important."
    *   *Good:* "Full-duplex (FD) communication is a potential game changer for future wireless networks." (Direct Definition).

---

## Part 7: Micro-Rhetoric (The "Glue") 🔗

Analysis of 76 papers reveals the specific words used to stitch the paper together.

### 1. How to Cite a Table?
Don't say "Table I lists..." or "Table I shows...". The winners are:
*   **"Summarizes" / "Surveys":** Used 60% of the time. (e.g., "Table I summarizes the existing surveys.")
*   **"Provides":** Used 10% of the time.
*   **Avoid:** "Lists" (Too simple), "shows" (Too generic).

### 2. The Power of "However"
"However" appears **500+ times** in successful papers (approx 7 times per paper). Using it correctly is the key to the "Gap Selling" strategy.
*   **Usage:** Use it to pivot from "What exists" to "What is missing".
*   **Paragraph Ending:** Use "**Therefore**" or "**Consequently**" to wrap up a thought block.

### 3. Verification of Scope
*   **Data Source:** This model is derived from the full text analysis of **76 standardized COMST papers**.
*   **Consistency:** Every major claim in your paper must be backed by a reference or a table. The ratio of (Table Mentions : Actual Tables) should be exactly 1:1.




