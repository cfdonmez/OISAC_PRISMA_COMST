# Section II figure insertion — 2026-09-11

The user explicitly authorized placement of the approved corrected image.

- Figure 2 is anchored in Section II-A and appears at full text width on PDF page 4.
- Asset: `manuscript/figures/fig_section2_signal_paths_icons_2026-09-10.png`. It is an unchanged copy of the approved raster PNG.
- Asset SHA-256: `ABF064925C8F4A61E979350AA10336A632338EA9043611F7736A368A054DEC69`.
- Only the existing Figure 2 environment and its caption were changed in Section II. All 14 Section II labels were preserved. The other 29 baseline manuscript inputs are unchanged.
- Caption describes the visible signal paths and measurement markers. References to an optional probe and absent mmWave/THz labels were omitted.
- Build: `latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error main.tex`, exit 0, 29 pages.
- Final log: no undefined references, multiply defined labels, missing characters, or overfull boxes; 9 underfull spacing warnings remain.
- Placement was visually reviewed on pages 4–7 after insertion; page 4 was rendered and checked again after the final caption correction. No clipping or overlap was observed in the figure placement.
- Independent review checked page 4 and identified the absent-label caption mismatch, which was corrected before final export.
- Original sources are backed up under `governance/section2_before_figure_insertion_2026-09-11/`; checks and diff are under `governance/qa/section2_figure_insertion_2026-09-11/`.
- Final export: `output/pdf/OISAC_COMST_V3_SECTION2_FIGURE_INSERTED_2026-09-11.pdf`.
- Final export SHA-256: `29F887E020206D36E7ABFAF80D224B91D1BBC1E6DF94150D9F842821D4B6F7FC`; 3837108 bytes. Reopened successfully and verified identical to the compiled manuscript PDF.

This check covers figure insertion and its caption; it is not a whole-manuscript scientific review.
