# VII-B MATH_ANCHOR QA

## PASS/FAIL Checklist
- Placeholder markers: PASS.
- Intent compliance (applications/deployment only): PASS.
- Bracket-safe math (no square-bracket math forms): PASS.
- Metric-plane separation (comm-plane vs sensing-plane explicitly labeled): PASS.
- Enabling-tech honesty (no ORIS/OPA variables without evidence): PASS.
- Word count (`analysis/VII_app_sub_v1_micro/VII-B_MATH_ANCHOR.md`, target 90-160): PASS (`101` words).

## Cite-Key Existence (`data/references.bib`)
- `O_ISAC_011`: YES (line `78`).
- `O_ISAC_030`: YES (line `192`).
- `O_ISAC_108`: YES (line `664`).
- `O_ISAC_388`: YES (line `1350`).

## Processed Markdown Validation Log

### Path Resolution
1. Attempted resolution via `analysis/man_v1/file_index.csv`.
2. Result: no hits for anchor keys (`O_ISAC_108`, `O_ISAC_388`).
3. Fallback explicitly applied via `analysis/II_md_inv.csv`.
4. Resolved paths:
   - `O_ISAC_108` -> `data/proc_markdowns/O_ISAC_108/O_ISAC_108/O_ISAC_108.md`
   - `O_ISAC_388` -> `data/proc_markdowns/O_ISAC_388/O_ISAC_388.md`

### Opened-Section Log (for this run)
- `O_ISAC_108` -> `data/proc_markdowns/O_ISAC_108/O_ISAC_108/O_ISAC_108.md`
  - Abstract/Intro opened: lines `9`, `13`.
  - Methods/results opened: lines `43`, `139-141`, `227-235`.
  - Conclusion opened: lines `237-253`.
  - D2 excerpt locators used: lines `233`, `139`.
- `O_ISAC_388` -> `data/proc_markdowns/O_ISAC_388/O_ISAC_388.md`
  - Abstract/Intro opened: lines `5-11`.
  - Methods/results opened: lines `111-119`, `131-139`.
  - Conclusion/limitations opened: lines `185-189`.
  - D2 excerpt locators used: lines `117`, `139`.

### Additional Pool-Validation Log (Decision D1-D2)
- `O_ISAC_011` -> `data/proc_markdowns/O_ISAC_011/O_ISAC_011.md` (Abstract `15`, Intro `19`, results `145/153/165`, conclusion `173`).
- `O_ISAC_030` -> `data/proc_markdowns/O_ISAC_030/O_ISAC_030.md` (Abstract `5`, Intro `9`, results `214/292`, limitations `302`, conclusion `304`).

## Decision Trace
- Selected option: **Option-1 (joint trade-off)**.
- Exact supporting evidence used for option admissibility:
  - Communication-plane metric support: BER evidence (`O_ISAC_108:233`), corroborated by multi-user BER behavior (`O_ISAC_388:139`).
  - Sensing-plane metric support: coordinate MSE statement (`O_ISAC_108:139`).
  - Indoor deployment terms in `s`: room geometry (`O_ISAC_388:117`) and user-density/load effect (`O_ISAC_388:139`).
- Option-2 was not required because both planes are directly evidenced and a joint objective can be written without introducing non-evidenced ORIS/OPA variables.

## SHA256
- `analysis/VII_app_sub_v1_micro/VII-B_MATH_ANCHOR_DECISION.md`: `89ca54ee45157d197c80cea810396d4885f4f6a7641bb4a7fac199f6d27ac7ee`
- `analysis/VII_app_sub_v1_micro/VII-B_MATH_ANCHOR.md`: `5940119af24755bfad59aae31bdabb0026d3281d4d3e7d21453792e0bda6e740`
- `analysis/VII_app_sub_v1_micro/VII-B_MATH_ANCHOR_supp.md`: `89e1a8330a8790dbc393b74bf164e215a3d60a6d2578d570d2c3b631f7df53bc`
