### VIII-E. Deployment Convergence Roadmap

For VIII-E under `deployment_convergence_roadmap`, evidence suggests that deployment convergence remains a distinct bottleneck beyond standards, hardware, channel modeling, and security, because sensing and communication functions may remain insufficiently co-integrated in practice [O_ISAC_039]. Across the micro-evidence set, four motifs recur: coupling between sensing-positioning and communication-channel-estimation tasks, orchestration and state-fusion stress, staged roll-out and readiness gating, and governance for transferability through compatibility, model validity, and provenance controls [O_ISAC_039; O_ISAC_151; O_ISAC_163; O_ISAC_200].

**Roadmap Case 1: Coupled deployment dependency between sensing and communication tasks.**
When convergence is assumed too early, separate task pipelines may keep bottlenecks at deployment interfaces [O_ISAC_039]. Affected layers include sensing-positioning interfaces, channel-estimation interfaces, and orchestration loops coordinating shared model states in nonstationary contexts [O_ISAC_039]. Source text reports both isolated-design limits and a unified architecture coupling these tasks, suggesting that convergence assumptions require explicit interface-level gating before portability interpretation [O_ISAC_039].

**Roadmap Case 2: Staged roll-out and readiness gating under multi-issue integration pressure.**
If convergence is treated as immediate, deployment planning may understate coordination requirements across multiple design issues, and readiness interpretation can remain unstable across settings [O_ISAC_163]. Affected layers include deployment orchestration, readiness signaling, and governance interfaces mapping application expectations to implementation constraints [O_ISAC_163]. Evidence indicating that practical implementation and eventual roll-out require issues to be addressed together supports symbolic staged roll-out framing [O_ISAC_163].

**Roadmap Case 3: Orchestration and state-fusion fragility in multimodal context loops.**
If orchestration assumptions are fixed before interfaces stabilize, multimodal sensing states and context annotations may drift across update loops under resource stress [O_ISAC_151]. Affected layers include orchestration APIs for multimodal inputs, context metadata interfaces (location/time), encoder update loops, and policy gates for state handoff [O_ISAC_151]. Evidence on multimodal physical quantities, contextual enrichment, and encoder-based semantic representations, together with edge-compute and bandwidth stress statements, suggests that context-bearing fusion contracts require readiness-oriented gating [O_ISAC_151].

**Roadmap Case 4: Open-source governance and transferability risk across heterogeneous stacks.**
If convergence is inferred from isolated implementations, transferability may weaken because infrastructure compatibility conditions and model-validity assumptions can vary across deployments [O_ISAC_200]. Affected layers include reference-stack governance, interoperability with standard DSP pipelines, provenance policy, and audit pathways for deployment claims [O_ISAC_200]. Evidence reports open-source hooks, compatibility pathways, incompatibility risk in some infrastructures, and a realistic time-varying model gap, indicating that governed validation traces remain necessary for portability interpretation [O_ISAC_200].

### VIII-E Math Anchor (Readiness-Gated Deployment Utility)

\[
\begin{aligned}
\max_{u=(u_{\mathrm{arch}},u_{\mathrm{api}},u_{\mathrm{stack}},u_{\mathrm{model}},u_{\mathrm{audit}})} \quad & U_{\mathrm{deploy}}(u) \\
\text{s.t.} \quad & g_{\mathrm{ready}}(u) \ge 0, \\
& \operatorname{compat}_{\mathrm{infra}}(u)=1, \\
& \operatorname{budget}_{\mathrm{edge}}(u) \le B_{\mathrm{edge}},\; \operatorname{budget}_{\mathrm{bw}}(u) \le B_{\mathrm{bw}}, \\
& \operatorname{valid}_{\mathrm{model}}(u)=1,\; \operatorname{prov}_{\mathrm{audit}}(u)=1.
\end{aligned}
\]

Here, `U_deploy` and `g_ready` map to coupling and staged deployment pressure [O_ISAC_039; O_ISAC_163], `u_api` with budget constraints captures context-fusion orchestration stress under edge/bandwidth limitations [O_ISAC_151], and governance constraints map to compatibility, model-validity, and provenance evidence from open-source and model-gap statements [O_ISAC_200]. Symbolic `B_edge` and `B_bw` are retained because no numeric deployment budgets are fixed in the cited excerpts.

### Key Takeaways and Research Priorities

- Deployment evaluation can require minimum interface contracts that bind sensing-positioning and channel-estimation coupling with explicit orchestration handoff checks [O_ISAC_039; O_ISAC_151].
- Roadmap claims can require staged readiness gates rather than immediate convergence assumptions when multi-issue integration pressure is present [O_ISAC_163].
- Governance baselines can require compatibility checks, model-validity checks, and provenance/audit traces before transferability interpretation [O_ISAC_200].
- Open-source reference stacks can support reproducibility, but deployment portability may still depend on explicit validation boundaries [O_ISAC_200].
