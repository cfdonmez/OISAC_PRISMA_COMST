# VII-E Math Anchor Decision Memo

1. Candidate comm-plane items from RUN2/RUN3: throughput or bitrate, BER, EVM; candidate sensing-plane item: range resolution.
2. Candidate deployment constraints from RUN2/RUN3: LEO satellite context, shared multi-beam payload topology, and pointing or jitter mentions.
3. SUPPORTED comm-plane evidence: "A 29.99-Mbps rate communication is achieved" and "BER is maintained below the 7% pre-forward error correction threshold" (`O_ISAC_187`, `Abstract:7`, `1. Introduction:23`).
4. SUPPORTED sensing-plane evidence: range-resolution reporting is explicit in both `O_ISAC_187` and `O_ISAC_195` (`Abstract:7`, `3.2. Verification test...:120`).
5. SUPPORTED deployment evidence: LEO satellite context (`O_ISAC_187`, `1. Introduction:13`) and shared multi-beam architecture (`O_ISAC_195`, `2. Framework...:43`).
6. UNSUPPORTED for this anchor: explicit pointing-jitter or ISL-graph constraints with anchor-level equations in the opened evidence set for selected keys.
7. Decision: Option-1 is selected because at least one comm-plane metric and one sensing-plane metric are both directly supported.
8. Anchor safety rule: use qualitative QoS thresholds (`\epsilon_{comm}`, `\epsilon_{sense}`) and conventional policy variables only; no ORIS or OPA variables are introduced.
