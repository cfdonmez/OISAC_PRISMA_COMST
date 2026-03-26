# OISAC IEEE Template Prep

This folder is now the active LaTeX workspace for the journal-facing manuscript transition.

## Active Files

- `oisac_review_working.tex`: main working entry file built on the local `IEEEtran.cls` template
- `oisac_frontmatter.tex`: title, author block, running header, abstract, and keywords
- `sections/`: native LaTeX section files for Sections I-IX
- `references.bib`: local bibliography copy for the template workspace
- `fig1.png`, `fig2.png`, `fig3.png`, `fig_v_1.png`, `fig_v_2.png`, `fig_vi_1.jpg`, `fig_vi_2.jpg`: locally mirrored root-level figure assets
- `figures/`: locally mirrored figure subfolder used by the manuscript sections
- `prepare_oisac_template_body.ps1`: retained as a legacy utility for regenerating cleaned markdown derivatives if needed
- `oisac_review_template_body.md`: legacy cleaned template-side body snapshot
- `oisac_review_remaining_body.md`: legacy Section II+ markdown snapshot from the migration phase
- `build_oisac_review_working.ps1`: local build helper for repeated PDF generation with `pdflatex -> bibtex -> pdflatex -> pdflatex`
- `oisac_review_working_build_<timestamp>.pdf`: timestamped compiled outputs that avoid overwrite-lock issues on Windows
- `OISAC_COMST_review_body.md`: local copy of the current integrated review body kept for traceability
- `../current_bundle/OISAC_COMST_review_body.md`: canonical upstream body, kept as fallback/reference

## Current Status

- The working manuscript compiles successfully inside this template folder.
- The template folder now contains the currently required bibliography, body source, and figure assets for local-only compilation.
- Sections I-IX are now wired as native LaTeX inputs.
- Textual placeholder references have been migrated to native `\cite{...}` commands tied to `references.bib`.
- The generated PDF is a native-LaTeX transition draft with BibTeX-backed references, not yet a submission-ready package.
- The current template-run length is about 32 pages in the latest timestamped build, which is still long for a compact journal submission.

## Edit Order

1. Finalize journal-facing title, author list, affiliations, and correspondence metadata.
2. Decide which sections stay in the short journal version and which move to supplement.
3. Replace placeholder running headers and submission notes with final journal metadata.
4. Compress wide tables and long explanatory passages for the target journal page budget.

## Known Risks

- Some Unicode-heavy passages and equation blocks still need manual LaTeX normalization.
- Figure placement and page budget are not yet tuned for journal submission.
- Several wide tables still need compression or redesign for final submission quality.
