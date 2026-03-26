# VII-E CONTEXT QA

## PASS/FAIL Checklist
- Placeholders (`TODO/TBD/FIXME/ELLIPSIZATION`): PASS
- Intent gate (Section VII = "Applications and Use Cases"): PASS
- Scope lock (`space_satellite` from `VII-E_PREFLIGHT_QA_PATCH_v2.md`): PASS
- Cite-key lock (only keys from `VII-E_PREFLIGHT.md`): PASS
- Cite-key existence in `data/references.bib`: PASS
- Lexical cue rule in D2 (>=2 excerpts, >=2 distinct cite-keys with satellite/space cues): PASS
- Word count for D1: PASS (`126` words; allowed `110-200`)

## Cite-Keys Used and Bib Verification
- `O_ISAC_089`: FOUND (`data/references.bib`: line 550)
- `O_ISAC_187`: FOUND (`data/references.bib`: line 1056)

## Processed Markdown Validation Log
- `O_ISAC_089` -> `data/proc_markdowns/O_ISAC_089/O_ISAC_089.md`
  - Opened sections: `Abstract` (line 9), `Introduction` (line 13), `ACQUISITION, POINTING, AND TRACKING` (line 75), `Conclusion` (line 161)
  - Excerpt locators recorded in D2: `Abstract:9-9`, `ACQUISITION, POINTING, AND TRACKING:75-75`
- `O_ISAC_187` -> `data/proc_markdowns/O_ISAC_187/O_ISAC_187.md`
  - Opened sections: `Abstract` (line 7), `1. Introduction` (line 13), `2. Principle` (line 19), `6. Conclusion` (lines 398-402)
  - Excerpt locators recorded in D2: `1. Introduction:13-13`, `6. Conclusion:402-402`

## Path Resolution Method
- Primary source: `analysis/man_v1/file_index.csv`
- Primary hits for used cite-keys: `0/2`
- Fallback source: `analysis/II_md_inv.csv`
- Fallback used: `Y`
- Fallback hits: `2/2`

## SHA256
- `analysis/VII_app_sub_v1_micro/VII-E_CONTEXT.md`: `cd3d30af398b3258b57bd77309e90c02f6c6ba72da06f54d06d2f10f84cb63b0`
- `analysis/VII_app_sub_v1_micro/VII-E_CONTEXT_supp.md`: `6da1371e665833770ecef59754ee1b67b5f34f6d699b3b7ad29eb0b63dd0e274`
