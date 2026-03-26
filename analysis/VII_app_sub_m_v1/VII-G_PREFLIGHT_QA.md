# VII-G Preflight QA

## Scope Evidence
- **Axis-definition status:** `analysis/VII_ev_v2/axis_definitions.md` does not explicitly map a subsection label for VII-G.
- **Direct scope quote (<=25 words):** “This report compares structured application tags (JSON) vs extracted evidence rows (raw and strict).”
- **Locator:** `analysis/VII_ev_v2/section7G_dual_view_report.md:3`
- **Scope-lock interpretation:** VII-G is locked as a dual-view comparison layer between structured domain flags and evidence-row (raw/strict) assignments.

## Cite-Key Existence Check
| cite_key | bib_status |
|---|---|
| `O_ISAC_010` | FOUND |
| `O_ISAC_024` | FOUND |
| `O_ISAC_017` | FOUND |
| `O_ISAC_021` | FOUND |
| `O_ISAC_058` | FOUND |
| `O_ISAC_071` | FOUND |
| `O_ISAC_070` | FOUND |
| `O_ISAC_356` | FOUND |

## Path-Resolution Method
- **Primary index:** `analysis/man_v1/file_index.csv` (key-level hits: `0`).
- **Fallback used:** `Y` (`analysis/II_md_inv.csv`).
- **Fallback resolution result:** `8/8` shortlisted cite-keys resolved to existing processed markdown paths.

## Readiness
- **Stoplight:** `PASS`
- **Why PASS:**
  - 4 scenarios selected.
  - All shortlisted cite keys exist in `data/references.bib`.
  - At least one processed markdown path resolved for each scenario (all four scenarios have resolved paths).
