## VIII-B - hardware_scalability_efficiency
### Context
Section VIII-B defines `hardware_scalability_efficiency` as a cross-cutting bottleneck because hardware-plane burdens accumulate even when integrated waveforms improve joint operation [O_ISAC_035][O_ISAC_162]. Evidence indicates that complexity growth is driven by extra baseband processing, filtering, and coordination overhead as integration depth increases [O_ISAC_162]. Representative works also report power/SWaP pressure at edge hardware, including sub-watt energy budgets with delays beyond tens of milliseconds for complex processing pipelines [O_ISAC_093]. A further friction point is implementation scaling in beamforming hardware: fine steering granularity is achievable, but control-system and fabrication burdens increase with larger arrays and tighter precision requirements [O_ISAC_171]. Communication-plane outcomes (rate/BER) and sensing-plane outcomes (resolution/accuracy) are relevant but secondary in this context; the primary blocker is hardware-plane feasibility under scaling, power, and implementation constraints [O_ISAC_093][O_ISAC_162][O_ISAC_171].
### Challenge Cases 1-2
### Challenge Case 1 — Front-End Co-Design Scalability Bottleneck

1) **Failure mode.** Evidence indicates that independently operated sensing and communication stacks increase hardware complexity, cost, and spectrum inefficiency [O_ISAC_237]. Evidence also indicates that bistatic sensing support can become infeasible on common communication receivers because required analogue FMCW hardware is unavailable [O_ISAC_237].

2) **Affected layers/resources.** The primary impact is hardware-plane: RF front-end sharing, receiver-chain composition, and implementation burden in sensing-aided estimation and interference-cancellation pipelines [O_ISAC_237]. Evidence further indicates that reducing RF hardware complexity and simplifying the FMCW receiver remains a central implementation pressure [O_ISAC_035].

3) **Evidence snippet summary.** Representative texts report both baseline hardware-duplication burden and explicit computational stacks for channel estimation, interference cancellation, and sensing algorithms [O_ISAC_237]. Complementary evidence reports simplified receiver design as a hardware-efficiency target [O_ISAC_035].

4) **Practical implication for roadmap.** For VIII-B, evidence indicates an implementation bottleneck where hardware simplification must keep pace with added receiver processing blocks [O_ISAC_237][O_ISAC_035].

### Challenge Case 2 — Edge Energy-Latency Hardware Ceiling

1) **Failure mode.** Evidence indicates that edge deployments face strict hardware feasibility limits because energy budgets are often below 1 watt and processing delays can exceed 50 milliseconds [O_ISAC_093].

2) **Affected layers/resources.** The primary impacts are hardware-plane power/SWaP budgets, edge inference latency budgets, and terminal DSP burdens [O_ISAC_093][O_ISAC_095]. Evidence also indicates increased computational complexity for a single ORIS unit during localization [O_ISAC_112].

3) **Evidence snippet summary.** Representative evidence reports sub-watt edge budgets and delay escalation for complex tasks [O_ISAC_093], and reports that FOE-free processing is used to reduce terminal complexity and power consumption [O_ISAC_095]. Additional evidence reports higher localization-stage complexity for ORIS-aided processing [O_ISAC_112].

4) **Practical implication for roadmap.** Communication-plane and sensing-plane metric gains remain conditional on hardware-plane energy and latency envelopes in edge and terminal implementations [O_ISAC_093][O_ISAC_095][O_ISAC_112].
### Challenge Cases 3-4
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
### Math Anchor
## Selected Form
Option-2 (resource-constrained performance optimization)

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
### Key Takeaways & Research Priorities

- Build integration-level complexity ledgers that jointly track RF architecture constraints and baseband-cost escalation before deployment decisions [O_ISAC_161][O_ISAC_162].
- Prioritize hardware-plane beam-control schemes that avoid switch-count explosion while preserving fine steering granularity for large arrays [O_ISAC_171].
- Add calibration-aware front-end drift handling as a first-class hardware requirement for sustained field performance [O_ISAC_162].
- Co-design multimodal pipeline FLOPs, latency envelopes, and beam-pruning strategy to reduce communication-plane overhead without destabilizing beam quality [O_ISAC_134].
