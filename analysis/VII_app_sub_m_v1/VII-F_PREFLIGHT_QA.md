# VII-F Preflight QA

## Scope Evidence (Exact Axis Heading Quote)
> "Axis-2 Application macro domains: smart_infrastructure, indoor_environments, automotive_transportation, underwater_harsh, space_satellite."

Auxiliary axis line used for scenario framing:
> "Axis-3 Application metadata: study-level domain tags + scenario description + scenario labels."

## Cite-Key Existence Check (`data/references.bib`)
- `O_ISAC_038`: FOUND
- `O_ISAC_074`: FOUND
- `O_ISAC_143`: FOUND
- `O_ISAC_164`: FOUND
- `O_ISAC_011`: FOUND
- `O_ISAC_108`: FOUND
- `O_ISAC_187`: FOUND
- `O_ISAC_252`: FOUND

## Path-Resolution Method Used
- Primary lookup: `analysis/man_v1/file_index.csv`
- Primary hits for selected cite keys: `0/8`
- Fallback lookup: `analysis/II_md_inv.csv`
- Fallback used: `Y`
- Fallback hits: `8/8`
- Scenario-level path coverage: `4/4` scenarios have at least one resolved processed markdown path.
- De-dup note: `analysis/VII_ev_v2/cluster_map.csv` does not expose an explicit `cluster_id`; duplicate avoidance was enforced via distinct macro-domain plus medium cluster profiles.

## Readiness
- **PASS**
- Criteria check:
  - 4 scenarios chosen: YES
  - All cite keys exist in `data/references.bib`: YES
  - At least one processed markdown path resolved per scenario: YES

