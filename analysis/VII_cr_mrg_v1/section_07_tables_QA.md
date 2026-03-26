# Section VII Tables QA

Source inputs used: `analysis/VII_cr_mrg_v1/section_07_draft_comst_polished.md`, `section_07_supplement.md`, `section_07_quality_report.md`.

## Check 1: No New Cite Keys
- Allowed cite-key set size from Section VII draft: 29
- Cite keys used in Table VII-1 and VII-2: 16 (O_ISAC_003, O_ISAC_005, O_ISAC_010, O_ISAC_011, O_ISAC_021, O_ISAC_038, O_ISAC_055, O_ISAC_060, O_ISAC_070, O_ISAC_071, O_ISAC_074, O_ISAC_108, O_ISAC_127, O_ISAC_187, O_ISAC_195, O_ISAC_220)
- Result: PASS
- New keys not in Section VII draft: none
- Every table row has at least one cite key: PASS

## Check 2: Comm-plane vs Sensing-plane Separation (Table VII-1)
- Rule: communication-plane and sensing-plane metrics are kept in separate dedicated columns.
- Result: PASS
- Rows checked: 10

## Check 3: VII-G Row References Present and Preserved (Table VII-2)
- Rule: each row must include both comparison and examples row references.
- Row-ref presence: PASS
- Numeric/value + row-ref exactness vs VII-G text: PASS
