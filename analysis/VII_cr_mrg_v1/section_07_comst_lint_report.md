# Section VII COMST Lint Report

Scope: editorial/style/structure normalization only on `section_07_draft.md`.
Output file: `section_07_draft_comst_polished.md`.

Integrity checks:
- No new cite keys introduced.
- Existing citations preserved and attached to the same claims.
- ORIS canon preserved (`OIRS`/standalone `IRS` not introduced).
- Bracket-safe math preserved.
- VII-G comparison/examples row references unchanged.

## Change Log

| Location (line range, polished file) | Before | After | Reason (Checklist Mapping) |
|---|---|---|---|
| 3, 42, 78 | `VII-A...`, `VII-B...`, `VII-C...` (plain lines) | `### VII-A...`, `### VII-B...`, `### VII-C...` | Normalize subsection heading hierarchy (Checklist Sec. 4: merge-time gate consistency). |
| 5, 8, 21 | No subhead labels in VII-A | Added `#### Context`, `#### Scenarios`, `#### Math Anchor` | Normalize internal subsection structure (Checklist Sec. 4; survey readability consistency). |
| 44, 47, 60 | No subhead labels in VII-B | Added `#### Context`, `#### Scenarios`, `#### Math Anchor` | Normalize internal subsection structure (Checklist Sec. 4; survey readability consistency). |
| 80, 83, 96 | No subhead labels in VII-C | Added `#### Context`, `#### Scenarios`, `#### Math Anchor` | Normalize internal subsection structure (Checklist Sec. 4; survey readability consistency). |
| 225, 227, 230 | VII-G started as free paragraph flow without section/sub-block headers | Added `### VII-G. Dual-View Consistency Layer`, `#### Context`, `#### Cases` | Normalize heading hierarchy and section structure for VII-G (Checklist Sec. 4). |
| 36, 72, 108, 141, 174, 217, 241 | Variants: `Key takeaways for this vertical:`, `#### Key Takeaways`, `Key takeaways:` | Unified closure line: `**Key takeaways and application priorities.**` | Standardize subsection closures to COMST-style synthesis line (Checklist Sec. 3: subsection closing style expectations). |
| 180 | `Transition: Having completed the domain-specific verticals, VII-F synthesizes ...` | `Consequently, VII-F synthesizes ... after the domain-specific verticals.` | Remove pipeline-style transition label and use COMST transition cue (Checklist Sec. 1: contrast-and-synthesis transitions; Sec. 4 gate). |
| 223 | `Transition: Building on this coverage-and-transfer synthesis, VII-G reconciles ...` | `Therefore, VII-G reconciles ... by building on the coverage-and-transfer synthesis.` | Remove pipeline-style transition label and use COMST transition cue (Checklist Sec. 1: contrast-and-synthesis transitions; Sec. 4 gate). |
| 186 | `The patched evidence base reports ...` | `The evidence base reports ...` | Remove pipeline/processing phrasing for survey voice normalization (Checklist Sec. 1: required tone cues). |
| 203 | `... keeps the portfolio anchor selected in Run4:` | `... keeps the selected portfolio anchor:` | Remove pipeline run-reference artifact; keep deployment-facing survey tone (Checklist Sec. 1: required tone cues). |

