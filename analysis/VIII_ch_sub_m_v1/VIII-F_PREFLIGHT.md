# VIII-F Preflight Plan (Capstone Scope Lock)

## Scope Lock

- Section VIII intent check: `Open Challenges and Research Roadmap` (PASS).
- Axis-2 domain list check: A–E domains are explicitly listed; `VIII-F` is not listed as a new Axis-2 domain.
- Declared interpretation: **VIII-F is CAPSTONE synthesis** (cross-domain dependency synthesis + agenda prioritization), not a new challenge domain.

## VIII-F Intent Interpretation (from `section8F_summary.json`)

- Dependency synthesis: supported by cross-domain counts and section-link coverage fields (`linked_section5_papers`, `linked_section6_papers`, `linked_section7_papers`).
- Agenda prioritization: supported by `priority_score` fields in `section8F_research_agenda.csv`.
- Operational interpretation: both dependency synthesis and agenda prioritization are in scope.

## Dependency Coverage Audit

### Covered/Linked A–E Domains

| domain | linked_section5 | linked_section6 | linked_section7 | status |
|---|---:|---:|---:|---|
| A: standardization_interoperability | 55 | 55 | 55 | covered |
| B: hardware_scalability_efficiency | 25 | 25 | 25 | covered |
| C: channel_modeling_evaluation | 54 | 54 | 54 | covered |
| D: security_privacy_reliability | 18 | 18 | 18 | covered |
| E: deployment_convergence_roadmap | 0 | 0 | 0 | isolated |

### Strongest Dependency Edges (Top 5 by coverage)

| rank | dependency_edge | weight |
|---:|---|---:|
| 1 | standardization_interoperability -> Section5 | 55 |
| 2 | standardization_interoperability -> Section6 | 55 |
| 3 | standardization_interoperability -> Section7 | 55 |
| 4 | channel_modeling_evaluation -> Section5 | 54 |
| 5 | channel_modeling_evaluation -> Section6 | 54 |

### Lowest-Coverage / Isolated Domains

- `deployment_convergence_roadmap` (0/0/0 links): isolated.
- `security_privacy_reliability` (18/18/18 links): lowest non-zero coverage.

## Agenda Shortlist (8-12 Items)

- Itemization note: `section8F_research_agenda.csv` provides domain-level priority rows (5); item-level shortlist is expanded using `s8f_pap_chal_map.csv` multi-challenge papers, while preserving domain priority references.

| agenda_id | title | linked_domains(A-E) | linked_challenge_ids | dependency_tags | cite_keys | violations_flag | planned_wording | readiness_fields |
|---|---|---|---|---|---|---|---|---|
| F-AG01 | A-B-C dependency hotspot in wireless FSO pipeline | A,B,C | 8A,8B,8C | S5+S6+S7; multi_challenge=3 | O_ISAC_133 | OK | normal | n_supported_challenges=3; priority_ref=A230/B110/C230 |
| F-AG02 | A-C-D triad for hybrid integration pressure | A,C,D | 8A,8C,8D | S5+S6+S7; multi_challenge=3 | O_ISAC_156 | FLAGGED | conservative | n_supported_challenges=3; priority_ref=A230/C230/D80 |
| F-AG03 | A-B-C convergence under hybrid stack coupling | A,B,C | 8A,8B,8C | S5+S6+S7; multi_challenge=3 | O_ISAC_161 | FLAGGED | conservative | n_supported_challenges=3; priority_ref=A230/B110/C230 |
| F-AG04 | B-C-D capstone dependency balancing | B,C,D | 8B,8C,8D | S5+S6+S7; multi_challenge=3 | O_ISAC_145 | FLAGGED | conservative | n_supported_challenges=3; priority_ref=B110/C230/D80 |
| F-AG05 | A-B-C cross-layer coupling in hybrid medium | A,B,C | 8A,8B,8C | S5+S6+S7; multi_challenge=3 | O_ISAC_142 | FLAGGED | conservative | n_supported_challenges=3; priority_ref=A230/B110/C230 |
| F-AG06 | A-B-C agenda path for wireless VLC deployment chain | A,B,C | 8A,8B,8C | S5+S6+S7; multi_challenge=3 | O_ISAC_049 | OK | normal | n_supported_challenges=3; priority_ref=A230/B110/C230 |
| F-AG07 | A-B-C dependency harmonization with hybrid operations | A,B,C | 8A,8B,8C | S5+S6+S7; multi_challenge=3 | O_ISAC_138 | FLAGGED | conservative | n_supported_challenges=3; priority_ref=A230/B110/C230 |
| F-AG08 | A-B-C integration stress test for hybrid profile | A,B,C | 8A,8B,8C | S5+S6+S7; multi_challenge=3 | O_ISAC_030 | OK | normal | n_supported_challenges=3; priority_ref=A230/B110/C230 |
| F-AG09 | A-B-C cross-domain consolidation with duplicate-path evidence | A,B,C | 8A,8B,8C | S5+S6+S7; multi_challenge=3 | O_ISAC_093 | FLAGGED | conservative | n_supported_challenges=3; priority_ref=A230/B110/C230 |
| F-AG10 | A-B-D governance-sensitive dependency agenda | A,B,D | 8A,8B,8D | S5+S6+S7; multi_challenge=3 | O_ISAC_107 | FLAGGED | conservative | n_supported_challenges=3; priority_ref=A230/B110/D80 |

## Planned Tables for VIII-F

- **Table VIII-F-1: Dependency Coverage Summary**
  - columns: `domain`, `coverage`, `top_dependencies`
- **Table VIII-F-2: Prioritized Research Agenda**
  - columns: `agenda_id`, `dependencies`, `evidence keys`
