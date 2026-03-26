# OISAC IEEE Template Prep

This folder is now the active LaTeX workspace for the journal-facing manuscript transition.

## Active Files

- `oisac_review_working.tex`: main working entry file built on the local `IEEEtran.cls` template
- `oisac_frontmatter.tex`: title, author block, running header, abstract, and keywords
- `prepare_oisac_template_body.ps1`: generates a template-cleaned markdown body from the canonical bundle
- `oisac_review_template_body.md`: cleaned template-side body used for compilation
- `build_oisac_review_working.ps1`: local build helper for repeated PDF generation
- `oisac_review_working_build.pdf`: preferred compiled output to avoid overwrite-lock issues
- `../current_bundle/OISAC_COMST_review_body.md`: current imported review body

## Current Status

- The working manuscript compiles successfully inside this template folder.
- The body is now compiled from a template-side cleaned derivative of the integrated markdown bundle.
- The generated PDF is a transition draft, not a submission-ready package.
- The current template-run length is about 55 pages, so a compact journal version is still required.

## Edit Order

1. Finalize journal-facing title, author list, affiliations, and correspondence metadata.
2. Decide which sections stay in the short journal version and which move to supplement.
3. Convert the highest-risk sections from markdown import to native LaTeX, starting with Introduction, figures/tables, and references.
4. Replace placeholder running headers and submission notes with final journal metadata.

## Known Risks

- Markdown-origin links still produce warnings during compilation.
- Some Unicode-heavy passages may need manual LaTeX normalization.
- Figure placement and page budget are not yet tuned for journal submission.
- Pipe tables now render structurally, but several wide tables still need native LaTeX conversion for final submission quality.
