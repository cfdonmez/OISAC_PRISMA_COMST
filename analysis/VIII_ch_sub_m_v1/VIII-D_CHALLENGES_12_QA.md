# VIII-D CHALLENGES_12 QA

## PASS/FAIL Checklist

| Check | Status | Evidence |
|---|---|---|
| placeholders removed | PASS | `TODO/TBD/PLACEHOLDER/XXX` scan across D1+D2 = 0 |
| Section VIII intent lock | PASS | `analysis/man_v1/section_intent_manifest.yaml` -> `section_VIII_intent: Open Challenges and Research Roadmap` |
| axis label exact (`security_privacy_reliability`) | PASS | `analysis/VIII_ev_v1/axis_definitions.md` Axis-2 line contains exact token |
| cite-key lock | PASS | used keys in D1/D2 = `{O_ISAC_145, O_ISAC_039}`; outside-lock keys = none |
| evidence excerpts present | PASS | D2 has 4 excerpts total (Case 1: 2, Case 2: 2), each with cite-key + locator |
| non-trivial statement support | PASS | D1 claim set mapped to D2 excerpts for confidentiality/trust risk and privacy-leakage/update-interface implication |
| violation-aware phrasing | PASS | overclaim token scan (`prevents|guarantees|eliminates`) = 0; downgrade wording applied (`can`, `remain susceptible`, `requires safeguards`) |
| D1 length in range (220-320) | PASS | word_count = 287 |

## Cite-Key Existence (references.bib)

| cite_key | in_references.bib |
|---|---|
| O_ISAC_145 | YES |
| O_ISAC_039 | YES |

## Contract-Violations Check (used keys)

| paper_id | section | category | severity | reason | evidence | resolution |
|---|---|---|---|---|---|---|
| O_ISAC_145 | 8A | EVIDENCE_WEAK | MINOR | standardization_interoperability lacks support gate (text anchors) | direct=0; indirect=0 | downgrade applied in D1 wording |
| O_ISAC_039 | 8A | EVIDENCE_WEAK | MINOR | standardization_interoperability lacks support gate (text anchors) | direct=0; indirect=0 | downgrade applied in D1 wording |
| O_ISAC_039 | 8E | EVIDENCE_WEAK | MINOR | deployment_convergence_roadmap lacks support gate (text anchors) | direct=0; indirect=0 | downgrade applied in D1 wording |

## Processed Markdown Validation Log

| cite_key | resolution | index entry used | opened markdown path | sections opened | excerpt locators |
|---|---|---|---|---|---|
| O_ISAC_145 | HIT_FALLBACK | `analysis/II_md_inv.csv:171` | `C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_145\O_ISAC_145\O_ISAC_145.md` | Intro `L15`; relevant `**1 INTRODUCTION**`; conclusion `L626` | `L23-L23`, `L37-L37` |
| O_ISAC_039 | HIT_FALLBACK | `analysis/II_md_inv.csv:40` (duplicate also at row 276; canonical row 40 selected) | `C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_039\O_ISAC_039.md` | Intro `L9`; relevant Section 4; conclusion `L690` | `L278-L278`, `L324-L324` |

## Path Resolution Method

- Primary index: `analysis/man_v1/file_index.csv`
- Fallback index: `analysis/II_md_inv.csv`
- Hit summary (used keys): `HIT_PRIMARY=0`, `HIT_FALLBACK=2`, `MISS=0`

## SHA256

- D1 `VIII-D_CHALLENGES_12.md`: `B1F789810856272CF4A35E2C37384336DD550CF5A6DB2FE15E7784F82DEEA4D1`
- D2 `VIII-D_CHALLENGES_12_supp.md`: `36778CB24E602BD1ED1DF623676FDD0F59289A2FDE364E3B15B4D1F408E61731`

## Final

- READY: PASS
