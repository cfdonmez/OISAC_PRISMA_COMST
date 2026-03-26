### VII-F Supplementary Evidence

#### Context and Takeaways
- Cite-key: `O_ISAC_074`  
  Excerpt: "telecom fibers facilitates the potential applications such as distributed acoustic sensor (DAS) to efficiently monitor health of the network infrastructure"  
  Locator: `I. INTRODUCTION`, line 17.
- Cite-key: `O_ISAC_187`  
  Excerpt: "low-Earth-orbit (LEO) satellite networks."  
  Locator: `Abstract`, line 7.

#### Scenario 1 (smart_infrastructure)
- Cite-key: `O_ISAC_074`  
  Excerpt: "50 GBaud 16-QAM transmission and vibration sensing with 1m resolution over 10.4km fiber"  
  Locator: `IV. CONCLUSIONS`, line 54.

#### Scenario 2 (space_satellite)
- Cite-key: `O_ISAC_187`  
  Excerpt: "sensing range resolution is better than 0.146 meters with a probability larger than 86%"  
  Locator: `Abstract`, line 7.
- Cite-key: `O_ISAC_187`  
  Excerpt: "For back-to-back communication with rate of 29.99 Mbps, the BER remains under the 7% pre-FEC threshold"  
  Locator: `6. Conclusion`, line 402.

#### Scenario 3 (automotive_transportation)
- Cite-key: `O_ISAC_164`  
  Excerpt: "vehicles exchange information with other vehicles (V2V) or infrastructure (V2I/I2V)."  
  Locator: `2.1. OC-ISAC Architecture`, line 55.
- Cite-key: `O_ISAC_143`  
  Excerpt: "can be applied to other applications ... such as vehicular network, underwater robots, human computer interactions."  
  Locator: `I. INTRODUCTION`, line 35.

#### Scenario 4 (indoor_environments)
- Cite-key: `O_ISAC_011`  
  Excerpt: "The simulation considers a space size of 5m*5m*3m indoor space."  
  Locator: `III.A. Simulation Setup`, line 105.
- Cite-key: `O_ISAC_011`  
  Excerpt: "BER vs. transmitted SNR for different modulation orders."  
  Locator: `III.B. Simulation Results`, line 145.
- Cite-key: `O_ISAC_011`  
  Excerpt: "distance measurement RMSE vs. symbol number."  
  Locator: `III.B. Simulation Results`, line 153.
- Cite-key: `O_ISAC_108`  
  Excerpt: "source layout optimization ... communication bit error rate (BER) and sensing mean squared error (MSE)."  
  Locator: `I. INTRODUCTION`, line 31.

#### Math Anchor
- Anchor-B evidence source: summary artifacts only (no additional paper-metric constraint in the anchor equations).
- Decision trace source: `analysis/VII_app_sub_v1_micro/VII-F_MATH_ANCHOR_DECISION.md`.

#### Summary-Artifact Evidence (Consolidated)
- `section7F_summary.json`:
  - `$.n_total_papers = 221`
  - `$.n_unique_micro_domains = 48`
  - `$.n_multi_macro_domain_papers = 157`
- `s7f_macro_med_cov.csv` rows used:
  - row 2: `smart_infrastructure,204,12,103`
  - row 3: `indoor_environments,81,10,65`
  - row 4: `automotive_transportation,104,7,76`
  - row 5: `underwater_harsh,23,4,16`
  - row 6: `space_satellite,34,5,17`
- `s7f_micro_dom_cnts.csv` rows used:
  - row 2: `industrial_manufacturing,66`
  - row 3: `vehicular,61`
  - row 4: `indoor_positioning,57`
  - row 5: `6g_networks,48`
- `section7F_transfer_map.csv` rows used:
  - hybrid structure: rows 3, 15, 25, 32, 36
  - wireless_vlc structure: rows 13, 23, 30, 39
  - cabled_fibre structure: rows 2, 14, 24, 31, 35
  - wireless_fso structure: rows 9, 20, 27, 34, 37
- `section7F_paper_macro_map.csv` rows used for incidence sanity:
  - row 1 schema
  - rows 12 (`O_ISAC_011`), 108 (`O_ISAC_108`), 143 (`O_ISAC_143`), 164 (`O_ISAC_164`), 173 (`O_ISAC_187`), 191 (`O_ISAC_252`)
