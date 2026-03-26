VII-B. Indoor Environments

Indoor O-ISAC deployments are characterized by shared optical infrastructure that must deliver communication service while extracting environment- or user-state information in the same transceiver workflow [O_ISAC_011] [O_ISAC_030]. In this vertical, the evidence base covers two core motifs. The first is localization-oriented retroreflective VLC, where transmitted and reflected optical signals are reused to support indoor 3D positioning without splitting communication and sensing into separate platforms [O_ISAC_011]. The second is human-centric interaction in lamp-centered settings, where VLC-capable luminaires concurrently support gesture-aware control and data communication in occupied indoor spaces [O_ISAC_030]. Across these motifs, deployment evidence remains application-facing: communication continuity is reported while sensing tasks execute, and sensing outputs remain operationally tied to positioning or interaction functions [O_ISAC_011] [O_ISAC_030].

Scenario 1: Retroreflective indoor VLC localization.  
Scenario vector s1 includes a 5 m x 5 m x 3 m room, four-LED transmitter geometry, and a PD/CCR retroreflective loop with cross-correlation delay estimation [O_ISAC_011]. Sensing plane: passive ranging and 3D localization are evaluated through distance-measurement RMSE and positioning RMSE behavior across receiver positions [O_ISAC_011]. Communication plane: the same platform reports BER versus transmitted SNR under multiple OFDM modulation orders [O_ISAC_011]. Dominant component label is Conventional because the reported implementation is based on LEDs, PDs, and CCR reflection paths, without explicit OPA or ORIS hardware [O_ISAC_011].

Scenario 2: VLC-lamp human-centric interaction under concurrent traffic.  
Scenario vector s2 is defined by a VLC-capable desk lamp, ring-shaped multi-LED emission, co-located PD reception, and table-surface reflection variability during simultaneous gesture and traffic operation [O_ISAC_030]. Sensing plane: reflected-light gesture recognition is reported with accuracy above 90 percent in the evaluated baseline PTD region [O_ISAC_030]. Communication plane: uplink/downlink BER behavior is maintained during gesture activity, and prototype throughput reaches 220 kbps [O_ISAC_030]. Dominant component label is Conventional, with evidence grounded in LED arrays, PD sensing, analog amplification, and FPGA processing, again without explicit OPA or ORIS claims [O_ISAC_030].

Scenario 3: Two-phase indoor LED O-ISAC with distributed O-APs.  
Scenario vector s3 captures indoor room geometry W x L x H, circular ceiling O-AP placement, multi-device PD-array reception, and directionless-to-directional operation [O_ISAC_108]. Sensing plane: device-position estimation uses coordinate MSE as the explicit sensing metric, including reported sensing MSE below 10^-4 at the evaluated operating point [O_ISAC_108]. Communication plane: BER is the communication metric, with reported gains of 2.70 dB in directionless mode and 63.35 dB in directional mode against a separated baseline [O_ISAC_108]. Dominant component label is Conventional because the implementation evidence centers on LED O-APs, pinhole cameras, PD arrays, and collimating lenses rather than explicit OPA or ORIS hardware [O_ISAC_108].

Scenario 4: Indoor multi-user VLC-CDMA with optical complementary codes.  
Scenario vector s4 uses a 5 m x 5 m x 3 m room, ceiling LED arrays with four wavelengths, desktop receivers at 0.85 m, and LOS plus reflected paths [O_ISAC_388]. Sensing plane: this scenario does not report an explicit sensing KPI. Communication plane: BER is reported against SNR, user count, and data rate, and BER degrades as user count increases because of multi-user interference [O_ISAC_388]. Dominant component label is Conventional because the architecture is described with LED arrays, optical filters, PD receivers, and OCC/OOC code structures without explicit OPA or ORIS hardware [O_ISAC_388].

A compact indoor deployment anchor consistent with the validated evidence is

```latex
\min_{u}\ \alpha\,\mathrm{BER}(u;s) + (1-\alpha)\,\mathrm{MSE}_{\mathrm{pos}}(u;s)
```
```latex
s=(g_{\mathrm{room}},\rho_{\mathrm{user}})
```

Here, u denotes indoor control variables such as resource allocation and waveform adaptation policy over the shared communication-sensing optical stack [O_ISAC_108] [O_ISAC_388]. The scenario vector s is restricted to evidenced deployment descriptors, namely room geometry and user density/load, both directly tied to reported indoor propagation and multi-user behavior [O_ISAC_108] [O_ISAC_388]. Communication-plane quality is represented by BER, while sensing-plane quality is represented by position-coordinate MSE, preserving strict metric-plane separation in deployment analysis [O_ISAC_108] [O_ISAC_388].

Key takeaways for this vertical:
- Indoor O-ISAC evidence consistently couples practical communication service with localization or gesture-driven sensing in shared lighting-centric infrastructure [O_ISAC_011] [O_ISAC_030].
- Scenario diversity spans both user-centric interaction and infrastructure-centric localization, and both report explicit communication-plane metrics while sensing is active [O_ISAC_011] [O_ISAC_030].
- Among later-stage indoor deployments, Scenario 3 provides explicit dual-plane metrics (BER and coordinate MSE), whereas Scenario 4 is communication-heavy with no explicit sensing KPI [O_ISAC_108] [O_ISAC_388].
- For deployment-level synthesis, BER and position MSE provide a conservative and evidenced cross-scenario objective pair under indoor geometry and user-density conditions [O_ISAC_108] [O_ISAC_388].
