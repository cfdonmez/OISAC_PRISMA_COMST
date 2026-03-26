`standardization_interoperability` in VIII-A is further instantiated through Challenge Case 3, Challenge Case 4, and evidence-scoped takeaways.

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

### Key takeaways & research priorities
- Interoperability risk in VIII-A is not only a standards-label issue; it also appears in branch-level sensing semantics and attribution contracts under PtMP operation [O_ISAC_104].
- Format compatibility between sensing payloads and communication-oriented DSP flows is a deployment-facing interoperability dependency in dense integrated links [O_ISAC_220].
- Evidence indicates that evaluation/reporting contracts and signal-format contracts should be prioritized separately because they fail at different interfaces [O_ISAC_104] [O_ISAC_220].
- working hypothesis: a compact conformance profile coupling branch-attribution semantics with DSP-interface checks may reduce cross-platform integration ambiguity.
