VIII-F operates as a capstone synthesis layer: it turns the domain-wise open issues in `section8F_research_agenda.csv` into a dependency-aware shortlist by reading `s8f_dep_cov.csv` as observational coverage rather than causality. In the current pack, `standardization_interoperability` and `channel_modeling_evaluation` are the densest hubs at 55/55/55 and 54/54/54 links across Sections V-VII, so agenda items touching A and C are treated as interface-heavy priorities. `hardware_scalability_efficiency` and `security_privacy_reliability` remain relevant bridge domains at 25/25/25 and 18/18/18. `deployment_convergence_roadmap` is underlinked at 0/0/0, so VIII-F treats E as a linkage-gap and governance problem that still needs an explicit agenda slot, not as a low-importance domain.

Under limited editorial or research bandwidth, the shortlist is organized by combining those coverage signals with multi-challenge mappings in `s8f_pap_chal_map.csv`, domain `priority_score` rows in `section8F_research_agenda.csv`, and the caution flags in `contract_violations.csv`. P1 is used for items that couple the A/C hubs or pair hub pressure with multi-challenge evidence. P2 is used for bridge items that pull B, D, and the E linkage gap into the roadmap without over-concentrating on any single thread. P3 is reserved for balancing items that preserve cross-domain coverage under a bounded selection budget. The math anchor below is framed as a survey-level organizational model rather than a system law.

Table VIII-F-2. Prioritized Research Agenda (dependency-aware, evidence-linked, non-causal synthesis).

| agenda_id | title | linked_domains | dependency_tags | evidence_keys | priority_tier | wording_mode |
|---|---|---|---|---|---|---|
| F-AG01 | Align interoperability rules with evaluation baselines | A,C | A55-C54 hub; S5/S6/S7 dense | O_ISAC_133; map:O_ISAC_133; depcov:A,C | P1 | normal |
| F-AG02 | Reduce multi-slot resource contention in optical ISAC | A,B,C | ABC multi-challenge; resource coupling | O_ISAC_049; map:O_ISAC_049; depcov:A,B,C | P1 | normal |
| F-AG03 | Hybrid stacks may require a unified security-evaluation framework | A,C,D | ACD triad; cross-layer security | O_ISAC_156; map:O_ISAC_156; depcov:A,C,D | P1 | conservative |
| F-AG04 | Prototype calibration may require hardware-scaling coordination | A,B,D | ABD triad; prototype-to-scale | O_ISAC_107; map:O_ISAC_107; depcov:A,B,D | P2 | conservative |
| F-AG05 | Keep low-coverage security threads in scope | D | D18 bridge; coverage guardrail | agenda:D; depcov:D | P2 | normal |
| F-AG06 | Bridge E isolation through convergence/governance hooks | A,C,E | E0 linkage gap; governance bridge | agenda:E; depcov:E; summary:n_deployment_convergence_roadmap_papers | P2 | normal |
| F-AG07 | Maintain balanced A-E coverage under fixed bandwidth | A,B,C,D,E | coverage floor; flagged-risk cap | summary_table:all; violations:used_keys | P3 | normal |

Survey-level organizational prioritization scaffold:

$$
\begin{aligned}
\max_{x \in \{0,1\}^N}\quad & \sum_{i=1}^{N} w_i x_i \\
\text{s.t.}\quad & \sum_{i=1}^{N} c_i x_i \le B,\\
& \mathrm{cover}_d(x) \ge z_d,\quad d \in \{A,B,C,D,E\}_{\mathrm{selected}},\\
& \mathrm{risk\_flag}(x) \le R_{\max}.
\end{aligned}
$$

Here, `x_i` marks whether agenda item `i` is selected; `w_i` is an evidence/dependency weight from the VIII-F artefacts; `c_i` is symbolic editorial or research bandwidth cost; `cover_d` is a domain-coverage indicator; and `risk_flag` limits the concentration of FLAGGED-evidence items. This is a survey-level editorial scaffold, not a validated system law or deployment guarantee.
