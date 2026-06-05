# PASS2 Diff Audit

## Original vs Pass-1 Section Compression

| Section | Original line range | Pass-1 line range | Reduction severity | Re-expand? | Reason |
|---|---:|---:|---|---|---|
| Introduction | 43-358 | 44-82 | Severe | MUST RE-EXPAND | Motivation, related-survey gap, optical-vs-RF distinction, and contribution architecture became too thin. |
| Background / Metric Governance | 359-739 | 83-148 | Severe | MUST RE-EXPAND | Metric-governance explanation is central and needs survey-level explanation of receiver planes, modality split, and admissibility. |
| PRISMA / TQAF Methodology | 740-867 | 149-188 | Moderate/severe | SHOULD RE-EXPAND | Credibility markers remain but database/search rationale, eligibility, extraction schema, and synthesis logic need more detail. |
| Unified Taxonomy | 868-1309 | 189-226 | Severe | MUST RE-EXPAND | Cross-modality taxonomy is a core contribution; medium, integration, detection, and task axes need developed prose. |
| Trade-off Synthesis | 1310-1514 | 227-277 | Severe | MUST RE-EXPAND | This is the strongest scientific core; governed attrition and sparse CRQ subset need fuller explanation. |
| Enablers | 1515-1811 | 278-331 | Severe | SHOULD RE-EXPAND | ORIS, OPA, PIC, photonic high-frequency generation, ML/security, and reporting contract need representative synthesis. |
| Applications | 1812-2120 | 332-358 | Severe | SHOULD RE-EXPAND | Deployment motifs need enough prose to remain useful while staying non-scorecard. |
| Roadmap / Challenges | 2121-2557 | 359-412 | Severe | SHOULD RE-EXPAND | Needs to read like a COMST roadmap rather than a compressed audit summary. |
| Conclusion | 2558-2592 | 413-442 | Mild/moderate | KEEP COMPRESSED | Compact conclusion already preserves the main message. |

## Artifact-Level Compression

| Object class | Original | Pass-1 | Pass-2 action |
|---|---:|---:|---|
| Words in TeX source | 25400 | 4312 | Re-expand narrative selectively, not back to original length. |
| Main figures | 14 | 7 | Keep Pass-1 figure set; restore `fig_v_2` only if page budget requires and caption remains scoped. |
| Main tables | 24 | 12 | Keep compact table architecture; do not blindly restore large original tables. |
| Numbered equations | 56 | 3 | Keep compact math; do not restore organizational optimization equations. |

## Re-Expansion Priorities

- MUST RE-EXPAND: Introduction, Background/Metric Governance, Taxonomy, Trade-off Synthesis.
- SHOULD RE-EXPAND: PRISMA/TQAF, Enablers, Applications, Roadmap.
- KEEP COMPRESSED: Conclusion.
- KEEP IN SUPPLEMENT: notation/acronym tables, RF-vs-O-ISAC table, duplicate taxonomy/metric/enabler/application figures, audit tables, and organizational equations.

## Pass-2 Outcome

| Section | Pass-2 outcome | Notes |
|---|---|---|
| Introduction | Re-expanded | Restored motivation, optical-vs-RF distinction, related-survey gap, fragmentation logic, and contributions without restoring removed duplicate figures/tables. |
| Background / Metric Governance | Re-expanded and cleaned | Restored explanatory metric-governance prose; kept only compact core equations and left NLSE/multiobjective scaffolding out of main text. |
| PRISMA / TQAF Methodology | Re-expanded | Preserved PRISMA-S, OSF registration, database set, freeze date, N=220, TQAF, extraction, and corpus-ledger traceability without full search strings. |
| Unified Taxonomy | Re-expanded | Restored axis-level and modality-level explanation while keeping the compact figure/table architecture. |
| Trade-off Synthesis | Re-expanded strongly | Preserved 225 scenario points, 20/16/13 governed subsets, sparse CRQ-valid interpretation, and core figure/table set. |
| Enablers | Re-expanded | Restored family-level synthesis for ORIS, OPA, PIC, photonics-assisted high-frequency generation, ML/security, and reporting. |
| Applications | Kept compact | Five deployment motifs retained; full audit layer remains out of main text to protect page budget. |
| Roadmap / Challenges | Kept compact with selective re-expansion | Retained main roadmap figure, compact challenge table, and five-item agenda; internal audit/math scaffolding remains out. |
| Conclusion | Kept compact | Preserves the non-monolithic O-ISAC and metric-governance closing message. |

Final build result: 27 pages, references start on page 22, 132 compiled bibliography items, no `\nocite{*}`, no biographies in the submission-length build, and no undefined citations or references.
