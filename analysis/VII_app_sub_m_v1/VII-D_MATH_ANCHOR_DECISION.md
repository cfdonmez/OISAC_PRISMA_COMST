# VII-D RUN4 Decision (Math Anchor)

## D1) Candidate Metric/Constraint Pool from Prior VII-D Runs
| item | plane | source in prior runs | D2 validation status | evidence label |
|---|---|---|---|---|
| 20 GBaud DP-QAM16 transmission | comm-plane | `VII-D_SCENARIOS_12.md` Scenario 2 | SUPPORTED | supports `R_comm` |
| Q factor improvement (0.2 dB) | comm-plane | `VII-D_SCENARIOS_12.md` Scenario 2 | SUPPORTED | supports `Q_comm` |
| Salinity sensitivity (0.192 nm/‰) and RI sensitivity (1200.7 nm/RIU) | sensing-plane | `VII-D_SCENARIOS_34_TAKEAWAYS.md` Scenario 4 | SUPPORTED | supports `J_sense` and `S_sal` |
| Temperature sensing resolution (0.0625°C) | sensing-plane | `VII-D_SCENARIOS_12.md` Scenario 2 | SUPPORTED | supports `T_res` |
| Subsea telecommunication cable setting | deployment state | `VII-D_CONTEXT.md`, `VII-D_SCENARIOS_12.md` | SUPPORTED | supports `s` |

## D2) Validation Notes
- All listed supported items have direct excerpts with locators in `VII-D_MATH_ANCHOR_supp.md`.
- No OPA/ORIS-specific control variable is required by the validated excerpt set.

## D3) Anchor Form Selection
- **Selected form: Option-1 (Joint trade-off)**

## D4) Decision Memo (Audit, 8 lines)
1. Comm-plane evidence is explicit for throughput-linked operation and communication quality in SMART subsea deployment (`20 GBaud`, `Q factor improvement`) from `O_ISAC_220`.
2. Sensing-plane evidence is explicit for salinity performance (`1200.7 nm/RIU`, `0.192 nm/‰`) from `O_ISAC_027`.
3. A second sensing-plane metric (`0.0625°C` temperature resolution) is directly reported in `O_ISAC_220`.
4. Subsea deployment state is explicit via telecommunication-cable monitoring wording in `O_ISAC_220`.
5. Because both planes have direct metric support, the evidence threshold for Option-1 is met.
6. Option-2 would be unnecessarily conservative under the current evidence strength.
7. The anchor therefore uses a weighted comm-versus-sensing objective with explicit QoS constraints on both planes.
8. Variables stay conventional and deployment-grounded; no ORIS/OPA phase-control variable is introduced.
