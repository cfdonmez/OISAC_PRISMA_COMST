A) Scenario 3 (case)
1) Case title (macro domain tag): Underwater raw-only asymmetry (`underwater_harsh`).
2) View-1 definition (study_flag_count; structured tags): Structured study-level tagging records `study_flag_count=16` for `underwater_harsh`.
3) View-2 definition (raw_evidence_count and strict_evidence_count; extracted evidence rows): Extracted evidence rows report `raw_evidence_count=123` and `strict_evidence_count=23` under raw and strict gates.
4) Numeric discrepancy statement: `flag_count=16`, `raw_count=123`, `strict_count=23`; deltas are `raw_only_vs_flag=107` and `strict_only_vs_flag=7` (comparison row #5).
5) Representative example note: The underwater raw-only pool includes `O_ISAC_021`, so the contrast is instantiated in concrete extracted rows, not an isolated instance (examples row #12; [O_ISAC_021]).
6) Interpretation: The raw view captures many mentions beyond structured study tags. After strict gating, the surplus contracts from `+107` to `+7`, showing strong dependence on evidence-support thresholds. The divergence is therefore a view-definition effect.

B) Scenario 4 (case)
1) Case title (macro domain tag): Space strict-view uplift (`space_satellite`).
2) View-1 definition (study_flag_count; structured tags): Structured study-level tagging records `study_flag_count=17` for `space_satellite`.
3) View-2 definition (raw_evidence_count and strict_evidence_count; extracted evidence rows): Extracted evidence rows report `raw_evidence_count=135` and `strict_evidence_count=34` after raw/strict gating.
4) Numeric discrepancy statement: `flag_count=17`, `raw_count=135`, `strict_count=34`; deltas are `raw_only_vs_flag=118` and `strict_only_vs_flag=17` (comparison row #6).
5) Representative example note: The space strict-only set includes `O_ISAC_070`, confirming strict-gated surplus in representative extracted rows for this domain (examples row #16; [O_ISAC_070]).
6) Interpretation: Even after strict filtering, evidence-row totals remain above the flag baseline. This indicates support-qualified domain evidence can remain outside study-level tags. The two views are complementary rather than interchangeable.

C) Key takeaways
- Raw vs strict gate effects are large: underwater shifts from `+107` raw-only to `+7` strict-only, and space from `+118` to `+17` (comparison rows #5, #6).
- Strict extraction can still expand survey coverage versus study flags (`34` strict vs `17` flags in space), so strict-gated evidence should be interpreted as additive coverage information (comparison row #6).
- Row-level representativeness is visible in the selected pools (`O_ISAC_021` underwater raw-only; `O_ISAC_070` space strict-only), reducing dependence on single-paper anecdotes (examples rows #12, #16).
- Domain-dependent annotation/extraction bias remains a risk because strict deltas differ under the same pipeline (`+7` underwater vs `+17` space) (working hypothesis; comparison rows #5, #6).
