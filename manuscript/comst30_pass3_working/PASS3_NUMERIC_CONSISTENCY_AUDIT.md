# PASS3 Numeric Consistency Audit

## Sources Checked

- Main Pass-3 source: `manuscript/comst30_pass3_working/bare_jrnl_new_sample4.tex`
- PRISMA counts: `screening/prisma_flow_counts.csv`
- Included corpus ledgers: `screening/canonical_included_corpus_ledger.csv`, `screening/included_studies_canonical.csv`
- Full-text records: `screening/fulltext_assessed_reconstruction.csv`, `screening/excluded_fulltext_log.csv`
- Taxonomy counts: `analysis/IV_ev_v2/section4E_taxonomy_tree.json`
- Trade-off scenario data: `analysis/V_ev_v2/section5C_tradeoff_points.csv`, filtered against the canonical 220-study ledger
- Enabler summary cross-check: `analysis/VI_ev_v2/section6E_summary_table.csv`
- Bibliography count: `manuscript/comst30_pass3_working/bare_jrnl_new_sample4.bbl`

## Claim Audit

| Claim | Current manuscript wording | Source location | Verified value | Status | Action |
|---|---|---:|---|---|---|
| PRISMA identification count | "databases_results = 980" is implied by the reconstructed PRISMA ledger discussion; detailed main text emphasizes later row-backed stages. | Methodology; source ledger | 980 database records | OK | No text change required. |
| Duplicates removed | Reconciled PRISMA flow language; no conflicting main-text value found. | Methodology; source ledger | 280 duplicates removed | OK | No text change required. |
| Records screened | Reconciled PRISMA flow language; no conflicting main-text value found. | Methodology; source ledger | 700 screened | OK | No text change required. |
| Title/abstract exclusions | Reconciled PRISMA flow language; no conflicting main-text value found. | Methodology; source ledger | 478 excluded | OK | No text change required. |
| Full texts assessed | "222 full texts assessed" | Fig. PRISMA flow and methodology | 222 | OK | No change. |
| Full-text exclusions | "2 full-text exclusions" | Fig. PRISMA flow and methodology | 2 | OK | No change. |
| Included corpus | "N=220 peer-reviewed studies" | Abstract, Introduction, Methodology, Conclusion | 220 included studies | OK | No change. |
| Search freeze date | "November 30, 2025" | Methodology | November 30, 2025 | OK | No change. |
| OSF registration | "February 12, 2026 (Registration ID: 7f6wb)" | Methodology | February 12, 2026; 7f6wb | OK | No change. |
| Corpus year metadata | "centered/primarily 2020--2025" | Introduction/Methodology | Exact 219/210 metadata claim is not used in current main text. | OK | No change. |
| TQAF dimensions | Five dimensions listed | Methodology | Five dimensions | OK | No change. |
| TQAF complete scores | No exact "208 complete scores" claim found in current main text. | Methodology | Not asserted | OK | No change. |
| Fiber taxonomy count | "45/220" and "45 records" | Taxonomy table and prose | 45 cabled-fiber records | OK | Standardized "cabled-fibre" to "cabled-fiber". |
| FSO taxonomy count | "19/220" | Taxonomy table/prose | 19 FSO records | OK | No change. |
| VLC/LiFi taxonomy count | "25/220" | Taxonomy table/prose | 25 wireless VLC/LiFi records | OK | No conflicting 26-value found in current main text. |
| Hybrid taxonomy count | "116/220 hybrid" | Taxonomy table/prose | 116 hybrid records | OK | No change. |
| Explicit terahertz count | "explicit terahertz label appears only once" | Taxonomy prose | 1 explicit terahertz record | OK | No change. |
| Photonic-THz anchors | "39 photonic-THz anchors" | Taxonomy table/prose | Anchor count retained from Pass-2 synthesis; exact anchor file not separately regenerated in this pass. | AMBIGUOUS | Left unchanged because it is a Pass-2 synthesis claim and no contradiction was found. |
| Raw communication metric coverage | "rate ... 197/225", "SNR 190/225", "OSNR 169/225" | Section V-A | Matches canonical-filtered scenario ledger counts. | OK | No change. |
| Raw sensing metric coverage | "Delta r_min 195", "eligible 173", "sigma_r 186", "CRB 148", "Delta z 161" | Section V-B | Matches canonical-filtered scenario ledger counts. | OK | No change. |
| Governed scenario points | "225 scenario points from 220 papers" | Section V | 225 scenario points after filtering against canonical 220 corpus | OK | No change. |
| Governed rate + Delta r_min | "20" | Section V | 20 CRQ-valid rate + Delta r_min points | OK | No change. |
| Governed rate + sigma_r/RMSE | "16" | Section V | 16 governed rate + sigma_r/RMSE records | OK | No change. |
| Governed full triplet | "13" | Section V | 13 full rate--Delta r_min--sigma_r triplet records | OK | No change. |
| CRQ candidate/valid/Pareto counts | "170 candidate, 20 valid, 2 Pareto" | Section V-C | Matches governed CRQ classification used by Pass-2 synthesis | OK | No change. |
| Enabler ML count | "machine learning appears in 53 studies" | Section VI-F before edit | Conflicting repository summaries: broad/draft tag view reported 53; `section6E_summary_table.csv` reports 45 ML papers. | NEEDS QUALIFICATION | Replaced exact count with count-free wording: ML is treated as a material but uneven subset under strict versus broad evidence rules. |
| ORIS count | No exact "ORIS 8" claim found in current main text. | Section VI | Not asserted | OK | No change. |
| OPA count | No exact "OPA 7" claim found in current main text. | Section VI | Not asserted | OK | No change. |
| Application transfer counts | No exact "15 domains", "8 domains", "industrial 65", "vehicular 60", "indoor 56", or "6G 46" claims found in current main text. | Section VII | Not asserted | OK | No change. |
| Main bibliography count | Main bibliography is representative, not exhaustive. | Methodology | Final compiled bibliography remains 132 bibitems. | OK | Added/kept explicit representative-bibliography language. |
| Full corpus preservation | Complete 220-study ledger/extraction/supplement preserved outside main bibliography. | Methodology/data-availability language | Ledger and supplementary evidence are present in repository; main bibliography has 132 items. | OK | Added Zenodo DOI and repository name to the data availability sentence. |

## Notes

- `data/status/prisma_metrics.json` contains older conflicting PRISMA-style values and was not treated as authoritative. The canonical screening files and `screening/README.md` identify the row-backed/reconciled ledgers as the reliable source.
- The numeric correction made in Pass 3 is deliberately narrow: the exact ML prevalence claim was softened because repository summaries disagreed under strict versus broad tag rules.
- No scientific conclusion was changed. The governed Section V sparse-subset result remains intact.
