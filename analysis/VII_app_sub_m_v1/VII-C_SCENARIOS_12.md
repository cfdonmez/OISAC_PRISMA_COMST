### Scenario 1
1) Scenario title
Autonomous-vehicle ISAC-OW V2V deployment under turbulence. [O_ISAC_060]

2) Scenario vector s
s = {distance: R0 = 100 m; relative mobility: two autonomous vehicles (ISAC-OW#1/#2); LoS/NLoS: none explicitly reported; weather/visibility: weak/moderate/strong Gamma-Gamma turbulence; lighting modality: optical wireless LiDAR with QPSK-DSSS unified waveform}. [O_ISAC_060]

3) Sensing task + sensing metric
Sensing task: LiDAR ranging of the vehicular object; sensing-plane metric: ranging result 100.011 m for reference range R0 = 100 m. [O_ISAC_060]

4) Communication task + comm metric
Communication task: data transmission between vehicle ISAC-OW nodes; comm-plane metric: BER versus SNR under turbulence, with spread-spectrum BER improvement. [O_ISAC_060]

5) Dominant component label + evidence justification
Dominant component label: Conventional. Evidence: the deployment is implemented with vehicle ISAC-OW nodes, QPSK-DSSS processing, and LiDAR ranging. [O_ISAC_060]

6) Representative works
O_ISAC_060

### Scenario 2
1) Scenario title
Outdoor OCC-based V2X deployment with exposure-time co-optimization. [O_ISAC_164]

2) Scenario vector s
s = {distance: no fixed road-link distance in the outdoor V2X model; testbed camera distance = 0.3 m; relative mobility: driving V2V/V2I/I2V exchanges and sensing-side speed 1.75 m/s; LoS/NLoS: LOS and NLOS both present; weather/visibility: dynamic illumination and wet-road/backlighting reflections; lighting modality: headlights/taillights/traffic-signal LEDs with camera reception}. [O_ISAC_164]

3) Sensing task + sensing metric
Sensing task: camera-based environmental perception; sensing-plane metric: normalized sensing gain Ge, reduced by higher fxv and scene complexity. [O_ISAC_164]

4) Communication task + comm metric
Communication task: OCC-based V2X information transfer; comm-plane metric: normalized communication gain Gc versus fc and exposure time, with gain reduction at higher fc. [O_ISAC_164]

5) Dominant component label + evidence justification
Dominant component label: Conventional. Evidence: the architecture explicitly uses vehicle/infrastructure LEDs and onboard/surveillance cameras for V2V, V2I, and I2V links. [O_ISAC_164]

6) Representative works
O_ISAC_164
