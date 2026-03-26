# Section V Correction Notes (Consistency Pass)

Owner: user + Codex  
Date: 2026-02-15  
Scope: Section I (Intro) <-> Section V (Trade-off Synthesis)

## Tasks (ordered)

- [ ] Resolve figure-index conflict for `Fig. 4`.
  - Issue: Section I already uses `Fig. 4` for survey organization, while Section V-A also references `Fig. 4` for performance visualization.
  - Source (Section I): `drafts/section_01_introduction.md:163`, `drafts/section_01_introduction.md:181`
  - Target (Section V-A): `drafts/section_05_template.md:5`, `drafts/section_05_template.md:11`
  - Proposed fix: rename the Section V performance anchor to `Fig. 5` (or final global figure index decided at camera-ready stage).

- [ ] Add explicit scope note to avoid study-level vs scenario-level count confusion.
  - Issue: Section I contributions use study-level corpus counts, while Section V-A reports scenario-level governed subset statistics.
  - Source (study-level statement): `drafts/section_01_introduction.md:153`
  - Target insertion point (Section V-A): `drafts/section_05_template.md:7`
  - Proposed fix: add one sentence such as "Unless explicitly stated otherwise, Section V reports scenario-level governed records rather than corpus-level study counts."

## Notes

- Keep governance language consistent with Section II contract: OSNR (optical plane) and SNR/ESNR (electrical plane) must remain separated.
- Keep metric-role separation explicit: `drmin` is not interchangeable with `dz`; CRQ statements remain restricted to eligible records.

## COMST Deliverables Checklist (Section V)

- [ ] Keep Section V synthesis tutorial-style (not paper-by-paper), with paragraph flow: context -> quantitative finding -> comparison -> caveat.
- [ ] Keep all quantitative claims traceable to `analysis/V_ev_v2/*` evidence files.

- [ ] Table V (Communication Metrics): add reported vs governance-usable coverage, plane-separated quality (OSNR vs SNR/ESNR), and medium-conditioned rate summaries.
- [ ] Table VI (Sensing Metrics): add role-separated coverage (`drmin`, `sigma_r`, `CRB`, `dz`), with explicit usability after governance filters.
- [ ] Table VII (Trade-off/Pareto): add point partitions (`total`, `CRQ-candidate`, `CRQ-valid`, `Pareto`) and coupling-mode coverage with sample-size caveats.
- [ ] Add sample-size columns in tables to prevent over-interpretation of sparse media slices.

- [ ] Figure anchor consistency: resolve the current `Fig. 4` cross-section conflict before camera-ready numbering.
- [ ] Fig. 4 should visualize governed operating clouds with role/plane separation (not pooled raw points).
- [ ] Fig. 5 should present Pareto/frontier points as sparse illustrative evidence, not a population-stable envelope.

- [ ] CRQ statements in Section V must remain restricted to CRQ-eligible records only.
- [ ] No `dz`-to-`drmin` substitution in any table, figure, or narrative claim.
