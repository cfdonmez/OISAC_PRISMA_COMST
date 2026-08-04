# O-ISAC Full-Corpus Manuscript Patch Package

Generated for controlled integration into the canonical manuscript after the
Phase A--F locks. This versioned package intentionally remains separate from
the user's dirty `manuscript/finalManuscript/` working file so that the
full-corpus migration can be reviewed as a scoped patch.

## Authoritative current counts

- Search window: 1 January 2020 to 22 June 2026.
- Records identified: 1,733.
- Duplicate records removed: 472.
- Records removed by automation: 0.
- Records removed for other metadata/platform reasons: 2.
- Records screened: 1,259.
- Records not advanced to retrieval: 927.
- Historical source-record retrieval queue: 332.
- Post-screening bibliographic aliases consolidated: 2.
- Unique reports sought: 330.
- Unique reports not retrieved: 58.
- Reports assessed for eligibility: 272.
- Full-text exclusions: 39.
- Full-text contextual-only reports: 6.
- Reports of included studies: 227.
- Studies included in the review: 206.
- Total contextual corpus: 67 records.
- Governed claims: 8,306.
- Claims eligible for qualitative synthesis: 3,206.
- Claims eligible for quantitative synthesis: 4,997.
- Context-only claims: 31.
- Quarantined claims: 72.
- Survey-ready studies: 175.
- Survey-ready studies with claim restrictions: 31.
- Conflict-register rows: 93.
- Explicit metric-conflict rows: 2.
- Primary synthesis claims: 8,203 (3,020 evidence, 4,779 metric, 404 trade-off).
- Inclusive governed non-quarantined claims: 8,234, including 31 context-only
  metrics that are excluded from primary synthesis.
- Study-level TQAF rows: 206; overall contribution = 6 low, 75 adequate, 125
  strong.
- S1--S7 evidence bodies: 115; certainty = 54 high, 47 moderate, 10 limited,
  and 4 unclear/non-substantive fallback bodies.
- Final-workbook invariance audit: 206 studies, 46 check families, 9,476
  comparisons, 0 mismatches and 0 failed studies.
- Independent full-corpus human verification: not documented.

## Locked full-corpus synthesis anchors

- Modality: photonic-THz 69, fiber 56, VLC/LiFi 38, FSO 31, hybrid optical 9,
  and other optical 3.
- Validation maturity: tier 2 = 32, tier 3 = 18, tier 4 = 78, tier 5 = 66,
  and tier 6 = 12.
- Open data: 13 open and 41 on request; open code/model availability was not
  documented for 197 studies, with 7 on request and 1 partial artifact.
- 6G relevance: 138 direct, 64 inferred, 1 weak, and 3 not applicable.
- S2 and S6 are multi-label. The ``other'' fallback is assigned only when no
  recognized category exists on that study/axis; final fallback counts are 0
  for integration, 19 for technology, and 15 for application.

## Integration order

1. Replace the stale review-methodology text with
   `01_METHODS_PRISMA_206_EN.tex`.
2. Replace the stale study-selection/PRISMA results and flow prose with
   `02_RESULTS_PRISMA_206_EN.tex`.
3. Insert `03_CLAIM_GOVERNANCE_EN.tex` after the data-extraction subsection or
   use it to replace the shorter governance paragraph in the Methods fragment.
4. Insert `06_PHASE_E_TQAF_RESULTS_EN.tex` as the appraisal-results layer.
5. Use `07_PHASE_F_S1_S7_RESULTS_EN.tex` and the attached Phase-F tables to
   replace legacy Section IV--VIII corpus-derived results.
6. Use `09_ABSTRACT_206_EN.tex` and `10_DISCUSSION_CONCLUSION_206_EN.tex` only
   after the Methods/Results fragments have been integrated and cross-checked.
7. Use `11_INCLUDED_STUDIES_206.tex` (or its CSV source) for the regenerated
   206-study appendix; its separate report-lineage field reconciles to 227
   eligible reports.
8. Consult `12_LATEX_FRAGMENT_QA.md` for the standalone syntax check.
9. Consult `13_PUBLIC_PACKAGE_SANITIZATION.md` for the path-only portability
   changes applied to the Git copies of Phase-E/F scripts and QA metadata.
10. Consult `14_RELEASE_QA_FINAL_2026-08-04.json` for the final package-level
   gate and the remaining manuscript/submission tasks.
11. Follow `08_RELEASE_GATE_206.md`; regenerate final figures rather than
   mechanically replacing 220 or 221 with 206.

## Current reporting boundary

The package reports locked Phase A--F facts and provides a safe English writing
layer for Methods, PRISMA Results, claim governance, TQAF, S1--S7 results, an
evidence-grounded Abstract, and Discussion/Roadmap/Conclusion. It does not
overwrite the active dirty manuscript, regenerate all figures, or establish
independent human verification. The 206-study appendix is complete and
machine-checked; manuscript integration and final figure regeneration remain
explicit release-gate tasks.
