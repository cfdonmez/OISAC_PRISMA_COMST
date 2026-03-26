VII-A. Smart Infrastructure & Outdoor Urban Sensing-Communication

Urban smart-infrastructure deployments use O-ISAC when the same optical platform must carry operational traffic while exposing environment and link state for control and supervision [O_ISAC_003] [O_ISAC_005] [O_ISAC_276]. Across representative studies, this vertical covers outdoor mobility corridors, metro and industrial fiber corridors, and live metropolitan access supervision, each with explicit sensing-plane and communication-plane reporting [O_ISAC_003] [O_ISAC_038] [O_ISAC_064] [O_ISAC_276].

Scenario 1: Outdoor mobility corridors with vehicular and UAV-assisted optical links.  
Scenario vector s1 includes V2V distance variation, mobility-driven geometry changes, and weather-dependent FSO attenuation [O_ISAC_003] [O_ISAC_005]. Sensing plane: target/background discrimination is reported through received-power-ratio behavior and RMS delay-spread trends in V2V operation, while backscattered light is used for FSO channel-gain estimation in UAV-assisted links [O_ISAC_003] [O_ISAC_005]. Communication plane: robust data delivery is evaluated through V2V transmission-quality behavior and throughput-oriented resource and trajectory control under backhaul limits [O_ISAC_003] [O_ISAC_005]. Dominant component label: Conventional (no ORIS or OPA explicitly evidenced), since the cited implementations describe VLC, FSO, RF transceiver and control designs without explicit ORIS or OPA components [O_ISAC_003] [O_ISAC_005]. Representative works are visible-light V2V channel characterization and mixed FSO-RF UAV trajectory optimization [O_ISAC_003] [O_ISAC_005].

Scenario 2: Fiber-corridor sensing-communication for metro and industrial infrastructure.  
Scenario vector s2 is characterized by 10-10.4 km fiber spans and interference-fading behavior in Rayleigh backscatter traces [O_ISAC_038] [O_ISAC_074]. Sensing plane: distributed vibration monitoring is reported with 1 m spatial resolution and interference-fading suppression [O_ISAC_038] [O_ISAC_074]. Communication plane: coherent payload transport is demonstrated with 50-60 GBaud 16-QAM and limited coexistence penalty [O_ISAC_038] [O_ISAC_074]. Dominant component label: Conventional (no ORIS or OPA explicitly evidenced), because the evidence is based on coherent-fiber DSP and waveform processing without explicit ORIS or OPA hardware [O_ISAC_038] [O_ISAC_074]. Representative works include NOMA-based DAS coexistence and endogenous training-sequence reuse [O_ISAC_038] [O_ISAC_074].

Scenario 3: Metropolitan deployed-fiber supervision.  
Scenario vector s3 includes metropolitan deployed fibers, point-to-multipoint access topology, and splitter branch-overlap risk [O_ISAC_064] [O_ISAC_276]. Sensing plane: event observability is reported via direct magnitude readout in live XGS-PON tests, including a 4.5 dB event measured as 4.55 dB [O_ISAC_276]. Communication plane: downstream traffic tests report no baseline performance difference between regular and upgraded remote nodes in the tested setup [O_ISAC_276]. Dominant component label: Conventional (no ORIS or OPA explicitly evidenced), with evidence centered on deployed-fiber OTDR and coherent monitoring workflows [O_ISAC_064] [O_ISAC_276]. Representative works include metropolitan smart-city deployed-fiber studies and live XGS-PON supervision [O_ISAC_064] [O_ISAC_276].

Scenario 4: Outdoor FSO ranging-communication for vehicular or autonomous links.  
Scenario vector s4 reflects outdoor free-space geometry, line-of-sight dependence, and atmospheric-loss or turbulence exposure [O_ISAC_012] [O_ISAC_034]. Sensing plane: distance observability is evaluated through MSE or RMSE behavior and related ranging metrics [O_ISAC_012] [O_ISAC_034]. Communication plane: reliability and efficiency are reported through code-rate and BER behavior in multi-user optical ISAC evaluations [O_ISAC_012] [O_ISAC_034]. Dominant component label: Conventional (no ORIS or OPA explicitly evidenced), since the validated papers emphasize waveform and receiver-DSP design rather than ORIS or OPA components [O_ISAC_012] [O_ISAC_034]. Representative works include PC-FMCW optical ISAC and PSS-PPM optical ISAC [O_ISAC_012] [O_ISAC_034].

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

Key takeaways for this vertical:
- Outdoor O-ISAC behavior is strongly scenario-vector dependent across mobility, weather, and topology [O_ISAC_003] [O_ISAC_005] [O_ISAC_276].
- Fiber-corridor deployments can co-support vibration sensing and high-rate coherent communication under controlled coexistence design [O_ISAC_038] [O_ISAC_074].
- Live access supervision shows that sensing readout and communication continuity can be jointly maintained in tested point-to-multipoint operation [O_ISAC_276].
- Reported optical ISAC evaluations use reliability metrics such as BER and ranging-error metrics such as MSE or RMSE to keep communication-plane and sensing-plane assessment separable [O_ISAC_012] [O_ISAC_034].
