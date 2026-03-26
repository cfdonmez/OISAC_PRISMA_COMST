# VII-C Preflight QA

## Scope Evidence (Evidence-Pack Distribution + Source Excerpts)
- In `section7C_evidence.csv`, `automotive_transportation` accounts for `1157/1157` rows (`100.00%`) in column `macro_domain`.
- Direct excerpt 1 (`O_ISAC_003`): "advancements in vehicle-to-vehicle (V2V) communication technology, which is crucial for improving road safety and traffic efficiency."
  - Locator: `data/proc_markdowns/O_ISAC_003/O_ISAC_003.md`, HeadingPath `# I. INTRODUCTION`, line span `11-11`.
- Direct excerpt 2 (`O_ISAC_164`): "typical V2X communication scenario based on OCC. While driving, vehicles exchange information with other vehicles (V2V) or infrastructure (V2I/I2V)"
  - Locator: `data/proc_markdowns/O_ISAC_164/O_ISAC_164.md`, HeadingPath `### *2.1. OC-ISAC Architecture*`, line span `55-55`.
- Therefore, VII-C scope is locked to `automotive_transportation` for subsequent runs.

## Cite-Key Existence Check (`data/references.bib`)
- `O_ISAC_003`: FOUND
- `O_ISAC_060`: FOUND
- `O_ISAC_055`: FOUND
- `O_ISAC_164`: FOUND

## Path-Resolution Method
- Primary lookup source: `analysis/man_v1/file_index.csv`
- Primary hits for selected cite keys: `0/4`
- Fallback source used: `analysis/II_md_inv.csv` -> `Y`
- Fallback hits: `4/4`
- Note: `analysis/VII_ev_v2/cluster_map.csv` has no explicit `cluster_id` column; distinct scenario selection was enforced via distinct `macro_domains_json` cluster profiles.

## Stoplight Readiness
- **PASS**
- Check results:
  - 4 scenarios selected: YES
  - All cite keys exist in `data/references.bib`: YES
  - At least one processed markdown path resolved per scenario: YES
