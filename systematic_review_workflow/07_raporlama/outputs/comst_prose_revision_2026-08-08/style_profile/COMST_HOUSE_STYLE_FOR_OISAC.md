# COMST House Style for the O-ISAC Survey

## What This Profile Is

This profile combines an automated analysis of the local corpus with a complete
rhetorical close reading of all 76 eligible Introduction sections. Selected
papers below serve as reference tiers, not as the limit of the qualitative
audit. The article-level records and consolidated recipe are in
`full_intro_audit/COMST_76_FULL_INTRO_RECIPE_AND_OISAC_CHECK.md`. This is a
writing and reader-load guide, not an instruction to imitate any article's
wording.

The local directory contains 77 labelled records. Seventy-six are confirmed
IEEE Communications Surveys & Tutorials papers. `COMST_031` belongs to IEEE
Wireless Communications (DOI `10.1109/MWC.2025.3600205`) and is excluded from
the COMST baseline.

## Reference Tiers

### Primary prose exemplars

- `COMST_042`: economical context-to-problem-to-contribution progression.
- `COMST_041`: gradual movement from a broad practical setting to a concrete
  communications constraint and then to the technical response.
- `COMST_047`: a focused motivation built around a small number of technical
  drivers rather than a catalogue of applications.
- `COMST_044`: integrated sonar and communication; especially relevant for
  explaining two historically separate functions before their integration.
- `COMST_025`: keeps systematic-review mechanics outside the opening story.
- `COMST_026`: useful conditional comparison logic - no technology is best
  under every operating condition.

### Structural references with cautions

- `COMST_015`: useful integration progression, but too acronym-dense in places.
- `COMST_067`: useful question-led motivation, but the introduction is long.
- `COMST_037`, `COMST_054`, and `COMST_068`: published structural examples,
  but not preferred language models because of long lists, promotional wording,
  or excessive concept loading.

## Reader Journey for the Introduction

The Introduction must move through these rhetorical tasks in order:

1. Present a concrete communications/sensing situation.
2. Explain the core O-ISAC idea in ordinary technical language.
3. Show why optical implementations form several physically different families.
4. Identify the scientific problem: results that look similar are not always
   comparable.
5. Position the work fairly against current surveys.
6. State the review scope and its research questions.
7. State three or four reader-facing technical contributions.
8. Give a short article map.

For this manuscript, the author-reviewed target is approximately 650-900 words
across the nine rhetorical moves below. This is deliberately shorter than the
corpus median: modality, metric, and validation inventories belong in their
technical sections and should not be previewed repeatedly in the Introduction.

Introduction constraints:

- No equation.
- No detailed PRISMA flow counts.
- Mention 206 studies once for scope.
- Keep PRISMA out of the opening story. If named in the Introduction, use no
  more than one subordinate transparency clause; the full account belongs in
  Methods.
- Introduce no more than two new abbreviations in the first two paragraphs.
- Do not claim to be the first or only optical-ISAC survey.
- Do not compare record performance values across incompatible platforms.

## Paragraph Contract

Each paragraph should perform one main rhetorical job:

> main idea -> explanation or evidence -> condition/contrast -> inference or transition

Practical guardrails:

- Prefer 3-5 sentences per paragraph.
- Prefer 70-120 words per paragraph.
- Review paragraphs over 150 words.
- Target an average sentence length around 20-24 words.
- Review sentences over 38 words.
- Split sentences over 45 words unless a precise definition requires the length.
- Avoid inline lists longer than three items.
- Introduce no more than three new abbreviations in one paragraph.
- Use a short sentence deliberately when the paragraph needs a conceptual reset.

These are review triggers rather than mechanical rejection rules.

## Voice

- Use `we review`, `we compare`, and `we identify` for author actions.
- Use evidence-centred subjects for findings: `the evidence shows`, `the
  included studies indicate`, or `the comparison reveals`.
- State the operating condition or evidence boundary with broad claims.
- Prefer direct verbs to abstract noun stacks.
- Build reader-facing prose around the scientific construct, evidence, and
  conditions that support interpretation. Avoid defect-first disclaimers,
  `neither ... nor`, repeated `not`, and denylist cadence.
- Do not use author-inserted colons or semicolons in reader-facing prose,
  captions, or table notes. Connect the thought with a natural conjunction or
  separate it into clear sentences.
- Use `however`, `therefore`, and similar transitions only for real logical
  relations.
- Remove promotional language such as `revolutionary`, `groundbreaking`,
  `transformative`, `vast untapped frontier`, or `undeniably`.
- Use `comprehensive` only if the stated scope and comparison table justify it.

## Technical Sections

Each major technical section should:

1. Tell the reader in two to four sentences what the section will explain.
2. Define terms only when the reader needs them.
3. Group studies by mechanism, design choice, or comparison axis rather than
   narrating one paper at a time.
4. Leave inventories to tables; use prose to explain patterns and exceptions.
5. Close with a compact synthesis: what was learned, when it holds, what limit
   remains, and why the next section follows.

Use representative primary studies to anchor a pattern. Do not use repeated
`authors in [x] proposed` catalogue prose as the default narrative.

## Methods and PRISMA Reporting

The method must be transparent but proportionate:

- Put search, screening, mapping, extraction, TQAF, and claim-governance detail
  in the Methods section.
- Correctly describe OSF record `7f6wb` as retrospective registration, not
  prospective preregistration.
- Explain deviations from the frozen historical registration.
- Keep the PRISMA flow in a compact Results subsection.
- Use report, study, and claim denominators explicitly and consistently.

## Evidence-Synthesis Paragraphs

Preferred order:

> observed pattern -> supporting evidence -> validity condition -> design meaning

Percentages and counts should support the interpretation, not replace it. A
paragraph containing several distributions should usually lead with the
scientific pattern and move the full inventory to a table.

## Discussion and Research Directions

Discussion sequence:

> finding -> plausible explanation -> implication -> limitation

Every future direction should identify:

1. the observed evidence gap;
2. why current approaches do not close it;
3. the study, experiment, or benchmark that is needed; and
4. the success measure.

Avoid generic statements such as `AI can improve O-ISAC` unless the decision
task, missing data, baseline, and joint communication-sensing success metrics
are specified.

## Conclusion

Target 220-300 words in two or three paragraphs. The Conclusion should add no
new citation, number, or claim. It should state the principal field-level
findings, the evidence boundary, and the conditions required for progress. It
should not repeat the paper's table of contents.

## Automated Review Triggers

The accompanying `comst_style_audit.py` flags:

- sentence and paragraph length outliers;
- sentences dominated by long comma-separated lists;
- high acronym and parenthetical density;
- high numeric density;
- unusually dense method vocabulary in an Introduction;
- promotional language;
- sparse transitions; and
- missing Introduction scope language.

Automated flags always require human interpretation and an independent
scientific-evidence check.
