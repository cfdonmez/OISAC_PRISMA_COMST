# Section I-II Alignment Task List (COMST + PRISMA)

Owner: user + Codex
Scope: Section I (Intro) <-> Section II (Fundamentals)

## Tasks (ordered)

- [x] Update Section I organization sentence to reflect Section II scope (add metric contract + trade-off foundations).
  - Source: `drafts/section_01_introduction.md:165`
  - Target: `drafts/section_01_introduction.md:165`

- [x] Normalize Table II "Resolution" row to separate Delta r_min (wireless) vs Delta z (fiber).
  - Source: `drafts/section_01_introduction.md:62`
  - Target: `drafts/section_01_introduction.md:54-62`

- [ ] Add a short boundary note at the start of Section II:
  - Clarify that Section II uses theory-standard foundations + representative examples, and that PRISMA synthesis appears later.
  - Source: `drafts/section_02_fundamentals_draft.md:3-6`
  - Target: `drafts/section_02_fundamentals_draft.md:3-6`

## Notes
- Keep measurement-plane separation (OSNR vs electrical SNR) consistent with the metric governance rules.
  - Reference: `drafts/section_02_fundamentals_draft.md:20-24`

## Pre-Section III Checklist (Before Methodology Writing)

- [ ] Add explicit Research Questions (RQ1-RQ3) to Section I (PRISMA Item 4 / COMST objective clarity).
  - Source: `protocol/prisma_proto.md:63-70`
  - Target: `drafts/section_01_introduction.md` (place after motivation/gap framing; before contributions)

- [ ] Add inline evidence anchors for the three numeric exemplars in Section I (auditability):
  - Target: `drafts/section_01_introduction.md:15-20`
  - Evidence: `data/proc_markdowns/O_ISAC_105/O_ISAC_105/O_ISAC_105.md:11`, `data/proc_markdowns/O_ISAC_016/O_ISAC_016/O_ISAC_016.md:13`, `data/proc_markdowns/O_ISAC_046/O_ISAC_046.md:10`

- [ ] Decide whether Section II should include (a) a compact metric-contract table and/or (b) a single measurement-plane figure.
  - Reference governance: `analysis/II_met_gov.md:7-12`
  - Target location: `drafts/section_02_fundamentals_draft.md` (near II-A measurement-plane contract or II-D metric contract)

## COMST/PRISMA Basis (Local References)

- COMST + PRISMA writing guide (RQ visibility + visual dominance rules):
  - `review_package/surv_write_guide.md:11,26-36,54-55`

- Golden Model targets (visual density budgets + survey comparison table rule):
  - `review_package/goldenModel.md:13-20,117-122,139-142`

- COMST master recipe (fig/table must-haves; fundamentals should include an architecture/signal-flow figure):
  - `writing_recipes/COMST_master_recipe.md:5-7,20-23,38-41`
