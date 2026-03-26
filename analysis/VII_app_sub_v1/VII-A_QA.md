VII-A Integration QA

Integration notes:
- Source parts merged: `VII-A_CONTEXT`, `VII-A_SCENARIOS_12`, `VII-A_SCENARIOS_34_TAKEAWAYS`, `VII-A_MATH_ANCHOR`.
- Alignment fix (i) applied: time-domain peak constraint replaced by per-subcarrier cap `0 <= p_k <= P_m` in D1, consistent with `O_ISAC_048` evidence.
- Alignment fix (ii) applied: BER bound treated as a reliability target; `10^-4` is stated as an illustrative reported operating point, not a universal fixed requirement, consistent with `O_ISAC_034`.

Checklist:
- Cite-key integrity check: PASS.
- Placeholders = 0: PASS.
- Intent compliance (Applications and Use Cases framing only): PASS.
- Bracket-safe math (no square-bracket math tokens in D1): PASS.

Cite keys used in D1:
- `O_ISAC_003`: present in `data/references.bib`.
- `O_ISAC_005`: present in `data/references.bib`.
- `O_ISAC_012`: present in `data/references.bib`.
- `O_ISAC_034`: present in `data/references.bib`.
- `O_ISAC_038`: present in `data/references.bib`.
- `O_ISAC_048`: present in `data/references.bib`.
- `O_ISAC_064`: present in `data/references.bib`.
- `O_ISAC_074`: present in `data/references.bib`.
- `O_ISAC_276`: present in `data/references.bib`.

New cite keys introduced beyond micro-parts:
- None.

SHA256:
- D1 `analysis/VII_app_sub_v1/VII-A.md`: `FD4A5A71121FD9645CE329CE106B370573AAF8D642402C5B1DCB5A314CA7FD67`
- D2 `analysis/VII_app_sub_v1/VII-A_supp.md`: `458167DB7B0BA2054C037BD6B0175B6739CD361B8B7CE4B3686DDFA27495B6F5`
