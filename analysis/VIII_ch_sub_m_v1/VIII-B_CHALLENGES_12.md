### Challenge Case 1 — Front-End Co-Design Scalability Bottleneck

1) **Failure mode.** Evidence indicates that independently operated sensing and communication stacks increase hardware complexity, cost, and spectrum inefficiency [O_ISAC_237]. Evidence also indicates that bistatic sensing support can become infeasible on common communication receivers because required analogue FMCW hardware is unavailable [O_ISAC_237].

2) **Affected layers/resources.** The primary impact is hardware-plane: RF front-end sharing, receiver-chain composition, and implementation burden in sensing-aided estimation and interference-cancellation pipelines [O_ISAC_237]. Evidence further indicates that reducing RF hardware complexity and simplifying the FMCW receiver remains a central implementation pressure [O_ISAC_035].

3) **Evidence snippet summary.** Representative texts report both baseline hardware-duplication burden and explicit computational stacks for channel estimation, interference cancellation, and sensing algorithms [O_ISAC_237]. Complementary evidence reports simplified receiver design as a hardware-efficiency target [O_ISAC_035].

4) **Practical implication for roadmap.** For VIII-B, evidence indicates an implementation bottleneck where hardware simplification must keep pace with added receiver processing blocks [O_ISAC_237][O_ISAC_035].

### Challenge Case 2 — Edge Energy-Latency Hardware Ceiling

1) **Failure mode.** Evidence indicates that edge deployments face strict hardware feasibility limits because energy budgets are often below 1 watt and processing delays can exceed 50 milliseconds [O_ISAC_093].

2) **Affected layers/resources.** The primary impacts are hardware-plane power/SWaP budgets, edge inference latency budgets, and terminal DSP burdens [O_ISAC_093][O_ISAC_095]. Evidence also indicates increased computational complexity for a single IRS unit during localization [O_ISAC_112].

3) **Evidence snippet summary.** Representative evidence reports sub-watt edge budgets and delay escalation for complex tasks [O_ISAC_093], and reports that FOE-free processing is used to reduce terminal complexity and power consumption [O_ISAC_095]. Additional evidence reports higher localization-stage complexity for IRS-aided processing [O_ISAC_112].

4) **Practical implication for roadmap.** Communication-plane and sensing-plane metric gains remain conditional on hardware-plane energy and latency envelopes in edge and terminal implementations [O_ISAC_093][O_ISAC_095][O_ISAC_112].
