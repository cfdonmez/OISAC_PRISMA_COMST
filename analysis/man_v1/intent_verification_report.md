# PRISMA-COMST Intent Gate Report

## Gate Status
- PASS: Constitution found and explicit for Section VII and Section VIII.
- Gate rule applied: Constitution is hard override; evidence-pack scores are supporting-only.

## Constitution Excerpts (Primary Source of Truth)
Source heading:
- `drafts/section_01_introduction.md` -> `## F. Organization of This Paper` (`drafts/section_01_introduction.md:161`)

Definitive lines:
- Organization lead-in: `drafts/section_01_introduction.md:163`
- Section VII intent: `drafts/section_01_introduction.md:175`
  - `Section VII (Applications and Use Cases)`
- Section VIII intent: `drafts/section_01_introduction.md:177`
  - `Section VIII (Open Challenges and Research Roadmap)`

Constitution decision:
- Section VII = Applications and Use Cases
- Section VIII = Open Challenges and Research Roadmap

## Per-Pack Signals and Soft Scores
Scoring model (supporting only):
- `Score_app = Σ_i w_i * 1{feature indicates applications}`
- `Score_chal = Σ_i w_i * 1{feature indicates challenges/roadmap}`
- weights `w_i ∈ {1,2}`

### Pack: `analysis/VII_ev_v2`
Files read:
- `analysis/VII_ev_v2/axis_definitions.md`
- `analysis/VII_ev_v2/mapping_rules.md`
- `analysis/VII_ev_v2/readiness_report.md`
- `analysis/VII_ev_v2/s7f_app_sum_tbl.csv`
- `analysis/VII_ev_v2/section7F_transfer_map.csv`

Activated application features:
- `+2` Axis explicitly says `Application macro domains` (`analysis/VII_ev_v2/axis_definitions.md:4`)
- `+2` Axis explicitly says `Application metadata ... scenario` (`analysis/VII_ev_v2/axis_definitions.md:5`)
- `+2` Mapping rule uses `study_level.application.application_domain` as primary source (`analysis/VII_ev_v2/mapping_rules.md:3`)
- `+1` Mapping rule states `application narrative coverage` (`analysis/VII_ev_v2/mapping_rules.md:5`)
- `+1` Readiness tracks macro application domains (`analysis/VII_ev_v2/readiness_report.md:34-38`)
- `+1` Summary header is macro-domain application counts (`analysis/VII_ev_v2/s7f_app_sum_tbl.csv:1`)

Activated challenge features:
- none

Scores:
- `Score_app = 9`
- `Score_chal = 0`

Intent from pack signals:
- Applications/Use Cases

### Pack: `analysis/VIII_ev_v1`
Files read:
- `analysis/VIII_ev_v1/axis_definitions.md`
- `analysis/VIII_ev_v1/mapping_rules.md`
- `analysis/VIII_ev_v1/readiness_report.md`
- `analysis/VIII_ev_v1/section8F_research_agenda.csv`
- `analysis/VIII_ev_v1/s8f_pap_chal_map.csv`

Activated challenge/roadmap features:
- `+2` Axis explicitly says `Challenge domains` (`analysis/VIII_ev_v1/axis_definitions.md:4`)
- `+2` Axis includes `deployment_convergence_roadmap` domain (`analysis/VIII_ev_v1/axis_definitions.md:4`)
- `+2` Mapping rule: `Challenge claims are text-anchored first` (`analysis/VIII_ev_v1/mapping_rules.md:3`)
- `+1` Mapping rule: `challenge prioritization` (`analysis/VIII_ev_v1/mapping_rules.md:5`)
- `+1` Mapping rule: `roadmap risks` (`analysis/VIII_ev_v1/mapping_rules.md:7`)
- `+1` Readiness tracks challenge-domain counts (`analysis/VIII_ev_v1/readiness_report.md:33-37`)
- `+1` Agenda header is challenge-domain and priority-oriented (`analysis/VIII_ev_v1/section8F_research_agenda.csv:1`)

Activated application features:
- `+1` Cross-section bridge mentions Section VII applications (`analysis/VIII_ev_v1/axis_definitions.md:5`)
- `+1` Challenge map header contains `has_section7_signal` bridge (`analysis/VIII_ev_v1/s8f_pap_chal_map.csv:1`)

Scores:
- `Score_app = 2`
- `Score_chal = 10`

Intent from pack signals:
- Open Challenges and Research Roadmap

## Final Canonical Mapping (Constitution-Enforced)
- Section VII <-> `analysis/VII_ev_v2`
- Section VIII <-> `analysis/VIII_ev_v1`

## Rename/Move Action
- Required: NO
- Reason: Evidence-pack intent is aligned with constitution labels for Section VII and Section VIII.

## Contradiction Check
- No constitution-vs-pack contradiction detected.
- If a future contradiction appears, constitution wins and pack naming should be marked: `misleading but usable`.
