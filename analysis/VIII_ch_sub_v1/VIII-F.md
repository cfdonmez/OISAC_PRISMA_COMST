### VIII-F. Capstone Dependency Synthesis and Prioritized Research Agenda

Section VIII-F acts as a capstone synthesis rather than a new Axis-2 domain: it summarizes cross-domain dependency coverage and then organizes a prioritized agenda linked to those dependencies. Table VIII-F-1 is derived from linkage counts across Sections V-VII and should be read as an observational co-linkage summary, not as a causal graph. Existing IVLCS/ISAC evidence indicates that shared sensing and communication resources can tighten coordination pressure [O_ISAC_049], repeatable calibration routines can remain restrictive when transfer is attempted across settings [O_ISAC_107], and power-limited OWC integration can add bandwidth and noise-management pressure [O_ISAC_133]. Within the current evidence pack, domains A and C appear as the densest linkage hubs, while domain E appears underlinked; VIII-F treats that pattern as a linkage-gap and governance observation, not as a statement of lower importance.

Table VIII-F-1. Dependency Coverage Summary across A-E domains (observational linkage counts).

| domain | linked_section5 | linked_section6 | linked_section7 | status |
|---|---:|---:|---:|---|
| standardization_interoperability | 55 | 55 | 55 | covered |
| channel_modeling_evaluation | 54 | 54 | 54 | covered |
| hardware_scalability_efficiency | 25 | 25 | 25 | covered |
| security_privacy_reliability | 18 | 18 | 18 | covered |
| deployment_convergence_roadmap | 0 | 0 | 0 | isolated |

Table VIII-F-2 converts these observations into an organizational shortlist. The cite-key-supported agenda items remain explicit: F-AG01 aligns interoperability and evaluation baselines under the A/C hotspot [O_ISAC_133], F-AG02 keeps A/B/C resource contention in scope [O_ISAC_049], F-AG03 retains conservative wording for a hybrid security-evaluation thread that may require a unified analytical framework [O_ISAC_156], and F-AG04 retains conservative wording for prototype-to-scale coordination under calibration overhead [O_ISAC_107]. These rows remain tied to their source papers and are not generalized beyond the cited evidence.

The remaining rows preserve artefact-derived agenda slots rather than new literature claims. F-AG05 is carried by the lower but nonzero D coverage signal, F-AG06 explicitly addresses the E-domain linkage gap as a convergence and governance problem, and F-AG07 preserves balanced A-E coverage under limited editorial or research bandwidth. Accordingly, P1, P2, and P3 are organizational labels assigned from observed co-linkage density, summary coverage, and FLAGGED-evidence concentration rather than scientific rankings. The prioritization anchor below is included only as a survey-level editorial scaffold.

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

### VIII-F Math Anchor (Survey-Level Organizational Prioritization Scaffold)

\[
\begin{aligned}
\max_{x \in \{0,1\}^N}\quad & \sum_{i=1}^{N} w_i x_i \\
\text{s.t.}\quad & \sum_{i=1}^{N} c_i x_i \le B,\\
& \mathrm{cover}_d(x) \ge z_d,\quad d \in \{A,B,C,D,E\}_{\mathrm{selected}},\\
& \mathrm{risk\_flag}(x) \le R_{\max}.
\end{aligned}
\]

Here, `x_i` marks whether agenda item `i` is prioritized; `w_i` is an evidence or dependency weight drawn from the VIII-F artefacts; `c_i` is a symbolic editorial or research bandwidth cost; `cover_d` is a domain-coverage indicator; and `risk_flag` limits the concentration of FLAGGED-evidence items. This is a survey-level organizational scaffold, not a validated scientific law and not a claim of deployment certainty.
