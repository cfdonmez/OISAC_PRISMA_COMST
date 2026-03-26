# VII-F Preflight QA Patch

## Scope Evidence (Replaced, Evidence-Backed from VII-F Summaries)
- Scope label retained from preflight: `cross-domain Section VII application view`.
- Evidence distribution statement: In VII-F, coverage spans top macro domains `smart_infrastructure`, `automotive_transportation`, and `indoor_environments`, with top micro domains `industrial_manufacturing`, `vehicular`, and `indoor_positioning`.
- Data-derived scope statement with numeric counts: `smart_infrastructure=204/221 (92.3%)`, `automotive_transportation=104/221 (47.1%)`, `indoor_environments=81/221 (36.7%)`, and `n_unique_micro_domains=48`.
- Locators used:
  - `section7F_summary.json:2-11` (JSON keys `$.n_total_papers=221`, `$.n_unique_micro_domains=48`, `$.n_multi_macro_domain_papers=157`)
  - `s7f_macro_med_cov.csv:2-4`
  - `s7f_micro_dom_cnts.csv:2-4`
  - `section7F_transfer_map.csv:2-39` (transfer relationships across macro domains and mediums)

## CiteKey-Existence Check (`data/references.bib`)
- `O_ISAC_038`: FOUND
- `O_ISAC_074`: FOUND
- `O_ISAC_143`: FOUND
- `O_ISAC_164`: FOUND
- `O_ISAC_011`: FOUND
- `O_ISAC_108`: FOUND
- `O_ISAC_187`: FOUND
- `O_ISAC_252`: FOUND

## CiteKey-Locator Consistency Table

| scenario_id | cite_keys | bib_ok | evidence_source_ok | path_ok | notes |
|---|---|---|---|---|---|
| S7F-01 | `O_ISAC_038`; `O_ISAC_074` | YES | YES | YES | `section7F_paper_macro_map.csv:39,75` and `cluster_map.csv:39,75` match cite keys exactly; both markdown paths exist. |
| S7F-02 | `O_ISAC_143`; `O_ISAC_164` | YES | YES | YES | `section7F_paper_macro_map.csv:143,164` and `cluster_map.csv:143,164` match cite keys exactly; nested path for `O_ISAC_143` exists and is valid. |
| S7F-03 | `O_ISAC_011`; `O_ISAC_108` | YES | YES | YES | `section7F_paper_macro_map.csv:12,108` and `cluster_map.csv:12,108` match cite keys exactly; nested path for `O_ISAC_108` exists and is valid. |
| S7F-04 | `O_ISAC_187`; `O_ISAC_252` | YES | YES | YES | `section7F_paper_macro_map.csv:173,191` and `cluster_map.csv:173,191` match cite keys exactly; both markdown paths exist. |

## Path-Resolution Method
- Primary lookup source: `analysis/man_v1/file_index.csv`
- Primary hits for selected cite keys: `0/8`
- Fallback source used: `analysis/II_md_inv.csv` -> `Y`
- Fallback hits: `8/8`
- Duplicate-folder path sanity: checked (`O_ISAC_143`, `O_ISAC_108`) and kept because files exist at those resolved paths.

## Unresolved Mismatches
- None.

## Readiness
- **PASS**
- Rationale: 4 scenarios retained, all cite keys found in `data/references.bib`, all evidence locators consistent with cite keys, and all scenario paths resolved.

