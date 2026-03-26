`standardization_interoperability` in VIII-A is instantiated below through two evidence-bound challenge cases.

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
