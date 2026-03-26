# Summary-Artifact Evidence (Anchor-B)

## Coverage(x) evidence rows
- Macro-domain weights \(W_d\):
  - `s7f_macro_med_cov.csv` row 2: `smart_infrastructure,204`
  - `s7f_macro_med_cov.csv` row 3: `indoor_environments,81`
  - `s7f_macro_med_cov.csv` row 4: `automotive_transportation,104`
  - `s7f_macro_med_cov.csv` row 5: `underwater_harsh,23`
  - `s7f_macro_med_cov.csv` row 6: `space_satellite,34`
- Micro-domain weights \(V_a\) (top micro domains used for coverage signal):
  - `s7f_micro_dom_cnts.csv` row 2: `industrial_manufacturing,66`
  - `s7f_micro_dom_cnts.csv` row 3: `vehicular,61`
  - `s7f_micro_dom_cnts.csv` row 4: `indoor_positioning,57`
  - `s7f_micro_dom_cnts.csv` row 5: `6g_networks,48`
- Incidence matrices \(M_{i,d}\) and \(U_{i,a}\):
  - Column schema from `section7F_paper_macro_map.csv` row 1 (`paper_id`, canonical domains, macro flags).
  - Example mapped rows used for sanity checks: row 12 (`O_ISAC_011`), row 108 (`O_ISAC_108`), row 143 (`O_ISAC_143`), row 164 (`O_ISAC_164`), row 173 (`O_ISAC_187`), row 191 (`O_ISAC_252`).
- Portfolio cardinality support:
  - `section7F_summary.json` key path `$.n_total_papers` = 221 (line 2).
  - `section7F_summary.json` key path `$.n_unique_micro_domains` = 48 (line 11).

## TransferPenalty(x) evidence rows
- Transfer-strength basis \(L_{d,q}\) from shared medium overlap in `section7F_transfer_map.csv`:
  - `hybrid` rows 3, 15, 25, 32, 36
  - `wireless_vlc` rows 13, 23, 30, 39
  - `cabled_fibre` rows 2, 14, 24, 31, 35
  - `wireless_fso` rows 9, 20, 27, 34, 37
- Explicit cross-domain transfer signals used:
  - Indoor and automotive share `hybrid` evidence: rows 15 and 25.
  - Indoor and automotive share `wireless_vlc` evidence: rows 23 and 30.

## Notes on cite-key metric constraints
- Anchor-B uses artifact-level coverage and transfer terms only.
- No paper-metric numeric constraint is introduced in the math block, so no processed-markdown metric excerpt is required for this anchor.
