# VIII. Open Challenges and Research Roadmap

Section VIII synthesizes open challenges and frames a deployment-facing research roadmap for optical integrated sensing and communication. In this review, the challenge map is treated as an organizational taxonomy and is scoped with five exact domains: `standardization_interoperability`, `hardware_scalability_efficiency`, `channel_modeling_evaluation`, `security_privacy_reliability`, and `deployment_convergence_roadmap`. This structure is used to consolidate heterogeneous findings into a consistent challenge lens, not to assert closed-form completeness. Representative evidence indicates that standards alignment and interoperability remain active issues in subsea-integrated settings [O_ISAC_220], while shared-waveform designs continue to expose hardware and implementation complexity tradeoffs in communication-plus-ranging pipelines [O_ISAC_035]. This prioritization supports a traceable transition from challenge diagnosis to roadmap planning.

The evidence policy for this section is intentionally strict. DIRECT support is restricted to text-anchored excerpt rows in the subsection evidence CSVs, whereas upstream bridge rows linking Sections V/VI/VII are treated as INDIRECT by design and interpreted cautiously. Under this policy, representative works show persistent channel-modeling and evaluation consistency gaps in deterministic high-frequency sensing studies [O_ISAC_115], and they also indicate security-facing reliability concerns when sensing and communication functions are co-integrated on the same transmission substrate [O_ISAC_202]. For roadmap framing, deployment convergence is treated as an open issue tied to technology-readiness and multi-constraint rollout planning, with representative survey evidence emphasizing practical integration dependencies [O_ISAC_163].

At the manuscript level, this section operationalizes protocol RQ3 by translating the evidence pack into methodological gaps, 6G-facing integration pressure, and a conservative research agenda. Section V established where comparison remains admissible, Section VI bounded what enabling stacks can realistically support, and Section VII showed where deployment evidence actually concentrates; Section VIII converts those upstream signals into a challenge-to-roadmap reading rather than reopening them as separate evidence pools. Consistent with the review's TQAF-aware synthesis policy, prioritization is interpreted cautiously whenever support remains indirect, weak, or FLAGGED, and any implication for optical RIS, ORIS, or optical phased arrays is treated only as a forward-looking architectural implication rather than as a separate evidence-bearing challenge domain.

![Fig. VIII-1. Challenge-to-roadmap dependency map for O-ISAC. The figure organizes the five Section VIII challenge domains around a central shared-system-pressure hub and a roadmap-outcome cluster while preserving the review's evidence-aware, dependency-driven interpretation. The bottom bridge ribbon should be read as a manuscript-level reminder that Section VIII is informed by Section V tradeoffs, constrained by Section VI enablers and benchmarks, and validated against Section VII deployments.](fig_viii_1.jpg)

The figure should be read as a dependency map rather than a maturity ladder: the domain cards identify where pressure accumulates, the central hub identifies what kind of pressure is shared across domains, and the outcome cluster summarizes what a credible roadmap must eventually deliver.

## VIII-A. Standardization and Interoperability Challenges

### Context

VIII-A (Standardization and Interoperability Challenges) frames the `standardization_interoperability` domain as a deployment-facing bottleneck rather than a closed technical problem. Evidence from representative studies indicates that interoperability pressure already appears where sensing and communication must co-exist on shared infrastructure. In SMART subsea settings, standardization is explicitly tied to joint-task-force framing and integrated sensing-communication operation over telecommunication cables [O_ISAC_220]. In optical transport support for ISAC, architecture-level interconnection across RAN, MEC, and SDN-controlled transport highlights practical interoperability requirements spanning radio, transport, and sensing workflows [O_ISAC_025]. A hardware-centric ISAC transceiver review further indicates that emerging standardization efforts and early commercial prototypes are moving the field from isolated demonstrations toward implementation-oriented integration [O_ISAC_161]. Accordingly, this subsection treats `standardization_interoperability` as an open issue focused on interface alignment, cross-domain control consistency, and implementation-ready integration boundaries, with cautious interpretation of any upstream bridge evidence because Section V/VI/VII links are INDIRECT by design.

### Challenge Case 1: Standards Vocabulary and Reference-Model Divergence
**Failure mode.** Without aligned standardization vocabulary and reference-model assumptions, implementations can expose incompatible expectations for integrated sensing-communication operation, which limits cross-system comparability and deployment transferability [O_ISAC_220] [O_ISAC_161].

**Affected interfaces/layers.** The most exposed points are control-plane terminology alignment, sensing-metadata semantics, timing/synchronization assumptions, and transceiver-to-orchestration interface consistency across multi-domain deployments [O_ISAC_220] [O_ISAC_161].

**Evidence snippet summary.** Evidence indicates that SMART-oriented integrated operation is explicitly tied to a standardized framing under a joint task-force context [O_ISAC_220]. A hardware-centric transceiver survey also reports intensified industry activity around standardization and prototype transition, indicating that interface consistency has shifted from conceptual discussion to implementation pressure [O_ISAC_161].

**Practical implication for roadmap.** The roadmap should treat reference-model and terminology alignment as a prerequisite gating item for credible cross-platform evaluation in this domain [O_ISAC_220] [O_ISAC_161].

### Challenge Case 2: Cross-Domain Interoperability Friction in Transport-Supported ISAC
**Failure mode.** When communication and sensing flows are jointly carried but interoperability assumptions differ across transport, orchestration, and sensing-processing stages, routing and capacity decisions can become brittle under operational variability [O_ISAC_025].

**Affected interfaces/layers.** Friction appears at data-plane IQ stream handling, control-plane orchestration and SDN policy exchange, sensing metadata exchange, and timing/latency coordination between access and aggregation segments [O_ISAC_025].

**Evidence snippet summary.** A transport-oriented ISAC architecture shows explicit RAN-core/MEC interconnection requirements and a joint optimization workflow for communication-plus-sensing flows, indicating nontrivial multi-interface coupling [O_ISAC_025].

**Practical implication for roadmap.** Evidence indicates that interoperability profiling across joint sensing/communication transport workflows should remain a first-order roadmap risk item [O_ISAC_025].

### Challenge Case 3: PtMP Branch-Attribution and Measurement-Semantics Misalignment
**Failure mode.** In point-to-multipoint access deployments, sensing pipelines can fail to provide unambiguous branch-level attribution when monitoring assumptions are not aligned with deployment topology and loss conditions, weakening interoperability at the measurement-contract level [O_ISAC_104].

**Affected interfaces/layers.** The main pressure points are sensing-metadata semantics (which branch/event a stream represents), evaluation/reporting contracts for anomaly attribution, and control-layer interpretation of branch-specific sensing quality under splitter loss [O_ISAC_104].

**Evidence snippet summary.** INDIRECT evidence indicates that PtMP structure is described as a practical challenge for fiber-based sensing in deployed access infrastructure, and that splitter-induced link-budget loss can drive sensing failure conditions [O_ISAC_104].

**Practical implication for roadmap.** The roadmap should treat branch-attribution semantics and reporting consistency as a first-class interoperability checkpoint before cross-vendor scaling in access scenarios [O_ISAC_104].

### Challenge Case 4: Sensing-Payload Formatting and DSP-Compatibility Contract Gaps
**Failure mode.** When sensing payload placement and frequency-allocation assumptions are not explicitly aligned with communication signal structure, interoperability can break at receiver processing boundaries and low-interference joint operation becomes fragile [O_ISAC_220].

**Affected interfaces/layers.** Critical interfaces include data-plane sensing-payload formatting, frequency/timing alignment between sensing joints and shore transceivers, and receiver-side DSP interface contracts used for joint demodulation [O_ISAC_220].

**Evidence snippet summary.** Evidence indicates that SMART-oriented dense integration must address precise allocation of sensing information into communication frequency blanks, and that communication-compatible DSP is treated as a compatibility condition [O_ISAC_220].

**Practical implication for roadmap.** Roadmap staging should prioritize explicit format-and-DSP conformance checks for sensing payload interoperability in dense integrated links [O_ISAC_220].

### Math Anchor
Decision variables are profile/format selection, sensing-payload placement policy, and receiver DSP processing mode:

$$
\begin{aligned}
u &= (u_{\mathrm{profile}},u_{\mathrm{placement}},u_{\mathrm{dsp}}),\\
\max_{u}\quad & J_{\mathrm{perf}}(u),\\
\text{s.t.}\quad 
& u_{\mathrm{profile}} \in \mathcal{U}_{\mathrm{SMART\_conform}},\\
& (u_{\mathrm{placement}},u_{\mathrm{profile}}) \in \mathcal{U}_{\mathrm{blank\_allocation}},\\
& (u_{\mathrm{dsp}},u_{\mathrm{placement}}) \in \mathcal{U}_{\mathrm{dsp\_compatible}},\\
& u \in \mathcal{U}_{\mathrm{PtMP\_attribution}},\quad J_{\mathrm{perf}}(u) \in \mathcal{J}_{\mathrm{QoS\_acceptable}}.
\end{aligned}
$$

This anchor uses Option-2 because the available evidence is constraint-centric rather than weight-tuning-centric: SMART is explicitly presented as a standardized configuration, and dense operation is explicitly tied to precise placement of sensing information into communication frequency blanks [O_ISAC_220]. The compatibility requirement is also textual and direct, since sensing transmission format design is linked to communication-compatible DSP behavior, so the feasible set must jointly constrain placement policy and DSP processing mode [O_ISAC_220]. For access-network interoperability, PON evidence reports both standards-linked spectral-occupancy requirements and PtMP ambiguity risk under simultaneous interrogation of multiple drop fibers, which motivates an explicit attribution-integrity constraint [O_ISAC_104]. Finally, the symbolic objective \(J_{\mathrm{perf}}\) is retained as a communication-plus-sensing QoS proxy because spectral-efficiency degradation and sensing-failure risk are both documented in the evidence base [O_ISAC_220] [O_ISAC_104].

### Key Takeaways and Research Priorities
- Interoperability risk in VIII-A is not only a standards-label issue; it also appears in branch-level sensing semantics and attribution contracts under PtMP operation [O_ISAC_104].
- Format compatibility between sensing payloads and communication-oriented DSP flows is a deployment-facing interoperability dependency in dense integrated links [O_ISAC_220].
- Evidence indicates that evaluation/reporting contracts and signal-format contracts should be prioritized separately because they fail at different interfaces [O_ISAC_104] [O_ISAC_220].
- working hypothesis: a compact conformance profile coupling branch-attribution semantics with DSP-interface checks may reduce cross-platform integration ambiguity.

## VIII-B. Hardware Scalability and Efficiency Challenges
### Context
Section VIII-B defines `hardware_scalability_efficiency` as a cross-cutting bottleneck because hardware-plane burdens accumulate even when integrated waveforms improve joint operation [O_ISAC_035][O_ISAC_162]. Evidence indicates that complexity growth is driven by extra baseband processing, filtering, and coordination overhead as integration depth increases [O_ISAC_162]. Representative works also report power/SWaP pressure at edge hardware, including sub-watt energy budgets with delays beyond tens of milliseconds for complex processing pipelines [O_ISAC_093]. A further friction point is implementation scaling in beamforming hardware: fine steering granularity is achievable, but control-system and fabrication burdens increase with larger arrays and tighter precision requirements [O_ISAC_171]. Communication-plane outcomes (rate/BER) and sensing-plane outcomes (resolution/accuracy) are relevant but secondary in this context; the primary blocker is hardware-plane feasibility under scaling, power, and implementation constraints [O_ISAC_093][O_ISAC_162][O_ISAC_171].
### Challenge Case 1: Front-End Co-Design Scalability Bottleneck

1) **Failure mode.** Evidence indicates that independently operated sensing and communication stacks increase hardware complexity, cost, and spectrum inefficiency [O_ISAC_237]. Evidence also indicates that bistatic sensing support can become infeasible on common communication receivers because required analogue FMCW hardware is unavailable [O_ISAC_237].

2) **Affected layers/resources.** The primary impact is hardware-plane: RF front-end sharing, receiver-chain composition, and implementation burden in sensing-aided estimation and interference-cancellation pipelines [O_ISAC_237]. Evidence further indicates that reducing RF hardware complexity and simplifying the FMCW receiver remains a central implementation pressure [O_ISAC_035].

3) **Evidence snippet summary.** Representative texts report both baseline hardware-duplication burden and explicit computational stacks for channel estimation, interference cancellation, and sensing algorithms [O_ISAC_237]. Complementary evidence reports simplified receiver design as a hardware-efficiency target [O_ISAC_035].

4) **Practical implication for roadmap.** For VIII-B, evidence indicates an implementation bottleneck where hardware simplification must keep pace with added receiver processing blocks [O_ISAC_237][O_ISAC_035].

### Challenge Case 2: Edge Energy-Latency Hardware Ceiling

1) **Failure mode.** Evidence indicates that edge deployments face strict hardware feasibility limits because energy budgets are often below 1 watt and processing delays can exceed 50 milliseconds [O_ISAC_093].

2) **Affected layers/resources.** The primary impacts are hardware-plane power/SWaP budgets, edge inference latency budgets, and terminal DSP burdens [O_ISAC_093][O_ISAC_095]. Evidence also indicates increased computational complexity for a single ORIS unit during localization [O_ISAC_112].

3) **Evidence snippet summary.** Representative evidence reports sub-watt edge budgets and delay escalation for complex tasks [O_ISAC_093], and reports that FOE-free processing is used to reduce terminal complexity and power consumption [O_ISAC_095]. Additional evidence reports higher localization-stage complexity for ORIS-aided processing [O_ISAC_112].

4) **Practical implication for roadmap.** Communication-plane and sensing-plane metric gains remain conditional on hardware-plane energy and latency envelopes in edge and terminal implementations [O_ISAC_093][O_ISAC_095][O_ISAC_112].
### Challenge Case 3: Integration-Level Hardware Co-Design and Baseband Cost Escalation

1) **Challenge title.** Integration-level hardware co-design and baseband cost escalation under `hardware_scalability_efficiency`.

2) **Failure mode.** Evidence indicates that optimizing one shared transceiver for sensing and communication is highly challenging because requirements conflict at architecture level [O_ISAC_161]. Evidence also indicates that high mobility and severe path loss can push beam-steering demands beyond economically viable conventional antenna designs [O_ISAC_142].

3) **Affected layers/resources.** The dominant impact is hardware-plane: antenna/RF architecture choices that require continuous trade-off balancing during development [O_ISAC_161]. A second impact is baseband resource pressure, where reused OFDM signals may introduce additional processing complexity and cost [O_ISAC_162].

4) **Evidence snippet summary.** Representative texts report that many architectural/electrical parameters require careful balancing [O_ISAC_161], and that integration level governs extra baseband cost exposure [O_ISAC_162]. Related evidence also reports unresolved analogue front-end drift effects in practical operation [O_ISAC_162].

5) **Practical implication for roadmap.** The VIII-B roadmap should treat integration-level complexity accounting as a hardware gate before scale-out to path-loss-constrained deployments [O_ISAC_161][O_ISAC_142][O_ISAC_162].

### Challenge Case 4: Beam-Control Scalability, FLOP Growth, and Latency Envelope Limits

1) **Challenge title.** Beam-control scalability, FLOP growth, and latency envelope limits in large-array operation.

2) **Failure mode.** Evidence indicates that communication-plane beamforming overhead becomes large in highly mobile cells [O_ISAC_134]. Evidence also indicates that conventional delay-line beam control can require substantial switching/control burden as steering granularity tightens [O_ISAC_171].

3) **Affected layers/resources.** The primary impacts are hardware-plane beam-control complexity and compute-plane FLOP/latency budgets in multimodal beam prediction pipelines [O_ISAC_134][O_ISAC_171]. Representative measurements report millisecond-level processing latency and model-stage complexity concentration [O_ISAC_134].

4) **Evidence snippet summary.** Representative studies report communication-overhead pressure [O_ISAC_134], MMT-dominated complexity and measurable processing latency [O_ISAC_134], and beam-control complexity reduction with scalable frequency-comb steering [O_ISAC_171].

5) **Practical implication for roadmap.** The VIII-B roadmap should co-design steering granularity, model complexity, and hardware budget jointly, rather than scaling them independently [O_ISAC_134][O_ISAC_171].
### Math Anchor
Selected form: Option-2 (resource-constrained performance optimization).

$$
\begin{aligned}
\max_{u=(u_{arch},u_{proc},u_{ctrl})} \quad & U_{perf}(u;s)=\beta_c U_{comm}(u;s_{comm})+\beta_s U_{sens}(u;s_{sens}) \\
\text{s.t.} \quad & C_{hw}(u;s) \le C_{max}, \\
& L_{hw}(u;s) \le L_{max}, \\
& P_{hw}(u;s) \le P_{max}, \\
& O_{ctrl}(u;s) \le O_{max}.
\end{aligned}
$$

This anchor adopts Option-2 because direct evidence supports four distinct hardware constraints for VIII-B: computational burden, processing-latency envelope, energy constraint, and beam-control overhead [O_ISAC_134][O_ISAC_161][O_ISAC_171]. The decision variable tuple $u=(u_{arch},u_{proc},u_{ctrl})$ captures architecture choice, processing schedule, and control-update policy under scenario context $s=(s_{shared},s_{mob},s_{array})$, where shared transceiver use, high mobility, and large-array steering pressure are explicitly evidenced [O_ISAC_134][O_ISAC_161][O_ISAC_171]. Plane separation is explicit in $U_{perf}$: $U_{comm}$ denotes comm-plane utility (beamforming/communication efficiency), while $U_{sens}$ denotes sensing-plane utility (sensing/imaging capability). Constraint $C_{hw}$ bounds compute and baseband complexity, $L_{hw}$ bounds delay, $P_{hw}$ bounds hardware energy demand, and $O_{ctrl}$ bounds steering/control overhead. This keeps hardware scalability and efficiency primary, while permitting performance optimization only inside hardware-feasible regions.
### Key Takeaways and Research Priorities

- Build integration-level complexity ledgers that jointly track RF architecture constraints and baseband-cost escalation before deployment decisions [O_ISAC_161][O_ISAC_162].
- Prioritize hardware-plane beam-control schemes that avoid switch-count explosion while preserving fine steering granularity for large arrays [O_ISAC_171].
- Add calibration-aware front-end drift handling as a first-class hardware requirement for sustained field performance [O_ISAC_162].
- Co-design multimodal pipeline FLOPs, latency envelopes, and beam-pruning strategy to reduce communication-plane overhead without destabilizing beam quality [O_ISAC_134].

## VIII-C. Channel Modeling and Evaluation Challenges

### Context
Evidence indicates that channel modeling and evaluation are foundational for O-ISAC credibility because conclusions are not transferable without validated propagation assumptions across environments and implementations [O_ISAC_005][O_ISAC_327]. Turbulence, pointing, and blockage factors remain a core bottleneck: weather-dependent attenuation and alignment-sensitive behavior can shift effective channel conditions across deployments [O_ISAC_005][O_ISAC_327]. NLoS geometry and intermittency are also unresolved, since multipath and scatterer-dependent effects require explicit modeling and estimation rather than fixed simplifications [O_ISAC_050]. Evaluation practice further needs metric-plane alignment: comm-plane indicators such as BER/capacity should be interpreted together with sensing-plane estimation outcomes, not in isolation [O_ISAC_381][O_ISAC_050]. Finally, benchmarking and reproducibility depend on consistent channel-model disclosure and measurement-campaign comparability, which remains an open issue for reliable cross-study roadmap decisions [O_ISAC_327].

### Challenge Case 1: Weather-Conditioned Channel-Model Transferability Gap

1) **Challenge title.** Weather-conditioned channel-model transferability gap in O-ISAC evaluation.

2) **Failure mode.** Evidence indicates that adverse weather can materially change channel behavior, so assumptions tuned under one condition can fail under another condition [O_ISAC_005]. Evidence also indicates that sensing feedback is tied to the back-scattered signal relation with forward channel gain, creating model drift risk when this relation changes [O_ISAC_005].

3) **Affected interfaces/assumptions.** The most affected interfaces are atmospheric attenuation assumptions, back-scattered-feedback-to-channel-gain mapping, and scenario conditioning for channel-state estimation [O_ISAC_005].

4) **Evidence snippet summary.** Representative text reports that adverse weather reduces FSO link reliability and that evaluation is performed using a realistic channel model with climatic data [O_ISAC_005]. This indicates that portability of conclusions depends on environmental conditioning, not only algorithm selection [O_ISAC_005].

5) **Practical implication for roadmap.** The VIII-C roadmap should treat climate-conditioned model validation as a prerequisite before cross-scenario comparison claims [O_ISAC_005].

### Challenge Case 2: LOS/NLOS Decomposition and Scatterer-State Identifiability Gap

1) **Challenge title.** LOS/NLOS decomposition and scatterer-state identifiability gap in channel evaluation.

2) **Failure mode.** Evidence indicates that practical modeling must decouple LOS and NLOS paths and jointly estimate scattering-related states; otherwise, model mismatch remains likely under multipath conditions [O_ISAC_050].

3) **Affected interfaces/assumptions.** The key interfaces are LOS/NLOS decomposition assumptions, equivalent NLOS channel-state representation, and estimation burden in non-convex settings [O_ISAC_050].

4) **Evidence snippet summary.** Representative text reports an equivalent discrete channel remodeling method that decouples LOS and NLOS paths and a joint estimation strategy for scattering states [O_ISAC_050]. Conclusion text further indicates multipath-interference and random-fading sensitivity in evaluation [O_ISAC_050].

5) **Practical implication for roadmap.** The VIII-C roadmap should prioritize explicit reporting of decomposition assumptions and estimation scope before claiming robust cross-study comparability [O_ISAC_050].

### Challenge Case 3: Comm-Plane Metric Interface Coupling Under Evaluation Conditions

1) **Challenge title.** Comm-plane metric interface coupling under evaluation conditions.

2) **Failure mode.** Evidence indicates that evaluation pipelines rely on comm-plane BER and comm-plane capacity outcomes, and these outcomes shift with transmission-distance settings [O_ISAC_381]. This creates a comparability risk when studies report metrics without a harmonized condition contract [O_ISAC_381].

3) **Affected assumptions/interfaces.** The affected interfaces are metric-definition choices, measurement-condition declarations, and channel-capacity interpretation boundaries across test distances and hardware capture constraints [O_ISAC_381].

4) **Evidence snippet summary.** Representative text reports BER-to-capacity evaluation and distance-conditioned BER/rate behavior [O_ISAC_381]. Additional text indicates capacity degradation with distance growth, reinforcing condition-sensitive evaluation outcomes [O_ISAC_381].

5) **Practical implication for roadmap.** The VIII-C roadmap should treat condition-tagged comm-plane reporting as mandatory before cross-paper ranking claims [O_ISAC_381].

### Challenge Case 4: Benchmark Contract Fragmentation Across Channel Modeling Studies

1) **Challenge title.** Benchmark contract fragmentation across channel modeling studies.

2) **Failure mode.** Evidence indicates that channel-modeling evidence is distributed across heterogeneous measurement campaigns, scenario types, and model families, reducing direct comparability across studies [O_ISAC_327]. Evidence also indicates that new technologies and applications introduce additional modeling challenges that invalidate static benchmark assumptions [O_ISAC_327].

3) **Affected assumptions/interfaces.** The affected interfaces are reporting contracts for channel-model class, measurement-campaign provenance, and framework compatibility for standardization-oriented evaluation [O_ISAC_327].

4) **Evidence snippet summary.** Representative text reports broad survey coverage of measurement campaigns and model families, and explicitly states that a standard VLC channel model is needed for 6G evaluation workflows [O_ISAC_327].

5) **Practical implication for roadmap.** The VIII-C roadmap should treat benchmark-contract normalization as a prerequisite for reproducible evidence aggregation [O_ISAC_327].

### Math Anchor
Selected form: Option-B (benchmark-contract constrained evaluation).

$$
\max_{\pi}\; U_{\mathrm{eval}}(\pi)
$$
$$
\text{s.t.}\; \pi \in \Pi_{\mathrm{contract}},\quad
\Pi_{\mathrm{contract}} = \{\kappa_{\mathrm{cond}},\,\gamma_{\mathrm{geom}},\,\mu_{\mathrm{metric}},\,\delta_{\mathrm{prov}}\}
$$

This anchor maps VIII-C to benchmark-contract constrained evaluation by forcing each result protocol to carry channel-condition tags and scenario-geometry descriptors before cross-paper comparison, which directly follows weather-conditioned channel behavior and geometry-dependent reporting contexts [O_ISAC_005, O_ISAC_327]. The term $\mu_{\mathrm{metric}}$ is comm-plane specific and binds BER-capacity definitions to evaluation conditions (for example distance-conditioned reporting), while sensing-plane metrics are intentionally not instantiated because direct sensing-plane evidence is not present in the locked evidence subset [O_ISAC_381]. The term $\delta_{\mathrm{prov}}$ encodes measurement-campaign and dataset/testbed provenance so that the documented need for a standard model becomes an enforceable contract item rather than a narrative recommendation [O_ISAC_327].

### Key Takeaways and Research Priorities

- Define an evaluation-contract minimum that records channel-model class plus measurement-campaign lineage before any cross-study synthesis step [O_ISAC_327].
- Require comm-plane metric declarations to be bound to measurement conditions in result tables to reduce hidden comparability drift [O_ISAC_381].
- Add a standard-framework compatibility field in benchmarks to align evidence with shared 6G evaluation baselines [O_ISAC_327].
- working hypothesis: a compact reporting card will reduce audit friction in Section VIII-C evidence integration.

## VIII-D. Security, Privacy, and Reliability Challenges

### Context

For VIII-D under security_privacy_reliability, evidence indicates that O-ISAC links couple security, privacy, and reliability because sensing increases observability while communication paths keep exploitable attack surfaces [O_ISAC_145][O_ISAC_039]. Physical-layer threat exposure remains a core motif: wireless transmissions can be susceptible to eavesdropping, so robust protection assumptions should be treated as conditional rather than guaranteed [O_ISAC_145]. A second motif is privacy leakage via sensing-enabled learning pipelines, where confidential user information can be involved and requires controlled data-handling practices [O_ISAC_039]. A third motif concerns authentication/trust posture, which remains tied to physical-layer security mechanisms and legitimacy checks in hybrid deployments [O_ISAC_145]. A fourth motif is fail-safe integrity monitoring, where transport-network ISAC evidence reports real-time warning pathways that can reduce service-interruption risk under disruptive vibration events [O_ISAC_041]. Together, these motifs frame VIII-D as a coupled risk-governance challenge, not a single-metric security problem.

### Challenge Case 1: Physical-Layer Confidentiality and Trust Exposure in Hybrid Links

1) **Challenge title.** Physical-layer confidentiality and trust exposure in hybrid RF-OWC security operation.

2) **Failure mode.** Evidence indicates that wireless links can remain susceptible to eavesdropping, and trust in received sensing/communication outputs can degrade when adversaries manipulate observations [O_ISAC_145].

3) **Affected interfaces/layers.** The affected interfaces include physical-layer signal confidentiality, jammer-aware channel behavior, and trust interpretation in edge decision loops that consume sensing-assisted communication outputs [O_ISAC_145].

4) **Evidence snippet summary.** Representative text states that wireless transmissions are susceptible to eavesdropping and require robust security treatment [O_ISAC_145]. Additional text reports attacker-side falsification risk that can undermine output trustworthiness in hybrid sensing/communication contexts [O_ISAC_145].

5) **Practical implication for roadmap.** The VIII-D roadmap should treat confidentiality-integrity checks as a coupled risk surface that requires safeguards before cross-scenario security claims [O_ISAC_145].

### Challenge Case 2: Privacy Leakage Pressure in Multi-User Sensing-Learning Pipelines

1) **Challenge title.** Privacy leakage pressure in federated multi-user sensing-learning pipelines.

2) **Failure mode.** Evidence indicates that distributed VIPAC training can involve sensitive location/trajectory information, so privacy exposure can increase if update exchange and aggregation boundaries are weakly specified [O_ISAC_039].

3) **Affected interfaces/layers.** The affected layers include metadata/privacy governance at user agents, model-update interfaces between agents and server, and orchestration policies that separate local datasets from shared parameters [O_ISAC_039].

4) **Evidence snippet summary.** Representative text reports explicit privacy-preservation intent in federated training and highlights confidential data-leakage concern in centralized handling [O_ISAC_039]. Additional text reports that only model weights are transmitted while local datasets remain local at user agents [O_ISAC_039].

5) **Practical implication for roadmap.** The VIII-D roadmap should treat privacy controls and update-interface constraints as mandatory context tags for reliability and trust evaluation across studies [O_ISAC_039].

### Challenge Case 3: Authentication and Trust Exposure Under Dense, Heterogeneous Connectivity

1) **Challenge title.** Authentication and trust exposure under dense, heterogeneous connectivity in security_privacy_reliability.

2) **Failure mode.** Evidence indicates that key-based encryption and authentication may be less well-tailored at massive scale, and dynamic key management can become a trust bottleneck [O_ISAC_156].

3) **Affected interfaces/layers.** Affected layers include physical-layer confidentiality/authentication primitives, key-management and distribution interfaces, and edge trust loops that depend on message legitimacy and integrity checks [O_ISAC_156].

4) **Evidence snippet summary.** Representative text states that dense-network operation raises dynamic key-management concerns, while authentication and integrity remain crucial security processes [O_ISAC_156]. The same source treats confidentiality, authentication, and malicious-node detection as coupled targets [O_ISAC_156].

5) **Practical implication for roadmap.** The VIII-D roadmap should treat authentication and trust as lifecycle constraints requiring explicit safeguards and conservative claims across heterogeneous deployments [O_ISAC_156].

### Challenge Case 4: Fail-Safe Integrity Monitoring for Co-Route Fiber Disruption Risk

1) **Challenge title.** Fail-safe integrity monitoring for co-route fiber disruption risk in transport-network operation.

2) **Failure mode.** Evidence indicates that co-route fiber faults can propagate into service interruption, and sudden failures can degrade reliability when warning response is delayed [O_ISAC_041].

3) **Affected interfaces/layers.** Affected interfaces include transport physical infrastructure, sensing-communication coexistence paths, SDN-linked monitoring loops, and edge orchestration decisions for service continuity [O_ISAC_041].

4) **Evidence snippet summary.** Representative text states that interruption events can significantly impede IoE operation and that real-time monitoring/warning is necessary under sudden failures [O_ISAC_041]. Additional text reports SDN-linked timely alerting and service adjustment steps to avoid interruption propagation [O_ISAC_041].

5) **Practical implication for roadmap.** The VIII-D roadmap should prioritize integrity-monitoring readiness in fail-safe loops before claiming reliability under disruption [O_ISAC_041].

### Math Anchor
Selected form: Option-1 (risk-constrained service utility).
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

## VIII-E. Deployment Convergence and Roadmap Challenges

### Context

For VIII-E under `deployment_convergence_roadmap`, evidence suggests that deployment convergence remains a distinct bottleneck beyond standards, hardware, channel modeling, and security, because sensing and communication functions may remain insufficiently co-integrated in practice [O_ISAC_039]. Across the micro-evidence set, four motifs recur: coupling between sensing-positioning and communication-channel-estimation tasks, orchestration and state-fusion stress, staged roll-out and readiness gating, and governance for transferability through compatibility, model validity, and provenance controls [O_ISAC_039; O_ISAC_151; O_ISAC_163; O_ISAC_200].

### Roadmap Case 1: Coupled deployment dependency between sensing and communication tasks
When convergence is assumed too early, separate task pipelines may keep bottlenecks at deployment interfaces [O_ISAC_039]. Affected layers include sensing-positioning interfaces, channel-estimation interfaces, and orchestration loops coordinating shared model states in nonstationary contexts [O_ISAC_039]. Source text reports both isolated-design limits and a unified architecture coupling these tasks, suggesting that convergence assumptions require explicit interface-level gating before portability interpretation [O_ISAC_039].

### Roadmap Case 2: Staged roll-out and readiness gating under multi-issue integration pressure
If convergence is treated as immediate, deployment planning may understate coordination requirements across multiple design issues, and readiness interpretation can remain unstable across settings [O_ISAC_163]. Affected layers include deployment orchestration, readiness signaling, and governance interfaces mapping application expectations to implementation constraints [O_ISAC_163]. Evidence indicating that practical implementation and eventual roll-out require issues to be addressed together supports symbolic staged roll-out framing [O_ISAC_163].

### Roadmap Case 3: Orchestration and state-fusion fragility in multimodal context loops
If orchestration assumptions are fixed before interfaces stabilize, multimodal sensing states and context annotations may drift across update loops under resource stress [O_ISAC_151]. Affected layers include orchestration APIs for multimodal inputs, context metadata interfaces (location/time), encoder update loops, and policy gates for state handoff [O_ISAC_151]. Evidence on multimodal physical quantities, contextual enrichment, and encoder-based semantic representations, together with edge-compute and bandwidth stress statements, suggests that context-bearing fusion contracts require readiness-oriented gating [O_ISAC_151].

### Roadmap Case 4: Open-source governance and transferability risk across heterogeneous stacks
If convergence is inferred from isolated implementations, transferability may weaken because infrastructure compatibility conditions and model-validity assumptions can vary across deployments [O_ISAC_200]. Affected layers include reference-stack governance, interoperability with standard DSP pipelines, provenance policy, and audit pathways for deployment claims [O_ISAC_200]. Evidence reports open-source hooks, compatibility pathways, incompatibility risk in some infrastructures, and a realistic time-varying model gap, indicating that governed validation traces remain necessary for portability interpretation [O_ISAC_200].

### Math Anchor

Selected form: readiness-gated deployment utility.

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

The discussion now shifts from domain-wise challenge clusters to a cross-domain capstone synthesis layer.

## VIII-F. Capstone Dependency Synthesis and Prioritized Research Agenda

Section VIII-F acts as a capstone synthesis rather than a new Axis-2 domain: it summarizes cross-domain dependency coverage and then organizes a prioritized agenda linked to those dependencies. Table VIII-F-1 is derived from linkage counts across Sections V-VII and should be read as an observational co-linkage summary, not as a causal graph. Existing IVLCS/ISAC evidence indicates that shared sensing and communication resources can tighten coordination pressure [O_ISAC_049], repeatable calibration routines can remain restrictive when transfer is attempted across settings [O_ISAC_107], and power-limited OWC integration can add bandwidth and noise-management pressure [O_ISAC_133]. In the observed linkage summary, domains A and C appear as the densest linkage hubs, while domain E appears underlinked; VIII-F treats that pattern as a linkage-gap and governance observation, not as a statement of lower importance.

Table VIII-F-1. Dependency Coverage Summary across A-E domains (observational linkage counts).

| domain | linked_section5 | linked_section6 | linked_section7 | status |
|---|---:|---:|---:|---|
| standardization_interoperability | 55 | 55 | 55 | covered |
| channel_modeling_evaluation | 54 | 54 | 54 | covered |
| hardware_scalability_efficiency | 25 | 25 | 25 | covered |
| security_privacy_reliability | 18 | 18 | 18 | covered |
| deployment_convergence_roadmap | 0 | 0 | 0 | isolated |

Table VIII-F-2 converts these observations into an organizational shortlist. The cite-key-supported agenda items remain explicit: F-AG01 aligns interoperability and evaluation baselines under the A/C hotspot [O_ISAC_133], F-AG02 keeps A/B/C resource contention in scope [O_ISAC_049], F-AG03 retains conservative wording for a hybrid security-evaluation thread that may require a unified analytical framework [O_ISAC_156], and F-AG04 retains conservative wording for prototype-to-scale coordination under calibration overhead [O_ISAC_107]. These rows remain tied to their source papers and are not generalized beyond the cited evidence.

The remaining rows preserve coverage-derived agenda slots rather than new literature claims. F-AG05 is carried by the lower but nonzero D coverage signal, F-AG06 explicitly addresses the E-domain linkage gap as a convergence and governance problem, and F-AG07 preserves balanced A-E coverage under limited editorial or research bandwidth. Accordingly, P1, P2, and P3 are organizational labels assigned from observed co-linkage density, summary coverage, and FLAGGED-evidence concentration rather than scientific rankings. The prioritization anchor below is included only as a review-level organizational guide, and the outcome cluster in Fig. VIII-1 should be read in the same bounded sense.

Within this capstone layer, any optical RIS, ORIS, or optical phased array implication remains a forward-looking architectural hook for future integration under RQ3, not a sixth challenge domain and not a direct claim of deployment readiness.

Table VIII-F-2. Prioritized Research Agenda (dependency-aware, evidence-linked, non-causal synthesis).

| agenda_id | title | linked_domains | linkage_rationale | representative_support | priority_tier | wording_mode |
|---|---|---|---|---|---|---|
| F-AG01 | Align interoperability rules with evaluation baselines | A,C | A/C hotspot across Sections V-VII | O_ISAC_133; dense interoperability-evaluation linkage | P1 | normal |
| F-AG02 | Reduce multi-slot resource contention in optical ISAC | A,B,C | shared A/B/C resource pressure across Sections V-VII | O_ISAC_049; joint sensing-communication resource coupling | P1 | normal |
| F-AG03 | Hybrid stacks may require a unified security-evaluation framework | A,C,D | A/C/D cross-layer security linkage | O_ISAC_156; hybrid security-evaluation coupling | P1 | conservative |
| F-AG04 | Prototype calibration may require hardware-scaling coordination | A,B,D | A/B/D prototype-to-scale calibration pressure | O_ISAC_107; calibration overhead in scaling-oriented settings | P2 | conservative |
| F-AG05 | Sustain lower-coverage security and reliability threads | D | persistent but lower-density D-domain continuity signal | targeted D-domain continuity signal | P2 | normal |
| F-AG06 | Strengthen deployment-convergence evidence through governance-aware integration studies | A,C,E | underlinked E-domain convergence pathway | deployment-convergence underlinkage in the current linkage summary | P2 | normal |
| F-AG07 | Maintain balanced cross-domain research coverage | A,B,C,D,E | cross-domain balance under finite research bandwidth | aggregate cross-domain coverage balance | P3 | normal |

### VIII-F Math Anchor (Review-Level Organizational Prioritization Scaffold)

\[
\begin{aligned}
\max_{x \in \{0,1\}^N}\quad & \sum_{i=1}^{N} w_i x_i \\
\text{s.t.}\quad & \sum_{i=1}^{N} c_i x_i \le B,\\
& \mathrm{cover}_d(x) \ge z_d,\quad d \in \{A,B,C,D,E\}_{\mathrm{selected}},\\
& \mathrm{risk\_flag}(x) \le R_{\max}.
\end{aligned}
\]

Here, `x_i` marks whether agenda item `i` is prioritized; `w_i` is an evidence or dependency weight drawn from the VIII-F linkage summary; `c_i` is a symbolic editorial or research bandwidth cost; `cover_d` is a domain-coverage indicator; and `risk_flag` limits the concentration of FLAGGED-evidence items. This is a review-level organizational guide, not a validated scientific law and not a claim of deployment certainty.

The section then closes with an alignment and traceability audit layer across the established domains.

## VIII-G. Cross-Section Alignment and Evidence-Consistency Check

Section VIII-G functions as a capstone cross-section alignment audit rather than a new Axis-2 challenge domain. It checks whether strict Section VIII challenge evidence is reflected in the upstream linkage signals inherited from Sections V, VI, and VII. Under the fixed A-E challenge inventory, this layer serves as a traceability and evidence-consistency check across the established domains, not as an extension of the domain set.

The alignment summary shows a fully matched pattern for the A-D domains: `standardization_interoperability`, `hardware_scalability_efficiency`, `channel_modeling_evaluation`, and `security_privacy_reliability` each have equal strict and upstream counts, with `unmatched_strict_count = 0`. For `deployment_convergence_roadmap`, both strict and upstream counts remain zero, so the row should be read only as a zero/underlinked evidence state within the present summary. The alignment indicates continuity across the existing challenge inventory and does not show completeness of the review, maturity of a domain, or any importance ranking.

Table VIII-G-1. Cross-section alignment summary between strict Section VIII evidence and upstream linkage signals.

| domain | strict_evidence_count | linked_any_upstream_count | unmatched_strict_count | interpretation |
|---|---:|---:|---:|---|
| standardization_interoperability | 55 | 55 | 0 | perfectly aligned |
| hardware_scalability_efficiency | 25 | 25 | 0 | perfectly aligned |
| channel_modeling_evaluation | 54 | 54 | 0 | perfectly aligned |
| security_privacy_reliability | 18 | 18 | 0 | perfectly aligned |
| deployment_convergence_roadmap | 0 | 0 | 0 | zero-row; no upstream linkage currently evidenced |

Methodological caution remains necessary when the alignment layer is interpreted beyond aggregate continuity. In the present locked summary, no populated paper-level discrepancy examples are available for any domain. Accordingly, VIII-G can verify whether strict Section VIII evidence remains connected to upstream signals at the aggregate level, but it cannot support paper-level discrepancy narratives in the current version of the alignment layer.

For final roadmap integration, VIII-G therefore strengthens traceability, not causal inference, and it should remain a continuity check across the established challenge inventory rather than a completeness or maturity claim.

Table VIII-G-2. Availability of paper-level discrepancy examples in the present alignment summary.

| domain | populated_discrepancy_example | interpretation_limit |
|---|---|---|
| standardization_interoperability | no | aggregate continuity only |
| hardware_scalability_efficiency | no | aggregate continuity only |
| channel_modeling_evaluation | no | aggregate continuity only |
| security_privacy_reliability | no | aggregate continuity only |
| deployment_convergence_roadmap | no | zero-row remains aggregate-only |

