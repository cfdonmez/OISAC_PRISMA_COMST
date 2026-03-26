# Section VII Merge Quality Report

- Generated: 2026-02-24 11:40:16 UTC
- Scope: D1/D2/D4 QA checks plus integrity checks mandated by merge contract.

## QA Summary
- Placeholders scan: PASS (total hits: 0)
- Cite-key union in `references.bib`: PASS
- ORIS canon scan: PASS
- Bracket-safe math scan: PASS
- VII-G row-reference integrity (#comparison/#examples): PASS

## 1) Placeholder Scan
- `placeholders = 0` confirmed across `section_07_draft.md`, `section_07_supplement.md`, and `merge_map.md`.

## 2) Cite-Key Union vs Bibliography
- D1 bracket-citation key count: 29
- D1 keys: O_ISAC_003, O_ISAC_005, O_ISAC_010, O_ISAC_011, O_ISAC_012, O_ISAC_020, O_ISAC_021, O_ISAC_027, O_ISAC_030, O_ISAC_034, O_ISAC_038, O_ISAC_048, O_ISAC_055, O_ISAC_060, O_ISAC_064, O_ISAC_070, O_ISAC_071, O_ISAC_074, O_ISAC_089, O_ISAC_108, O_ISAC_127, O_ISAC_137, O_ISAC_143, O_ISAC_164, O_ISAC_187, O_ISAC_195, O_ISAC_220, O_ISAC_276, O_ISAC_388
- D2 supplement key token count (`O_ISAC_###`): 29
- D2 keys: O_ISAC_003, O_ISAC_005, O_ISAC_010, O_ISAC_011, O_ISAC_012, O_ISAC_020, O_ISAC_021, O_ISAC_027, O_ISAC_030, O_ISAC_034, O_ISAC_038, O_ISAC_048, O_ISAC_055, O_ISAC_060, O_ISAC_064, O_ISAC_070, O_ISAC_071, O_ISAC_074, O_ISAC_089, O_ISAC_108, O_ISAC_127, O_ISAC_137, O_ISAC_143, O_ISAC_164, O_ISAC_187, O_ISAC_195, O_ISAC_220, O_ISAC_276, O_ISAC_388
- Missing in `data/references.bib` (D1): none
- Missing in `data/references.bib` (D2): none

## 3) ORIS Canon Scan
- Canon check rules: no `OIRS`; no standalone `IRS` token unless explicitly RF-prefixed context.
- Canon term counts in D1: ORIS=28, OPA=25, Conventional=26
- No canon violations detected.

## 4) Bracket-Safe Math Scan
- Total math blocks scanned: 14 (fenced latex + `$$...$$`).
- No square-bracket tokens found inside math blocks.

## 5) VII-G Numeric Row Reference Integrity
- Source VII-G comparison rows: #2, #4, #5, #6
- Merged D1 comparison rows: #2, #4, #5, #6
- Source VII-G examples rows: #12, #16, #4, #9
- Merged D1 examples rows: #12, #16, #4, #9
- Integrity verdict: PASS

## 6) Word Counts and SHA256

| file | words | sha256 |
|---|---:|---|
| `analysis/VII_cr_mrg_v1/section_07_draft.md` | 4930 | `00ca5aba32afc22cfccf48473d737a5498bd5cca2edfd8d3d6b3a2b0a0795f19` |
| `analysis/VII_cr_mrg_v1/section_07_supplement.md` | 1970 | `86a49b73b24bd797df0161396b0e804addacf28be0dc2b77e2d53fa121ea2e59` |
| `analysis/VII_cr_mrg_v1/section_07_quality_report.md` | 274 | `self-referential (compute externally)` |
| `analysis/VII_cr_mrg_v1/merge_map.md` | 133 | `0822d6b181a2d18a46251eed27590317752696b2b9314d6bde93e8bc7226fc79` |
