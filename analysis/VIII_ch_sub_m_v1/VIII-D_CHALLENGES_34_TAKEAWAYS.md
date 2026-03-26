### Challenge Case 3 - Authentication and Trust Exposure Under Dense, Heterogeneous Connectivity

1) **Challenge title.** Authentication and trust exposure under dense, heterogeneous connectivity in security_privacy_reliability.

2) **Failure mode.** Evidence indicates that key-based encryption and authentication may be less well-tailored at massive scale, and dynamic key management can become a trust bottleneck [O_ISAC_156].

3) **Affected interfaces/layers.** Affected layers include physical-layer confidentiality/authentication primitives, key-management and distribution interfaces, and edge trust loops that depend on message legitimacy and integrity checks [O_ISAC_156].

4) **Evidence snippet summary.** Representative text states that dense-network operation raises dynamic key-management concerns, while authentication and integrity remain crucial security processes [O_ISAC_156]. The same source treats confidentiality, authentication, and malicious-node detection as coupled targets [O_ISAC_156].

5) **Practical implication for roadmap.** The VIII-D roadmap should treat authentication and trust as lifecycle constraints requiring explicit safeguards and conservative claims across heterogeneous deployments [O_ISAC_156].

### Challenge Case 4 - Fail-Safe Integrity Monitoring for Co-Route Fiber Disruption Risk

1) **Challenge title.** Fail-safe integrity monitoring for co-route fiber disruption risk in transport-network operation.

2) **Failure mode.** Evidence indicates that co-route fiber faults can propagate into service interruption, and sudden failures can degrade reliability when warning response is delayed [O_ISAC_041].

3) **Affected interfaces/layers.** Affected interfaces include transport physical infrastructure, sensing-communication coexistence paths, SDN-linked monitoring loops, and edge orchestration decisions for service continuity [O_ISAC_041].

4) **Evidence snippet summary.** Representative text states that interruption events can significantly impede IoE operation and that real-time monitoring/warning is necessary under sudden failures [O_ISAC_041]. Additional text reports SDN-linked timely alerting and service adjustment steps to avoid interruption propagation [O_ISAC_041].

5) **Practical implication for roadmap.** The VIII-D roadmap should prioritize integrity-monitoring readiness in fail-safe loops before claiming reliability under disruption [O_ISAC_041].

### Key Takeaways and Research Priorities

- Dense heterogeneous operation can stress key-management assumptions; reliability evaluation should expose trust-loop dependencies rather than assuming static credential logistics [O_ISAC_156].
- Confidentiality, authentication, and malicious-node detection are coupled; fail-safe reliability studies should keep integrity checks as first-class evaluation artifacts [O_ISAC_156].
- Co-route fiber disruption risk is operationally significant; security/privacy framing should be tied to continuity and survivability checks [O_ISAC_041].
- SDN-linked alerting and service adjustment are central to fail-safe behavior; reliability roadmaps should require integrity-monitoring hooks in control loops [O_ISAC_041].
