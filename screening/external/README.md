# External Screening Evidence

Purpose
- This folder preserves supplemental screening artefacts discovered outside the repo during the March 10, 2026 Section III recovery search.

Current contents
- `IEEE_511_OISAC_Results.csv`
  - raw IEEE export with `511` rows
- `IEEE_511_OISAC_Results_Screened.csv`
  - screened IEEE title/abstract decisions with `510` rows
  - decision split: `158 INCLUDE`, `352 EXCLUDE`
- `ieee_511_conflicts_vs_canonical.csv`
  - `17` rows where the external IEEE screened file marks a record as `EXCLUDE` but the current canonical corpus includes it
- `ieee_511_conflict_triage_20260310.csv`
  - row-level recommended bucket/action for each of the `17` active conflicts
- `ieee_511_conflict_decisions_20260310.csv`
  - final Section III audit decision table for the same `17` conflicts
- `ieee_511_conflict_review_20260310.md`
  - narrative summary of the conflict review and suggested next steps

How to use
- Treat this folder as supplemental evidence, not automatic canonical truth.
- Use `IEEE_511_OISAC_Results_Screened.csv` to strengthen title/abstract-stage auditability.
- Use `ieee_511_conflicts_vs_canonical.csv` before importing or reconciling any external screening decisions into the canonical Section III trail.
- Use `ieee_511_conflict_triage_20260310.csv` when you need a fast action table.
- Use `ieee_511_conflict_decisions_20260310.csv` when you need the final audit-level disposition for each conflict.
- Use `ieee_511_conflict_review_20260310.md` when you need the reasoning behind those recommendations.

Current status
- Helpful for narrowing the `records_screened = 700` gap.
- Not sufficient to close the full PRISMA freeze by itself.
