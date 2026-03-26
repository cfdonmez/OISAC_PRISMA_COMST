\[
\max_{u}\; \alpha\,R_{\mathrm{comm}}(u;s) - (1-\alpha)\,J_{\mathrm{sense}}(u;s)
\]
\[
\text{s.t. } Q_{\mathrm{comm}}(u;s) \geq Q_{\min},\; S_{\mathrm{sal}}(u;s) \geq S_{\min},\; T_{\mathrm{res}}(u;s) \leq T_{\max},\; u \in \mathcal{U}(s).
\]

Here, `u` denotes a conventional underwater/subsea O-ISAC policy over communication-format selection, sensing-demodulation settings, and scheduling. The scenario state `s` captures underwater_harsh deployment context, including subsea telecommunication-cable operation and environment-coupled sensing conditions. Comm-plane terms (`R_comm`, `Q_comm`) map to reported SMART-link communication performance, while sensing-plane terms (`J_sense`, `S_sal`, `T_res`) map to salinity-sensitivity and temperature-resolution evidence in deep-ocean and subsea monitoring studies [O_ISAC_220], [O_ISAC_027]. This anchor intentionally uses conventional cross-layer control variables and avoids unverified ORIS or OPA phase-control parameters.
