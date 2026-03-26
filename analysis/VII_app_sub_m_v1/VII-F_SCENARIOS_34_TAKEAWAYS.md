Scenario 3
1) Scenario title: Vehicular OC-ISAC camera links for cooperative road awareness (automotive_transportation).
2) Scenario vector s: Outdoor V2X setting with V2V and V2I/I2V exchange, mobility, and LOS plus reflected paths captured by vehicle or roadside cameras [O_ISAC_164].
3) Sensing task + sensing metric: Sensing-plane task is environmental perception; sensing metric is normalized sensing gain or contrast under exposure and mobility [O_ISAC_164].
4) Communication task + comm metric: Comm-plane task is OCC payload recovery on vehicular links; comm metric is normalized communication gain with BER-context analysis [O_ISAC_164].
5) Dominant component label + 1-sentence evidence justification: Conventional. The source presents LED-camera architecture and exposure optimization without explicit OPA, ORIS, or Hybrid hardware [O_ISAC_164].
6) Transfer hook (1 sentence; if not evidenced -> “working hypothesis” minimal): The localization plus OCC design is explicitly stated as applicable to vehicular networks, giving direct transfer evidence from drone deployment [O_ISAC_143].
7) Representative works: O_ISAC_164; O_ISAC_143.

Scenario 4
1) Scenario title: Indoor localization-plus-access deployment with distributed LEDs and cameras (indoor_environments).
2) Scenario vector s: Indoor geometry-defined deployment with distributed optical access points, LED/PD or LED/camera nodes, and LOS-centered propagation with reflected-light sensing [O_ISAC_011] [O_ISAC_108].
3) Sensing task + sensing metric: Sensing-plane task is indoor ranging and positioning; sensing metrics include distance-measurement RMSE and positioning MSE or RMSE [O_ISAC_011] [O_ISAC_108].
4) Communication task + comm metric: Comm-plane task is optical data delivery over OFDM or IM/DD pipelines; comm metric is BER versus transmitted SNR [O_ISAC_011] [O_ISAC_108].
5) Dominant component label + 1-sentence evidence justification: Conventional. These indoor works use source-layout optimization, beamforming, and signal processing but do not claim OPA, ORIS, or Hybrid dominance [O_ISAC_011] [O_ISAC_108].
6) Transfer hook (1 sentence; if not evidenced -> “working hypothesis” minimal): Working hypothesis: indoor source-layout and shared-intensity objectives can transfer to other dense distributed optical deployments [O_ISAC_108].
7) Representative works: O_ISAC_011; O_ISAC_108.

Key takeaways
- VII-F coverage supports these picks: automotive has 104 papers, indoor has 81, and vehicular and indoor_positioning have 61 and 57 (macro rows 3-4; micro rows 3-4).
- Transfer-map rows show shared medium structure across these macros, including hybrid and wireless_vlc entries, supporting deployment-level portability (transfer rows 15, 23, 25, 30).
- Across both scenarios, sensing-plane and comm-plane metrics remain explicitly separated: sensing-side gains or RMSE versus communication BER or gain descriptors [O_ISAC_164] [O_ISAC_011] [O_ISAC_108].
