# V3 Introduction revision - author reading copy

Date: 2026-09-06

## Reading copy

- PDF: `output/pdf/OISAC_COMST_V3_INTRODUCTION_REVISED_2026-09-06.pdf` (27 pages).
- Introduction prose: pages 1-2.
- Approved overview illustration: Figure 1, page 2.
- Related-survey overview: Table I, page 3.
- Source: `manuscript/sections/01_INTRODUCTION.tex`.

## Narrative model used

The user requested the explanatory style of the two papers in
`C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06`.
Their introductions were read directly, with rendered pages checked.

- P01, Zhang et al., *Integrated Sensing and Communications Over the Years*
  (`P01/1.pdf`, Introduction pages 1-3). Used the progression from a practical
  need to shared-system design, related surveys, and contributions.
- P02, Mohsan et al., *Optical integrated sensing and communication*
  (`P02/2.pdf`, Introduction pages 1-3 and related-work table on page 4).
  Used physical descriptions of optical implementations and concrete examples.

The new prose is original. Numerical records, promotional claims, and broad
superiority statements from these papers were not imported. The organizing
sequence is need, physical implementation, shared-design consequence, related
surveys, scope, and three technical contributions. Internal extraction codes
and evidence-management terminology are absent from the Introduction.

## Evidence examples

- `OISAC_SCR00057`: primary PDF page 3, Section III and Fig. 3(e), verified
  against the local source. Raising sensing-probe power at fixed communication
  launch power improves sensing SNR while worsening communication BER in that
  configuration. This is not described as a fixed-total-power allocation.
- `OISAC_SCR00196`: primary full text, Section 2.D and Fig. 5 discussion,
  supports position-guided beamforming and communication improvement at tested
  locations. The text does not claim an experimentally completed real-time
  feedback loop or identify this prototype with the figure's ceiling-light scene.

## Change boundary

- Content revision is confined to Introduction, its caption, and Table I.
- The approved `C:/Users/fatih/Downloads/img_gi11.png` was copied unchanged to
  `manuscript/figures/fig_introduction_oisac_platforms.png`.
- Section II received a layout-only change. Its later figure and table
  declarations were moved beside its first figure declaration so the new
  Introduction would not create a mostly empty page downstream. Its prose,
  figure contents, table contents, and citation/label identifiers are unchanged.
- The abstract and Sections III-IX were not rewritten. The entire manuscript
  has not been brought to this narrative style in this pass.
- The canonical original manuscript and the 206-study evidence base remain
  unchanged. This is an author reading draft, not a submission-release claim.

## Preservation and checks

- Before-revision Introduction: `section1_before_narrative_revision_2026-09-06.tex`.
- Before-layout Section II: `section2_before_intro_float_layout_2026-09-06.tex`.
- Build: `latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error main.tex`.
- Final build completed. No undefined references, LaTeX warnings, or overfull
  boxes in the final log. Existing underfull line warnings remain elsewhere.
- All 32 distinct Introduction citation keys resolve in the existing bibliography.
- Section II prose and all three float contents match the layout backup after
  whitespace normalization and separation of float declarations.
- Final PDF pages 1-5 rendered and visually inspected. Figure 1 and Table I
  are legible, and the formerly mostly empty downstream page is eliminated.
- `git diff --check` passed.

SHA-256 values:

| Artifact | SHA-256 |
|---|---|
| Final PDF | `FAF3D41C39B2EFADFFAB9754C1254BC4CE99FE9BC8B9F8BC0949ED429FD65A5D` |
| Revised Introduction | `81AFD2B2966D8956BE32ABF481A15F2A67072CB5F536780161A3170456A1BC6E` |
| Section II after layout-only move | `9770EBD1B507F486DA3E5A1BD8EA7CEF62E74121C132E229DCBE0BF2A15E4B19` |
| Approved PNG and manuscript copy | `48EF1D02A4E59B18C256395AAD811946B2230C1623A5F7DCE30C998B9FD36FF0` |
| Canonical original Introduction and backup | `AD7AFB117D43EB196BFEC38EE7EE3CD5559E3E009E70BB8A09D9149BBED6E03A` |
| Canonical original PDF | `6A195C6856E5BD784DEF0A5149B1DF025771E5E50D7B2C02A7D229108B450DC2` |
