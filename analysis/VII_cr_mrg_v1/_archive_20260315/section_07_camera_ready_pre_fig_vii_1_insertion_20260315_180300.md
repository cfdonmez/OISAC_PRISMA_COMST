## VII. Applications and Use Cases Across Domains

Section VII translates the application evidence pack into deployment-facing use cases while staying inside the classification and governance contracts fixed earlier in the manuscript. Whenever medium labels are used below, they inherit the Section IV normalized vocabulary, namely cabled fiber, FSO, VLC/LiFi, photonic-THz or terahertz proxy, and hybrid systems. Likewise, any OPA or ORIS mention remains contextual in the Section VI sense and is not used by itself to assign an application domain. Finally, any SNR-family quantity reported in this section is treated as a source-reported communication-plane variable unless the cited paper explicitly states an optical-plane model; no implicit OSNR-to-SNR conversion is implied.

Table VII-1. Application Portfolio Matrix (Representative Cases).

| Vertical (VII-A..VII-E) | Scenario motif (short) | Comm-plane metrics (comma-separated) | Sensing-plane metrics (comma-separated) | Dominant component (Conventional/OPA/ORIS/Hybrid) | Representative cite keys |
|---|---|---|---|---|---|
| VII-A | Outdoor V2V/UAV optical corridors | V2V transmission-quality behavior, throughput-oriented resource and trajectory control | received-power-ratio behavior, RMS delay-spread trends, FSO channel-gain estimation | Conventional | O_ISAC_003, O_ISAC_005 |
| VII-A | Cabled-fiber corridor DAS + coherent carriage | 50-60 GBaud 16-QAM, coexistence penalty | distributed vibration monitoring, 1 m spatial resolution, interference-fading suppression | Conventional | O_ISAC_038, O_ISAC_074 |
| VII-B | Retroreflective indoor VLC/LiFi localization | BER vs reported electrical-plane SNR | distance-measurement RMSE, positioning RMSE | Conventional | O_ISAC_011 |
| VII-B | Two-phase indoor LED O-AP deployment | BER gains (2.70 dB directionless; 63.35 dB directional) | coordinate MSE (including <10^-4 operating point) | Conventional | O_ISAC_108 |
| VII-C | Autonomous-vehicle ISAC-OW V2V | BER vs reported electrical-plane SNR under turbulence | LiDAR ranging estimate (100.011 m for 100 m reference) | Conventional | O_ISAC_060 |
| VII-C | Vehicular-network FSO ISAC link (LFM-CPM) | BER, achievable data rate | ToF-oriented CRB, RMSE | Conventional | O_ISAC_055 |
| VII-D | Secure underwater OWC link | BER reduction, secrecy-rate outcomes | environmental-state prediction MAE (0.008 PSU) | Conventional | O_ISAC_127 |
| VII-D | SMART subsea cable monitoring | 20 GBaud DP-QAM16 transmission, Q-factor gain | in-line temperature sensing resolution (0.0625°C) | Conventional | O_ISAC_220 |
| VII-E | LEO photonic O-ISAC payload | 29.99 Mbps, BER below 7% pre-FEC threshold at 500 kHz Doppler | range-resolution behavior better than 0.146 m | Conventional | O_ISAC_187 |
| VII-E | Multi-beam satellite payload | BER (8.15 × 10^-7), EVM (6.74%), 2.4 Gbps 16-QAM link | range resolution (14.9 cm), remote-sensing and imaging performance descriptors | Conventional | O_ISAC_195 |

### VII-A. Smart Infrastructure & Outdoor Urban Sensing-Communication

#### Context
Urban smart-infrastructure deployments use O-ISAC when the same optical platform must carry operational traffic while exposing environment and link state for control and supervision [O_ISAC_003] [O_ISAC_005] [O_ISAC_276]. Across representative studies, this vertical covers outdoor mobility corridors, metro and industrial cabled-fiber corridors, and live metropolitan access supervision, each with explicit sensing-plane and communication-plane reporting [O_ISAC_003] [O_ISAC_038] [O_ISAC_064] [O_ISAC_276].

#### Scenarios
Scenario 1: Outdoor mobility corridors with vehicular and UAV-assisted optical links.  
Scenario vector s1 includes V2V distance variation, mobility-driven geometry changes, and weather-dependent FSO attenuation [O_ISAC_003] [O_ISAC_005]. Sensing plane: target/background discrimination is reported through received-power-ratio behavior and RMS delay-spread trends in V2V operation, while backscattered light is used for FSO channel-gain estimation in UAV-assisted links [O_ISAC_003] [O_ISAC_005]. Communication plane: robust data delivery is evaluated through V2V transmission-quality behavior and throughput-oriented resource and trajectory control under backhaul limits [O_ISAC_003] [O_ISAC_005]. Dominant component label: Conventional (no ORIS or OPA explicitly evidenced), since the cited implementations describe VLC, FSO, RF transceiver and control designs without explicit ORIS or OPA components [O_ISAC_003] [O_ISAC_005]. Representative works are visible-light V2V channel characterization and mixed FSO-RF UAV trajectory optimization [O_ISAC_003] [O_ISAC_005].

Scenario 2: Cabled-fiber corridor sensing-communication for metro and industrial infrastructure.  
Scenario vector s2 is characterized by 10-10.4 km cabled-fiber spans and interference-fading behavior in Rayleigh backscatter traces [O_ISAC_038] [O_ISAC_074]. Sensing plane: distributed vibration monitoring is reported with 1 m spatial resolution and interference-fading suppression [O_ISAC_038] [O_ISAC_074]. Communication plane: coherent payload transport is demonstrated with 50-60 GBaud 16-QAM and limited coexistence penalty [O_ISAC_038] [O_ISAC_074]. Dominant component label: Conventional (no ORIS or OPA explicitly evidenced), because the evidence is based on coherent-fiber DSP and waveform processing without explicit ORIS or OPA hardware [O_ISAC_038] [O_ISAC_074]. Representative works include NOMA-based DAS coexistence and endogenous training-sequence reuse [O_ISAC_038] [O_ISAC_074].

Scenario 3: Metropolitan deployed-fiber supervision.  
Scenario vector s3 includes metropolitan deployed fibers, point-to-multipoint access topology, and splitter branch-overlap risk [O_ISAC_064] [O_ISAC_276]. Sensing plane: event observability is reported via direct magnitude readout in live XGS-PON tests, including a 4.5 dB event measured as 4.55 dB [O_ISAC_276]. Communication plane: downstream traffic tests report no baseline performance difference between regular and upgraded remote nodes in the tested setup [O_ISAC_276]. Dominant component label: Conventional (no ORIS or OPA explicitly evidenced), with evidence centered on deployed-fiber OTDR and coherent monitoring workflows [O_ISAC_064] [O_ISAC_276]. Representative works include metropolitan smart-city deployed-fiber studies and live XGS-PON supervision [O_ISAC_064] [O_ISAC_276].

Scenario 4: Outdoor FSO ranging-communication for vehicular or autonomous links.  
Scenario vector s4 reflects outdoor free-space geometry, line-of-sight dependence, and atmospheric-loss or turbulence exposure [O_ISAC_012] [O_ISAC_034]. Sensing plane: distance observability is evaluated through MSE or RMSE behavior and related ranging metrics [O_ISAC_012] [O_ISAC_034]. Communication plane: reliability and efficiency are reported through code-rate and BER behavior in multi-user optical ISAC evaluations [O_ISAC_012] [O_ISAC_034]. Dominant component label: Conventional (no ORIS or OPA explicitly evidenced), since the validated papers emphasize waveform and receiver-DSP design rather than ORIS or OPA components [O_ISAC_012] [O_ISAC_034]. Representative works include PC-FMCW optical ISAC and PSS-PPM optical ISAC [O_ISAC_012] [O_ISAC_034].

#### Math Anchor
A compact deployment anchor for this vertical is

```latex
\max_{u,\pi,T}\ \alpha R_{\mathrm{comm}}(u,\pi;s) - (1-\alpha) J_{\mathrm{sense}}(u,T;s)
```
```latex
\text{s.t.}\ \sum_{k=1}^{K} p_k \le P_{\mathrm{avg}},\quad 0 \le p_k \le P_m,\ \forall k,
```
```latex
\mathrm{BER}(u,\pi;s) \le \beta_{\mathrm{rel}}.
```

Here, u denotes waveform and link-adaptation settings and s denotes deployment state such as distance, load, and atmospheric condition [O_ISAC_034] [O_ISAC_048]. The communication plane is captured by `R_comm` and BER reliability, while the sensing plane is captured by `J_sense` as a ranging-error surrogate [O_ISAC_034] [O_ISAC_048]. The per-subcarrier cap `P_m` follows reported maximum normalized subcarrier-power allocation, and the BER bound is treated as a service reliability target with 10^-4 as an illustrative reported operating point rather than a universal fixed threshold [O_ISAC_034] [O_ISAC_048].

**Key takeaways and application priorities.**
- Outdoor O-ISAC behavior is strongly scenario-vector dependent across mobility, weather, and topology [O_ISAC_003] [O_ISAC_005] [O_ISAC_276].
- Fiber-corridor deployments can co-support vibration sensing and high-rate coherent communication under controlled coexistence design [O_ISAC_038] [O_ISAC_074].
- Live access supervision shows that sensing readout and communication continuity can be jointly maintained in tested point-to-multipoint operation [O_ISAC_276].
- Reported optical ISAC evaluations use reliability metrics such as BER and ranging-error metrics such as MSE or RMSE to keep communication-plane and sensing-plane assessment separable [O_ISAC_012] [O_ISAC_034].

### VII-B. Indoor Environments

#### Context
Indoor O-ISAC deployments are characterized by shared optical infrastructure that must deliver communication service while extracting environment- or user-state information in the same transceiver workflow [O_ISAC_011] [O_ISAC_030]. In this vertical, the evidence base covers two core motifs. The first is localization-oriented retroreflective VLC, where transmitted and reflected optical signals are reused to support indoor 3D positioning without splitting communication and sensing into separate platforms [O_ISAC_011]. The second is human-centric interaction in lamp-centered settings, where VLC-capable luminaires concurrently support gesture-aware control and data communication in occupied indoor spaces [O_ISAC_030]. Across these motifs, deployment evidence remains application-facing: communication continuity is reported while sensing tasks execute, and sensing outputs remain operationally tied to positioning or interaction functions [O_ISAC_011] [O_ISAC_030].

#### Scenarios
Scenario 1: Retroreflective indoor VLC/LiFi localization.  
Scenario vector s1 includes a 5 m x 5 m x 3 m room, four-LED transmitter geometry, and a PD/CCR retroreflective loop with cross-correlation delay estimation [O_ISAC_011]. Sensing plane: passive ranging and 3D localization are evaluated through distance-measurement RMSE and positioning RMSE behavior across receiver positions [O_ISAC_011]. Communication plane: the same platform reports BER versus a source-reported electrical-plane SNR variable under multiple OFDM modulation orders [O_ISAC_011]. Dominant component label is Conventional because the reported implementation is based on LEDs, PDs, and CCR reflection paths, without explicit OPA or ORIS hardware [O_ISAC_011].

Scenario 2: VLC-lamp human-centric interaction under concurrent traffic.  
Scenario vector s2 is defined by a VLC-capable desk lamp, ring-shaped multi-LED emission, co-located PD reception, and table-surface reflection variability during simultaneous gesture and traffic operation [O_ISAC_030]. Sensing plane: reflected-light gesture recognition is reported with accuracy above 90 percent in the evaluated baseline PTD region [O_ISAC_030]. Communication plane: uplink/downlink BER behavior is maintained during gesture activity, and prototype throughput reaches 220 kbps [O_ISAC_030]. Dominant component label is Conventional, with evidence grounded in LED arrays, PD sensing, analog amplification, and FPGA processing, again without explicit OPA or ORIS claims [O_ISAC_030].

Scenario 3: Two-phase indoor LED O-ISAC with distributed O-APs.  
Scenario vector s3 captures indoor room geometry W x L x H, circular ceiling O-AP placement, multi-device PD-array reception, and directionless-to-directional operation [O_ISAC_108]. Sensing plane: device-position estimation uses coordinate MSE as the explicit sensing metric, including reported sensing MSE below 10^-4 at the evaluated operating point [O_ISAC_108]. Communication plane: BER is the communication metric, with reported gains of 2.70 dB in directionless mode and 63.35 dB in directional mode against a separated baseline [O_ISAC_108]. Dominant component label is Conventional because the implementation evidence centers on LED O-APs, pinhole cameras, PD arrays, and collimating lenses rather than explicit OPA or ORIS hardware [O_ISAC_108].

Scenario 4: Indoor multi-user VLC-CDMA with optical complementary codes.  
Scenario vector s4 uses a 5 m x 5 m x 3 m room, ceiling LED arrays with four wavelengths, desktop receivers at 0.85 m, and LOS plus reflected paths [O_ISAC_388]. Sensing plane: this scenario does not report an explicit sensing KPI. Communication plane: BER is reported against a source-reported electrical-plane SNR variable, user count, and data rate, and BER degrades as user count increases because of multi-user interference [O_ISAC_388]. Dominant component label is Conventional because the architecture is described with LED arrays, optical filters, PD receivers, and OCC/OOC code structures without explicit OPA or ORIS hardware [O_ISAC_388].

#### Math Anchor
A compact indoor deployment anchor consistent with the validated evidence is

```latex
\min_{u}\ \alpha\,\mathrm{BER}(u;s) + (1-\alpha)\,\mathrm{MSE}_{\mathrm{pos}}(u;s)
```
```latex
s=(g_{\mathrm{room}},\rho_{\mathrm{user}})
```

Here, u denotes indoor control variables such as resource allocation and waveform adaptation policy over the shared communication-sensing optical stack [O_ISAC_108] [O_ISAC_388]. The scenario vector s is restricted to evidenced deployment descriptors, namely room geometry and user density/load, both directly tied to reported indoor propagation and multi-user behavior [O_ISAC_108] [O_ISAC_388]. Communication-plane quality is represented by BER, while sensing-plane quality is represented by position-coordinate MSE, preserving strict metric-plane separation in deployment analysis [O_ISAC_108] [O_ISAC_388].

**Key takeaways and application priorities.**
- Indoor O-ISAC evidence consistently couples practical communication service with localization or gesture-driven sensing in shared lighting-centric infrastructure [O_ISAC_011] [O_ISAC_030].
- Scenario diversity spans both user-centric interaction and infrastructure-centric localization, and both report explicit communication-plane metrics while sensing is active [O_ISAC_011] [O_ISAC_030].
- Among later-stage indoor deployments, Scenario 3 provides explicit dual-plane metrics (BER and coordinate MSE), whereas Scenario 4 is communication-heavy with no explicit sensing KPI [O_ISAC_108] [O_ISAC_388].
- For deployment-level synthesis, BER and position MSE provide a conservative and evidenced cross-scenario objective pair under indoor geometry and user-density conditions [O_ISAC_108] [O_ISAC_388].

### VII-C. Automotive Transportation

#### Context
Within Section VII, the VII-C vertical is locked to automotive transportation, where O-ISAC is deployed in moving-road contexts that require concurrent optical connectivity and environment-aware operation in the same workflow [O_ISAC_003] [O_ISAC_164]. The evidence base is deployment-facing: reported systems are framed around V2V and V2X exchanges, optical source-receiver pairing in driving scenes, and co-present sensing and communication functions under mobility and outdoor illumination variability [O_ISAC_003] [O_ISAC_060] [O_ISAC_164]. Across this scope, representative optical motifs include taillight/headlight signaling, camera-based OCC reception, and FSO-style vehicular relay links, with metrics reported in separate sensing and communication planes [O_ISAC_003] [O_ISAC_055] [O_ISAC_164].

#### Scenarios
Scenario 1: Autonomous-vehicle ISAC-OW V2V deployment.  
Scenario vector s1 includes two autonomous-vehicle ISAC-OW nodes, vehicular relative motion, and Gamma-Gamma turbulence regimes over an optical wireless LiDAR plus communication setup [O_ISAC_060]. Sensing plane: the study reports a LiDAR ranging estimate of 100.011 m for a 100 m reference target condition [O_ISAC_060]. Communication plane: BER versus a source-reported electrical-plane SNR variable is reported under different turbulence strengths, with spread-spectrum processing improving BER behavior relative to the non-spread baseline [O_ISAC_060]. Dominant component label is Conventional because the deployment evidence is built on QPSK-DSSS signaling, vehicular optical nodes, and LiDAR ranging flow, without explicit OPA or ORIS hardware claims [O_ISAC_060].

Scenario 2: Outdoor OCC-based V2X deployment with exposure-time tuning.  
Scenario vector s2 captures driving V2V/V2I/I2V exchange, LED-based vehicular/infrastructure emitters, camera reception, and outdoor LOS/NLOS coexistence with illumination variation [O_ISAC_164]. Sensing plane: normalized sensing gain Ge is used, and the reported trend shows reduced sensing gain with higher relative motion or scene complexity [O_ISAC_164]. Communication plane: normalized communication gain Gc is used for data-bearing optical components and is analyzed versus communication frequency and exposure-time settings [O_ISAC_164]. Dominant component label is Conventional because the architecture is explicitly formulated around headlights/taillights/traffic lights and onboard or surveillance cameras, with no explicit OPA or ORIS hardware statement [O_ISAC_164].

Scenario 3: V2V VLC deployment with mono-static and bi-static sensing modes.  
Scenario vector s3 is described by front-rear V2V spacing, unilateral taillight VLC emission, and mode-dependent propagation composition across mono-static and bi-static setups [O_ISAC_003]. Sensing plane: target/background sensing behavior is reported through target-channel received-power ratio and RMS delay-spread trends versus distance [O_ISAC_003]. Communication plane: the study is deployment-relevant for V2V optical link support, but no explicit communication KPI is reported as a standalone comm-plane metric [O_ISAC_003]. Dominant component label is Conventional, evidenced by vehicle-scene ray-tracing construction and LED taillight signaling without explicit OPA or ORIS components [O_ISAC_003].

Scenario 4: Vehicular-network FSO ISAC link with LFM-CPM waveform.  
Scenario vector s4 includes vehicular two-node relay context, LoS optical-link assumption, and atmospheric-turbulence-aware FSO channel modeling [O_ISAC_055]. Sensing plane: ToF-oriented sensing metrics are explicitly reported through CRB and RMSE descriptors [O_ISAC_055]. Communication plane: BER and achievable data rate are explicitly reported in the same framework [O_ISAC_055]. Dominant component label is Conventional because the implementation path uses laser-diode IM/DD transmission, photodiode reception, and shared waveform processing, without explicit OPA or ORIS hardware statement [O_ISAC_055].

#### Math Anchor
A compact vehicular deployment anchor consistent with validated VII-C evidence is

```latex
\max_{u}\ \alpha\,R_{\mathrm{comm}}(u;s) - (1-\alpha)\,J_{\mathrm{sense}}(u;s)
```
```latex
R_{\mathrm{comm}}(u;s)=R(u;s),\qquad J_{\mathrm{sense}}(u;s)=\varepsilon_{\tau_0}^{2}(u;s),\qquad s=(m_{\mathrm{veh}},\ell_{\mathrm{LoS}})
```

Here, u denotes conventional vehicular O-ISAC control policy over shared optical resources, including transmission-parameter adaptation and sensing-processing adaptation [O_ISAC_055] [O_ISAC_164]. The scenario vector s is restricted to evidenced mobility and LoS visibility descriptors for automotive deployment settings [O_ISAC_055] [O_ISAC_164]. Communication-plane utility is represented by achievable data-rate behavior, while sensing-plane loss is represented by ToF-CRB cost, preserving explicit metric-plane separation [O_ISAC_055] [O_ISAC_164].

**Key takeaways and application priorities.**
- VII-C evidence is consistently deployment-centered around V2V or V2X operation, with optical communication and sensing co-present in vehicular scenes [O_ISAC_003] [O_ISAC_060] [O_ISAC_164].
- Communication-plane reporting ranges from explicit BER/data-rate metrics to normalized communication gain, while sensing-plane reporting spans ranging estimates, CRB/RMSE, normalized sensing gain, and channel-sensing descriptors [O_ISAC_003] [O_ISAC_055] [O_ISAC_060] [O_ISAC_164].
- The four-scenario set covers OCC-style camera reception, VLC taillight channels, and FSO vehicular links under mobility and outdoor optical propagation effects [O_ISAC_003] [O_ISAC_055] [O_ISAC_164].
- A joint trade-off anchor is defensible in this vertical because both planes are explicitly evidenced, enabling conservative deployment-level synthesis with comm-plane and sensing-plane terms kept distinct [O_ISAC_055] [O_ISAC_164].

### VII-D. Underwater and Harsh Maritime Deployments

#### Context
Section VII-D is scoped to the `underwater_harsh` vertical, where O-ISAC deployments couple underwater wireless links with subsea infrastructure monitoring [O_ISAC_127], [O_ISAC_220]. In this vertical, optical propagation and sensing quality are shaped by environmental dynamics such as salinity variation, temperature change, and turbulence-linked channel fluctuation [O_ISAC_127]. The same scope also includes submarine-cable settings where sensing information is integrated with ongoing communication services in shared physical infrastructure [O_ISAC_220]. Across the selected evidence base, this yields a deployment-oriented view with explicit comm-plane and sensing-plane roles: comm-plane operation sustains optical data transport in underwater or subsea conditions, while sensing-plane operation tracks environmental or physical-state variables needed for monitoring and adaptation [O_ISAC_127], [O_ISAC_220].

#### Scenarios 1-2
Scenario 1 corresponds to secure underwater optical wireless links, with scenario factors centered on salinity and temperature variation, turbulence-induced noise, and absorption/scattering-driven attenuation [O_ISAC_127]. In this case, sensing-plane functionality is represented by environmental-state prediction with reported MAE of 0.008 PSU, and comm-plane functionality is represented by secure optical transmission with reported BER reduction and secrecy-rate outcomes [O_ISAC_127]. In the same evidence, dominant implementation is kept as Conventional because the opened text does not explicitly establish ORIS-dominant control variables for this deployment [O_ISAC_127].

Scenario 2 captures SMART subsea monitoring over telecommunication submarine cables, with in-line sensing joints and shared-channel sensing-plus-communication operation [O_ISAC_220]. Here, the sensing-plane metric is in-line temperature sensing resolution at 0.0625°C, while the comm-plane metrics include 20 GBaud DP-QAM16 transmission and Q-factor gain under the integrated configuration [O_ISAC_220]. This scenario is also labeled Conventional for the same evidence-bound reason: explicit ORIS control parametrization is not provided in the opened deployment text [O_ISAC_220].

#### Scenarios 3-4
Scenario 3 extends coverage to coastal-event monitoring through submarine-fiber infrastructure, with deployment evidence tied to submarine cable routing, neritic-sea context, and operational sensing windows along the monitored link [O_ISAC_020]. Sensing-plane reporting includes ocean-wave and seismic-event observation, including microseism detection range and Mw-class event records in the cited deployment, whereas comm-plane reporting confirms coexistence with optical communication via wavelength-channel separation [O_ISAC_020].

Scenario 4 focuses on deep-ocean salinity monitoring at the 2 µm band, with evidenced factors including salinity-linked refractive-index range, depth-pressure relation in the marine environment, and low-crosstalk sensing behavior [O_ISAC_027]. Its sensing-plane metrics are explicit, including refractive-index and salinity sensitivities, while comm-plane reporting is conservative and framed as same-fiber coexistence potential between C-band communication and 2 µm sensing, with no standalone throughput or BER metric explicitly reported in the opened salinity-sensor evidence [O_ISAC_027]. As with the other cases, dominant implementation remains Conventional under the current evidence constraints [O_ISAC_027].

#### Math Anchor
To summarize the deployment-level trade space in VII-D, the subsection uses one joint comm-sensing anchor:

$$
\max_{u}\; \alpha R_{\mathrm{comm}}(u;s) - (1-\alpha) J_{\mathrm{sense}}(u;s)
$$
$$
\text{s.t. } Q_{\mathrm{comm}}(u;s) \geq Q_{\min},\; S_{\mathrm{sal}}(u;s) \geq S_{\min},\; T_{\mathrm{res}}(u;s) \leq T_{\max},\; u \in \mathcal{U}(s).
$$

Here, `u` denotes a conventional underwater/subsea policy over communication-format choice, sensing demodulation settings, and scheduling, and `s` captures underwater_harsh deployment state such as subsea cable context and environment-coupled sensing conditions [O_ISAC_220], [O_ISAC_027]. Comm-plane terms map to reported communication-side outcomes in SMART subsea operation, while sensing-plane terms map to reported salinity and temperature sensing outcomes in deep-ocean and subsea monitoring studies [O_ISAC_220], [O_ISAC_027].

**Key takeaways and application priorities.**
- VII-D evidence supports a unified underwater_harsh narrative that includes both underwater wireless links and submarine-cable monitoring deployments [O_ISAC_127], [O_ISAC_220], [O_ISAC_020].
- Comm-plane evidence is strongest in SMART-style subsea cable scenarios, where integrated transmission performance and channel-compatible sensing are jointly reported [O_ISAC_220].
- Sensing-plane evidence is strongest in deep-ocean salinity monitoring, where refractive-index and salinity sensitivities are explicitly quantified with deployment-relevant crosstalk context [O_ISAC_027].
- Across all four scenarios, a conservative Conventional dominant-component label is evidence-consistent because explicit ORIS control-variable formulations are not directly reported in the opened scenario texts [O_ISAC_127], [O_ISAC_220], [O_ISAC_020], [O_ISAC_027].

### VII-E. Space and Satellite Deployments

#### Context
Section VII-E is scoped to `space_satellite`, where O-ISAC is deployed in satellite-network settings rather than terrestrial access domains [O_ISAC_089], [O_ISAC_187]. In this scope, communication-plane operation is centered on optical inter-satellite connectivity and constellation relay behavior, while sensing-plane operation is integrated on the same payload chain to support remote observation and environment-aware functions [O_ISAC_089], [O_ISAC_195]. The evidence also covers LEO-oriented deployments and station-to-satellite links, so the subsection remains deployment-facing: it tracks how shared optical resources are organized in space topology, then separates what is measured for communication and what is measured for sensing [O_ISAC_089], [O_ISAC_137], [O_ISAC_187].

#### Scenarios 1-2
Scenario 1 is a spaceborne optical ISL backbone for constellation networking. Its scenario vector includes mesh-style ISL connectivity in the LEO layer, high relative motion among satellites, and APT-governed beam alignment [O_ISAC_089]. Sensing-plane evidence is not explicitly reported as a standalone KPI in this deployment framing. Communication-plane evidence is explicit through throughput-oriented inter-satellite transport and relay operation over laser ISLs [O_ISAC_089]. Dominant component is labeled Conventional because the opened text describes architecture, tracking, modulation, and networked ISL operation without explicit OPA- or ORIS-dominant control statements [O_ISAC_089].

Scenario 2 is a LEO photonic O-ISAC payload under dynamic Doppler conditions. Its scenario vector is supported by LEO deployment context, high mobility, and chirp-multiplexed shared-waveform operation designed for Doppler robustness [O_ISAC_187]. Sensing-plane reporting is explicit through range-resolution outcomes. Communication-plane reporting is also explicit through rate-oriented and BER-oriented outcomes under Doppler-shifted operation [O_ISAC_187]. Dominant component is again Conventional because the implementation evidence is presented as photonic transceiver and signal-chain design, not as explicit OPA- or ORIS-dominant reconfiguration hardware [O_ISAC_187].

#### Scenarios 3-4
Scenario 3 is ground-to-satellite SLR integration with simultaneous ranging and data transfer. Its scenario vector is deployment-specific: SLR station operation, orbital-parameter-assisted timing flow, and continuous event recording over a station-to-satellite optical path [O_ISAC_137]. Sensing-plane function is realized through propagation-time-based ranging with lidar-compatible event capture. Communication-plane function is realized through PPM or TR-PPM information transfer layered on the same optical pulse framework [O_ISAC_137]. The dominant component remains Conventional because the evidence describes time-tagging, ranging, and optical communication integration, without explicit OPA- or ORIS-dominant hardware claims [O_ISAC_137].

Scenario 4 is a multi-beam satellite payload for concurrent Earth-observation sensing and communication. Its scenario vector includes multi-beam synthesis on a shared payload, spatially separated beam roles, and shared processing architecture across sensing and communication channels [O_ISAC_195]. Sensing-plane reporting is explicit through remote-sensing and imaging performance descriptors. Communication-plane reporting is explicit through transmission-quality metrics on the communication beam path [O_ISAC_195]. This scenario is labeled Conventional because the opened deployment evidence focuses on photonic multi-beam integration and experimental validation, without explicit OPA- or ORIS-dominant labeling [O_ISAC_195].

#### Math Anchor
A compact space-deployment anchor consistent with the validated VII-E evidence is

$$
\max_{u\in\mathcal{U}(s)}\;\alpha R_{\mathrm{comm}}(u;s)-(1-\alpha)J_{\mathrm{sense}}(u;s)
$$
$$
\text{s.t. } \mathrm{BER}(u;s)\le\epsilon_{\mathrm{comm}},\quad \rho_{\mathrm{range}}(u;s)\le\epsilon_{\mathrm{sense}},\quad s=(s_{\mathrm{LEO}},s_{\mathrm{mb}})
$$

Here, `u` is a conventional policy bundle over waveform adaptation, scheduling, and beam assignment on shared space payload resources [O_ISAC_187], [O_ISAC_195]. The comm-plane terms are tied to rate and BER evidence, while sensing-plane terms are tied to range-resolution evidence, preserving strict plane separation [O_ISAC_187], [O_ISAC_195].

**Key takeaways and application priorities.**
- VII-E evidence is consistently deployment-grounded in space-satellite operation and spans ISL backbone networking, LEO Doppler-robust payloads, SLR integration, and multi-beam Earth-observation payloads [O_ISAC_089], [O_ISAC_137], [O_ISAC_187], [O_ISAC_195].
- Communication-plane reporting and sensing-plane reporting are both explicit in this vertical, but they are carried by different metric families and must remain separated in synthesis [O_ISAC_187], [O_ISAC_195].
- The scenario vectors are driven by topology and motion conditions that are directly evidenced in the opened texts, including mesh ISLs, LEO mobility context, station-to-satellite links, and multi-beam payload structure [O_ISAC_089], [O_ISAC_137], [O_ISAC_187], [O_ISAC_195].
- Under the current evidence contract, all four scenarios remain Conventional because no micro-part source text explicitly establishes OPA- or ORIS-dominant deployment control for VII-E [O_ISAC_089], [O_ISAC_137], [O_ISAC_187], [O_ISAC_195].

Consequently, VII-F synthesizes cross-domain coverage and transfer under the same evidence contract after the domain-specific verticals.


### VII-F. Cross-Domain Application Synthesis

#### Context
Section VII-F is treated as a cross-domain applications layer for O-ISAC rather than a single vertical slice. Under the frozen manuscript policy, Section VII uses strict evidence counts over the canonical 220-paper included corpus as its primary coverage view, while structured `study_flag_count` values are retained only in VII-G as a secondary consistency lens. On that primary view, the evidence base covers 220 included papers and 48 micro-domains, with strongest macro coverage in smart infrastructure (203 papers), automotive transportation (104 papers), and indoor environments (81 papers), establishing a deployment-synthesis scope that is broader than any one medium or scenario family. Within this scope, representative deployments already span endogenous telecom cabled-fiber monitoring, vehicular camera-based V2X operation, and space-satellite ISAC under LEO mobility, so the subsection keeps comm-plane and sensing-plane evidence separated while comparing transferable design patterns across domains [O_ISAC_074] [O_ISAC_164] [O_ISAC_187]. The four scenarios below keep this evidence contract explicit, deployment-grounded, and bounded away from unresolved dual-view mismatches.

#### Scenarios 1-2
Scenario 1: Endogenous telecom cabled-fiber monitoring and carriage co-design (smart_infrastructure).  
Scenario vector s includes a 10.4 km telecom cabled-fiber span with dual-polarization chirp training and coherent payload plus sensing coexistence [O_ISAC_074]. Sensing plane: distributed vibration monitoring is reported with 1 m spatial resolution [O_ISAC_074]. Communication plane: the same deployment reports 50 GBaud 16-QAM transmission and BER behavior versus SCPR [O_ISAC_074]. Dominant component label is Conventional because the opened evidence describes signal-processing and coherent reception flow without explicit OPA or ORIS hardware dominance [O_ISAC_074]. Transfer hook: Working hypothesis, chirp-based training reuse can transfer to other mobility-stressed optical ISAC links [O_ISAC_074] [O_ISAC_187]. Representative works: [O_ISAC_074].

Scenario 2: Photonic Doppler-robust payload link in LEO satellite networking (space_satellite).  
Scenario vector s captures LEO deployment, high mobility, Doppler stress, and chirp-multiplexed shared waveform operation [O_ISAC_187]. Sensing plane: target ranging is reported with range-resolution behavior better than 0.146 m under stated probability condition [O_ISAC_187]. Communication plane: the same source reports payload communication behavior including 29.99 Mbps and BER below the 7% pre-FEC threshold at 500 kHz Doppler [O_ISAC_187]. Dominant component label is Conventional because the evidence is built around photonic up-conversion and de-chirp processing without explicit OPA or ORIS dominance claims [O_ISAC_187]. Transfer hook: Working hypothesis, Doppler-robust waveform logic can transfer to mobility-driven vehicular optical links [O_ISAC_187] [O_ISAC_164]. Representative works: [O_ISAC_187].

#### Scenarios 3-4
Scenario 3: Vehicular OC-ISAC camera links for cooperative road awareness (automotive_transportation).  
Scenario vector s reflects outdoor V2X operation with V2V and V2I or I2V exchange, mobility, and LOS plus reflected optical paths observed by vehicle or roadside cameras [O_ISAC_164]. Sensing plane: environmental perception is reported through normalized sensing gain and contrast behavior under mobility and exposure settings [O_ISAC_164]. Communication plane: OCC payload recovery is reported through normalized communication-gain and BER-context analysis [O_ISAC_164]. Dominant component label is Conventional because the deployment is LED-camera architecture plus exposure optimization without explicit OPA or ORIS control hardware [O_ISAC_164]. Transfer hook: evidence-backed, the integrated localization plus OCC design is explicitly stated as applicable to vehicular networks [O_ISAC_143]. Representative works: [O_ISAC_164] [O_ISAC_143].

Scenario 4: Indoor localization-plus-access deployment with distributed optical access points (indoor_environments).  
Scenario vector s includes indoor geometry-defined placement of distributed optical access points, LED and PD or camera roles, and LOS-centered propagation with reflected-light sensing [O_ISAC_011] [O_ISAC_108]. Sensing plane: indoor ranging and positioning are reported with distance-measurement RMSE and positioning MSE or RMSE metrics [O_ISAC_011] [O_ISAC_108]. Communication plane: optical data delivery is reported through BER behavior versus a source-reported electrical-plane SNR variable and BER-oriented gains under integrated layout operation [O_ISAC_011] [O_ISAC_108]. Dominant component label is Conventional because the opened sources discuss layout optimization, beamforming, and baseband processing without explicit OPA or ORIS dominance statements [O_ISAC_011] [O_ISAC_108]. Transfer hook: Working hypothesis, source-layout plus shared-intensity objectives can transfer to other dense distributed optical deployments [O_ISAC_108]. Representative works: [O_ISAC_011] [O_ISAC_108].

#### Math Anchor
To preserve VII-F cross-domain synthesis, the subsection keeps the selected portfolio anchor:

$$
\max_{x,z,g,y}\; \sum_{d \in D} W_d z_d + \sum_{a \in A} V_a g_a - \lambda \sum_{d<q} L_{d,q}(1-y_{d,q})
$$
$$
\text{s.t. } z_d \le \sum_{i=1}^{N} M_{i,d}x_i,\quad g_a \le \sum_{i=1}^{N} U_{i,a}x_i,\quad \sum_{i=1}^{N}x_i \le B
$$
$$
y_{d,q}\le z_d,\quad y_{d,q}\le z_q,\quad x_i \in \{0,1\},\quad z_d,g_a,y_{d,q}\in\{0,1\}.
$$

Here, x is the scenario or paper-selection vector, coverage terms are parameterized by macro- and micro-domain evidence counts, and TransferPenalty is parameterized by shared-medium cross-domain structure.

**Key takeaways and application priorities.**
- VII-F coverage statistics justify the cross-domain scenario set on the strict primary view: smart infrastructure has 203 papers, automotive has 104 papers, and indoor has 81 papers, while vehicular plus indoor-positioning micro-domains have 61 and 57 papers.
- Transfer-map evidence shows these macros share medium structure, especially hybrid and VLC-oriented entries, which supports conservative deployment-level portability analysis.
- Across all four scenarios, sensing-plane and comm-plane reporting remain explicitly separated: sensing-side RMSE or MSE or gain descriptors are not mixed with comm-plane BER or throughput descriptors in one claim [O_ISAC_074] [O_ISAC_187] [O_ISAC_164] [O_ISAC_011] [O_ISAC_108].
- Evidence-bound synthesis in this subsection remains Conventional at scenario level unless explicit OPA or ORIS dominance is directly reported in opened deployment sources [O_ISAC_074] [O_ISAC_187] [O_ISAC_164] [O_ISAC_011] [O_ISAC_108].

Therefore, VII-G reconciles findings through dual-view consistency accounting by building on the coverage-and-transfer synthesis.

### VII-G. Dual-View Consistency Layer

Table VII-2. Dual-View Discrepancy Summary (Structured Tags vs Raw/Strict Evidence).

| macro_domain | flag_count | raw_count | strict_count | raw_only_delta | strict_only_delta | example_key | row_refs (comparison row #; examples row #) |
|---|---:|---:|---:|---:|---:|---|---|
| automotive_transportation | 76 | 212 | 104 | 136 | 28 | O_ISAC_010 | comparison row #4; examples row #9 |
| smart_infrastructure | 103 | 220 | 203 | 117 | 100 | O_ISAC_071 | comparison row #2; examples row #4 |
| underwater_harsh | 16 | 122 | 23 | 106 | 7 | O_ISAC_021 | comparison row #5; examples row #12 |
| space_satellite | 17 | 134 | 34 | 117 | 17 | O_ISAC_070 | comparison row #6; examples row #16 |


#### Context
VII-G is treated as a dual-view consistency layer rather than a vertical application survey. The subsection compares study-level structured application tags (`study_flag_count`) with extracted evidence-row counts under two gates (`raw_evidence_count`, `strict_evidence_count`). This framing follows the dual-view report scope and is used to assess where structured annotation and evidence extraction align or diverge across macro domains. Numerically, the contrast space spans large raw-only surpluses (for example, automotive `+136`, underwater `+106`) and domain-specific strict-view behavior (smart infrastructure `+100`, space `+17`) (comparison rows #4, #5, #2, #6). The intent is methodological: expose view-dependent coverage patterns before interpreting domain conclusions. Accordingly, raw and study-flag discrepancies are treated here as audit diagnostics only; headline prevalence claims elsewhere in Section VII follow the strict primary view.

#### Cases
Case 1, automotive raw-only expansion (`automotive_transportation`): View-1 records `study_flag_count=76`, while View-2 reports `raw_evidence_count=212` and `strict_evidence_count=104`. The discrepancy is `raw_only_vs_flag=136` and `strict_only_vs_flag=28` (comparison row #4). The representative evidence pool for this pattern is explicitly bound through automotive `raw_only` examples (examples row #9), which include `O_ISAC_010` [O_ISAC_010]. The contrast indicates that row-level extraction surfaces many application mentions not retained in study-tag fields; strict gating reduces but does not eliminate that surplus.

Case 2, strict-only surplus in smart infrastructure (`smart_infrastructure`): View-1 records `study_flag_count=103`; View-2 reports `raw_evidence_count=220` and `strict_evidence_count=203`. The deltas remain large under both gates, especially `strict_only_vs_flag=100` (with `raw_only_vs_flag=117`) (comparison row #2). Representativeness is anchored in the smart-infrastructure `strict_only` examples set (examples row #4), which includes `O_ISAC_071` [O_ISAC_071]. This case shows that strict filtering can still preserve a large body of support-qualified evidence beyond structured tags, so disagreement is not only a raw-extraction artifact.

Case 3, underwater raw-only asymmetry (`underwater_harsh`): View-1 records `study_flag_count=16`; View-2 reports `raw_evidence_count=122` and `strict_evidence_count=23`. The domain moves from a very large raw surplus (`raw_only_vs_flag=106`) to a small strict surplus (`strict_only_vs_flag=7`) (comparison row #5). The case is represented in underwater `raw_only` examples (examples row #12), including `O_ISAC_021` [O_ISAC_021]. The pattern supports a conservative interpretation: this divergence is strongly gate-sensitive, so coverage claims based on raw extraction alone can overstate durable evidence support for this domain.

Case 4, strict-view uplift in space (`space_satellite`): View-1 records `study_flag_count=17`; View-2 reports `raw_evidence_count=134` and `strict_evidence_count=34`. Even after strict filtering, strict evidence remains above structured tags (`strict_only_vs_flag=17`, `raw_only_vs_flag=117`) (comparison row #6). The representative binding is the space `strict_only` examples set (examples row #16), including `O_ISAC_070` [O_ISAC_070]. Unlike underwater, strict contraction does not collapse the surplus to near-zero, indicating that support-qualified evidence remains materially broader than study-level annotation in this domain.

Across all four domains, strict retention relative to raw evidence differs materially: automotive `104/212`, smart infrastructure `203/220`, underwater `23/122`, and space `34/134` (comparison rows #4, #2, #5, #6). This cross-case spread reinforces that one gate setting does not yield uniform coverage behavior across macro domains. For interpretation, the dual-view table should therefore be read as domain-conditioned evidence accounting rather than a single global correction factor.

**Key takeaways and application priorities.**
- Raw-versus-strict gating materially changes observed coverage; underwater contracts from `+106` raw-only to `+7` strict-only, while space contracts from `+117` to `+17` (comparison rows #5, #6).
- Strict-gated extraction can still exceed structured tags by a large margin, as in smart infrastructure (`strict_only_vs_flag=100`) and space (`strict_only_vs_flag=17`) (comparison rows #2, #6).
- Each domain case is evidence-anchored at two levels: numeric discrepancy through comparison rows and representativeness through examples rows (#9, #4, #12, #16), with concrete papers `O_ISAC_010`, `O_ISAC_071`, `O_ISAC_021`, and `O_ISAC_070`.
- Domain-dependent annotation and extraction bias remains a risk because identical gates yield very different strict deltas across domains (`+100`, `+28`, `+7`, `+17`) (working hypothesis; comparison rows #2, #4, #5, #6).
- Unresolved scope-mismatch and weak-evidence rows are therefore quarantined from headline prevalence claims and retained only in this audit-oriented consistency layer.
