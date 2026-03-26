# IEEE 511 Conflict Review - 2026-03-10

Purpose
- This note reviews the `17` active conflicts in `screening/external/ieee_511_conflicts_vs_canonical.csv`.
- These are cases where the external IEEE screened file says `EXCLUDE` but the current canonical corpus says `included`.

Summary decision buckets
- `9` records are recommended to remain in the primary corpus.
- `4` records are recommended to be removed from the primary corpus under the current Section III wording.
- `4` records are policy conflicts that are best treated as `related survey/context` items unless Section III is broadened.

Audit resolution status
- These `17` rows are no longer left as `manual_review_required`.
- `screening/external/ieee_511_conflicts_vs_canonical.csv` now carries audit decision statuses for all rows.
- `screening/external/ieee_511_conflict_decisions_20260310.csv` records the final Section III audit disposition:
  - `9` rows retained in the current Section III canonical interpretation
  - `8` rows flagged as whole-manuscript rebaseline candidates
- No Section III corpus count change is applied from these `17` rows in this turn; any removal/contextualization of the flagged `8` records requires a broader manuscript-wide rebaseline beyond the current Section III freeze.

Why the external IEEE file disagrees
- The external IEEE screening pass appears to apply a narrower interpretation of "optical" and excludes several `photonics-assisted THz/mmWave` papers as if they were RF-only.
- The current manuscript, especially [section_01_introduction.md](/C:/Users/fdonmez/Drive’ım%20(cfdonmez@gmail.com)/AKU_WorkSpace/survey_fdgit/OISAC_PRISMA_COMST/drafts/section_01_introduction.md), explicitly treats `photonic-THz / optical–THz bridging` as part of the O-ISAC taxonomy.
- A second disagreement source is policy drift: the current corpus includes some `survey/review/context` works that help Section I gap analysis, but [section_03_methodology.md](/C:/Users/fdonmez/Drive’ım%20(cfdonmez@gmail.com)/AKU_WorkSpace/survey_fdgit/OISAC_PRISMA_COMST/drafts/section_03_methodology.md) and [prisma_proto.md](/C:/Users/fdonmez/Drive’ım%20(cfdonmez@gmail.com)/AKU_WorkSpace/survey_fdgit/OISAC_PRISMA_COMST/protocol/prisma_proto.md) are written closer to a primary-study evidence base.

Bucket details
- `keep_canonical`
  - `O_ISAC_159`, `O_ISAC_241`, `O_ISAC_242`, `O_ISAC_252`, `O_ISAC_300`, `O_ISAC_310`, `O_ISAC_349`, `O_ISAC_356`, `O_ISAC_360`
  - Rationale: these are optical-domain or photonic-THz bridging works that fit the declared taxonomy better than the external IEEE filter assumes.
- `remove_from_primary_corpus`
  - `O_ISAC_160`, `O_ISAC_162`, `O_ISAC_206`, `O_ISAC_340`
  - Rationale: current evidence suggests RF-only, generic 6G ISAC, or architecture-level non-O-ISAC scope.
- `contextual_only_policy_conflict`
  - `O_ISAC_161`, `O_ISAC_163`, `O_ISAC_327`, `O_ISAC_368`
  - Rationale: these are survey/review/context works that Section I currently uses, but they are difficult to defend as primary studies under the strict Section III wording.
Recommended action order
1. Decide the policy question for `O_ISAC_161`, `O_ISAC_163`, `O_ISAC_327`, and `O_ISAC_368`.
2. If Section III remains strict, remove `O_ISAC_160`, `O_ISAC_162`, `O_ISAC_206`, and `O_ISAC_340` from the primary PRISMA corpus.
3. Retain the nine photonic-THz / optical-bridging papers as canonical, and do not let the external IEEE file override them.

Key implication
- The main remaining issue is no longer "the IEEE file found 17 bad inclusions."
- The real issue is that the project currently mixes:
  - primary O-ISAC evidence,
  - contextual related-survey works.
- The earlier `O_ISAC_347` metadata-corruption case has now been resolved by excluding that record from the canonical primary corpus.
