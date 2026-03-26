# VII-B SCENARIOS_34_TAKEAWAYS QA

## Gate Status
- G0: PASS (`section_VII_intent = "Applications and Use Cases"` in `analysis/man_v1/section_intent_manifest.yaml`).
- G1: PASS (`analysis/man_v1/build_contract.md` and `analysis/man_v1/stylekit_paths.md` reviewed; referenced COMST docs opened).
- G2: PASS (VII-B official title/scope locked to `Indoor Environments` from `analysis/VII_ev_v2/axis_definitions.md`).
- G3: PASS (scope and cite-key pool match `analysis/VII_app_sub_v1_micro/VII-B_PREFLIGHT.md` and `analysis/VII_app_sub_v1_micro/VII-B_PREFLIGHT_QA.md`).

## PASS/FAIL Checklist
- Placeholders (`TODO`/`TBD`/`FIXME`): PASS.
- Intent discipline (applications/deployment only): PASS.
- Scope alignment (both scenarios indoor-aligned): PASS.
- Plane separation (sensing-plane vs communication-plane explicit): PASS.
- Dominant-component lock (`Conventional` unless explicit OPA/ORIS/Hybrid evidence): PASS.
- Indoor lexical cue in excerpts from >=2 distinct cite-keys: PASS (`O_ISAC_108`, `O_ISAC_388`).
- Setup/geometry excerpt present in D2: PASS (`O_ISAC_388`, lines 117-117).
- Cite-key lock (only preflight keys used): PASS (`O_ISAC_108`, `O_ISAC_388`).
- Word count (`D1`): PASS (`332`, target 240-340; fail guardrail 220-380).

## Cite-Key Existence (`data/references.bib`)
- `O_ISAC_108`: present (YES, entry line `664`).
- `O_ISAC_388`: present (YES, entry line `1350`).

## Path Resolution Method
1. Attempted resolution via `analysis/man_v1/file_index.csv`.
2. Result: no per-paper hits (`O_ISAC_108:0`, `O_ISAC_388:0`).
3. Fallback applied via `analysis/II_md_inv.csv`.
4. Resolved paths:
   - `O_ISAC_108` -> `data/proc_markdowns/O_ISAC_108/O_ISAC_108/O_ISAC_108.md`
   - `O_ISAC_388` -> `data/proc_markdowns/O_ISAC_388/O_ISAC_388.md`

## Processed Markdown Validation Log
- `O_ISAC_108`
  - Opened path: `data/proc_markdowns/O_ISAC_108/O_ISAC_108/O_ISAC_108.md`
  - Opened sections: Abstract (line 9), Intro (`### I. INTRODUCTION`, line 13), relevant method/results (`### II. PROBLEM FORMULATION`, line 43; `#### V. NUMERICAL AND SIMULATION RESULTS`, lines 227-233), Conclusion (`### VI. CONCLUSION`, lines 237-253).
  - D2 locator coverage: lines 43, 139, 233.
- `O_ISAC_388`
  - Opened path: `data/proc_markdowns/O_ISAC_388/O_ISAC_388.md`
  - Opened sections: Abstract (line 5), Intro (`# Introduction`, lines 9-13), relevant method/results (`### SIMULATION SETUP AND RESULTS`, lines 111-139), Conclusion (`# Conclusions`, lines 187-189).
  - D2 locator coverage: lines 11, 117, 139.

## Constraint-Specific Evidence Checks
- C7 (indoor cue in >=2 distinct cite-keys): PASS.
  - `O_ISAC_108` excerpt includes "indoor" (D2 line 6).
  - `O_ISAC_388` excerpt includes "indoor" (D2 line 21).
- C8 (setup/geometry evidence): PASS.
  - `O_ISAC_388` geometry excerpt records room dimensions (D2 line 26).

## SHA256
- D1 `analysis/VII_app_sub_v1_micro/VII-B_SCENARIOS_34_TAKEAWAYS.md`: `BA85EACC0599E272B7AD7A5DB9F873F54F17CE5F79DCB6A30B03F7ECC3ED4701`
- D2 `analysis/VII_app_sub_v1_micro/VII-B_SCENARIOS_34_TAKEAWAYS_supp.md`: `C55FACBF70B51EA99B27F7E93053952FB778DD266110940910645A7682A380BA`
