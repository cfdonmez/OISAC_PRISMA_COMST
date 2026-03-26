### VIII-A. Standardization and Interoperability Challenges

VIII-A (Standardization and Interoperability Challenges) frames the `standardization_interoperability` domain as a deployment-facing bottleneck rather than a closed technical problem. Evidence from representative studies indicates that interoperability pressure already appears where sensing and communication must co-exist on shared infrastructure. In SMART subsea settings, standardization is explicitly tied to joint-task-force framing and integrated sensing-communication operation over telecommunication cables [O_ISAC_220]. In optical transport support for ISAC, architecture-level interconnection across RAN, MEC, and SDN-controlled transport highlights practical interoperability requirements spanning radio, transport, and sensing workflows [O_ISAC_025]. A hardware-centric ISAC transceiver review further indicates that emerging standardization efforts and early commercial prototypes are moving the field from isolated demonstrations toward implementation-oriented integration [O_ISAC_161]. Accordingly, this subsection treats `standardization_interoperability` as an open issue focused on interface alignment, cross-domain control consistency, and implementation-ready integration boundaries, with cautious interpretation of any upstream bridge evidence because Section V/VI/VII links are INDIRECT by design.

#### Challenge Case 1: Standards Vocabulary and Reference-Model Divergence
**Failure mode.** Without aligned standardization vocabulary and reference-model assumptions, implementations can expose incompatible expectations for integrated sensing-communication operation, which limits cross-system comparability and deployment transferability [O_ISAC_220] [O_ISAC_161].

**Affected interfaces/layers.** The most exposed points are control-plane terminology alignment, sensing-metadata semantics, timing/synchronization assumptions, and transceiver-to-orchestration interface consistency across multi-domain deployments [O_ISAC_220] [O_ISAC_161].

**Evidence snippet summary.** Evidence indicates that SMART-oriented integrated operation is explicitly tied to a standardized framing under a joint task-force context [O_ISAC_220]. A hardware-centric transceiver survey also reports intensified industry activity around standardization and prototype transition, indicating that interface consistency has shifted from conceptual discussion to implementation pressure [O_ISAC_161].

**Practical implication for roadmap.** The roadmap should treat reference-model and terminology alignment as a prerequisite gating item for credible cross-platform evaluation in this domain [O_ISAC_220] [O_ISAC_161].

#### Challenge Case 2: Cross-Domain Interoperability Friction in Transport-Supported ISAC
**Failure mode.** When communication and sensing flows are jointly carried but interoperability assumptions differ across transport, orchestration, and sensing-processing stages, routing and capacity decisions can become brittle under operational variability [O_ISAC_025].

**Affected interfaces/layers.** Friction appears at data-plane IQ stream handling, control-plane orchestration and SDN policy exchange, sensing metadata exchange, and timing/latency coordination between access and aggregation segments [O_ISAC_025].

**Evidence snippet summary.** A transport-oriented ISAC architecture shows explicit RAN-core/MEC interconnection requirements and a joint optimization workflow for communication-plus-sensing flows, indicating nontrivial multi-interface coupling [O_ISAC_025].

**Practical implication for roadmap.** Evidence indicates that interoperability profiling across joint sensing/communication transport workflows should remain a first-order roadmap risk item [O_ISAC_025].

#### Challenge Case 3: PtMP Branch-Attribution and Measurement-Semantics Misalignment
**Failure mode.** In point-to-multipoint access deployments, sensing pipelines can fail to provide unambiguous branch-level attribution when monitoring assumptions are not aligned with deployment topology and loss conditions, weakening interoperability at the measurement-contract level [O_ISAC_104].

**Affected interfaces/layers.** The main pressure points are sensing-metadata semantics (which branch/event a stream represents), evaluation/reporting contracts for anomaly attribution, and control-layer interpretation of branch-specific sensing quality under splitter loss [O_ISAC_104].

**Evidence snippet summary.** INDIRECT evidence indicates that PtMP structure is described as a practical challenge for fiber-based sensing in deployed access infrastructure, and that splitter-induced link-budget loss can drive sensing failure conditions [O_ISAC_104].

**Practical implication for roadmap.** The roadmap should treat branch-attribution semantics and reporting consistency as a first-class interoperability checkpoint before cross-vendor scaling in access scenarios [O_ISAC_104].

#### Challenge Case 4: Sensing-Payload Formatting and DSP-Compatibility Contract Gaps
**Failure mode.** When sensing payload placement and frequency-allocation assumptions are not explicitly aligned with communication signal structure, interoperability can break at receiver processing boundaries and low-interference joint operation becomes fragile [O_ISAC_220].

**Affected interfaces/layers.** Critical interfaces include data-plane sensing-payload formatting, frequency/timing alignment between sensing joints and shore transceivers, and receiver-side DSP interface contracts used for joint demodulation [O_ISAC_220].

**Evidence snippet summary.** Evidence indicates that SMART-oriented dense integration must address precise allocation of sensing information into communication frequency blanks, and that communication-compatible DSP is treated as a compatibility condition [O_ISAC_220].

**Practical implication for roadmap.** Roadmap staging should prioritize explicit format-and-DSP conformance checks for sensing payload interoperability in dense integrated links [O_ISAC_220].

#### Math Anchor (`standardization_interoperability`)
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

#### Key Takeaways and Research Priorities
- Interoperability risk in VIII-A is not only a standards-label issue; it also appears in branch-level sensing semantics and attribution contracts under PtMP operation [O_ISAC_104].
- Format compatibility between sensing payloads and communication-oriented DSP flows is a deployment-facing interoperability dependency in dense integrated links [O_ISAC_220].
- Evidence indicates that evaluation/reporting contracts and signal-format contracts should be prioritized separately because they fail at different interfaces [O_ISAC_104] [O_ISAC_220].
- working hypothesis: a compact conformance profile coupling branch-attribution semantics with DSP-interface checks may reduce cross-platform integration ambiguity.
