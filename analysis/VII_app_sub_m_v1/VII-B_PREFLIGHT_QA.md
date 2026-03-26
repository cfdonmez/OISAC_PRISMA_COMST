# VII-B Preflight QA

## Scope Evidence
| Item | Evidence |
|---|---|
| Axis heading | "Section 7 Axis Definitions (v2)" |
| Macro-domain definition | "Axis-2 Application macro domains: smart_infrastructure, indoor_environments, automotive_transportation, underwater_harsh, space_satellite." |
| VII-B official title lock | `Indoor Environments` (derived from Axis-2 token `indoor_environments`) |

## Scenario Scope Evidence (Quote Heading Name)
| Scenario ID | Cite key | Quoted heading name (`section7B_evidence.csv:heading_path`) | Strength used |
|---|---|---|---|
| S1 | `O_ISAC_011` | "Retroreflective Optical ISAC Supporting 3D Positioning in Indoor Environments" | DIRECT lexical |
| S2 | `O_ISAC_030` | "I. INTRODUCTION" | DIRECT lexical |
| S3 | `O_ISAC_108` | "Optical Integrated Sensing and Communication with Light-Emitting Diode > III. SYNERGIES BETWEEN OPTICAL SENSING AND OPTICAL COMMUNICATION > VI. CONCLUSION" | DIRECT lexical |
| S4 | `O_ISAC_388` | "Introduction" | DIRECT lexical |

## Cite-Key Existence (`data/references.bib`)
| Cite key | Exists |
|---|---|
| `O_ISAC_011` | YES |
| `O_ISAC_030` | YES |
| `O_ISAC_108` | YES |
| `O_ISAC_388` | YES |

## Path-Resolution Method
1. Attempted per-key lookup in `analysis/man_v1/file_index.csv`.
2. Result: 0 hits for all shortlisted keys.
3. Fallback applied: `analysis/II_md_inv.csv` using `paper_id`.

## Path-Resolution Log
| Cite key | `file_index.csv` hits | Resolved via | Processed markdown path | Exists |
|---|---|---|---|---|
| `O_ISAC_011` | 0 | `analysis/II_md_inv.csv` | `data/proc_markdowns/O_ISAC_011/O_ISAC_011.md` | YES |
| `O_ISAC_030` | 0 | `analysis/II_md_inv.csv` | `data/proc_markdowns/O_ISAC_030/O_ISAC_030.md` | YES |
| `O_ISAC_108` | 0 | `analysis/II_md_inv.csv` | `data/proc_markdowns/O_ISAC_108/O_ISAC_108/O_ISAC_108.md` | YES |
| `O_ISAC_388` | 0 | `analysis/II_md_inv.csv` | `data/proc_markdowns/O_ISAC_388/O_ISAC_388.md` | YES |
