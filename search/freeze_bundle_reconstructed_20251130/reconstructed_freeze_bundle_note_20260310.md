# Reconstructed Freeze Bundle Note - 2026-03-10

Purpose
- This note documents the best search-stage substitute currently available for the missing freeze-time raw search bundle.

Important boundary
- These files are reconstructed support artefacts.
- They do not claim to be the original `2025-11-30` IEEE / Scopus / Web of Science raw exports.
- They exist so Section III can cite a transparent evidence pack instead of leaving the upstream search stages undocumented.

Files created for this purpose
- `search/formal_identification_reconstruction_20251130.csv`
  - source-level matrix comparing the canonical `2025-11-30` identification claims against what raw export coverage is actually visible in the repo snapshot
- `search/upstream_prisma_reconstruction_20260310.csv`
  - stage-level support table for `identified -> deduplicated -> screened -> title-excluded -> fulltext -> included`
- `search/inferred_freeze_provenance_timeline_20260310.csv`
  - dated chronology linking memory-bank history, current repo files, and the visible Dec 28 update exports
- `search/inferred_freeze_provenance_from_memory_bank_20260310.md`
  - narrative interpretation of why the Nov 30 freeze remains historically grounded even though the original raw bundle is missing
- `search/dedup_log.csv`
  - best available row-level duplicate ledger in the current repo snapshot
- `search/dedup_reconstruction_status.md`
  - narrative note explaining why the dedup trail remains partial

Interpretation
- The search-stage evidence is now documented in a reviewer-readable way even though the original freeze-time bundle is absent.
- The memory-bank-supported inferred provenance layer shows that the Nov 30 freeze claim predates the March 2026 Section III backfill and that the visible Dec 28 raw exports belong to a later update wave.
- The late-stage PRISMA counts (`222 -> 2 -> 220`) remain stronger than the early-stage counts (`980 -> 280 -> 700`).
- If the original Web of Science / merged raw-search bundle is later recovered, these reconstructed files should be replaced or superseded by a true freeze-level export pack.
