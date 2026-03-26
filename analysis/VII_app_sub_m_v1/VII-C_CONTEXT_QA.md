# VII-C CONTEXT QA

RUN_MODE: `CONTEXT`

## PASS/FAIL Checklist
- Placeholders (`TODO/TBD/FIXME`): PASS
- Section intent gate (Section VII = "Applications and Use Cases"): PASS
- Scope lock gate (`automotive_transportation` proven in `VII-C_PREFLIGHT_QA_PATCH_v2.md`): PASS
- Cite-key lock (used keys must be in `VII-C_PREFLIGHT.md`): PASS
- Cite-key existence in `data/references.bib`: PASS
- Lexical cue rule for D2 (>=2 excerpts, >=2 distinct cite-keys, direct vehicle/V2X cues): PASS
- Word count gate for D1 (110-185 allowed; target 120-170): PASS (`137` words)
- Roadmap/challenges framing absent in D1: PASS
- Metric-plane separation constraint (if metrics mentioned): PASS (no metric claims used)

## Cite-Keys Used in D1
- `O_ISAC_003` -> FOUND in `data/references.bib`
- `O_ISAC_164` -> FOUND in `data/references.bib`

## Processed Markdown Validation Log
- Path resolution method:
  - `analysis/man_v1/file_index.csv`: no key-level hits for `O_ISAC_003`, `O_ISAC_164`
  - Fallback `analysis/II_md_inv.csv`: used (`Y`), hits found for both keys
- `O_ISAC_003`:
  - Markdown path opened: `data/proc_markdowns/O_ISAC_003/O_ISAC_003.md`
  - Sections opened: `*Abstract*` (line `5`), `# I. INTRODUCTION` (lines `11`, `15`), `## *A. Simulation Scenario Set Up*` (line `33`), `## IV. CONCLUSIONS` (line `157`)
  - Excerpt locators recorded in D2: lines `5-5`, `15-15`
- `O_ISAC_164`:
  - Markdown path opened: `data/proc_markdowns/O_ISAC_164/O_ISAC_164.md`
  - Sections opened: `#### **Abstract**` (line `17`), `# **1. Introduction**` (line `33`), `### *2.1. OC-ISAC Architecture*` (line `55`), `# **6. Conclusions**` (lines `434-440`)
  - Excerpt locators recorded in D2: lines `33-33`, `55-55`

## SHA256
- `analysis/VII_app_sub_v1_micro/VII-C_CONTEXT.md`: `2281d8f87a084777c5168c97f714b94f461afd76c0efdcb165c34db81be0cef0`
- `analysis/VII_app_sub_v1_micro/VII-C_CONTEXT_supp.md`: `8ed256807f6ac26e51de3727dfdfc8b41d41250234d521114d575b338a7aa12c`
