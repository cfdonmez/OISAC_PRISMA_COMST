# Full COMST Introduction Audit and O-ISAC Check

## Audit status

The audit covers every eligible Introduction in the local `corp_std` corpus.
All 76 confirmed IEEE *Communications Surveys & Tutorials* papers were read
through the transition to the next major section. `COMST_031` was excluded
because it is an IEEE *Wireless Communications* paper (DOI
`10.1109/MWC.2025.3600205`), not a COMST article.

The three article-level audit records are:

- `GROUP_A_COMST_001_026.md`: 26/26 Introductions;
- `GROUP_B_COMST_027_052_EXCL_031.md`: 25/25 eligible Introductions; and
- `GROUP_C_COMST_053_077.md`: 25/25 Introductions.

This report combines those close readings with the aggregate corpus profile.
It extracts rhetorical functions and transition logic; it does not copy or
imitate the wording of any source article.

## What the corpus actually shows

There is no single COMST sentence style. Published Introductions range from
economical and causal to long, catalogue-like, and heavily promotional. Journal
publication is therefore not, by itself, a reason to reproduce a paper's prose.
The useful commonality is the reader journey followed by the stronger examples.

Across the 76-paper baseline:

- the median Introduction length is 1,962.5 words;
- the median paragraph count is 17;
- the median sentence length is 25.0 words;
- 72/76 Introductions state their scope;
- 61/76 state explicit contributions;
- 39/76 use explicit related-survey positioning; and
- 52/76 include an organization paragraph.

These are descriptive values, not targets. Several of the longest papers impose
substantial reader load through application catalogues, acronym clusters, and
repeated contribution summaries. For the O-ISAC survey, clarity takes priority
over reproducing that length.

## Consolidated COMST narrative recipe

The most reliable Introduction sequence contains nine connected moves.

1. **Begin with a physical or engineering fact.** Show the system doing
   something recognizable before introducing a research label.
2. **Explain why reuse or integration is attractive.** Connect the technical
   fact to an infrastructure, performance, or deployment need.
3. **Reverse benefit into cost.** State what the integration consumes, hides,
   constrains, or makes difficult. This prevents promotional prose.
4. **Narrow the field through its physical regimes.** Explain why apparently
   related platforms cannot be treated as interchangeable.
5. **Define the survey boundary.** Tell the reader what counts, what forms the
   technical connection, and what the definition does not assume.
6. **Expose the unresolved scientific or decision problem.** A strong gap is
   not merely “few surveys exist”; it identifies a comparison, design, or
   interpretation that the existing literature does not yet support.
7. **Position prior surveys fairly.** Group them by purpose or analytical lens,
   state what each group contributes, and derive the remaining need without a
   “first” or “only” claim.
8. **State scope, questions, and contributions as matching operations.** The
   contributions should answer the gap through actions such as classifying,
   reconciling, comparing, explaining, or evaluating—not through breadth alone.
9. **End with a short intellectual roadmap.** Explain the order in which the
   reader will understand the problem, not a mechanical table of contents.

## How strong transitions are built

The strongest papers make each paragraph answer a question created by the
previous one. Their transitions rely on six recurring mechanisms:

- **lexical carry-over:** a key term at the end of one paragraph becomes the
  subject of the next;
- **benefit-to-cost reversal:** an opportunity is immediately bounded by what
  it requires or sacrifices;
- **generic-to-medium-specific contrast:** a broad concept is narrowed by the
  physics of the particular medium;
- **mechanism-to-evidence movement:** a claimed effect is followed by the
  observations or examples that make it concrete;
- **fair-concession-to-gap movement:** prior work is credited before the
  residual limitation is stated; and
- **synthesis after accumulation:** examples lead to one interpretation rather
  than ending as a list.

Short connective sentences are useful when they reset the argument. Repeated
`First`, `Second`, `Moreover`, and `Finally` markers do not create a narrative
unless the underlying causal relation is present.

## Tone and paragraph contract

The preferred tone is confident but bounded. It uses concrete technical nouns
and direct verbs, explains why a claim matters, and carries the condition of a
comparison with the comparison itself. It avoids hype, universal rankings, and
unsupported novelty claims.

A strong paragraph normally performs one primary job:

> main idea -> explanation or evidence -> condition or contrast -> inference

Useful review triggers are 70–120 words per paragraph, three to five sentences,
and an average sentence length near 20–24 words. These are not mechanical rules.
A longer paragraph is acceptable when it preserves one argument; it should be
split when it changes rhetorical job.

## Strong references and negative controls

Particularly useful structural references include:

- `COMST_041`: physical problem to optical opportunity to residual limit;
- `COMST_042`: economy, conceptual boundaries, and lexical continuity;
- `COMST_044`: shared integration concept without erasing medium-specific
  physics—the closest structural analogue to O-ISAC;
- `COMST_048`: a trade-off explained through one causal mechanism;
- `COMST_034` and `COMST_052`: defensible multi-axis scope; and
- `COMST_056`, `COMST_060`, `COMST_063`, `COMST_069`, and `COMST_075`: useful
  problem-to-framework and gap-to-contribution movement.

`COMST_028`, `COMST_037`, `COMST_046`, and `COMST_050` are useful negative
controls for catalogue prose, slogan-like transitions, or excessive navigation.
Their publication status does not make those traits desirable for this survey.

## Current O-ISAC Introduction against the full-corpus recipe

The current file is `manuscript/comst_206_v1/sections/01_INTRODUCTION.tex`.
Its narrative maps cleanly to the full-corpus recipe:

| Current passage | Function | Full-corpus fit |
|---|---|---|
| Lines 4--11 | Light carries environmental signatures; representative modalities | Move 1: strong |
| Lines 13--20 | Reuse motivation, followed by resource and receiver costs | Moves 2--3: strong |
| Lines 22--36 | IMT-2030 context and physically different optical regimes | Move 4: strong |
| Lines 38--46 | Broad operational O-ISAC boundary | Move 5: strong |
| Lines 48--54 | Compact measurement/comparability problem | Move 6: strong |
| Lines 56--64 | Fair positioning against current survey families | Move 7: strong |
| Lines 66--68 | Exact 206-study primary-evidence scope | Move 8a: strong |
| Lines 70--85 | Four non-overlapping intellectual contributions | Move 8b: strong |
| Lines 87--92 | Reader-oriented intellectual route | Move 9: strong |

After the author-approved economy pass, the Introduction contains 679 style
words. Its mean sentence length is 18.9 words, its mean paragraph length is
56.6 words, and the automated list-heavy rate is 16.7%. It triggers no current
COMST-style outlier flag. It is intentionally much shorter than the corpus
median because technical inventories are deferred to the appropriate survey
sections rather than previewed repeatedly.

## Editorial verdict

The revised Introduction is structurally and tonally aligned with the strongest
COMST examples. Its opening is technical rather than ceremonial, PRISMA is not
presented as the scientific novelty, the earlier surveys are acknowledged
fairly, and the four contributions answer the stated comparison problem.

The former 208-word comparability paragraph has been reduced to one compact
rhetorical move. Repeated platform inventories were removed from the
contribution list, repeated comparison-condition lists were confined to the
comparability passage, and the roadmap no longer retells the contributions.
The operational boundary remains separate because inclusion scope and
comparison admissibility answer different questions.

## Author-review checklist for each remaining Introduction passage

1. What single question does this paragraph answer?
2. Was that question created naturally by the preceding paragraph?
3. Does the paragraph explain a mechanism, or merely name examples?
4. If it states a benefit, does it also preserve the relevant cost or condition?
5. Are platforms kept distinct where their physics or measurement plane differs?
6. Is every field-level claim supported at the point where it is made?
7. Are prior surveys described fairly before the remaining gap is claimed?
8. Does each contribution perform a distinct intellectual operation?
9. Can an inventory be moved to a table without losing the argument?
10. Does the closing sentence create the need for the next paragraph?

## Decision

Use the compact Introduction as the working text and subject it to the next
author read-through before freezing it. Do not import prose, counts, or
citations from the unpublished 220/221-study manuscript; it remains only a
historical idea reservoir.
