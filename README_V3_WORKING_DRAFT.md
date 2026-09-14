# O-ISAC COMST V3 Working Draft

- Branch: `rev/comst-v3-20260906`
- Source baseline: original V2 commit `13e3727241cb1d7726abb3ddb1833505c73c157f`
- Opened: 2026-09-06
- Status: author-review working draft; not a locked or submission-ready version

Latest reading copy: [review.pdf](output/pdf/review.pdf), 29 pages.
The 14 September structure and verification are recorded in
[review.md](governance/review.md). Review Methodology is now Introduction I-C,
between Related Surveys and Scope and Contributions. The standalone methods
section has been removed, leaving eight main sections. The compact selection
flow is Figure 2; technical appraisal is presented with the validation results.

Detailed methods and analysis-unit counts are in
[methods.md](supplement/methods.md), with source carriers mapped in
[index.md](supplement/index.md). The manuscript uses the author-approved
final-state OSF statement. Updating the OSF archive remains a separate joint
task; no remote update was performed in this manuscript revision.

GitHub repository: https://github.com/cfdonmez/OISAC_PRISMA_COMST
This branch contains the standalone V3 manuscript snapshot and its local
baseline history. It is not based on the repository's `main` branch history.
The 14 September transfer also includes project memory, source carriers,
revision backups and recorded QA. Start with [README.md](README.md) and
[handoff/state.md](handoff/state.md). Machine-local browser profiles remain excluded.

Active authoring decisions are in `governance/V3_ACTIVE_WRITING_RULES.md`.
They supersede conflicting historical recipes. Methodological dates and counts
are confined to the new methods subsection/flow and supplements; they are not
presented as scientific contributions.

The applied Section I recipe and Section II handoff guide are in
`governance/SECTION1_RECETESI_VE_SECTION2_UYGULAMA_REHBERI_2026-09-07.md`.
The ready-to-use agent prompt is
`governance/SECTION2_AJAN_PROMPTU_2026-09-07.md`.

The Section II figure briefs are preserved in
`governance/SECTION2_FIGUR_PROMPTLARI_2026-09-07.md`.
The author-approved signal-path and resource-sharing illustrations have been
integrated with their captions and in-text references.

This worktree is the only location used for the V3 rewrite. The canonical V2
source and the earlier RC1 revision worktree remain unchanged.

The Section II technical rewrite was completed on 2026-09-07. Its four
subsections explain signal paths, shared resources and optical constraints,
communication and sensing measures, and joint performance interpretation.
Two icon-based illustrations and one native-LaTeX figure support these
explanations. Table II presents
source-specific numerical configurations from fiber, visible-light, and
photonic-THz studies, with their distinct measurement conditions preserved.

The current performance and validation analyses are in Sections IV and V.
Section II provides the technical foundation without importing old composite
scores or creating a pooled cross-platform benchmark. Existing technical
figure assets are preserved; figure and table numbering follows the new order.

The subsection/figure map, source locations, and scoped verification record
are in `governance/V3_SECTION_II_TECHNICAL_REWRITE_NOTE_2026-09-07.md`.

Section II received a further house-style audit on 2026-09-07. Missing
abbreviation and equation-variable definitions were supplied, and repeated
defensive captions were replaced with direct physical explanations.

In the earlier 7 September version, Section III was rewritten around search and study reconciliation,
extraction and analysis units, and technical appraisal and synthesis.
Its Table III distinguished study, coding-record, metric, relationship, and
synthesis-group counts. The executed investigator-supervised, AI-assisted
workflow and retrospective registration were described with their actual scope.
Those detailed records now belong in the scientific methods supplement.
The earlier PRISMA artwork remains preserved alongside the new selection
diagram. Historical verification below describes those earlier versions.

The earlier audit and subsection map are in
`governance/V3_SECTION_II_RECHECK_AND_SECTION_III_REVISION_2026-09-07.md`.

Historical 12 September state: that update ordered Section III-A around eligibility, searches,
the executed review workflow, retrospective registration, and report-to-study
reconciliation. The then-Figure 5 retained its labels and counts with corrected
panel spacing. That historical reading-copy hash and its build/layout checks
are documented in `governance/qa/s3a/result.json`. The current reading copy
is `review.pdf`, and the current selection diagram is Figure 2.

To build, run from `manuscript/`:

```sh
latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```
