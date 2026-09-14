# COMST Full-Text Almanac: Cross-Coding Reliability Protocol

## Purpose

The close-reading layer contains interpretive judgments. A small, stratified
cross-coding exercise is used to measure whether those judgments are stable
across coders. Reliability is a quality-control device, not proof that a code
is objectively true and not a basis for inferring publication probability.

## Sampling

Six papers are selected before inspecting agreement results. The sample spans
the three primary coding groups and deliberately includes different body
architectures:

- `COMST_004`: comparison-led, fork-and-rejoin architecture;
- `COMST_019`: optimization-led architecture;
- `COMST_041`: concise, mechanism-led survey prose;
- `COMST_044`: integration-led architecture with explicit transfer limits;
- `COMST_065`: late-corpus architecture and visual practice;
- `COMST_067`: late-corpus architecture and visual practice.

Each secondary coder receives fixed source-line and heading boundaries but not
the primary coder's qualitative labels. This prevents boundary disagreement
from being mistaken for rhetorical-role disagreement.

## Fields to Recode

Every sampled section is independently recoded for:

- `normalized_primary_role`;
- `opening_relation`;
- `closing_relation`;
- `paragraph_contract`;
- `sentence_architecture`;
- `dominant_organization`;
- `tone`;
- `tutorial_depth`;
- `comparison_explicitness`;
- `visual_dependency`;
- the ordered set of rhetorical moves in `move_sequence`.

Every numbered visual in the sampled papers is independently recoded for:

- `visual_function`;
- `placement_within_section`;
- `prose_prepares_before`;
- `prose_interprets_after`;
- `data_density`;
- `inventory_offload`.

## Statistics

For single-label categorical fields, report raw percentage agreement and
Cohen's kappa. For sparse fields, always show the contingency counts because a
high percentage can coexist with a low kappa. For `move_sequence`, report:

1. exact sequence agreement;
2. Jaccard overlap of the unique move sets; and
3. agreement on the first and final move.

For the visual coding fields, report the same single-label statistics. Missing
values are not silently recoded as `none`; they are reported separately.

Bootstrap 95% confidence intervals are descriptive and use a fixed seed of
`20260810`. No significance test is used to claim that the coding is valid.

## Adjudication

Disagreements are examined against the source text. The primary code is changed
only when the second reading exposes a clearly better fit to the coding manual.
The original and adjudicated labels remain in the reliability dataset. Any
manual category that repeatedly produces disagreement is narrowed or clarified
before the final corpus statistics are frozen.

## Completion Gate

Reliability QA is complete when:

1. all six sampled papers have fixed-boundary secondary codes;
2. section and visual rows reconcile with the primary records;
3. agreement statistics and disagreement counts are reproducible from a script;
4. every adjudicated change is recorded with a short rationale; and
5. the Markdown report and workbook show the same headline values.
