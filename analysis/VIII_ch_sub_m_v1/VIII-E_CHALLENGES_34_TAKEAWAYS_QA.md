# VIII-E CHALLENGES_34_TAKEAWAYS QA

## PASS/FAIL Checklist

| Check | Status | Evidence |
|---|---|---|
| placeholders | PASS | marker scan across D1+D2 = 0 |
| intent lock | PASS | `analysis/man_v1/section_intent_manifest.yaml` -> `section_VIII_intent: Open Challenges and Research Roadmap` |
| axis exact (`deployment_convergence_roadmap`) | PASS | D1 contains exact axis token `deployment_convergence_roadmap` |
| cite-key lock | PASS | used keys in D1 = `{O_ISAC_151, O_ISAC_200}`; outside-lock keys = none |
| evidence excerpts present | PASS | D2 has 9 excerpts total (Case 3: 4, Case 4: 5), each with cite-key + locator, each <=25 words |
| conservative phrasing | PASS | overclaim token scan (`will|guarantees|eliminates|prevents`) = 0; downgrade wording retained |
| no-ghost-TRL | PASS | D1 has no TRL number/time-horizon threshold statement |
| takeaways discipline | PASS | bullets=4; each bullet has evidence citation or `working hypothesis` label; governance-actionable bullets >=2 |
| length (260-390 words) | PASS | D1 word_count = 359 |

## Cite-Key Existence (data/references.bib)

| cite_key | in_references.bib |
|---|---|
| O_ISAC_151 | YES |
| O_ISAC_200 | YES |

## Contract-Violations Acknowledgement (used keys)

| paper_id | section | category | severity | reason | handling |
|---|---|---|---|---|---|
| O_ISAC_151 | 8E | EVIDENCE_WEAK | MINOR | deployment_convergence_roadmap lacks support gate (text anchors) | downgrade/conservative wording applied |
| O_ISAC_200 | 8E | EVIDENCE_WEAK | MINOR | deployment_convergence_roadmap lacks support gate (text anchors) | downgrade/conservative wording applied |

## Processed Markdown Validation Log

| cite_key | resolution | index entry used | opened markdown path | sections opened | excerpt locators |
|---|---|---|---|---|---|
| O_ISAC_151 | HIT_FALLBACK | `analysis/II_md_inv.csv:165` | `data/proc_markdowns/O_ISAC_151/O_ISAC_151/O_ISAC_151.md` | Abstract `L9`; Intro `L13`; Relevant `L124/L126`; Conclusion `L232/L242` | `L126`, `L126`, `L124`, `L242` |
| O_ISAC_200 | HIT_FALLBACK | `analysis/II_md_inv.csv:113` | `data/proc_markdowns/O_ISAC_200/O_ISAC_200.md` | Intro `L27`; Relevant `L41/L280/L282/L286/L332`; Conclusion `L354/L356`; Limitations `L358` | `L41`, `L282`, `L332`, `L286`, `L358` |

## Path Resolution Method

- Primary index: `analysis/man_v1/file_index.csv`
- Fallback index: `analysis/II_md_inv.csv`
- Hit summary (used keys): `HIT_PRIMARY=0`, `HIT_FALLBACK=2`, `MISS=0`

## SHA256

- D1 `VIII-E_CHALLENGES_34_TAKEAWAYS.md`: `2F04926E4A75B3785FF6E9993E155E096865F26C2E4B0473A96A50E35AA2C069`
- D2 `VIII-E_CHALLENGES_34_TAKEAWAYS_supp.md`: `76B56D10EBF14271AB34837F1A01D5738CE672B11FB9F7DBCE049C872EF1F87A`

## Final

- READY: PASS
