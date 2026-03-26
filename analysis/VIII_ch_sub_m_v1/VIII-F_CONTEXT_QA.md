# VIII-F CONTEXT QA

## PASS/FAIL Checklist

| Check | Status | Evidence |
|---|---|---|
| placeholders removed | PASS | placeholder scan across D1+D2 = 0 |
| capstone interpretation lock | PASS | D1 states VIII-F is a capstone synthesis, not a new Axis-2 domain |
| no-causality language | PASS | D1 uses observational framing (`observational co-linkage map`, `not as a causal graph`); token scan (`cause/causes/caused/therefore`) = 0 |
| cite-key lock (allowed set only) | PASS | used keys in D1 = `{O_ISAC_049, O_ISAC_107, O_ISAC_133}`; outside-lock keys = none |
| evidence excerpts present | PASS | D2 has 3 cite-key excerpts (<=25 words) + VIII-F artefact evidence block (axis list + E isolated row) |
| length (180-260 words, context paragraph) | PASS | D1 first paragraph word_count = 185 |

## Cite-Key Existence (data/references.bib)

| cite_key | in_references.bib |
|---|---|
| O_ISAC_049 | YES |
| O_ISAC_107 | YES |
| O_ISAC_133 | YES |

## Contract-Violations Summary for Used Keys

| cite_key | status | evidence | handling |
|---|---|---|---|
| O_ISAC_049 | OK | not listed in `contract_violations.csv` | normal wording allowed |
| O_ISAC_107 | FLAGGED | `O_ISAC_107,8C,EVIDENCE_WEAK,MINOR,...` in `contract_violations.csv` | conservative wording applied |
| O_ISAC_133 | OK | not listed in `contract_violations.csv` | normal wording allowed |

## Processed Markdown Validation Log

| cite_key | resolution | index entry used | opened markdown path | sections opened | excerpt locator |
|---|---|---|---|---|---|
| O_ISAC_049 | HIT_FALLBACK | `analysis/II_md_inv.csv:L266` (duplicate also at `L50`; canonical nested path selected) | `data/proc_markdowns/O_ISAC_049/O_ISAC_049/O_ISAC_049.md` | Abstract `L9`; Intro `L25`; Relevant `L39`; Conclusion `L708-L712` | `L39` |
| O_ISAC_107 | HIT_FALLBACK | `analysis/II_md_inv.csv:L209` | `data/proc_markdowns/O_ISAC_107/O_ISAC_107/O_ISAC_107.md` | Abstract `L9`; Intro `L13`; Relevant `L456`; Conclusion `L460-L466` | `L456` |
| O_ISAC_133 | HIT_FALLBACK | `analysis/II_md_inv.csv:L183` | `data/proc_markdowns/O_ISAC_133/O_ISAC_133/O_ISAC_133.md` | Abstract `L9`; Intro `L13`; Relevant `L35`; Conclusion `L348-L350` | `L35` |

## Path-Resolution Method

- Primary index: `analysis/man_v1/file_index.csv`
- Fallback index: `analysis/II_md_inv.csv`
- Hit summary (used keys): `HIT_PRIMARY=0`, `HIT_FALLBACK=3`, `MISS=0`
- Duplicate-path decision: for `O_ISAC_049`, selected `data/proc_markdowns/O_ISAC_049/O_ISAC_049/O_ISAC_049.md` as canonical to match preflight convention.

## SHA256

- D1 `VIII-F_CONTEXT.md`: `976C281D454AC9803F8E6F14669A2AD7B2F7C1597E86ABEE1F6CF1F77A4BBBB8`
- D2 `VIII-F_CONTEXT_supp.md`: `F143ECEFF5064C75FC02F23F7A75996CAB7D40E57417C1F2FC70B9D79F28F2AE`

## Final

- READY: PASS
