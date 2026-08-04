# OISAC Phase-F S1-S7 publication-ready numeric summary

**QA status:** PASS
**Locked source SHA-256:** `c1b3b89789c6ed3e20da5a6283e480875c1913e21af88ff59ac747a6aa949348`
**Authoritative Phase-E crosswalk SHA-256:** `41d6f8f574bdd0d6eba04806b2930ade8fa1d3d56e28b083de3d56bb13e7d122`
**Denominator:** 206 unique study clusters
**Claim governance:** The inclusive governed universe contains 8,234 non-quarantined records, but this includes 31 context-only metrics. Primary synthesis therefore uses 8,203 claims: 3,020 evidence, 4,779 metric, and 404 tradeoff claims. The 31 context-only metrics and 72 quarantined claims are excluded from primary numeric synthesis. Within the primary set, 1,505 claims meet the explicit conditional/guardrail definition and are shown as a subset, not as unconditional evidence.

## Reading rule

Modality, validation maturity, open-data status, open-code status, and 6G relevance come only from the frozen Phase-E `per_study_crosswalk`; Phase F does not reclassify them. These fields and study status are mutually exclusive and each reconciles to 206. A mismatch with Phase E is a blocking QA failure. Integration mechanisms, validation types, enabling technologies, and application domains are multi-label: their category totals can exceed 206 because one study can contribute to several categories. For integration, enabling technology, and application domain, `other` is used only when a study has no recognized category on that axis; unmatched co-occurring tokens remain audit-only. Each of these axes still covers all 206 studies. Metric-domain/family and tradeoff tables report both claim counts and unique-study counts; summing unique-study counts across categories double-counts multi-topic studies.

## S1 — Optical modality

| Modality | Studies | % of 206 |
| --- | --- | --- |
| photonic_THz | 69 | 33.5 |
| fiber | 56 | 27.2 |
| VLC_LiFi | 38 | 18.4 |
| FSO | 31 | 15.0 |
| hybrid_optical | 9 | 4.4 |
| other_optical | 3 | 1.5 |

## S2 — Integration mechanisms

| Mechanism | Studies | % of 206 |
| --- | --- | --- |
| shared_waveform | 113 | 54.9 |
| shared_hardware | 117 | 56.8 |
| shared_optical_carrier | 49 | 23.8 |
| shared_link_or_channel | 87 | 42.2 |
| shared_resource_allocation | 118 | 57.3 |
| joint_design_or_optimization | 72 | 35.0 |
| shared_application_scenario | 46 | 22.3 |
| mixed | 3 | 1.5 |
| other | 0 | 0.0 |
| unclear | 0 | 0.0 |

## S3 — Metric domains

| Metric domain | Studies | Primary metric claims | Conditional subset |
| --- | --- | --- | --- |
| sensing | 203 | 1816 | 505 |
| communication | 194 | 1328 | 296 |
| joint | 158 | 870 | 260 |
| implementation | 64 | 476 | 28 |
| system | 11 | 104 | 0 |
| energy | 5 | 25 | 23 |
| scenario | 5 | 12 | 0 |
| waveform | 5 | 11 | 4 |
| channel | 4 | 9 | 0 |
| tradeoff | 4 | 5 | 3 |
| illumination | 3 | 9 | 1 |
| optical | 3 | 8 | 0 |
| resource | 3 | 5 | 0 |
| security | 2 | 40 | 0 |
| machine_learning | 2 | 31 | 0 |
| component | 2 | 8 | 8 |
| network | 2 | 2 | 0 |
| simulation | 2 | 2 | 0 |
| power_transfer | 1 | 4 | 0 |
| algorithm | 1 | 3 | 3 |
| control | 1 | 3 | 0 |
| mobility | 1 | 2 | 0 |
| operations | 1 | 2 | 0 |
| baseline | 1 | 1 | 1 |
| optimization | 1 | 1 | 0 |
| processing | 1 | 1 | 0 |
| resource_performance | 1 | 1 | 0 |

The complete 2,000+ family vocabulary is retained in `s3_metric_families.csv`; no semantic collapse of source-specific metric families was imposed. Both S3 tables exclude the 31 context-only metric rows as well as quarantined rows.

## S4 — Derived tradeoff families

| Tradeoff family | Studies | Primary claims | Conditional subset |
| --- | --- | --- | --- |
| bandwidth_spectrum_or_resource_allocation | 71 | 95 | 90 |
| power_energy_or_dynamic_range | 64 | 90 | 81 |
| communication_reliability_vs_sensing_quality | 48 | 59 | 55 |
| rate_resolution | 39 | 46 | 41 |
| rate_accuracy_or_localization | 33 | 40 | 39 |
| waveform_hardware_or_complexity | 20 | 21 | 21 |
| rate_range_or_coverage | 16 | 21 | 18 |
| other_joint_tradeoff | 15 | 19 | 18 |
| qualitative_or_partial_general | 9 | 11 | 8 |
| security_or_resilience_tradeoff | 1 | 1 | 1 |
| synergy_or_non_antagonistic_coupling | 1 | 1 | 1 |

## S5 — Validation maturity

| Maturity tier | Phase-E label | Studies | % of 206 |
| --- | --- | --- | --- |
| 2 | simulation_or_numerical | 32 | 15.5 |
| 3 | enhanced_simulation_or_dataset | 18 | 8.7 |
| 4 | laboratory_experiment_or_proof_of_concept | 78 | 37.9 |
| 5 | controlled_prototype | 66 | 32.0 |
| 6 | field_trial_or_deployment | 12 | 5.8 |

### Open data

| Data status | Studies | % of 206 |
| --- | --- | --- |
| unavailable_or_NR | 145 | 70.4 |
| on_request | 41 | 19.9 |
| open | 13 | 6.3 |
| NA | 7 | 3.4 |

### Open code/model

| Code/model status | Studies | % of 206 |
| --- | --- | --- |
| unavailable_or_NR | 197 | 95.6 |
| on_request | 7 | 3.4 |
| partial_components | 1 | 0.5 |
| NA | 1 | 0.5 |

## S6 — Enabling technologies

| Technology | Studies | % of 206 |
| --- | --- | --- |
| OFDM | 56 | 27.2 |
| beamforming | 13 | 6.3 |
| MIMO | 7 | 3.4 |
| coherent_optics | 64 | 31.1 |
| photonic_integration | 20 | 9.7 |
| photonic_THz_generation | 68 | 33.0 |
| ML_AI | 20 | 9.7 |
| RIS_ORIS | 2 | 1.0 |
| OPA | 11 | 5.3 |
| digital_twin | 2 | 1.0 |
| fiber_DAS | 22 | 10.7 |
| FMCW | 66 | 32.0 |
| other | 19 | 9.2 |

## S6 — Application domains

| Application | Studies | % of 206 |
| --- | --- | --- |
| 6G_access | 100 | 48.5 |
| indoor_positioning | 25 | 12.1 |
| vehicular | 41 | 19.9 |
| industrial | 34 | 16.5 |
| security | 26 | 12.6 |
| environment_monitoring | 55 | 26.7 |
| underwater | 2 | 1.0 |
| aerospace | 20 | 9.7 |
| datacenter | 4 | 1.9 |
| optical_access_network | 32 | 15.5 |
| healthcare | 8 | 3.9 |
| smart_infrastructure | 41 | 19.9 |
| other | 15 | 7.3 |

## S7 — 6G relevance

| 6G relevance | Studies | % of 206 |
| --- | --- | --- |
| direct | 138 | 67.0 |
| inferred | 64 | 31.1 |
| weak | 1 | 0.5 |
| not_applicable | 3 | 1.5 |

## Restrictions and provenance boundary

Study use status is 175 `survey_ready` and 31 `survey_ready_with_claim_restrictions`, reconciling to 206. Independent human verification status is `not_documented` for all 206 studies. These outputs therefore must be described as AI-assisted/user-delegated survey-scope adjudication, not as dual-independent-reviewer verification.

The five exclusive S1/S5/S7 dimensions are copied per study from Phase E and are marked `phase_e_frozen_crosswalk` in `normalization_audit.csv`. Phase-F normalization of the preserved multi-label fields is deterministic and fully exposed there. Source-explicit `other` tokens that accompany a recognized category are marked `other_explicit_token_audit_only` and do not inflate the `other` study count; true fallback studies remain `fallback_other_or_unclear`. Fine-grained long-tail fragments remain visible after broad mapping. None of these audit buckets silently admits a quarantined claim. The locked Phase-D workbook and Phase-E crosswalk were read only and were not changed.
