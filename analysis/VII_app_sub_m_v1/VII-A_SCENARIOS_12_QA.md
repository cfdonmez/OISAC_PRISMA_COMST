VII-A SCENARIOS_12 QA

Path-resolution note:
- `analysis/man_v1/file_index.csv` contains no per-paper entries for `O_ISAC_003`, `O_ISAC_005`, `O_ISAC_038`, `O_ISAC_074` (`file_index_matches=0`).
- Fallback inventory used: `analysis/II_md_inv.csv`.
- Resolved markdown paths from fallback inventory:
  - `data/proc_markdowns/O_ISAC_003/O_ISAC_003.md`
  - `data/proc_markdowns/O_ISAC_005/O_ISAC_005.md`
  - `data/proc_markdowns/O_ISAC_038/O_ISAC_038.md`
  - `data/proc_markdowns/O_ISAC_074/O_ISAC_074.md`

PASS/FAIL checklist:
- Placeholder markers: PASS (no unresolved placeholder tags detected).
- Intent compliance (applications/deployment only; no roadmap framing): PASS.
- Metric-plane separation (sensing vs communication clauses separated): PASS.
- Dominant-component evidence lock: PASS.
  - Both scenarios are labeled `Conventional (no ORIS/OPA explicitly evidenced)`.
  - Processed markdown check for explicit `OPA`/`ORIS`/`OIRS` returned no matches for all used keys.
- Word count in target: PASS (`274` words in D1; target `220-280`).

Cite-key integrity (D1):
- `O_ISAC_003`: present in `data/references.bib`.
- `O_ISAC_005`: present in `data/references.bib`.
- `O_ISAC_038`: present in `data/references.bib`.
- `O_ISAC_074`: present in `data/references.bib`.

Processed-markdown validation log:
- `O_ISAC_003` -> `data/proc_markdowns/O_ISAC_003/O_ISAC_003.md`
  - Opened sections: Abstract (line 5), I. INTRODUCTION (line 9), III. VL-BASED ISAC CHANNEL CHARACTERIZATION (line 63), IV. CONCLUSIONS (line 155).
  - Excerpt locator recorded: Abstract, lines 5-5.
- `O_ISAC_005` -> `data/proc_markdowns/O_ISAC_005/O_ISAC_005.md`
  - Opened sections: Abstract (line 5), I. INTRODUCTION (line 9), IV. RESULTS AND SYSTEM PERFORMANCE (line 191), V. CONCLUSION (line 213).
  - Excerpt locator recorded: Abstract, lines 5-5.
- `O_ISAC_038` -> `data/proc_markdowns/O_ISAC_038/O_ISAC_038.md`
  - Opened sections: Abstract (line 7), 1. Introduction (line 9), 4. Results and Discussions (line 54), 5. Conclusion (line 58).
  - Excerpt locator recorded: Abstract, lines 7-7.
- `O_ISAC_074` -> `data/proc_markdowns/O_ISAC_074/O_ISAC_074.md`
  - Opened sections: Abstract (line 11), I. INTRODUCTION (line 15), III. EXPERIMENTAL RESULTS (line 38), IV. CONCLUSIONS (line 52).
  - Excerpt locator recorded: Abstract, lines 11-11.

SHA256:
- D1 `analysis/VII_app_sub_v1_micro/VII-A_SCENARIOS_12.md`: `0DB77D7A73072C0C2362AE95E7EABDF6F28D86A9C51334582D7818C090C7648F`
- D2 `analysis/VII_app_sub_v1_micro/VII-A_SCENARIOS_12_supp.md`: `B282A0DB1EFCB534E849B98868BB8305F2C05CB03252C8ED143EE29190A78B7C`
