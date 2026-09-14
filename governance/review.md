# Introduction methods integration

Date: 2026-09-14

The author-approved plan in [plan.md](../handoff/maps/s3/plan.md) has been applied.
The manuscript now has eight main sections. Introduction I-C, Review
Methodology, contains a 189-word, two-paragraph summary between Related Surveys
and Scope and Contributions. The three technical contributions and the final
organization paragraph retain their roles.

## Content destinations

| Earlier element | Current location |
|---|---|
| III-A search and selection summary | Introduction I-C |
| Earlier Fig. 5 | Fig. 2, Introduction; `manuscript/figures/selection.svg` and `.pdf` |
| Detailed workflow and registration lineage | `supplement/methods.md`, with source mapping in `supplement/index.md` |
| Earlier Table III: analysis units | Supplementary methods, Table S1 |
| Extraction and original measurement conditions | Brief I-C summary, Section IV-A application, full supplementary methods |
| Earlier III-C TQAF definition and Fig. 6 | Section V opening and Fig. 8 |
| Synthesis and interpretation limits | I-C summary, technical sections, Section VII limitations, supplementary methods |

The old Section III source is preserved in `qa/review/section3.tex` and Git
history; it has been removed from the live manuscript. Existing source filenames
need not match the automatically assigned section numbers. The main input
manifest, Introduction roadmap, Section II transition and limitations reference
were updated. A redundant sentence announcing the three contribution themes
was removed; the substantive contributions are preserved.

## Reporting-location map

This map records current reporting locations, not a declaration that every
PRISMA item has been independently satisfied. No standalone PRISMA checklist
was found in the frozen v10 package; this location map must not be described
as a completed full checklist.

| Reporting content | Main manuscript | Detailed carrier |
|---|---|---|
| Eligibility | I-C | Methods: Review scope and eligibility; S-Protocol |
| Sources, dates, search strategies | I-C | Methods: Search sources and execution; S-Search |
| Selection process | I-C and Fig. 2 | Methods: Selection and review conduct; S-Protocol, S-Exclusions |
| Data collection and fields | I-C and IV-A | Methods: Extraction and units of analysis; S-Data Dictionary, S-Evidence |
| Effect measures and synthesis methods | Sections II and IV | Methods: Thematic synthesis and interpretation limits; S-Bodies |
| Technical appraisal and its limits | Section V | Methods: Technical appraisal; S-Appraisal, S-Protocol |
| Selection results and excluded reports | Fig. 2 | Methods: Selection; ST-01 and S-Exclusions |
| Registration and amendments | Archive access through I-C | Methods: Review conduct and registration history; S-Protocol |
| Materials access | I-C OSF footnote | Supplement index and source carriers |

TQAF is not substituted for a conventional risk-of-bias assessment or GRADE.
The explicit absence of formal publication-bias/sensitivity analyses remains
in the scientific supplement. Actual conduct and methodological limitations
are retained there. Editor-facing statements and internal QA are not scientific
manuscript content.

## Figure and manuscript verification

The selection figure is an editable 516 x 264 pt vector drawing with embedded
text and no raster image. Its smallest font is 8.8 pt at the manuscript width.
Each disposition branches from its corresponding stage. Seven arithmetic checks
preserve 1,733 records, 1,259 screened, 332 forwarded records, 330 sought reports,
272 assessed reports, 227 eligible reports, 206 studies and the separate 67
contextual records. All 21 companion reports remain included.

An independent source review found no blocking scientific or structural issue.
Original TQAF figure content and all pre-existing figure assets are preserved.
The final build and source checks are recorded in `qa/review/result.json`;
figure checks are in `qa/review/selection.json`.

Reading copy: `output/pdf/review.pdf`, 29 pages. I-C begins on page 2; the
selection flow is on page 3; TQAF is on page 18. The build has no undefined
citations/references, duplicate labels, missing figures, missing characters or
overfull boxes. Underfull typesetting notices are recorded separately. Final
render inspection is recorded in the QA result.

## Separate joint OSF task

The manuscript uses the final-state archive sentence explicitly requested by
the author. This revision did not update or publish anything on OSF. During the
joint OSF task, assemble the carrier files listed in the supplement index,
update the repository contents, and verify the final manuscript link against
the accessible archive. This task stays outside the manuscript narrative.

## GitHub transfer follow-up

The complete frozen v10 carrier package has now been copied into `supplement/v10/`, with portable links in the supplement index. The joint OSF update and remote archive verification remain open. See [current handoff](../handoff/state.md).
