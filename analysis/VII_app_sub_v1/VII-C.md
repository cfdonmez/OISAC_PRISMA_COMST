VII-C. Automotive Transportation

Within Section VII, the VII-C vertical is locked to automotive transportation, where O-ISAC is deployed in moving-road contexts that require concurrent optical connectivity and environment-aware operation in the same workflow [O_ISAC_003] [O_ISAC_164]. The evidence base is deployment-facing: reported systems are framed around V2V and V2X exchanges, optical source-receiver pairing in driving scenes, and co-present sensing and communication functions under mobility and outdoor illumination variability [O_ISAC_003] [O_ISAC_060] [O_ISAC_164]. Across this scope, representative optical motifs include taillight/headlight signaling, camera-based OCC reception, and FSO-style vehicular relay links, with metrics reported in separate sensing and communication planes [O_ISAC_003] [O_ISAC_055] [O_ISAC_164].

Scenario 1: Autonomous-vehicle ISAC-OW V2V deployment.  
Scenario vector s1 includes two autonomous-vehicle ISAC-OW nodes, vehicular relative motion, and Gamma-Gamma turbulence regimes over an optical wireless LiDAR plus communication setup [O_ISAC_060]. Sensing plane: the study reports a LiDAR ranging estimate of 100.011 m for a 100 m reference target condition [O_ISAC_060]. Communication plane: BER versus SNR is reported under different turbulence strengths, with spread-spectrum processing improving BER behavior relative to the non-spread baseline [O_ISAC_060]. Dominant component label is Conventional because the deployment evidence is built on QPSK-DSSS signaling, vehicular optical nodes, and LiDAR ranging flow, without explicit OPA or ORIS hardware claims [O_ISAC_060].

Scenario 2: Outdoor OCC-based V2X deployment with exposure-time tuning.  
Scenario vector s2 captures driving V2V/V2I/I2V exchange, LED-based vehicular/infrastructure emitters, camera reception, and outdoor LOS/NLOS coexistence with illumination variation [O_ISAC_164]. Sensing plane: normalized sensing gain Ge is used, and the reported trend shows reduced sensing gain with higher relative motion or scene complexity [O_ISAC_164]. Communication plane: normalized communication gain Gc is used for data-bearing optical components and is analyzed versus communication frequency and exposure-time settings [O_ISAC_164]. Dominant component label is Conventional because the architecture is explicitly formulated around headlights/taillights/traffic lights and onboard or surveillance cameras, with no explicit OPA or ORIS hardware statement [O_ISAC_164].

Scenario 3: V2V VLC deployment with mono-static and bi-static sensing modes.  
Scenario vector s3 is described by front-rear V2V spacing, unilateral taillight VLC emission, and mode-dependent propagation composition across mono-static and bi-static setups [O_ISAC_003]. Sensing plane: target/background sensing behavior is reported through target-channel received-power ratio and RMS delay-spread trends versus distance [O_ISAC_003]. Communication plane: the study is deployment-relevant for V2V optical link support, but no explicit communication KPI is reported as a standalone comm-plane metric [O_ISAC_003]. Dominant component label is Conventional, evidenced by vehicle-scene ray-tracing construction and LED taillight signaling without explicit OPA or ORIS components [O_ISAC_003].

Scenario 4: Vehicular-network FSO ISAC link with LFM-CPM waveform.  
Scenario vector s4 includes vehicular two-node relay context, LoS optical-link assumption, and atmospheric-turbulence-aware FSO channel modeling [O_ISAC_055]. Sensing plane: ToF-oriented sensing metrics are explicitly reported through CRB and RMSE descriptors [O_ISAC_055]. Communication plane: BER and achievable data rate are explicitly reported in the same framework [O_ISAC_055]. Dominant component label is Conventional because the implementation path uses laser-diode IM/DD transmission, photodiode reception, and shared waveform processing, without explicit OPA or ORIS hardware statement [O_ISAC_055].

A compact vehicular deployment anchor consistent with validated VII-C evidence is

```latex
\max_{u}\ \alpha\,R_{\mathrm{comm}}(u;s) - (1-\alpha)\,J_{\mathrm{sense}}(u;s)
```
```latex
R_{\mathrm{comm}}(u;s)=R(u;s),\qquad J_{\mathrm{sense}}(u;s)=\varepsilon_{\tau_0}^{2}(u;s),\qquad s=(m_{\mathrm{veh}},\ell_{\mathrm{LoS}})
```

Here, u denotes conventional vehicular O-ISAC control policy over shared optical resources, including transmission-parameter adaptation and sensing-processing adaptation [O_ISAC_055] [O_ISAC_164]. The scenario vector s is restricted to evidenced mobility and LoS visibility descriptors for automotive deployment settings [O_ISAC_055] [O_ISAC_164]. Communication-plane utility is represented by achievable data-rate behavior, while sensing-plane loss is represented by ToF-CRB cost, preserving explicit metric-plane separation [O_ISAC_055] [O_ISAC_164].

Key takeaways for this vertical:
- VII-C evidence is consistently deployment-centered around V2V or V2X operation, with optical communication and sensing co-present in vehicular scenes [O_ISAC_003] [O_ISAC_060] [O_ISAC_164].
- Communication-plane reporting ranges from explicit BER/data-rate metrics to normalized communication gain, while sensing-plane reporting spans ranging estimates, CRB/RMSE, normalized sensing gain, and channel-sensing descriptors [O_ISAC_003] [O_ISAC_055] [O_ISAC_060] [O_ISAC_164].
- The four-scenario set covers OCC-style camera reception, VLC taillight channels, and FSO vehicular links under mobility and outdoor optical propagation effects [O_ISAC_003] [O_ISAC_055] [O_ISAC_164].
- A joint trade-off anchor is defensible in this vertical because both planes are explicitly evidenced, enabling conservative deployment-level synthesis with comm-plane and sensing-plane terms kept distinct [O_ISAC_055] [O_ISAC_164].
