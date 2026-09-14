# Full Revision RC1 Technical QA

Date: `2026-09-01`

Status:
`RC1_TECHNICAL_QA_PASS__HUMAN_RELEASE_GATES_PENDING`

Scope: technical, scientific-consistency, traceability, build, and visual QA
for the isolated full-revision RC1. This record is not a G10 release decision.

## Frozen-authority preservation

| Check | Result |
|---|---:|
| Phase A--F authority manifest | 22/22 matched |
| G0 baseline manifest | 11/11 matched |
| Frozen ST-19 rows | 4,779 |
| Frozen ST-19 SHA-256 | `DAC20625EF18C97BAC289F6AA05C2E2A75172E14CC76745780DDEDF9B689C539` |
| Overleaf core manifest | 25/25 paths, sizes, and hashes matched |

The RC1 is maintained in the isolated full-revision worktree. It does not
overwrite the frozen 27-page G0 manuscript or any canonical Phase A--F record.

## Scientific and traceability checks

| Check | Result |
|---|---:|
| Included studies / eligible reports | 206 / 227 |
| Quantitative evidence reconciliation | 4,997 = 4,779 primary metric + 218 tradeoff rows |
| Phase-G records / studies / reports | 118 / 15 / 16 |
| Independent human source decisions | 236 |
| Full-row agreement / discrepancies | 118/118 / 0 |
| Canonical comparison groups / multi-study groups | 76 / 0 |
| Main-text anchors / cards | 18 / 8 |
| Context-only / supplement-only rows | 7 / 93 |
| Validation distribution | 98 laboratory, 9 simulation, 7 analytical, 2 mixed, 2 prototype/testbed, 0 field |
| Phase-G metric domains | 39 communication, 70 sensing, 9 joint, 0 implementation |
| ST-G01--ST-G09 row counts | 118, 16, 236, 0, 76, 18, 76, 0, 5 |

Table V, Figure 6, the five-step design workflow, and recipes R1--R5 were
checked against the 18-row evidence crosswalk and the source-bound conditions.
No cross-study pooling, common-unit normalization, platform ranking, or
deployment-readiness claim is introduced.

## Clean build and citation QA

- Build route: pdfLaTeX + BibTeX through `latexmk`, from a clean auxiliary
  state.
- Output: 29 pages, 621,479 bytes.
- RC1 SHA-256:
  `8212A0941F3A16578EE4B3962A01346B73156351140660563AED400A34657775`.
- Bibliography entries: 241.
- Undefined citations/references: 0.
- LaTeX/package warnings: 0.
- Overfull boxes: 0.
- Fatal build findings: 0.
- Underfull boxes: 9, informational only; none caused clipping or overlap.

## Visual PDF QA

The final RC1 was rendered at 180 dpi into 29 page images. All 29 pages were
inspected. Page headers, footers, two-column flow, figures, captions, tables,
section boundaries, and references showed no clipping or overlap. Particular
checks passed for Table V on page 12, Figure 6 on page 14, Figure 7 on page 17,
Table VII on page 21, and Table VIII on page 23.

## Workbook and supplement QA

- Workbook: 12 sheets, 172,869 bytes.
- Workbook SHA-256:
  `4D61F834736850F474B77D5657D191768A0895BCD88B735AC7E114421B991559`.
- Export/reopen summary: exact expected values.
- Formula-error scan: 0.
- Sheet previews produced and visually inspected: 12/12.
- Active human-review records use anonymous roles and the review date; no
  personal-name or tool-activity disclosure is recorded in those active
  records.
- The historical source-only lock remains identifiable by its old hashes; the
  current G7 analysis lock supersedes it explicitly without changing canonical
  data.

## Release boundary

Technical QA is complete. G8 still requires authorized human scientific
approval; G9 still requires human data-steward approval; G10 still requires two
independent final-manuscript readers and explicit all-author release signoff.
Until those records exist, this PDF remains RC1 and is neither final release nor
submission-ready.
