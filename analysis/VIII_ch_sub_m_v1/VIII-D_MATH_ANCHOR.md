### VIII-D Math Anchor (Option-1: risk-constrained service utility)

\[
\begin{aligned}
\max_{u=(u_{\mathrm{auth}},u_{\mathrm{mon}},u_{\mathrm{priv}})} \quad & U_{\mathrm{service}}(u) \\
\text{s.t.} \quad & R_{\mathrm{int}}(u) \le \varepsilon_{\mathrm{int}}, \\
& L_{\mathrm{priv}}(u) \le \varepsilon_{\mathrm{priv}}, \\
& A_{\mathrm{auth}}(u) \ge \tau_{\mathrm{auth}}.
\end{aligned}
\]

Evidence indicates that service utility is exposed when network interruption events occur and when falsification risks degrade trustworthiness, so `R_int` is linked to interruption and integrity-monitoring risk under SDN alerting and service-adjustment workflows [O_ISAC_041; O_ISAC_145]. Evidence also reports confidential-data leakage concern and a model-update exchange rule, which directly supports the privacy-leakage constraint `L_priv` and the `u_priv` policy component [O_ISAC_039]. For authentication feasibility, evidence indicates that dense heterogeneous connectivity raises dynamic key-management burden while authentication and integrity remain central security processes, supporting `A_auth` and the `u_auth` policy component [O_ISAC_156]. The monitoring component `u_mon` maps to real-time warning, alert-routing, and service-adjustment evidence [O_ISAC_041]. All thresholds are kept symbolic (`ε_int`, `ε_priv`, `τ_auth`) because no bound values are fixed in the extracted source text.
