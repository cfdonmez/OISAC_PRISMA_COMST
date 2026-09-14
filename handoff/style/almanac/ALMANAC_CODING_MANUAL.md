# COMST 76 Full-Text Almanac: Coding Manual

## Purpose

This almanac models how published *IEEE Communications Surveys & Tutorials*
articles organize, explain, compare, and visually support a survey. It is a
decision aid for the new 206-study O-ISAC manuscript. It is not a source of
phrasing to copy and it is not an acceptance predictor.

The corpus contains `COMST_001`--`COMST_077`. `COMST_031` is excluded because
its DOI and front matter identify it as an *IEEE Wireless Communications*
article. The eligible denominator is therefore 76.

## Two Evidence Layers

1. **Automated layer:** headings, section boundaries, word/sentence/paragraph
   counts, citation markers, transition markers, equations, tables, figures,
   and their approximate locations.
2. **Close-reading layer:** rhetorical purpose, reader journey, opening and
   closing moves, comparison logic, tutorial strategy, evidence use, visual
   purpose, transition quality, and the relationship to adjacent sections.

Automated values and human-coded judgments must remain separate fields.
Extraction uncertainty must be recorded rather than silently resolved.

## Unit of Analysis

The primary unit is one visible heading-bounded section or subsection. Every
eligible paper must have a complete ordered map from Abstract through its last
substantive synthesis/conclusion section. References, biographies,
acknowledgments, copyright boilerplate, and extraction-only image filenames are
not prose units.

The visual unit is one numbered figure or table. Multi-panel items remain one
record unless the panels perform materially different rhetorical jobs; in that
case the parent item receives one record and the panel functions are summarized
in `visual_subfunctions`.

## Normalized Section Roles

Assign one primary role and zero or more secondary roles:

- `abstract`
- `introduction_motivation`
- `related_surveys_gap`
- `scope_contributions_organization`
- `background_foundations`
- `taxonomy_framework`
- `system_model_architecture`
- `methods_review_protocol`
- `corpus_descriptive_results`
- `technical_family_synthesis`
- `integration_design`
- `metrics_performance_comparison`
- `tradeoff_optimization`
- `validation_experiment_reproducibility`
- `technology_enabler`
- `application_use_case`
- `standardization_implementation`
- `challenges_open_issues`
- `future_directions_roadmap`
- `lessons_learned_discussion`
- `limitations`
- `conclusion`
- `other_substantive`

Topic nouns do not determine the role. Code the work the section performs for
the reader.

## Rhetorical-Move Codes

Code the ordered moves actually present. Multiple codes may occur in one unit:

- `context`: establishes the technical setting.
- `need`: explains why the problem matters now.
- `mechanism`: explains how a system or phenomenon works.
- `problem`: identifies a limitation, conflict, or failure mode.
- `gap`: distinguishes what prior surveys or methods do not resolve.
- `definition`: fixes terminology or scope.
- `taxonomy`: introduces organizing categories.
- `example`: grounds a general pattern in representative studies.
- `comparison`: contrasts approaches under an explicit axis.
- `condition`: states when a finding or comparison holds.
- `evidence`: reports counts, ranges, or literature-supported observations.
- `implication`: explains design or research meaning.
- `limitation`: bounds the authors' own inference.
- `recommendation`: proposes a practice, experiment, or benchmark.
- `contribution`: states what the survey provides.
- `navigation`: previews or links sections.
- `synthesis`: closes a group of evidence with a field-level takeaway.

Store move sequences as ordered `>`-joined codes, for example
`context>problem>taxonomy>comparison>synthesis`.

## Transition and Sentence-Architecture Codes

For each unit, record:

- opening relation to previous unit: `continuation`, `cause`, `contrast`,
  `narrowing`, `broadening`, `example`, `definition`, `return`, `reset`, or
  `none`;
- closing relation to next unit using the same vocabulary;
- dominant paragraph contract: `claim-explain-evidence-inference`,
  `mechanism-condition-example-implication`, `finding-explanation-implication-
  limitation`, `gap-cause-test-success`, `catalog`, or `mixed`;
- dominant sentence architecture: `simple_direct`, `balanced_compound`,
  `conditional`, `contrastive`, `enumerative`, `definition_heavy`, or `mixed`;
- tone: `tutorial`, `analytical`, `critical`, `procedural`, `promotional`,
  `cautious`, or `mixed`;
- whether the prose is mainly mechanism-led, paper-led, metric-led,
  chronology-led, or taxonomy-led.

Transition-word counts are descriptive. A transition is judged effective only
when the logical relation is real.

## Figure and Table Function Codes

Figures:

- `survey_roadmap`
- `taxonomy_map`
- `system_architecture`
- `signal_processing_flow`
- `physical_mechanism`
- `protocol_workflow`
- `timeline_evolution`
- `performance_plot`
- `tradeoff_plot`
- `application_map`
- `challenge_roadmap`
- `bibliometric_distribution`
- `other`

Tables:

- `related_survey_comparison`
- `acronym_notation`
- `taxonomy_definition`
- `study_inventory`
- `system_parameter_comparison`
- `metric_definition_comparison`
- `method_algorithm_comparison`
- `dataset_testbed_comparison`
- `performance_comparison`
- `tradeoff_matrix`
- `application_mapping`
- `challenge_future_work`
- `standardization_summary`
- `quality_reproducibility`
- `other`

For every visual, code its first mention, approximate placement, whether prose
prepares the reader before it, whether prose interprets it afterward, its data
density, and whether it carries inventory that would otherwise overload prose.

## Canonical Controlled Vocabularies

The master datasets use the following canonical values. Group-level source
values are retained in `*_raw` fields, and every non-identity recode is recorded
in a harmonization flag. A value that is absent from these mappings is an error;
it must not be silently coerced.

Section judgments:

- `tutorial_depth`: `brief`, `moderate`, `deep`;
- `comparison_explicitness`: `none`, `implicit`, `explicit`, `systematic`;
- `visual_dependency`: `none`, `supporting`, `substantial`, `essential`;
- `coding_confidence`: `low`, `medium`, `high`.

Legacy section mappings:

| Field | Source values | Canonical value |
|---|---|---|
| `tutorial_depth` | `none`, `light`, `low`, `brief` | `brief` |
| `tutorial_depth` | `medium`, `moderate` | `moderate` |
| `tutorial_depth` | `high`, `deep` | `deep` |
| `comparison_explicitness` | `low`, `medium`, `implicit` | `implicit` |
| `comparison_explicitness` | `moderate`, `high`, `explicit_local`, `explicit` | `explicit` |
| `comparison_explicitness` | `explicit_systematic`, `systematic` | `systematic` |
| `visual_dependency` | `low`, `none` | `none` |
| `visual_dependency` | `medium`, `moderate`, `supportive`, `supporting` | `supporting` |
| `visual_dependency` | `high`, `substantial` | `substantial` |

Visual judgments:

- `placement_within_section`: `early`, `middle`, `late`;
- `first_mention_relation`: `before_visual`, `at_visual`, `after_visual`,
  `not_recovered`;
- `prose_prepares_before`, `prose_interprets_after`, and
  `inventory_offload`: `yes`, `partial`, `no`, `unclear`;
- `data_density`: `low`, `medium`, `high`, `unclear`.

Legacy visual mappings:

| Field | Source value | Canonical value |
|---|---|---|
| `placement_within_section` | `section_opening` | `early` |
| `placement_within_section` | `section_middle` | `middle` |
| `placement_within_section` | `section_closing` | `late` |
| `first_mention_relation` | `before_caption` | `before_visual` |
| `first_mention_relation` | `at_caption_or_no_earlier_mention` | `at_visual` |
| `first_mention_relation` | `mention_only_caption_unrecovered` | `not_recovered` |

The `at_caption_or_no_earlier_mention` recode is deliberately flagged because
the source code combines two states. It supports placement-level description,
not a claim that an earlier prose search was certainly complete. `partial` and
`unclear` remain distinct; neither is converted to `no`.

## Required Section-Level Fields

Each row in the section dataset must contain:

`paper_id`, `title`, `doi`, `year`, `source_path`, `section_order`,
`heading_level`, `heading_raw`, `parent_heading`, `normalized_primary_role`,
`normalized_secondary_roles`, `start_line`, `end_line`, `start_page`,
`end_page`, `word_count`, `sentence_count`, `paragraph_count`,
`mean_sentence_words`, `median_sentence_words`, `short_sentence_ratio_12`,
`long_sentence_ratio_35`, `mean_paragraph_words`, `citation_group_count`,
`citation_marker_count`, `unique_citation_markers`, `transition_count`,
`transition_profile`, `semicolon_count`, `question_count`, `equation_count`,
`figure_mentions`, `table_mentions`, `figure_items`, `table_items`,
`opening_relation`, `closing_relation`, `move_sequence`,
`paragraph_contract`, `sentence_architecture`, `dominant_organization`, `tone`,
`tutorial_depth`, `comparison_explicitness`, `visual_dependency`,
`reader_takeaway`, `adjacent_section_effect`, `coder_note`, `coding_confidence`,
and `extraction_flags`.

`reader_takeaway`, `adjacent_section_effect`, and `coder_note` must be concise
paraphrases. Do not reproduce source paragraphs.

## Required Paper-Level Fields

Every eligible paper must record total narrative words, page span when
recoverable, top-level and lower-level heading counts, reference-list size,
figures, tables, equations, citation density, section-role sequence, whether a
related-survey table appears, whether an early survey-roadmap figure appears,
and whether challenges, lessons learned, limitations, and conclusion are
separate or combined.

## O-ISAC Crosswalk Fields

For every current O-ISAC section and subsection, the almanac must report:

- its intended reader job;
- matched COMST role and comparison denominator;
- corpus distribution and representative architectural patterns;
- what the O-ISAC draft currently does;
- what is already aligned;
- what is missing or overused;
- a decision: `retain`, `trim`, `expand`, `merge`, `move_to_supplement`,
  `add_table`, `add_figure`, `add_citations`, or `rewrite_transition`;
- the scientific reason for that decision;
- the expected effect on the preceding and following sections;
- the evidence/citation gate that must remain intact;
- implementation status and author-review status.

## Statistical Reporting Rules

- Report `n`, minimum, p10, Q1, median, Q3, p90, and maximum for continuous
  variables.
- Report numerator/denominator and percentage for categorical variables.
- Show both all-76 results and a documented strong-prose reference subset when
  language is being evaluated.
- Do not treat topic-dependent figure, table, equation, or word counts as
  acceptance thresholds.
- Do not use significance tests to imply that matching a journal corpus causes
  acceptance. Effect sizes and percentile positions are descriptive.
- Record parser and OCR failures explicitly. Never convert missing values to
  zero.
- Separate current manuscript values from planned values.

## Completion Gate

The almanac is complete only when:

1. all 76 eligible papers have paper-level records;
2. every substantive heading-bounded unit has a section record;
3. all numbered figures and tables have a function record or an extraction
   exception;
4. paper totals reconcile with section totals within documented exclusions;
5. every O-ISAC section has a completed crosswalk and decision rationale;
6. the Markdown report and Excel workbook reconcile on headline statistics;
7. the workbook passes formula, range, and rendered-layout checks;
8. manuscript changes remain a separate, reviewable step after the almanac.
