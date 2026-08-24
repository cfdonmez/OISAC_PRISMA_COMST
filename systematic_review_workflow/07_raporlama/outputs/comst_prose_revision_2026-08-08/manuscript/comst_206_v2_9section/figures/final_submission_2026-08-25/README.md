# Final submission figure package

This package contains the eight figures used in the O-ISAC survey. Every
figure is produced by deterministic Python drawing code in
`tools/build_final_figures.py`. The package contains no generated AI imagery
and no external artwork. All visual elements are native lines, shapes, text,
and data marks.

## Build

Run the following command from the manuscript root after installing Python,
Matplotlib, and Pillow.

```text
python tools/build_final_figures.py
```

The script regenerates the complete package and validates the declared totals
before writing the QA manifest.

## Canonical evidence sources

- Figure 1 and Figure 2 are conceptual diagrams derived from the native
  evidence framing and comparison framework stated in Section II.
- Figure 3 uses
  `systematic_review_workflow/09_kayitlar/checkpoints/prisma_flow_PHASE_C_FINAL_2026-07-30/PRISMA_FLOW_COUNTS_FINAL_2026-07-30.csv`.
- Figure 4 uses
  `systematic_review_workflow/09_kayitlar/checkpoints/quality_assessment_PHASE_E_FINAL_2026-08-04/phase_e_tqaf_dimension_audit_2026-08-04.csv`.
- Figure 5 uses
  `systematic_review_workflow/09_kayitlar/checkpoints/synthesis_PHASE_F_FINAL_2026-08-04/s2_integration_mechanisms.csv`.
- Figure 6 uses
  `systematic_review_workflow/09_kayitlar/checkpoints/synthesis_PHASE_F_FINAL_2026-08-04/s4_tradeoff_families.csv`.
  Its substantive view removes the two absence status audit rows and therefore
  reconciles 404 governed rows to 402 substantive relationships from 168
  studies. The resulting totals are 218 quantitative, 184 qualitative, and
  371 condition dependent relationships.
- Figure 7 uses
  `systematic_review_workflow/09_kayitlar/checkpoints/synthesis_PHASE_F_FINAL_2026-08-04/s5_validation_maturity.csv`
  and
  `systematic_review_workflow/09_kayitlar/checkpoints/synthesis_PHASE_F_FINAL_2026-08-04/s5_validation_types.csv`.
- Figure 8 uses the display crosswalk in `data/fig08_chain_display.csv` and the
  locked Phase F technology, application, and 6G relevance tables named
  `s6_enabling_technologies.csv`, `s6_application_domains.csv`, and
  `s7_six_g_relevance.csv`.

The QA manifest records SHA256 hashes for every data source used by a figure.

## Outputs

Each figure has an editable SVG and a vector PDF. The `data` directory contains
the plotted display tables. The `qa` directory contains color and grayscale PNG
previews together with `figure_build_qa.json`.

| Figure | PDF and SVG stem | PDF page size in points |
| --- | --- | --- |
| 1 | `fig01_native_evidence_objects` | 405.288 by 197.028 |
| 2 | `fig02_comparison_framework` | 405.288 by 241.380 |
| 3 | `fig03_prisma_report_study_flow` | 405.288 by 302.364 |
| 4 | `fig04_tqaf_profile` | 503.855 by 300.538 |
| 5 | `fig05_integration_map` | 405.288 by 202.572 |
| 6 | `fig06_tradeoff_profile` | 454.369 by 371.054 |
| 7 | `fig07_validation_profile` | 504.769 by 301.326 |
| 8 | `fig08_technology_application_chain` | 405.288 by 274.644 |

All PDFs contain one page and embedded TrueType fonts. All SVG files preserve
text as editable text and contain no embedded raster images. Concise
accessibility descriptions are provided in `ALT_TEXT.md`.
