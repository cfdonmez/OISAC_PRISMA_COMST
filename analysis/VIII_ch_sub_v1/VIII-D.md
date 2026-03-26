## VIII-D security_privacy_reliability

### Context

For VIII-D under security_privacy_reliability, evidence indicates that O-ISAC links couple security, privacy, and reliability because sensing increases observability while communication paths keep exploitable attack surfaces [O_ISAC_145][O_ISAC_039]. Physical-layer threat exposure remains a core motif: wireless transmissions can be susceptible to eavesdropping, so robust protection assumptions should be treated as conditional rather than guaranteed [O_ISAC_145]. A second motif is privacy leakage via sensing-enabled learning pipelines, where confidential user information can be involved and requires controlled data-handling practices [O_ISAC_039]. A third motif concerns authentication/trust posture, which remains tied to physical-layer security mechanisms and legitimacy checks in hybrid deployments [O_ISAC_145]. A fourth motif is fail-safe integrity monitoring, where transport-network ISAC evidence reports real-time warning pathways that can reduce service-interruption risk under disruptive vibration events [O_ISAC_041]. Together, these motifs frame VIII-D as a coupled risk-governance challenge, not a single-metric security problem.

### Challenge Cases 1-2

#### Challenge Case 1 - Physical-Layer Confidentiality and Trust Exposure in Hybrid Links

1) **Challenge title.** Physical-layer confidentiality and trust exposure in hybrid RF-OWC security operation.

2) **Failure mode.** Evidence indicates that wireless links can remain susceptible to eavesdropping, and trust in received sensing/communication outputs can degrade when adversaries manipulate observations [O_ISAC_145].

3) **Affected interfaces/layers.** The affected interfaces include physical-layer signal confidentiality, jammer-aware channel behavior, and trust interpretation in edge decision loops that consume sensing-assisted communication outputs [O_ISAC_145].

4) **Evidence snippet summary.** Representative text states that wireless transmissions are susceptible to eavesdropping and require robust security treatment [O_ISAC_145]. Additional text reports attacker-side falsification risk that can undermine output trustworthiness in hybrid sensing/communication contexts [O_ISAC_145].

5) **Practical implication for roadmap.** The VIII-D roadmap should treat confidentiality-integrity checks as a coupled risk surface that requires safeguards before cross-scenario security claims [O_ISAC_145].

#### Challenge Case 2 - Privacy Leakage Pressure in Multi-User Sensing-Learning Pipelines

1) **Challenge title.** Privacy leakage pressure in federated multi-user sensing-learning pipelines.

2) **Failure mode.** Evidence indicates that distributed VIPAC training can involve sensitive location/trajectory information, so privacy exposure can increase if update exchange and aggregation boundaries are weakly specified [O_ISAC_039].

3) **Affected interfaces/layers.** The affected layers include metadata/privacy governance at user agents, model-update interfaces between agents and server, and orchestration policies that separate local datasets from shared parameters [O_ISAC_039].

4) **Evidence snippet summary.** Representative text reports explicit privacy-preservation intent in federated training and highlights confidential data-leakage concern in centralized handling [O_ISAC_039]. Additional text reports that only model weights are transmitted while local datasets remain local at user agents [O_ISAC_039].

5) **Practical implication for roadmap.** The VIII-D roadmap should treat privacy controls and update-interface constraints as mandatory context tags for reliability and trust evaluation across studies [O_ISAC_039].

### Challenge Cases 3-4

#### Challenge Case 3 - Authentication and Trust Exposure Under Dense, Heterogeneous Connectivity

1) **Challenge title.** Authentication and trust exposure under dense, heterogeneous connectivity in security_privacy_reliability.

2) **Failure mode.** Evidence indicates that key-based encryption and authentication may be less well-tailored at massive scale, and dynamic key management can become a trust bottleneck [O_ISAC_156].

3) **Affected interfaces/layers.** Affected layers include physical-layer confidentiality/authentication primitives, key-management and distribution interfaces, and edge trust loops that depend on message legitimacy and integrity checks [O_ISAC_156].

4) **Evidence snippet summary.** Representative text states that dense-network operation raises dynamic key-management concerns, while authentication and integrity remain crucial security processes [O_ISAC_156]. The same source treats confidentiality, authentication, and malicious-node detection as coupled targets [O_ISAC_156].

5) **Practical implication for roadmap.** The VIII-D roadmap should treat authentication and trust as lifecycle constraints requiring explicit safeguards and conservative claims across heterogeneous deployments [O_ISAC_156].

#### Challenge Case 4 - Fail-Safe Integrity Monitoring for Co-Route Fiber Disruption Risk

1) **Challenge title.** Fail-safe integrity monitoring for co-route fiber disruption risk in transport-network operation.

2) **Failure mode.** Evidence indicates that co-route fiber faults can propagate into service interruption, and sudden failures can degrade reliability when warning response is delayed [O_ISAC_041].

3) **Affected interfaces/layers.** Affected interfaces include transport physical infrastructure, sensing-communication coexistence paths, SDN-linked monitoring loops, and edge orchestration decisions for service continuity [O_ISAC_041].

4) **Evidence snippet summary.** Representative text states that interruption events can significantly impede IoE operation and that real-time monitoring/warning is necessary under sudden failures [O_ISAC_041]. Additional text reports SDN-linked timely alerting and service adjustment steps to avoid interruption propagation [O_ISAC_041].

5) **Practical implication for roadmap.** The VIII-D roadmap should prioritize integrity-monitoring readiness in fail-safe loops before claiming reliability under disruption [O_ISAC_041].

### Math Anchor

#### Decision

- Decision: **Option-1 (risk-constrained service utility)**.
- Why Option-2 is weaker: explicit overhead and availability constraint semantics are not directly grounded in the selected evidence subset.

\[
\begin{aligned}
\max_{u=(u_{\mathrm{auth}},u_{\mathrm{mon}},u_{\mathrm{priv}})} \quad & U_{\mathrm{service}}(u) \\
\text{s.t.} \quad & R_{\mathrm{int}}(u) \le \varepsilon_{\mathrm{int}}, \\
& L_{\mathrm{priv}}(u) \le \varepsilon_{\mathrm{priv}}, \\
& A_{\mathrm{auth}}(u) \ge \tau_{\mathrm{auth}}.
\end{aligned}
\]

Evidence indicates that service utility is exposed when network interruption events occur and when falsification risks degrade trustworthiness, so `R_int` is linked to interruption and integrity-monitoring risk under SDN alerting and service-adjustment workflows [O_ISAC_041; O_ISAC_145]. Evidence also reports confidential-data leakage concern and a model-update exchange rule, which directly supports the privacy-leakage constraint `L_priv` and the `u_priv` policy component [O_ISAC_039]. For authentication feasibility, evidence indicates that dense heterogeneous connectivity raises dynamic key-management burden while authentication and integrity remain central security processes, supporting `A_auth` and the `u_auth` policy component [O_ISAC_156]. The monitoring component `u_mon` maps to real-time warning, alert-routing, and service-adjustment evidence [O_ISAC_041]. All thresholds are kept symbolic (`ε_int`, `ε_priv`, `τ_auth`) because no bound values are fixed in the extracted source text.

### Key Takeaways and Research Priorities

- Dense heterogeneous operation can stress key-management assumptions; reliability evaluation should expose trust-loop dependencies rather than assuming static credential logistics [O_ISAC_156].
- Confidentiality, authentication, and malicious-node detection are coupled; fail-safe reliability studies should keep integrity checks as first-class evaluation artifacts [O_ISAC_156].
- Co-route fiber disruption risk is operationally significant; security/privacy framing should be tied to continuity and survivability checks [O_ISAC_041].
- SDN-linked alerting and service adjustment are central to fail-safe behavior; reliability roadmaps should require integrity-monitoring hooks in control loops [O_ISAC_041].
