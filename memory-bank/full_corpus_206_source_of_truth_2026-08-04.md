# Full-corpus source of truth — 2026-08-04

This file supersedes the old 220/221-study operational locks for current analysis and writing. Historical files are retained for audit; their corpus-derived counts must not be reused without regeneration from the 206-study source.

## Review identity

- Topic: Optical Integrated Sensing and Communication (O-ISAC) for 6G.
- Review type: PRISMA 2020-grounded narrative systematic review with a scoping-style PCC component.
- Survey purpose: cross-modality taxonomy, architecture/integration mapping, metric governance and comparability, rate–sensing trade-offs, enabling technologies/applications, validation maturity, benchmark readiness, and a 6G research roadmap.
- Current journal target in this repository: IEEE Photonics Journal.
- COMST material: writing/survey-structure reference, not the current submission target.
- Actual final search cutoff: 22 June 2026.
- External registration: not performed; the internally versioned protocol and amendments are the auditable record.

## Locked PRISMA and corpus counts

| Item | Count |
|---|---:|
| Records identified | 1,733 |
| Records screened | 1,259 |
| Unique reports sought | 330 |
| Reports not retrieved | 58 |
| Reports assessed at full text | 272 |
| Full-text exclusions | 39 |
| Full-text contextual-only reports | 6 |
| Reports of included studies | 227 |
| Included studies | 206 |
| Total contextual corpus | 67 |

Reports and studies are different counting units. The 227 eligible reports map to 206 included studies; companion or version reports must never be counted as independent studies.

## Phase-D survey-use closure

| Claim or study status | Count |
|---|---:|
| Evidence items | 3,041 |
| Metric results | 4,861 |
| Trade-off records | 404 |
| Total claims | 8,306 |
| Qualitative-use claims | 3,206 |
| Quantitative-use claims | 4,997 |
| Context-only claims | 31 |
| Quarantined exact claims | 72 |
| Survey-ready studies | 175 |
| Survey-ready with claim restrictions | 31 |
| Conflict/decision register rows | 93 |
| Explicit unresolved metric-conflict rows | 2 |

The four claim-use categories reconcile exactly: `3,206 + 4,997 + 31 + 72 = 8,306`. The study statuses reconcile exactly: `175 + 31 = 206`.

The 72 quarantined rows are claim-level restrictions, not excluded studies. A disputed exact value or trend is omitted from quantitative synthesis while unaffected architecture, method, taxonomy, validation and properly scoped metric evidence remains usable.

Canonical local workbook SHA-256:

`c1b3b89789c6ed3e20da5a6283e480875c1913e21af88ff59ac747a6aa949348`

## Phase-E TQAF lock

- 206/206 unique studies scored; no blank final score.
- Dimension audit: 1,854 rows.
- Body-normalization audit: 7,951 rows.
- Legacy metric missingness: 92 rows explicitly resolved as `insufficient_information_due_legacy_extraction`.
- Overall evidence contribution: 6 low, 75 adequate, 125 strong.
- Evidence bodies: 115 total (S1=6, S2=8, S3=47, S4=10, S5=3, S6=31, S7=10).
- Certainty: 54 high, 47 moderate, 10 limited, 4 unclear/non-substantive fallback bodies.
- QA: PASS 43/43.
- Final-workbook invariance: PASS; 206 studies, 46 check families, 9,476 comparisons, 0 mismatches and 0 failed studies. The predecessor source entry in the frozen crosswalk is lineage metadata, not an untested analytical dependency.

Guardrails are mandatory: an overall score of 3 requires the four core dimensions to be at least 2; any quarantined claim caps overall at 2; quarantined metric evidence caps comparison admissibility at 1; absent author-reported limitations cap limitation transparency at 1. TQAF calibrates synthesis language and does not exclude an eligible study.

## Phase-F S1–S7 lock

Primary synthesis uses **8,203** claims: 3,020 evidence, 4,779 metric and 404 trade-off claims. The inclusive non-quarantined universe is 8,234 but contains 31 context-only metrics and must not be called the primary evidence count.

Exclusive 206-study anchors:

- modality: photonic-THz 69, fiber 56, VLC/LiFi 38, FSO 31, hybrid optical 9, other optical 3;
- validation maturity: tier 2=32, tier 3=18, tier 4=78, tier 5=66, tier 6=12;
- data availability: 13 open, 41 on request, 145 unavailable/NR, 7 NA;
- code/model availability: 197 unavailable/NR, 7 on request, 1 partial, 1 NA;
- 6G relevance: 138 direct, 64 inferred, 1 weak, 3 not applicable.

S2 and S6 are multi-label. `other` is a fallback only when no recognized category exists for that study/axis; final fallback counts are integration=0, enabling technology=19 and application=15. Internal QA and an independent artifact-tool check both pass; the latter re-imported the locked workbook and checked 29 cross-file invariants.

## Reviewer and AI provenance boundary

The completed process is described as **investigator-supervised, AI-assisted, user-delegated and claim-governed**. It is not documented as independent duplicate human screening or independent full-corpus human PDF verification.

`independent_human_status = not_documented`

Historical filenames or state labels containing `human_adjudicated` or `human_locked` are preserved for lineage. They do not prove that two independent humans reviewed every PDF.

## Quantitative-use rules

- Quantitative eligibility does not automatically imply cross-study comparability.
- Metric definition, metric role, measurement plane, scenario and validation context must be compatible.
- Optical OSNR is not pooled with electrical SNR/ESNR without an explicit conversion model.
- Physical resolution, estimator accuracy/RMSE, CRB-type bounds and fiber spatial granularity remain different constructs.
- Simulation, analytical, laboratory, prototype and field results remain different validation planes.
- Conflicting values are not averaged, silently normalized or replaced by a plausible preferred value.
- No project-level graph digitization or newly derived performance value is introduced.

## Manuscript migration rule

Do not perform a global `220 → 206` or `221 → 206` replacement. Taxonomy totals, figures, metric counts, trade-off counts, applications and included-study appendices must be regenerated from the governed 206-study source. Existing `O_ISAC_*` citation keys are identifiers and must never be changed by a numeric search-and-replace.

The active dirty manuscript under `manuscript/finalManuscript/` must not be overwritten by an automated corpus migration. Integrate `review_package/full_corpus_206_20260804/` only after reviewing the scoped diff. That package now contains an English Abstract, Methods, PRISMA Results, claim governance, TQAF results, S1–S7 synthesis, Discussion/Roadmap/Conclusion, final CSV/JSON audit artifacts and a release gate.

The package also contains a regenerated included-studies appendix in CSV and LaTeX form. It has exactly 206 unique study rows, reconciles to 227 eligible reports through a separate lineage field, reproduces the locked modality/maturity/use-status distributions, records `independent_human_status = not_documented` for every row, and passes path-leakage and artifact re-import checks.

For public Git publication, host-specific paths in copied Phase-E/F scripts and QA metadata were parameterized or replaced by logical filenames. This portability sanitization changes no analytical value, classification, source hash or QA assertion; canonical local checkpoints retain the original runtime provenance.

The final dated package-level gate is `14_RELEASE_QA_FINAL_2026-08-04.json`. Its status is `PASS_FOR_REVIEWED_MANUSCRIPT_INTEGRATION`, not submission-ready: protected-manuscript integration, regenerated final figures/tables, bibliography/cross-reference resolution, IEEEtran/rendered-PDF QA and author-owned declarations remain explicit gates.
