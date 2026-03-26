### Scenario 3
1) Scenario title
V2V VLC ISAC deployment with mono-static and bi-static sensing modes. [O_ISAC_003]

2) Scenario vector s
s = {distance: mono-static about 4 m and bi-static about 5-10 m; mobility/relative velocity: front-rear V2V spacing d; LoS/NLoS: both; weather/visibility: none explicitly reported; lighting modality: unilateral LED taillight VLC}. [O_ISAC_003]

3) Sensing task + sensing metric
Sensing task: target/background channel sensing; sensing-plane metrics: target-channel received-power ratio and RMS DS trends versus distance. [O_ISAC_003]

4) Communication task + comm metric
Communication task: V2V optical link support in the ISAC channel; comm-plane metric: none explicitly reported. [O_ISAC_003]

5) Dominant component label + 1-sentence evidence justification
Dominant component label: Conventional. Evidence: the study uses vehicle scenarios, LED taillight emission, and ray-tracing construction, with no OPA/ORIS mention. [O_ISAC_003]

6) Representative works: 1–3 cite keys
O_ISAC_003

### Scenario 4
1) Scenario title
Vehicular-network FSO ISAC deployment using LFM-CPM over LoS links. [O_ISAC_055]

2) Scenario vector s
s = {distance: Device-A to Device-B distance D = 200 m; mobility/relative velocity: two-device vehicular relay context; LoS/NLoS: LoS assumed; weather/visibility: Gamma-Gamma turbulence and scintillation; lighting modality: laser-diode IM/DD transmission with photodiode reception}. [O_ISAC_055]

3) Sensing task + sensing metric
Sensing task: ToF-based distance measurement; sensing-plane metrics: CRB for ToF estimation and RMSE for sensing. [O_ISAC_055]

4) Communication task + comm metric
Communication task: shared-waveform data demodulation at Device B; comm-plane metrics: BER and achievable data rate. [O_ISAC_055]

5) Dominant component label + 1-sentence evidence justification
Dominant component label: Conventional. Evidence: the model explicitly uses a Device-A/Device-B laser-photodiode IM/DD chain, with no OPA/ORIS mention. [O_ISAC_055]

6) Representative works: 1–3 cite keys
O_ISAC_055

### Key takeaways for this vertical
- Coverage spans two deployment motifs: V2V VLC channel-mode operation and vehicular-network FSO link operation. [O_ISAC_003] [O_ISAC_055]
- Sensing-plane reporting differs by modality: received-power-ratio/RMS DS in V2V VLC versus CRB/RMSE in FSO. [O_ISAC_003] [O_ISAC_055]
- Comm-plane reporting is explicit in FSO through BER and achievable-rate analysis, while the V2V VLC case reports no explicit comm metric. [O_ISAC_003] [O_ISAC_055]
