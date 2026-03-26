# IEEE Photonics Journal Target Notes

Last updated: 2026-03-24

## Verified target context

- Target journal: IEEE Photonics Journal
- Journal page: https://ieeephotonics.org/publications/photonics-journal/
- LaTeX guide: https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/sites/7/IEEE_Photonics_Journal_instructions2.pdf
- Template/tools page: https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/authoring-tools-and-templates/

## Positioning decision

- Safest manuscript identity: `review article` / `systematic review`
- PRISMA should remain as the review method, not as a reason to present the paper as a `survey`
- Scope fit should emphasize photonics-centered O-ISAC:
  - fiber optics and optical communications systems
  - free-space optics
  - visible-light / LiFi sensing-communication systems
  - photonic-THz / microwave photonics bridging
  - optical sensors and reporting-governance issues

## Submission constraints to remember

- Manuscript format: standard two-column, single-spaced
- Figures should be embedded in the manuscript for accurate page estimation
- Abstract should be one paragraph and self-contained
- Abstract should not include references, footnotes, displayed equations, or tables
- Abstract should include three or four keywords/phrases
- Graphical abstracts are peer reviewed and cannot be added after acceptance
- The journal requests an impact statement under 500 characters
- Contributed submissions may be 7 pages before mandatory overlength charges begin
- IEEE Photonics Journal is fully open access

## Local workspace implication

- Review framing edits should be applied first to canonical authoring sources
- Bundle refresh must follow any canonical edit to avoid drift
- Local TeX Live currently includes `IEEEtran.cls` and `markdown.sty`
- `IEEEphot.cls` is referenced by the official guide but is not yet present in this workspace
- Until `IEEEphot.cls` is added, a staging LaTeX file may use `IEEEtran` for drafting only
- Current staging artifacts:
  - `manuscript/ieee_photonics_review_staging.tex`
  - `manuscript/current_bundle/OISAC_COMST_review_body.md`
  - `manuscript/ieee_photonics_review_staging.pdf`
- Current staging compile status:
  - `pdflatex --shell-escape ieee_photonics_review_staging.tex` succeeds
  - output is a working draft PDF, not a journal-final package
  - markdown-originated link-reference warnings and page-layout roughness still remain
