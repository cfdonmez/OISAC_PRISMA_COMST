# V3 I-A Background and Motivation revision

Date: 2026-09-07
Working tree: C:\OISAC\worktrees\comst-v3-20260906

## Applied scope

- Rewrote the four I-A paragraphs around physical opportunity, shared design,
  two bounded experimental examples, and the synthesis needed for design selection.
- Connected Figure 1's shared-resource question to the prose. Updated its caption;
  the approved image itself is unchanged.
- Revised the I-B opening and shortened its closing to make the handoff explicit
  without repeating I-C contributions.
- Table I and Scope and Contributions are textually unchanged. The other 29
  inventoried manuscript inputs retain their before-turn SHA-256 values.
- Canonical V2, full-revision RC1, Sections II-IX, the bibliography, and evidence
  data were not edited.

## Preservation and reading copy

- Before-turn Introduction: governance/section1_before_background_revision_2026-09-07.tex.
  Its text matches the before-turn source after newline normalization.
- Reading PDF: output/pdf/OISAC_COMST_V3_INTRO_BACKGROUND_REVISED_2026-09-07.pdf.
- Reading PDF and manuscript/main.pdf SHA-256 both equal
  8880C527DB2B1C7703DCABF502E6BDCE944341869EBEF9D16522CAC0A13F8594.

## Scientific and prose checks

The COMST house-style and author-governed claim-language recipes in
governance/v3_source_snapshot_2026-09-06 were read and applied. Physical meaning
leads the paragraphs; internal status codes and promotional novelty claims are absent.

- SCR00057 retains fixed communication launch power while sensing-probe power
  increases. This is not a fixed-total-power allocation or the separate
  pre-compensation gain.
- SCR00196 retains position-guided beamforming and improvement at tested
  locations. No demonstrated real-time closed-loop claim was introduced.
- Optical signal generation is stated as one possible photonic implementation
  using "can generate"; optically processed wireless systems are not excluded.
- Shared infrastructure does not imply an identical waveform in every platform.
- Independent AI read-through checked source support and continuity through
  I-B, I-C, and the opening of Section II. It is not a human-review decision.

A scoped prose count excludes citations, headings, and Figure 1/caption.
Hyphenated words count as one word and the figure reference as one token.

| I-A measure | Before | After |
|---|---:|---:|
| Words | 372 | 346 |
| Paragraphs | 4 | 4 |
| Sentences | 22 | 18 |
| Mean sentence length | 16.9 | 19.2 |
| Longest sentence | 27 | 26 |

The revised paragraphs contain 92, 89, 79, and 86 words. I-A has no inserted
colons/semicolons, author-name-plus-et-al wording, or raw missingness labels.
All 17 distinct Introduction citation keys resolve in the local bibliography.

The whole-Introduction automated report is
governance/qa/INTRO_BACKGROUND_STYLE_2026-09-07.md. It uses a different TeX
parser from the scoped I-A count and retains an "explicit transitions sparse"
flag. Paragraph continuity was checked directly; extra transition adverbs were
not inserted merely to remove the flag.

## Build and boundary

latexmk completed successfully with resolved references and citations, no
missing characters, and no overfull boxes. Underfull spacing warnings remain,
including an I-A paragraph warning. git diff --check passed.

No PDF visual inspection was performed, following the user's preference for
text-level checks on this revision. This is an author-reading revision, not a
whole-manuscript submission-release assessment.
