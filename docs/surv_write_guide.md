# O-ISAC Survey Writing Guide (IEEE COMST & PRISMA 2020)

| Tarih | Revizyon | Açıklama |
|-------|----------|----------|
| 2026-01-05 | v1.0 | İlk taslak oluşturuldu. IEEE COMST ve PRISMA 2020 temelleri atıldı. |
| 2026-01-07 | v1.1 | Abstract ve Introduction analiz sonuçlarına göre şablonlar güncellendi. |
| 2026-01-10 | v1.2 | "Non-list" sentez stratejisi ve Metodoloji rigor (TQAF) detayları eklendi. |

**Target Journal:** IEEE Communications Surveys & Tutorials (Impact Factor: ~35)
**Standard:** PRISMA 2020 Statement
**Purpose:** This guide serves as a bridge between the `prisma_proto.md` and the final manuscript, ensuring every section meets both the rigorous reporting standards of PRISMA and the tutorial-style depth required by COMST.

---

## 0. Abstract (The "Storefront")

**Goal:** Sell the paper in <30 seconds.
**COMST Requirement:** Strict 200-250 word limit. No references usually.

*   **Structure (The Golden Formula):**
    1.  **Context:** "With the rapid development of [Trend]..."
    2.  **Gap:** "**However**, existing solutions ignore [X]..."
    3.  **Solution:** "In this paper, we present the first unified survey..."
    4.  **Future:** "**Finally**, we outline open challenges..."

## 1. Introduction (PRISMA Item 3 & 4)

**Goal:** Establish the "Why" and "What".
**COMST Requirement:** Must justify why a *new* survey is needed (Gap Analysis of existing surveys).

*   **Rationale (Item 3):**
    *   Start with the broad context: 6G, ISAC, and the "Optical Spectrum" opportunity.
    *   **CRITICAL:** Table comparing *existing surveys* vs. *this survey*. Highlight that previous works focus only on RF, only on Fiber, or only on VLC. This is the first "Unified Physical Layer" review.
*   **Objectives (Item 4):**
    *   Explicitly state the Research Questions (RQ1-RQ3 form Protocol).
    *   Outline the structure of the paper (using the Sunburst Taxonomy concept).

## 2. Methodology (The "Shield" - PRISMA 2020)

**Goal:** Defend your rigor and uniqueness.
**Action:** Follow the three-phase screening workflow described in `memory-bank/methodology_template.md`.

*   **Standard Opening:** "This systematic review was conducted in strict accordance with the **PRISMA 2020** guidelines [Ref]."
*   **Search Rigor:** Explicitly list databases (IEEE, WoS, Scopus) and the Boolean search strings.
*   **Quality Appraisal:** Mention the **Technical Quality Assessment Form (TQAF)** used to score the 221 included studies. This proves you didn't just find papers, but evaluated them.

## 4. Main Synthesis (The "Non-List" Strategy)

**Goal:** Provide a tutorial-style synthesis, not a list of summaries.
**Action:** Use templates from `memory-bank/body_section_templates.md`.

*   **Grouping:** Cluster papers by **Problem/Challenge** (e.g., "Non-linearity mitigation") or **Architecture** (e.g., "Full-duplex ISAC").
*   **The "However" Pivot:** Use "However" or "In contrast" to transition between different technical schools of thought.
*   **Visual Dominance:** Every major section MUST have a comparison table. Refer to the **Golden Model** for visual density standards (Target: 18-22 figures).

## 6. Performance Trade-offs (Quantitative Synthesis)

**Goal:** The "Engineer's Discussion". Use the data extracted in `tradeoff` fields.

*   **Metrics:** Data Rate (Gbps) vs Sensing Accuracy (RMSE).
*   **Visuals:**
    *   **Bubble Chart:** X-axis = Range, Y-axis = Data Rate, Bubble Size = Resolution.
    *   **Pareto Frontiers:** Discuss studies that explicitly show the trade-off curve (like `O_ISAC_029`).
*   **Discussion:**
    *   "Resource Division (TDM) creates a hard trade-off (linear loss)."
    *   "Joint Waveforms offer better spectral efficiency but higher complexity."

## 7. Open Challenges and Research Roadmap (PRISMA Item 23)

**Goal:** Guide future research.

*   **Emerging Hardware:** Optical RIS, OPA, Photonic Integrated Circuits.
*   **Methodological Gaps:** Lack of standardized datasets, inconsistency in channel modeling assumptions (identified via TQAF).
*   **6G Integration:** How O-ISAC fits into the larger 6G ecosystem.

---

## Appendix
*   **Search Strings (Item 7):** Full query strings.
*   **Excluded Studies List (Item 16b):** Good practice for full transparency.
