# VIII-F Final QA

## PASS/FAIL Checklist

| Check | Status | Evidence |
|---|---|---|
| ph-token removal | PASS | `ph_token_hits=0` across D1+D2 |
| capstone interpretation | PASS | D1 states VIII-F is a capstone synthesis rather than a new Axis-2 domain |
| no new cite keys | PASS | cite-key union across D1+D2 = `{O_ISAC_049, O_ISAC_107, O_ISAC_133, O_ISAC_156}`; outside-union keys = none |
| no-causality language | PASS | `cause|causes|caused|therefore|will follow` scan on D1 = 0 |
| conservative phrasing preserved | PASS | FLAGGED keys `O_ISAC_156` and `O_ISAC_107` remain in `may require` phrasing and `wording_mode=conservative` rows |
| no-ghost-TRL | PASS | `TRL|time horizon|months|years` scan on D1 = 0 |
| bracket-safe math | PASS | display-math square-bracket scan = 0 |
| ORIS canon | PASS | D1 preserves VIII-F as capstone synthesis and keeps the prioritization model labeled as a survey-level organizational scaffold |
| word count | PASS | D1 `word_count=566` |

## Cite-Key List and Bibliography Verification

| cite_key | in_data/references.bib | evidence |
|---|---|---|
| O_ISAC_049 | YES | `data/references.bib:L306` |
| O_ISAC_107 | YES | `data/references.bib:L658` |
| O_ISAC_133 | YES | `data/references.bib:L816` |
| O_ISAC_156 | YES | `data/references.bib:L954` |

## Artefact-Derived Agenda Integrity Note

- PASS: artefact-derived agenda items remain labeled as such in D1 and are not restated as stand-alone literature claims.
- `F-AG05` retains `evidence_keys = agenda:D; depcov:D`.
- `F-AG06` retains `evidence_keys = agenda:E; depcov:E; summary:n_deployment_convergence_roadmap_papers`.
- `F-AG07` retains `evidence_keys = summary_table:all; violations:used_keys`.

## Additional Integrity Checks

- supplement merge/de-dup: PASS (merged supplement keeps one copy of the duplicated `O_ISAC_049` excerpt and preserves the distinct `O_ISAC_107` and `O_ISAC_133` excerpt variants)
- duplicate-path decision preserved: PASS (`O_ISAC_049` nested canonical path retained)
- overclaim scan: PASS (`will|guarantee|guarantees|eliminate|eliminates|prevent|prevents` on D1 = 0)

## SHA256

- D1 `VIII-F.md`: `9B2EA48B2FCB36D6C4C643DAFB0329361A103B66469BF7C268CF21F381A1CA6B`
- D2 `VIII-F_supp.md`: `899B9AAD50BD35F44BDE979BE5A77A151B18B3C7C1A3FBBBDFEB5EF670C4ABA5`

## Final

- READY: PASS
