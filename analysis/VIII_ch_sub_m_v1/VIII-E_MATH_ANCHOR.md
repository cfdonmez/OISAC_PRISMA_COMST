### VIII-E Math Anchor (Option-1: readiness-gated deployment utility)

\[
\begin{aligned}
\max_{u=(u_{\mathrm{arch}},u_{\mathrm{api}},u_{\mathrm{stack}},u_{\mathrm{model}},u_{\mathrm{audit}})} \quad & U_{\mathrm{deploy}}(u) \\
\text{s.t.} \quad & g_{\mathrm{ready}}(u) \ge 0, \\
& \operatorname{compat}_{\mathrm{infra}}(u)=1, \\
& \operatorname{budget}_{\mathrm{edge}}(u) \le B_{\mathrm{edge}},\; \operatorname{budget}_{\mathrm{bw}}(u) \le B_{\mathrm{bw}}, \\
& \operatorname{valid}_{\mathrm{model}}(u)=1,\; \operatorname{prov}_{\mathrm{audit}}(u)=1.
\end{aligned}
\]

For `deployment_convergence_roadmap`, `U_deploy` and `g_ready` map to coupling and staged deployment pressure: unified sensing-communication architecture is reported, and practical roll-out is described as multi-issue [O_ISAC_039; O_ISAC_163]. The orchestration side is captured by `u_api` with `budget_edge` and `budget_bw`, since multimodal context fusion and location/time-conditioned semantic encoding are reported alongside edge-compute and bandwidth stress [O_ISAC_151]. Governance-side constraints `compat_infra`, `valid_model`, and `prov_audit` follow evidence on infrastructure incompatibility risk, standard-DSP compatibility pathways, open-source implementation hooks, and the stated gap in realistic time-varying channel models [O_ISAC_200].
