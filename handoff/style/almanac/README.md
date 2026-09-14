# COMST 76 Full-Text Almanac

## Objective

This package compares the complete rhetorical and visual architecture of 76
eligible local IEEE *Communications Surveys & Tutorials* articles with the new
206-study O-ISAC survey candidate. It is designed to answer section-level
author questions: what published surveys normally do at this point, what the
O-ISAC draft currently does, why a difference is defensible or problematic,
and how a proposed change affects neighboring sections.

`COMST_031` is excluded because it is an *IEEE Wireless Communications*
article rather than a COMST article.

## Evidence Layers

- `data/comst_papers_harmonized_master.csv`: canonical 76-paper metrics.
- `data/comst_sections_harmonized_master.csv`: 3,994 harmonized section units.
- `data/comst_visuals_close_read_master.csv`: 1,750 coded figures and tables.
- `data/group_*_*.csv`: three disjoint close-read coding groups and their
  preserved audit trail.
- `reports/GROUP_*_FULLTEXT_CLOSE_READ.md`: paper-by-paper human reading notes.
- `data/*statistics.csv`: paper-clustered descriptive statistics, role and
  transition distributions, visual-function summaries, and missingness.
- `data/reliability_*`: independent six-paper cross-coding, disagreements,
  source-based adjudication, and the final `COMPLETE` reconciliation.
- `data/oisac_decision_crosswalk_final.csv`: 71 active-manuscript units with a
  registered decision, rationale, evidence gate, and adjacent-section effect.
- `data/oisac_visual_plan.csv`: six proposed figures and eight proposed tables;
  their visual design has not yet been implemented.
- `COMST_76_FULLTEXT_ALMANAC.md`: final human-readable decision almanac.
- `COMST_76_STATISTICAL_ALMANAC.xlsx`: final auditable analytical workbook.

## Current Status

The full-text almanac is complete. All 76 eligible papers were close-read and
the canonical merge contains 3,994 heading-bounded units and 1,750 numbered
visuals (1,096 figures and 654 tables). The exact paper-ID, key, count,
boundary, category, and missing-value gates pass.

Independent double coding covered 243 section units and 137 visuals from six
prespecified papers. All 1,994 field-level disagreements were adjudicated
against the source text: 135 primary codes were confirmed, 1,774 secondary
codes were adopted, and 85 third values were assigned. No disagreement is
pending.

The O-ISAC decision register contains all 71 active manuscript units. Its
current action distribution is 31 retain, 11 merge, 8 add-table, 7 trim,
6 add-figure, 3 add-citations, 3 rewrite-transition, 1 expand, and 1
move-to-supplement. These actions remain unimplemented and await author review.

The active O-ISAC manuscript is not edited during almanac construction.
Manuscript changes form a separate reviewable stage after the almanac has
passed coverage and reconciliation checks.

## Interpretation Boundary

The corpus describes published COMST practice; it does not establish that
matching a word count, sentence pattern, or number of visuals causes
acceptance. Subject-specific choices remain governed by the O-ISAC evidence
base. The almanac uses journal patterns to improve reader navigation,
tutorial value, comparison design, and editorial fit without copying source
wording.
