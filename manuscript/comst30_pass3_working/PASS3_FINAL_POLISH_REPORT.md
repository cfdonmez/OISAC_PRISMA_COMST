# PASS3 Final Polish Report

## Phase 0 Baseline

- Working directory: `manuscript/comst30_pass3_working/`
- Source copied from: `manuscript/comst30_pass2_working/`
- Baseline build command: `latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl_new_sample4.tex`
- Baseline page count: 27
- Baseline references start page: 22
- Baseline compiled bibliography items: 132
- Baseline main figures: 7
- Baseline main tables: 12
- Baseline numbered equation environments: 3
- Baseline overfull hbox count: 0
- Baseline underfull hbox count: 99
- Baseline underfull vbox count: 8
- Baseline undefined citations: 0
- Baseline undefined references: 0
- `\nocite{*}` absent: YES
- Biographies omitted from main build: YES
- Biography blocks preserved in `biographies_moved_for_submission.tex`: 3

The copied Pass-2 source is a clean 27-page baseline. Pass 3 will avoid major rewriting and will only apply safe numeric consistency, reference/corpus wording, table/layout, caption, and light academic style cleanup inside this Pass-3 working directory.

## Pass-3 Edits Applied

### Files Edited

- `bare_jrnl_new_sample4.tex`
- `PASS3_NUMERIC_CONSISTENCY_AUDIT.md`
- `PASS3_LAYOUT_AND_UNDERFULL_AUDIT.md`
- `PASS3_SUBMISSION_READINESS_CHECKLIST.md`
- `PASS3_FINAL_POLISH_REPORT.md`
- `ORIGINAL_AND_PASS2_PRESERVATION_MANIFEST_BEFORE.md`
- `ORIGINAL_AND_PASS2_PRESERVATION_MANIFEST_AFTER.md`

### What Changed

- Added local ragged-right `tabularx` column types (`L{}` and `Y`) and applied them to all main-text tables to reduce underfull warnings without introducing global layout hacks.
- Shortened selected table-cell phrases in the modality, metric, taxonomy, comparative-slice, enabler, application, and roadmap tables.
- Added explicit text references for previously weakly referenced objects: `tab:ii1`, `tab:iii1`, `fig:fig_iii_1`, `fig:fig_iv_1`, `tab:challenge_compact`, and `tab:viii_f_2`.
- Replaced internal Pass-2 wording about `\nocite{*}` with paper-facing bibliography/corpus language.
- Added the public evidence package statement with Zenodo DOI `10.5281/zenodo.19643231` and repository name `OISAC_PRISMA_COMST`.
- Softened the exact ML prevalence sentence because repository tag summaries disagreed under strict versus broad counting rules.
- Standardized visible terminology from `photonic-terahertz` to `photonic-THz` in keywords and from `cabled-fibre` to `cabled-fiber` in the main text.
- Removed remaining comments that referred to "Pass-2 main text" and replaced them with neutral "main text" comments.

### What Was Not Changed

- No original protected folder was edited.
- No figures, figure files, simulation outputs, data ledgers, bibliography entries, author names, affiliations, or correspondence metadata were edited.
- No large tables or removed figures from the 44-page version were restored.
- No numerical findings were fabricated or reinterpreted beyond the narrow ML-count qualification.
- Section V structure and governed-subset conclusion were preserved.

## Final Build Metrics

These metrics are from the final clean build:
`latexmk -C; latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl_new_sample4.tex`.

| Metric | Value |
|---|---:|
| Page count | 27 |
| References start page | 22 |
| Compiled bibliography items | 132 |
| Main figures | 7 |
| Main tables | 12 |
| Overfull hbox | 0 |
| Underfull hbox | 16 |
| Underfull vbox | 7 |
| Undefined citations | 0 |
| Undefined references | 0 |
| Active `\nocite{*}` commands | 0 |
| Main-build biography blocks | 0 |

## Scientific Core Preservation

- PRISMA/TQAF evidence base with `N=220` remains.
- Cross-modality taxonomy remains across fiber, FSO, VLC/LiFi, photonic-THz, and hybrid records.
- Metric governance remains explicit: `Delta r_min`, `sigma_r`/RMSE, CRB/FIM, `Delta z`, and OSNR/SNR/ESNR are not collapsed.
- Section V still reports 225 scenario points, 20 rate + `Delta r_min`, 16 rate + `sigma_r`/RMSE, and 13 full-triplet records.
- CRQ remains described as a sparse illustrative subset, not a stable design envelope.
- Enablers, applications, and roadmap remain compact and domain-conditioned.

## Remaining Harmless Warnings

- 16 underfull hbox warnings remain, mostly paragraph-level narrow-column effects.
- 7 underfull vbox warnings remain, mostly float-placement effects around large IEEE figures.
- These are documented in `PASS3_LAYOUT_AND_UNDERFULL_AUDIT.md`; no overfull boxes remain.

## Unresolved Ambiguities

- The photonic-THz anchor count of 39 was retained from the Pass-2 synthesis; it was not independently regenerated in Pass 3.
- Enabler ML prevalence differs across broad and strict repository tag views, so the exact 53-study claim was removed from the main text.
- Some legacy re-expanded prose still contains dense survey phrasing and should receive a human read-through for cadence and citation punctuation.

## Recommendation

Ready for human read-through. The Pass-3 manuscript keeps the 27-page target, corrects the bibliography/corpus architecture, preserves the governed Section V result, and has a clean build with 0 overfull hboxes and no undefined citations or references.
