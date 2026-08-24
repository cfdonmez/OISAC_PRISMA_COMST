# Trade-off Denominator Reconciliation

## Reason for the check

The earlier manuscript wording combined the 404-row governed trade-off ledger
with the 168-study substantive denominator. Direct row-level review showed that
these figures describe different universes.

## Recomputed result

The public projection
`tradeoff_evidence_404_public.csv` contains:

- 404 rows;
- 169 unique nonblank `study_cluster_id` values;
- two rows with `reported_status = absent`; and
- 402 non-absent rows from 168 contributing studies.

The two audit sentinels are:

- `TRD-SCR00008-001`: an absence-status row in a study that also contributes
  two non-absent records; and
- `TRD-SCR00038-G2-001`: the only trade-off row for its study.

After removing both sentinels, the substantive set partitions into 218 records
eligible for quantitative use and 184 eligible for qualitative use. Of these,
371 are conditionally comparable and 31 are descriptive only; 371/402 is 92.3
percent.

## Reporting rule

- Use **404 rows / 169 studies** only when describing the governed extraction
  ledger, and state that it includes two explicit absence-status audit rows.
- Use **402 substantive records / 168 studies** for scientific trade-off
  synthesis.
- Do not call either records or rows experiments, effects, or statistically
  independent observations.
- The primary claim-ledger arithmetic remains 8,203 = 3,020 evidence + 4,779
  metric + 404 trade-off-ledger rows. This governance total is distinct from
  the 402-record substantive trade-off synthesis.

## Consequential corrections

Removing the two sentinel rows changes the substantive trade-off partition to
218 quantitative + 184 qualitative and the conditional subset to 371/402. The
two rows belong to different locked families. After removing
`TRD-SCR00038-G2-001`, `bandwidth_spectrum_or_resource_allocation` contains 94
records from 70 studies, including 50 quantitative, 44 qualitative, and 89
conditional records. After removing `TRD-SCR00008-001`,
`qualitative_or_partial_general` contains 10 records from 8 studies, including
2 quantitative, 8 qualitative, and 7 conditional records. Other family counts
are unchanged.

This reconciliation supersedes manuscript wording that described all 404
ledger rows as if they came from the 168 studies with non-absent reporting.
