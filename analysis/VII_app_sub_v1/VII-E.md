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

#### Key Takeaways
- VII-E evidence is consistently deployment-grounded in space-satellite operation and spans ISL backbone networking, LEO Doppler-robust payloads, SLR integration, and multi-beam Earth-observation payloads [O_ISAC_089], [O_ISAC_137], [O_ISAC_187], [O_ISAC_195].
- Communication-plane reporting and sensing-plane reporting are both explicit in this vertical, but they are carried by different metric families and must remain separated in synthesis [O_ISAC_187], [O_ISAC_195].
- The scenario vectors are driven by topology and motion conditions that are directly evidenced in the opened texts, including mesh ISLs, LEO mobility context, station-to-satellite links, and multi-beam payload structure [O_ISAC_089], [O_ISAC_137], [O_ISAC_187], [O_ISAC_195].
- Under the current evidence contract, all four scenarios remain Conventional because no micro-part source text explicitly establishes OPA- or ORIS-dominant deployment control for VII-E [O_ISAC_089], [O_ISAC_137], [O_ISAC_187], [O_ISAC_195].
