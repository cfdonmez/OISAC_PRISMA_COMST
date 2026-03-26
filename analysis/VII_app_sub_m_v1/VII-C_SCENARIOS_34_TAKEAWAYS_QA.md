# VII-C SCENARIOS_34_TAKEAWAYS QA

RUN_MODE: `SCENARIOS_34_TAKEAWAYS`

## PASS/FAIL Checklist
- Placeholder-token check: PASS
- Intent gate (Section VII = `Applications and Use Cases`): PASS
- Scope lock (`automotive_transportation` from `VII-C_PREFLIGHT_QA_PATCH_v2.md`): PASS
- Preflight cite-key pool lock (only keys from `VII-C_PREFLIGHT.md`): PASS
- Run2 non-duplication (Scenario 3/4 add coverage beyond Scenario 1/2): PASS (`O_ISAC_003`, `O_ISAC_055` vs prior `O_ISAC_060`, `O_ISAC_164`)
- Plane separation (sensing-plane vs comm-plane metrics separated): PASS
- Dominant-component lock (OPA/ORIS/Hybrid only with explicit evidence): PASS (both labeled `Conventional`)
- C7 lexical cue in >=2 distinct cite-keys: PASS (`O_ISAC_003`, `O_ISAC_055` excerpts contain vehicle/V2V cues)
- C8 setup/geometry excerpt present: PASS (D2 excerpts include scenario setup and D=200 m LoS link)
- C9 metric semantics safety: PASS (`RMSE` used only with explicit RMSE excerpt; no unsupported accuracy/error claims)
- Word count gate for D1 (target 240-340): PASS (`329` words)
- Roadmap/challenges framing absent: PASS

## Cite-Key Existence (data/references.bib)
- `O_ISAC_003`: FOUND
- `O_ISAC_055`: FOUND

## Processed Markdown Validation Log
- Path resolution method:
  - `analysis/man_v1/file_index.csv`: no key-level hits for `O_ISAC_003`, `O_ISAC_055`
  - Fallback `analysis/II_md_inv.csv`: used (`Y`), hits found for both keys
- `O_ISAC_003`
  - Markdown path opened: `data/proc_markdowns/O_ISAC_003/O_ISAC_003.md`
  - Sections opened: `*Abstract*` (line `5`), `# I. INTRODUCTION` (lines `11`, `15`), `## *A. Simulation Scenario Set Up*` (line `33`), `## IV. CONCLUSIONS` (line `157`)
  - D2 locator coverage: `5-5`, `33-33`
- `O_ISAC_055`
  - Markdown path opened: `data/proc_markdowns/O_ISAC_055/O_ISAC_055.md`
  - Sections opened: `*Abstract*` (line `5`), `## I. INTRODUCTION` (lines `11`, `13`), `# II. SYSTEM MODEL` (line `33`), `#### IV. NUMERICAL RESULTS` (lines `212`, `226`), `#### V. CONCLUSION` (line `234`)
  - D2 locator coverage: `13-13`, `212-212`, `96-96`, `226-226`

## SHA256
- `analysis/VII_app_sub_v1_micro/VII-C_SCENARIOS_34_TAKEAWAYS.md`: `bfc2f6ca4b27fb8e9edbfd4739e1d636c7055a7b98d09a7959de804ada25bfba`
- `analysis/VII_app_sub_v1_micro/VII-C_SCENARIOS_34_TAKEAWAYS_supp.md`: `aebdab9e9502d1f33a056a5374e865845a335d0804a73534ad34a669bb02e092`
