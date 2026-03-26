### Challenge Case 1 - Weather-Conditioned Channel-Model Transferability Gap

1) **Challenge title.** Weather-conditioned channel-model transferability gap in O-ISAC evaluation.

2) **Failure mode.** Evidence indicates that adverse weather can materially change channel behavior, so assumptions tuned under one condition can fail under another condition [O_ISAC_005]. Evidence also indicates that sensing feedback is tied to the back-scattered signal relation with forward channel gain, creating model drift risk when this relation changes [O_ISAC_005].

3) **Affected interfaces/assumptions.** The most affected interfaces are atmospheric attenuation assumptions, back-scattered-feedback-to-channel-gain mapping, and scenario conditioning for channel-state estimation [O_ISAC_005].

4) **Evidence snippet summary.** Representative text reports that adverse weather reduces FSO link reliability and that evaluation is performed using a realistic channel model with climatic data [O_ISAC_005]. This indicates that portability of conclusions depends on environmental conditioning, not only algorithm selection [O_ISAC_005].

5) **Practical implication for roadmap.** The VIII-C roadmap should treat climate-conditioned model validation as a prerequisite before cross-scenario comparison claims [O_ISAC_005].

### Challenge Case 2 - LOS/NLOS Decomposition and Scatterer-State Identifiability Gap

1) **Challenge title.** LOS/NLOS decomposition and scatterer-state identifiability gap in channel evaluation.

2) **Failure mode.** Evidence indicates that practical modeling must decouple LOS and NLOS paths and jointly estimate scattering-related states; otherwise, model mismatch remains likely under multipath conditions [O_ISAC_050].

3) **Affected interfaces/assumptions.** The key interfaces are LOS/NLOS decomposition assumptions, equivalent NLOS channel-state representation, and estimation burden in non-convex settings [O_ISAC_050].

4) **Evidence snippet summary.** Representative text reports an equivalent discrete channel remodeling method that decouples LOS and NLOS paths and a joint estimation strategy for scattering states [O_ISAC_050]. Conclusion text further indicates multipath-interference and random-fading sensitivity in evaluation [O_ISAC_050].

5) **Practical implication for roadmap.** The VIII-C roadmap should prioritize explicit reporting of decomposition assumptions and estimation scope before claiming robust cross-study comparability [O_ISAC_050].
