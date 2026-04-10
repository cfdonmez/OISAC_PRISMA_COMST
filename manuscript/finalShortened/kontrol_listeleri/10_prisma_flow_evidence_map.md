# PRISMA Flow Evidence Map

Purpose:

- This file consolidates the repository evidence for the PRISMA 2020 flow reported in the manuscript.
- It separates row-backed stages from reconstructed stages.
- It also flags what is currently missing from the repo snapshot.

## 1. Freeze and Canonical Source Policy

- Declared formal freeze date: `2025-11-30`
- Canonical formal databases:
  - `IEEE Xplore`
  - `Scopus`
  - `Web of Science`
- Supplementary monitoring sources:
  - `arXiv`
  - `TechRxiv`
- Canonical supplementary-source contribution for the frozen flow:
  - `other_sources_results = 0`

Primary evidence:

- `protocol/prisma_proto.md`
- `search/search_strings.md`
- `screening/prisma_flow_counts.csv`
- `search/formal_identification_reconstruction_20251130.csv`
- `search/upstream_prisma_reconstruction_20260310.csv`

Important gap:

- `search/search_log.csv` is referenced across the repo as the canonical formal search log, but it is not present in the current repo snapshot.

## 2. Canonical PRISMA Counts

From `screening/prisma_flow_counts.csv`:

- `databases_results = 980`
- `other_sources_results = 0`
- `duplicates_removed = 280`
- `records_screened = 700`
- `records_excluded_title = 478`
- `fulltext_assessed = 222`
- `fulltext_excluded = 2`
- `studies_included = 220`

## 3. Stage-by-Stage Evidence Status

### 3.1 Identification

Canonical count:

- `980`

Canonical source split:

- `IEEE Xplore = 410`
- `Scopus = 320`
- `Web of Science = 250`

Evidence:

- `search/formal_identification_reconstruction_20251130.csv`
- `search/search_strings.md`
- `protocol/prisma_proto.md`

Current raw-export availability:

- `data/srch_logs/export2025.12.28-05.30.23.csv`: `28` visible IEEE rows
- `data/srch_logs/scopus_export_Dec 28-2025_b7fbefb1-055d-45f8-a240-8163c71acaa5.csv`: `385` visible Scopus rows
- Matching freeze-time Web of Science raw export: not present

Status:

- `980` is canonically declared and reconstruction-supported.
- It is not fully row-backed in the current repo snapshot.

### 3.2 Deduplication

Canonical count:

- `280 duplicates removed`

Evidence:

- `search/dedup_log.csv`
- `search/dedup_reconstruction_status.md`
- `search/dedup_reconstruction_available_exports.csv`

What is row-backed now:

- `152` explicit duplicate decisions
- `149` linked to available Scopus raw-export rows
- `3` linked to available IEEE raw-export rows
- `128` of the `152` resolve to a retained non-duplicate master

Status:

- `duplicates_removed = 280` is not fully row-backed.
- The current repo still lacks row-level support for `128` duplicate decisions.

### 3.3 Title and Abstract Screening

Canonical count:

- `700 records screened`
- `478 excluded at title/abstract`

Evidence:

- `screening/title_abstract_screening_reconstruction.csv`
- `screening/title_abstract_screening_reconstruction_status.md`
- `screening/screening_log.csv`
- `screening/section3_evidence_reconstruction.md`

What is directly reconstructable in-repo:

- `393` normalized title/abstract record groups
- `260` reconstructable non-duplicate screened records
- `133` duplicate-only groups
- `196` directly supported title/abstract exclusions
- `64` directly supported include/forward decisions

External supplemental support preserved in repo:

- `screening/external/IEEE_511_OISAC_Results.csv`
- `screening/external/IEEE_511_OISAC_Results_Screened.csv`

Important limitation:

- External IEEE support raises combined title/abstract coverage substantially, but it is not canonical because conflict rows remain and the current repo does not fully prove the canonical `700` screened records at row level.

Status:

- `700` and `478` are reconstruction-supported, not fully row-backed.

### 3.4 Full-Text Assessment

Canonical count:

- `222 full-text articles assessed`

Evidence:

- `screening/fulltext_assessed_reconstruction.csv`
- `screening/fulltext_assessed_anomalies.csv`
- `screening/screening_log.csv`
- `analysis/ph2_ext/extraction_dataset.csv`
- `analysis/ph2_ext/extraction_queue.csv`

What is row-backed now:

- `222` unique assessed IDs
- `220` map to the final included corpus
- `2` map to the canonical full-text exclusion log

Status:

- `222` is row-backed in the current repo snapshot.

### 3.5 Full-Text Exclusions

Canonical count:

- `2`

Evidence:

- `screening/excluded_fulltext_log.csv`

Excluded records:

- `O_ISAC_087`
  - Code: `EXC-PURE-COMM`
  - Reason: pure communication / non-O-ISAC under protocol Section 4.2
- `O_ISAC_347`
  - Code: `EXC-UNVERIFIED-FULLTEXT`
  - Reason: intended JLT record identified, but the linked repo assets map to the wrong ACM full text and no verified frozen full text is present

Status:

- `2` is row-backed.

### 3.6 Final Included Corpus

Canonical count:

- `220`

Evidence:

- `screening/included_studies_canonical.csv`
- `screening/canonical_included_corpus_ledger.csv`
- `screening/canonical_included_corpus_anomalies.csv`

What is row-backed now:

- `220` included study IDs in the canonical file
- `220` entries present in `analysis/ph2_ext/extraction_dataset.csv` or `analysis/ph2_ext/extraction_queue.csv` via the assessed-stage reconstruction
- `220` entries represented in the canonical included-study ledger

Useful detail:

- `219` of the `220` included studies are also present in the legacy included-studies list.
- `213` of the `220` currently have non-empty DOI entries in the canonical included file.

Status:

- `220` is row-backed.

## 4. Reviewer Workflow Evidence

Protocol-level evidence:

- `protocol/prisma_proto.md`
  - pilot calibration on `50` records
  - two-reviewer title/abstract screening
  - two-reviewer full-text assessment
  - conservative `Include/Unsure` carry-forward rule
  - consensus discussion
  - third-reviewer arbitration

Manuscript-level wording:

- `manuscript/finalShortened/bare_jrnl_new_sample4.tex`

Current structured-log situation:

- `screening/screening_log.csv` includes workflow-related fields such as `reviewer_initials` and `date_decided`
- however, only `2` rows currently contain non-empty `reviewer_initials`

Interpretation:

- The reviewer workflow is clearly protocol-backed and manuscript-stated.
- It is not fully demonstrated as row-level dual-review metadata across the reconstructed screening ledger now present in the repo snapshot.

## 5. What Is Original vs Reconstructed

- `980 identified records`: reconstructed / canonically declared, not fully row-backed
- `280 duplicates removed`: reconstructed / partially row-backed
- `700 screened`: reconstructed / partially row-backed
- `478 title-abstract exclusions`: reconstructed / partially row-backed
- `222 full-text assessed`: row-backed
- `2 full-text excluded`: row-backed
- `220 included studies`: row-backed

## 6. Missing or Partial Artifacts

- Missing canonical formal search log:
  - `search/search_log.csv`
- Missing freeze-time raw export pack:
  - especially the matching `Web of Science` export
- Missing complete freeze-level dedup ledger:
  - canonical `280` not fully row-backed
- Missing complete freeze-level title/abstract ledger:
  - canonical `700` not fully row-backed

## 7. Safe Manuscript Interpretation

What the current repo can defend strongly:

- the formal source policy
- the `2025-11-30` declared freeze date as historically grounded
- the final `222 -> 2 -> 220` end of the PRISMA chain
- the existence of a canonical included-study corpus of `220`

What the manuscript should not overclaim without caveat:

- that the current repo snapshot fully preserves the original row-level trail for `980 -> 280 -> 700`
- that the missing upstream artifacts have already been recovered

Recommended audit wording:

- describe the earlier PRISMA stages as canonical aggregate counts reconciled against the best available reconstruction artifacts
- describe the later PRISMA stages as directly backed by the current structured ledgers

