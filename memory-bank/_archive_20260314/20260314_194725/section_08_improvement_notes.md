# Section 8 Improvement Notes

Context
- This note is the Section 8 counterpart of the workflow notes used for other sections under `.agent/workflows/`.
- Section 8 is no longer in evidence-building mode. The current state is camera-ready merge complete, with only manuscript-integration and editorial-closeout work remaining.
- Primary working files:
  - `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md`
  - `analysis/VIII_cr_mrg_v1/section_08_supplement.md`
  - `analysis/VIII_cr_mrg_v1/section_08_final_QA.md`
  - `analysis/VIII_cr_mrg_v1/section_08_merge_map.md`
  - `analysis/s08_repo_dec_mtx.md`

Current status
- Final QA status is `READY: PASS`.
- Canonical structure is fixed as `Overview -> VIII-A -> VIII-B -> VIII-C -> VIII-D -> VIII-E -> VIII-F -> VIII-G`.
- `VIII-F` is preserved as capstone dependency-aware synthesis, not a new challenge domain.
- `VIII-G` is preserved as artefact-only cross-section alignment/audit, not a new challenge domain.
- Protocol-surface visibility has already been tightened for `RQ3`, `TQAF`, and `RIS/ORIS/optical phased array` references.
- Intro/manuscript organization text has already been aligned to the current Section 8 contract.
- Legacy outline/reminder copies have been updated to match the current `A..G` structure.
- Manuscript-wide Section VIII reference sweep is complete; active manuscript/review/template files no longer carry stale `Future Directions` or old seven-section organization wording.

Remaining items
1) Editorial standardization pass inside Section 8
   - Issue: Section headings and subheading styles are scientifically acceptable but not fully presentation-uniform.
   - Risk: COMST-level polish remains slightly uneven even though the content is already stable.
   - Fix:
     1. Standardize challenge heading tone across `VIII-A` to `VIII-E`.
     2. Normalize internal subheading style where mixed labels such as `Challenge Cases`, `Math Anchor`, and prose-style transitions coexist.
     3. Preserve all evidence anchors, cite-key unions, tables, and capstone/audit role boundaries.
   - Constraint: This is an editorial-only pass; no substantive restructuring.

2) Final Section 8 QA refresh after manuscript-level edits
   - Issue: Any additional wording cleanup can invalidate hashes or desynchronize QA notes.
   - Risk: Final Section 8 package can be textually correct but QA metadata can lag behind.
   - Fix:
     1. Recompute word count and SHA256 hash for `section_08_camera_ready.md`.
     2. Re-check cite-key union, placeholder count, and `F/G` role integrity.
     3. Refresh `section_08_final_QA.md` only if the text changes.

3) Optional legacy editorial cleanup
   - Issue: Some legacy outline/template files still contain encoding artefacts in unrelated headings such as `Visual Budget` and `Word Budget`.
   - Risk: Not a Section 8 scientific problem, but they reduce repository cleanliness.
   - Fix: Clean those artefacts only if we decide to spend time on repo hygiene after Section 8 freeze.
   - Priority: low

Freeze criteria
- Section 8 can be called fully closed when all of the following hold:
  - manuscript-wide references no longer contradict the current Section 8 contract
  - any editorial polish inside Section 8 is complete
  - final QA, hashes, and counts are refreshed if text changed
  - no active file describes `VIII-F` or `VIII-G` as independent challenge domains

Recommended execution order
1. Apply editorial standardization only where it improves consistency without changing meaning.
2. Refresh final QA if any Section 8 text changed.
3. Mark Section 8 as frozen in the next status summary.
