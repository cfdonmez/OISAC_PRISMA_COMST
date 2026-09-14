# O-ISAC COMST V3 Working Draft

- Branch: `rev/comst-v3-20260906`
- Source baseline: original V2 commit `13e3727241cb1d7726abb3ddb1833505c73c157f`
- Opened: 2026-09-06
- Status: author-review working draft; not a locked or submission-ready version

Latest reading copy: [s3a.pdf](output/pdf/s3a.pdf), 30 pages.
The latest Section III-A changes and Figure 5 layout check are recorded in
[s3a.md](governance/s3a.md).

GitHub repository: https://github.com/cfdonmez/OISAC_PRISMA_COMST
This branch contains the standalone V3 manuscript snapshot and its local
baseline history. It is not based on the repository's `main` branch history.
Temporary render files, browser profiles, and intermediate backup PDFs are
kept locally outside the published revision.

Active authoring decisions are in `governance/V3_ACTIVE_WRITING_RULES.md`.
They supersede conflicting historical recipe instructions, including the old
requirement to state the study count in Introduction.

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

Corpus counts and the full quantitative synthesis remain in Sections III, V,
and VI. Section II provides the technical foundation without importing old
composite scores or creating a pooled cross-platform benchmark. The previously
revised Introduction is preserved.

The subsection/figure map, source locations, and scoped verification record
are in `governance/V3_SECTION_II_TECHNICAL_REWRITE_NOTE_2026-09-07.md`.

Section II received a further house-style audit on 2026-09-07. Missing
abbreviation and equation-variable definitions were supplied, and repeated
defensive captions were replaced with direct physical explanations.

Section III was then rewritten around search and study reconciliation,
extraction and analysis units, and technical appraisal and synthesis.
Table III now distinguishes study, coding-record, metric, relationship, and
synthesis-group counts. The executed investigator-supervised, AI-assisted
workflow and retrospective registration are described with their actual scope.
The PRISMA artwork has a separate layout-corrected vector copy with unchanged
text and numbers. Section IV and later sections have not been revised in this
pass.

The current audit and subsection map are in
`governance/V3_SECTION_II_RECHECK_AND_SECTION_III_REVISION_2026-09-07.md`.

The 12 September update orders Section III-A around eligibility, searches,
the executed review workflow, retrospective registration, and report-to-study
reconciliation. Figure 5 retains its labels and counts with corrected panel
spacing. The reading-copy hash matches the recorded verification result;
build and layout checks are documented in `governance/qa/s3a/result.json`.

To build, run from `manuscript/`:

```sh
latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```
