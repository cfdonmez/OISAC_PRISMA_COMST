# PASS3 Submission Readiness Checklist

| Item | Status | Notes |
|---|---|---|
| PDF page count <= 30 | PASS | Current build is 27 pages. |
| Target 27--29 pages achieved | PASS | Current build remains at the lower bound of the target window. |
| References start page >= 22 | PASS | References begin on page 22. |
| Biographies omitted from submission build | PASS | No `IEEEbiography` blocks in the main TeX source. |
| `\nocite{*}` absent | PASS | No active `\nocite{*}` command found. |
| Full 220 corpus preserved through ledger / supplement / Zenodo | PASS | Main text cites representative records; complete corpus is pointed to ledger/supplement/Zenodo DOI. |
| No undefined citations | PASS | Build log reports 0 undefined citations. |
| No undefined references | PASS | Build log reports 0 undefined references. |
| No overfull hbox | PASS | Build log reports 0 overfull hbox warnings. |
| Underfull warnings documented | PASS | Remaining 16 hbox and 7 vbox warnings are documented in `PASS3_LAYOUT_AND_UNDERFULL_AUDIT.md`. |
| Section V governed result preserved | PASS | 225 scenario points, 20 rate + Delta r_min, 16 rate + sigma_r/RMSE, and 13 full triplet remain. |
| PRISMA N=220 preserved | PASS | Abstract, methods, and conclusion retain N=220. |
| Metric-governance distinctions preserved | PASS | Delta r_min, sigma_r/RMSE, CRB/FIM, Delta z, and OSNR/SNR/ESNR remain separated. |
| Title and abstract consistent | PASS | Title, abstract, keywords, and conclusion use consistent O-ISAC and photonic-THz terminology. |
| Data availability statement present | PASS | Methodology now includes Zenodo DOI 10.5281/zenodo.19643231 and `OISAC_PRISMA_COMST`. |
| Supplementary moved tables present | PASS | `supplement_moved_tables.tex` is present in the Pass-3 working directory. |
| No contradiction between main bibliography count and 220-study corpus | PASS | Main bibliography is described as representative; the 220-study corpus is preserved externally. |
| All figures cited in order | PASS | All seven main figures have explicit text references in source order. |
| All tables cited in order | PASS | All twelve main tables have explicit text references in source order or local section context. |
| No references to removed figures/tables | PASS | Source scan found no active references to removed Pass-1/Pass-2 figures or large moved tables. |
| No claims of full technical peer review after previous special issue rejection | PASS | No such claim found in Pass-3 source scan. |
| No author/affiliation metadata damaged | PASS | Author, affiliation, correspondence, and ORCID metadata were not edited in Pass 3. |

## Readiness Recommendation

Ready for human read-through after Pass-3 cleanup. The manuscript is not yet a final submission proof because remaining paragraph-level style issues and legacy prose with sparse citation punctuation should receive a human editorial pass, but the build, page budget, bibliography architecture, and scientific core are submission-ready for review.
