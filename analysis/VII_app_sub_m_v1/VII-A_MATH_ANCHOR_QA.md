VII-A MATH_ANCHOR QA

Gate checks:
- G0: PASS (`Section VII intent = Applications and Use Cases`; evidence pack = `analysis/VII_ev_v2/*`).
- G1: PASS (`analysis/man_v1/build_contract.md` and `analysis/man_v1/stylekit_paths.md` applied).
- G2: PASS (`writing_recipes/COMST_master_recipe.md` has no micro math-anchor budget; fallback target `90-140` used).

PASS/FAIL checklist:
- Placeholder markers: PASS (none detected).
- Intent compliance (deployment anchor, no roadmap framing): PASS.
- Bracket-safe math (no square-bracket math tokens): PASS.
- Metric-plane separation (explicit communication plane vs sensing plane): PASS.
- NO ORIS/OPA variables: PASS.
- Word count in target: PASS (`D1_word_count=103`, target `90-140`).

Cite-key integrity (D1):
- `O_ISAC_034`: present in `data/references.bib`.
- `O_ISAC_048`: present in `data/references.bib`.

Path resolution and processed-markdown validation log:
- `analysis/man_v1/file_index.csv`: no per-paper markdown paths for used cite keys (`file_index_per_paper_matches=0`).
- Fallback inventory used: `analysis/II_md_inv.csv`.
- `O_ISAC_048` -> `data/proc_markdowns/O_ISAC_048/O_ISAC_048.md`
  - Opened relevant sections: II. SYSTEM MODEL > A. Communication Subsystem; III. OPTIMAL POWER ALLOCATION FOR DCO-OFDM.
  - Excerpt locators recorded: lines 62-62 (comm metric), 67-67 (average power), 141-141 (peak-power cap).
- `O_ISAC_034` -> `data/proc_markdowns/O_ISAC_034/O_ISAC_034.md`
  - Opened relevant sections: III. THEORETICAL PERFORMANCE METRICS; IV. NUMERICAL RESULTS.
  - Excerpt locators recorded: lines 89-89 (sensing metric scope), 222-222 (BER reliability behavior).

SHA256:
- D1 `analysis/VII_app_sub_v1_micro/VII-A_MATH_ANCHOR.md`: `CE0C6C38CBA0756B5570B7AC71586400AAE10805B416AE8798A14BDEF8CBEFFE`
- D2 `analysis/VII_app_sub_v1_micro/VII-A_MATH_ANCHOR_supp.md`: `284DFD6EB53AA6904CE8BE424124B078068B7745A4392A71B1D6343D4C1A4936`
