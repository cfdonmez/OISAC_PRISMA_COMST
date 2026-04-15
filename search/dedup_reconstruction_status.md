# Dedup Reconstruction Status

Scope
- This note documents only what can be proven from the raw export artifacts and explicit duplicate decisions currently present in the repository.

Available raw export coverage
- `data/srch_logs/export2025.12.28-05.30.23.csv`: 28 rows
- `data/srch_logs/scopus_export_Dec 28-2025_b7fbefb1-055d-45f8-a240-8163c71acaa5.csv`: 385 rows
- Total raw export rows currently available: 413
- Formal PRISMA identification count claimed in `search/search_log.csv`: 980
- Missing raw export coverage relative to the claimed formal identification total: 567 rows

What can currently be proven
- `search/dedup_log.csv` now records `152` explicit duplicate decisions reconstructed from `analysis/ph1_scr/screening_log.csv`.
- Of those `152` rows, `149` are cross-linked to the available Scopus raw export and `3` are cross-linked to the available IEEE Xplore raw export.
- `128` duplicate rows in `search/dedup_log.csv` resolve to a retained non-duplicate master record in the current repo snapshot; the remaining `24` preserve an explicit duplicate decision but do not yet expose a recoverable retained master.
- `search/dedup_reconstruction_available_exports.csv` still captures `12` lower-level DOI duplicate links that can be seen directly inside the available raw exports.
- `search/dedup_external_overlap_support_20260411.csv` records `152` normalized overlap rows between the repo-preserved external `IEEE_511_OISAC_Results.csv` export and the visible Dec 28 Scopus export.
- Of those external overlap rows, `116` are already covered by `search/dedup_log.csv`, while `36` provide additional noncanonical duplicate-support rows not previously captured in the in-repo dedup ledger.
- The earlier 5-row example file has been preserved as `search/dedup_log_legacy_examples_20260310.csv`.

What cannot currently be proven
- The repository snapshot does not row-back `duplicates_removed = 280` in `screening/prisma_flow_counts.csv`.
- A Web of Science raw export matching the final `search/search_log.csv` is not present in the current repo snapshot.
- The available raw exports cover only part of the formal search record universe, so the reconstructed `search/dedup_log.csv` remains a partial Dec 28 update-workflow ledger rather than a complete freeze-level dedup trail for the canonical `2025-11-30` PRISMA identification stage.
- Relative to the claimed canonical `duplicates_removed = 280`, the repo snapshot still lacks row-level support for `128` duplicate decisions.
- Even after adding the `36` noncanonical external overlap-support rows, the combined evidence stack still falls short of the canonical duplicate count by `92`.

Recommended next step
- Add the missing formal raw exports, especially the missing Web of Science side, or regenerate the final dedup ledger from the original freeze-time search result files before claiming a fully auditable `duplicates_removed = 280`.
- Treat the `36` external overlap-support rows as reviewer-facing supplemental evidence only unless they can be promoted into a canonical freeze-level ledger through verified source reconciliation.
