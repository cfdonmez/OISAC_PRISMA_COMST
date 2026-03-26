\[
\max_{u}\ \alpha\,R_{\mathrm{comm}}(u;s)\;-\;(1-\alpha)\,J_{\mathrm{sense}}(u;s)
\]
\[
R_{\mathrm{comm}}(u;s) = -\mathrm{BER}(u;s), \qquad
J_{\mathrm{sense}}(u;s)=\mathrm{MSE}_{\mathrm{pos}}(u;s)
\]
\[
s=(g_{\mathrm{room}},\rho_{\mathrm{user}})
\]

Here `u` denotes indoor O-ISAC operational controls, including waveform selection, LED radiation and power-allocation settings, and phase-level adaptation policy that jointly governs communication delivery and localization service in shared infrastructure. The scenario vector `s` is restricted to evidenced indoor descriptors, namely room geometry `g_room` and active user density `\rho_user`, because these parameters shape propagation conditions, interference, and multi-user load in practical VLC deployments. Communication-plane quality is encoded through BER in `R_comm`, while sensing-plane quality is encoded through coordinate-position MSE in `J_sense`, matching reported indoor evaluations [O_ISAC_108] [O_ISAC_388].
