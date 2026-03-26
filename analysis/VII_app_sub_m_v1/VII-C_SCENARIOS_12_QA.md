# VII-C SCENARIOS_12 QA

RUN_MODE: `SCENARIOS_12`

## PASS/FAIL Checklist
- Placeholders (`TODO`/`TBD`/`FIXME`): PASS
- Intent gate (Section VII = `Applications and Use Cases`): PASS
- Scope lock gate (`automotive_transportation` from `VII-C_PREFLIGHT_QA_PATCH_v2.md`): PASS
- Preflight cite-key pool lock (only keys from `VII-C_PREFLIGHT.md`): PASS
- Plane separation gate (sensing-plane vs comm-plane metrics separated in each scenario): PASS
- Dominant-component lock (OPA/ORIS/Hybrid only if explicit; otherwise Conventional): PASS
- Scenario excerpt coverage gate (>=1 excerpt per scenario in D2): PASS
- Word count gate for D1 (target 220-300): PASS (`285` words)

## Cite-Key Existence (data/references.bib)
- `O_ISAC_060`: FOUND
- `O_ISAC_164`: FOUND

## Processed Markdown Validation Log
- Path resolution method:
  - `analysis/man_v1/file_index.csv`: no key-level hits for `O_ISAC_060`, `O_ISAC_164`
  - Fallback `analysis/II_md_inv.csv`: used (`Y`), hits found for both keys
- `O_ISAC_060`
  - Resolved markdown path opened: `data/proc_markdowns/O_ISAC_060/O_ISAC_060.md`
  - Opened sections for validation: Abstract (line `27`), `### I. INTRODUCTION` (line `33`), `#### II. SYSTEM MODEL` (line `55`), `#### III. SIMULATION ANALYSIS` (lines `155-197`), `## IV. CONCLUSION` (line `199`)
  - D2 locators recorded: lines `55-55`, `197-197`
- `O_ISAC_164`
  - Resolved markdown path opened: `data/proc_markdowns/O_ISAC_164/O_ISAC_164.md`
  - Opened sections for validation: `#### **Abstract**` (line `17`), `# **1. Introduction**` (line `33`), `### *2.1. OC-ISAC Architecture*` (line `55`), `#### 5.3. Normalized Gains for Communication and Sensing` (line `410`), `# **6. Conclusions**` (lines `434-440`)
  - D2 locators recorded: lines `55-55`, `410-410`

## Additional Contract Notes
- Cluster separation check: `cluster_map.csv` contains no explicit `cluster_id` column; selected scenarios use distinct macro profiles (`automotive_transportation;smart_infrastructure` vs `automotive_transportation`).
- Dominant-component evidence: explicit OPA/ORIS mentions were not found in opened markdowns; both scenarios labeled `Conventional`.

## SHA256
- `analysis/VII_app_sub_v1_micro/VII-C_SCENARIOS_12.md`: `b1fb7c188532ae5c2ad1d315397b7a9a01664ab7ba27461364ba7110e297f65e`
- `analysis/VII_app_sub_v1_micro/VII-C_SCENARIOS_12_supp.md`: `749e01f085a88bf2a1858fe9739358a2b6cd97c5d0eeb67ed5f7e1b5e34f033c`
