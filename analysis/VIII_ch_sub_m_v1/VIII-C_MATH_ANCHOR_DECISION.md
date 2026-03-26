# VIII-C Run4 Decision Memo

1. Axis lock: `channel_modeling_evaluation`.
2. Option-A support check: SUPPORTED via environment-shift evidence (`adverse weather` and `realistic channel model`) [O_ISAC_005].
3. Option-B support check: SUPPORTED via `measurement campaigns`, `standard model is needed`, and comm-plane `BER/capacity` evaluation language [O_ISAC_327, O_ISAC_381].
4. Selected option: **Option-B (benchmark-contract constrained evaluation)**.
5. Supported term list for Option-B: channel-condition descriptors, scenario-geometry descriptors, comm-plane metric definitions, dataset/testbed provenance.
6. Objective mapping: maximize evaluation utility under a minimum reporting contract.
7. Constraint mapping: contract membership enforces cross-paper comparability and reproducibility fields.
8. Why Option-B over Option-A: explicit standard-model and campaign-provenance language is directly present in excerpts; this is stronger than robustness-only framing.
9. Why Option-A is weaker for Run4 anchor: it captures domain shift but does not directly encode reporting-contract enforceability.
10. Decision outcome: proceed with Option-B anchor using locked keys only {O_ISAC_005, O_ISAC_327, O_ISAC_381}.
