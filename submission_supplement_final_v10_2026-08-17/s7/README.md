# Supplement S7 — Paired-Function Validation View

`S7_CANONICAL_JOIN_206.csv` documents the one-to-one join between the 206-study inventory and the 206 TQAF rows. `S7_PAIRED_FUNCTION_VALIDATION_12.csv` is the publication-facing 12-study maximum-field/deployment subset.

Exactly 12 studies reached maximum validation tier 6. Six of those 12 also received TQAF validation-maturity score 3, the narrower review-specific gate requiring field or deployment outcomes for both communication and sensing. The other six are not failed studies; tier 6 alone does not prove paired-function field validation.

The existing audited TQAF trace provides combined record locators. It does not expose relationship timing or a separate locator-to-function mapping, so those fields remain explicit `NR` values rather than inferred text. Supplement S7 is not the Phase-F S7 6G-relevance domain.

Hard-gate QA status: `PASS_WITH_EXPLICIT_UNRESOLVED_FUNCTION_SPECIFIC_LOCATORS`.
