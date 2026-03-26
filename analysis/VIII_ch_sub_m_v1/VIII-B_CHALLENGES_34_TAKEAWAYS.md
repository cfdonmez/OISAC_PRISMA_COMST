### Challenge Case 3 — Integration-Level Hardware Co-Design and Baseband Cost Escalation

1) **Challenge title.** Integration-level hardware co-design and baseband cost escalation under `hardware_scalability_efficiency`.

2) **Failure mode.** Evidence indicates that optimizing one shared transceiver for sensing and communication is highly challenging because requirements conflict at architecture level [O_ISAC_161]. Evidence also indicates that high mobility and severe path loss can push beam-steering demands beyond economically viable conventional antenna designs [O_ISAC_142].

3) **Affected layers/resources.** The dominant impact is hardware-plane: antenna/RF architecture choices that require continuous trade-off balancing during development [O_ISAC_161]. A second impact is baseband resource pressure, where reused OFDM signals may introduce additional processing complexity and cost [O_ISAC_162].

4) **Evidence snippet summary.** Representative texts report that many architectural/electrical parameters require careful balancing [O_ISAC_161], and that integration level governs extra baseband cost exposure [O_ISAC_162]. Related evidence also reports unresolved analogue front-end drift effects in practical operation [O_ISAC_162].

5) **Practical implication for roadmap.** The VIII-B roadmap should treat integration-level complexity accounting as a hardware gate before scale-out to path-loss-constrained deployments [O_ISAC_161][O_ISAC_142][O_ISAC_162].

### Challenge Case 4 — Beam-Control Scalability, FLOP Growth, and Latency Envelope Limits

1) **Challenge title.** Beam-control scalability, FLOP growth, and latency envelope limits in large-array operation.

2) **Failure mode.** Evidence indicates that communication-plane beamforming overhead becomes large in highly mobile cells [O_ISAC_134]. Evidence also indicates that conventional delay-line beam control can require substantial switching/control burden as steering granularity tightens [O_ISAC_171].

3) **Affected layers/resources.** The primary impacts are hardware-plane beam-control complexity and compute-plane FLOP/latency budgets in multimodal beam prediction pipelines [O_ISAC_134][O_ISAC_171]. Representative measurements report millisecond-level processing latency and model-stage complexity concentration [O_ISAC_134].

4) **Evidence snippet summary.** Representative studies report communication-overhead pressure [O_ISAC_134], MMT-dominated complexity and measurable processing latency [O_ISAC_134], and beam-control complexity reduction with scalable frequency-comb steering [O_ISAC_171].

5) **Practical implication for roadmap.** The VIII-B roadmap should co-design steering granularity, model complexity, and hardware budget jointly, rather than scaling them independently [O_ISAC_134][O_ISAC_171].

### Key Takeaways & Research Priorities

- Build integration-level complexity ledgers that jointly track RF architecture constraints and baseband-cost escalation before deployment decisions [O_ISAC_161][O_ISAC_162].
- Prioritize hardware-plane beam-control schemes that avoid switch-count explosion while preserving fine steering granularity for large arrays [O_ISAC_171].
- Add calibration-aware front-end drift handling as a first-class hardware requirement for sustained field performance [O_ISAC_162].
- Co-design multimodal pipeline FLOPs, latency envelopes, and beam-pruning strategy to reduce communication-plane overhead without destabilizing beam quality [O_ISAC_134].
