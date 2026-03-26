# COMST Style Alignment Report for Section I-D

**Generated:** 2026-01-19  
**Purpose:** Document alignment between I-D outline and COMST writing assets

---

## 1. COMST Asset Files Used

| Asset Type | File Path |
|------------|-----------|
| Phrasebank | `analysis/pbank.json` |
| Master Recipe | `writing_recipes/COMST_master_recipe.md` |
| Intro Templates | `memory-bank/introduction_templates.md` |
| COMST Analysis Cards | `data/an_cards/v1.2/COMST_*.json` (76 files) |

---

## 2. Extracted COMST I-D Style Profile

### 2.1 Rhetorical Moves (from master_recipe.md, Section 1)

The canonical "Related Surveys" section follows this move sequence:

1. **Categorize** — Group existing surveys by scope/focus area
2. **Delimit Scope** — Describe what each survey covers and its boundaries
3. **Compare Coverage** — Use Table I/III to show coverage matrix
4. **Expose Gaps** — State what is missing using gap phrases
5. **State Contributions** — Bridge to contributions with "Our survey addresses..."

### 2.2 High-Frequency Phrase Templates (from phrasebank.json)

**Gap Identification Patterns:**
- "There is a lack of..." (27 instances in phrasebank)
- "To the best of our knowledge, no prior survey..." (18 instances)
- "Although extensive research..., there is still a lack of..."
- "However, they rarely..."
- "Unlike other research domains..."

**Comparison/Contrast Patterns:**
- "In contrast to [Ref], our work..."
- "While [Ref] focuses on [X], we address [Y]."
- "Existing surveys tend to be confined to..."

**Survey Verb Templates:**
- "surveys/summarizes/shows/provides" (top caption verbs)

**Transition Patterns:**
- "To address these gaps, this survey provides..."
- "The main contributions are summarized as follows:"

### 2.3 Quantitative Guidance (from master_recipe.md)

| Metric | COMST Guideline | I-D Target |
|--------|-----------------|------------|
| Word budget | ~10% of total (~4k words if 40k total) | ~600 words (condensed) |
| Must-have table | Survey comparison (Table I or III) | Table III exists |
| Caption verbs | "summarizes", "compares", "contrasts" | Applied |
| Citation density | 5-10 external surveys + internal | 5 external + 7 internal |

---

## 3. I-D Outline Alignment with COMST Moves

| I-D Paragraph | COMST Rhetorical Move | Alignment Status |
|---------------|----------------------|------------------|
| Para 1 (RF-ISAC context) | Categorize | ✅ Groups RF surveys |
| Para 2 (Fiber/DAS) | Delimit Scope | ✅ [O_ISAC_006], [O_ISAC_033] |
| Para 3 (VLC/LiFi) | Delimit Scope | ✅ [O_ISAC_068], [O_ISAC_327], [O_ISAC_039] |
| Para 4 (FSO/Photo-THz) | Delimit Scope | ✅ [O_ISAC_021], [O_ISAC_161] |
| Para 5 (Gap synthesis) | Expose Gaps | ✅ G1-G7 explicitly stated |
| Para 6 (Table III) | Compare + Contribute | ✅ Table III reference + bridge |

---

## 4. Gap-to-COMST-Phrase Mapping

| Gap ID | Recommended COMST Phrase |
|--------|--------------------------|
| G1 | "There is a lack of unified terminology bridging..." |
| G3 | "To the best of our knowledge, no prior survey provides cross-modality benchmarks..." |
| G5 | "Existing surveys tend to be confined to specific sub-domains, lacking a unified framework..." |
| G7 | "Critically, no existing work applies PRISMA systematic review methodology..." |

---

## 5. Table III Enhancement Checklist

The existing Table III (Section I-D, lines 136-147) should verify:

- [ ] All 7 O-ISAC survey-like works included
- [ ] Gap coverage columns (G1–G7) added or implicit in scope columns
- [ ] "PRISMA 2020" methodology highlighted for "This Survey" row
- [ ] ●●●●● coverage symbols consistent

---

## 6. Summary

The I-D outline skeleton follows COMST rhetorical conventions:
- **Move order:** ✅ Categorize → Delimit → Compare → Gaps → Contribute
- **Phrase templates:** ✅ Drawn from phrasebank
- **Table requirement:** ✅ Table III exists and is referenced
- **Gap statement patterns:** ✅ "There is a lack of...", "To the best of our knowledge..."

**Confidence:** High alignment with COMST style expectations.
