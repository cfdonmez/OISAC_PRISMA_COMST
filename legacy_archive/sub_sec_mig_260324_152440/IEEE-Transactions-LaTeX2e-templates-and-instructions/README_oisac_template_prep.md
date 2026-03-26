# OISAC IEEE Template Prep

This folder is now the active LaTeX workspace for the journal-facing manuscript transition.

## Active Files

- `oisac_review_working.tex`: main working entry file built on the local `IEEEtran.cls` template
- `oisac_frontmatter.tex`: title, author block, running header, abstract, and keywords
- `sections/section_01_introduction.tex`: native LaTeX version of Section I
- `references.bib`: local bibliography copy for the template workspace
- `fig1.png`, `fig2.png`, `fig3.png`, `fig_v_1.png`, `fig_v_2.png`, `fig_vi_1.jpg`, `fig_vi_2.jpg`: locally mirrored root-level figure assets
- `figures/`: locally mirrored figure subfolder used by the remaining manuscript sections
- `prepare_oisac_template_body.ps1`: generates a template-cleaned markdown body from the canonical bundle
- `oisac_review_template_body.md`: cleaned template-side body used for compilation
- `oisac_review_remaining_body.md`: Section II onward during staged migration
- `build_oisac_review_working.ps1`: local build helper for repeated PDF generation
- `oisac_review_working_build.pdf`: preferred compiled output to avoid overwrite-lock issues
- `OISAC_COMST_review_body.md`: local copy of the current integrated review body used first by the prep script
- `../current_bundle/OISAC_COMST_review_body.md`: canonical upstream body, kept as fallback/reference

## Current Status

- The working manuscript compiles successfully inside this template folder.
- The template folder now contains the currently required bibliography, body source, and figure assets for local-only compilation.
- Section I is now native LaTeX.
- Section II onward is still compiled from a template-side cleaned derivative of the integrated markdown bundle.
- The generated PDF is a transition draft, not a submission-ready package.
- The current template-run length is about 47 pages, so a compact journal version is still required.

## Edit Order

1. Finalize journal-facing title, author list, affiliations, and correspondence metadata.
2. Decide which sections stay in the short journal version and which move to supplement.
3. Continue converting the highest-risk sections from markdown import to native LaTeX, starting with Section II figures/tables and then the remaining core sections.
4. Replace placeholder running headers and submission notes with final journal metadata.

## Known Risks

- Markdown-origin links still produce warnings during compilation.
- Some Unicode-heavy passages may need manual LaTeX normalization.
- Figure placement and page budget are not yet tuned for journal submission.
- Pipe tables now render structurally, but several wide tables still need native LaTeX conversion for final submission quality.
