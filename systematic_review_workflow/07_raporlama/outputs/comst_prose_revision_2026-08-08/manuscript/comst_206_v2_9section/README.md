# O-ISAC COMST Survey: Nonvisual Review Candidate

## Current frozen state

This directory is the active survey-first reading candidate. It consolidates
the former 13-section draft into nine main sections using the descriptive
architecture of the locally audited 76-paper COMST corpus. The unpublished
220/221-study manuscript is not an evidence authority, and the preceding
`comst_206_v1` directory remains unchanged as a rollback source.

The citation-complete nonvisual closeout is complete. `main.tex` is the live
IEEEtran driver and compiles to 23 pages with all eight main-text tables
implemented and rendered. Every one of the 206 included studies is now cited
in a scientifically matched main-text context. The 243-entry main bibliography
contains those 206 studies, 29 contextual or methodological sources, and eight
companion reports used for report-specific claims. Electronic Supplement ST-01
maps all 227 eligible reports to the 206 studies and provides their complete
report bibliography. No figure asset is active: Figures 1--8 remain the only
unfinished content carriers. Figure insertion will require a final compile and
figure-inclusive layout pass; the page count is not being optimized before
that pass.

The current author-reading pass is separate from this machine-verified
baseline. Sections I--V have been reviewed and approved. Section V now closes
with Conditions for Comparison Across Studies, which applies the Section II
alignment rules and hands the argument directly to validation and
reproducibility. Planned Fig. 6 retains the detailed eleven-family evidence
profile. Section VI has been revised as a four-part survey narrative and has
passed scientific, citation, build, style, and rendered-page QA. It remains
awaiting author rereading and approval. Sections VII--IX remain for the same
pass, and the Abstract is finalized last. Figures are produced only after that
prose review is closed.

## Start here

1. Compile or read `main.tex`; it is the active manuscript driver.
2. Use `MANUSCRIPT_BODY_INPUTS.tex` for the authoritative reading order.
3. Read the ten fragments in `sections/` as one article: abstract followed by
   Sections I--IX.
4. Consult `SECTION_BY_SECTION_REVIEW_GUIDE_TR_2026-08-14.md` during the
   section-by-section author review.
5. Read `02_VISUAL_AND_TABLE_PLACEMENT_CONTRACT.md` before producing the eight
   pending figures. Tables I--VIII are already live.
6. Use `03_SUPPLEMENTARY_EVIDENCE_CONTRACT.md` together with the materialized
   files under `supplements/` for study-level and claim-level evidence.
7. Use `FRONT_MATTER_ACTIVE_2026-08-14.md` for the active title, authors,
   affiliations, correspondence, and reporting statements.
8. Treat the undated `qa/FINAL_VISUAL_CONTRACT_QA.md` and
   `qa/FINAL_VISUAL_CONTRACT_QA.json` as superseded pre-closeout snapshots;
   they describe one live table and 15 pending carriers and therefore do not
   describe the frozen manuscript.
9. Treat `qa/SECTION6_VALIDATION_RECONSTRUCTABILITY_SURVEY_FIRST_QA_2026-08-24.md/json`
   as the governing Section VI wording, evidence-boundary, compact Table VI,
   and current-PDF report. The section remains awaiting author approval. Treat
   `qa/SECTION5_CROSS_STUDY_COMPARISON_QA_2026-08-24.md/json` as the governing
   Section V closeout report whose dated PDF identity is now superseded. Treat
   `qa/SECTION5_TRADEOFF_MECHANISMS_SURVEY_FIRST_QA_2026-08-24.md/json` as the
   governing V-C wording, evidence-boundary, and citation report whose dated
   PDF identity is superseded by the Section V closeout report. Treat
   `qa/MEMORY_HANDOFF_QA_2026-08-19.md/json` as the continuity baseline,
   `qa/SECTION2_TABLE2_SURVEY_MAP_QA_2026-08-21.md/json` as the governing
   Section II and compact Table II current-text report, and
   `qa/SECTION5_TABLE5_SURVEY_MAP_QA_2026-08-21.md/json` as the governing
   Table V and Metrics Across Functions baseline whose dated PDF identity is
   superseded by the Section V closeout report, and
   `qa/SECTION5_OPENING_SURVEY_FIRST_QA_2026-08-21.md/json` as the approved
   opening baseline whose former Table V layout identity is superseded.
   Treat `qa/SECTION4_SURVEY_FIRST_QA_2026-08-20.md/json` as the approved
   Section IV report, `qa/SECTION3_AUTHOR_REREAD_PREP_QA_2026-08-19.md/json`
   as the approved Section III snapshot, and
   `qa/FINAL_SECTION3_SURVEY_FIRST_QA_2026-08-17.md/json` as the compression
   baseline. The verified submission supplement is
   `OISAC_COMST_SUPPLEMENT_FINAL_V10_2026-08-17.zip` at the project root; its
   SHA-256 is
   `4f140851568a667ac0b9dde0b57c104742b0f747f2abb28335cffe37fe61617d`.
   V4--V9 packages and the earlier closeout QAs are preserved as superseded
   snapshots.

## Completed in this candidate

- nine main sections, within the local COMST interquartile range of seven to
  nine;
- a live 23-page `main.tex` build with eight implemented tables, 206/206
  included studies cited in claim-matched prose or table context, 243 main
  bibliography entries, and no active figure assets;
- compact survey maps in Tables II and V that retain reader-facing comparison
  structure while assigning exact schema and record detail to the supplements;
- a standalone, citation-linked 206-study ST-01 supplement, 227-report
  bibliography and lineage, 21-report companion provenance layer, and 14-row
  report-specific guardrail register, with Item 17 and workbook QA under
  `qa/`;
- journal-facing evidence carriers for 3,020 primary evidence rows, 4,779
  primary metric rows, 404 governed and 402 substantive tradeoff rows, 206
  study-level TQAF rows, 115 evidence bodies, and 4,931 body-membership rows;
- a bounded 38-source contextual-synthesis register retained for internal
  positioning audit only, outside the 206-study denominator and excluded from
  the submission annexes;
- a 206-row S7 join and 12-study field/deployment subset, with six studies
  satisfying the narrower paired-function validation gate;
- a reporting supplement containing executed search records, protocol and
  amendment records, a 446-row data dictionary, and explicit conduct and
  reporting boundaries;
- active front matter with source-verified article metadata and the no-support
  and no-sponsor-role statement;
- evidence, manuscript-integrity, architecture, lineage, PRISMA, supplement,
  compilation, and rendered-layout checks recorded under `qa/`;
- eight figure specifications with distinct reader jobs, draft captions, data
  authorities, accessibility constraints, and nonduplication rules.

## Remaining work in order

- reread and approve the revised Section VI on validation evidence,
  reconstructability, and benchmark readiness;
- review Sections VII--IX in survey-first order and finalize the Abstract last;
- produce and insert Figures 1--8 from their locked specifications;
- after insertion, rerun compilation, rendered-page inspection, and the final
  submission-layout pass; and
- complete external submission-portal actions, including author ORCID
  authentication and supplement upload.

All prose, tables, references, supplementary evidence carriers, and local
nonvisual QA are complete. Public repository deposition remains an
external release action and does not change the locally complete evidence
package.

