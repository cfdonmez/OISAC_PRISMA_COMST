# Discovery Report (v1)

Generated: 2026-02-19
Mode: discovery-only

## PASS/FAIL checklist

- [PASS] Found canonical organization paragraph(s).
  - Evidence: `drafts/section_01_introduction.md:161-179`.

- [PASS] Identified Section VII and Section VIII canonical intent.
  - Evidence: `drafts/section_01_introduction.md:175-177`, `analysis/VII_ev_v2/axis_definitions.md:4`, `analysis/VIII_ev_v1/axis_definitions.md:4-5`.

- [PASS] Identified stylekit assets (explicit stylekit exists).
  - Evidence: `writing_recipes/COMST_master_recipe.md:10-63`, `docs/surv_write_guide.md:9-75`, `memory-bank/master_writing_guide.md:302-337`.

- [PASS] Identified bibliography source-of-truth and citation format (with conflict flags).
  - Evidence: `scripts/generate_bibtex.py:9,69,125`, `data/references.bib:8`, `data/references.bib:1354-1356`, `analysis/README.md:28`, `drafts/section_01_introduction.md:5`, `drafts/section_01_introduction.md:238-266`.

- [PASS] Identified numbering policy (mixed, requires normalization before final compile).
  - Evidence: `drafts/section_01_introduction.md:26,52`, `drafts/section6_20260217_143141/section_06_camera_ready.md:7,109`.

## Contradiction summary

1. Organization-map contradiction between current manuscript intro and legacy style templates.
   - Current constitution: `drafts/section_01_introduction.md:163-179`.
   - Legacy templates: `memory-bank/master_writing_guide.md:138-140`, `memory-bank/introduction_templates.md:38-40`.
2. Bibliography source conflict between docs and scripts.
   - Doc claim: `analysis/README.md:28`.
   - Operational write target: `scripts/generate_bibtex.py:9,69`.
3. Citation and numbering conventions are mixed (project-key citations + numeric references; Roman tables + section-prefixed tables).
   - Citation evidence: `drafts/section_01_introduction.md:5`, `drafts/section_01_introduction.md:238-266`, `drafts/section6_20260217_143141/section_06_camera_ready.md:162`.
   - Numbering evidence: `drafts/section_01_introduction.md:26,52`, `drafts/section6_20260217_143141/section_06_camera_ready.md:7,109`.

## SHA256 hashes

Note on D4 self-hash: exact raw-file self-hash cannot be embedded without mutating file bytes. The D4 hash below is from the pre-injection snapshot used to generate this report.

### Manifest artifacts

- `analysis/man_v1/section_map.md`: `ca0a881db331855dd15c1a9c9309dd17017e3ac820421e94a2dcfc5b7c2b441e`
- `analysis/man_v1/stylekit_paths.md`: `b9423e8293788d3acc6cff02261cd77a80e3940e9cec351d199540f7430fd958`
- `analysis/man_v1/build_contract.md`: `4d953efcbb2e531b76adf0f11683f77bb8828e98dc1c80b1137f22d97479e4bc`
- `analysis/man_v1/discovery_report.md` (pre-injection snapshot): `fb31e79e111c82e1e48dcc6d9b0e272cc8402bbc97edef86a548dc1894706dd0`
- `analysis/man_v1/file_index.csv`: `d403538aff46f7dfa221318e38bd17a9848c2565b36e820656b0f2ece2c55fc4`

### Key source files relied on

- `drafts/section_01_introduction.md`: `0867e6b91db6bb63352867067c7a27749e5da5ffe08e384d88b568ca676df75f`
- `drafts/section_02_fundamentals_draft.md`: `3aa3413f215e6aa06ec1501a2b6f58bc01050fb0df0f6d254c7da8658b4c1816`
- `drafts/section_03_methodology.md`: `3b2db65a1c6c3be0de4cae7d6a2ac98537c9b9711df2ec9c1aa585e25ef6e7b5`
- `drafts/section_04_taxonomy.md`: `d39e3a451fa8993de47a62f493d30bc0a9bf4255a2d0729c29c6b25ae1d62d30`
- `drafts/section_05_template.md`: `9c789ebc92d50ef8163fd62d672218b960a5980450c324a7222ac369e7027830`
- `drafts/section_06_draft.md`: `57acd79a782071782abf31339246f57675489dd212686283cf17b8978f6b9a3b`
- `drafts/section6_20260217_143141/section_06_camera_ready.md`: `8c28c215b0cee2854a41b04849140cacf20862babc80f86e4cb5ad48189e430b`
- `writing_recipes/COMST_master_recipe.md`: `38a337467b61a62143f40094296c64b6fdd832f2e2e44a9fcd78871c962dccff`
- `docs/surv_write_guide.md`: `227d0694bed60b38052de1744b03fb100abb23da316a9f3da45d4e88096f04c3`
- `memory-bank/master_writing_guide.md`: `28e7e0a5adf656f18a492f30adc8dc7f2dcc712e6be1b159a36000eff5bd2ff9`
- `memory-bank/introduction_templates.md`: `619902145a07abab7abbc43f190259796d38232e106929fde196c21db77dfc8a`
- `memory-bank/body_section_templates.md`: `09f3d143609fffdf7f2b2fd1bbc724544bd832875cf4a22fae98ddb18f8060f1`
- `scripts/generate_bibtex.py`: `f96bc03fb3fb44459ab4ecb7c475b565ec09ecea901aeb1b3af7b5389aabaa6a`
- `analysis/README.md`: `8f3463f40cb936268b7f5e03b95ad9c65f9ffaec29bf362183edd6052c89f279`
- `data/references.bib`: `12976873c25386011f9988ed2070999b6c38a2429243e9bd2d06919ca645e06f`
- `analysis/refs.bib`: `973907ccdfd37b6f40d34a9448c273356309261c96039921430de1392717b6a3`
- `manuscript/comst_template.tex`: `c97902dbad90cb9c30842db4c1446529fa2fc8f6d12d96a15491a860417565f0`
- `analysis/VII_ev_v2/axis_definitions.md`: `c58ae1e9b9967e39668c7e48742a3b49dcd8b5bcb16de89ae8b2a04d8b4e1e93`
- `analysis/VIII_ev_v1/axis_definitions.md`: `f377fd8dd127d64aaad8104b94e1a92e0e43275aa43a32610455d5b8fd915d10`


