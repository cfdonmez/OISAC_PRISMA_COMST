# Section III Evidence Reconstruction

Purpose
- This note records what the repository can currently prove for Section III without inventing missing PRISMA trail data.

Verified evidence
- `data/proc_markdowns/` contains `221` valid `O_ISAC_###` directories, including one legacy wrong-linked asset (`O_ISAC_347`) that is no longer part of the final canonical corpus and has now been explicitly relabeled in place.
- `data/ext_v4_uni.csv` contains `220` unique `Paper_ID` values that start with `O_ISAC_`.
- `screening/included_studies_canonical.csv` is the reconstructed canonical included set for the final corpus.
- `screening/canonical_included_corpus_ledger.csv` links each included `track_id` to a corpus path, a primary markdown source, and legacy reconciliation fields.
- `analysis/ph2_ext/extraction_dataset.csv` and `analysis/ph2_ext/extraction_queue.csv` together contain `222` unique `Track_ID` values.
- `screening/fulltext_assessed_reconstruction.csv` records that 222-row assessed set in a reviewer-readable form.
- `screening/screening_log.csv` now records a reconstructed master screening ledger with `441` evidence-backed rows.
- `screening/title_abstract_screening_reconstruction.csv` records `393` normalized title/abstract record groups from the currently available legacy and Scopus-batch screening artefacts.
- `search/formal_identification_reconstruction_20251130.csv` records how the canonical source-level identification claims compare with the raw export evidence currently visible in the repo snapshot.
- `search/upstream_prisma_reconstruction_20260310.csv` records stage-level support for the upstream PRISMA chain.
- `search/inferred_freeze_provenance_timeline_20260310.csv` and `search/inferred_freeze_provenance_from_memory_bank_20260310.md` record the dated memory-bank and repo chronology supporting the historical plausibility of the `2025-11-30` freeze claim.
- `.agent/workflows/section3_external_evidence_search_20260310.md` records external supplemental artefacts discovered outside the repo snapshot during the March 10, 2026 recovery search.

What this reconstruction proves
- The repository currently supports a final included corpus of `N = 220`.
- The repository also supports a full-text assessed set of `N = 222`, reconstructed from the phase-2 extraction artifacts, with `2` reconciled full-text exclusions.
- The repository now has a reconstructed screening master that combines:
  - `222` assessed records backed by phase-2 extraction artifacts
  - `219` legacy-only screening groups backed by the earlier screening log
- The repository also supports a lower-bound title/abstract reconstruction of `260` unique non-duplicate screened records plus `133` duplicate-only groups from the available Dec 28 update workflow.
- The reconstructed included set now matches the `220`-row legacy `analysis/ph1_scr/included_studies_list.csv` in size, but it is stronger as a freeze artifact because it records explicit repository reconciliation decisions.
- External supplemental evidence now also exists for the title/abstract stage:
  - `C:\Users\fdonmez\Drive’ım (cfdonmez@gmail.com)\IEEE_511_OISAC_Results_Screened.csv` contains `510` screened IEEE records with a `158 INCLUDE / 352 EXCLUDE` split.
  - When normalized by DOI/title and unioned with the current in-repo title/abstract reconstruction, the combined support reaches `738` unique title/abstract records.

What this reconstruction does not prove
- It does not prove the upstream PRISMA chain `980 -> 280 -> 700 -> 222 -> 2 -> 220` at row level.
- It only partially repairs the duplicate audit trail: `search/dedup_log.csv` now records `152` explicit duplicate decisions from the available Dec 28 update workflow, but it still does not fully back the canonical `duplicates_removed = 280`.
- The reconstructed title/abstract evidence is still incomplete relative to the claimed `records_screened = 700`, because the repo snapshot directly supports only `260` unique non-duplicate screened records.
- The external IEEE screening artifact narrows the screened-record gap substantially, but it is not yet canonical because `17` of its `EXCLUDE` decisions still collide with items that are currently in the final included corpus.
- `search/dedup_reconstruction_status.md` now documents that the repo snapshot currently exposes only `413` raw export rows against a claimed formal identification total of `980`, and that the current best dedup ledger reaches `152` explicit duplicate decisions with `128` resolved retained masters.
- `screening/title_abstract_screening_reconstruction_status.md` now documents that `analysis/nb/01_search_and_dedup.ipynb` expects `data/raw_search_results/`, but that directory is absent from the current repo snapshot.
- The inferred provenance files improve the historical credibility of the `2025-11-30` freeze date, but they still do not replace a true WoS or merged raw-search export pack.

Resolved and unresolved reconciliation results
- `O_ISAC_044` remains in the final corpus; its earlier anomaly was resolved after identifying the extensionless retrieved PDF and adding the named alias `data/ret_docs/O_ISAC_044.pdf`.
- `O_ISAC_347` is intended to be the JLT paper `10.1109/JLT.2023.3265799`, but the currently linked PDF and processed markdown point to the ACM paper `10.1145/3638782.3638830`; the record was therefore removed from the final included corpus during repository reconciliation.
- `O_ISAC_087` appears in the 222-row full-text assessed reconstruction, but is absent from both the final included corpus and the named PDF inventory.
- The canonical `screening/excluded_fulltext_log.csv` now records two repository-reconciled exclusions: `O_ISAC_087` and `O_ISAC_347`, while the earlier `O_ISAC_007` version has been preserved as `screening/excluded_fulltext_log_legacy_20260309.csv`.
- No included-corpus anomaly remains open after the `O_ISAC_044` reconciliation.
- The assessed-stage anomalies are listed in `screening/fulltext_assessed_anomalies.csv`.
- The screening-master follow-up list is captured in `screening/screening_log_anomalies.csv`.

How to use this for Section III
- Use `included_studies_canonical.csv` when the manuscript needs the authoritative list behind `N = 220`.
- Use `canonical_included_corpus_ledger.csv` when a reviewer asks how the final included set was reconstructed from repository evidence.
- Use `fulltext_assessed_reconstruction.csv` when a reviewer asks how the repo supports `fulltext_assessed = 222`.
- Use `screening/screening_log.csv` as the best available row-level screening ledger in the current repo snapshot.
- Use `screening/title_abstract_screening_reconstruction.csv` when a reviewer asks what the current repo snapshot can directly support at the title/abstract stage.
- Use `.agent/workflows/section3_external_evidence_search_20260310.md` when a reviewer asks what additional off-repo evidence was recovered during the March 10, 2026 search.
- Use `search/dedup_log.csv` as the best available row-level duplicate ledger in the current repo snapshot.
- Use `search/formal_identification_reconstruction_20251130.csv` when a reviewer asks how the canonical IEEE / Scopus / WoS counts relate to the raw exports still visible in the repo.
- Use `search/upstream_prisma_reconstruction_20260310.csv` when a reviewer asks which upstream PRISMA transitions are row-backed versus only canonically claimed.
- Use `search/inferred_freeze_provenance_timeline_20260310.csv` and `search/inferred_freeze_provenance_from_memory_bank_20260310.md` when a reviewer asks why the `2025-11-30` freeze date is still treated as historically grounded despite the missing original raw bundle.
- Use `search/dedup_reconstruction_status.md` and `search/dedup_reconstruction_available_exports.csv` when a reviewer asks why the duplicate trail is still only partially auditable.
- Use `screening/validate_section3_freeze.py` to re-check the current canonical Section III freeze conditions after any future edits.
- Do not cite `analysis/ph1_scr/screening_log.csv` or `analysis/PRISMA_stat.md` as proof of the final `980 -> 280 -> 700 -> 222 -> 2 -> 220` chain.

Next required actions before full freeze
- Recover or regenerate the remaining `128` duplicate decisions needed to fully row-back `duplicates_removed = 280`.
- Recover or regenerate the missing raw search inputs needed to close the `440`-record gap between the current title/abstract reconstruction (`260` screened records) and the claimed `records_screened = 700`.
- Keep the in-place warning labels on the legacy wrong-linked `O_ISAC_347` ACM assets unless a verified JLT replacement is later recovered.

Supplemental repo-preserved external evidence
- `screening/external/IEEE_511_OISAC_Results.csv` preserves the discovered 511-row IEEE export inside the repo.
- `screening/external/IEEE_511_OISAC_Results_Screened.csv` preserves the paired 510-row screened IEEE decision file inside the repo.
- `screening/external/ieee_511_conflicts_vs_canonical.csv` records the `17` active conflicts between external IEEE `EXCLUDE` decisions and the current canonical included corpus, now with audit decisions assigned.
- `screening/external/ieee_511_conflict_decisions_20260310.csv` records the final Section III audit decision for each of those `17` conflict rows.
- `screening/external/README.md` describes how these supplemental artifacts should be used during Section III reconciliation.
