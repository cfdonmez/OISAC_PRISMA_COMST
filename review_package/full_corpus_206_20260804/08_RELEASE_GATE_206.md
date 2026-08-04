# Full-Corpus 206-Study Release Gate

Date: 2026-08-04
Package status: **READY FOR REVIEWED MANUSCRIPT INTEGRATION**
Active manuscript status: **NOT YET MIGRATED**

## Passed source and analysis gates

- [x] Phase A eligibility locked: 272 reports assessed; 227 primary, 39 excluded, 6 contextual.
- [x] Phase B report mapping locked: 227 eligible reports → 206 studies.
- [x] Phase C PRISMA flow locked and internally reconciled.
- [x] Phase D extraction/governance QA PASS: 8,306 claims, 72 quarantined, 31 context-only.
- [x] Primary synthesis denominator locked at 8,203 claims.
- [x] Phase E TQAF covers 206/206 studies with no blank final score.
- [x] Phase E cap/guardrail QA PASS.
- [x] Frozen Phase-E crosswalk reconciled to the authoritative final Phase-D workbook: 9,476 comparisons, 0 mismatches.
- [x] Phase F S1–S7 synthesis reconciles to the Phase-D claim ledger.
- [x] Exclusive S1/S5/S7 fields match the frozen Phase-E 206-study crosswalk.
- [x] Multi-label fallback inflation guard applied; unmatched tokens retained in audit.
- [x] English Methods, PRISMA Results, claim-governance, TQAF, and S1–S7 fragments created.
- [x] Evidence-grounded Abstract and Discussion/Roadmap/Conclusion drafts created.
- [x] Included-studies appendix regenerated as 206 study rows with 227-report lineage and no local-path leakage.
- [x] Public-package absolute workstation paths removed or parameterized without changing scientific fields or locked source hashes.
- [x] Final package-level QA recorded in `14_RELEASE_QA_FINAL_2026-08-04.json`: PASS for reviewed manuscript integration.
- [x] Combined fragment-level LaTeX compilation PASS (fatal errors 0; overfull boxes 0).
- [x] Independent-human provenance boundary explicitly stated.

## Required integration sequence

1. Review and integrate `01_METHODS_PRISMA_206_EN.tex`.
2. Integrate `02_RESULTS_PRISMA_206_EN.tex` and the locked Phase-C PRISMA figure.
3. Integrate `03_CLAIM_GOVERNANCE_EN.tex` without relabeling claim-use classes as quality grades.
4. Integrate `06_PHASE_E_TQAF_RESULTS_EN.tex`.
5. Replace legacy corpus-derived Section IV–VIII results with `07_PHASE_F_S1_S7_RESULTS_EN.tex` and the final Phase-F tables.
6. Integrate `09_ABSTRACT_206_EN.tex` and `10_DISCUSSION_CONCLUSION_206_EN.tex`, then align their cross-references with the final section order.
7. Integrate `11_INCLUDED_STUDIES_206.tex`, preserving its 206-study unit and separate 227-report lineage.
8. Run citation-key, cross-reference, IEEEtran compilation, float/layout, and rendered-PDF QA.

## Blocking checks before submission

- [ ] No active prose claims a 220- or 221-study corpus.
- [ ] No active PRISMA figure uses the legacy 980/280/700/478/222/2/220 flow.
- [ ] All prevalence figures/tables were regenerated rather than denominator-edited.
- [ ] `8,234` is never called the primary synthesis universe; primary = `8,203`.
- [ ] Context-only and quarantined claims do not support primary technical conclusions.
- [ ] Multi-label totals are not summed or described as mutually exclusive prevalence.
- [ ] TQAF scores are not described as independently double-human-scored.
- [ ] The final limitations state `independent_human_status = not_documented` unless later independent review is actually performed and recorded.
- [ ] No `O_ISAC_*` citation key was changed through numerical replacement.
- [ ] Author-owned declarations (funding, conflicts, data availability, contributions) are completed.
- [ ] Final manuscript compiles and its rendered PDF passes visual inspection.

## Protected working file

`manuscript/finalManuscript/bare_jrnl_new_sample4.tex` already contains user edits and is intentionally not overwritten by this package. Integration must be performed as a separate, reviewed patch with a scoped diff.
