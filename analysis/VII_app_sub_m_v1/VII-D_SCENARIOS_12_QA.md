# VII-D SCENARIOS_12 QA

## PASS/FAIL Checklist
- Placeholder markers scan: **PASS** (none in D1/D2).
- Intent gate (Section VII = Applications and Use Cases): **PASS** (`analysis/man_v1/section_intent_manifest.yaml`).
- Scope lock gate (`underwater_harsh`): **PASS** (`analysis/VII_app_sub_v1_micro/VII-D_PREFLIGHT_QA_PATCH_v2.md`).
- Plane separation (sensing-plane vs comm-plane explicitly separated): **PASS** (each scenario field 3 and field 4 are separated).
- Dominant-component lock: **PASS** (both scenarios labeled `Conventional`; OPA/ORIS not explicitly named in opened sections).
- Word count check (target 220-320): **PASS** (`254` words in D1).

## Cite-Key Existence (`data/references.bib`)
- `O_ISAC_127`: FOUND (`data/references.bib:780`)
- `O_ISAC_220`: FOUND (`data/references.bib:1128`)

## Processed Markdown Validation Log
- `O_ISAC_127`
  - Resolved path: `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md`
  - Opened Abstract/Intro: `**ABSTRACT**` line `23`; `I. INTRODUCTION` line `29`
  - Opened relevant method/results: `A. UNDERWATER OPTICAL CHANNEL MODEL` lines `95-99`; `C. PERFORMANCE METRICS AND RESULTS` lines `467-471`
  - Opened Conclusion/Limitations: `E. FIELD VALIDATION, SENSITIVITY ANALYSIS, AND LIMITATIONS` lines `529-531`; `VI. CONCLUSION` lines `573-575`
  - Excerpt locators recorded in D2: `23-23`

- `O_ISAC_220`
  - Resolved path: `data/proc_markdowns/O_ISAC_220/O_ISAC_220.md`
  - Opened Abstract/Intro: top summary line `9`; `1. INTRODUCTION` lines `13-23`
  - Opened relevant method/results: `2. PRINCIPLE OF THE PROPOSED ISAC SCHEME FOR THE ADVANCED SMART NETWORK` lines `25-33`; `4. RESULTS AND DISCUSSION` lines `134-136`
  - Opened Conclusion/Limitations: `5. CONCLUSION` lines `182-184`
  - Excerpt locators recorded in D2: `19-19`, `184-184`

## Path Resolution Method
- Primary source: `analysis/man_v1/file_index.csv`
- Primary hits for used cite-keys: `0/2`
- Fallback source: `analysis/II_md_inv.csv` -> `Y`
- Fallback hits: `2/2`

## SHA256
- `analysis/VII_app_sub_v1_micro/VII-D_SCENARIOS_12.md`: `dde66de8809084b79039ed00f38b91419c50e51551885c8f2b12b36bd23dea48`
- `analysis/VII_app_sub_v1_micro/VII-D_SCENARIOS_12_supp.md`: `b4b3467cab94c38ceb13f7e10fa0590c6a2140fa4cdec278d21be77781edbd6d`
