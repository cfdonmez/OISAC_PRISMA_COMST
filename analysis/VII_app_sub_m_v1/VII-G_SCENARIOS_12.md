### Scenario 1
1. **Case title (macro domain tag):** Automotive raw-only expansion case (`automotive_transportation`).
2. **View-1 definition (structured tags):** Study-level structured tagging uses `study_flag_count` as the baseline domain assignment count for this macro domain.
3. **View-2 definition (extracted evidence rows):** Evidence-row extraction reports both `raw_evidence_count` and `strict_evidence_count` after applying raw and strict support gates.
4. **Numeric discrepancy statement:** For automotive, `flag_count=76`, `raw_count=213`, `strict_count=104`; deltas are `raw_only_vs_flag=137` and `strict_only_vs_flag=28` (comparison row #4).
5. **Representative example note:** The raw-only automotive exemplar pool explicitly includes `O_ISAC_010` (examples row #9), which is typical of deployment-driven evidence appearing beyond structured study tags.
6. **Interpretation:** This divergence is consistent with extraction surfacing application mentions across sections that are not always mirrored in study-level tagging fields. The strict gate narrows that gap but does not remove it, indicating partial but not full alignment.
7. **Representative works:** `O_ISAC_010`.

### Scenario 2
1. **Case title (macro domain tag):** Smart-infrastructure strict-only surplus case (`smart_infrastructure`).
2. **View-1 definition (structured tags):** Study-level structured tagging again defines the baseline via `study_flag_count` under the smart-infrastructure label.
3. **View-2 definition (extracted evidence rows):** Extracted evidence provides both raw and strict counts, where strict retains rows meeting tighter support criteria.
4. **Numeric discrepancy statement:** For smart infrastructure, `flag_count=103`, `raw_count=221`, `strict_count=204`; deltas are `raw_only_vs_flag=118` and `strict_only_vs_flag=101` (comparison row #2).
5. **Representative example note:** The strict-only smart-infrastructure exemplar list contains `O_ISAC_071` (examples row #4), making it a representative strict-surplus instance in this dual-view setting.
6. **Interpretation:** The persistence of a large strict-only delta suggests that many extracted rows remain support-qualified even under stricter gating. This pattern indicates a systematic coverage difference between structured tagging and evidence-row accounting.
7. **Representative works:** `O_ISAC_071`.
