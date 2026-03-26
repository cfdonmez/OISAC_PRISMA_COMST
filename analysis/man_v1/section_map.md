# Section Map Manifest (v1)

Generated: 2026-02-19
Scope: discovery-only (no drafting/rewrite actions).

## Canonical Section Map (paper constitution)

| section_id | canonical title/purpose | source evidence | current implementation file(s) |
|---|---|---|---|
| I | Introduction: motivation, gaps, contributions, organization map, notation primer. | `drafts/section_01_introduction.md:1`, `drafts/section_01_introduction.md:145-185` | `drafts/section_01_introduction.md`, `review_package/section_01_introduction.md` |
| II | Technical fundamentals of optical sensing/communication. | `drafts/section_01_introduction.md:165`, `drafts/section_02_fundamentals_draft.md:1` | `drafts/section_02_fundamentals_draft.md` |
| III | PRISMA methodology and study-selection protocol. | `drafts/section_01_introduction.md:167`, `drafts/section_03_methodology.md:1-4` | `drafts/section_03_methodology.md` |
| IV | Unified O-ISAC taxonomy. | `drafts/section_01_introduction.md:169`, `drafts/section_04_taxonomy.md:1-3` | `drafts/section_04_taxonomy.md` |
| V | Performance trade-off synthesis. | `drafts/section_01_introduction.md:171`, `drafts/section_05_template.md:1` | `drafts/section_05_template.md` |
| VI | Enabling technologies (ORIS/OPA/ML/etc.). | `drafts/section_01_introduction.md:173`, `drafts/section6_20260217_143141/section_06_camera_ready.md:1-3` | `drafts/section_06_draft.md`, `drafts/section6_20260217_143141/section_06_camera_ready.md` |
| VII | Applications and use cases across domains. | `drafts/section_01_introduction.md:175`, `analysis/VII_ev_v2/axis_definitions.md:1-5`, `analysis/VII_ev_v2/mapping_rules.md:1-4` | `analysis/VII_ev_v2/s7f_app_sum_tbl.csv`, `analysis/VII_ev_v2/section7F_transfer_map.csv`, `analysis/nb/Section7_Applications_Evidence_Lab.ipynb` |
| VIII | Open challenges and research roadmap. | `drafts/section_01_introduction.md:177`, `analysis/VIII_ev_v1/axis_definitions.md:1-5`, `analysis/VIII_ev_v1/mapping_rules.md:1-7` | `analysis/VIII_ev_v1/section8F_research_agenda.csv`, `analysis/VIII_ev_v1/section8G_cross_section_report.md`, `analysis/nb/Section8_OpenChallenges_Roadmap_Evidence_Lab.ipynb` |
| IX | Conclusion section. | `drafts/section_01_introduction.md:179`, `memory-bank/fileMap.md:83-90` | Conclusion intent declared; section-level draft file is not yet materialized in the active draft bundle. |

## Section VII vs Section VIII: canonical intent

- Section VII is explicitly application-centric (smart infrastructure, transportation, healthcare, industrial IoT): `drafts/section_01_introduction.md:175`.
- Section VIII is explicitly challenge/roadmap-centric: `drafts/section_01_introduction.md:177`.
- The evidence packs are semantically aligned with this split:
  - VII pack axis defines macro application domains: `analysis/VII_ev_v2/axis_definitions.md:4`.
  - VIII pack axis defines challenge domains and cross-links from Section VII: `analysis/VIII_ev_v1/axis_definitions.md:4-5`.

## Contradictions Block

### A) Canonical org vs legacy style templates

- Current manuscript organization uses Sections II-IX with Section IX as conclusion: `drafts/section_01_introduction.md:163-179`.
- Legacy writing templates still state "Section VII concludes the paper":
  - `memory-bank/master_writing_guide.md:138-140`
  - `memory-bank/introduction_templates.md:38-40`
- Impact: style assets are partially stale relative to current manuscript constitution.

Resolution options (discovery only, not applied):
1. Option A (recommended): update legacy templates to the 9-section map (II-IX) now used by the manuscript intro and VII/VIII evidence packs.
2. Option B: revert manuscript organization back to the 7-section legacy template.

### B) Evidence-pack naming vs canonical VII/VIII intent

- No mismatch detected. Section VII evidence assets are application-oriented and Section VIII evidence assets are challenge/roadmap-oriented (`analysis/VII_ev_v2/axis_definitions.md:4`, `analysis/VIII_ev_v1/axis_definitions.md:4-5`).
