# VII-D Preflight QA

## Scope Evidence (Evidence-Pack Distribution + Source Excerpts)
- In `section7D_evidence.csv`, `underwater_harsh` accounts for `298/298` rows (`100.00%`) in column `macro_domain`.
- Direct excerpt 1 (`O_ISAC_127`): "Underwater Optical Wireless Communication systems are subject to significant degradation due to dynamic salinity gradients."
  - Locator: `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md`, HeadingPath `**ABSTRACT**`, line span `23-23`.
- Direct excerpt 2 (`O_ISAC_220`): "is an ISAC configuration for subsea monitoring via telecommunication cables."
  - Locator: `data/proc_markdowns/O_ISAC_220/O_ISAC_220.md`, HeadingPath `1. INTRODUCTION`, line span `19-19`.
- Therefore, VII-D scope is locked to `underwater_harsh` for subsequent runs.

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

