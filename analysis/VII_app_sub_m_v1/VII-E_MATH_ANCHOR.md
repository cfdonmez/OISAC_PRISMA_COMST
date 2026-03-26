For the space_satellite vertical, we adopt a joint trade-off anchor with conventional space O-ISAC controls [O_ISAC_187], [O_ISAC_195]:

$$\max_{u\in\mathcal{U}(s)}\;\alpha R_{\mathrm{comm}}(u;s)-(1-\alpha)J_{\mathrm{sense}}(u;s)$$
$$\text{s.t. } \mathrm{BER}(u;s)\le\epsilon_{\mathrm{comm}},\quad \rho_{\mathrm{range}}(u;s)\le\epsilon_{\mathrm{sense}}$$
$$s=(\text{LEO satellite deployment context},\;\text{shared multi-beam ISAC payload topology})$$

Here, $u$ denotes a conventional policy bundle for waveform adaptation, link scheduling, and beam selection on shared space payload resources [O_ISAC_187], [O_ISAC_195]. The comm-plane term $R_{\mathrm{comm}}$ captures communication-rate utility under BER reliability control, while the sensing-plane term $J_{\mathrm{sense}}$ captures range-resolution quality [O_ISAC_187], [O_ISAC_195]. The scenario vector $s$ is restricted to excerpt-supported deployment attributes only, namely LEO satellite context and multi-beam payload architecture [O_ISAC_187], [O_ISAC_195].
