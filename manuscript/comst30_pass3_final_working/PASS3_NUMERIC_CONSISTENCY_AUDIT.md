# PASS-3 Numeric Consistency Audit

## Sources Checked

- `bare_jrnl_new_sample4.tex`
- `screening/prisma_flow_counts.csv`
- `screening/fulltext_assessed_reconstruction.csv`
- `screening/excluded_fulltext_log.csv`
- `screening/canonical_included_corpus_ledger.csv`
- `screening/O_ISAC_347_metadata_anomaly_20260310.md`
- `analysis/IV_ev_v2/section4E_taxonomy_tree.json`
- `analysis/V_ev_v2/section5C_tradeoff_points.csv`
- `review_package/COMST_review_bundle_01_manuscript.md`
- Final compiled `bare_jrnl_new_sample4.bbl`

## Audit Table

| Claim | Location | Status | Action |
|---|---|---|---|
| PRISMA upstream counts: 980 identified, 280 duplicates removed, 700 screened, 478 excluded | Not printed in main manuscript; ledger `screening/prisma_flow_counts.csv` | OK | Left out of main text; verified in ledger. |
| 222 full texts assessed | `bare_jrnl_new_sample4.tex` lines 233, 241, 304 | OK | Verified against `screening/fulltext_assessed_reconstruction.csv` count 222. |
| 2 full-text exclusions | `bare_jrnl_new_sample4.tex` lines 234, 241, 304 | OK | Verified against `screening/excluded_fulltext_log.csv` count 2. |
| Final corpus `N=220` | Abstract, Introduction, Methodology, Taxonomy, Data Availability | OK | Verified against `screening/canonical_included_corpus_ledger.csv` count 220. |
| Main bibliography is representative/load-bearing, not all 220 records | `bare_jrnl_new_sample4.tex` lines 255, 304, 775 | OK | Confirmed wording does not claim all 220 studies are printed in the main bibliography. |
| Compiled bibliography has 132 bibitems | `bare_jrnl_new_sample4.bbl` | OK | Verified by counting `\bibitem` entries. |
| Full 220 corpus preserved via ledger/supplement/Zenodo | Methodology and Data Availability | OK | DOI `10.5281/zenodo.19643231` and `OISAC_PRISMA_COMST` present. |
| Hybrid 116/220 | Taxonomy table/prose | OK | Verified from `analysis/IV_ev_v2/section4E_taxonomy_tree.json`. |
| Fiber 45/220 | Taxonomy table/prose | OK | Verified from taxonomy JSON. |
| VLC/LiFi 25/220 | Taxonomy table/prose | OK | Verified from taxonomy JSON. |
| FSO 19/220 | Taxonomy table/prose | OK | Verified from taxonomy JSON. |
| Terahertz 1/220 | Taxonomy prose | OK | Verified from taxonomy JSON. |
| Shared front-end 194/220 | Taxonomy prose | OK | Verified from taxonomy JSON. |
| Direct 118/220 and coherent 97/220 | Taxonomy prose | OK | Verified from taxonomy JSON. |
| Ranging 162/220 | Taxonomy prose | OK | Preserved from previous taxonomy audit; no contradictory repository value found. |
| `39 photonic-THz anchors` vs `terahertz 1/220` | Taxonomy compact table | QUALIFIED | Reworded to `39 direct photonic-THz anchors` and added prose stating this is an anchor-level tag within mostly hybrid records, not a separate medium total. Verified from `review_package/COMST_review_bundle_01_manuscript.md`. |
| 225 scenario points from 220 papers | Section V | OK | `analysis/V_ev_v2/section5C_tradeoff_points.csv` has 226 rows, but one row is the documented `O_ISAC_347` asset-mismatch anomaly. Excluding it yields 225 rows and 220 unique papers. |
| 20 rate + `\Delta r_{\min}` | Section V | OK | Verified from filtered Section V CSV. |
| 16 rate + `\sigma_r`/RMSE | Section V | OK | Verified from filtered Section V CSV. |
| 13 full triplet | Section V | OK | Verified from filtered Section V CSV. |
| 53 governed usable scenarios | Section V | OK | Verified from filtered Section V CSV. |
| 172 blocked scenarios | Section V | OK | Verified from filtered Section V CSV. |
| 197 rate records, 190 electrical SNR records, 169 OSNR records | Section V-A | OK | Verified from filtered Section V CSV. |
| 195 `\Delta r_{\min}`, 173 eligible, 186 `\sigma_r`, 148 CRB, 161 `\Delta z` | Section V-B | OK | Verified against previous Section V bundle and consistent with filtered synthesis. |
| 170 CRQ-candidate, 20 CRQ-valid, 2 Pareto points | Section V-C | OK | Verified from filtered Section V CSV and prior Section V bundle. |
| 299 MAJOR violations across 169 papers | Section V-A/V-B/V-C | OK | Verified from previous Section V audit bundle; preserved as governance-audit context. |
| Enabler counts ML 53 / ORIS 8 / OPA 7 | Not present as exact counts in main manuscript | OK | Did not add exact counts. |
| Application counts 15 domains / 8 domains / industrial 65 / vehicular 60 / indoor 56 / 6G networking 46 | Not present in main manuscript | OK | Did not add exact counts. |

## Conclusion

No unverified numerical claim was added. The only corrected/qualified issue was the 39 photonic-THz anchor wording, which now distinguishes anchor-level evidence from the explicit terahertz medium count.
