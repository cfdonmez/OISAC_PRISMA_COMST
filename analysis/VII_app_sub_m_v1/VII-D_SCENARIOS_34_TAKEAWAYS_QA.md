# VII-D SCENARIOS_34_TAKEAWAYS QA

## PASS/FAIL Checklist
- Placeholder markers scan: **PASS** (none in D1/D2).
- Intent gate (Section VII = Applications and Use Cases): **PASS** (`analysis/man_v1/section_intent_manifest.yaml`).
- Scope lock (`underwater_harsh`): **PASS** (`analysis/VII_app_sub_v1_micro/VII-D_PREFLIGHT_QA_PATCH_v2.md`).
- Plane separation (sensing-plane vs comm-plane): **PASS** (both scenarios separate field 3 and field 4).
- Dominant-component lock: **PASS** (both scenarios labeled `Conventional`; no explicit OPA/ORIS statement in opened sections).
- Lexical cue in >=2 distinct cite-keys: **PASS** (`O_ISAC_020` excerpt includes "underwater/submarine"; `O_ISAC_027` excerpt includes "deep ocean").
- Setup/environment excerpt present: **PASS** (`O_ISAC_020` line `45-45`; `O_ISAC_027` line `96-96`).
- Word count (target 240-360): **PASS** (`328` words in D1).

## Cite-Key Existence (`data/references.bib`)
- `O_ISAC_020`: FOUND (`data/references.bib:132`)
- `O_ISAC_027`: FOUND (`data/references.bib:174`)

## Processed Markdown Validation Log
- `O_ISAC_020`
  - Resolved path: `data/proc_markdowns/O_ISAC_020/O_ISAC_020.md`
  - Opened Abstract/Intro: `ABSTRACT` lines `7-9`; `Introduction` lines `11-15`
  - Opened relevant method/results: `Photonic IntegratedSensingandCommunication TechnologyUsingSubmarineOpticalCables` lines `43-45`; `Ocean Wave AnalysisUsing Photonic ISAC withSubmarine Telecommunication Fiber` lines `49-51`
  - Opened Conclusion/Limitations: `Conclusion` lines `93-95`
  - Excerpt locators recorded in D2: `9-9`, `45-45`, `43-43`

- `O_ISAC_027`
  - Resolved path: `data/proc_markdowns/O_ISAC_027/O_ISAC_027.md`
  - Opened Abstract/Intro: `Abstract` line `7`; `I. INTRODUCTION` lines `27-35`
  - Opened relevant method/results: `II. PRINCIPLE AND DEVICE DESIGN` line `39`; `III. RESULTS AND DISCUSSION` lines `96-104`
  - Opened Conclusion/Limitations: `IV. CONCLUSION` lines `148-150`
  - Excerpt locators recorded in D2: `7-7`, `96-96`, `150-150`

## Path Resolution Method
- Primary source: `analysis/man_v1/file_index.csv`
- Primary hits for used cite-keys: `0/2`
- Fallback source: `analysis/II_md_inv.csv` -> `Y`
- Fallback hits: `2/2`

## SHA256
- `analysis/VII_app_sub_v1_micro/VII-D_SCENARIOS_34_TAKEAWAYS.md`: `4340b270161c1a3f442e0d49c4cd4d12e08fb1b1e01737a19d661079d970381f`
- `analysis/VII_app_sub_v1_micro/VII-D_SCENARIOS_34_TAKEAWAYS_supp.md`: `d8a783d117cbe6401295f6369bf68b405e88b79024642977e7d286fbe72a4a30`
