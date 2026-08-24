# Current QA Index — updated 2026-08-24

## Governing status

The current local candidate status is
`PASS_CITATION_COMPLETE_FIGURES_ONLY`.

The active IEEEtran driver compiles to 23 pages. Tables I--VIII, declarations,
206/206 included-study citations, a 243-entry main bibliography, a 227-report
ST-01, and the journal supplement package are materialized and verified.
Figures 1--8 are the only missing content assets. Page optimization is deferred
until those assets are inserted.

This is the technical production state, not a claim that the author-reading
pass has ended. Sections I--V have been reviewed and approved. Section VI has
been revised as a four-part survey narrative and has passed scientific,
evidence-boundary, citation, style, build, and rendered-page QA. It remains
awaiting author rereading and approval. Sections VII--IX follow. The Abstract
is finalized last before figure production.

## Current control reports

1. `SECTION6_VALIDATION_RECONSTRUCTABILITY_SURVEY_FIRST_QA_2026-08-24.md/json`:
   governing Section VI wording, evidence boundaries, count reconciliation,
   compact Table VI, rendered pages 11--14, current main-PDF identity, and the
   author rereading point.
2. `SECTION5_CROSS_STUDY_COMPARISON_QA_2026-08-24.md/json`: governing V-D
   wording, metric and tradeoff comparison boundaries, carrier allocation,
   rendered pages 11--13, and the Section VI reading point. Its dated main-PDF
   identity is superseded by the Section VI report above.
3. `SECTION5_TRADEOFF_MECHANISMS_SURVEY_FIRST_QA_2026-08-24.md/json`: governing
   V-C wording, locked tradeoff denominators, family reconciliation,
   claim-adjacent citation boundaries, carrier allocation, rendered pages
   9--12, and the V-D reading point. Its dated main-PDF identity is superseded
   by the V-D report above.
4. `SECTION5_TABLE5_SURVEY_MAP_QA_2026-08-21.md/json`: governing compact Table V
   content and all three revised Metrics Across Functions units. Its dated
   main-PDF identity is superseded by the V-D report above.
5. `SECTION2_TABLE2_SURVEY_MAP_QA_2026-08-21.md/json`: governing compact Table II
   content, linked Section II prose, carrier allocation, and rendered pages
   2--4. Its dated main-PDF identity is superseded by the Section V report above.
6. `SECTION5_OPENING_SURVEY_FIRST_QA_2026-08-21.md/json`: approved Section V
   opening wording baseline. Its prior Table V layout identity is superseded by
   the compact survey-map report above.
7. `SECTION4_SURVEY_FIRST_QA_2026-08-20.md/json`: governing approved Section IV
   wording, Table IV and Figure 5 carrier allocation, citation placement, and
   adjacent transitions.
8. `MEMORY_HANDOFF_QA_2026-08-19.md/json`: continuity baseline; current reading
   position is advanced by the 2026-08-20 Section IV control report and the
   updated current-state files.
9. `SECTION3_AUTHOR_REREAD_PREP_QA_2026-08-19.md/json`: governing approved
   Section III wording, locked-eligibility alignment, adjacent transition, and
   its dated PDF snapshot. `FINAL_SECTION3_SURVEY_FIRST_QA_2026-08-17.md/json`
   remains the compression baseline.
10. `GLOBAL_SECTION_COHERENCE_QA_2026-08-17.md/json`: governing section-role,
   transition, terminology, citation-preservation, and current-build gate.
11. `FINAL_TABLE1_CONTRIBUTION_QA_2026-08-17.md/json`: governing editorial and
   package closeout after removing the reader-facing ST-RS1 annex and revising
   the contribution list.
12. `FINAL_CITATION_COMPLETION_QA_2026-08-16.md/json`: citation-completion
   baseline, superseded for current placement locations by the regenerated
   crosswalk and for the main-PDF identity by the V-D report above.
13. `FINAL_MAIN_CITATION_COVERAGE_206.md/json` and
   `CITATION_PLACEMENT_CROSSWALK_206.csv/xlsx`: regenerated 2026-08-24;
   206/206 studies, zero missing, 415 included-study citation uses, and the
   current active-source line locations.
14. `FINAL_COMPANION_DELIVERABLE_QA.md/json`: 227-report bibliography,
   companion provenance, and report-specific guardrails.
15. `PRISMA_2020_FINAL_LOCAL_REAUDIT_2026-08-14.md/json/csv`: 33 READY,
   2 PARTIAL, 0 OPEN, and 7 justified not applicable; both partial items are
   figure dependent.
16. `POSTFIX_INTEGRATED_QA_2026-08-13.md/json`: 32/32 live integrity gates,
   regenerated after the final prose and carrier corrections.
17. `FINAL_PRISMA_ITEM17_QA.md/json` and workbook QA: 206 included-study rows
   and primary report identities; the current ST-01 extension resolves all 227
   eligible reports through 227 combined bibliography entries.
18. `MANUSCRIPT_CLAIM_REAUDIT_2026-08-13.md/json`: sentence-level claim and
   denominator audit.
19. Journal evidence/reporting, S7, and workbook QA files under this directory
   govern the corresponding supplements. The 38-source contextual-synthesis
   matrix and its QA are retained only as an internal positioning audit.
20. `02_VISUAL_AND_TABLE_PLACEMENT_CONTRACT.md` governs the eight pending
   figures and records all eight tables as implemented.

## Superseded snapshots

The 14 August `FINAL_NONVISUAL_CLOSEOUT_QA`, undated `FINAL_*`, `INTERIM_*`, and
`BASELINE_*` architecture/integrity files, the pre-fix PRISMA re-audit, and the
undated `FINAL_VISUAL_CONTRACT_QA.*` are preserved only as audit history. They
predate the 206/206 main-text citation layer, 227-report ST-01, and V10 package.

## Remaining gates

- Reread and approve the revised Section VI, review Sections VII--IX in the same
  survey-first sequence, and finalize the Abstract last.
- Produce and insert Figures 1--8.
- Recompile, inspect every rendered page, and complete the figure-inclusive
  submission-layout pass.
- Complete author-controlled submission-portal and optional public-release
  actions.
