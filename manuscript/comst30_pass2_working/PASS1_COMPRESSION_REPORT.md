# PASS1 COMST Compression Report

## 1. Scope and Safety

- Working directory: `manuscript/comst30_working/`
- Original package preserved: `manuscript_submission/`
- Older final manuscript preserved: `manuscript/finalShortened/`
- Active working source: `manuscript/comst30_working/bare_jrnl_new_sample4.tex`
- Active working PDF: `manuscript/comst30_working/bare_jrnl_new_sample4.pdf`
- Build command used: `latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl_new_sample4.tex`
- Baseline page count: 44
- Final page count: 16
- Page reduction achieved: 28 pages

No files in `manuscript_submission/` or `manuscript/finalShortened/` were edited.

## 2. Files Edited or Created

| Path | Action |
|---|---|
| `manuscript/comst30_working/bare_jrnl_new_sample4.tex` | Edited; pass-1 compressed manuscript source |
| `manuscript/comst30_working/references.bib` | Edited; removed only `openai_codex_2026` |
| `manuscript/comst30_working/supplement_moved_tables.tex` | Created; moved/copied removed tables, figures, and equations |
| `manuscript/comst30_working/reference_slimming_candidates.md` | Created; deferred reference-reduction plan |
| `manuscript/comst30_working/COMST_COMPRESSION_LOG.md` | Updated; baseline and final metrics |
| `manuscript/comst30_working/compress_pass1.py` | Created; local helper used for controlled pass-1 transformation |
| `manuscript/comst30_working/PASS1_COMPRESSION_REPORT.md` | Created; this report |

## 3. Tables Moved to Supplement

| Label | Main-text action | Supplement location |
|---|---|---|
| `tab:performance_comparison` | Removed; replaced by compact prose | `supplement_moved_tables.tex` |
| `tab:math_notation` | Removed; replaced by supplement sentence | `supplement_moved_tables.tex` |
| `tab:acronyms` | Removed; replaced by supplement sentence | `supplement_moved_tables.tex` |
| `tab:section6_notation` | Removed | `supplement_moved_tables.tex` |
| `tab:taxonomy_contract` | Moved; replaced by compact taxonomy paragraph | `supplement_moved_tables.tex` |
| `tab:medium_classes` | Merged into `tab:taxonomy_compact` | `supplement_moved_tables.tex` |
| `tab:integration_mechanisms` | Merged into `tab:taxonomy_compact` | `supplement_moved_tables.tex` |
| `tab:detection_observability` | Merged into `tab:taxonomy_compact` | `supplement_moved_tables.tex` |
| `tab:taxonomy_clusters` | Merged into `tab:taxonomy_compact` | `supplement_moved_tables.tex` |
| `tab:comm_metrics` | Merged into `tab:governance_attrition` | `supplement_moved_tables.tex` |
| `tab:sensing_metrics` | Merged into `tab:governance_attrition` | `supplement_moved_tables.tex` |
| `tab:section7_dualview` | Removed from main application section | `supplement_moved_tables.tex` |
| `tab:viii_f_1` | Removed from roadmap section | `supplement_moved_tables.tex` |
| `tab:viii_g_1` | Removed from roadmap audit layer | `supplement_moved_tables.tex` |
| `tab:viii_g_2` | Removed from roadmap audit layer | `supplement_moved_tables.tex` |

## 4. Figures Moved or Removed From Main Text

| Label | Main-text action | Notes |
|---|---|---|
| `fig:fig1` | Kept | Opening O-ISAC landscape |
| `fig:fig2` | Moved to supplement | Duplicate optical-advantage argument |
| `fig:fig3` | Moved to supplement | Replaced by Section IV taxonomy synthesis |
| `fig:fig_ii_1` | Kept | Unified system abstraction |
| `fig:fig_ii_2` | Moved to supplement | Duplicated `tab:ii2` metric contract |
| `fig:fig_iii_1` | Kept in compact form | PRISMA flow retained |
| `fig:fig_iv_1` | Kept | Single taxonomy figure |
| `fig:fig_iv_2` | Moved to supplement | Redundant taxonomy view |
| `fig:fig_v_1` | Kept | Protected governed operating-cloud figure |
| `fig:fig_v_2` | Moved to supplement | CRQ frontier retained as illustrative supplement |
| `fig:fig_vi_1` | Moved to supplement | Enabler landscape replaced by deployment map |
| `fig:fig_vi_2` | Kept | Enabler-to-deployment systems map |
| `fig:fig_vii_1` | Moved to supplement | Applications compressed to portfolio table |
| `fig:fig_viii_1` | Kept | Main roadmap figure |

Underlying graphics files in `manuscript/comst30_working/figures/` were not deleted.

## 5. Equations Moved, Removed, or Inlined

| Object | Main-text action |
|---|---|
| Conceptual NLSE / `eq:nlse_conceptual` | Moved to supplement; replaced by one guided-propagation sentence |
| Canonical observation/channel expansions | Inlined into compact prose and `tab:ii1` |
| `\Delta r_{\min}=v/(2B_{\mathrm{eff}})` | Kept numbered as `eq:range_resolution` |
| `\mathrm{CRQ}_{\Delta}=R/\Delta r_{\min}` | Kept numbered as `eq:crq_delta` |
| Taxonomy vector `T(p)=(m(p),i(p),d(p),s(p))` | Kept numbered as `eq:taxonomy_vector` |
| Section VI multi-user/resource/security optimization equations | Moved to supplement as organizational scaffolding |
| Section VII application organizational equations | Moved to supplement as organizational scaffolding |
| Section VIII roadmap/utility/governance equations | Moved to supplement as organizational scaffolding |

## 6. Section-by-Section Compression Summary

| Section | Pass-1 action | Estimated reduction |
|---|---|---|
| Title/Abstract | Shortened title; abstract reduced to metric-governed summary | High |
| I Introduction | Kept Fig. 1 and compact Table I; removed RF comparison table and preview figure | High |
| II Background/Metric Governance | Renamed and compressed; kept metric contract table | High |
| III Methodology | PRISMA/TQAF credibility retained; detailed search prose moved out | Medium |
| IV Taxonomy | Merged taxonomy tables; retained one taxonomy figure | High |
| V Tradeoff Synthesis | Protected; light compression only | Low/medium |
| VI Enablers | One compact table, one deployment map, compact reporting contract | High |
| VII Applications | Reduced to one five-row portfolio table and one synthesis block | High |
| VIII Roadmap | One figure, one challenge table, one five-row agenda | High |
| Conclusion | Reduced to one compact conclusion | Medium |

## 7. Final Build Metrics

| Metric | Baseline | Final |
|---|---:|---:|
| Pages | 44 | 16 |
| Overfull hbox | 20 | 0 |
| Underfull hbox | not separately recorded | 83 |
| Underfull boxes total | 87 | 88 |
| Undefined citations | 0 | 0 |
| Undefined references | 0 | 0 |
| LaTeX warnings | 0 | 0 |
| Bibliography items in compiled PDF | 220 | 220 |

The working `.bib` database now has 220 entries after removing only `openai_codex_2026`.

## 8. Core Scientific Content Preserved

- PRISMA-grounded `N=220` evidence base.
- 222 full texts assessed, 2 full-text exclusions, final `N=220`.
- Cross-modality taxonomy across fiber, FSO, VLC/LiFi, photonic-THz/hybrid.
- Metric-governance separation of `\Delta r_{\min}`, `\sigma_r`/RMSE, CRB/FIM, `\Delta z`, OSNR/SNR/ESNR plane.
- Governed subset result: 225 scenario points; 20 rate + `\Delta r_{\min}`; 16 rate + `\sigma_r`; 13 full triplet.
- CRQ-valid subset treated as sparse and illustrative, not a stable design envelope.
- Enablers retained: ORIS/optical RIS, OPA, PIC/photonic integration, photonics-assisted mmWave/THz generation, ML/security adaptation.
- Applications retained as a deployment map rather than a maturity scorecard.
- Roadmap retained: taxonomy, metric-governed reporting, reproducible benchmarks, scalable hardware, deployment validation.

## 9. Remaining Biggest Page Inflators

- Full 220-item bibliography is still present through `\nocite{*}`.
- IEEE biographies remain in the working PDF.
- Seven main figures remain, including several full-width figures.
- Twelve main tables remain, although most are compact.
- Underfull boxes mostly come from dense tables with narrow columns.

## 10. Deferred to Pass 2

- Rebalance from 16 pages toward the desired 29--30 page COMST manuscript if more explanatory depth is needed.
- Add back carefully selected representative citations in main text while preserving the full corpus ledger in supplement/OSF/Zenodo.
- Decide whether IEEE biographies are required for the COMST traditional submission build.
- Tune table column widths and possibly convert some dense tables into one-column prose/table hybrids.
- Produce a polished supplementary package that compiles independently, if desired.
- Use corpus/data scripts to verify every count before any numerical edits.

## 11. Scientific-Risk Warnings

- This first pass is intentionally aggressive. It produces a clean, compiling 16-page working draft, which is below the eventual 29--30 page target and may need controlled re-expansion for COMST narrative depth.
- The reference list is preserved via `\nocite{*}`; this is safe for traceability but not ideal final citation practice.
- No numerical findings were recalculated. Counts were preserved from the existing manuscript text.
- The removed figures/tables/equations are preserved in `supplement_moved_tables.tex` or in the untouched original submission source, but the supplement file has not been made into an independently compiling supplement.
