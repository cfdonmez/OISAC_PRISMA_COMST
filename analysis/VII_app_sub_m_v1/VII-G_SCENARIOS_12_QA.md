# VII-G SCENARIOS_12 QA

## PASS/FAIL Checklist
- Placeholders (`TODO/TBD/FIXME/ELLIPSIZATION`): **PASS**
- Intent discipline (method/contrast framing only): **PASS**
- Dual-view numeric safety (all numeric discrepancy claims cite comparison row IDs): **PASS**
- Cite-key lock (only keys from `VII-G_PREFLIGHT.md`): **PASS**
- Word count target 220-320: **PASS** (`273`)

## Cite-Key Existence (data/references.bib)
| cite_key | status |
|---|---|
| `O_ISAC_010` | FOUND |
| `O_ISAC_071` | FOUND |

## Processed Markdown Validation Log
| cite_key | resolved_path | sections opened | excerpt locator used |
|---|---|---|---|
| `O_ISAC_010` | `data/proc_markdowns/O_ISAC_010/O_ISAC_010.md` | Abstract (line 69), Introduction (line 75), Relevant section `II. EXPERIMENTAL SETUP` (line 85), Conclusion (line 139) | `IV. CONCLUSION`, line 141 |
| `O_ISAC_071` | `data/proc_markdowns/O_ISAC_071/O_ISAC_071.md` | Abstract (line 5), Introduction (line 9), Relevant section `III. EXPERIMENTAL RESULTS` (line 57), Conclusion (line 75) | `I. INTRODUCTION`, line 11 |

## Path Resolution Method
- `analysis/man_v1/file_index.csv` hits for used keys: `0`
- Fallback used: **Y**
- Fallback source: `analysis/II_md_inv.csv`
- Fallback resolution: both used keys resolved to existing markdown paths.

## SHA256
- `analysis/VII_app_sub_v1_micro/VII-G_SCENARIOS_12.md`  
  `fa520c4a495962c7ccc5ee293b69d9f446cb36aaf52d18f5a3df92f8954e3996`
- `analysis/VII_app_sub_v1_micro/VII-G_SCENARIOS_12_supp.md`  
  `daa2293a2bcd43ca1a0668fba03cc3cdb44bb4f70f4b3fc796aabf406bb664f2`
