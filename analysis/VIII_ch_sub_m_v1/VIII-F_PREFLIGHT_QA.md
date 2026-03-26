# VIII-F Preflight QA

## Scope Evidence

- Quote: "Axis-2 Challenge domains: standardization_interoperability, hardware_scalability_efficiency, channel_modeling_evaluation, security_privacy_reliability, deployment_convergence_roadmap."
- Locator: `analysis/VIII_ev_v1/axis_definitions.md:L4`
- Interpretation lock: `VIII-F` not listed in Axis-2 domains -> treated as **CAPSTONE synthesis**.

## Gate Status

| Gate | Status | Evidence |
|---|---|---|
| G0 intent lock | PASS | `analysis/man_v1/section_intent_manifest.yaml` -> `section_VIII_intent: Open Challenges and Research Roadmap` |
| G1 build/style lock | PASS | `analysis/man_v1/build_contract.md` + `analysis/man_v1/stylekit_paths.md` opened |
| G2 axis-domain interpretation | PASS | `axis_definitions.md` includes A–E only; VIII-F treated as capstone |

## section8F Assets Existence Check

| file | exists |
|---|---|
| `analysis/VIII_ev_v1/s8f_dep_cov.csv` | PASS |
| `analysis/VIII_ev_v1/s8f_pap_chal_map.csv` | PASS |
| `analysis/VIII_ev_v1/section8F_research_agenda.csv` | PASS |
| `analysis/VIII_ev_v1/section8F_summary.json` | PASS |
| `analysis/VIII_ev_v1/section8F_summary_table.csv` | PASS |

## Cite-Key Existence Summary (Agenda Shortlist Union)

| cite_key | in_data/references.bib |
|---|---|
| O_ISAC_133 | FOUND |
| O_ISAC_156 | FOUND |
| O_ISAC_161 | FOUND |
| O_ISAC_145 | FOUND |
| O_ISAC_142 | FOUND |
| O_ISAC_049 | FOUND |
| O_ISAC_138 | FOUND |
| O_ISAC_030 | FOUND |
| O_ISAC_093 | FOUND |
| O_ISAC_107 | FOUND |

- Missing keys: none

## Contract-Violations Summary (Selected Keys)

| cite_key | violations_status | note |
|---|---|---|
| O_ISAC_133 | OK | normal wording allowed |
| O_ISAC_156 | FLAGGED | downgrade required |
| O_ISAC_161 | FLAGGED | downgrade required |
| O_ISAC_145 | FLAGGED | downgrade required |
| O_ISAC_142 | FLAGGED | downgrade required |
| O_ISAC_049 | OK | normal wording allowed |
| O_ISAC_138 | FLAGGED | downgrade required |
| O_ISAC_030 | OK | normal wording allowed |
| O_ISAC_093 | FLAGGED | downgrade required |
| O_ISAC_107 | FLAGGED | downgrade required |

- Totals: `FLAGGED=7`, `OK=3`

## Path-Resolution Method and Coverage

- Primary index: `analysis/man_v1/file_index.csv` (path contains key probe)
- Fallback index: `analysis/II_md_inv.csv` (`paper_id -> markdown_path`)
- Hit summary (selected keys): `HIT_PRIMARY=0`, `HIT_FALLBACK=10`, `MISS=0`

| cite_key | resolution | duplicate_paths | resolved_markdown_paths |
|---|---|---|---|
| O_ISAC_133 | HIT_FALLBACK | N | `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_133\O_ISAC_133\O_ISAC_133.md` |
| O_ISAC_156 | HIT_FALLBACK | N | `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_156\O_ISAC_156\O_ISAC_156.md` |
| O_ISAC_161 | HIT_FALLBACK | N | `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_161\O_ISAC_161.md` |
| O_ISAC_145 | HIT_FALLBACK | N | `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_145\O_ISAC_145\O_ISAC_145.md` |
| O_ISAC_142 | HIT_FALLBACK | N | `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_142\O_ISAC_142\O_ISAC_142.md` |
| O_ISAC_049 | HIT_FALLBACK | Y | `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_049\O_ISAC_049.md`; `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_049\O_ISAC_049\O_ISAC_049.md` |
| O_ISAC_138 | HIT_FALLBACK | N | `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_138\O_ISAC_138\O_ISAC_138.md` |
| O_ISAC_030 | HIT_FALLBACK | Y | `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_030\O_ISAC_030.md`; `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_030\O_ISAC_030\O_ISAC_030.md` |
| O_ISAC_093 | HIT_FALLBACK | Y | `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_093\O_ISAC_093.md`; `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_093\O_ISAC_093\O_ISAC_093.md` |
| O_ISAC_107 | HIT_FALLBACK | N | `c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_107\O_ISAC_107\O_ISAC_107.md` |

## Readiness Decision

Readiness rule: PASS only if `(8-12 agenda items selected) AND (all cite keys exist) AND (>=1 markdown path per cited key)`.

- Derivation note: domain priorities come from `section8F_research_agenda.csv`; candidate agenda itemization is expanded via `s8f_pap_chal_map.csv`.

- agenda_items_selected: 10 (PASS)
- all_cite_keys_exist: YES (PASS)
- markdown_path_per_key: YES (PASS)

- READY: PASS
