# O_ISAC_044 Reconciliation Note - 2026-03-10

Purpose
- This note records why `O_ISAC_044` is no longer treated as an unresolved Section III anomaly.

Evidence
- `screening/fulltext_assessed_reconstruction.csv` records `O_ISAC_044` in the assessed set and final included corpus.
- `screening/screening_log.csv` records `O_ISAC_044` as `Included`.
- `data/proc_markdowns/O_ISAC_044/` contains a full processed corpus bundle, including markdown, figures, and metadata.
- `data/proc_markdowns/O_ISAC_044/O_ISAC_044/O_ISAC_044_meta.json` confirms DOI `10.1109/JLT.2024.3354070`.
- `data/ret_docs/O_ISAC_044` was found as an extensionless retrieved PDF and has now been aliased as `data/ret_docs/O_ISAC_044.pdf`.
- `data/ext_v4_uni.csv` contains `O_ISAC_044` as a final-corpus paper.

Interpretation
- The earlier anomaly was not a missing-full-text problem; it was a file-naming inconsistency in `data/ret_docs/`.
- The legacy `analysis/ph1_scr/included_studies_list.csv` omission is now treated as an interim-list gap, not as a blocker against canonical inclusion.

Resolution
- `O_ISAC_044` remains in the final included corpus.
- The named-PDF issue is resolved by the in-repo `.pdf` alias.
- `O_ISAC_044` has been removed from the included/anomaly follow-up lists for Section III.
