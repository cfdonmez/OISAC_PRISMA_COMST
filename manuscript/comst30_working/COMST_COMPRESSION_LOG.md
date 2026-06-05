# COMST Pass 1 Compression Log

## Baseline

- Working directory: `manuscript/comst30_working/`
- Source copied from: `manuscript_submission/bare_jrnl_new_sample4.tex`
- Bibliography copied from: `manuscript_submission/references.bib`
- Class copied from: `manuscript_submission/IEEEtran.cls`
- Figures copied from: `manuscript_submission/figures/`
- Baseline build command: `latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl_new_sample4.tex`
- Baseline compiled PDF: `bare_jrnl_new_sample4.pdf`
- Baseline page count: 44
- Baseline overfull hbox count: 20
- Baseline underfull box count: 87
- Baseline undefined citations: 0
- Baseline undefined references: 0

## Pass 1 Edit Plan

- Preserve the original `manuscript_submission/` and `manuscript/finalShortened/` packages unchanged.
- Edit only files inside `manuscript/comst30_working/`.
- Move removed main-text tables, duplicate figures, and organizational equations into `supplement_moved_tables.tex`.
- Keep the PRISMA/TQAF N=220 evidence claim, cross-modality taxonomy, metric-governance contract, and Section V governed trade-off/CRQ result.

## Pass 1 Actions Completed

- Rewrote the working-copy title and abstract.
- Replaced the main body with a compact nine-section COMST pass-1 structure.
- Preserved author names, affiliations, correspondence metadata, IEEE biographies, class file, and figures directory.
- Moved removed or duplicate main-text blocks into `supplement_moved_tables.tex`.
- Kept the main metric contract in `tab:ii2`, retained the governed trade-off result in Section V, and preserved the PRISMA `N=220` corpus statement.
- Removed only the non-core bibliography entry `openai_codex_2026` from the working bibliography.
- Added `\nocite{*}` so the remaining 220 included-corpus references remain visible in this first structural pass.
- Created `reference_slimming_candidates.md` for a later, safer reference-reduction pass.

## Final Build

- Final build command: `latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl_new_sample4.tex`
- Final compiled PDF: `bare_jrnl_new_sample4.pdf`
- Final page count: 16
- Page reduction achieved: 28 pages
- Final overfull hbox count: 0
- Final underfull hbox count: 83
- Final underfull vbox count: 5
- Final undefined citations: 0
- Final undefined references: 0
- Final LaTeX warnings: 0
- Final bibliography items: 220
