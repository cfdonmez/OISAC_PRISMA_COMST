# Reconstructed Canonical Search Log Note

Prepared on: 2026-04-11

Purpose:

- This note explains why `search/search_log.csv` exists as a reconstructed aggregate log in the current repository snapshot.
- It restores a missing canonical search-stage artifact that is referenced across the repo, the manuscript, and the evidence pack.

What was reconstructed:

- `search/search_log.csv` now records the canonical formal database split used for the frozen PRISMA flow:
  - `IEEE Xplore = 410`
  - `Scopus = 320`
  - `Web of Science = 250`
- All three rows are anchored to the declared freeze date `2025-11-30`.

What this file is not:

- It is not the original freeze-time raw export bundle.
- It does not replace the missing row-level IEEE / Scopus / Web of Science search exports for the freeze date.

Reconstruction basis:

- `protocol/prisma_proto.md`
- `search/search_strings.md`
- `search/formal_identification_reconstruction_20251130.csv`
- `search/inferred_freeze_provenance_timeline_20260310.csv`
- manuscript Section III references that explicitly cite `search/search_log.csv` as the canonical formal search log

Interpretation guidance:

- Use `search/search_log.csv` as the canonical aggregate identification log for PRISMA reporting and manuscript cross-reference consistency.
- Use `search/formal_identification_reconstruction_20251130.csv` and the provenance notes when a reviewer asks about the missing freeze-time raw export pack.
- Do not describe `search/search_log.csv` as a row-level raw-search archive.
