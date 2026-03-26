# VIII-E CONTEXT QA

## PASS/FAIL Checklist

| Check | Status | Evidence |
|---|---|---|
| placeholders removed | PASS | template-marker scan across D1+D2 = 0 |
| axis label exact (`deployment_convergence_roadmap`) | PASS | D1 contains exact axis token `deployment_convergence_roadmap` |
| cite-key lock | PASS | used keys in D1 = `{O_ISAC_039, O_ISAC_163, O_ISAC_200}`; outside-lock keys = none |
| evidence excerpts present | PASS | D2 has 3 excerpts (one per used key), each with cite-key + locator, each <=25 words |
| conservative phrasing (violation-aware mode) | PASS | overclaim token scan (`prevents|guarantees|eliminates`) = 0; modal phrasing (`may/can/suggests/requires`) retained |
| length in range (130-190 words) | PASS | D1 word_count = 136 |
| no-ghost-TRL | PASS | D1 contains no TRL number or maturity threshold statement |

## Cite-Key Existence (data/references.bib)

| cite_key | in_references.bib |
|---|---|
| O_ISAC_039 | YES |
| O_ISAC_163 | YES |
| O_ISAC_200 | YES |

## Contract-Violations Acknowledgement (cited keys)

| paper_id | section | category | severity | reason | handling |
|---|---|---|---|---|---|
| O_ISAC_039 | 8E | EVIDENCE_WEAK | MINOR | deployment_convergence_roadmap lacks support gate (text anchors) | downgrade/conservative wording applied |
| O_ISAC_163 | 8E | EVIDENCE_WEAK | MINOR | deployment_convergence_roadmap lacks support gate (text anchors) | downgrade/conservative wording applied |
| O_ISAC_200 | 8E | EVIDENCE_WEAK | MINOR | deployment_convergence_roadmap lacks support gate (text anchors) | downgrade/conservative wording applied |

## Processed Markdown Validation Log

| cite_key | resolution | index entry used | opened markdown path | sections opened | excerpt locator |
|---|---|---|---|---|---|
| O_ISAC_039 | HIT_FALLBACK | `analysis/II_md_inv.csv:40` (duplicate also at row 276; canonical row 40 selected) | `data/proc_markdowns/O_ISAC_039/O_ISAC_039.md` | Abstract `L5`; Intro `L9`; Relevant `L25`; Conclusion `L690-L692` | `L5-L5` |
| O_ISAC_163 | HIT_FALLBACK | `analysis/II_md_inv.csv:97` | `data/proc_markdowns/O_ISAC_163/O_ISAC_163.md` | Abstract `L5`; Intro `L23`; Relevant `L90`; Conclusion `L640-L642` | `L90-L90` |
| O_ISAC_200 | HIT_FALLBACK | `analysis/II_md_inv.csv:113` | `data/proc_markdowns/O_ISAC_200/O_ISAC_200.md` | Intro `L27`; Relevant `L280-L282`; Conclusion `L354-L356` | `L282-L282` |

## Path Resolution Method

- Primary index: `analysis/man_v1/file_index.csv`
- Fallback index: `analysis/II_md_inv.csv`
- Hit summary (used keys): `HIT_PRIMARY=0`, `HIT_FALLBACK=3`, `MISS=0`

## SHA256

- D1 `VIII-E_CONTEXT.md`: `0D70E75560A4A725F15AE3C8F6A0C78D96AD2F638C2D68A81726C1878D2516A5`
- D2 `VIII-E_CONTEXT_supp.md`: `1066E90EB6BEC3114A9B31BBFE539B0AA2E518392BB308FD7690F13C49466105`

## Final

- READY: PASS
