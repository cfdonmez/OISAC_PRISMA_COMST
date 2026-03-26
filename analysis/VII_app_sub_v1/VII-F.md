### VII-F. Cross-Domain Application Synthesis

#### Context
Section VII-F is treated as a cross-domain applications layer for O-ISAC rather than a single vertical slice. The patched evidence base reports 221 papers and 48 micro-domains, with strongest macro coverage in smart infrastructure (204 papers), automotive transportation (104 papers), and indoor environments (81 papers), establishing a deployment-synthesis scope that is broader than any one medium or scenario family (section7F_summary.json key paths `$.n_total_papers`, `$.n_unique_micro_domains`; s7f_macro_med_cov.csv rows 2-4). Within this scope, representative deployments already span endogenous telecom-fiber monitoring, vehicular camera-based V2X operation, and space-satellite ISAC under LEO mobility, so the subsection keeps comm-plane and sensing-plane evidence separated while comparing transferable design patterns across domains [O_ISAC_074] [O_ISAC_164] [O_ISAC_187]. The four scenarios below keep this evidence contract explicit and deployment-grounded.

#### Scenarios 1-2
Scenario 1: Endogenous telecom-fiber monitoring and carriage co-design (smart_infrastructure).  
Scenario vector s includes a 10.4 km telecom-fiber span with dual-polarization chirp training and coherent payload plus sensing coexistence [O_ISAC_074]. Sensing plane: distributed vibration monitoring is reported with 1 m spatial resolution [O_ISAC_074]. Communication plane: the same deployment reports 50 GBaud 16-QAM transmission and BER behavior versus SCPR [O_ISAC_074]. Dominant component label is Conventional because the opened evidence describes signal-processing and coherent reception flow without explicit OPA or ORIS hardware dominance [O_ISAC_074]. Transfer hook: Working hypothesis, chirp-based training reuse can transfer to other mobility-stressed optical ISAC links [O_ISAC_074] [O_ISAC_187]. Representative works: [O_ISAC_074].

Scenario 2: Photonic Doppler-robust payload link in LEO satellite networking (space_satellite).  
Scenario vector s captures LEO deployment, high mobility, Doppler stress, and chirp-multiplexed shared waveform operation [O_ISAC_187]. Sensing plane: target ranging is reported with range-resolution behavior better than 0.146 m under stated probability condition [O_ISAC_187]. Communication plane: the same source reports payload communication behavior including 29.99 Mbps and BER below the 7% pre-FEC threshold at 500 kHz Doppler [O_ISAC_187]. Dominant component label is Conventional because the evidence is built around photonic up-conversion and de-chirp processing without explicit OPA or ORIS dominance claims [O_ISAC_187]. Transfer hook: Working hypothesis, Doppler-robust waveform logic can transfer to mobility-driven vehicular optical links [O_ISAC_187] [O_ISAC_164]. Representative works: [O_ISAC_187].

#### Scenarios 3-4
Scenario 3: Vehicular OC-ISAC camera links for cooperative road awareness (automotive_transportation).  
Scenario vector s reflects outdoor V2X operation with V2V and V2I or I2V exchange, mobility, and LOS plus reflected optical paths observed by vehicle or roadside cameras [O_ISAC_164]. Sensing plane: environmental perception is reported through normalized sensing gain and contrast behavior under mobility and exposure settings [O_ISAC_164]. Communication plane: OCC payload recovery is reported through normalized communication-gain and BER-context analysis [O_ISAC_164]. Dominant component label is Conventional because the deployment is LED-camera architecture plus exposure optimization without explicit OPA or ORIS control hardware [O_ISAC_164]. Transfer hook: evidence-backed, the integrated localization plus OCC design is explicitly stated as applicable to vehicular networks [O_ISAC_143]. Representative works: [O_ISAC_164] [O_ISAC_143].

Scenario 4: Indoor localization-plus-access deployment with distributed optical access points (indoor_environments).  
Scenario vector s includes indoor geometry-defined placement of distributed optical access points, LED and PD or camera roles, and LOS-centered propagation with reflected-light sensing [O_ISAC_011] [O_ISAC_108]. Sensing plane: indoor ranging and positioning are reported with distance-measurement RMSE and positioning MSE or RMSE metrics [O_ISAC_011] [O_ISAC_108]. Communication plane: optical data delivery is reported through BER behavior versus transmitted SNR and BER-oriented gains under integrated layout operation [O_ISAC_011] [O_ISAC_108]. Dominant component label is Conventional because the opened sources discuss layout optimization, beamforming, and baseband processing without explicit OPA or ORIS dominance statements [O_ISAC_011] [O_ISAC_108]. Transfer hook: Working hypothesis, source-layout plus shared-intensity objectives can transfer to other dense distributed optical deployments [O_ISAC_108]. Representative works: [O_ISAC_011] [O_ISAC_108].

#### Math Anchor
To preserve VII-F cross-domain synthesis, the subsection keeps the portfolio anchor selected in Run4:

$$
\max_{x,z,g,y}\; \sum_{d \in D} W_d z_d + \sum_{a \in A} V_a g_a - \lambda \sum_{d<q} L_{d,q}(1-y_{d,q})
$$
$$
\text{s.t. } z_d \le \sum_{i=1}^{N} M_{i,d}x_i,\quad g_a \le \sum_{i=1}^{N} U_{i,a}x_i,\quad \sum_{i=1}^{N}x_i \le B
$$
$$
y_{d,q}\le z_d,\quad y_{d,q}\le z_q,\quad x_i \in \{0,1\},\quad z_d,g_a,y_{d,q}\in\{0,1\}.
$$

Here, x is the scenario or paper-selection vector, Coverage terms are parameterized by macro and micro evidence counts, and TransferPenalty is parameterized by shared-medium cross-domain structure (s7f_macro_med_cov.csv rows 2-6; s7f_micro_dom_cnts.csv rows 2-5; section7F_transfer_map.csv rows 3, 13, 15, 23, 25, 30, 32, 36, 39).

#### Key Takeaways
- VII-F coverage statistics justify the cross-domain scenario set: automotive has 104 papers, indoor has 81 papers, and vehicular plus indoor_positioning micro domains have 61 and 57 papers (s7f_macro_med_cov.csv rows 3-4; s7f_micro_dom_cnts.csv rows 3-4).
- Transfer-map evidence shows these macros share medium structure, especially hybrid and wireless_vlc entries, which supports conservative deployment-level portability analysis (section7F_transfer_map.csv rows 15, 23, 25, 30).
- Across all four scenarios, sensing-plane and comm-plane reporting remain explicitly separated: sensing-side RMSE or MSE or gain descriptors are not mixed with comm-plane BER or throughput descriptors in one claim [O_ISAC_074] [O_ISAC_187] [O_ISAC_164] [O_ISAC_011] [O_ISAC_108].
- Evidence-bound synthesis in this subsection remains Conventional at scenario level unless explicit OPA or ORIS dominance is directly reported in opened deployment sources [O_ISAC_074] [O_ISAC_187] [O_ISAC_164] [O_ISAC_011] [O_ISAC_108].
