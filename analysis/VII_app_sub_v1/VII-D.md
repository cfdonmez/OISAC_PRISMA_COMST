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

#### Key Takeaways
- VII-D evidence supports a unified underwater_harsh narrative that includes both underwater wireless links and submarine-cable monitoring deployments [O_ISAC_127], [O_ISAC_220], [O_ISAC_020].
- Comm-plane evidence is strongest in SMART-style subsea cable scenarios, where integrated transmission performance and channel-compatible sensing are jointly reported [O_ISAC_220].
- Sensing-plane evidence is strongest in deep-ocean salinity monitoring, where refractive-index and salinity sensitivities are explicitly quantified with deployment-relevant crosstalk context [O_ISAC_027].
- Across all four scenarios, a conservative Conventional dominant-component label is evidence-consistent because explicit ORIS control-variable formulations are not directly reported in the opened scenario texts [O_ISAC_127], [O_ISAC_220], [O_ISAC_020], [O_ISAC_027].
