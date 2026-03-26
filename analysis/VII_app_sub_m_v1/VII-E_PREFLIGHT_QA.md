# VII-E Preflight QA

## Scope Evidence (Exact Axis Heading Quote)
> "Axis-2 Application macro domains: smart_infrastructure, indoor_environments, automotive_transportation, underwater_harsh, space_satellite."

Auxiliary scope-keyword support used from the same file:
> "Axis-3 Application metadata: study-level domain tags + scenario description + scenario labels."

## Cite-Key Existence Check (`data/references.bib`)
- `O_ISAC_089`: FOUND
- `O_ISAC_137`: FOUND
- `O_ISAC_187`: FOUND
- `O_ISAC_195`: FOUND

## Path-Resolution Method
- Primary lookup source: `analysis/man_v1/file_index.csv`
- Primary hits for selected cite keys: `0/4`
- Fallback source used: `analysis/II_md_inv.csv` -> `Y`
- Fallback hits: `4/4`
- Note: `analysis/VII_ev_v2/cluster_map.csv` has no explicit `cluster_id` column; scenario de-duplication was approximated using distinct `macro_domains_json` cluster profiles where available.

## Stoplight Readiness
- **PASS**
- Check results:
  - 4 scenarios selected: YES
  - All cite keys exist in `data/references.bib`: YES
  - At least one processed markdown path resolved per scenario: YES

