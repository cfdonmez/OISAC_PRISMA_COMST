# Phase E — Deterministic TQAF

Status: final analytical artifact set, QA PASS 43/43.

The historical `DRAFT` suffixes are retained in several generated filenames for lineage; their contents are the locked 2026-08-04 Phase-E outputs. In this public package, host-specific path strings were removed from the builder and QA metadata without changing scores, counts, source hashes, or scientific fields.

Key results: 206 study rows, 1,854 dimension-audit rows, 7,951 normalization-audit rows, 92 explicit legacy-missingness resolutions, and 115 S1–S7 evidence bodies. Overall contribution is 6 low, 75 adequate, and 125 strong. Evidence-body certainty is 54 high, 47 moderate, 10 limited, and 4 unclear/non-substantive fallback bodies.

The frozen crosswalk retains predecessor-workbook metadata for lineage. `PHASE_E_FINAL_WORKBOOK_INVARIANCE_AUDIT_2026-08-04.{json,md}` independently re-imports the authoritative final workbook and proves invariance: 206 studies, 46 check families, 9,476 comparisons, 0 mismatches and 0 failed studies.

The builder reads the workbook supplied through `OISAC_PHASE_D_WORKBOOK` and verifies its locked SHA-256, `c1b3b89789c6ed3e20da5a6283e480875c1913e21af88ff59ac747a6aa949348`.

Provenance boundary: `independent_human_status = not_documented`.
