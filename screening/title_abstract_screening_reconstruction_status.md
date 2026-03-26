# Title/Abstract Screening Reconstruction Status

Purpose
- This note documents the strongest title/abstract screening evidence that can currently be reconstructed from the repository without inventing missing PRISMA trail data.

Inputs used
- `analysis/ph1_scr/screening_log.csv`
- `scopus_screening_entries.csv`
- `analysis/ph1_scr/ai_scr_dec_scopus.csv`
- `analysis/nb/01_search_and_dedup.ipynb`

What can currently be proven
- `screening/title_abstract_screening_reconstruction.csv` now records `393` normalized record groups derived from the legacy screening log plus the Scopus batch artefacts.
- Of those `393` record groups:
  - `260` are reconstructable as unique non-duplicate title/abstract screened records,
  - `133` are only supported as duplicate-only groups.
- The `260` reconstructable screened records currently break down as:
  - `196` title/abstract exclusions,
  - `64` title/abstract inclusions or forward-to-full-text decisions.
- The reconstruction basis is dominated by the legacy screening log:
  - `255` rows come directly from explicit legacy include/exclude decisions,
  - `5` legacy `Unscreened` rows can be resolved using linked AI Scopus decisions,
  - duplicate-only groups are preserved separately and not counted as screened records.

What cannot currently be proven
- The repository snapshot does not row-back the canonical `records_screened = 700` in `screening/prisma_flow_counts.csv`.
- Relative to the canonical PRISMA flow, the current repo snapshot is still missing row-level support for `440` unique screened records.
- The current title/abstract reconstruction also does not recover the canonical `records_excluded_title = 478` and `fulltext_assessed = 222` split at row level.
- `analysis/nb/01_search_and_dedup.ipynb` explicitly expects raw search inputs in `data/raw_search_results/`, but that directory is absent from the current repo snapshot.

Interpretation
- The available screening artefacts primarily document a Dec 28, 2025 update workflow, not the full freeze-time screening universe behind the canonical `2025-11-30` PRISMA counts.
- This title/abstract reconstruction is therefore useful as a lower-bound audit trail, not as a complete freeze-ready replacement for the canonical `700` screened count.

Recommended next step
- Recover `data/raw_search_results/` or the equivalent freeze-time IEEE/Scopus/Web of Science exports and regenerate the title/abstract screening ledger from those original inputs before claiming a fully auditable `records_screened = 700`.
