# VIII-F Agenda and Anchor QA

## PASS/FAIL Checklist
- placeholders: PASS (`placeholder_hits=0` across D1 and D2)
- capstone interpretation: PASS (D1 frames VIII-F as a capstone synthesis layer, not a new Axis-2 domain)
- no-causality language: PASS (`cause|causes|caused|therefore` scan on D1 = 0)
- cite-key lock: PASS (`D1` keys = `O_ISAC_049`, `O_ISAC_107`, `O_ISAC_133`, `O_ISAC_156`; outside-lock keys = none)
- conservative phrasing for FLAGGED keys: PASS (`F-AG03` and `F-AG04` use `may require`; `wording_mode=conservative`)
- no-ghost-TRL: PASS (`TRL` and invented-horizon scan on D1 = 0)
- excerpts present: PASS (4 excerpts in D2; each quote <=25 words)
- table present: PASS (`Table VIII-F-2` caption hit = 1)
- anchor present: PASS (`Survey-level organizational prioritization scaffold` hit = 1)
- paragraph length: PASS (first two paragraphs = 200 words)

- Overall verdict: **PASS**

## Cite-Key Existence (data/references.bib)
- `O_ISAC_049`: present (`data/references.bib:L306`)
- `O_ISAC_107`: present (`data/references.bib:L658`)
- `O_ISAC_133`: present (`data/references.bib:L816`)
- `O_ISAC_156`: present (`data/references.bib:L954`)
- Missing keys: none

## Contract-Violations Summary for Cited Keys
| cite_key | status | evidence | handling |
|---|---|---|---|
| O_ISAC_049 | OK | 0 matching rows in `contract_violations.csv` | normal wording retained |
| O_ISAC_107 | FLAGGED | `section=8C`, `category=EVIDENCE_WEAK`, `severity=MINOR` | conservative row title and wording mode |
| O_ISAC_133 | OK | 0 matching rows in `contract_violations.csv` | normal wording retained |
| O_ISAC_156 | FLAGGED | `section=8B`, `category=EVIDENCE_WEAK`, `severity=MINOR` | conservative row title and wording mode |

## Processed Markdown Validation Log
| cite_key | resolution | index entry used | opened markdown path | sections opened | excerpt locator |
|---|---|---|---|---|---|
| O_ISAC_049 | HIT_FALLBACK | `analysis/II_md_inv.csv:L266` (duplicate also at `L50`) | `data/proc_markdowns/O_ISAC_049/O_ISAC_049/O_ISAC_049.md` | `Abstract L9`; `Intro L25`; `Relevant L39`; `Conclusion L708` | `L39` |
| O_ISAC_107 | HIT_FALLBACK | `analysis/II_md_inv.csv:L209` | `data/proc_markdowns/O_ISAC_107/O_ISAC_107/O_ISAC_107.md` | `Abstract L9`; `Intro L13`; `Relevant L456`; `Conclusion L460` | `L456` |
| O_ISAC_133 | HIT_FALLBACK | `analysis/II_md_inv.csv:L183` | `data/proc_markdowns/O_ISAC_133/O_ISAC_133/O_ISAC_133.md` | `Abstract L9`; `Intro L13`; `Relevant L35`; `Conclusion L348` | `L35` |
| O_ISAC_156 | HIT_FALLBACK | `analysis/II_md_inv.csv:L160` | `data/proc_markdowns/O_ISAC_156/O_ISAC_156/O_ISAC_156.md` | `Abstract L9`; `Intro L173`; `Relevant L978`; `Conclusion L1006` | `L978` |

## Path Resolution Method
- Primary index checked: `analysis/man_v1/file_index.csv`
- Primary result: no cited paper IDs were resolvable from the primary index
- Fallback index used: `analysis/II_md_inv.csv`
- fallback hits: `4/4`
- duplicate-path decision: only `O_ISAC_049` had duplicates; the nested canonical path was selected

## SHA256
- `VIII-F_AGENDA_AND_ANCHOR.md`: `E7878CCB3F1406A59587CD16D0F56CFA6CE9D7AB9BF68D6060CEB4E27FEBC815`
- `VIII-F_AGENDA_AND_ANCHOR_supp.md`: `DDEBD50D8449E44BF5343E1D34ED0F1D51DEDD7D8101BC4C0C49FAFE866191AB`
