# VII-D MATH ANCHOR QA

## PASS/FAIL Checklist
- Placeholder scan: **PASS** (no placeholder markers found).
- Intent gate (Section VII = Applications and Use Cases): **PASS** (`analysis/man_v1/section_intent_manifest.yaml`).
- Scope lock (`underwater_harsh`): **PASS** (`analysis/VII_app_sub_v1_micro/VII-D_PREFLIGHT_QA_PATCH_v2.md`).
- Bracket-safe math: **PASS** (no square-bracket math tokens in D1 math block).
- Metric-plane separation: **PASS** (comm-plane terms `R_comm`, `Q_comm`; sensing-plane terms `J_sense`, `S_sal`, `T_res`).
- Enabling-tech honesty: **PASS** (no ORIS/OPA/RIS phase variables introduced).
- No-ghost-parameter safety: **PASS** (no unsupported depth/distance/wavelength/salinity-gradient symbol introduced in D1).
- Word count (required 90-180 words for D1): **PASS** (`99` words).

## Cite-Key Existence (`data/references.bib`)
- `O_ISAC_220`: FOUND (`data/references.bib:1128`)
- `O_ISAC_027`: FOUND (`data/references.bib:174`)

## Processed Markdown Validation Log
- `O_ISAC_220`
  - Resolved path: `data/proc_markdowns/O_ISAC_220/O_ISAC_220.md`
  - Opened Abstract/Intro: summary line `9`; `1. INTRODUCTION` lines `13-23`
  - Opened relevant methods/results: lines `128-136` (`Q factor` estimation and `100 km` discussion)
  - Opened Conclusion/Limitations: `5. CONCLUSION` lines `182-184`
  - Excerpts used in D2: line `19-19`, line `9-9`

- `O_ISAC_027`
  - Resolved path: `data/proc_markdowns/O_ISAC_027/O_ISAC_027.md`
  - Opened Abstract/Intro: `Abstract` line `7`; `I. INTRODUCTION` lines `27-35`
  - Opened relevant methods/results: `III. RESULTS AND DISCUSSION` lines `96-110`
  - Opened Conclusion/Limitations: `IV. CONCLUSION` lines `148-150`
  - Excerpts used in D2: line `150-150`

## Path Resolution Method
- Primary source: `analysis/man_v1/file_index.csv`
- Primary hits for anchor cite-keys: `0/2`
- Fallback source used: `analysis/II_md_inv.csv` -> `Y`
- Fallback hits: `2/2`

## Decision Trace
- Selected option: **Option-1 (Joint trade-off)**.
- Supported comm-plane items: `20 GBaud DP-QAM16 transmission`, `0.2 dB Q factor improvement` (`O_ISAC_220`).
- Supported sensing-plane items: `0.192 nm/‰ salinity sensitivity`, `1200.7 nm/RIU RI sensitivity` (`O_ISAC_027`), and `0.0625°C` temperature resolution (`O_ISAC_220`).
- Decision rationale file: `analysis/VII_app_sub_v1_micro/VII-D_MATH_ANCHOR_DECISION.md`.

## SHA256
- `analysis/VII_app_sub_v1_micro/VII-D_MATH_ANCHOR_DECISION.md`: `bf224f3b3aa27ce1276ab2d28a876ae0d6f0a5037627103211ce5b8260d87908`
- `analysis/VII_app_sub_v1_micro/VII-D_MATH_ANCHOR.md`: `2a2315ff466d8958aa7a98a9b02ad08bb0fdcd49e7963bd68a1cbe335d94bbf9`
- `analysis/VII_app_sub_v1_micro/VII-D_MATH_ANCHOR_supp.md`: `40e77cdac6f08d157f16497505bd66369732eb5804c5afff095cb09beaefd172`
