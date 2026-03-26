# Section VIII Repo Decision Matrix

Purpose: consolidate the repo-level contract for Section VIII before any freeze or rewrite decision.

Date: 2026-03-08

## 1. Authority Hierarchy

Use the following source order when conflicts appear:

1. `protocol/prisma_proto.md`
2. `drafts/section_01_introduction.md`
3. `analysis/man_v1/section_intent_manifest.yaml`
4. `analysis/VIII_ev_v1/axis_definitions.md`
5. `analysis/VIII_ev_v1/mapping_rules.md`
6. `analysis/VIII_cr_mrg_v1/section_08_merge_map.md`
7. `analysis/VIII_cr_mrg_v1/section_08_final_QA.md`
8. COMST writing guides and recipes
9. legacy outline/reminder files

Rationale:
- protocol defines the review objective and RQ3 contract;
- introduction + manifest define manuscript constitution;
- Section VIII local evidence pack defines the operational writing rules;
- merge map + QA define what the current camera-ready package actually locked.

## 2. Decision Matrix

| repo expectation | primary repo evidence | current Section VIII coverage | status | decision implication |
|---|---|---|---|---|
| Canonical section intent must be `Open Challenges and Research Roadmap` | `analysis/man_v1/section_intent_manifest.yaml:2`; `drafts/section_01_introduction.md:177`; `analysis/VIII_cr_mrg_v1/section_08_merge_map.md:7` | Final title is `# VIII. Open Challenges and Research Roadmap` in `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md:1` | MATCH | No rename needed. |
| Section VIII must answer protocol RQ3 on gaps, 6G context, and enabling technologies | `protocol/prisma_proto.md:69-72`; `protocol/osf_reg_pack.md:76-80` | Final text covers gaps and limited 6G-facing roadmap framing in `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md:3-5`, `190`, `211`, `299-331`, `336-364` | PARTIAL | Gap/roadmap core is present, but enabling-technology implication is only partially visible. |
| Section VIII must be a dedicated synthesis subsection for gap analysis and architectural implications | `protocol/prisma_proto.md:812-824`; `review_package/COMST_review_bundle_02_rules_methodology.md:900-912` | Final section is a dedicated synthesis layer with `A..E` challenge domains plus capstone `F/G`, but it does not explicitly foreground architectural implications as a named frame | PARTIAL | Structure is valid, but protocol language is only partly surfaced in the prose. |
| PRISMA Item 23 function is to provide a general interpretation of results in context | `protocol/prisma_2020_chk.md:42-43` | Final Section VIII interprets evidence in relation to challenge clusters and upstream Sections V-VII, especially in `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md:338-399` | MATCH | Discussion-role expectation is satisfied. |
| COMST challenge/future section should guide future research, not just list issues | `docs/surv_write_guide.md:68-74`; `review_package/COMST_review_bundle_02_rules_methodology.md:72-78` | Final `VIII-F` provides a prioritized research agenda in `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md:336-377` | MATCH | Section VIII is functioning as a guidance layer, not merely a problem list. |
| Future section should mirror taxonomy/challenge axes | `reference_compendium/COMST_master_rcp.md:31-33` | Final structure mirrors fixed A-E domains in `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md:3`, `7`, `70`, `139`, `214`, `297`; local axis lock in `analysis/VIII_ev_v1/axis_definitions.md:4` | MATCH | Current A-E branching is repo-consistent. |
| Main synthesis must follow a non-list, challenge-driven structure | `docs/surv_write_guide.md:47-54`; `review_package/body_section_templates.md:5-14` | Final subsections are challenge-organized and synthesis-driven across `VIII-A..VIII-E` | MATCH | No structural rewrite toward annotated-bibliography style should be done. |
| Section VIII must keep strict evidence governance: DIRECT first, bridges second | `analysis/VIII_ev_v1/mapping_rules.md:3-8`; `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md:5` | Final overview explicitly states DIRECT/INDIRECT policy in `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md:5` | MATCH | Evidence policy is clearly exposed and should remain locked. |
| Section VIII must preserve continuity with Sections V-VII | `drafts/section_01_introduction.md:177`; `analysis/VIII_ev_v1/axis_definitions.md:5`; `analysis/VIII_cr_mrg_v1/section_08_merge_map.md:14-17` | `VIII-F` and `VIII-G` are explicitly designed as continuity/capstone layers in `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md:338-399` | MATCH | `F/G` are constitutionally justified, not accidental additions. |
| `VIII-F` must remain capstone synthesis, not a new challenge domain | `analysis/VIII_cr_mrg_v1/section_08_final_QA.md:83-86`; `analysis/VIII_ch_sub_v1/VIII-F.md:1-17` | Final text explicitly preserves this in `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md:338-377` | MATCH | `VIII-F` should not be collapsed back into A-E or rewritten as causal theory. |
| `VIII-G` must remain alignment/audit, not paper-level discrepancy narrative | `analysis/VIII_cr_mrg_v1/section_08_final_QA.md:88-90`; `analysis/VIII_ch_sub_v1/VIII-G.md:1-19` | Final text preserves aggregate-only audit logic in `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md:381-409` | MATCH | `VIII-G` is legitimate and should stay aggregate/audit-only. |
| COMST/PRISMA guides expect methodological gaps to be visible | `docs/surv_write_guide.md:72-74`; `review_package/COMST_review_bundle_02_rules_methodology.md:76-78`; `review_package/section_02_methodology.md:90-94` | Methodological gap content is present most strongly in `VIII-C` benchmark/reproducibility framing and in `VIII-G` methodological caution | PARTIAL | Methodological-gap coverage exists, but is unevenly distributed and not named as such at section level. |
| Protocol expects quality-appraisal-aware interpretation | `protocol/prisma_proto.md:810`; `review_package/02_templates_methodology_bundle.md:1073`; `drafts/section_03_methodology.md:76-84` | Final Section VIII has no explicit `TQAF` mention and no overt study-quality weighting language; only indirect caution via `FLAGGED-evidence` appears in `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md:352-377` | PARTIAL | If protocol-tightening is desired, quality-appraisal linkage is the cleanest missing explicit bridge. |
| Guides expect emerging hardware/enabling-tech implications such as RIS/OPA/PIC to remain visible | `protocol/prisma_proto.md:812-824`; `docs/surv_write_guide.md:72-74`; `review_package/COMST_review_bundle_02_rules_methodology.md:900-910` | Final merged section contains `ORIS` mentions in `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md:88-90` and limited 6G baseline language in `190`, `211`, but no explicit whole-word `RIS`, `OPA`, `PIC`, or dedicated enabling-tech implication paragraph | PARTIAL | This is the clearest protocol-to-text tension in the current package. |
| COMST recipe says the section should connect challenges to trade-offs and risks | `reference_compendium/COMST_master_rcp.md:31-33` | Final text does this across A-E and especially via `VIII-F` dependency/priority tables in `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md:338-364` | MATCH | Strong reason to preserve the current dependency-aware design. |
| Legacy outline expected a generic `Challenges & Future Directions` section | `memory-bank/surveyOutline.md:193-214`; `reference_compendium/surv_outline.md:193-214` | Final Section VIII evolved beyond this to `A..E + F + G`, replacing old `Integration with RF-ISAC` with `deployment_convergence_roadmap` | SUPERSEDED | Old outline is historical context only, not a decision source. |
| Deployment roadmap claims must stay cautious because strict support is weak/zero | `.agent/workflows/section_08_improvement_notes.md:20-28`; `analysis/VIII_ev_v1/readiness_report.md:32-39` | Final text keeps deployment convergence symbolic/cautious in `analysis/VIII_cr_mrg_v1/section_08_camera_ready.md:299-331`, and `VIII-G` keeps E as zero/underlinked in `385` and `395` | MATCH WITH RISK | Current wording is careful enough, but this remains a freeze-risk if someone tries to strengthen E claims later. |

## 3. Net Reading of the Repo

### Strongly supported conclusions

- The current `Overview -> A..E -> F -> G` design is repo-legitimate.
- `VIII-F` and `VIII-G` are not accidental overengineering; they are constitutionally supported by the introduction, manifest, local Section VIII evidence rules, merge map, and QA.
- The current section is much closer to the protocol than the old generic `future directions` outline.

### Real tensions that still exist

1. Protocol-level `RIS/OPA architectural implications` are not prominently surfaced in the final merged prose.
2. Quality-appraisal linkage is expected at protocol level, but `TQAF` is not explicitly connected to Section VIII judgments.
3. The section clearly contains methodological gaps, but it does not always announce them with protocol-level wording.

## 4. Decision Options

### Option A: Freeze as-is

Use when the decision criterion is:
- preserve the validated local Section VIII contract;
- avoid destabilizing a passed camera-ready merge;
- accept that protocol themes can be distributed across the manuscript rather than fully restated inside Section VIII.

Pros:
- aligns with current merge map and final QA;
- preserves the strongest part of the current design: evidence-governed challenge synthesis plus capstone audit;
- lowest regression risk.

Cost:
- leaves a mild protocol-surface gap around explicit `RIS/OPA` and `TQAF` visibility.

### Option B: Protocol-tightening micro-revision

Use when the decision criterion is:
- maximize visible alignment between Section VIII text and the protocol/COMST guides.

Safe micro-edits would be limited to:
- one overview sentence linking the section to `RQ3` and quality-weighted interpretation;
- one conservative sentence in `VIII-F` or `VIII-E` surfacing enabling-platform implications for `RIS/OPA` without introducing new unsupported claims;
- no new domain, no new citation set, no change to `F/G` role.

Pros:
- reduces protocol-to-text tension;
- improves defensibility in a reviewer or supervisor discussion about "why this exact Section VIII structure?"

Cost:
- requires a new QA pass because Section VIII is already locally frozen.

## 5. Working Recommendation

Recommended default: `Option B` only if you want protocol-surface tightness.

Reason:
- structurally, the section is already correct;
- the open question is not architecture, but explicit visibility of protocol motifs;
- this can be addressed with a very small polish pass rather than a redesign.

If the priority is stability over perfection, `Option A` is fully defensible from the repo evidence.
