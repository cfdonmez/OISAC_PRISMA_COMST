# VIII-B CHALLENGES_12 QA

## PASS/FAIL Checklist

| Check | Status | Evidence |
|---|---|---|
| placeholders removed | PASS | D1/D2/D3 contain no TODO/TBD/placeholder tokens |
| Section VIII intent lock | PASS | section_intent_manifest.yaml -> "Open Challenges and Research Roadmap" |
| axis label exact | PASS | axis_definitions.md Axis-2 includes exact `hardware_scalability_efficiency` |
| PATCH preflight readiness | PASS | VIII-B_PREFLIGHT_QA_PATCH.md -> Status PASS |
| CONTEXT readiness gate | PASS | VIII-B_CONTEXT_QA.md -> READY PASS |
| motif diversity (cases differ) | PASS | selected Case_1 motif != selected Case_2 motif |
| case selection cardinality | PASS | exactly two cases selected: Case_1 + Case_2 |
| cite-key lock (selected two cases only) | PASS | used keys: O_ISAC_035, O_ISAC_237, O_ISAC_093, O_ISAC_095, O_ISAC_112 |
| evidence excerpts present | PASS | D2 includes 9 excerpts total (Case_1=4, Case_2=5; each <=25 words) |
| hardware-vs-plane separation | PASS | D1 keeps hardware-plane primary; comm/sensing-plane mentioned only as labeled conditional implication |
| D1 length in target range (220-320) | PASS | 275 words |

## Selected Cases (Locked)

- Case_1: `transceiver_sharing;rf_hardware_simplification;cost_reduction`
- Case_2: `power_budget;signal_chain_amplification;edge_latency`

## Cite-Key Existence in references.bib

| cite_key | in_references.bib |
|---|---|
| O_ISAC_035 | YES |
| O_ISAC_237 | YES |
| O_ISAC_093 | YES |
| O_ISAC_095 | YES |
| O_ISAC_112 | YES |

## Contract Violations Check (section=8B)

- Source: analysis/VIII_ev_v1/contract_violations.csv
- Filtered keys: O_ISAC_035, O_ISAC_237, O_ISAC_093, O_ISAC_095, O_ISAC_112
- Rows found: 0
- Resolution action: N/A (no violation rows)

## Processed Markdown Validation Log

| cite_key | resolution method | resolved index path | opened markdown path | sections opened | excerpt locator(s) |
|---|---|---|---|---|---|
| O_ISAC_035 | HIT_FALLBACK | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_035\O_ISAC_035.md | C:\Users\Süleyman\Drive'ým\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_035\O_ISAC_035.md | Abstract L5; Intro L9; relevant L44; Conclusion L291 | L44-L44 |
| O_ISAC_237 | HIT_FALLBACK | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_237\O_ISAC_237.md | C:\Users\Süleyman\Drive'ým\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_237\O_ISAC_237.md | Abstract L5; Intro L9; relevant L188/L351; Conclusion L521 | L11-L11, L188-L188, L351-L351 |
| O_ISAC_093 | HIT_FALLBACK | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_093\O_ISAC_093.md | C:\Users\Süleyman\Drive'ým\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_093\O_ISAC_093.md | Abstract L7; Intro L9; relevant L158; Conclusion L212 | L158-L158 |
| O_ISAC_095 | HIT_FALLBACK | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_095\O_ISAC_095\O_ISAC_095.md | C:\Users\Süleyman\Drive'ým\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_095\O_ISAC_095\O_ISAC_095.md | Abstract L9; Intro L27; relevant L53/L108; Conclusion L242 | L53-L53, L108-L108 |
| O_ISAC_112 | HIT_FALLBACK | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_112\O_ISAC_112\O_ISAC_112.md | C:\Users\Süleyman\Drive'ým\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_112\O_ISAC_112\O_ISAC_112.md | Abstract L9; Intro L13; relevant L371; Conclusion L493 | L371-L371 |

## Path Resolution Method

- Primary: analysis/man_v1/file_index.csv
- Fallback: analysis/II_md_inv.csv
- Result (used keys): HIT_PRIMARY=0, HIT_FALLBACK=5

## SHA256

- D1 (VIII-B_CHALLENGES_12.md): `DEA5A5536512103286F99B530E3E805B9E2C41EAD9250E423DD940CF78786D47`
- D2 (VIII-B_CHALLENGES_12_supp.md): `393B3C21A476CDA9F748ED4607BAF6EF868AAC02EBE41E1736FBDFD56D1A7BB6`

## Final

- READY: PASS
