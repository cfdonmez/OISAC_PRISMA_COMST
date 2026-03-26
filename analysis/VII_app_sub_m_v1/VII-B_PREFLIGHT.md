# VII-B Preflight Plan + Cite-Key Shortlist

## Scope Lock
- source_file: `analysis/VII_ev_v2/axis_definitions.md`
- section_axis_heading: "Section 7 Axis Definitions (v2)"
- subsection_id: `VII-B`
- official_title: `Indoor Environments`
- title_derivation_rule: Axis-2 macro-domain order (2nd token = `indoor_environments`)
- scope_keywords: `indoor_environments`, `application macro domains`, `study-level domain tags`, `scenario description`, `scenario labels`

## Plan
1. Lock VII-B to macro-domain token `indoor_environments` from Axis-2.
2. Filter `analysis/VII_ev_v2/section7B_evidence.csv` for scenario candidates aligned with indoor scope keywords.
3. Keep 4 candidates with explicit indoor semantics and usable evidence rows.
4. Assign 1-3 cite keys per candidate (paper IDs).
5. Validate cite keys against `data/references.bib`.
6. Resolve processed markdown paths via `analysis/man_v1/file_index.csv`; fallback to `analysis/II_md_inv.csv`.

## Scenario Candidate Shortlist (Locked)
| Scenario ID | Scenario candidate (`section7B_evidence.csv:scenario_description`) | Scope keyword match | Cite keys (1-3) | Evidence snapshot (D/I/N/Rows) | Processed markdown path(s) |
|---|---|---|---|---|---|
| S1 | 3D positioning in indoor environments | indoor, positioning | `O_ISAC_011` | 2/2/3/7 | `data/proc_markdowns/O_ISAC_011/O_ISAC_011.md` |
| S2 | Hand gesture recognition using visible light communication | indoor-context VLC sensing | `O_ISAC_030` | 3/2/2/7 | `data/proc_markdowns/O_ISAC_030/O_ISAC_030.md` |
| S3 | Indoor optical communication and sensing using LED-based O-ISAC | indoor, communication, sensing | `O_ISAC_108` | 3/2/1/6 | `data/proc_markdowns/O_ISAC_108/O_ISAC_108/O_ISAC_108.md` |
| S4 | VLC-CDMA system for indoor multi-user scenario | indoor, multi-user, VLC | `O_ISAC_388` | 2/0/2/4 | `data/proc_markdowns/O_ISAC_388/O_ISAC_388.md` |

## Bib Existence Gate
- `O_ISAC_011`: present in `data/references.bib`
- `O_ISAC_030`: present in `data/references.bib`
- `O_ISAC_108`: present in `data/references.bib`
- `O_ISAC_388`: present in `data/references.bib`
