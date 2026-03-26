VII-A SCENARIOS_34_TAKEAWAYS QA

Gate checks:
- G0: PASS (`Section VII intent = Applications and Use Cases`; evidence pack = `analysis/VII_ev_v2/*`).
- G1: PASS (`analysis/man_v1/build_contract.md` and `analysis/man_v1/stylekit_paths.md` applied).
- G2: PASS (`writing_recipes/COMST_master_recipe.md` has no VII-A micro budget; fallback target `230-320` used).

PASS/FAIL checklist:
- Placeholder markers: PASS.
- Intent compliance (applications/deployment framing only): PASS.
- Metric-plane separation (explicit sensing plane vs communication plane clauses): PASS.
- Dominant-component evidence lock: PASS.
  - Both scenarios labeled `Conventional (no ORIS/OPA explicitly evidenced)`.
  - Explicit term check in processed markdown (`OPA`/`ORIS`/`OIRS`) found no matches for `O_ISAC_012`, `O_ISAC_034`, `O_ISAC_064`, `O_ISAC_276`.
- Vertical-scope alignment: PASS.
- Excerpt-claim semantic match: PASS.
- Word count: PASS (`D1_word_count=320`, target `230-320`).

Cite-key integrity (D1):
- `O_ISAC_012`: present in `data/references.bib`.
- `O_ISAC_034`: present in `data/references.bib`.
- `O_ISAC_064`: present in `data/references.bib`.
- `O_ISAC_276`: present in `data/references.bib`.

Path resolution and validation log:
- `analysis/man_v1/file_index.csv`: no per-paper markdown entries for used keys (`file_index_per_paper_matches=0`).
- Fallback inventory used: `analysis/II_md_inv.csv`.
- `O_ISAC_012` -> `data/proc_markdowns/O_ISAC_012/O_ISAC_012.md`
  - Opened: Abstract (line 11), I. INTRODUCTION (line 15), III. SIMULATION AND RESULT (line 101), IV. CONCLUSION (line 117).
  - Excerpt locator recorded: Abstract, lines 11-11 (Core Claim S4).
- `O_ISAC_034` -> `data/proc_markdowns/O_ISAC_034/O_ISAC_034.md`
  - Opened: Abstract (line 5), I. INTRODUCTION (line 9), IV. NUMERICAL RESULTS (line 179), V. CONCLUSION (line 226).
  - Excerpt locator recorded: IV. NUMERICAL RESULTS, lines 222-222 (Takeaway support).
- `O_ISAC_064` -> `data/proc_markdowns/O_ISAC_064/O_ISAC_064.md`
  - Opened: Abstract (line 9), 1. Introduction (line 11), relevant urban deployment paragraph (line 13), no explicit conclusion heading.
  - Excerpt locator recorded: Abstract, lines 9-9 (Takeaway support).
- `O_ISAC_276` -> `data/proc_markdowns/O_ISAC_276/O_ISAC_276.md`
  - Opened: Abstract (line 5), I. INTRODUCTION (line 9), IV. TEST IN LIVE XGS-PON (line 121), V. SUMMARY (line 147).
  - Excerpt locators recorded: IV. TEST IN LIVE XGS-PON, lines 143-143 (Core Claim S3) and 145-145 (Takeaway support).

Vertical scope evidence (axis definition used):
- Source: `analysis/VII_ev_v2/axis_definitions.md` (Axis-2).
- Evidence quote: `Axis-2 Application macro domains: smart_infrastructure, indoor_environments, automotive_transportation, underwater_harsh, space_satellite.`
- Alignment rationale: both scenarios are selected from `smart_infrastructure`-tagged `7A` evidence rows and explicitly anchored to metropolitan or outdoor vectors (`O_ISAC_064`, `O_ISAC_012`, `O_ISAC_034`, `O_ISAC_276`).

Excerpt-claim match audit:
- Core Claim S3 in D1 is directly supported by Supplement Excerpt 1 (`O_ISAC_276`, line 143: direct 4.5 dB -> 4.55 dB readout).
- Core Claim S4 in D1 is directly supported by Supplement Excerpt 2 (`O_ISAC_012`, line 11: no mutual interference statement).

SHA256:
- D1 `analysis/VII_app_sub_v1_micro/VII-A_SCENARIOS_34_TAKEAWAYS.md`: `B9324C1CBE4008A11B435898E4C0A4B705D39B9651855C2BEBDF11CCF7637148`
- D2 `analysis/VII_app_sub_v1_micro/VII-A_SCENARIOS_34_TAKEAWAYS_supp.md`: `635BA9AF6E18E7384C52B76B74676DFFF3A3DEE402D7D6A35E687EF5E150E0E3`
