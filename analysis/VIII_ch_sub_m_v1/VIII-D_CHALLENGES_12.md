### Challenge Case 1 - Physical-Layer Confidentiality and Trust Exposure in Hybrid Links

1) **Challenge title.** Physical-layer confidentiality and trust exposure in hybrid RF-OWC security operation.

2) **Failure mode.** Evidence indicates that wireless links can remain susceptible to eavesdropping, and trust in received sensing/communication outputs can degrade when adversaries manipulate observations [O_ISAC_145].

3) **Affected interfaces/layers.** The affected interfaces include physical-layer signal confidentiality, jammer-aware channel behavior, and trust interpretation in edge decision loops that consume sensing-assisted communication outputs [O_ISAC_145].

4) **Evidence snippet summary.** Representative text states that wireless transmissions are susceptible to eavesdropping and require robust security treatment [O_ISAC_145]. Additional text reports attacker-side falsification risk that can undermine output trustworthiness in hybrid sensing/communication contexts [O_ISAC_145].

5) **Practical implication for roadmap.** The VIII-D roadmap should treat confidentiality-integrity checks as a coupled risk surface that requires safeguards before cross-scenario security claims [O_ISAC_145].

### Challenge Case 2 - Privacy Leakage Pressure in Multi-User Sensing-Learning Pipelines

1) **Challenge title.** Privacy leakage pressure in federated multi-user sensing-learning pipelines.

2) **Failure mode.** Evidence indicates that distributed VIPAC training can involve sensitive location/trajectory information, so privacy exposure can increase if update exchange and aggregation boundaries are weakly specified [O_ISAC_039].

3) **Affected interfaces/layers.** The affected layers include metadata/privacy governance at user agents, model-update interfaces between agents and server, and orchestration policies that separate local datasets from shared parameters [O_ISAC_039].

4) **Evidence snippet summary.** Representative text reports explicit privacy-preservation intent in federated training and highlights confidential data-leakage concern in centralized handling [O_ISAC_039]. Additional text reports that only model weights are transmitted while local datasets remain local at user agents [O_ISAC_039].

5) **Practical implication for roadmap.** The VIII-D roadmap should treat privacy controls and update-interface constraints as mandatory context tags for reliability and trust evaluation across studies [O_ISAC_039].
