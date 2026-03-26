## VIII-C - channel_modeling_evaluation

### Context
Evidence indicates that channel modeling and evaluation are foundational for O-ISAC credibility because conclusions are not transferable without validated propagation assumptions across environments and implementations [O_ISAC_005][O_ISAC_327]. Turbulence, pointing, and blockage factors remain a core bottleneck: weather-dependent attenuation and alignment-sensitive behavior can shift effective channel conditions across deployments [O_ISAC_005][O_ISAC_327]. NLoS geometry and intermittency are also unresolved, since multipath and scatterer-dependent effects require explicit modeling and estimation rather than fixed simplifications [O_ISAC_050]. Evaluation practice further needs metric-plane alignment: comm-plane indicators such as BER/capacity should be interpreted together with sensing-plane estimation outcomes, not in isolation [O_ISAC_381][O_ISAC_050]. Finally, benchmarking and reproducibility depend on consistent channel-model disclosure and measurement-campaign comparability, which remains an open issue for reliable cross-study roadmap decisions [O_ISAC_327].

### Challenge Cases 1-2
#### Challenge Case 1 - Weather-Conditioned Channel-Model Transferability Gap

1) **Challenge title.** Weather-conditioned channel-model transferability gap in O-ISAC evaluation.

2) **Failure mode.** Evidence indicates that adverse weather can materially change channel behavior, so assumptions tuned under one condition can fail under another condition [O_ISAC_005]. Evidence also indicates that sensing feedback is tied to the back-scattered signal relation with forward channel gain, creating model drift risk when this relation changes [O_ISAC_005].

3) **Affected interfaces/assumptions.** The most affected interfaces are atmospheric attenuation assumptions, back-scattered-feedback-to-channel-gain mapping, and scenario conditioning for channel-state estimation [O_ISAC_005].

4) **Evidence snippet summary.** Representative text reports that adverse weather reduces FSO link reliability and that evaluation is performed using a realistic channel model with climatic data [O_ISAC_005]. This indicates that portability of conclusions depends on environmental conditioning, not only algorithm selection [O_ISAC_005].

5) **Practical implication for roadmap.** The VIII-C roadmap should treat climate-conditioned model validation as a prerequisite before cross-scenario comparison claims [O_ISAC_005].

#### Challenge Case 2 - LOS/NLOS Decomposition and Scatterer-State Identifiability Gap

1) **Challenge title.** LOS/NLOS decomposition and scatterer-state identifiability gap in channel evaluation.

2) **Failure mode.** Evidence indicates that practical modeling must decouple LOS and NLOS paths and jointly estimate scattering-related states; otherwise, model mismatch remains likely under multipath conditions [O_ISAC_050].

3) **Affected interfaces/assumptions.** The key interfaces are LOS/NLOS decomposition assumptions, equivalent NLOS channel-state representation, and estimation burden in non-convex settings [O_ISAC_050].

4) **Evidence snippet summary.** Representative text reports an equivalent discrete channel remodeling method that decouples LOS and NLOS paths and a joint estimation strategy for scattering states [O_ISAC_050]. Conclusion text further indicates multipath-interference and random-fading sensitivity in evaluation [O_ISAC_050].

5) **Practical implication for roadmap.** The VIII-C roadmap should prioritize explicit reporting of decomposition assumptions and estimation scope before claiming robust cross-study comparability [O_ISAC_050].

### Challenge Cases 3-4
#### Challenge Case 3 - Comm-Plane Metric Interface Coupling Under Evaluation Conditions

1) **Challenge title.** Comm-plane metric interface coupling under evaluation conditions.

2) **Failure mode.** Evidence indicates that evaluation pipelines rely on comm-plane BER and comm-plane capacity outcomes, and these outcomes shift with transmission-distance settings [O_ISAC_381]. This creates a comparability risk when studies report metrics without a harmonized condition contract [O_ISAC_381].

3) **Affected assumptions/interfaces.** The affected interfaces are metric-definition choices, measurement-condition declarations, and channel-capacity interpretation boundaries across test distances and hardware capture constraints [O_ISAC_381].

4) **Evidence snippet summary.** Representative text reports BER-to-capacity evaluation and distance-conditioned BER/rate behavior [O_ISAC_381]. Additional text indicates capacity degradation with distance growth, reinforcing condition-sensitive evaluation outcomes [O_ISAC_381].

5) **Practical implication for roadmap.** The VIII-C roadmap should treat condition-tagged comm-plane reporting as mandatory before cross-paper ranking claims [O_ISAC_381].

#### Challenge Case 4 - Benchmark Contract Fragmentation Across Channel Modeling Studies

1) **Challenge title.** Benchmark contract fragmentation across channel modeling studies.

2) **Failure mode.** Evidence indicates that channel-modeling evidence is distributed across heterogeneous measurement campaigns, scenario types, and model families, reducing direct comparability across studies [O_ISAC_327]. Evidence also indicates that new technologies and applications introduce additional modeling challenges that invalidate static benchmark assumptions [O_ISAC_327].

3) **Affected assumptions/interfaces.** The affected interfaces are reporting contracts for channel-model class, measurement-campaign provenance, and framework compatibility for standardization-oriented evaluation [O_ISAC_327].

4) **Evidence snippet summary.** Representative text reports broad survey coverage of measurement campaigns and model families, and explicitly states that a standard VLC channel model is needed for 6G evaluation workflows [O_ISAC_327].

5) **Practical implication for roadmap.** The VIII-C roadmap should treat benchmark-contract normalization as a prerequisite for reproducible evidence aggregation [O_ISAC_327].

### Math Anchor
Selected form: Option-B (benchmark-contract constrained evaluation).

$$
\max_{\pi}\; U_{\mathrm{eval}}(\pi)
$$
$$
\text{s.t.}\; \pi \in \Pi_{\mathrm{contract}},\quad
\Pi_{\mathrm{contract}} = \{\kappa_{\mathrm{cond}},\,\gamma_{\mathrm{geom}},\,\mu_{\mathrm{metric}},\,\delta_{\mathrm{prov}}\}
$$

This anchor maps VIII-C to benchmark-contract constrained evaluation by forcing each result protocol to carry channel-condition tags and scenario-geometry descriptors before cross-paper comparison, which directly follows weather-conditioned channel behavior and geometry-dependent reporting contexts [O_ISAC_005, O_ISAC_327]. The term $\mu_{\mathrm{metric}}$ is comm-plane specific and binds BER-capacity definitions to evaluation conditions (for example distance-conditioned reporting), while sensing-plane metrics are intentionally not instantiated because direct sensing-plane evidence is not present in the locked evidence subset [O_ISAC_381]. The term $\delta_{\mathrm{prov}}$ encodes measurement-campaign and dataset/testbed provenance so that the documented need for a standard model becomes an enforceable contract item rather than a narrative recommendation [O_ISAC_327].

### Key Takeaways & Research Priorities

- Define an evaluation-contract minimum that records channel-model class plus measurement-campaign lineage before any cross-study synthesis step [O_ISAC_327].
- Require comm-plane metric declarations to be bound to measurement conditions in result tables to reduce hidden comparability drift [O_ISAC_381].
- Add a standard-framework compatibility field in benchmarks to align evidence with shared 6G evaluation baselines [O_ISAC_327].
- working hypothesis: a compact reporting card will reduce audit friction in Section VIII-C evidence integration.
