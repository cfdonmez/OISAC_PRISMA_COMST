# COMST Jargon Checklist for Section VII Merge

## Source Basis
Checklist distilled from:
- `writing_recipes/COMST_master_recipe.md`
- `docs/surv_write_guide.md`
- `memory-bank/master_writing_guide.md`
- `memory-bank/introduction_templates.md`
- `memory-bank/body_section_templates.md`
- style anchor: `drafts/section6_20260217_143141/section_06_camera_ready.md`

## 1) Required Tone Cues (Keep/Prefer)

Use these cues to preserve COMST-style survey voice:
- **Survey-positioning cues:**
  - "In this survey, we..."
  - "To the best of our knowledge..."
  - "Despite recent progress..."
  - Sources: `memory-bank/master_writing_guide.md:320-323`, `docs/surv_write_guide.md:28-36`.
- **Contrast-and-synthesis transitions:**
  - "However, ...", "In contrast, ...", "Therefore, ...", "Consequently, ..."
  - Sources: `writing_recipes/COMST_master_recipe.md:44-47`, `docs/surv_write_guide.md:52-54`, `memory-bank/body_section_templates.md:14,21`.
- **Evidence-grounded technical verbs:**
  - prefer "characterizes", "quantifies", "mitigates", "enables" over vague verbs.
  - Source: `writing_recipes/COMST_master_recipe.md:47`.
- **Representative-evidence phrasing:**
  - "representative methods", "representative works", "as demonstrated by ..."
  - Sources: `writing_recipes/COMST_master_recipe.md:26`, `memory-bank/master_writing_guide.md:317`.
- **Engineering-tradeoff framing cue:**
  - "From an engineering perspective, the trade-off between ..."
  - Source: `memory-bank/body_section_templates.md:36-39`.
- **Active caption verbs (for figure/table mentions):**
  - "illustrates", "compares", "depicts", "surveys", "summarizes", "shows", "provides".
  - Sources: `memory-bank/master_writing_guide.md:310`, `writing_recipes/COMST_master_recipe.md:41`.

## 2) Forbidden or Fragile Phrasings

Treat the following as blocked or fragile unless tightly evidenced.

- **Blocked:** Annotated-bibliography style lists.
  - Avoid: "Paper [1] does X. Paper [2] does Y." or long citation dumps.
  - Sources: `memory-bank/body_section_templates.md:5-7`, `memory-bank/master_writing_guide.md:315-317`.
- **Fragile (require explicit proof/evidence):**
  - "we prove", "guarantees", "always", "optimal", "state-of-the-art".
  - Gate: only use if theorem/proof, benchmark protocol, or explicit quantitative evidence is present.
  - Sources: evidence-traceability requirements in `memory-bank/master_writing_guide.md:334-337`.
- **Fragile:** Unsupported quantitative uplift wording.
  - Avoid percentage or superiority claims without metric + source pairing.
  - Source: `memory-bank/master_writing_guide.md:336`.
- **Fragile:** Absolute authority claims without scope guard.
  - Example templates such as "first comprehensive survey" or "we pioneer" must be scoped and defended.
  - Source anchor: `memory-bank/master_writing_guide.md:322`.

## 3) Subsection Closing Style Expectations

For Section VII camera-ready merge, subsection endings should follow one of these COMST-consistent forms:
- **Preferred template form:** end each major subsection with a bold synthesis line:
  - `**Lesson X:** <one-line synthesized takeaway>`
  - Sources: `writing_recipes/COMST_master_recipe.md:26,46`, `memory-bank/master_writing_guide.md:325-327`, `memory-bank/introduction_templates.md:57`.
- **Camera-ready anchor form (accepted):** end with a compact evidence synthesis block:
  - `**Key takeaways and open problems.**` followed by evidence strength, current bottleneck, and 1-2 concrete open directions.
  - Source pattern: `drafts/section6_20260217_143141/section_06_camera_ready.md:58,75,92,120,137,160`.
- **Close in survey perspective, not theorem perspective:**
  - synthesize across studies; do not introduce ungrounded universal claims.
  - Sources: `writing_recipes/COMST_master_recipe.md:35-36,47`, `memory-bank/master_writing_guide.md:334-337`.

## 4) Merge-Time Jargon Gate (Quick Pass/Fail)

Apply this gate after concatenating VII-A..VII-G:
- PASS if transition and synthesis cues are present (However/In contrast/Therefore + representative evidence wording).
- PASS if no annotated-bibliography sentence pattern appears.
- PASS if all quantitative claims remain evidence-bound.
- PASS if each subsection ends with `Lesson` or `Key takeaways and open problems` style closure.
- FAIL if absolute certainty verbs appear without explicit evidence support.
