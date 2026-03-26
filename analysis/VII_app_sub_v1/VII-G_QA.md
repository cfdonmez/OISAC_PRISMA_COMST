# VII-G Integrated QA

## Mandatory Gate Status
- `analysis/VII_app_sub_v1_micro/VII-G_PREFLIGHT_QA.md`: **PASS** (`Stoplight: PASS`).
- `analysis/VII_app_sub_v1_micro/VII-G_CONTEXT_QA.md`: **PASS**.
- `analysis/VII_app_sub_v1_micro/VII-G_SCENARIOS_12_QA.md`: **PASS**.
- `analysis/VII_app_sub_v1_micro/VII-G_SCENARIOS_34_TAKEAWAYS_QA.md`: **PASS**.

## Integrated Checklist
- Placeholder markers in final deliverables: **PASS** (`0` matches in D1 and D2).
- Flow order (Context -> Case 1-2 -> Case 3-4 -> Takeaways): **PASS**.
- Method/contrast framing only (no roadmap/challenges): **PASS**.
- No new cite keys beyond G micro-parts: **PASS** (used only `O_ISAC_010`, `O_ISAC_021`, `O_ISAC_070`, `O_ISAC_071`).
- Every case has both comparison row and examples row: **PASS** (Case1: rows #4/#9; Case2: #2/#4; Case3: #5/#12; Case4: #6/#16).
- Numeric delta statements carry comparison row IDs: **PASS**.
- `working hypothesis` label retained where used: **PASS**.
- Bracket-safe math (no square-bracket math forms): **PASS**.
- Word count target 520-780: **PASS** (`559` words).

## Cite Keys Used and Existence
| cite_key | source in D1 | references.bib status | bib locator |
|---|---|---|---|
| `O_ISAC_010` | Case 1, line 3 | FOUND | `data/references.bib:72` |
| `O_ISAC_021` | Case 3, line 7 | FOUND | `data/references.bib:138` |
| `O_ISAC_070` | Case 4, line 9 | FOUND | `data/references.bib:432` |
| `O_ISAC_071` | Case 2, line 5 | FOUND | `data/references.bib:438` |

## Numeric Row-Reference Validation (D1)
| D1 line | numeric statement summary | comparison row ref present |
|---|---|---|
| 1 | Context deltas `+137`, `+107`, `+101`, `+17` | Yes (`#4`, `#5`, `#2`, `#6`) |
| 3 | Automotive `76/213/104`, deltas `+137`, `+28` | Yes (`#4`) |
| 5 | Smart infrastructure `103/221/204`, deltas `+118`, `+101` | Yes (`#2`) |
| 7 | Underwater `16/123/23`, deltas `+107`, `+7` | Yes (`#5`) |
| 9 | Space `17/135/34`, deltas `+118`, `+17` | Yes (`#6`) |
| 11 | Cross-case strict/raw ratios `104/213`, `204/221`, `23/123`, `34/135` | Yes (`#4`, `#2`, `#5`, `#6`) |
| 14 | Takeaway deltas `+107` to `+7`, `+118` to `+17` | Yes (`#5`, `#6`) |
| 15 | Takeaway strict deltas `+101`, `+17` | Yes (`#2`, `#6`) |
| 17 | Bias takeaway strict deltas `+101`, `+28`, `+7`, `+17` | Yes (`#2`, `#4`, `#5`, `#6`) |

## Supplement Merge QA
- Excerpts de-duplicated across micro supplements: **PASS**.
- Combined G-artefact evidence block includes all used comparison rows: **PASS** (`#2`, `#4`, `#5`, `#6`).
- Combined G-artefact evidence block includes all used examples rows: **PASS** (`#9`, `#4`, `#12`, `#16`).
- Scope continuity locator retained: **PASS** (`analysis/VII_ev_v2/section7G_dual_view_report.md:3`).

## SHA256
- `analysis/VII_app_sub_v1/VII-G.md`
  `ea6f9df45d0f53a0c27ffcd9199025ff4e504b8a794557dd91380b4587c6a5a1`
- `analysis/VII_app_sub_v1/VII-G_supp.md`
  `db214ba2b7cc92a239d28f6ce0232b608c4581fe75e340636f86bc3359091d9f`
