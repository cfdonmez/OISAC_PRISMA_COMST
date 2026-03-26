# VIII-D CHALLENGES_34_TAKEAWAYS QA

## PASS/FAIL Checklist

| Check | Status | Evidence |
|---|---|---|
| placeholders removed | PASS | `TODO/TBD/PLACEHOLDER/XXX` scan across D1+D2 = 0 |
| Section VIII intent lock | PASS | `analysis/man_v1/section_intent_manifest.yaml` -> `section_VIII_intent: Open Challenges and Research Roadmap` |
| axis label exact (`security_privacy_reliability`) | PASS | `analysis/VIII_ev_v1/axis_definitions.md` Axis-2 line includes exact token |
| prerequisite QA gates | PASS | `VIII-D_PREFLIGHT_QA.md`, `VIII-D_CONTEXT_QA.md`, `VIII-D_CHALLENGES_12_QA.md` each `READY: PASS` |
| cite-key lock | PASS | used keys in D1/D2 = `{O_ISAC_156, O_ISAC_041}`; outside-lock keys = none |
| evidence excerpts present | PASS | D2 has 8 excerpts total (Case 3: 4, Case 4: 4), each with cite-key + locator |
| case evidence minimum | PASS | each new case has >=2 excerpts and includes failure-mode + implication support |
| takeaways discipline | PASS | 4 bullets; each bullet evidence-backed with citations; >=2 bullets connect security/privacy to reliability/fail-safe operations |
| violation-aware phrasing (if applicable) | PASS | `O_ISAC_156` is flagged; overclaim token scan (`prevents|guarantees|eliminates`) = 0; conservative wording retained |
| D1 length in range (260-390) | PASS | word_count = 365 |

## Cite-Key Existence (references.bib)

| cite_key | in_references.bib |
|---|---|
| O_ISAC_156 | YES |
| O_ISAC_041 | YES |

## Contract-Violations Check (used keys)

| paper_id | section | category | severity | reason | evidence | resolution |
|---|---|---|---|---|---|---|
| O_ISAC_156 | 8B | EVIDENCE_WEAK | MINOR | hardware_scalability_efficiency lacks support gate (text anchors) | direct=0; indirect=1 | downgrade applied in D1 wording |
| O_ISAC_041 | - | - | - | no row found | - | none required |

## Processed Markdown Validation Log

| cite_key | resolution | index entry used | opened markdown path | sections opened | excerpt locators |
|---|---|---|---|---|---|
| O_ISAC_156 | HIT_FALLBACK | `analysis/II_md_inv.csv:160` | `C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_156\O_ISAC_156\O_ISAC_156.md` | Abstract `L9`; Intro `L173`; Relevant `I. INTRODUCTION > *A. Motivation* L191`; Conclusion `L1006` | `L27-L27`, `L187-L187`, `L191-L191`, `L1008-L1008` |
| O_ISAC_041 | HIT_FALLBACK | `analysis/II_md_inv.csv:42` (duplicate also at row 274; canonical row 42 selected) | `C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_041\O_ISAC_041.md` | Abstract `L5`; Intro `L19`; Relevant `IV. RESULTS AND ANALYSIS L215`, `*C. Fiber Vibration Pattern Recognition* L363`; Conclusion `L419` | `L23-L23`, `L215-L215`, `L363-L363` |

## Path Resolution Method

- Primary index: `analysis/man_v1/file_index.csv`
- Fallback index: `analysis/II_md_inv.csv`
- Hit summary (used keys): `HIT_PRIMARY=0`, `HIT_FALLBACK=2`, `MISS=0`

## SHA256

- D1 `VIII-D_CHALLENGES_34_TAKEAWAYS.md`: `96958BD78C1420456B699B08650065264C26154EA8F8ECB91C80264B66B70CF5`
- D2 `VIII-D_CHALLENGES_34_TAKEAWAYS_supp.md`: `49B7E7DA49EFFCFBDBA8787DB746EA1DC067E84B2765BE5E3D62D68DA939B02A`

## Final

- READY: PASS
