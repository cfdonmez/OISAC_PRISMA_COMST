# VII-D Preflight QA

## Scope Evidence
- Exact axis string used: "Axis-2 Application macro domains: smart_infrastructure, indoor_environments, automotive_transportation, underwater_harsh, space_satellite."
- Scope lock used for VII-D: `underwater_harsh`.

## Cite-Key Existence Check (`data/references.bib`)
- `O_ISAC_127`: FOUND
- `O_ISAC_220`: FOUND
- `O_ISAC_020`: FOUND
- `O_ISAC_027`: FOUND

## Path-Resolution Method
- Primary lookup source: `analysis/man_v1/file_index.csv`
- Primary hits for selected cite keys: `0/4`
- Fallback source used: `analysis/II_md_inv.csv` -> `Y`
- Fallback hits: `4/4`
- Note: `analysis/VII_ev_v2/cluster_map.csv` has no explicit `cluster_id` column; cluster diversity was approximated using distinct `macro_domains_json` profiles where available.

## Stoplight Readiness
- **PASS**
- Check results:
  - 4 scenarios selected: YES
  - All cite keys exist in `data/references.bib`: YES
  - At least one processed markdown path resolved per scenario: YES

