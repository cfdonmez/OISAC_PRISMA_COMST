# Evidence-Pack Intent Verdict (Section VII vs Section VIII)

## 1) Constitution excerpt (canonical Section VII and Section VIII)
Source file and heading:
- `drafts/section_01_introduction.md` under `## F. Organization of This Paper` (`drafts/section_01_introduction.md:161-179`)

Definitive statements:
- "The remainder of this survey is organized as follows..." (`drafts/section_01_introduction.md:163`)
- "Section VII (Applications and Use Cases)" (`drafts/section_01_introduction.md:175`)
- "Section VIII (Open Challenges and Research Roadmap)" (`drafts/section_01_introduction.md:177`)

Canonical intent from constitution:
- Section VII = Applications and Use Cases
- Section VIII = Open Challenges and Research Roadmap

## 2) Scoring rubric used (deterministic)
Intent classes:
- CLASS VII: Applications/Use Cases
- CLASS VIII: Open Challenges/Roadmap

Indicator sets (from request):
- I_app terms: application, use case, scenario, deployment, vertical, industry, smart city, ITS, healthcare, manufacturing, localization service, sensing-as-a-service
- I_chal terms: challenge, open problem, limitation, future direction, roadmap, benchmarking, reproducibility, dataset gap, standardization, hardware non-idealities, CSI/feedback overhead

Matching rule used:
- Case-insensitive matching against `axis_definitions.md` text.
- Single-word terms matched as whole words; multi-word/hyphen/slash terms matched as literal phrases.

Scores:
- `Score_app = count(I_app hits) - count(I_chal hits)`
- `Score_chal = count(I_chal hits) - count(I_app hits)`
- Classification thresholds:
  - Applications if `Score_app >= +3`
  - Open Challenges/Roadmap if `Score_chal >= +3`
  - Otherwise `AMBIGUOUS`

## 3) Axis file summary: `analysis/VII_ev_v2/axis_definitions.md`
Evidence (headings/axes):
- Heading: `# Section 7 Axis Definitions (v2)` (`analysis/VII_ev_v2/axis_definitions.md:1`)
- Axis-2: `Application macro domains: smart_infrastructure, indoor_environments, automotive_transportation, underwater_harsh, space_satellite` (`analysis/VII_ev_v2/axis_definitions.md:4`)
- Axis-3: `Application metadata ... scenario ...` (`analysis/VII_ev_v2/axis_definitions.md:5`)
- Governance note for Section VII and Section II metric-plane guardrails (`analysis/VII_ev_v2/axis_definitions.md:7`)

Indicator hits from this axis file:
- I_app hits: `application`, `scenario`
- I_chal hits: none

Score:
- `Score_app = 2 - 0 = +2`
- `Score_chal = 0 - 2 = -2`
- Axis-only classification: `AMBIGUOUS` (threshold not met)

Axis type:
- Domain/vertical axis (application macro domains), not bottleneck-first (`analysis/VII_ev_v2/axis_definitions.md:4-5`)

Secondary disambiguation evidence:
- Primary source is `study_level.application.application_domain` (`analysis/VII_ev_v2/mapping_rules.md:3`)
- Scenario fields are secondary disambiguation (`analysis/VII_ev_v2/mapping_rules.md:4`)
- Application narrative coverage is explicit (`analysis/VII_ev_v2/mapping_rules.md:5`)
- Readiness tracks macro-domain counts (`analysis/VII_ev_v2/readiness_report.md:34-38`)
- Section 7 summary CSV header is application-domain count based (`analysis/VII_ev_v2/s7f_app_sum_tbl.csv:1`)

Resolved intent:
- Applications/Use Cases

## 4) Axis file summary: `analysis/VIII_ev_v1/axis_definitions.md`
Evidence (headings/axes):
- Heading: `# Section 8 Axis Definitions (v1)` (`analysis/VIII_ev_v1/axis_definitions.md:1`)
- Axis-2: `Challenge domains: standardization_interoperability, hardware_scalability_efficiency, channel_modeling_evaluation, security_privacy_reliability, deployment_convergence_roadmap` (`analysis/VIII_ev_v1/axis_definitions.md:4`)
- Axis-3: cross-section links to Section V/VI/VII (`analysis/VIII_ev_v1/axis_definitions.md:5`)
- Governance note for Section VIII and Section II plane/metric alias rules (`analysis/VIII_ev_v1/axis_definitions.md:7`)

Indicator hits from this axis file:
- I_app hits: none
- I_chal hits: `challenge`

Score:
- `Score_app = 0 - 1 = -1`
- `Score_chal = 1 - 0 = +1`
- Axis-only classification: `AMBIGUOUS` (threshold not met)

Axis type:
- Technical bottleneck/challenge axis (challenge-domain taxonomy), not application vertical-first (`analysis/VIII_ev_v1/axis_definitions.md:4`)

Secondary disambiguation evidence:
- Challenge claims are text-anchored first (`analysis/VIII_ev_v1/mapping_rules.md:3`)
- Challenge prioritization and roadmap risk links are explicit (`analysis/VIII_ev_v1/mapping_rules.md:5-7`)
- Readiness reports challenge-domain counts (`analysis/VIII_ev_v1/readiness_report.md:33-37`)
- Research agenda and challenge-map outputs are present (`analysis/VIII_ev_v1/readiness_report.md:6,9`)
- Section 8 agenda CSV header is challenge-domain and priority based (`analysis/VIII_ev_v1/section8F_research_agenda.csv:1`)

Resolved intent:
- Open Challenges and Research Roadmap

## 5) Final verdict
- `analysis/VII_ev_v2/axis_definitions.md` maps to canonical **Section VII (Applications and Use Cases)** after secondary-evidence disambiguation.
- `analysis/VIII_ev_v1/axis_definitions.md` maps to canonical **Section VIII (Open Challenges and Research Roadmap)** after secondary-evidence disambiguation.
- No pack-to-constitution mismatch detected against `drafts/section_01_introduction.md:175,177`.

Contingency strategy if a future mismatch appears:
- Option A: Rename/move evidence-pack folders and output artifacts to match constitution section numbering.
- Option B: Update constitution section mapping text to match stabilized evidence-pack intent.

## 6) Risk note for upcoming drafting (citation/notation constraints)
- Citation pattern is square-bracket key style in draft prose (e.g., `[O_ISAC_...]`) (`drafts/section_04_taxonomy.md:11,28`; `drafts/section_01_introduction.md:5`).
- Bib-key generation script writes to `data/references.bib` and normalizes keys to `O_ISAC_xxx` (`scripts/generate_bibtex.py:9,98,125`).
- Section II notation guardrails are explicitly required in both packs:
  - Section VII pack: metric-plane guardrails and SNR/OSNR plane-separation wording (`analysis/VII_ev_v2/axis_definitions.md:7`; `analysis/VII_ev_v2/mapping_rules.md:8`)
  - Section VIII pack: metric alias and SNR/OSNR plane-separation wording (`analysis/VIII_ev_v1/axis_definitions.md:7`; `analysis/VIII_ev_v1/mapping_rules.md:8`)
