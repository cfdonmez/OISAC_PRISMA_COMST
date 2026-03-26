# VIII-E CHALLENGES_12 QA

## PASS/FAIL Checklist

| Check | Status | Evidence |
|---|---|---|
| placeholders | PASS | marker scan across D1+D2 = 0 |
| intent lock | PASS | `analysis/man_v1/section_intent_manifest.yaml` -> `section_VIII_intent: Open Challenges and Research Roadmap` |
| axis exact (`deployment_convergence_roadmap`) | PASS | D1 contains exact axis token `deployment_convergence_roadmap` |
| cite-key lock | PASS | used keys in D1 = `{O_ISAC_039, O_ISAC_163}`; outside-lock keys = none |
| evidence excerpts present | PASS | D2 has 6 excerpts total (Case 1: 3, Case 2: 3), each with cite-key + locator, each <=25 words |
| conservative phrasing | PASS | overclaim token scan (`will|guarantees|eliminates|prevents`) = 0; downgrade wording retained |
| no-ghost-TRL | PASS | D1 has no TRL number, maturity score, or time-horizon threshold |
| length (220-320 words) | PASS | D1 word_count = 305 |

## Cite-Key Existence (data/references.bib)

| cite_key | in_references.bib |
|---|---|
| O_ISAC_039 | YES |
| O_ISAC_163 | YES |

## Contract-Violations Acknowledgement (used keys)

| paper_id | section | category | severity | reason | handling |
|---|---|---|---|---|---|
| O_ISAC_039 | 8E | EVIDENCE_WEAK | MINOR | deployment_convergence_roadmap lacks support gate (text anchors) | downgrade/conservative wording applied |
| O_ISAC_163 | 8E | EVIDENCE_WEAK | MINOR | deployment_convergence_roadmap lacks support gate (text anchors) | downgrade/conservative wording applied |

## Processed Markdown Validation Log

| cite_key | resolution | index entry used | opened markdown path | sections opened | excerpt locators |
|---|---|---|---|---|---|
| O_ISAC_039 | HIT_FALLBACK | `analysis/II_md_inv.csv:40` (duplicate also at row 276; canonical row 40 selected) | `data/proc_markdowns/O_ISAC_039/O_ISAC_039.md` | Abstract `L5`; Intro `L9`; Relevant `L25/L43`; Conclusion `L690/L692` | `L5`, `L5`, `L43` |
| O_ISAC_163 | HIT_FALLBACK | `analysis/II_md_inv.csv:97` | `data/proc_markdowns/O_ISAC_163/O_ISAC_163.md` | Abstract `L5`; Intro `L23`; Relevant `L90/L588`; Conclusion `L640/L642` | `L90`, `L5`, `L588` |

## Path Resolution Method

- Primary index: `analysis/man_v1/file_index.csv`
- Fallback index: `analysis/II_md_inv.csv`
- Hit summary (used keys): `HIT_PRIMARY=0`, `HIT_FALLBACK=2`, `MISS=0`

## SHA256

- D1 `VIII-E_CHALLENGES_12.md`: `E1166316C34DEF8D7AEED4902AB65722B8B0D4471FDCB0EA9FE5DFEBB9E3814C`
- D2 `VIII-E_CHALLENGES_12_supp.md`: `D771A49CC2F90ED4508B41636A60D39DA06BC0C5FB079FF7E5698AB30B1019C1`

## Final

- READY: PASS
