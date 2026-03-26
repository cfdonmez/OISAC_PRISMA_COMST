\[
\max_{u}\ \alpha\,R_{\mathrm{comm}}(u;s) - (1-\alpha)\,J_{\mathrm{sense}}(u;s)
\]
\[
R_{\mathrm{comm}}(u;s)=R(u;s),\qquad
J_{\mathrm{sense}}(u;s)=\varepsilon_{\tau_0}^{2}(u;s)
\]
\[
s=(m_{\mathrm{veh}},\ell_{\mathrm{LoS}})
\]

Here `u` denotes a conventional vehicular O-ISAC control policy over shared optical links, including transmission-parameter adaptation and sensing-processing adaptation. The scenario vector `s` is restricted to evidenced deployment factors only: vehicular driving mobility `m_veh` and LoS visibility regime `\ell_LoS` in outdoor optical links. Communication-plane utility is modeled by achievable data rate `R_comm`, while sensing-plane loss is modeled by ToF-CRB cost `J_sense`; `\alpha` tunes their joint trade-off for automotive transportation deployments without introducing ORIS/OPA phase-control variables [O_ISAC_055] [O_ISAC_164].
