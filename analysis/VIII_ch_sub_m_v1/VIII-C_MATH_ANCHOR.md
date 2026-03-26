# VIII-C Math Anchor

$$
\max_{\pi}\; U_{\mathrm{eval}}(\pi)
$$
$$
\text{s.t.}\; \pi \in \Pi_{\mathrm{contract}},\quad
\Pi_{\mathrm{contract}} = \{\kappa_{\mathrm{cond}},\,\gamma_{\mathrm{geom}},\,\mu_{\mathrm{metric}},\,\delta_{\mathrm{prov}}\}
$$

This anchor maps VIII-C to benchmark-contract constrained evaluation by forcing each result protocol to carry channel-condition tags and scenario-geometry descriptors before cross-paper comparison, which directly follows weather-conditioned channel behavior and geometry-dependent reporting contexts [O_ISAC_005, O_ISAC_327]. The term $\mu_{\mathrm{metric}}$ is comm-plane specific in this run and binds BER-capacity definitions to evaluation conditions (for example distance-conditioned reporting), while sensing-plane metrics are intentionally not instantiated because direct sensing-plane evidence is not present in the locked Run4 evidence subset [O_ISAC_381]. The term $\delta_{\mathrm{prov}}$ encodes measurement-campaign and dataset/testbed provenance so that the documented need for a standard model becomes an enforceable contract item rather than a narrative recommendation [O_ISAC_327].
