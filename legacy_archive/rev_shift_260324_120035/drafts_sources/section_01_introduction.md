# I. INTRODUCTION

## A. The Convergence of Sensing and Communication: A 6G Imperative

The escalating complexity of the electromagnetic environment has intensified demands for ultra-reliable wireless connectivity, driving significant interest in Integrated Sensing and Communication (ISAC) systems [O_ISAC_070:1]. This integrated approach enables ultra-efficient spectrum utilization and significantly reduces hardware costs, and more importantly, establishes a foundational framework for achieving seamless connectivity in future wireless networks [O_ISAC_070:2]. ISAC has now emerged as a core enabler in 6G networks and is recognized as one of the six key usage scenarios by both the ITU-R IMT-2030 framework [O_ISAC_162:1] and 3GPP [O_ISAC_162:2], spanning the coexistence, cooperation, and co-design of communication and sensing functionalities [O_ISAC_070:3].

The intelligence of future society necessitates an immediate requirement for ultra-high-speed communication and ultra-resolution sensing in the 6G era [O_ISAC_016]. As intelligent applications—including robot navigation, augmented reality, autonomous driving, and human–machine interaction—continue to proliferate, these emerging services require the capability of highly-reliable wireless communication and high-accuracy environment sensing simultaneously [O_ISAC_351]. Wireless communication frequency bands are gradually transitioning to higher frequency ranges—encompassing millimeter-wave (mmWave) and terahertz (THz)—to fulfill the ultra-high data rate requirements of this vision. **Despite significant progress in RF-based ISAC**, the conventional independent design of communication and sensing systems generally occupies disjoint spectral resources, profoundly aggravating spectrum congestion [O_ISAC_351]. Moreover, using traditional all-electronic approaches to generate mmWave or THz signals will inevitably encounter challenges such as high complexity and **bandwidth limitation**, which will increase the system costs significantly [O_ISAC_286]. To the best of our knowledge, conventional RF-ISAC systems face three fundamental constraints:

1. **Spectrum Congestion**: With the rapid advances of wireless mobile devices, RF communication and sensing systems face challenges such as spectrum congestion, limited bandwidth, and susceptibility to electromagnetic interference [O_ISAC_068]. The exponentially growing demand for mobile data, coupled with stringent sensing resolution requirements of emerging applications (holographic telepresence, digital twins, autonomous navigation), has created significant pressure on the congested RF spectrum [O_ISAC_161].

2. **Limited Resolution and Bandwidth**: The spatial resolution achievable in the mmWave band is fundamentally limited to approximately centimeter-level, insufficient for millimeter-precision applications [O_ISAC_021]. Furthermore, RF-ISAC systems commonly suffer from **spectrum scarcity, high power consumption, and limited sensing capabilities** [O_ISAC_203].

3. **Hardware Constraints**: Purely electrical THz systems struggle to achieve the wide bandwidth and flexible reconfigurability demanded by 6G [O_ISAC_070]. The construction of mmWave/THz ISAC systems using purely electrical means is associated with bandwidth and frequency adjustability limitations that increase overall system complexity [O_ISAC_286].

**Recent advances in photonic THz techniques have opened new opportunities** for transcending these RF limitations. **Optical Integrated Sensing and Communication (O-ISAC)** has emerged as a transformative paradigm that unifies perception, transmission, and processing on optical carriers [O_ISAC_021]. **Fig. 1** illustrates this paradigm evolution through three distinct phases: **(A)** the fundamental spectral and bandwidth constraints of conventional RF-ISAC; **(B)** the transformative opportunities of the optical domain, leveraging the 28.3–845 THz spectrum to enable Tbps-class capacity and mm-scale resolution; and **(C)** the unified taxonomy of this survey, which branches O-ISAC into fiber-based, wireless (FSO/THz), and VLC modalities. Our systematic analysis of **220 peer-reviewed O-ISAC studies (2020–2025)** reveals that optical ISAC prototypes have pushed these limits: photonic-terahertz integration has achieved **120 Gbps wireless throughput with 2.5 mm sensing resolution** [O_ISAC_105], corresponding to $\text{CRQ}_{\Delta} \approx 4.8\times10^{13}$ bps/m [O_ISAC_105]. Earlier photonic sub-THz demonstrations report $\text{CRQ}_{\Delta}$ on the order of $1.0\times10^{13}$ bps/m [O_ISAC_016].

![Fig. 1. The O-ISAC paradigm evolution. (A) RF-ISAC systems in sub-6 GHz/mmWave bands often face deployment-constrained spectrum and hardware limits, motivating a transition toward photonic carriers to pursue Tbps-class capacity and mm-scale sensing targets. (B) Optical-ISAC leverages the broad photonic spectrum (≈28.3–845 THz), with implementations clustering in operational windows (telecom for fiber and NIR/visible/photonic-THz for wireless). The survey taxonomy branches Optical-ISAC into fiber-based, free-space/photonic-THz, and VLC/LiFi modalities, each characterized by distinct signal models and dominant impairments.](fig1.png)


Recent photonic and fiber demonstrations illustrate the rate–resolution frontier: a 275 GHz LFM-QAM system reports 120 Gbps with a (two-way) bandwidth-limited range resolution $\Delta r_{\min} \approx 2.5$ mm, yielding $\text{CRQ}_{\Delta} := R / \Delta r_{\min} = 4.8\times10^{13}$ bps/m (equivalently 480 Gbps/cm) [O_ISAC_105]; a D-band sub-THz FDM link delivers 251.03 Gbps with $\Delta r_{\min}=2.5$ cm [O_ISAC_016]; and co-wavelength DAS/DSM over a 38 km seven-core fiber sustains 241.85 Tb/s while sensing 0.1 Hz vibrations with 20 m spatial granularity [O_ISAC_046]. These exemplars highlight the bandwidth advantages of optical carriers and motivate a systematic question.

*These demonstrations motivate a fundamental question: What unique properties of the optical domain enable such performance gains, and how can these advantages be systematically exploited for next-generation ISAC systems?* To address this question, we now examine the physical foundations that position the optical spectrum as the natural substrate for high-performance ISAC.

Table I previews the axis-based comparison of related survey-style works discussed in Section I-D.

### Table I: Axis-Based Comparison of This Survey with Existing Related Survey-Style Works

| Ref. | Year | Tier | Modality Scope (F / FSO / VLC / THz) | Int. Depth | Methodology | Taxonomy | Metrics | Benchmark | Transfer | Enablers |
|:---:|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [O_ISAC_161] | 2025 | 2 | ○ / ○ / ○ / ○ | ● | Review | ◐ | – | – | – | – |
| [O_ISAC_068] | 2023 | 2 | ○ / ○ / ● / ○ | ● | Narrative | – | – | – | – | – |
| [O_ISAC_327] | 2024 | 2 | ○ / ○ / ● / ○ | ◐ | Survey | ◐ | – | – | – | – |
| [O_ISAC_006] | 2024 | 2 | ● / ○ / ○ / ○ | ◐ | Review | – | ◐ | – | – | – |
| [O_ISAC_368] | 2023 | 2 | ● / ○ / ○ / ○ | ◐ | Review | – | – | – | – | – |
| [O_ISAC_021] | 2023 | 2 | ○ / ● / ○ / ○ | ● | Tutorial | ◐ | ◐ | – | – | ◐ |
| [O_ISAC_070] | 2025 | 2 | ○ / ○ / ○ / ● | ● | Narrative | ◐ | – | – | – | – |
| [O_ISAC_163] | 2025 | 2 | ○ / ○ / ○ / ○ | ● | Survey | ◐ | – | – | ◐ | ● |
| [O_ISAC_303] | 2024 | 1 | ○ / ○ / ● / ○ | ● | Review | ◐ | ◐ | – | – | – |
| **This Survey** | **2026** | **–** | **● / ● / ● / ●** | **●** | **PRISMA 2020** | **●** | **●** | **●** | **●** | **●** |

*Legend: ● = strong/explicit (Score 1); ◐ = partial/within-modality (Score 0.5); – = absent (Score 0); ○ = out-of-scope. Modality Scope uses (○/◐/●) only. F = Fiber, FSO = Free-Space Optics, VLC = Visible Light, THz = Photo-THz. THz denotes photonic-THz / optical–THz bridging O-ISAC (not generic RF THz-ISAC hardware surveys).*
*Scoring Criteria: Symbols are mapped via $s_a(p) \in \{0, 1/2, 1\}$ to $\{–, ◐, ●\}$ based on evidence strength: **●** = Systematic/Cross-modal (e.g., unified taxonomy, defined benchmark suite); **◐** = Partial/Single-modality; **–** = Absent/Unaddressed.*

## B. The Optical Opportunity: A Vast and Untapped Frontier

Moving from the RF spectrum crisis to a potential solution, the optical domain—spanning the infrared (IR), visible, and ultraviolet bands—presents an opportunity of transformative scale. While RF-ISAC operates within a congested spectrum below 300 GHz, O-ISAC nominally spans approximately **28.3 THz to 845 THz** (corresponding to wavelengths from 355 nm to 10.6 μm), though practical systems cluster within established atmospheric transmission windows and fiber telecom bands [O_ISAC_021]. In this survey, Photo-THz O-ISAC refers to photonics-enabled architectures where optical carriers are used for generation/LO/distribution, while the wireless propagation carrier resides in the sub-THz/THz band—thus forming an optical–THz bridging modality. This section elucidates the fundamental physical advantages that position the optical domain as the natural substrate for next-generation ISAC systems.

### B.1 Quantitative Comparison: RF-ISAC vs. O-ISAC

To ground our analysis in empirical data, Table II presents a head-to-head comparison between RF-ISAC modalities (WiFi, mmWave) and O-ISAC, synthesized from our systematic corpus analysis of 220 peer-reviewed studies [O_ISAC_021].

**Table II: RF-ISAC vs. O-ISAC Performance Comparison [O_ISAC_021]**

| Characteristic | RF-ISAC (Sub-6 GHz / mmWave) | Wireless O-ISAC (FSO / VLC / Photo-THz) | Wired O-ISAC (Fiber Sensing) |
| :--- | :--- | :--- | :--- |
| **Carrier Frequency** | 2.4–100 GHz | 0.1–10 THz (Photo-THz) + 28.3–845 THz (FSO/VLC) | 193 THz (C-Band / L-Band) |
| **Physics Model** | Diffuse Multipath (Rich) | Line-of-Sight (LoS) Dominated | Guided Mode (Low Loss, Dispersive) |
| **Signal Type** | Complex (I/Q) | Real (IM/DD) or Complex (Coherent FSO) | Complex (Coherent Phase/Polarization) |
| **Key Impairments** | Interference, Multi-path Fading | Ambient Light, Turbulence, Pointing Error | Nonlinearity (Kerr), PMD, Phase Noise |
| **Sensing Task** | Radar (Range/Doppler) | Localization, Gesture, Surface Profiling | DAS (Vibration), Strain, Temperature |
| **Peak Data Rate** | ~10–20 Gbps | **~100–120 Gbps** [O_ISAC_105] | **> 200 Tbps** (Aggregate) [O_ISAC_046] |
| **Resolution** | cm-level | **mm-level (2.5 mm)** [O_ISAC_105] | m-level (Spatial) / nε (Strain) |

### B.2 Three Competitive Advantages of O-ISAC

Drawing from the generalized O-ISAC system architecture proposed in [O_ISAC_021], we identify three fundamental advantages that differentiate optical approaches from their RF counterparts. **Fig. 2** provides a technical "zoom-in" on the physical mechanisms underlying these advantages, contrasting optical physics with RF constraints.

![Fig. 2. Physical mechanisms behind the three competitive advantages of O-ISAC. (Left) Capacity scaling is achieved via dense Multiplexing (WDM/SDM), enabling aggregate rates of 241.85 Tb/s (wired) [O_ISAC_046] and dense parallel channels (wireless) [O_ISAC_021]. (Center) Sensing precision is driven by ultra-wide effective bandwidth, enabling wireless range resolution down to $\Delta r_{\min} = 2.5$ mm and $\text{CRQ}_{\Delta}$ of $4.8\times10^{13}$ bps/m (480 Gbps/cm) [O_ISAC_105]. (Right) Spatial isolation is inherent to narrow optical beams, reducing multi-user interference and RF-EMI susceptibility compared to wide RF sectors.](fig2.png)


#### Advantage 1: Capacity Scaling Through Spectral Abundance and Multiplexing

The optical spectrum (spanning **28.3 THz to 845 THz** [O_ISAC_021]) offers massive resources for dense multiplexing. Unlike RF systems limited by sub-6 GHz blocks, optical carriers support massive parallelism as illustrated in **Fig. 2 (Left)**:
- **Wireless Parallelism:** Experimental demonstrations of Mode Division Multiplexing (MDM) combined with WDM have realized **64 parallel channels** (16 wavelengths × 4 OAM modes) to scale wireless throughput [O_ISAC_021].
- **Wired Aggregate Capacity:** In the cabled domain, Space Division Multiplexing (SDM) using 7-core fiber has achieved an aggregate capacity of **241.85 Tbps** (96 WDM channels × 7 cores) over 38 km [O_ISAC_046].
*These independent demonstrations validate the scalability of optical multiplexing beyond single-link RF limits.*

#### Advantage 2: Enhancing Sensing Precision via Ultra-Wide Bandwidth

Range resolution ($\Delta r_{\min}$) is bandwidth-limited in two-way sensing according to $\Delta r_{\min} = v/(2B_{\text{eff}})$ (two-way ranging convention). The ultra-wide bandwidths available in the optical domain enable millimeter-level resolution that is physically difficult for narrowband RF systems to match (**Fig. 2, Center**):
- **Wireless Ranging:** Photonic-THz systems have demonstrated a **range resolution of 2.5 mm** alongside 120 Gbps data transmission [O_ISAC_105].
- **Capacity-Resolution Quotient (CRQ$_{\Delta}$):** This combination yields $\text{CRQ}_{\Delta} := R / \Delta r_{\min}$ of $4.8\times10^{13}$ bps/m (480 Gbps/cm) for wireless ranging [O_ISAC_105].
*Note: We strictly distinguish bandwidth-limited range resolution ($\Delta r_{\min}$) from SNR-dependent range accuracy ($\sigma_r = \sqrt{\mathbb{E}[(\hat r - r)^2]}$). While fiber DAS achieves meter-level spatial granularity ($\Delta z \approx 20$ m [O_ISAC_046]), its sensing value lies in ultra-sensitive vibration detection rather than high-resolution ranging.*

#### Advantage 3: Spatial Isolation and Reduced RF-EMI Coupling
The high directionality of optical beams provides deployment-dependent spatial isolation, significantly reducing Multi-User Interference (MUI) compared to wide-beam RF sectors in clear line-of-sight scenarios [O_ISAC_021]. While wireless O-ISAC links remain susceptible to atmospheric turbulence and ambient light [O_ISAC_003], their reduced susceptibility to conventional RF Electromagnetic Interference (EMI) and narrow beam divergence (typically on the order of milliradians [O_ISAC_021]) enable dense spatial reuse in deployment scenarios with favorable propagation conditions.

### B.3 Unified O-ISAC Taxonomy

Having established the physical mechanisms behind the three optical advantages—capacity scaling via multiplexing, bandwidth-limited ranging resolution, and directional spatial isolation—we next formalize the scope of this survey. Specifically, the O-ISAC literature does not constitute a single monolithic system class; rather, it clusters into distinct modalities determined by the propagation medium and the associated signal/impairment models. **Fig. 3** summarizes the resulting evidence-based taxonomy from our PRISMA-compliant 2020–2025 corpus, organizing O-ISAC into four modalities (fiber, free-space optical, VLC/LiFi, and photonic-THz) with their representative operating windows, dominant techniques, and canonical sensing–communication metrics.

![Fig. 3. The unified taxonomy of O-ISAC modalities derived from a systematic PRISMA-compliant analysis of 220 primary studies (2020–2025). (Top-Left) Fiber O-ISAC (Cabled) leveraging existing DAS/DSCM infrastructure for long-haul (>100 km) sensing and Tb/s-scale data transmission. (Top-Right) Free-Space Optical (FSO) O-ISAC for outdoor inter-building links utilizing coherent detection and atmospheric compensation. (Bottom-Left) Visible Light Communication (VLC) O-ISAC for indoor environments using LED infrastructure for joint illumination, high-speed connectivity, and sub-centimeter positioning. (Bottom-Right) Photonic Terahertz (Photo-THz) O-ISAC bridging the optical and wireless THz domains to achieve the highest reported $\text{CRQ}_{\Delta}$ metrics (>100 Gbps/cm, i.e., >$1.0\times10^{13}$ bps/m).](fig3.png)


1. **Fiber O-ISAC (Cabled):** Integration of DAS/DFOS with coherent optical transmission over single-mode/few-mode fibers. Key techniques include φ-OTDR, DSCM, and WDM-based sensing-communication multiplexing.

2. **Free-Space Optical (FSO) O-ISAC:** Outdoor/inter-building links using 1550 nm laser transmission with atmospheric channel compensation. Achieved ranges: <1 km with 100 Gbps capacity.

3. **Visible Light Communication (VLC) O-ISAC:** Indoor systems leveraging LED illumination infrastructure for simultaneous lighting, communication, and positioning. Key modulations: DCO-OFDM, CE-OFDM, OOK.

4. **Photo-THz O-ISAC:** Photonic-assisted sub-THz (100–300 GHz) systems bridging optical generation with wireless THz transmission. This emerging modality offers the highest reported $\text{CRQ}_{\Delta}$ values (>100 Gbps/cm, i.e., >$1.0\times10^{13}$ bps/m) [O_ISAC_016].

This unified taxonomy bridges the previously disjoint communities of optical communications, distributed fiber sensing, and optical wireless research—providing a coherent framework for cross-domain technology transfer. This taxonomy provides a common reference frame; however, the same modality boundaries also expose a deeper issue—terminology, metrics, and evaluation protocols remain inconsistent across communities, motivating the fragmentation challenge discussed next in Section I-C.

## C. The Fragmentation Challenge: A Landscape Without Unity

Despite the compelling physical advantages outlined above, the O-ISAC research landscape remains highly fragmented. Our systematic analysis of **220 peer-reviewed O-ISAC studies (2020–2025)** reveals four intertwined manifestations of this fragmentation—(i) inconsistent terminology, (ii) non-standardized sensing metrics, (iii) siloed modality communities, and (iv) limited cross-domain technology transfer—together impeding reproducibility, cross-study comparability, and ultimately the maturation of a unified 6G optical sensing–communication framework.

**Terminology Proliferation.** A foundational barrier to synthesis is the proliferation of synonymous and near-synonymous terms for closely related concepts. For instance, a single work may frame ISAC under an umbrella of aliases such as *"radar-communication (RadCom), joint radar-communication (JRC), and other related terms"* [O_ISAC_161], while VLC-centric studies describe *"Joint Communication and Sensing (JCS), also known as Integrated Sensing And Communication (ISAC), [and] Sensing-Communication Integration (SCI)"* [O_ISAC_068]. In the fiber community, the vocabulary further diverges into "ISAC-OF" (ISAC in optical fiber), "fiber-ISAC," and "photonic ISAC" [O_ISAC_041], [O_ISAC_033]. This aliasing is not merely cosmetic: it complicates systematic discovery, inflates perceived novelty through re-labeling, and obscures conceptual linkages across modalities and hardware assumptions.

**Metric Non-Isomorphism.** Equally problematic is the absence of a shared sensing-performance language. A first-order example is the recurrent conflation of **physical resolution limits** with **estimator-dependent accuracy** and **information-/estimation-theoretic bounds**. For ranging, the bandwidth-limited (two-way) physical resolution is governed by
$$
\Delta r_{\min}=\frac{v}{2B_{\text{eff}}},
$$
where $v=c$ in free space and $v\approx c/n_g$ in guided media (with group index $n_g$), hence representing a modality-dependent propagation speed but a common bandwidth principle. In contrast, reported "accuracy" metrics—RMSE, $\sigma_r = \sqrt{\mathbb{E}[(\hat r - r)^2]}$, or "localization error"—are inherently SNR-dependent and estimator-dependent, while CRB/FIM-based quantities characterize information-/estimation-theoretic bounds under an explicitly stated observation model [O_ISAC_013], [O_ISAC_050], [O_ISAC_056]. The practical consequence is that papers can report "resolution" in incommensurate senses: fiber DAS studies may report "spatial resolution" as a minimum resolvable segment length [O_ISAC_013], whereas FSO ranging papers may report "range resolution" via bandwidth-derived definitions [O_ISAC_035]. Additionally, "signal quality" is not referenced to a consistent measurement plane: coherent fiber systems often report OSNR in the optical domain [O_ISAC_028], whereas VLC systems typically report electrical SNR after photodetection [O_ISAC_009], complicating direct cross-modality comparisons without an explicit normalization convention.

**Sub-Domain Siloing and Limited Cross-Citation.** The literature has evolved along several largely independent trajectories—fiber DAS/communication co-design, FSO ranging–communication integration, VLC positioning–data links, and photonic-THz ISAC—each anchored in distinct channel models (guided vs. turbulent vs. LoS-dominated), transceiver paradigms (coherent DSP-driven optics vs. IM/DD LEDs), and evaluation benchmarks, with limited cross-pollination [O_ISAC_033], [O_ISAC_050], [O_ISAC_082]. Consequently, what appears as a "trade-off frontier" in one modality is often not directly comparable to another without carefully harmonized assumptions and metrics. This siloing is echoed in recent assessments: *"VLC and VLP systems are usually designed separately... mutual benefits between positioning and communication have not been utilized effectively"* [O_ISAC_039], and *"interoperability and certification across sectors remain a significant barrier"* [O_ISAC_161].

**Weak Cross-Domain Technology Transfer.** Beyond vocabulary and metrics, fragmentation manifests as limited portability of methods and abstractions. Waveform and probing strategies developed in fiber-ISAC contexts (e.g., LFM-embedded training structures [O_ISAC_042], polarization-based sensing probes [O_ISAC_074]) are only rarely transferred to free-space or VLC channels, while VLC-driven approaches (e.g., multi-carrier localization with m-CAP [O_ISAC_022], learning-enabled joint positioning [O_ISAC_039]) seldom reappear in FSO or photonic-THz settings. Hardware constraints further impede transfer: coherent fiber transceivers rely on DSP-intensive equalization and phase-sensitive reception [O_ISAC_033], whereas IM/DD LED-based O-ISAC is amplitude-constrained and often bandwidth-limited [O_ISAC_054]. In the absence of shared benchmarks and reporting protocols, it remains difficult to distinguish what is fundamentally modality-specific from what is transferable across optical platforms [O_ISAC_068], [O_ISAC_067].

**The Missing Unifying Framework.** Collectively, these issues point to a critical gap: the absence of a unified physical-layer taxonomy, a standardized performance-reporting contract, and a cross-modality benchmark suite. A minimal reporting contract should at least specify: (i) communication performance (rate, BER/FEC margin), (ii) sensing performance separated into physical resolution $\Delta r_{\min}$, estimator-level error (RMSE/$\sigma_r$), and information-/estimation-theoretic bounds (CRB/FIM), (iii) signal quality defined at an explicit reference plane (electrical SNR vs. OSNR), and (iv) channel/scenario assumptions that govern comparability. Recent calls for *"a standard VLC channel model... following the modeling methodology of 3GPP"* [O_ISAC_327] and for *"standardization efforts for facilitating interoperability"* [O_ISAC_068], [O_ISAC_082] underscore the urgency of this unification. Without such a framework, O-ISAC risks continued siloing, duplicated effort, and missed opportunities for cross-domain synergy—an observation that directly motivates the next section, where we systematically position existing surveys and identify the gaps that our PRISMA-based unified treatment addresses.

## D. Related Surveys and Gap Analysis

The rapid maturation of RF-based ISAC has given rise to a well-developed survey landscape in the radio-frequency domain, where comprehensive tutorials address waveform design, beamforming strategies, and information-theoretic limits for dual-function radar-communication systems. Hardware-centric ISAC transceiver surveys (RF-oriented) provide useful background but do not address optical modalities [O_ISAC_161]. In contrast, the optical ISAC domain remains comparatively underserved: existing review-style works are distributed across disjoint modality communities—VLC positioning, distributed fiber sensing, FSO channel modeling, and photonic-THz transmission—with limited cross-pollination and no unifying systematic treatment. This section maps the current landscape of related survey-style works, organized into Tier-1 (true O-ISAC surveys within our corpus) and Tier-2 (feeder/adjacent works that inform but do not unify the O-ISAC narrative), and identifies the critical gaps that motivate the present systematic review.

**VLC Positioning and Indoor Optical Surveys.** A growing body of work examines visible light communication for indoor positioning and data transmission. Studies exploring joint communication and sensing prospects through visible light highlight the potential of VLC for simultaneous high-speed data links and localization, while noting that spectrum scarcity, interference management, and hardware limitations remain significant barriers [O_ISAC_068]. Channel characterization surveys for VLC-IoE applications in 6G provide detailed modeling of indoor optical propagation but focus primarily on the communication link rather than integrated sensing functionality [O_ISAC_327]. Experimental works on integrated VLC positioning and communication—including 6-DoF location-and-pose estimation algorithms [O_ISAC_062] and photonic W-band ISAC demonstrations [O_ISAC_044]—advance individual system designs but do not consolidate findings into a unified cross-modality framework.

**Distributed Fiber Sensing and Fiber-ISAC Reviews.** In the cabled domain, distributed fiber optic sensing (DFOS) techniques—particularly φ-OTDR-based distributed acoustic sensing (DAS)—have reached commercial maturity for infrastructure monitoring. Recent works addressing integrated sensing and communication in optical fiber present the current development status and representative system architectures [O_ISAC_006], while experimental demonstrations of co-route fiber recognition and status diagnosis based on ISAC principles [O_ISAC_041] and high-precision vibration localization in bidirectional transmission systems [O_ISAC_090] illustrate the growing interest in fiber-ISAC integration. Ultra-large dynamic vibration sensing with fronthaul analog radio-over-fiber transmission further extends the sensing–communication co-design paradigm [O_ISAC_189]. However, these works remain largely anchored in fiber-specific channel models and DSP paradigms, with limited consideration of how insights might transfer to wireless optical or hybrid fiber-wireless scenarios.

**FSO Channel Modeling and Photonic-THz Surveys.** Free-space optical (FSO) and photonic-terahertz research constitutes a third cluster of related work. Conceptual overviews of optical integrated sensing and communication discuss architectures, potentials, and challenges for FSO-ISAC [O_ISAC_021], while emerging demonstrations of MIMO FSO with fiber Bragg grating sensors illustrate 6G IoT application potential [O_ISAC_199]. Waveform-centric studies—including OCDM-based FMCW design for FSO ISAC [O_ISAC_035] and photonic-based flexible ISAC with multiple targets detection capability [O_ISAC_058]—advance signal processing techniques but do not synthesize findings across the FSO–fiber–VLC divide. In the photonic-THz domain, survey-style treatments exploring integrated waveforms for THz-ISAC systems summarize recent worldwide research efforts and extrapolate technological evolution tendencies [O_ISAC_070], complemented by demonstrations achieving 251 Gbps real-time communication with cm-scale sensing [O_ISAC_016] and THz-over-fiber systems based on orthogonal chirp division multiplexing [O_ISAC_077]. These works collectively highlight photonic-THz as the highest-CRQ$_{\Delta}$ modality but do not bridge to VLC or fiber sensing communities.

**True O-ISAC Surveys (Tier-1).** Within our systematic corpus of 220 studies, only one work explicitly frames optical ISAC as its primary subject: the VLC-based LiSAC review [O_ISAC_303]. A separate RIS-for-ISAC survey [O_ISAC_163] provides enabling-technology context but remains RF/THz-centric and is therefore treated as Tier-2 in Table I. Notably, the VLC review does not apply a systematic methodology (e.g., PRISMA) and remains anchored to a single modality rather than spanning the full fiber–FSO–VLC–photo-THz spectrum under a unified physical-layer abstraction.

**Gap Synthesis.** Within the optical-ISAC corpus considered in this review, our analysis reveals five critical gaps that distinguish the current landscape from a unified framework. First, no cross-modality, modality-agnostic taxonomy spanning fiber–FSO–VLC/LiFi–photo-THz under a single PHY abstraction is available; existing survey-style works typically remain medium-centric (e.g., [O_ISAC_303] for VLC, [O_ISAC_006] for fiber), often with overlapping or inconsistent definitions. Second, among the identified survey-style works in the considered corpus, PRISMA-aligned systematic methodology is not adopted; most contributions employ narrative or tutorial-style treatments that limit reproducibility and evidence-traceable synthesis. Third, metric normalization remains unresolved: no standardized reporting contract consistently separates bandwidth-limited physical resolution (e.g., $\Delta r_{\min} = v/(2B_{\text{eff}})$) from estimator-dependent accuracy (e.g., RMSE/$\sigma_r = \sqrt{\mathbb{E}[(\hat r - r)^2]}$) and information-/estimation-theoretic bounds (CRB/FIM), nor does a common convention exist for signal-quality reporting across modalities (electrical SNR after photodetection versus optical OSNR/power-budget conventions). Fourth, cross-domain technology transfer is underexplored, with limited explicit evaluation of portability of waveform/probing strategies and DSP abstractions across media (e.g., from coherent fiber sensing to FSO/VLC). Fifth, emerging enabling technologies—such as optical RIS and optical phased arrays—are treated in a fragmented, technology-centric manner rather than through a systematic synthesis of integration pathways and modality-agnostic design abstractions. Table I summarizes these limitations by comparing this survey against representative Tier-1 and Tier-2 survey-style works; it reports *context descriptors* (Tier, modality scope, integration depth, methodology) and evaluates **five gap axes** (taxonomy, metrics, benchmarking, transfer, enablers).

These gaps collectively establish the rationale for this survey: a PRISMA-compliant systematic review that unifies O-ISAC across all four modalities, establishes a standardized taxonomy and reporting contract, and synthesizes quantitative trade-off frontiers to guide future research.

> **Lesson 1:** Without axis-aligned reporting (scope–taxonomy–metrics–benchmarks–transfer), the existing survey landscape cannot be converted into a defensible cross-modality O-ISAC research gap.





## E. Contributions of This Survey

To close the five gaps identified in Section I-D, we provide evidence-backed contributions grounded in the PRISMA corpus and extraction schema; each item includes a compact Contribution-Gap-Section mapping:

1. **PRISMA evidence base and quality scoring (Gap 2):** We apply the PRISMA 2020 protocol [14] to a unified corpus of 220 studies with bibliographic year metadata available for 219 records (210 in 2020-2025), and we report complete 5-dimension TQAF scores for 208 studies. *Contribution-Gap-Section:* Gap 2 -> Section III.

2. **Cross-modality taxonomy with measured coverage (Gap 1):** We construct a unified taxonomy spanning fiber, FSO, VLC/visible-light, photo-THz, and hybrid O-ISAC; the extracted medium labels include 46 fiber, 19 FSO, 26 VLC/visible-light/UV, 1 photo-THz, and 116 hybrid studies (optical-THz bridging can appear under hybrid depending on the extraction label ontology). *Contribution-Gap-Section:* Gap 1 -> Section IV.

3. **Standardized reporting contract and trade-off synthesis (Gap 3):** We normalize reporting using $\Delta r_{\min}$, $\sigma_r$, and $\text{CRQ}_{\Delta}$ and quantify coverage: 217 studies report data-rate metrics, 213 report a resolution-type metric ($\Delta r_{\min}$ in ranging or $\Delta z$/spatial granularity in fiber), 208 report $\sigma_r$, and 171 report CRB/CRLB values; 213 studies report both rate and a resolution-type metric, enabling $\text{CRQ}_{\Delta}$ comparisons where $\Delta r_{\min}$ is available (N_rate_and_resType = 213; N_rate_and_Drmin = 160). *Contribution-Gap-Section:* Gap 3 -> Section V.

4. **Enabler-centric synthesis across optical platforms (Gap 5):** We quantify enabling-technology prevalence to ground Section VI, including machine learning (53 studies), optical RIS (ORIS, 8 studies), and optical phased arrays (OPA, 7 studies), and relate these tags to the integration pathways discussed in the enabler section. *Contribution-Gap-Section:* Gap 5 -> Section VI.

5. **Cross-domain transfer map tied to applications (Gap 4):** We build a modality-application transfer map in Section VII; 15 application domains appear in >=2 modality classes (8 domains in >=3), with high-frequency domains including industrial manufacturing (65), vehicular (60), indoor positioning (56), and 6G networking (46). *Contribution-Gap-Section:* Gap 4 -> Section VII.

> **Lesson 2:** A systematic, PRISMA-based methodology enables reproducible evidence synthesis and uncovers research gaps that are invisible in narrative reviews.

## F. Organization of This Paper

The remainder of this survey is organized as follows:

- **Section II (Technical Fundamentals)**: Provides the physical-layer foundations of optical sensing and communication, covering modulation schemes, channel models, and hardware architectures.

- **Section III (Methodology)**: Details the PRISMA 2020-compliant systematic review methodology, including search strategy, eligibility criteria, study selection process, and the 5-dimensional Technical Quality Assessment Form (TQAF).

- **Section IV (Unified O-ISAC Taxonomy)**: Presents the proposed cross-domain taxonomy, organizing 220 studies by medium, integration mechanism, and signal dimension.

- **Section V (Performance Trade-off Analysis)**: Synthesizes quantitative performance metrics to characterize rate-resolution trade-offs and Pareto-optimal operating regions.

- **Section VI (Enabling Technologies)**: Analyzes key enabling technologies including ORIS, OPA, photonics-assisted signal generation, and machine learning integration.

- **Section VII (Applications and Use Cases)**: Synthesizes representative use cases across smart infrastructure (including industrial IoT motifs), indoor environments (including healthcare-oriented motifs), automotive transportation, underwater/subsea monitoring, and space/satellite networks, and then consolidates cross-domain transfer in VII-F with dual-view consistency analysis in VII-G.

- **Section VIII (Open Challenges and Research Roadmap)**: Synthesizes five challenge domains, organizes a capstone dependency-aware research agenda toward 6G integration, and closes with a cross-section alignment audit that verifies continuity with Sections V-VII.

- **Section IX (Conclusions)**: Summarizes the key findings and provides closing remarks.

## G. Notation and Acronyms

For the reader's convenience, the mathematical notation conventions and the most frequently used acronyms in this paper are defined in Tables III and IV, respectively.

### Table III: Mathematical Notation Conventions

| Symbol | Definition |
|:------:|:-----------|
| $\lambda$ | Optical wavelength (nm) |
| $B_{\text{eff}}$ | Effective signal bandwidth (Hz) |
| $R$ | Data rate (bit/s) |
| $d$ | Target distance/range (m) |
| $\Delta r_{\min}$ | Bandwidth-limited (two-way) range resolution (m) |
| $\sigma_r = \sqrt{\mathbb{E}[(\hat r - r)^2]}$ | Range estimation error / RMSE (m) |
| $\text{SNR}$ | Signal-to-noise ratio |
| $\text{BER}$ | Bit error rate |
| $\alpha$ | Power allocation factor (C&S trade-off) |

### Table IV: List of Frequently Used Acronyms

| Acronym | Definition |
|:--------|:-----------|
| **ISAC** | Integrated Sensing and Communication |
| **O-ISAC** | Optical Integrated Sensing and Communication |
| **ISAC-OF** | Integrated Sensing and Communication in Optical Fiber |
| **DFS** | Distributed Fiber Sensing |
| **DAS** | Distributed Acoustic Sensing |
| **VLC** | Visible Light Communication |
| **FSO** | Free-Space Optical |
| **OWC** | Optical Wireless Communication |
| **LFM** | Linear Frequency Modulation |
| **OFDM** | Orthogonal Frequency Division Multiplexing |
| **DCO-OFDM** | DC-biased Optical OFDM |
| **OCDM** | Orthogonal Chirp Division Multiplexing |
| **IM/DD** | Intensity Modulation / Direct Detection |
| **ORIS** | Optical Reconfigurable Intelligent Surface |
| **OPA** | Optical Phased Array |
| **PIC** | Photonic Integrated Circuit |
| **CCR** | Corner Cube Reflector |
| **RO-ISAC** | Retroreflective O-ISAC |
| **φ-OTDR** | Phase-Sensitive Optical Time-Domain Reflectometry |
| **SMF** | Single-Mode Fiber |
| **FMF** | Few-Mode Fiber |
| **MCF** | Multi-Core Fiber |
| **WDM** | Wavelength Division Multiplexing |
| **DSCM** | Digital Subcarrier Multiplexing |
| **THz** | Terahertz |
| **MIMO** | Multiple-Input Multiple-Output |
| **PRISMA** | Preferred Reporting Items for Systematic Reviews and Meta-Analyses |
| **TQAF** | Technical Quality Assessment Form |
| **RMSE** | Root Mean Square Error |
| **CRB** | Cramér-Rao Bound |

---

# REFERENCES

[1] ITU-R, "Framework and overall objectives of the future development of IMT for 2030 and beyond," Recommendation ITU-R M.2160-0, Nov. 2023.

[2] C. de Lima *et al.*, "Convergent Communication and Sensing in 6G: Visions, Prospects, and Challenges," *IEEE Communications Magazine*, vol. 59, no. 1, pp. 12–18, Jan. 2021.

[3] F. Liu *et al.*, "Integrated Sensing and Communications: Towards Dual-Functional Wireless Networks for 6G and Beyond," *IEEE J. Sel. Areas Commun.*, vol. 40, no. 6, pp. 1631–1652, Jun. 2022.

[4] IEEE 802.11 Working Group, "Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications—Amendment: Enhancements for WLAN sensing," IEEE Std 802.11bf (Draft), 2024.

[5] Z. Zhang *et al.*, "6G Wireless Networks: Vision, Requirements, Architecture, and Key Technologies," *IEEE Veh. Technol. Mag.*, vol. 14, no. 3, pp. 28–41, Sep. 2019.

[6] M. Z. Chowdhury *et al.*, "Optical Wireless Hybrid Networks for 5G and Beyond Communications—A Survey," *IEEE Commun. Surveys Tuts.*, vol. 22, no. 2, pp. 1090–1121, Secondquarter 2020.

[7] H. Haas, "LiFi is a Paradigm-Shifting 5G Technology," *Reviews in Physics*, vol. 3, pp. 26–31, 2018.

[8] M. A. Khalighi and M. Uysal, "Survey on Free Space Optical Communication: A Communication Theory Perspective," *IEEE Commun. Surveys Tuts.*, vol. 16, no. 4, pp. 2231–2258, Fourthquarter 2014.

[9] F. Liu *et al.*, "Integrated Sensing and Communication: Towards Dual-Functional Wireless Networks for 6G," *IEEE Commun. Surveys Tuts.*, vol. 24, no. 3, pp. 1726–1767, Thirdquarter 2022.

[10] A. Liu *et al.*, "A Survey on Fundamental Limits of Integrated Sensing and Communication," *IEEE Commun. Surveys Tuts.*, vol. 24, no. 2, pp. 994–1034, Secondquarter 2022.

[11] Y. Zhuang *et al.*, "A Survey of Positioning Systems Using Visible LED Lights," *IEEE Commun. Surveys Tuts.*, vol. 20, no. 3, pp. 1963–1988, Thirdquarter 2018.

[12] X. Bao and L. Chen, "Recent Progress in Distributed Fiber Optic Sensors," *Sensors*, vol. 12, no. 7, pp. 8601–8639, 2012.

[13] M. A. Esmail, H. Fathallah, and M.-S. Alouini, "A Survey on the Impact of Rain and Fog on Free Space Optical Communication," *IEEE Commun. Surveys Tuts.*, vol. 19, no. 2, pp. 1194–1222, Secondquarter 2017.

[14] M. J. Page *et al.*, "The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews," *BMJ*, vol. 372, p. n71, Mar. 2021.

---

*Note: Corpus paper identifiers [O_ISAC_XXX] refer to studies in the systematic review database. Full bibliographic details are provided in the Supplementary Material.*
