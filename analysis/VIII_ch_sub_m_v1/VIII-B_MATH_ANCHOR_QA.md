# VIII-B MATH ANCHOR QA

## PASS/FAIL Checklist

| Check | Status | Evidence |
|---|---|---|
| placeholders removed | PASS | D0/D1/D2/D3 contain no TODO/TBD/placeholder tokens |
| Section VIII intent lock | PASS | section_intent_manifest.yaml -> "Open Challenges and Research Roadmap" |
| axis label exact | PASS | axis_definitions.md Axis-2 includes exact `hardware_scalability_efficiency` |
| cite-key lock | PASS | used keys only: O_ISAC_134, O_ISAC_161, O_ISAC_171 (all in prior VIII-B runs and preflight patch) |
| bracket-safe math | PASS | D1 math block uses no square brackets |
| hardware-plane primacy | PASS | D1 constraints prioritize compute/latency/power/control overhead before performance optimization |
| plane separation | PASS | D1 explicitly labels `U_comm` as comm-plane and `U_sens` as sensing-plane |
| no-ghost-parameter | PASS | no numeric threshold in constraints; all cited numbers appear only in excerpt-backed evidence |
| D1 explanation length (120-200 words) | PASS | 130 words |
| single-option decision | PASS | D0 selects Option-2 only |

## Cite-Key Existence in references.bib

| cite_key | in_references.bib |
|---|---|
| O_ISAC_134 | YES |
| O_ISAC_161 | YES |
| O_ISAC_171 | YES |

## Contract Violations Check (section=8B)

- Source: analysis/VIII_ev_v1/contract_violations.csv
- Filtered keys: O_ISAC_134, O_ISAC_161, O_ISAC_171
- Rows found: 0
- Resolution action: N/A (no violation rows)

## Processed Markdown Validation Log

| cite_key | resolution method | resolved index path | opened markdown path | sections opened | excerpt locator(s) |
|---|---|---|---|---|---|
| O_ISAC_134 | HIT_FALLBACK | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_134\O_ISAC_134\O_ISAC_134.md | C:\Users\Süleyman\Drive'ým\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_134\O_ISAC_134\O_ISAC_134.md | Abstract L21; Intro L25; relevant L541/L549; Conclusion L553 | L21-L21, L541-L541, L549-L549 |
| O_ISAC_161 | HIT_FALLBACK | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_161\O_ISAC_161.md | C:\Users\Süleyman\Drive'ým\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_161\O_ISAC_161.md | Abstract L17; Intro L21; relevant L121/L602; Conclusion L620 | L17-L17, L121-L121, L602-L602 |
| O_ISAC_171 | HIT_FALLBACK | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_171\O_ISAC_171.md | C:\Users\Süleyman\Drive'ým\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_171\O_ISAC_171.md | Abstract L15; Intro L17; relevant L108/L158; Conclusion/Discussion L154 | L15-L15, L108-L108, L158-L158 |

## Path Resolution Method

- Primary: analysis/man_v1/file_index.csv
- Fallback: analysis/II_md_inv.csv
- Result (used keys): HIT_PRIMARY=0, HIT_FALLBACK=3

## SHA256

- D0 (VIII-B_MATH_ANCHOR_DECISION.md): `591853BCF7E746E4D4B4675093A54306028FC7FC2D8A3DD07C2F9BD3610042BF`
- D1 (VIII-B_MATH_ANCHOR.md): `F028D5D32E924929635FEF89BA46A6379D91E92BA34CDEC9C51E965BA0089338`
- D2 (VIII-B_MATH_ANCHOR_supp.md): `267F356BD46938B7BFDB03DA5D1346C650F00794988CECEF15C35E485B87AF3D`

## Final

- READY: PASS
