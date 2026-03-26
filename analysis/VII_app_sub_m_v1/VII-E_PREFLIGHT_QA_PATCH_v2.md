# VII-E Preflight QA

## Scope Evidence (Evidence-Pack Distribution + Source Excerpts)
- In `section7E_evidence.csv`, `space_satellite` accounts for `329/329` rows (`100.00%`) in column `macro_domain`.
- Direct excerpt 1 (`O_ISAC_089`): "The introduction of inter-satellite links (ISLs) can significantly improve the throughput of the satellite network."
  - Locator: `data/proc_markdowns/O_ISAC_089/O_ISAC_089.md`, HeadingPath `Free Space Optical Communication for Inter-Satellite Link: Architecture, Potentials and Trends > lead paragraph`, line span `9-9`.
- Direct excerpt 2 (`O_ISAC_187`): "low-Earth-orbit (LEO) satellite networks offer broad coverage and low communication latency."
  - Locator: `data/proc_markdowns/O_ISAC_187/O_ISAC_187.md`, HeadingPath `1. Introduction`, line span `13-13`.
- Therefore, VII-E scope is locked to `space_satellite` for subsequent runs.

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

