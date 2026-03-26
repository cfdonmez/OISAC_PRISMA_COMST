# Screening Operations Guide

Purpose
- This folder contains the canonical screening artifacts for the final PRISMA 2020 audit trail used by Section III.

## Canonical source-of-truth for Section III

The final Section III methodology text must align with the files below:

- `screening/prisma_flow_counts.csv`
- `screening/excluded_fulltext_log.csv`
- `screening/included_studies_canonical.csv`
- `screening/canonical_included_corpus_ledger.csv`
- `screening/canonical_included_corpus_anomalies.csv`
- `screening/fulltext_assessed_reconstruction.csv`
- `screening/fulltext_assessed_anomalies.csv`
- `screening/screening_log.csv`
- `screening/screening_log_anomalies.csv`
- `screening/title_abstract_screening_reconstruction.csv`
- `screening/title_abstract_screening_reconstruction_status.md`
- `search/search_log.csv`
- `search/dedup_log.csv`
- `search/formal_identification_reconstruction_20251130.csv`
- `search/upstream_prisma_reconstruction_20260310.csv`
- `search/inferred_freeze_provenance_timeline_20260310.csv`
- `search/inferred_freeze_provenance_from_memory_bank_20260310.md`
- `drafts/section_03_methodology.md`
- `protocol/prisma_proto.md`

Rule
- If any older report, notebook output, or archive artifact conflicts with the files above, the files above govern the manuscript and PRISMA flow.

## Archival and preliminary materials

The `analysis/ph1_scr/` directory contains exploratory and interim Phase 1 artifacts.

- These files are useful for traceability and debugging.
- They are not the canonical source for final PRISMA counts unless their numbers have been explicitly reconciled into the files listed above.

## Screening workflow

### 1. Title and abstract screening

Goal
- Remove clearly out-of-scope studies before full-text review.

Input
- Exported CSV/RIS files from the formal search sources defined in the final protocol and recorded in `search/search_log.csv`.

Decision criteria
- `Include`: matches the O-ISAC definition in `protocol/prisma_proto.md`, Section 4.
- `Exclude`: RF-only, pure sensing, pure communication, thesis/grey literature, or otherwise out of scope.
- `Unsure`: insufficient evidence at title/abstract level; advance conservatively to the next stage.

Logging
- Record title/abstract decisions in `screening/screening_log.csv`.
- Keep exclusion codes and final adjudicated decisions auditable.

### 2. Full-text eligibility

Goal
- Apply the final inclusion/exclusion criteria to all candidate records.

Logging
- Record full-text exclusions in `screening/excluded_fulltext_log.csv`.
- Keep `screening/prisma_flow_counts.csv` synchronized with the full-text decision trail.

### 3. File roles in this directory

- `screening_log.csv`: reconstructed master screening record built from the repo-backed phase-2 assessed set plus legacy screening groups.
- `screening_log_anomalies.csv`: focused follow-up list for the reconstructed screening log.
- `title_abstract_screening_reconstruction.csv`: normalized title/abstract-stage reconstruction for the currently available legacy and Scopus-batch screening artefacts.
- `title_abstract_screening_reconstruction_status.md`: status note explaining what the title/abstract reconstruction can and cannot prove.
- `excluded_fulltext_log.csv`: canonical list of full-text exclusions and reasons.
- `prisma_flow_counts.csv`: canonical final counts for the PRISMA flow diagram.
- `validate_section3_freeze.py`: repeatable validation script for the current canonical Section III state.
- `included_studies_canonical.csv`: reconstructed 220-row canonical included set derived from the repo corpus plus repository-reconciliation exclusions.
- `canonical_included_corpus_ledger.csv`: evidence ledger for the included corpus, with source paths and reconciliation fields against legacy artifacts.
- `canonical_included_corpus_anomalies.csv`: focused list of reconciliation conflicts that must be resolved before a full PRISMA freeze.
- `fulltext_assessed_reconstruction.csv`: reconstructed 222-row full-text assessed set derived from `analysis/ph2_ext/extraction_dataset.csv` and `analysis/ph2_ext/extraction_queue.csv`.
- `fulltext_assessed_anomalies.csv`: focused list of full-text assessment conflicts and gaps discovered during reconstruction.

## Current reconstruction status

- The final included corpus (`N = 220`) is now directly supported by `included_studies_canonical.csv` and `canonical_included_corpus_ledger.csv`.
- The full-text assessed stage is now directly supported by `fulltext_assessed_reconstruction.csv`, which contains `222` unique assessed IDs.
- The best available duplicate ledger is now `search/dedup_log.csv`, which records `152` explicit duplicate decisions linked back to available raw exports (`149` Scopus, `3` IEEE Xplore); `128` of those rows also resolve to a retained non-duplicate master in the current repo snapshot.
- The best available title/abstract reconstruction is now `title_abstract_screening_reconstruction.csv`, which records `393` normalized record groups:
  - `260` reconstructable non-duplicate screened records
  - `133` duplicate-only groups
- The reconstructed `screening/screening_log.csv` now contains `441` evidence-backed rows:
  - `222` phase-2 assessed records
  - `219` legacy-only screening groups not linked to the assessed set
- These files support the `222 -> 220` end of the PRISMA chain, but they still do not prove the full upstream counts `980 -> 280 -> 700 -> 222 -> 2 -> 220` at row level.
- `canonical_included_corpus_anomalies.csv` is now empty; no included-corpus anomaly remains open after the `O_ISAC_044` reconciliation.
- `fulltext_assessed_anomalies.csv` currently flags two important signals:
  - `O_ISAC_087` appears in the 222-row assessed set, is absent from the final included corpus and named PDF inventory, and now serves as the reconciled full-text exclusion target.
  - `O_ISAC_347` is no longer in the final included corpus; its legacy PDF/markdown assets still point to the wrong ACM full-text record, but they have now been relabeled in place as wrong assets to prevent accidental reuse.
- `screening_log_anomalies.csv` currently highlights six follow-up records:
  - `O_ISAC_087`
  - `O_ISAC_347` (resolved by exclusion, legacy assets still mismatched)
  - `LEGACY_003`
  - `LEGACY_026`
  - `LEGACY_078`
  - `LEGACY_197`
- `python screening/validate_section3_freeze.py` currently passes for the canonical Section III state.
- The best reconstructed substitute for the missing freeze-time raw-search bundle is now documented in `search/formal_identification_reconstruction_20251130.csv`, `search/upstream_prisma_reconstruction_20260310.csv`, `search/inferred_freeze_provenance_timeline_20260310.csv`, `search/inferred_freeze_provenance_from_memory_bank_20260310.md`, and `search/reconstructed_freeze_bundle_note_20260310.md`.
