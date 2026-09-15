# Whole-manuscript revision

Author instruction: 16 September 2026. Working branch: `rev/flow-20260916`.
Reference: `0d5d6f869336266fde80d8e9ad829108c29b1c7e`, archived in `../archive/base.zip`.

## Reader's path

| Section | Question answered | Depends on | Carries forward |
|---|---|---|---|
| I | Why combine these optical platforms in one review, and how was evidence selected? | Related surveys; frozen selection records | Three technical contributions and concise PRISMA method |
| II | Where does the target affect the signal, what can be shared, and what do the outputs measure? | Physical observation models | Signal planes, resource constraints, metric meanings |
| III | How does each physical path constrain the available architecture choices? | II | Shared component or resource and limiting impairment |
| IV | How does varying that choice change communication and sensing? | II–III; source-level relations | Supported within-study mechanisms with conditions |
| V | Under what validation conditions were those outcomes established? | IV; study appraisal | Joint evidence, environment dependence, reconstruction limits |
| VI | Which application conditions challenge the demonstrated design? | III–V | Traffic, mobility, geometry, timing and control requirements |
| VII | Which experiments would resolve the resulting uncertainties? | IV–VI | Testable questions, perturbations, paired outputs and baselines |
| VIII | What has the survey established? | The actual synthesis | Findings and their supported limits |

## Editorial decisions

- Retain eight sections: methodology has already moved into I-C. Remove redundant explanation within the remaining structure rather than deleting architecture analysis merely because an old Section III was methodological.
- Keep the concise method and truthful scientific limits in their agreed locations. No cover-letter, AI workflow, internal approval or project QA prose in the article.
- Consolidate the opening platform tour into the physical signal-path explanation. Replace raster signal-path and resource diagrams with editable vectors. Remove the standalone graph of a formula already explained numerically.
- Replace equal-weight architecture cards and the numbered technology chain with a mechanism figure and application experiments table. Counts do not imply causal strength or a mandatory technology sequence.
- Move detailed metric, relationship, appraisal and application inventories into an accessible scientific supplement. Frozen records remain unchanged.
- Correct 118 to conditional comparison candidates; do not imply verified independent cross-study relations. Zero padding changes a sampling/interpolation grid, not the information-limited physical resolution.
- Preserve within-study measurement conditions, power budget definitions, separate versus joint experiments, and the 12-field/6-both-domain distinction. A logical engineering chain is not a pooled causal estimate.
- Check every revised figure at actual article width and inside the final PDF. Page target is 20–30 including references; do not manufacture evidence or discard essential limits to reach a count.

## Completion checks

All eight sections and the Abstract were revised. The article now has 20 pages,
five figures and seven tables; detailed evidence profiles have a separate
six-page scientific carrier. Source/claim and contribution-to-body audits,
build checks and full-page visual review are recorded in `qa/flow/result.json`
and [compare.md](../compare.md). The main PDF has seven inspected underfull
notices and no overfull boxes or unresolved citations/references.

## Reporting locations

These are reporting destinations, not a completed independent PRISMA checklist.

| Content | Current article | Scientific detail |
|---|---|---|
| Eligibility and search sources/dates | I-C | `supplement/methods.md`; S-Search, S-Protocol |
| Selection process and result | I-C, Fig. 1 | ST-01, S-Exclusions, methods and source records |
| Extraction and analysis units | I-C summary | Methods, S-Data Dictionary, S-Evidence, supplementary profiles |
| Metric meaning and synthesis | II and IV | Methods, S-Core, S-Evidence, S-Bodies |
| Technical appraisal and limits | V-C; VII-C | S-Appraisal, S-Protocol, full profile in supplementary Fig. S2 |
| Field evidence in both domains | V-A/B, Fig. 5 | S7, source locators and timing fields |
| Registration/conduct history | Archive access in I-C | Supplementary methods and S-Protocol |
| Materials access | I-C OSF footnote | `supplement/index.md` and linked carriers |
| Limits and nonperformed analyses | VII-C | Supplementary methods and S-Protocol |

## New explanatory relation

VI-B adds an illustrative, sequential observation-age budget and a small-angle
motion relation. Assumptions: the estimate is referenced to acquisition start,
relative transverse velocity is constant, range is nearly fixed, and no motion
prediction is applied. An overlapped pipeline uses actual reference-to-actuation
age. This supplies a physical explanation for the timing requirement; it is
not a fitted corpus result or a sufficient condition for service success.
