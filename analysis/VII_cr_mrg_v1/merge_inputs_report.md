# Section VII Merge Inputs Report (Preflight)

## Scope
This preflight validates merge readiness for `VII-A..VII-G` without generating any new Section VII manuscript text.

## 1) File Presence Check

| Subsection | Main file | QA file | Supplement file | Status |
|---|---|---|---|---|
| VII-A | `analysis/VII_app_sub_v1/VII-A.md` | `analysis/VII_app_sub_v1/VII-A_QA.md` | `analysis/VII_app_sub_v1/VII-A_supp.md` | OK |
| VII-B | `analysis/VII_app_sub_v1/VII-B.md` | `analysis/VII_app_sub_v1/VII-B_QA.md` | `analysis/VII_app_sub_v1/VII-B_supp.md` | OK |
| VII-C | `analysis/VII_app_sub_v1/VII-C.md` | `analysis/VII_app_sub_v1/VII-C_QA.md` | `analysis/VII_app_sub_v1/VII-C_supp.md` | OK |
| VII-D | `analysis/VII_app_sub_v1/VII-D.md` | `analysis/VII_app_sub_v1/VII-D_QA.md` | `analysis/VII_app_sub_v1/VII-D_supp.md` | OK |
| VII-E | `analysis/VII_app_sub_v1/VII-E.md` | `analysis/VII_app_sub_v1/VII-E_QA.md` | `analysis/VII_app_sub_v1/VII-E_supp.md` | OK |
| VII-F | `analysis/VII_app_sub_v1/VII-F.md` | `analysis/VII_app_sub_v1/VII-F_QA.md` | `analysis/VII_app_sub_v1/VII-F_supp.md` | OK |
| VII-G | `analysis/VII_app_sub_v1/VII-G.md` | `analysis/VII_app_sub_v1/VII-G_QA.md` | `analysis/VII_app_sub_v1/VII-G_supp.md` | OK |

Additional required inputs:
- `analysis/man_v1/build_contract.md`: present
- `analysis/man_v1/stylekit_paths.md`: present
- `data/references.bib`: present

## 2) QA Gate Check (STOP-IF-FAIL)

All subsection QA files were read and contain PASS-only checklists (no explicit failing gate item).

| QA file | Gate result |
|---|---|
| `VII-A_QA.md` | PASS |
| `VII-B_QA.md` | PASS |
| `VII-C_QA.md` | PASS |
| `VII-D_QA.md` | PASS |
| `VII-E_QA.md` | PASS |
| `VII-F_QA.md` | PASS |
| `VII-G_QA.md` | PASS |

**Stop condition:** Not triggered.

## 3) Cite-Key Union from Bracket Citations in VII-A..VII-G

Scan method: bracket-cite extraction across `analysis/VII_app_sub_v1/VII-[A-G].md` using regex `(?<=\[)[A-Za-z][A-Za-z0-9_]*(?=\])`.

Extracted cite-key union (29 keys):
- `O_ISAC_003`, `O_ISAC_005`, `O_ISAC_010`, `O_ISAC_011`, `O_ISAC_012`, `O_ISAC_020`, `O_ISAC_021`, `O_ISAC_027`, `O_ISAC_030`, `O_ISAC_034`, `O_ISAC_038`, `O_ISAC_048`, `O_ISAC_055`, `O_ISAC_060`, `O_ISAC_064`, `O_ISAC_070`, `O_ISAC_071`, `O_ISAC_074`, `O_ISAC_089`, `O_ISAC_108`, `O_ISAC_127`, `O_ISAC_137`, `O_ISAC_143`, `O_ISAC_164`, `O_ISAC_187`, `O_ISAC_195`, `O_ISAC_220`, `O_ISAC_276`, `O_ISAC_388`.

Bibliography verification against `data/references.bib`:
- All 29/29 keys found.
- Missing keys: none.

## 4) Merge Order Definition (No New Text Drafting)

Recommended camera-ready merge order:
1. `VII-A` Smart Infrastructure & Outdoor Urban Sensing-Communication
2. `VII-B` Indoor Environments
3. `VII-C` Automotive Transportation
4. `VII-D` Underwater and Harsh Maritime Deployments
5. `VII-E` Space and Satellite Deployments
6. `VII-F` Cross-Domain Application Synthesis
7. `VII-G` Dual-View Consistency Layer

Rationale:
- `VII-A..VII-E` provide vertical deployment slices.
- `VII-F` is explicitly cross-domain synthesis and should follow vertical slices.
- `VII-G` is explicitly a methodological dual-view consistency check and should close Section VII as an evidence audit layer.

## 5) Stylekit/Recipe Docs Opened for Jargon Gate

Opened inputs referenced by `analysis/man_v1/stylekit_paths.md`:
- `writing_recipes/COMST_master_recipe.md`
- `docs/surv_write_guide.md`
- `memory-bank/master_writing_guide.md`
- `memory-bank/introduction_templates.md`
- `memory-bank/body_section_templates.md`
- `writing_recipes/manifest.json`
- style anchor: `drafts/section6_20260217_143141/section_06_camera_ready.md`

## Preflight Verdict

**PASS**: inputs are merge-ready under current QA and citation-integrity gates.
