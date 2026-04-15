# External Dedup Overlap Support Summary

Prepared on: 2026-04-11

Scope
- This file summarizes duplicate-support overlap recovered by comparing the repo-preserved external IEEE 511 export against the visible Dec 28 Scopus export.
- The result is supplemental only; it does not replace the canonical freeze-level dedup ledger.

Counts
- Total normalized overlap rows: `152`
- Exact DOI overlap rows: `142`
- Normalized-title-only overlap rows: `10`
- Overlap rows already present in `search/dedup_log.csv`: `116`
- New supplemental duplicate-support rows not already present in `search/dedup_log.csv`: `36`

Interpretation
- `search/dedup_log.csv` still provides the best canonical in-repo duplicate ledger with `152` explicit decisions.
- The external IEEE-Scopus overlap contributes `36` additional noncanonical duplicate-support rows not already captured in that ledger.
- Taken together, the current evidence stack supports `188` duplicate-removal rows (`152` explicit + `36` supplemental overlap-only support), leaving a residual gap of `92` relative to the canonical `duplicates_removed = 280`.

Boundary
- These overlap rows are evidence of duplicate support, not newly invented final canonical decisions.
- They should be cited as `noncanonical_external_overlap_support` whenever used in reviewer-facing explanations.
