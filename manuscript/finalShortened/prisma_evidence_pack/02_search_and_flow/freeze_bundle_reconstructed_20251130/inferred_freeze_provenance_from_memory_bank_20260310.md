# Inferred Freeze Provenance From Memory Bank - 2026-03-10

Purpose
- This note adds an explicitly inferred provenance layer for the missing `2025-11-30` freeze-time raw search bundle.

Boundary
- This note is not an original raw export.
- It does not convert inferred chronology into row-level evidence.
- Its role is narrower: to show that the claimed `2025-11-30` freeze date is historically plausible inside the repository and predates the March 2026 Section III log backfill.

Evidence classes used here
- `declared_historical`: older project notes whose own content describes the search or corpus state
- `repo_visible`: files currently present in the repo snapshot
- `inferred`: conclusions drawn by linking the dated notes above

Core inference
- `memory-bank/projectbrief.md` declares, as of `2025-12-11`, a PRISMA 2020 systematic review with `221` screened or included studies, `221` collected PDFs, and `1500+` identified records.
- `memory-bank/activeContext.md` and `memory-bank/survey_global_backlog_2026-03-09.md` then show that, on `2026-03-09`, Section III work still consisted of backfilling `search/search_log.csv`, `search/dedup_log.csv`, and `screening/prisma_flow_counts.csv` while preserving pre-existing manuscript counts.
- The most coherent interpretation is that the search-and-screening workflow had already happened before `2025-12-11`, but the formal PRISMA audit pack was only reconstructed and synchronized in March 2026.
- The visible `2025-12-28` IEEE and Scopus exports therefore fit better as a later update wave than as the original freeze-time bundle.

Why this matters for Section III
- It gives reviewers a transparent reason to treat `2025-11-30` as a declared historical freeze date rather than a date invented during the March 2026 clean-up.
- It explains why the late-stage counts (`222 -> 2 -> 220`) are row-backed while the early-stage counts (`980 -> 280 -> 700`) still rely partly on declared historical totals and reconstruction.
- It supports the current wording in `drafts/section_03_methodology.md` without pretending that the original WoS or merged raw-search exports have been recovered.

What this note can safely support
- The claim that a mature O-ISAC screening corpus existed by `2025-12-11`
- The claim that March 2026 activity mainly rebuilt and aligned PRISMA logging artifacts
- The interpretation that the currently visible Dec 28 exports are later update exports, not the original Nov 30 freeze exports

What this note cannot safely support
- Exact row-level proof for `980` identified records
- Exact row-level proof for `280` duplicate removals
- Exact row-level proof for `700` screened records
- Any claim that a hidden or deleted WoS raw export has been recovered

Recommended citation use
- Cite `search/formal_identification_reconstruction_20251130.csv` and `search/upstream_prisma_reconstruction_20260310.csv` for the current reconstruction tables.
- Cite `search/inferred_freeze_provenance_timeline_20260310.csv` and this note when a reviewer asks why the `2025-11-30` freeze date is still treated as historically grounded despite the missing raw bundle.
- Do not cite this note as a substitute for a true raw-export archive if one is later recovered.
