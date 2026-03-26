Under `deployment_convergence_roadmap`, the first two cases suggest that deployment friction can persist even when component-level gains appear strong.

### Roadmap Case 1 - Coupled Deployment Dependency Between Sensing and Communication Tasks

1) **Case title.** Coupled deployment dependency between sensing-positioning and communication-channel-estimation workflows.

2) **Failure mode.** When convergence is assumed too early, isolated task pipelines can keep performance bottlenecks at the deployment boundary, because separate design practice can weaken joint efficiency expectations [O_ISAC_039].

3) **Affected interfaces/layers.** The affected layers include sensing-positioning and channel-estimation interfaces, plus orchestration loops that coordinate shared model states across nonstationary operating contexts [O_ISAC_039].

4) **Evidence snippet summary.** Source text states that isolated design has limited efficiency and that positioning and channel-estimation tasks are integrated in one unified architecture [O_ISAC_039]. The same source also indicates an MTFL orchestration element for spatiotemporal generalization, which suggests deployment coupling across task states [O_ISAC_039].

5) **Practical implication for roadmap.** The roadmap requires explicit convergence gating across coupled interfaces before portability claims are made across deployment contexts [O_ISAC_039].

### Roadmap Case 2 - Staged Roll-Out and Readiness Gating Under Multi-Issue Integration

1) **Case title.** Staged roll-out and readiness gating under multi-issue integration pressure.

2) **Failure mode.** When convergence is treated as immediate, deployment plans can understate the need to coordinate multiple design issues jointly, and readiness interpretation can become unstable across settings [O_ISAC_163].

3) **Affected interfaces/layers.** The affected layers include deployment orchestration, readiness signaling, and governance interfaces that map application expectations to implementation constraints [O_ISAC_163].

4) **Evidence snippet summary.** Source text reports that practical implementation and eventual roll-out require multiple issues to be addressed together [O_ISAC_163]. The same source also highlights deployment-linked challenges and uneven maturity signals, which can support staged readiness framing [O_ISAC_163].

5) **Practical implication for roadmap.** The roadmap requires symbolic staged roll-out checkpoints with readiness gating language, without assuming uniform convergence across deployment scenarios [O_ISAC_163].
