# VIII-A Math Anchor (`standardization_interoperability`)

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
