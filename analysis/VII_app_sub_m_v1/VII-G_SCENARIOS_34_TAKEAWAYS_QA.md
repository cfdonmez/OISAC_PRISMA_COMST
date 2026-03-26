# VII-G SCENARIOS_34_TAKEAWAYS QA

## PASS/FAIL Checklist
- Placeholders (`TODO/TBD/FIXME/ELLIPSIZATION`): **PASS** (no matches in D1/D2).
- Intent discipline (method/contrast framing only; no roadmap/challenges): **PASS**.
- Non-duplication vs Run2 domains (`automotive_transportation`, `smart_infrastructure`): **PASS** (used `underwater_harsh`, `space_satellite`).
- Dual-view numeric safety (numeric discrepancy statements tied to comparison rows): **PASS** (comparison rows #5 and #6).
- Cite-key lock (only keys from `VII-G_PREFLIGHT.md`): **PASS** (`O_ISAC_021`, `O_ISAC_070`).
- Word count target 240-360: **PASS** (`351`).
- Takeaways evidence discipline (each bullet supported by artefact refs or marked hypothesis): **PASS**.

## Cite-Key Existence (data/references.bib)
| cite_key | status | bib locator |
|---|---|---|
| `O_ISAC_021` | FOUND | `data/references.bib:138` |
| `O_ISAC_070` | FOUND | `data/references.bib:432` |

## Processed Markdown Validation Log
| cite_key | resolved_path | sections opened | excerpt locator used |
|---|---|---|---|
| `O_ISAC_021` | `data/proc_markdowns/O_ISAC_021/O_ISAC_021.md` | Abstract (lines 5-7), Introduction (lines 9-11), Relevant section `System Structure and Advantages of O-ISAC` (lines 39-41), Conclusion (lines 191-193) | Introduction line 11; Conclusion line 193 |
| `O_ISAC_070` | `data/proc_markdowns/O_ISAC_070/O_ISAC_070.md` | Abstract (line 5), Introduction (lines 9 and 27-31), Relevant section `IV. TRANSMISSION SYSTEM DEMONSTRATIONS` (lines 149-155), Conclusion (lines 205-207) | Abstract line 5; Conclusion line 207 |

## Path Resolution Method
- Primary index checked: `analysis/man_v1/file_index.csv`
- Primary index hits for used keys: `0`
- Fallback used: **Y**
- Fallback source: `analysis/II_md_inv.csv`
- Fallback resolution: `2/2` used cite-keys resolved to existing processed markdown paths.

## SHA256
- `analysis/VII_app_sub_v1_micro/VII-G_SCENARIOS_34_TAKEAWAYS.md`
  `0a5533aca86c9061534351c5c407d7ee5c28573ac8087c782076ff99cbcb4392`
- `analysis/VII_app_sub_v1_micro/VII-G_SCENARIOS_34_TAKEAWAYS_supp.md`
  `95130fa9d5db969ce14c7eae784dddebf41f9560c50dce5aad9385073aa94678`
