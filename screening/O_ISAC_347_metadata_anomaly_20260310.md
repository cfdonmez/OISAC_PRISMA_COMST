# O_ISAC_347 Metadata Anomaly - 2026-03-10

Purpose
- This note records the repository-backed evidence that `O_ISAC_347` currently has a mismatched paper identity versus its linked full-text assets.

Evidence
- `screening/screening_log.csv` records `O_ISAC_347` as:
  - `Spectral-Efficient Frequency-Division Photonic Millimeter-Wave Integrated Sensing and Communication System Using Improved Sparse LFM Sub-Bands Fusion`
  - DOI: `10.1109/JLT.2023.3265799`
  - row origin: `phase2_assessed_reconstruction`
  - full-text decision: `Excluded`
- `analysis/ph1_scr/included_studies_list.csv` and `analysis/ph2_ext/extraction_queue.csv` also point `O_ISAC_347` to that same JLT record.
- `screening/included_studies_canonical.csv` and `screening/canonical_included_corpus_ledger.csv` had drifted to the markdown heading from the linked corpus asset.
- DOI confirmation outside the local repo also supports the JLT identity:
  - Crossref resolves `10.1109/JLT.2023.3265799` to the same JLT title with authors `Ningyuan Zhong`, `Peixuan Li`, `Wenlin Bai`, `Wei Pan`, `Lianshan Yan`, and `Xihua Zou`.
  - DOI redirection resolves to IEEE Xplore document `10097785`.
- `data/ret_docs/O_ISAC_347.pdf` is not the JLT paper. PDF text extraction shows:
  - title: `Learned Digital Back-Propagation for an optical-domain waveform integrated with communication and sensing`
  - DOI: `10.1145/3638782.3638830`
- `data/proc_markdowns/O_ISAC_347/O_ISAC_347.md` is generated from that ACM paper, not from the intended JLT paper.

Interpretation
- The intended bibliographic identity for `O_ISAC_347` is the JLT photonic millimeter-wave ISAC paper (`10.1109/JLT.2023.3265799`).
- The currently linked PDF and processed markdown are wrong assets attached to the same track ID.
- Because the frozen repo snapshot does not contain a verified JLT full text, this record was excluded from the primary corpus during repository reconciliation rather than retained as an included anomaly.
- This is a metadata / asset-linking error, not a title/abstract screening disagreement.

Repair status
- `screening/excluded_fulltext_log.csv` now records `O_ISAC_347` with exclusion code `EXC-UNVERIFIED-FULLTEXT`.
- `screening/fulltext_assessed_anomalies.csv` and `screening/screening_log_anomalies.csv` retain `O_ISAC_347` only as a legacy asset-mismatch record.
- `screening/included_studies_canonical.csv` and `screening/canonical_included_corpus_ledger.csv` no longer treat `O_ISAC_347` as part of the final included corpus.
- `data/proc_markdowns/O_ISAC_347/O_ISAC_347.md` now carries an explicit wrong-asset warning banner, and sidecar warning notes have been added next to the markdown and PDF assets.

Next action
- Keep the current exclusion decision in the canonical PRISMA trail unless a verified JLT full text is later recovered.
- If a verified JLT full text is later recovered, regenerate a clean replacement rather than reusing the current ACM-linked asset bundle.
