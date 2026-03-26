# VIII-B Math Anchor (RUN4)

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
