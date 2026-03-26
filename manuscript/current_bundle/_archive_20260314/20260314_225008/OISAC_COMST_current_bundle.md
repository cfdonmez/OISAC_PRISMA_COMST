# Review Bundle

## drafts/section_01_introduction.md

# I. INTRODUCTION

## A. The Convergence of Sensing and Communication: A 6G Imperative

The escalating complexity of the electromagnetic environment has intensified demands for ultra-reliable wireless connectivity, driving significant interest in Integrated Sensing and Communication (ISAC) systems [O_ISAC_070:1]. This integrated approach enables ultra-efficient spectrum utilization and significantly reduces hardware costs, and more importantly, establishes a foundational framework for achieving seamless connectivity in future wireless networks [O_ISAC_070:2]. ISAC has now emerged as a core enabler in 6G networks and is recognized as one of the six key usage scenarios by both the ITU-R IMT-2030 framework [O_ISAC_162:1] and 3GPP [O_ISAC_162:2], spanning the coexistence, cooperation, and co-design of communication and sensing functionalities [O_ISAC_070:3].

The intelligence of future society necessitates an immediate requirement for ultra-high-speed communication and ultra-resolution sensing in the 6G era [O_ISAC_016]. As intelligent applications—including robot navigation, augmented reality, autonomous driving, and human–machine interaction—continue to proliferate, these emerging services require the capability of highly-reliable wireless communication and high-accuracy environment sensing simultaneously [O_ISAC_351]. Wireless communication frequency bands are gradually transitioning to higher frequency ranges—encompassing millimeter-wave (mmWave) and terahertz (THz)—to fulfill the ultra-high data rate requirements of this vision. **Despite significant progress in RF-based ISAC**, the conventional independent design of communication and sensing systems generally occupies disjoint spectral resources, profoundly aggravating spectrum congestion [O_ISAC_351]. Moreover, using traditional all-electronic approaches to generate mmWave or THz signals will inevitably encounter challenges such as high complexity and **bandwidth limitation**, which will increase the system costs significantly [O_ISAC_286]. To the best of our knowledge, conventional RF-ISAC systems face three fundamental constraints:

1. **Spectrum Congestion**: With the rapid advances of wireless mobile devices, RF communication and sensing systems face challenges such as spectrum congestion, limited bandwidth, and susceptibility to electromagnetic interference [O_ISAC_068]. The exponentially growing demand for mobile data, coupled with stringent sensing resolution requirements of emerging applications (holographic telepresence, digital twins, autonomous navigation), has created significant pressure on the congested RF spectrum [O_ISAC_161].

2. **Limited Resolution and Bandwidth**: The spatial resolution achievable in the mmWave band is fundamentally limited to approximately centimeter-level, insufficient for millimeter-precision applications [O_ISAC_021]. Furthermore, RF-ISAC systems commonly suffer from **spectrum scarcity, high power consumption, and limited sensing capabilities** [O_ISAC_203].

3. **Hardware Constraints**: Purely electrical THz systems struggle to achieve the wide bandwidth and flexible reconfigurability demanded by 6G [O_ISAC_070]. The construction of mmWave/THz ISAC systems using purely electrical means is associated with bandwidth and frequency adjustability limitations that increase overall system complexity [O_ISAC_286].

**Recent advances in photonic THz techniques have opened new opportunities** for transcending these RF limitations. **Optical Integrated Sensing and Communication (O-ISAC)** has emerged as a transformative paradigm that unifies perception, transmission, and processing on optical carriers [O_ISAC_021]. **Fig. 1** illustrates this paradigm evolution through three distinct phases: **(A)** the fundamental spectral and bandwidth constraints of conventional RF-ISAC; **(B)** the transformative opportunities of the optical domain, leveraging the 28.3–845 THz spectrum to enable Tbps-class capacity and mm-scale resolution; and **(C)** the unified taxonomy of this survey, which branches O-ISAC into fiber-based, wireless (FSO/THz), and VLC modalities. Our systematic analysis of **220 peer-reviewed O-ISAC studies (2020–2025)** reveals that optical ISAC prototypes have pushed these limits: photonic-terahertz integration has achieved **120 Gbps wireless throughput with 2.5 mm sensing resolution** [O_ISAC_105], corresponding to $\text{CRQ}_{\Delta} \approx 4.8\times10^{13}$ bps/m [O_ISAC_105]. Earlier photonic sub-THz demonstrations report $\text{CRQ}_{\Delta}$ on the order of $1.0\times10^{13}$ bps/m [O_ISAC_016].

![Fig. 1. The O-ISAC paradigm evolution. (A) RF-ISAC systems in sub-6 GHz/mmWave bands often face deployment-constrained spectrum and hardware limits, motivating a transition toward photonic carriers to pursue Tbps-class capacity and mm-scale sensing targets. (B) Optical-ISAC leverages the broad photonic spectrum (≈28.3–845 THz), with implementations clustering in operational windows (telecom for fiber and NIR/visible/photonic-THz for wireless). The survey taxonomy branches Optical-ISAC into fiber-based, free-space/photonic-THz, and VLC/LiFi modalities, each characterized by distinct signal models and dominant impairments.](figures/fig1.png)


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

![Fig. 2. Physical mechanisms behind the three competitive advantages of O-ISAC. (Left) Capacity scaling is achieved via dense Multiplexing (WDM/SDM), enabling aggregate rates of 241.85 Tb/s (wired) [O_ISAC_046] and dense parallel channels (wireless) [O_ISAC_021]. (Center) Sensing precision is driven by ultra-wide effective bandwidth, enabling wireless range resolution down to $\Delta r_{\min} = 2.5$ mm and $\text{CRQ}_{\Delta}$ of $4.8\times10^{13}$ bps/m (480 Gbps/cm) [O_ISAC_105]. (Right) Spatial isolation is inherent to narrow optical beams, reducing multi-user interference and RF-EMI susceptibility compared to wide RF sectors.](figures/fig2.png)


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

![Fig. 3. The unified taxonomy of O-ISAC modalities derived from a systematic PRISMA-compliant analysis of 220 primary studies (2020–2025). (Top-Left) Fiber O-ISAC (Cabled) leveraging existing DAS/DSCM infrastructure for long-haul (>100 km) sensing and Tb/s-scale data transmission. (Top-Right) Free-Space Optical (FSO) O-ISAC for outdoor inter-building links utilizing coherent detection and atmospheric compensation. (Bottom-Left) Visible Light Communication (VLC) O-ISAC for indoor environments using LED infrastructure for joint illumination, high-speed connectivity, and sub-centimeter positioning. (Bottom-Right) Photonic Terahertz (Photo-THz) O-ISAC bridging the optical and wireless THz domains to achieve the highest reported $\text{CRQ}_{\Delta}$ metrics (>100 Gbps/cm, i.e., >$1.0\times10^{13}$ bps/m).](figures/fig3.png)


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


## drafts/section_02_fundamentals_draft.md

# II. TECHNICAL FUNDAMENTALS OF O-ISAC

## A. Unified O-ISAC System Model and Integration Paradigms

### A.1 Canonical Joint Waveform/Resource Model
Design rationale: We define a joint design variable set that spans waveform parameters (bandwidth, chirp rate, pilot structure, coding), optical front-end parameters (source, modulation, detection), and sensing-task parameters (range/angle/velocity versus fiber spatial granularity). This compact variable set supports cross-modality comparisons without erasing the physical constraints that distinguish coherent and IM/DD architectures.

**Generic baseband observation (complex coherent model):**
\[
\mathbf{y}(t)=\mathbf{H}(t;\boldsymbol{\theta})\mathbf{s}(t)+\mathbf{w}(t),
\]
where \(\mathbf{y}(t)\) is the received complex baseband observation, \(\mathbf{s}(t)\) is the transmitted complex baseband waveform, \(\mathbf{H}(t;\boldsymbol{\theta})\) is a parametric operator embedding sensing parameters \(\boldsymbol{\theta}\) (e.g., delay, Doppler, angle), and \(\mathbf{w}(t)\) is receiver noise.

**IM/DD observation (real, nonnegative intensity constraint):**
\[
y(t)=\mathcal{R}\,\big(x(t)\ast h(t)\big)+n(t),\qquad x(t)\ge 0,
\]
where \(y(t)\) is the electrical observation after direct detection, \(x(t)\) is the transmitted optical intensity waveform, \(h(t)\) is the intensity channel impulse response, \(\mathcal{R}\) is photodetector responsivity, and \(n(t)\) is additive electrical noise. Here \(x(t)\) denotes the modulated optical intensity (post square-law abstraction), not the optical field amplitude; the nonnegativity constraint follows.

**Measurement-plane contract.** We map each reported metric \(m\) to a measurement plane via
\[
\pi(m)\in\{\text{OPTICAL\_PLANE},\;\text{ELECTRICAL\_PLANE},\;\text{AMBIGUOUS}\},
\]
where OPTICAL\_PLANE refers to pre-detection optical field/power (\(E(t)\), \(P(t)=|E(t)|^2\ge 0\)) and ELECTRICAL\_PLANE refers to post-detection electrical baseband observations. OSNR and electrical SNR must be reported on their native planes, and OSNR-to-SNR conversion is prohibited unless a source provides an explicit receiver model (Metric Governance). Generic "SNR" without an optical/electrical cue remains AMBIGUOUS and is not used to justify plane separation (Metric Governance). For ranging tasks, the delay-to-range relation \(\tau=2r/v\) underpins \(\Delta r_{\min}=v/(2B_{\text{eff}})\), whereas fiber DAS reports spatial granularity via \(\Delta z\) (gauge/segment length) rather than \(\Delta r_{\min}\) (Metric Governance).

Evidence alignment: Representative studies report BER against OSNR (explicitly optical signal-to-noise ratio) for coherent optical links [O_ISAC_132], [O_ISAC_076].
Representative studies separately report electrical SNR after photodetection for BER/RMSE evaluation [O_ISAC_061], [O_ISAC_100], [O_ISAC_023]. Consistent with the governance contract, we keep these as different measurement planes and do not infer one from the other without an explicit receiver/noise model.

### A.2 Integration Paradigms (Communication-centric / Sensing-centric / Joint Design)
Design rationale: For cross-modality synthesis, we classify integration by mechanism (shared waveform, shared hardware, shared time/frequency resources, shared processing) rather than by medium. This mechanism-first lens keeps fiber/FSO/VLC/photonic-THz cases comparable while preserving their physical constraints.

**Communication-centric:** Communication performance is primary; sensing operates under communication-driven resource limits. A minimal exemplar is maximize \(R\) subject to \(J_{\text{sense}}(\boldsymbol{\theta})\le \varepsilon\).

**Sensing-centric:** Sensing fidelity is primary; communication is constrained to satisfy a service floor. A minimal exemplar is minimize \(J_{\text{sense}}(\boldsymbol{\theta})\) subject to \(R\ge R_0\) (and/or BER \(\le \beta\)).

**Joint design:** Communication and sensing are co-optimized as explicit multi-objective trade-offs. A minimal exemplar is minimize \([J_{\text{sense}}(\boldsymbol{\theta}),\; -R]\) (Pareto) or minimize \(\alpha J_{\text{sense}}(\boldsymbol{\theta})-(1-\alpha)R\), where \(R\) is throughput and \(J_{\text{sense}}\) is a sensing loss (e.g., estimation MSE or a ranging-error proxy).

These three paradigms denote operating intent (not mutually exclusive hardware classes); one architecture may move between them by changing constraints or operating point.

Paradigm-to-mechanism bridge:
- Communication-centric -> shared processing / shared resources -> sensing piggybacks on communication signaling.
- Sensing-centric -> shared waveform / shared hardware -> communication is embedded under sensing-driven constraints.
- Joint design -> shared waveform + shared processing -> explicit co-optimization couples both objectives.

We define an integration depth variable
\[
d_{\text{int}}\in\{0,\;1/2,\;1\},
\]
where \(d_{\text{int}}=0\) corresponds to coexistence, \(d_{\text{int}}=1/2\) to partial sharing/cooperation, and \(d_{\text{int}}=1\) to full co-design. This internal axis is used later to align taxonomy and trade-off synthesis without rewriting modality-specific models.

Evidence alignment: A.2 defines a survey-internal synthesis scaffold for later sections; it does not claim prevalence or superiority of any paradigm in this subsection, so no paper-specific performance claim is asserted here.

**Lesson (A):** A unified system model combined with explicit measurement-plane mapping is necessary to make later taxonomy and trade-off statements falsifiable rather than narrative.

---

## B. Propagation and Channel Models Across Modalities
This subsection defines a modality-aware channel layer for O-ISAC. The aim is not to rank modalities, but to expose dominant propagation impairments under a common operator view. The measurement-plane contract from Section II-A remains binding: channel modeling does not justify OSNR-to-SNR conversion, and optical/electrical plane separation is preserved.

### B.1 Fiber Channel (Guided Medium)
Design rationale: Fiber links are naturally represented by a linear dispersive baseband model in most communication analyses, with nonlinear wave dynamics added when launch power and distance require it.

A baseline model is
\[
\mathbf{y}(t)=\mathbf{G}_{\text{disp}}(t)\ast \mathbf{s}(t)+\mathbf{w}(t),
\]
where \(\mathbf{G}_{\text{disp}}(t)\) captures chromatic-dispersion-dominated propagation.

For nonlinear regimes, a conceptual NLSE form is
\[
\frac{\partial A(z,t)}{\partial z}= -\frac{\alpha}{2}A - j\frac{\beta_2}{2}\frac{\partial^2 A}{\partial t^2} + j\gamma|A|^2A + \eta(z,t),
\]
where \(A(z,t)\) is the optical field envelope, \(\alpha\) is attenuation, \(\beta_2\) is group-velocity dispersion, and \(\gamma\) is the nonlinear coefficient. For sensing tasks, fiber reports spatial granularity via \(\Delta z\) (gauge/segment length), not wireless-style \(\Delta r_{\min}\) (Metric Governance).

Evidence alignment: This part is theory-standard modeling; no paper-specific prevalence claim is asserted here.

### B.2 FSO Channel (Atmosphere + Pointing)
Design rationale: FSO propagation is dominated by multiplicative effects (turbulence and misalignment/pointing) plus path attenuation.

A compact IM/DD-friendly form is
\[
y = h_{\text{turb}}\,h_{\text{point}}\,h_{\text{att}}\,x + n,\qquad x\ge 0,
\]
with
\[
h_{\text{att}}=\exp(-\kappa d),
\]
where \(d\) is propagation distance and \(\kappa\) is the extinction coefficient. Turbulence statistics are typically modeled with log-normal or Gamma-Gamma families depending on regime assumptions.

Evidence alignment: Representative studies explicitly model Beer-Lambert attenuation and pointing/turbulence effects in FSO channel setup and analysis [O_ISAC_035], [O_ISAC_005].

### B.3 VLC Channel (Lambertian + LoS/NLoS Impulse Response)
Design rationale: VLC behavior is geometry-driven and typically represented by an intensity impulse response under Lambertian emission assumptions.

A generic representation is
\[
h(t)=h_{\text{LOS}}(t)+h_{\text{NLOS}}(t),
\]
where LoS and reflected components are separated in the CIR. Shot noise, thermal noise, and ambient-light-induced noise are included according to receiver setup.

Evidence alignment: Representative VLC/OWC studies model LoS/NLoS decomposition and Lambertian emission within impulse-response channel formulations [O_ISAC_039], [O_ISAC_022].

### B.4 Photonic-THz Bridging (Optical Generation/Distribution + THz Propagation)
Design rationale: Photonic-THz O-ISAC is inherently a two-stage channel chain: optical-domain generation/distribution followed by THz wireless propagation.

We therefore model this link as a split channel: an optical stage (carrier generation/distribution and optical front-end impairments) plus a THz stage (wireless propagation with multipath/frequency-selective effects). This split avoids plane conflation and keeps impairment attribution explicit.

Evidence alignment: Representative photonics-assisted mmWave/THz studies discuss multipath and frequency-selective channel effects in fiber-wireless settings [O_ISAC_241], [O_ISAC_077].

**Lesson (B):** Channel models are modality-specific in dominant impairments, but the reporting contract (plane separation plus metric governance) is modality-invariant.

---

## C. Transceiver and Hardware Abstractions (What is Common, What is Modality-Specific)
This subsection defines a hardware abstraction layer that stays valid across fiber/FSO/VLC/photonic-THz implementations. The focus is architectural role (source/modulator, receiver/detection, wavefront control), not device-level ranking.

### C.1 Sources and Modulators
Design rationale: The source-modulator stack determines whether operation is coherent or IM/DD and sets the feasible waveform interface for joint communication-sensing design.

Evidence alignment: Representative photonic-THz chains use ECL-driven MZM/IQ-modulator front-ends consistent with coherent operation [O_ISAC_029]. IM/DD-oriented VLC implementations use LED/LD intensity modulation with nonnegative optical intensity constraints [O_ISAC_001].

### C.2 Receivers and Detection
Design rationale: Receiver architecture defines the observation plane and therefore the admissible signal-quality interpretation.

We restate the measurement-plane contract for receiver-side interpretation:
\[
\pi(m)\in\{\text{OPTICAL\_PLANE},\;\text{ELECTRICAL\_PLANE},\;\text{AMBIGUOUS}\},
\]
where OSNR is optical-plane and electrical SNR/ESNR is post-detection electrical-plane; OSNR-to-SNR conversion is prohibited without an explicit receiver/noise model (Metric Governance).

Evidence alignment: Coherent receiver implementations explicitly use optical-hybrid/balanced-photodetector style detection chains [O_ISAC_028], [O_ISAC_029]. IM/DD receiver implementations explicitly use photodiode-based direct detection and O/E conversion [O_ISAC_001], [O_ISAC_023].

### C.3 Beamforming/Wavefront Control Enablers
Design rationale: Spatial-control elements (especially OPA-class front ends) are treated as enablers that shape beam directionality and angular observability while remaining compatible with the source-modulator-channel-detector abstraction.

A generic array response model for steering/sensing is
\[
\mathbf{a}(\phi)=\left[1,\;e^{jkd\sin\phi},\;\ldots,\;e^{jkd(N-1)\sin\phi}\right]^{\top}.
\]

Evidence alignment: Representative OW-ISAC studies explicitly use OPA-based beamforming front ends and discuss their role in joint communication-sensing operation [O_ISAC_061], [O_ISAC_091].

**Lesson (C):** Hardware commonality is abstraction-level (source-modulator-receiver-wavefront control), while implementations remain modality-specific.

---

## D. Sensing Principles and the Metric Contract (Resolution vs Accuracy vs Bounds)
Design rationale: Section II-D defines the metric contract that keeps sensing comparisons valid across O-ISAC modalities. The key separation is between physics-limited resolution, estimator-dependent accuracy, and bound-based limits.

### D.1 Ranging/ToF/FMCW/LFM Fundamentals
Design rationale: A two-way ranging convention provides a shared physical baseline for ToF/FMCW/LFM sensing and ties resolution to effective bandwidth instead of estimator choice.

We adopt the two-way delay model with
\[
\Delta r_{\min} := \frac{v}{2B_{\text{eff}}},
\]
where \(v=c\) in free space and \(v\approx c/n_g\) in guided media. For ranging tasks, \(\tau=2r/v\) links delay and range. Fiber DAS/OTDR records are mapped to \(\Delta z\) (gauge/segment length), not \(\Delta r_{\min}\) (Metric Governance).

Evidence alignment: Representative photonic ranging studies report bandwidth-limited resolution forms consistent with \(c/(2B)\) under the two-way convention [O_ISAC_026], [O_ISAC_034].

### D.2 Accuracy (Estimator-Dependent) and CRB/FIM Bounds
Design rationale: Accuracy is estimator- and noise-model-dependent, so it must remain distinct from bandwidth-limited resolution.

Estimator-dependent accuracy is defined as
\[
\sigma_r := \sqrt{\mathbb{E}[(\hat r-r)^2]},
\]
while a canonical delay-bound form is
\[
\mathrm{var}(\hat\tau) \ge \frac{1}{8\pi^2\beta^2\,\mathrm{SNR}} \Rightarrow \mathrm{var}(\hat r) \ge \left(\frac{v}{2}\right)^2\mathrm{var}(\hat\tau).
\]
Here SNR is an abstract estimator-plane quantity unless a source explicitly fixes the measurement plane; this expression does not permit OSNR/electrical-SNR substitution (Metric Governance).

Evidence alignment: This subsection states theory-standard definitions and bound forms; no paper-specific prevalence claim is asserted.

### D.3 Fiber Spatial Granularity (\(\Delta z\)) vs Wireless Range Resolution (\(\Delta r_{\min}\))
Design rationale: Fiber spatial granularity and wireless range resolution are not interchangeable metrics.

We enforce the mapping rule: in DAS/OTDR-like fiber contexts, spatial/distance granularity maps to \(\Delta z\); in bandwidth-limited ToF/FMCW ranging contexts, resolution maps to \(\Delta r_{\min}\). **Comparability warning:** \(\Delta z\) must not be substituted into \(\mathrm{CRQ}_{\Delta}\).

Evidence alignment: Representative fiber sensing works report meter-scale spatial granularity aligned with \(\Delta z\) rather than \(\Delta r_{\min}\) [O_ISAC_006], [O_ISAC_013].

### D.4 Capacity-Resolution Quotient
Design rationale: A compact cross-architecture indicator is useful only under strict admissibility constraints.

We define
\[
\mathrm{CRQ}_{\Delta} := \frac{R}{\Delta r_{\min}} \quad [\mathrm{bps/m}].
\]
\(\mathrm{CRQ}_{\Delta}\) is computed only when both \(R\) and \(\Delta r_{\min}\) are available from the same scenario record and the measurement-plane note is explicit. If only \(\Delta z\) (or generic spatial_resolution_m) is available, \(\mathrm{CRQ}_{\Delta}\) remains undefined.

Evidence alignment: This is a governance-level construct used to control later synthesis; no prevalence claim is asserted in Section II-D.

**Lesson (D):** Without explicit separation of \(\Delta r_{\min}\), \(\sigma_r\)/CRB, and \(\Delta z\), resolution becomes non-isomorphic and cross-study comparisons become non-defensible.

---

## E. ISAC Coupling and Trade-off Foundations (Optimization View)

### E.1 Multiobjective Formulation
Design rationale. We cast O-ISAC co-design as a multiobjective program over a shared design vector $\mathbf{x}$ that collects waveform/resource parameters, optical front-end knobs, sensing-task parameters, and processing knobs, so that communication performance and sensing fidelity are optimized on the same degrees of freedom. Let $f_c(\mathbf{x})$ denote a communication objective (e.g., rate/BER/outage) and $f_s(\mathbf{x})$ denote a sensing objective (e.g., resolution/accuracy/bound), with feasibility $\mathbf{x}\in\mathcal{X}$ capturing nonnegativity, power/bandwidth, and hardware limits. A point $\mathbf{x}^*$ is Pareto-optimal if no other feasible design improves one objective without degrading the other; scalarizations such as $\max_{\mathbf{x}\in\mathcal{X}} f_c(\mathbf{x})-\lambda f_s(\mathbf{x})$ provide convenient operating points but do not exhaust the Pareto set.

Evidence alignment. Representative FSO O-ISAC works explicitly maximize spectral efficiency subject to sensing-precision (Fisher-information) constraints via power allocation, yielding a constrained trade-off formulation. [O_ISAC_048] <!-- evidence: ⟦O_ISAC_048 | # I. INTRODUCTION > ## C. Clipping Noise Statistics > #### III. OPTIMAL POWER ALLOCATION FOR DCO-OFDM | L124-L132 | strength_final=strong | context_verified=YES⟧ -->
Other works formulate joint power-allocation problems for communication-centric and sensing-centric scenarios and solve them with block-coordinate-descent algorithms, explicitly positioning the comm-sensing trade-off within the optimization. [O_ISAC_023] <!-- evidence: ⟦O_ISAC_023 | # Free-Space Optical Integrated Sensing and Communication Based on DCO-OFDM: Performance Metrics and Resource Allocation | L5-L5 | strength_final=strong | context_verified=YES⟧ -->

### E.2 Coupling Mechanisms by Modality
Design rationale. Coupling is most stable when categorized by mechanism rather than modality: resource coupling (power/bandwidth/time), waveform coupling (shared modulation and signaling), hardware coupling (shared optical/electrical front-ends), algorithmic coupling (joint inference/control), and propagation/environment coupling (shared impairments). These mechanisms manifest differently across modalities (e.g., IM/DD nonnegativity, coherent phase access, fiber probe interactions, turbulence/ambient light), but the coupling logic is invariant.

Evidence alignment. Resource coupling is explicit in DCO-OFDM FSO-ISAC studies where communication and sensing objectives are jointly controlled through constrained power allocation [O_ISAC_048], [O_ISAC_023].
Waveform-level coupling is directly shown through waveform-parameter tuning (e.g., power-split control) [O_ISAC_075] and further supported by modulation-index trade-off discussions [O_ISAC_001].
Algorithmic coupling is explicit in optimization pipelines using block-coordinate decomposition and weighted-sum scalarization to tune trade-off operating points under joint constraints [O_ISAC_023], [O_ISAC_052].
Hardware and propagation couplings are retained as synthesis categories in this section; we do not assert cross-corpus prevalence claims for those categories here.

### E.3 What This Enables Later (Bridge to Sections IV-V)
Design rationale. The optimization view provides a common language to map architectures to coupling families, define operating points, and align evaluation protocols with the metric contract (Section II-D). This lets later sections compare designs on consistent objectives without re-interpreting metrics across modalities.

Evidence alignment. Because representative O-ISAC studies already instantiate coupling-aware optimization and explicit trade-off curves (e.g., spectral-efficiency versus sensing-precision under constrained power allocation), Sections IV-V can map architectures to objective forms and admissible operating regions without redefining the metric contract [O_ISAC_048], [O_ISAC_023], [O_ISAC_052].

**Lesson (E):** O-ISAC is a constrained multiobjective design problem; without explicit coupling families and objective forms, cross-architecture comparisons devolve into metric aliasing.


## drafts/section_03_methodology.md

# III. SURVEY METHODOLOGY (PRISMA 2020)

## A. Protocol and Registration
This systematic survey adheres to the **Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) 2020** statement [14] and the PRISMA-S extension for literature search reporting [15]. To ensure transparency and minimize reporting bias, the study protocol—including research questions, search strategy, and eligibility criteria—was registered with the **Open Science Framework (OSF)** on **February 12, 2026** (Registration ID: `7f6wb`). The protocol and associated metadata are accessible via the OSF Registries at https://osf.io/7f6wb.

## B. Information Sources and Search Strategy
A comprehensive literature search for the formal PRISMA identification stage was conducted across three engineering and physics databases: **IEEE Xplore**, **Scopus**, and **Web of Science**, all last searched on **November 30, 2025**. Supplementary search templates were retained for **arXiv** and **TechRxiv** to support preprint monitoring and version tracing, but these supplementary sources did not contribute separate records to the canonical PRISMA flow reported in this review (`other_sources_results = 0`).

The search strategy employed two mandatory concept blocks and one optional refinement block:
1.  **Integrated Sensing and Communication Concepts:** Terms such as "integrated sensing and communication", ISAC, "joint sensing and communication", and related variants.
2.  **Optical Medium Terms:** Terms restricting retrieval to optical carriers and platforms, such as optical/photonic, fiber/fibre, FSO, VLC, LiFi, and LiDAR.
3.  **Physical-Layer Refinement (Optional):** Additional terms such as waveform, modulation, signal model, channel model, or optical front-end, used only when a database required extra disambiguation.

The exact executed search strings for the formal databases are archived in `search/search_strings.md` and logged in `search/search_log.csv`. The literature search was frozen as of **November 30, 2025**.

## C. Eligibility Criteria
To ensure the survey's coherence and focus on the *optical* domain, strict inclusion and exclusion criteria were applied (Table II).

**Inclusion Criteria:**
*   **Domain:** Systems utilizing optical carrier frequencies (infrared, visible, or ultraviolet) for *both* sensing and communication.
*   **Integration:** Studies proposing shared hardware, spectrum, or waveforms (True O-ISAC) or coordinated coexistence.
*   **Content and Time Frame:** Peer-reviewed journal articles and full-length conference papers providing technical depth on physical/link-layer architecture, performance limits, or experimental validation, primarily focused on the **2020–2025** period.

**Exclusion Criteria:**
*   **RF-Only:** ISAC systems operating solely in radio frequency/microwave/THz bands without an optical component.
*   **Disjoint Functionality:** Pure sensing (e.g., standard LiDAR) or pure communication (e.g., standard FSO) papers without integration mechanisms.
*   **Type:** Short abstracts, non-English publications, and grey literature (theses, white papers) lacking peer review.

**TABLE II: Eligibility criteria applied for study selection.**

| Criterion | Inclusion Requirements | Exclusion Conditions |
| :--- | :--- | :--- |
| **Domain Scope** | Systems utilizing **optical carrier frequencies** (IR, Visible, UV) for joint sensing and communication functionalities. | **RF-only ISAC** systems (sub-6 GHz, mmWave, THz) lacking an optical component; Biomedical or chemical sensing without data transmission. |
| **Integration Level** | **True O-ISAC** (shared hardware/waveform) or **Coexistence** (resource sharing) strategies operating at Physical or Link Layer. | **Disjoint systems:** Pure optical sensing (e.g., standard LiDAR) or pure optical communications (e.g., FSO link) without explicit integration mechanisms. |
| **Publication & Time** | Peer-reviewed **journal articles** and **full-length conference papers** published in English, primarily within the **2020–2025** core window. | Short abstracts, non-English publications, and **grey literature** (theses, white papers, patents, technical reports). |
| **Technical Content** | Studies reporting at least one **Sensing metric** (e.g., Detection Probability, CRB, RMSE) AND one **Communication metric** (e.g., BER, SINR, Data Rate). | Studies lacking technical depth on the integration mechanism, trade-offs, or performance evaluation (e.g., high-level vision papers without analysis). |


## D. Study Selection and PRISMA Flow
Study selection followed a three-step PRISMA workflow:
1.  **Deduplication:** Automatic removal of duplicate records across databases.
2.  **Screening:** Title and abstract screening to remove clearly irrelevant (e.g., RF-only or biomedical sensing) records.
3.  **Eligibility:** Full-text review of candidate papers against the inclusion criteria.

Following the registered protocol, two reviewers first calibrated the eligibility criteria on a pilot sample of 50 records, then independently conducted title/abstract screening and full-text eligibility assessment. Any record marked as *Include* or *Unsure* by at least one reviewer advanced to full-text review. Disagreements were resolved by consensus discussion and, where needed, third-reviewer arbitration, with adjudications archived in the structured screening logs.

The canonical aggregate PRISMA counts are maintained in `search/search_log.csv` and `screening/prisma_flow_counts.csv`. In the current repository snapshot, the best available row-level audit artefacts for the earlier stages are `search/dedup_log.csv` and `screening/title_abstract_screening_reconstruction.csv`, while the later stages are directly backed by `screening/fulltext_assessed_reconstruction.csv` (**222** full-text assessed records), `screening/excluded_fulltext_log.csv` (**2** reconciled full-text exclusions), `screening/included_studies_canonical.csv` (final included corpus of **N = 220**), and `screening/screening_log.csv` (consolidated screening ledger). The attrition process is summarised in Fig. 5.

```mermaid
graph TD
    A[<b>Identification</b><br>Records identified from databases<br>(n = 980)<br><i>IEEE Xplore, Scopus, WoS</i>] --> B[Duplicated records removed<br>(n = 280)]
    B --> C[<b>Screening</b><br>Records screened via Title/Abstract<br>(n = 700)]
    C --> D[Records excluded<br>(n = 478)<br><i>Irrelevant topic, RF-only, etc.</i>]
    C --> E[<b>Eligibility</b><br>Full-text articles assessed<br>(n = 222)]
    E --> F[Full-text articles excluded<br>(n = 2)<br><i>Reasons: non-O-ISAC / unverifiable full-text record</i>]
    E --> G[<b>Included</b><br>Studies included in review<br>(n = 220)]
    style G fill:#bef67a,stroke:#33691e,stroke-width:2px
```
*Fig. 5. PRISMA 2020 flow diagram describing the systematic literature search and selection process.*


## E. Data Extraction and Taxonomical Classification
Data extraction was performed using a standardized schema (archived in `analysis/ID_survey_catalog.csv`) to rigorously map the O-ISAC landscape. Key extracted variables include modality coverage (categorizing fiber, FSO, VLC/LiFi, or hybrid regimes), integration depth (distinguishing true waveform/hardware sharing from resource coexistence), quantitative performance metrics (capturing sensing resolution and range alongside communication data rate and BER), and validation level (coding empirical evidence as simulation, experiment, prototype, or analytical). This structured extraction directly feeds the quantitative trade-off frontiers evaluated in Section V.

## F. Quality Appraisal (TQAF)
To assess the reliability of the surveyed literature, we developed a custom **Technical Quality Assessment Form (TQAF)**. Each included study was evaluated independently by two reviewers across five formal dimensions:
1.  **Modelling Fidelity:** Realism of channel and noise models, and their suitability for physical/link-layer evaluation.
2.  **Experimental Validity:** Presence of hardware proof-of-concept versus pure analytical simulation.
3.  **Metric Completeness:** Reporting of joint sensing and communication metrics versus cherry-picked single-function reporting.
4.  **Reproducibility:** Explicitness of parameter assumptions and availability of code or datasets.
5.  **Clarity:** Clear definition of assumptions and physical limitations.

Each dimension was scored on a 0–2 scale (low/moderate/high quality). Any scoring disagreements were resolved by consensus discussion or third-party arbitration. While TQAF scores did not determine study exclusion, they are used throughout Sections IV, VI, and VIII to formally weight the strength of evidence, highlighting methodological gaps where high-impact claims lack rigorous validation.

## G. Data Synthesis Strategy
Given the heterogeneity of metrics across fiber, FSO, and VLC domains—combined with varying assumptions in channel modeling and hardware bounds—a formal statistical meta-analysis was not feasible. Instead, we employ a structured qualitative and quantitative descriptive synthesis driven by the taxonomic model. The literature is first organized by physical modality (Section IV) to reveal domain-specific integration techniques. Following this taxonomic mapping, we conduct a quantitative trade-off analysis (Section V) using visual synthesis tools, such as rate-resolution scatter plots, to identify empirical Pareto frontiers within the joint sensing and communication performance space.


## drafts/section_04_taxonomy.md

# IV. UNIFIED O-ISAC TAXONOMY

Section IV converts the physical-layer contracts of Section II and the systematic evidence base of Section III into a single taxonomy for cross-modality synthesis. The purpose is not to rank modalities, but to define a consistent classification frame that keeps communication-sensing comparisons traceable across fiber, FSO, VLC/LiFi, photonic-THz, and hybrid systems.

## A. Taxonomy Design Principles
### A.1 Design Requirements
Section IV builds a unified O-ISAC taxonomy for cross-modality synthesis, not modality ranking. This distinction is operational rather than rhetorical: the objective is to preserve valid comparisons across heterogeneous implementations by conditioning each comparison on explicit classification variables. Therefore, Section IV-A defines the contract that downstream sections must satisfy before reporting trends, tradeoffs, or representative operating points.

The design starts from a corpus of N=220 studies, which is sufficiently broad to expose repeated structural patterns and sufficiently diverse to reveal incompatibilities in reporting conventions. However, corpus size alone does not guarantee comparability. A taxonomy is useful only if it supports reproducible assignment decisions and traceable evidence paths from each paper to each synthesized statement. Consequently, the design is anchored in three requirements. First, cross-modality comparability: studies must be grouped using axes that separate substrate, integration architecture, observability conditions, and sensing objective. Second, evidence traceability: each axis label must be recoverable from document-level descriptors and retained even when reports are incomplete or partially contradictory. Third, metric-governance consistency with Section II: synthesis is admissible only if measurement plane and metric role remain explicitly governed.

These requirements are motivated by representative cross-modality evidence where integration and sensing objectives are shared but physical assumptions differ materially [O_ISAC_006], [O_ISAC_021], [O_ISAC_068], [O_ISAC_016]. The practical implication is that Section IV does not ask which modality is best in absolute terms. Instead, it asks whether two results are comparable under the same taxonomy state and governance contract. If the answer is no, the comparison is withheld or conservatively qualified.

### A.2 Axis Definitions
To enforce deterministic synthesis, each study \(p\) is mapped to
\[
T(p) = (m(p), i(p), d(p), s(p)).
\]
Here, \(m(p)\) denotes medium class, \(i(p)\) denotes integration class, \(d(p)\) denotes detection/observability class, and \(s(p)\) denotes sensing-task class. Therefore, each axis isolates one comparability condition, and joint interpretation requires all four axes simultaneously.

Axis 1 (Medium) captures propagation and deployment substrate. The dominant classes in the N=220 corpus are hybrid 116/220 (52.7%), fiber 45/220 (20.5%), VLC/LiFi 25/220 (11.4%), and FSO 19/220 (8.6%). These shares support a synthesis-first reading: hybrid systems are common enough to be central to transferability analysis, while fiber, VLC/LiFi, and FSO provide modality-specific anchors for controlled contrasts. However, medium share is not interpreted as superiority; it is interpreted as evidence concentration for conditioned comparison.

Axis 2 (Integration) captures whether sensing and communication rely on shared front-end resources or separate front-ends. Shared front-end designs account for 194/220 (88.2%), while separate front-ends account for 26/220 (11.8%). This skew indicates that most evidence evaluates coupled architectures, so claims about decoupled coexistence should be treated as a minority profile rather than as a default assumption.

Axis 3 (Detection/plane) captures dominant receiver observability through direct and coherent regimes. The corpus contains direct 118/220 and coherent 97/220. Consequently, synthesis across these groups must preserve plane semantics and estimator assumptions instead of collapsing both into one generic detection label.

Axis 4 (Task class) captures sensing objectives. Ranging is the primary task in 162/220 (73.6%), with additional classes including localization, vibration, and detection. Therefore, comparisons should be task-conditioned first and only then interpreted across medium and integration classes.

This axis design follows evidence-grounded cross-modality practice and remains compatible with downstream mapping and governance checks [O_ISAC_021], [O_ISAC_039], [O_ISAC_077].

### A.3 Mapping Rules
Deterministic mapping is required because many O-ISAC papers report multi-stage systems, multi-task outcomes, or partially implicit measurement assumptions. The mapping pipeline follows six fixed principles: structured descriptors first; textual fallback if missing; multi-task keeps all labels with one primary only for tabulation; hybrids remain hybrid; normalize labels before aggregation; contradictions retained and flagged. Therefore, assignment is reproducible while preserving uncertainty rather than hiding it.

Measurement-plane governance follows the Section II contract:
\[
\pi(m) \in \{\text{OPTICAL\_PLANE}, \text{ELECTRICAL\_PLANE}, \text{AMBIGUOUS}\}.
\]
No implicit OSNR-to-SNR substitution is allowed without an explicit receiver/noise model. This rule is falsifiable at extraction time because any substitution must be accompanied by a stated model, otherwise the record is tagged as governed ambiguity.

Metric governance is equally strict. Resolution and accuracy are distinct roles and must remain separate in synthesis statements. In particular, \(\Delta r_{\min}\) and \(\sigma_r\) are not aliases and cannot be pooled as interchangeable evidence. Consequently, aggregate claims are built from role-consistent subsets only, and mixed-role reporting is retained with reduced interpretive weight.

Table IV-A summarizes the operational contract that binds axis assignment, deterministic mapping, and comparability protection.

| Element | Role in taxonomy | Operational rule | Comparability guard |
|:--|:--|:--|:--|
| Design requirements | Defines admissible synthesis scope | Enforce cross-modality comparability, evidence traceability, and Section II metric-governance consistency | Reject unconditioned cross-modality claims |
| Axis 1 (Medium) | Encodes propagation/deployment substrate | Map each study to one medium label, preserving hybrid when present | Compare results only within medium-conditioned subsets |
| Axis 2 (Integration) | Encodes coupling architecture | Assign shared front-end or separate front-ends from explicit implementation evidence | Do not merge co-designed and coexistence regimes |
| Axis 3 (Detection/plane) | Encodes observability regime | Assign direct or coherent with plane-aware interpretation | Block plane conflation across observability regimes |
| Axis 4 (Task class) | Encodes sensing objective | Keep all task labels; use one primary only for tabulation | Avoid cross-task pooling without task conditioning |
| Mapping pipeline | Guarantees reproducible assignment | Apply structured descriptors first, then textual fallback; normalize labels before aggregation | Preserve deterministic labels across reruns |
| Measurement-plane governance | Protects signal-domain validity | Enforce \(\pi(m)\) set membership; require explicit receiver/noise model for OSNR-SNR linkage | No implicit OSNR-to-SNR substitution |
| Metric governance | Protects metric-role validity | Keep resolution and accuracy separate; treat \(\Delta r_{\min}\) and \(\sigma_r\) as non-alias quantities | Prevent metric aliasing in pooled statistics |
| Ambiguity handling | Preserves uncertainty information | Retain contradictions and mark ambiguity at record level | Down-weight ambiguous evidence in conclusions |

A conservative limitation remains necessary. The taxonomy retains and conservatively interprets 84 ambiguity cases, comprising 75 metric-aliasing cases and 9 measurement-plane ambiguity cases. However, these cases are retained by design because exclusion would inflate apparent certainty and reduce auditability. The resulting synthesis is intentionally conservative: it prioritizes traceable comparability over maximal but potentially invalid aggregation [O_ISAC_021], [O_ISAC_039], [O_ISAC_077].

**Lesson (A):** Unified O-ISAC taxonomy is defensible only when four-axis classification, deterministic mapping, and measurement-metric governance are enforced jointly under explicit ambiguity retention.

---

## B. Medium-Based Classes
Section IV-B instantiates Axis 1 by grouping studies according to normalized medium labels and then conditioning mechanism, detection, and task interpretations on that grouping. The objective is cross-modality synthesis with explicit comparability guards, not medium ranking. At the corpus level (N=220), five classes define the main synthesis frame: hybrid 116/220 (52.7%), cabled fiber 45/220 (20.5%), VLC/LiFi 25/220 (11.4%), FSO 19/220 (8.6%), and terahertz 1/220 (0.5%). These five classes cover 206/220 studies (93.6%), while the remaining 14/220 records form a long tail that includes generic wireless, retroreflective wireless, RF-assisted wireless, UV wireless, retroreflective optical, and other low-support labels.

Cross-axis coupling is strong but not uniform. Shared front-end integration is dominant in every main class, yet detection profiles diverge by medium: cabled fiber is coherent-heavy, VLC/LiFi is strongly direct-detection dominant, FSO is mixed with a direct-leading balance, terahertz appears as a single direct-detection record, and hybrid remains near-balanced between coherent and direct with a small residual of other labels. Consequently, medium-based discussion is necessary to prevent false pooling across observability regimes.

Task emphasis is likewise medium-conditioned. Ranging is the primary task in all five main classes, but the secondary pattern differs: vibration and fault monitoring are visible in cabled fiber, localization tails are stronger in VLC/LiFi and hybrid, and FSO remains tightly ranging-centered. This corpus-level composition is consolidated in Fig. IV-1 and then unpacked through the class-specific discussion below. Therefore, each class discussion preserves Section II metric governance: plane-aware interpretation is enforced, no implicit OSNR-to-SNR substitution is made without explicit receiver/noise modeling, and resolution versus accuracy terms are not treated as aliases.

**Table IV-B summarizes medium-based taxonomy classes, corpus share, and dominant operational profiles.**

| Medium class | Corpus share | Dominant integration profile | Dominant detection profile | Dominant sensing emphasis | Representative studies |
|:--|:--|:--|:--|:--|:--|
| Fiber (cabled) | 45/220 (20.5%) | Shared front-end (43/45) | Coherent-leading (27 coherent, 18 direct) | Ranging primary (27), then vibration (8) and 2D localization (6) | [O_ISAC_006], [O_ISAC_033], [O_ISAC_046], [O_ISAC_041], [O_ISAC_090] |
| FSO | 19/220 (8.6%) | Shared front-end (14/19) | Direct/coherent mixed with direct lead (11/8) | Ranging primary (18), 2D localization tail (1) | [O_ISAC_021], [O_ISAC_035], [O_ISAC_005], [O_ISAC_023], [O_ISAC_199] |
| VLC/LiFi | 25/220 (11.4%) | Shared front-end dominant (18/25) | Direct-detection dominant (24/25) | Ranging (12) and localization-heavy tail (10 2D localization, 3 localization) | [O_ISAC_068], [O_ISAC_303], [O_ISAC_039], [O_ISAC_327], [O_ISAC_062], [O_ISAC_009] |
| Photonic-THz / terahertz proxy | 1/220 (0.5%) explicit terahertz class | Shared front-end (1/1) | Direct (1/1) | Ranging (1/1) | [O_ISAC_016], [O_ISAC_077], [O_ISAC_105], [O_ISAC_070], [O_ISAC_029] |
| Hybrid systems | 116/220 (52.7%) | Shared front-end dominant (106/116) | Near-balanced coherent/direct (59/53) with residual labels (4) | Ranging primary (95), 2D localization tail (12), broader multi-task remainder | [O_ISAC_021], [O_ISAC_077], [O_ISAC_041], [O_ISAC_199], [O_ISAC_010] |
| Long-tail media (outside main five) | 14/220 (6.4%) | Mixed, mostly shared front-end | Mostly direct-detection | Heterogeneous low-support tasks | [O_ISAC_039], [O_ISAC_070], [O_ISAC_090] |

### B.1 Fiber (Cabled) O-ISAC
Design rationale: the cabled-fibre class is the guided-medium anchor for O-ISAC because the propagation environment and infrastructure coupling are sufficiently controlled to expose integration and observability effects without free-space geometry uncertainty.

Evidence-conditioned synthesis from the N=220 corpus shows 45 cabled fiber records (20.5%). Integration is predominantly shared front-end (43/45), indicating that most fibre studies evaluate tight sensing-communication coupling rather than loose coexistence. Detection is coherent-leading (27 coherent versus 18 direct), which is consistent with the role of phase-sensitive observability in many fibre sensing pipelines. Primary task distribution is ranging-led (27), followed by vibration (8) and 2D localization (6), with a small remainder in temperature, fault localization, and non-task-labeled records. Consequently, fibre results in Section IV should be interpreted as communication-sensing co-design under guided-channel assumptions, not as a direct baseline for wireless classes [O_ISAC_006], [O_ISAC_033], [O_ISAC_046], [O_ISAC_041], [O_ISAC_090].

Comparability guard: fibre class comparisons remain valid only when measurement-plane semantics are explicit and metric roles are preserved. Therefore, resolution-type quantities and accuracy-type quantities are kept separate, and optical-plane indicators are not converted into electrical-plane SNR claims without explicit receiver/noise models.

### B.2 Free-Space Optical (FSO) O-ISAC
Design rationale: the FSO class isolates optical wireless links where atmospheric and alignment conditions materially affect both communication reliability and sensing confidence, so medium-specific conditioning is mandatory.

Evidence-conditioned synthesis identifies 19 FSO records (8.6%). Integration remains mostly shared front-end (14/19), but separate-front-end coexistence is non-negligible (5/19), so both tightly coupled and partially decoupled implementations appear in this class. Detection is mixed with a direct lead (11 direct, 8 coherent), unlike the stronger coherent bias in cabled fibre. Task concentration is narrow: 18 records are primarily ranging and one record is primarily 2D localization. In contrast to VLC/LiFi, where localization tails are larger, FSO evidence remains predominantly range-oriented. Therefore, cross-class statements involving FSO should be framed as ranging-dominant and observability-mixed, rather than extrapolated from one detection regime [O_ISAC_021], [O_ISAC_035], [O_ISAC_005], [O_ISAC_023], [O_ISAC_199].

Comparability guard: FSO synthesis must preserve explicit detection class and measurement-plane interpretation. Consequently, direct and coherent FSO outcomes are not merged into a single performance statistic when metric definitions differ, and accuracy claims are not inferred from resolution values.

### B.3 Visible Light / LiFi O-ISAC
Design rationale: the VLC/LiFi class captures intensity-domain indoor optical systems where communication, illumination, and sensing objectives are jointly constrained by the same optical front-end and deployment geometry.

Evidence-conditioned synthesis yields 25 VLC/LiFi records (11.3%). Integration is mostly shared front-end (18/25), while separate-front-end designs remain visible (7/25). Detection is highly concentrated in direct mode (24/25), with only one coherent-labeled record. Task emphasis is split between ranging (12) and localization-heavy tails (10 2D localization and 3 localization), which makes VLC/LiFi the strongest localization-oriented class among the main wireless media. However, this localization emphasis coexists with direct-detection observability assumptions; therefore, comparisons against coherent-leading classes require explicit conditioning on receiver model and metric role [O_ISAC_068], [O_ISAC_303], [O_ISAC_039], [O_ISAC_327], [O_ISAC_062], [O_ISAC_009].

Comparability guard: VLC/LiFi evidence is interpreted under intensity-domain measurement semantics, and pooled results preserve Section II separation between resolution and accuracy. In contrast to narrative summaries that interchange these terms, this section treats them as non-alias quantities.

### B.4 Photonic-THz / Optical-THz Bridging
Design rationale: photonic-THz analysis must be framed as a bridge between optical distribution and high-frequency wireless operation, so an explicit single-medium class alone cannot represent the full evidence footprint.

Evidence-conditioned synthesis from the normalized table shows one explicit terahertz record (1/220, 0.5%), labeled as a shared front-end, direct-detection, ranging-primary system. However, anchor-level evidence indicates broader photonic-THz relevance beyond this explicit class: among 39 papers with direct photonic-THz anchors, 31 are mapped to hybrid medium labels, while only one is mapped to explicit terahertz. Therefore, terahertz is used in Section IV-B as an explicit proxy class, while the system-level bridge behavior is interpreted jointly with Section B.5 hybrid evidence [O_ISAC_016], [O_ISAC_077], [O_ISAC_105], [O_ISAC_070], [O_ISAC_029].

Comparability guard: photonic-THz reporting is stage-aware by construction. Consequently, optical-plane and electrical-plane claims are not conflated, and no implicit OSNR-to-SNR substitution is admitted without an explicit cross-plane receiver/noise model.

### B.5 Hybrid Systems
Design rationale: hybrid systems are the structural core of O-ISAC synthesis because they expose cross-medium transferability and integration tradeoffs in one model, rather than isolating single-substrate behavior.

Evidence-conditioned synthesis confirms that hybrid is the majority class with 116/220 records (52.7%). Integration is strongly shared-front-end (106/116), signaling that most hybrid studies pursue deep functional coupling. Detection is near-balanced between coherent and direct (59 and 53), with a four-record residual in envelope detection, unknown, and other labels; this residual is small but analytically important because it signals edge-case observability classes that should not be silently merged. Task profile is ranging-dominant (95), followed by 2D localization (12) and a low-volume multi-task tail (including localization, motion detection, vibration, target detection, and volcanic-ash detection). Consequently, hybrid evidence supports broad transferability analysis, but only when mechanism and detection conditioning remain explicit [O_ISAC_021], [O_ISAC_077], [O_ISAC_041], [O_ISAC_199], [O_ISAC_010].

Comparability guard: hybrid conclusions are valid only under full axis conditioning and Section II governance. Therefore, cross-link reports that mix measurement planes or blur resolution and accuracy are retained as constrained evidence rather than pooled as homogeneous performance, consistent with the contract-violation audit used in Section IV.

**Lesson (B):** Medium class determines dominant physical constraints, but comparability is recovered only when all classes are interpreted under a common metric-governance contract.

---

## C. Integration Mechanisms
This subsection instantiates Axis 2 using the normalized mechanism labels of shared front-end and separate front-ends. At corpus scale (N=220), the mechanism split is strongly asymmetric, with shared front-end architectures in 194/220 studies (88.2%) and separate front-end architectures in 26/220 studies (11.8%). However, the asymmetry is not uniform across media. The medium-conditioned taxonomy tree shows shared front-end dominance in hybrid (106/116, 91.4%) and cabled fiber (43/45, 95.6%), while VLC/LiFi (18/25, 72.0%) and FSO (14/19, 73.7%) retain larger separate front-end fractions. Therefore, integration conclusions must be conditioned on medium and cannot be inferred from global counts alone.

Section IV-C further resolves this axis into four recurrent coupling modes extracted from the Section IV-C evidence table: shared waveform, shared hardware, shared resources, and shared processing. Evidence intensity is reported as unique-paper support under combined direct+indirect anchors, with direct-only counts as a stricter secondary support level. Consequently, the mechanism narrative below is both structural (axis assignment) and evidential (anchor intensity), while remaining compatible with mapping rules that prioritize structured fields, apply label normalization, and retain contradictory anchors for auditability.

**Table IV-C summarizes integration mechanisms, evidence intensity, and dominant trade-off implications.**

| Mechanism Class | Evidence Intensity (Unique Papers, Direct+Indirect) | Typical Coupling Layer | Dominant Benefit | Primary Risk | Representative Studies |
|:--|:--|:--|:--|:--|:--|
| Shared Waveform | 34 (direct+indirect); direct-only: 13 | Signal and waveform design chain | Joint reuse of modulation degrees of freedom under tight synchronization | Strong objective coupling can amplify tradeoffs between rate, robustness, and estimator stability | [O_ISAC_035], [O_ISAC_190], [O_ISAC_304], [O_ISAC_016] |
| Shared Hardware | 15 (direct+indirect); direct-only: 5 | Optical/electrical front-end components and transceiver chain | Reduced platform duplication and tighter timing alignment | Hardware impairment coupling reduces decoupling flexibility and calibration margin | [O_ISAC_021], [O_ISAC_164], [O_ISAC_324], [O_ISAC_056], [O_ISAC_161] |
| Shared Resources | 43 (direct+indirect); direct-only: 16 | Time/frequency/power scheduling and allocation plane | Flexible balancing of sensing and communication utility under deployment constraints | Resource contention can degrade both links if sensing and traffic loads are co-peaked | [O_ISAC_061], [O_ISAC_114], [O_ISAC_142], [O_ISAC_141], [O_ISAC_021] |
| Shared Processing | 30 (direct+indirect); direct-only: 8 | Joint estimation/decoding and algorithmic inference stack | Cross-task feature reuse and improved end-to-end decision coherence | Model mismatch and task interference can bias both communication and sensing outputs | [O_ISAC_086], [O_ISAC_166], [O_ISAC_134], [O_ISAC_381], [O_ISAC_161] |

### C.1 Shared Waveform
Design rationale: shared-waveform integration uses one coordinated signal structure to support communication payload transfer and sensing observability, so coupling is introduced at the earliest stage of system design rather than after front-end partitioning.

Evidence-conditioned synthesis shows 34 unique papers with combined direct+indirect support for shared waveform (15.5% of N=220), including 13 unique papers with direct-only support. This intensity places shared waveform below shared resources but above shared hardware, indicating that waveform-level co-design is a substantial, yet not universal, strategy in the current corpus. In medium terms, the high prevalence of shared front-end architectures in hybrid and cabled-fiber classes provides a structural context in which waveform reuse is operationally feasible; however, the larger separate front-end shares in VLC/LiFi and FSO indicate that waveform unification is not a necessary condition for integration. Consequently, shared-waveform designs should be interpreted as high-coupling operating points that can improve joint efficiency while tightening cross-objective constraints [O_ISAC_035], [O_ISAC_190], [O_ISAC_304], [O_ISAC_016].

Comparability and governance guard: waveform-level results are compared only when receiver/noise assumptions are explicit; therefore, no implicit OSNR-to-SNR substitution is accepted, and resolution-type and accuracy-type outcomes remain non-alias metrics under Section II rules.

### C.2 Shared Hardware
Design rationale: shared-hardware integration couples sensing and communication through common transceiver or front-end components, aiming to reduce duplication while preserving deterministic synchronization across both functions.

Evidence intensity for shared hardware is 15 unique papers under combined direct+indirect support (6.8% of N=220), with 5 unique papers under direct-only support. In contrast to shared waveform and shared resources, this is the lowest concept-level support among the four mechanism classes. Therefore, explicit hardware-sharing claims appear as a selective strategy rather than a dominant one, even though the axis-level shared front-end label is common in the corpus. This gap is expected: axis assignment captures integration structure at paper level, whereas concept anchors isolate explicit mechanism articulation. Consequently, shared-hardware interpretation should emphasize implementation pragmatics, including impairment co-propagation and calibration discipline, rather than assume broad generality across all shared front-end records [O_ISAC_021], [O_ISAC_164], [O_ISAC_324], [O_ISAC_056], [O_ISAC_161].

Comparability and governance guard: hardware-sharing claims are admissible for cross-study synthesis only when measurement plane and metric role are explicitly separated; in particular, optical-plane quantities are not merged with electrical-plane SNR statements without a stated conversion model, and accuracy is not inferred from reported resolution alone.

### C.3 Shared Resources
Design rationale: shared-resources integration coordinates time, frequency, and power allocation between sensing and communication without requiring full waveform or hardware unification, which makes it a practical mechanism under heterogeneous deployment constraints.

Shared resources has the highest concept-level evidence intensity, with 43 unique papers under combined direct+indirect support (19.5% of N=220) and 16 unique papers under direct-only support. This high support is consistent with the non-negligible separate front-end fractions in VLC/LiFi (7/25) and FSO (5/19), where resource coupling often provides integration without complete physical co-design. However, the same mechanism is also present in shared front-end-dominant classes, indicating that resource coupling is complementary rather than mutually exclusive with tighter integration modes. Therefore, resource sharing should be interpreted as a control-plane mechanism that spans both co-designed and coexistence architectures, with performance governed by contention patterns and scheduling policy quality [O_ISAC_061], [O_ISAC_114], [O_ISAC_142], [O_ISAC_141], [O_ISAC_021].

Comparability and governance guard: resource-level tradeoff claims are retained only when sensing and communication metrics are role-consistent; consequently, statements that blur resolution with accuracy or mix optical-plane and electrical-plane indicators without model disclosure are treated as constrained evidence, not pooled facts.

### C.4 Shared Processing
Design rationale: shared-processing integration couples communication decoding and sensing inference at the algorithmic level to exploit cross-task information and improve decision consistency at system output.

Evidence intensity for shared processing reaches 30 unique papers under combined direct+indirect support (13.6% of N=220), with 8 unique papers under direct-only support. In contrast to shared resources, this mechanism is less frequently explicit, but it remains materially represented across the corpus and is especially relevant in hybrid-dominant settings where multi-stage pipelines benefit from joint inference. Therefore, shared processing should be interpreted as an algorithmic integration layer that can absorb heterogeneity across links, provided that model assumptions remain transparent and task interference is controlled. Consequently, gains attributed to shared-processing pipelines should be evaluated alongside robustness to mismatch and not solely by best-case communication or sensing endpoints [O_ISAC_086], [O_ISAC_166], [O_ISAC_134], [O_ISAC_381], [O_ISAC_161].

Comparability and governance guard: processing-level synthesis remains valid only under explicit plane labeling and metric separation, so no implicit OSNR-to-SNR substitution is permitted and no resolution/accuracy aliasing is accepted in aggregated conclusions.

**Lesson (C):** Integration mechanisms should be interpreted as evidence-weighted coupling layers over the shared front-end/separate front-end axis, where stronger coordination improves joint efficiency only when governance constraints preserve metric and measurement-plane comparability.

---

## D. Signal Dimension and Detection
This subsection instantiates Axis 3 and formalizes how detection model and signal observability constrain valid cross-study comparison. In the N=220 corpus, detection labels are concentrated in direct 118/220 and coherent 97/220, with five residual records distributed across unknown (2), other (1), envelope detection (1), and MIMO (1). Therefore, most synthesis statements can be anchored in direct/coherent regimes, but residual classes must remain explicit rather than silently absorbed. Structured receiver typing further supports auditability: the structured receiver-detection annotation is populated in 218/220 records, which enables deterministic detection mapping for nearly the full corpus. This high structured-field coverage is operationally important because mapping rules prioritize structured descriptors and invoke textual fallback only when structured fields are missing; consequently, only a small minority of records requires fallback handling for Axis 3 assignment. However, frequency of occurrence is not interpreted as modality superiority; it only indicates evidence concentration under the current extraction contract.

### D.1 IM/DD vs Coherent Detection
Design rationale: IM/DD and coherent detection are not interchangeable implementation choices because they operate on different observables and induce different estimator and impairment sensitivities. IM/DD pipelines are anchored in intensity-domain observations with non-negativity constraints, whereas coherent pipelines retain field amplitude/phase information and typically require tighter optical front-end control.

Evidence-conditioned synthesis supports this distinction at two levels. At taxonomy level, direct and coherent detections account for 215/220 records (97.7%), which establishes these regimes as the primary basis for Section IV-D interpretation. Medium-conditioned counts sharpen this view: cabled fiber is coherent-leading (27 coherent, 18 direct), VLC/LiFi is strongly direct-heavy (24 direct, 1 coherent), FSO is mixed with direct lead (11 direct, 8 coherent), and hybrid remains near-balanced (59 coherent, 53 direct, plus four residual labels). At concept-evidence level, the curated Section IV-D evidence table reports 29 unique papers with combined direct+indirect support for IM/DD (23 direct-only) and 46 unique papers with combined direct+indirect support for coherent detection (26 direct-only). In contrast to paper-by-paper descriptions, these counts indicate that both regimes are materially represented but differently articulated in textual evidence. Consequently, comparisons across these regimes must be framed as model-conditioned contrasts, not as one-dimensional performance rankings [O_ISAC_001], [O_ISAC_023], [O_ISAC_028], [O_ISAC_029], [O_ISAC_190].

Comparability guard: direct/IM-DD and coherent outcomes are comparable only after explicit receiver/noise-model alignment; therefore, no implicit OSNR-to-SNR substitution is admissible when transferring conclusions across detection regimes.

### D.2 Intensity-Only vs Complex-Field Observability
Design rationale: observability class determines which information is directly measurable and, consequently, which estimation structures are physically admissible. Intensity-only observability supports robust low-complexity chains in many settings, whereas complex-field observability can expose phase-dependent structure at the cost of stricter calibration and front-end requirements.

Evidence-conditioned synthesis reveals strong asymmetry in explicit observability reporting. The intensity-only regime has combined direct+indirect support in 118 unique papers (58 direct-only), while the complex-field regime has combined direct+indirect support in 17 unique papers (4 direct-only). In contrast, this asymmetry should be interpreted as reporting concentration under current corpus composition, not as evidence that one observability class is intrinsically superior. The practical implication is that identical task labels such as ranging or localization can encode materially different uncertainty behavior depending on whether phase information is directly observable. Therefore, observability conditioning is mandatory before cross-medium or cross-algorithm aggregation, and cross-task synthesis must preserve the detection-observability pair as a coupled label rather than treating observability as an optional annotation [O_ISAC_021], [O_ISAC_082], [O_ISAC_039], [O_ISAC_056].

Comparability guard: task-level metrics are aggregated only within compatible observability classes; consequently, intensity-only and complex-field records are not merged into a single estimator-performance trend without explicit model harmonization.

### D.3 Metric Reporting Implications
Design rationale: once detection and observability are fixed, metric comparability depends on measurement-plane governance and metric-role separation. Section II remains binding through
\[
\pi(m)\in\{\text{OPTICAL\_PLANE},\;\text{ELECTRICAL\_PLANE},\;\text{AMBIGUOUS}\},
\]
and
\[
\Delta r_{\min}\neq \sigma_r.
\]
The first constraint enforces explicit plane typing and forbids implicit OSNR-to-SNR substitution without an explicit receiver/noise model. The second constraint prevents resolution and accuracy from being treated as aliases during pooled synthesis.

Receiver-side structured typing mitigates, but does not eliminate, governance risk: although structured receiver-detection coverage reaches 218/220, plane ambiguity can still arise when reported SNR-family metrics are not explicitly tagged as optical-plane or electrical-plane quantities in the narrative or tables.

Evidence-conditioned auditing confirms that this governance is necessary rather than optional. The contract-violation audit reports 84 flagged records in total, split into 75 metric-aliasing cases and 9 measurement-plane ambiguity cases. However, these records are retained for transparency and interpreted conservatively, because removing them would artificially increase apparent agreement at the cost of traceability. Consequently, Section IV-D conclusions prioritize defensible comparability over maximal aggregation: claims are pooled only when plane labels are explicit and metric roles are non-aliased [O_ISAC_132], [O_ISAC_061], [O_ISAC_013], [O_ISAC_050], [O_ISAC_056].

Comparability guard: any cross-study statement that mixes optical-plane and electrical-plane metrics without explicit conversion, or that interchanges \(\Delta r_{\min}\) and \(\sigma_r\), is treated as non-comparable evidence under the taxonomy contract.

**Lesson (D):** Detection and observability labels are only the first step; valid O-ISAC synthesis requires joint enforcement of receiver-model transparency, measurement-plane separation, and non-alias metric reporting.

---

## E. Taxonomy Summary Views
### E.1 Taxonomy Figure
Section IV-E consolidates taxonomy evidence into figure and matrix views that are auditable against the mapping contract. The primary figure is a three-stage taxonomy visual from Medium to Integration to Detection, and internal consistency is verified because the full branch sum in the taxonomy tree equals N=220. Fig. IV-1 summarizes the corpus-level O-ISAC taxonomy by mapping medium classes to integration mechanisms and detection profiles. The figure should explicitly annotate the dominant branches: hybrid/shared front-end/coherent = 59, hybrid/shared front-end/direct = 44, cabled fiber/shared front-end/coherent = 27, VLC/LiFi/shared front-end/direct = 17, VLC/LiFi/separate front-ends/direct = 7, FSO/shared front-end/coherent = 7, and FSO/shared front-end/direct = 7.

These branch values are interpreted jointly with corpus distributions, not in isolation. Medium composition is hybrid 116/220 (52.7%), cabled fiber 45/220 (20.5%), VLC/LiFi 25/220 (11.4%), FSO 19/220 (8.6%), and terahertz 1/220 (0.5%), with the remaining 14/220 records in minor classes. Integration composition is shared front-end 194/220 (88.2%) and separate front-ends 26/220 (11.8%). Detection composition is direct 118/220 (53.6%), coherent 97/220 (44.1%), and five residual labels. Primary-task tokenization further shows ranging 162/220 (73.6%), 2D localization 31/220 (14.1%), vibration 9/220 (4.1%), and localization 7/220 (3.2%), with the remaining tasks distributed across low-support classes. However, these shares indicate evidence concentration only; they do not establish modality superiority.

Minor media classes may be grouped as "other" in the visual for readability, but they must be footnoted with explicit membership and counts to preserve reproducibility. Therefore, grouped labels should disclose generic wireless (6), retroreflective wireless (2), other (2), and single-record labels such as RF-assisted wireless, UV wireless, retroreflective, and retroreflective optical. Consequently, visual compression remains traceable to the underlying taxonomy without erasing low-support clusters.

Section II governance remains binding at figure level. In contrast to purely structural tree views, Fig. IV-1 interpretation is valid only under plane-aware metric semantics: no implicit OSNR-to-SNR substitution is allowed without explicit receiver/noise modeling, and no resolution-versus-accuracy aliasing is admitted when comparing branches [O_ISAC_021], [O_ISAC_039], [O_ISAC_077], [O_ISAC_132], [O_ISAC_061].

### E.2 Taxonomy Table
The matrix companion to Fig. IV-1 must encode clustered patterns rather than one-row-per-paper listings, so Sections IV-VI can reference stable taxonomy clusters with explicit comparability guards. Table IV-E summarizes the cluster-level synthesis contract by linking deployment context, integration mechanism, detection/observability class, and metric roles within a single textual anchor.

| Taxonomy Cluster | Dominant Deployment Scenario | Integration Mechanism | Detection/Observability Class | Representative Sensing Tasks | Primary Communication Metrics | Primary Sensing Metrics | Representative References |
|:--|:--|:--|:--|:--|:--|:--|:--|
| Fiber-guided O-ISAC cluster | Long-reach cabled links with distributed monitoring overlays | Shared front-end dominant | Coherent-leading with direct subset | Ranging primary, vibration concentration, fault-localization tail | BER, FEC margin, communication robustness | Spatial granularity/ranging and vibration indicators | [O_ISAC_006], [O_ISAC_041], [O_ISAC_013] |
| FSO wireless optical cluster | Line-of-sight outdoor and inter-building optical links | Shared front-end with non-negligible separate front-ends | Direct/coherent mixed | Ranging dominant with small localization tail | BER, outage, spectral efficiency | Range estimation and resolution-class indicators | [O_ISAC_021], [O_ISAC_023], [O_ISAC_199] |
| VLC/LiFi indoor cluster | Illumination-constrained indoor access and positioning | Shared front-end dominant | Direct-detection and intensity-only dominant | Ranging plus strong localization concentration | Throughput, BER, link reliability | Localization error and ranging metrics | [O_ISAC_068], [O_ISAC_039], [O_ISAC_009] |
| Hybrid bridge cluster | Fiber-wireless and photonic-THz bridging pipelines | Shared front-end dominant | Near-balanced coherent/direct with residual labels | Ranging dominant with multi-task tail | Throughput and BER under cross-link coupling | Range/localization and task-specific errors | [O_ISAC_077], [O_ISAC_010], [O_ISAC_190] |
| Residual low-support cluster | Specialized or emerging deployment cases | Mixed mechanisms | Mostly direct with sparse alternatives | Heterogeneous low-support tasks | Context-dependent | Context-dependent | [O_ISAC_070], [O_ISAC_056] |

An explicit ambiguity note is required for cluster interpretation. The contract audit reports 84 ambiguity flags, split into 75 metric-aliasing cases and 9 measurement-plane ambiguity cases. Therefore, ambiguity-prone clusters are retained but interpreted conservatively, and cross-cluster claims are qualified when aliasing or plane ambiguity remains unresolved.

Fig. IV-2 shows the medium-task heatmap derived from primary-task tokenization and complements the matrix by revealing concentration effects that branch counts alone cannot show. Ranging remains globally dominant at 162/220 (73.6%). However, VLC/LiFi exhibits localization concentration (13/25 across 2D localization and localization primary tokens), fiber shows vibration concentration (8/45), and hybrid preserves a meaningful multi-task tail beyond ranging (21/116 non-ranging primary tokens). Consequently, Fig. IV-2 provides specialization structure for interpretation of Fig. IV-1 and Table IV-E without violating the no-superiority rule for raw prevalence [O_ISAC_006], [O_ISAC_068], [O_ISAC_077], [O_ISAC_039].

**Lesson (E):** Figure-table dual representation is necessary to keep taxonomy synthesis transparent, auditable, and governance-consistent when translating corpus structure into downstream trade-off analysis.


## drafts/section_05_template.md

# V. COMMUNICATION-SENSING TRADEOFF SYNTHESIS

## A. Communication Metrics

Unless explicitly stated otherwise, this subsection reports scenario-level governed records rather than corpus-level study counts. Communication metrics are scoped to reported communication rate (R) and link-quality indicators, with strict separation between optical-plane OSNR and electrical-plane SNR/ESNR. This separation is not stylistic; it is required because OSNR and SNR are measured at different receiver-chain stages and are not numerically comparable without an explicit conversion model. The text corpus also supports treating communication outcomes as a primary trade-off axis: across 2,352 extracted snippets (221 papers), communication-centric objectives appear with DIRECT evidence in 167 snippets (124 papers), and explicit trade-off wording appears with DIRECT evidence in 157 snippets (92 papers). Therefore, Table V summarizes plane-aware communication coverage, and Fig. 4 visualizes medium-conditioned communication behavior without collapsing planes.

### Table V: Governed Communication-Metric Coverage and Plane-Aware Availability

| Communication metric | Raw scenario coverage | Governed usable coverage | Governed range / median | Interpretation note |
|:--|:--|:--|:--|:--|
| Rate ($R$) | 198/226 records; 195/221 papers | 34 rate-bearing records within 54 governed scenarios | 25 Mbps to 448 Gbps; median 10 Gbps | Supports comparative communication synthesis only with explicit support-size caveats |
| Electrical-plane SNR | 191/226 records; 187/221 papers | 21/54 governed records | 7-22 dB; median 10 dB | The only governed quality indicator that survives filtering across more than one medium slice |
| Optical-plane OSNR | 169/226 records; 166/221 papers | 0/54 governed records | -- | All OSNR-bearing records are blocked by plane-mixing in this release |

Before governance filtering, communication reporting appears broad. The trade-off point set contains 226 scenario records from 221 papers, with rate reported in 198/226 records (87.6%), electrical-plane SNR in 191/226 (84.5%), and optical-plane OSNR in 169/226 (74.8%). At paper level, at least one rate value appears in 195/221 papers, at least one SNR value in 187/221 papers, and at least one OSNR value in 166/221 papers. However, raw prevalence should not be confused with synthesis readiness. All 169 OSNR-bearing records co-report SNR and are flagged as plane-mixed, which means that unfiltered counts overstate the amount of quality evidence that can support defensible cross-study comparison.

Applying the Section II governance contract reduces this pool substantially. Of 226 scenario records, 172 (76.1%) are blocked and 54 (23.9%) remain usable. The dominant blocker is metric-plane mixing (169 records), followed by dz-to-drmin aliasing flags (19 records); 16 records exhibit both issues. In addition, IM/DD-OSNR inconsistency is present in 98 records, while no SNR-ambiguity flags are observed in this release. At paper level, 169 papers have all scenarios blocked, leaving 52 papers with at least one governed usable scenario. Consequently, Section V-A evidence is intentionally selective: it prioritizes measurement consistency over nominal coverage.

Medium-conditioned rate behavior is interpretable only on the 54 governed records and must be read with explicit sample-size caveats. The usable distribution is hybrid (27), cabled_fibre (16), wireless_fso (5), wireless (2), wireless_vlc (1), wireless_rf (1), terahertz (1), and other (1). Rate-bearing usable records are concentrated in hybrid (17) and cabled_fibre (13). Hybrid rates span 0.025-128 Gbps (median 10 Gbps), while cabled_fibre spans 0.04-448 Gbps (median 25 Gbps). In contrast, singleton media should be interpreted as anchors rather than distributions: wireless_fso (120 Gbps), wireless_vlc (0.125 Gbps), wireless_rf (1 Gbps), and terahertz (1 Gbps). Therefore, Table V and Fig. 4 report these slices with sample-size values and avoid modality-wide ranking claims from sparse supports.

Quality-indicator synthesis becomes more constrained after filtering. In the governed subset, electrical-plane SNR remains in 21 records, whereas optical-plane OSNR remains in 0 records. SNR-bearing governed records are primarily hybrid (10) and cabled_fibre (9), with smaller contributions from wireless_fso (1) and terahertz (1). Reported SNR ranges are 7-20 dB for hybrid (median 10 dB) and 10-22 dB for cabled_fibre (median 10 dB), with single-point values of 13.75 dB (wireless_fso) and 10 dB (terahertz). Because no governance-usable OSNR records survive, this subsection can describe electrical-plane quality patterns but cannot make quantitative optical-plane quality comparisons across media. Table V reports this absence explicitly as an evidence gap rather than hiding it in aggregate summaries.

A communication-resolution coupling view is admissible only inside CRQ-eligible records. The eligible set contains 20 records (all with non-null CRQ values), dominated by hybrid (14), followed by cabled_fibre (4), plus one terahertz and one wireless_fso point. This restriction is consistent with the aliasing guardrail: dz is not a surrogate for drmin, and no governed record in this subsection relies on dz substitution. Therefore, CRQ references in V-A are contextual and eligibility-bounded, while full frontier interpretation is deferred to the dedicated trade-off subsection.

Limitations remain material and are stated directly. The contract-violation audit reports 299 MAJOR violations across 169 papers: 261 metric-plane violations and 38 metric-aliasing violations. This imbalance explains why communication evidence appears abundant before filtering but sparse after governance enforcement. Therefore, the V-A conclusions are robust to plane/alias confounding by construction, yet sensitive to current reporting practice in the literature. A practical implication for future corpus growth is straightforward: plane-explicit quality reporting is required to recover optical-plane comparability in cross-medium synthesis.

Lesson (V-A): communication evidence in O-ISAC is numerically rich, but only plane-consistent and alias-free subsets support defensible comparative synthesis.

## B. Sensing Metrics

Unless explicitly stated otherwise, this subsection reports scenario-level governed records rather than corpus-level study counts. Sensing metrics are organized by functional role, not by lexical similarity: drmin represents physical resolution, sigma_r represents estimator-level accuracy, CRB provides bound-level context, and dz denotes fiber spatial granularity. These roles are not interchangeable, and quantitative comparison is admitted only when role consistency is preserved. Therefore, Table VI summarizes role-separated sensing evidence, while Fig. 4 retains only governed comparisons rather than raw pooled counts. This framing also aligns with the qualitative record, where trade-off wording is present but unevenly explicit across studies.

### Table VI: Governed Sensing-Metric Coverage by Functional Role

| Sensing role | Raw scenario coverage | Governed usable coverage | Governed range / median | Interpretation note |
|:--|:--|:--|:--|:--|
| Resolution ($dr_{min}$-eligible) | 173/226 eligible records; 170/221 papers | 20/173 eligible records | 0.0025 m to 15 m; median 0.0397 m | Physical resolution is retained only on the role-consistent governed subset |
| Accuracy ($\sigma_r$) | 186/226 records; 183/221 papers | 16/186 records | 0.001 m to 1000 m; median 0.0575 m | Estimator-level accuracy remains distinct from resolution and is not pooled with $dr_{min}$ |
| CRB | 148/226 records; 145/221 papers | 0/148 records | -- | Bound-level reporting remains contextual only after governance filtering |
| Fiber spatial granularity ($dz$) | 161/226 records; 158/221 papers | 0/161 records | -- | $dz$ is retained as fiber-specific context and is never substituted for $dr_{min}$ |

Before governance filtering, sensing coverage appears broad at both scenario and paper levels. Across 226 scenario points, drmin is reported in 195 records (86.3%), with 173 records (76.5%) marked drmin-eligible; sigma_r appears in 186 records (82.3%); CRB appears in 148 records (65.5%); and dz appears in 161 records (71.2%). Paper-level coverage remains similarly high: 192/221 papers report drmin, 170/221 include at least one drmin-eligible scenario, 183/221 report sigma_r, 145/221 report CRB, and 158/221 report dz, although only 27/221 contain dz-eligible contexts under the contract. Consequently, extraction-level richness is substantial, but direct comparability is still contingent on governance compliance.

After governance filtering, the synthesis-ready subset contracts sharply. Only 54/226 scenarios (23.9%) remain usable overall, while 172/226 (76.1%) are blocked. At role level, only 20/173 drmin-eligible records survive (11.6%), and only 16/186 sigma_r records survive (8.6%). In contrast, both CRB and dz drop to zero usable records in the retained subset (0/148 and 0/161, respectively). The exclusion pattern is highly structured rather than random: among blocked drmin-eligible records, 151/153 are plane-mixed; among blocked sigma_r records, 169/170 are plane-mixed; among blocked CRB records, 147/148 are plane-mixed. Therefore, Table VI distinguishes reported coverage from governance-usable coverage, because raw prevalence alone overstates comparative readiness.

Medium-conditioned resolution behavior can be interpreted only within the 54 governed records and must be read with explicit sample-size caveats. drmin-eligible usable records are concentrated in hybrid (14) and cabled_fibre (4), with single records in wireless_fso (1) and terahertz (1). Across all usable drmin-eligible points, drmin spans 0.0025-15 m, with a median of 0.0397 m. However, within-medium profiles differ materially: hybrid spans 0.0025-10 m (median 0.0191 m), whereas cabled_fibre spans 0.01-15 m (median 5.5 m). In contrast, wireless_fso and terahertz each contribute one value (0.0025 m and 0.1 m), so they should be interpreted as anchors rather than distributions. Consequently, cross-medium ranking should be avoided unless the claim is explicitly conditioned on support size and task context.

Estimator-level accuracy shows a distinct governed profile and should not be conflated with resolution. Only 16 usable records report sigma_r: hybrid (8), cabled_fibre (7), and terahertz (1). Overall, sigma_r spans 0.001-1000 m with a median of 0.0575 m, but this range is strongly medium- and scenario-conditioned. Hybrid values cluster between 0.001 and 0.1 m (median 0.01 m), whereas cabled_fibre spans 0.001-1000 m (median 1 m), indicating heterogeneous operating assumptions and estimator regimes. Moreover, only 13 usable records contain both drmin-eligible and sigma_r values. Therefore, direct resolution-versus-accuracy interpretation is feasible only in a minority slice, and Fig. 4 should keep these layers separated rather than collapsing them into one sensing axis.

CRB and dz should be treated as constrained context in this subsection. Although CRB is reported in 148 raw records, none remains governance-usable after filtering, so CRB cannot replace measured sigma_r in quantitative comparison. Likewise, dz appears in 161 raw records but has zero usable entries in the retained subset and remains explicitly non-substitutable for drmin. This is consistent with the aliasing guardrail: 19 records are flagged for dz-to-drmin aliasing, and any ranging-style inference from dz would violate the contract. In contrast, CRQ-linked comments remain admissible only within CRQ-eligible records (20 records, all within the usable subset).

Measurement-plane discipline further constrains sensing-quality interpretation. In the usable subset, OSNR remains absent (0 records for both drmin-eligible and sigma_r subsets), while electrical-plane SNR remains available in 12/20 drmin-eligible records and 14/16 sigma_r records. Therefore, V-B can support limited electrical-plane-conditioned sensing remarks, but cannot support optical-plane-conditioned sensing comparisons across media. This absence is itself informative for Table VI: governed sensing evidence currently depends on post-detection quality reporting rather than optical-plane quality reporting.

The qualitative evidence is consistent with this quantitative contraction. Trade-off mention extraction reports 188 mentions (26 DIRECT, 60 INDIRECT, 102 NONE). DIRECT mentions concentrate in capacity-resolution quotient (11) and resource-allocation trade-off (7), while DIRECT rate-resolution trade-off mentions are sparse (2) and DIRECT Fisher-information-constraint mentions remain limited (4). Therefore, explicit sensing-role articulation exists, but strong synthesis-ready articulation is still a minority pattern relative to total mention volume.

Limitations are material and remain explicit. The governance audit records 299 MAJOR violations across 169 papers, including 261 metric-plane violations and 38 metric-aliasing violations. This profile explains why reported sensing coverage is high before filtering but sharply reduced after governance enforcement. Consequently, V-B conclusions are intentionally conservative: they preserve role-consistent and plane-consistent comparability at the expense of sample size.

Lesson (V-B): sensing evidence in O-ISAC is abundant in raw reporting, but defensible cross-medium synthesis requires strict role separation and governance filtering.

## C. Sensing-Communication Trade-off

Unless explicitly stated otherwise, this subsection reports scenario-level governed records rather than corpus-level study counts. The trade-off synthesis is role-separated by construction: rate-versus-resolution is interpreted through rate and drmin, while rate-versus-accuracy is interpreted through rate and sigma_r; CRB remains bound-level context, and dz is never treated as a surrogate for drmin. Therefore, Fig. 4 visualizes governed operating clouds with separated sensing roles, Fig. 5 presents frontier behavior only under explicit eligibility constraints, and Table VII consolidates this subsection through point partitions and coupling-mode coverage with sample-size fields.

The raw operating set includes 226 scenario points from 221 papers, but governance filtering retains only 54 points (23.9%) and blocks 172 points (76.1%). At paper level, only 52 papers contribute at least one governed usable point. This contraction is not a peripheral cleanup; it determines the admissible evidence for trade-off inference. Consequently, V-C addresses both the shape of the governed region and the magnitude of evidence loss relative to the nominal cloud. In contrast, treating the raw cloud as fully comparable would overstate the maturity of cross-study trade-off evidence.

Trade-off dimensions are present in labels, but not always in governed metric content. In the raw set, 213 points carry rate-versus-RMSE labeling and 36 carry rate-versus-range-resolution labeling; in the usable subset, these counts become 48 and 6, respectively. However, only 14 of the 48 usable rate-versus-RMSE-labeled points actually report sigma_r, and none of the 6 usable rate-versus-range-resolution-labeled points is drmin-eligible. Therefore, dimensional interpretation in V-C is grounded in governed metric availability rather than label strings alone. Consequently, labels are treated as narrative cues, while eligibility-filtered fields define the quantitative core.

Coupling-mode coverage exhibits a similar asymmetry. Across all 226 points, resource_division appears in 181 points and joint_waveform in 41 points, with 4 points carrying missing or non-standard coupling labels. In the 54 governed points, resource_division remains dominant (39), joint_waveform remains secondary (13), and 2 points remain unlabeled. Therefore, coupling comparisons are informative but incomplete, and Table VII preserves an explicit unlabeled category for auditability rather than forcing every point into a binary allocation.

The governed operating region can still be summarized numerically with clear caveats. Within the usable subset, rate is available in 34 points, spanning 25 Mbps to 448 Gbps with a median of 10 Gbps. drmin-eligible values appear in 20 points, spanning 0.0025-15 m (median 0.0397 m), while sigma_r appears in 16 points, spanning 0.001-1000 m (median 0.0575 m). Overlap remains limited: 20 points support rate-plus-drmin interpretation, 16 support rate-plus-sigma_r interpretation, and only 13 support the full triplet (rate, drmin, sigma_r). Therefore, Fig. 4 presents separate resolution-coupled and accuracy-coupled layers rather than a pooled sensing axis.

CRQ partitioning makes admissibility compression explicit. The point taxonomy is 226 total points, 170 CRQ-candidate points, 20 CRQ-valid points, and 2 Pareto points; these totals are consistent with the Section V summary table. The transition from candidate to valid points (170 to 20) is substantial, and frontier evidence is sparse by design (2 points). Within governed records, all CRQ candidates are valid (20/20), indicating that most admissibility selection occurs before frontier extraction. Consequently, CRQ claims in V-C are restricted to the 20 valid records and should not be extrapolated to the full raw cloud.

Within the CRQ-valid set, medium-conditioned heterogeneity remains visible but support is uneven. The 20 valid points are distributed across hybrid (14), cabled_fibre (4), terahertz (1), and wireless_fso (1). CRQ spans 6.67x10^8 to 4.8x10^13 bps/m, with a median of 4.33x10^10 bps/m. Hybrid has the strongest support and a median of 8.83x10^10 bps/m, while cabled_fibre has a lower median of 5.5x10^9 bps/m. However, terahertz and wireless_fso remain single-point anchors. Therefore, cross-medium interpretation should be coverage-weighted and explicitly non-ranking when support collapses to singleton slices.

Pareto interpretation requires an additional caution layer. The Pareto file contains 2 points from 2 papers: one hybrid and one wireless_fso. Both are rate-versus-RMSE points with CRQ value 4.8x10^13 bps/m, and coupling modes split one-to-one between resource_division and joint_waveform. Because this frontier is minimal, Fig. 5 should be interpreted as an illustrative boundary snapshot rather than a stable envelope of the O-ISAC design space. Consequently, V-C uses Pareto points as exemplar operating points, not as a basis for modality-wide conclusions.

Measurement-plane constraints remain active throughout this subsection. In the governed subset, 21 points retain electrical-plane SNR while 0 retain optical-plane OSNR; in the CRQ-valid subset, 12 retain SNR and 0 retain OSNR. Therefore, the trade-off synthesis can condition selected claims on electrical-plane quality but cannot establish optical-plane-conditioned frontier trends. This caveat should remain explicit in Table VII notes and figure captions to avoid implicit cross-plane equivalence.

Qualitative trade-off language supports this conservative interpretation while confirming articulation gaps. Trade-off mention extraction reports 188 mentions across 61 papers: 26 DIRECT, 60 INDIRECT, and 102 NONE. DIRECT mentions are concentrated in capacity-resolution quotient (11) and resource-allocation trade-off (7), with smaller counts for Fisher-information constraints (4), Pareto optimality (2), and rate-resolution trade-off (2). Therefore, explicit trade-off reasoning exists, but it is still a minority pattern relative to total mention volume.

Limitations remain material for V-C. The governance audit reports 299 MAJOR violations across 169 papers, including 261 metric-plane violations and 38 metric-aliasing violations. These violations account for much of the candidate-to-valid compression and the sparse Pareto set. Consequently, V-C conclusions are intentionally conservative: they prioritize role-consistent, plane-consistent, and traceable synthesis over broader but weakly governed aggregation.

Lesson (V-C): sensing-communication trade-off evidence is abundant in raw extraction, but defensible operating-region and frontier claims emerge only after strict eligibility partitioning and explicit support-size caveats.

## D. Comparative Analysis: Fiber vs Wireless

Unless explicitly stated otherwise, this subsection reports scenario-level governed records rather than corpus-level study counts. The comparison protocol has three steps. First, candidate points are filtered by the Section II governance contract (plane separation, metric-role separation, and alias controls). Second, medium labels are kept exactly as normalized in Section IV (cabled_fibre, wireless_*, hybrid, and residual classes). Third, comparative claims are restricted to sample-supported slices and reported with explicit coverage caveats. Therefore, Table VII is the primary comparative anchor, and this subsection is framed as evidence-weighted comparison rather than ranking.

### Table VII: Head-to-Head Comparison of Governed Fiber, Wireless, and Hybrid Slices

| Comparative slice | Governed points (papers) | Median rate | Median $dr_{min}$ | Median $\sigma_r$ | Median CRQ (eligible only) | Coupling composition |
|:--|:--|:--|:--|:--|:--|:--|
| Fiber (`cabled_fibre`) | 16 (14) | 25 Gbps (`n_rate=13`) | 5.5 m (`n=4`) | 0.1 m (`n=7`) | 5.50 x 10^9 bps/m (`n=4`) | `resource_division` 14; `joint_waveform` 2 |
| Wireless (`wireless_*`) | 9 (9) | 1 Gbps (`n_rate=3`) | 0.0025 m (`n=1`) | -- | 4.80 x 10^13 bps/m (`n=1`) | `resource_division` 5; `joint_waveform` 4 |
| Hybrid bridge | 27 (27) | 10 Gbps (`n_rate=17`) | 0.019075 m (`n=14`) | 0.01 m (`n=8`) | 8.83 x 10^10 bps/m (`n=14`) | `resource_division` 19; `joint_waveform` 6; unlabeled 2 |

The contraction from raw to governed evidence is substantial and directly shapes what can be compared. The raw trade-off set contains 226 scenario points across 12 medium labels, dominated by hybrid (117) and cabled_fibre (48), followed by wireless_vlc (27), wireless_fso (19), wireless (6), and a long tail of low-support classes. Governance filtering blocks 172 points (76.1%) and retains 54 points (23.9%). The governed medium mix then becomes hybrid (27), cabled_fibre (16), wireless_fso (5), wireless (2), wireless_rf (1), wireless_vlc (1), terahertz (1), and other (1). Consequently, V-D should be interpreted as a constrained synthesis over a reduced admissible set, not as a direct mirror of raw-corpus prevalence.

For the explicit fiber-versus-wireless contrast, cabled_fibre is used as the fiber slice and wireless_* labels are pooled as the wireless slice, while hybrid is treated as a bridge class rather than assigned to either endpoint. In the governed set, fiber contributes 16 points from 14 papers, wireless contributes 9 points from 9 papers, and hybrid contributes 27 points from 27 papers. Metric completeness is asymmetric: fiber contributes 13 rate values, 7 drmin values, and 7 sigma_r values; wireless contributes 3 rate values, 1 drmin value, and 0 sigma_r values; hybrid contributes 17 rate values, 14 drmin values, and 8 sigma_r values. Therefore, hybrid remains central for transferability analysis, but endpoint comparison must still be reported without collapsing hybrid into fiber or wireless.

Rate-side medians in governed slices indicate different operating emphases but do not support universal superiority claims. Fiber shows a median rate of 25 Gbps (n_rate=13), wireless shows 1 Gbps (n_rate=3), and hybrid shows 10 Gbps (n_rate=17). However, the wireless median is structurally unstable because it comes from a sparse, heterogeneous mix that includes one high-value wireless_fso point and lower-rate entries from other wireless labels. Therefore, Table VII reports median rate together with support counts so that apparent ordering is interpreted as support-weighted evidence.

Sensing-side comparison is more constrained by missingness. In governed slices, fiber has median drmin of 1 m (n=7) and median sigma_r of 0.1 m (n=7). Wireless has only one drmin value (0.0025 m) and no governed sigma_r value. Hybrid has median drmin of 0.019075 m (n=14) and median sigma_r of 0.01 m (n=8). Consequently, a limited rate-versus-resolution contrast can be stated between fiber and wireless, but a balanced rate-versus-accuracy contrast cannot be established for this release. In contrast, hybrid supports a dual-metric interpretation because both resolution and accuracy are represented.

CRQ-conditioned comparison should be read through the strict 20-point eligible subset summarized in the modality-slice file. In that subset, hybrid contributes 14 points (median CRQ 8.83x10^10 bps/m), cabled_fibre contributes 4 points (median CRQ 5.50x10^9 bps/m), wireless_fso contributes 1 point (4.80x10^13 bps/m), and terahertz contributes 1 point (1.00x10^10 bps/m). This normalization is useful for high-selectivity comparison, but it is intentionally sparse and does not represent the full governed cloud. Therefore, Table VII keeps governed medium slices as the primary comparative artifact and retains CRQ only as a bounded contextual column rather than as a frontier-summary substitute.

Coupling composition adds an additional interpretation layer. Fiber governed points are mostly resource-division (14/16), with a smaller joint-waveform tail (2/16). Wireless points are split more evenly between resource-division (5/9) and joint-waveform (4/9). Hybrid is also resource-division-led (19/27), with joint-waveform support (6/27) and an unlabeled remainder (2/27). Therefore, observed medium-level differences in medians should be read jointly with coupling composition, because allocation strategy and medium are entangled in the reported operating points.

Measurement-plane constraints remain active in this subsection and limit quality-conditioned comparison. In the governed slices, optical-plane OSNR has zero usable entries for fiber, wireless, and hybrid, whereas electrical-plane SNR remains available for fiber (9 points) and hybrid (10 points) but not for wireless (0 points). Consequently, V-D can support limited electrical-plane-conditioned remarks for fiber and hybrid, but cannot establish optical-plane-conditioned fiber-versus-wireless trends.

Limitations are explicit and materially relevant for comparative claims. The governance audit reports 299 MAJOR violations across 169 papers, including 261 metric-plane violations and 38 metric-aliasing violations. At paper level, 169/221 papers have all scenarios blocked, leaving 52 papers with at least one governed usable scenario and only 20 papers with CRQ-eligible evidence. Therefore, V-D conclusions are deliberately conservative: they preserve defensible comparison where support exists and mark sparse slices as non-ranking evidence.

Lesson (V-D): fiber-versus-wireless comparison in O-ISAC is defensible only under governance filtering, explicit support-size reporting, and explicit treatment of hybrid as a bridge class rather than an endpoint.

**Section V closeout synthesis.** Pareto interpretation in Section V remains bounded by three nested evidence layers: the raw trade-off cloud (226 points), the governed cloud (54 points), and the CRQ-valid subset (20 points) from which only 2 Pareto points are selected. Consequently, Fig. 5 is interpreted as a governance-conditioned frontier view rather than as a direct projection of the raw operating landscape. This compression is analytically central, not cosmetic: candidate abundance does not translate into frontier-level comparability unless plane, role, and eligibility constraints are simultaneously satisfied.

The frontier is also highly selective in composition. Within the CRQ-valid subset, hybrid contributes 14 points, cabled_fibre 4, terahertz 1, and wireless_fso 1; however, the Pareto set itself contains only one hybrid point and one wireless_fso point. Therefore, the absence of fiber and terahertz points from the frontier cannot be interpreted as inferiority. It only indicates that current nondominated evidence is sparse and unevenly distributed across media. The same caution applies to coupling mode: the valid set is resource-division-led (15 points versus 3 joint-waveform points, plus 2 unlabeled points), yet the frontier splits one-to-one between resource_division and joint_waveform. Accordingly, Section V supports conditional design interpretation, not stable medium-wide or coupling-wide ranking.

Metric-role and measurement-plane constraints remain active at this closing stage. All CRQ-valid points are drmin-eligible, but only 13/20 also report sigma_r, and only 1 of the 2 Pareto points includes sigma_r. Likewise, OSNR is absent from the governed, valid, and Pareto subsets, while electrical-plane SNR remains available in 21 governed points, 12 valid points, and 1 Pareto point. Therefore, frontier interpretation is stronger for rate-versus-resolution than for rate-versus-accuracy, and it cannot support optical-plane-conditioned frontier claims. Fig. 5 should therefore be captioned as sparse illustrative evidence of admissible extreme operating points under the current reporting contract.

These observations still yield practical guidance. Decision-stage claims should be restricted to CRQ-valid evidence rather than to the full candidate cloud; operating-point discussions should report both drmin and sigma_r whenever possible; and medium and coupling context should remain attached to every frontier-style interpretation. This bounded reading is consistent with the qualitative trade-off record, where DIRECT trade-off language remains a minority relative to INDIRECT and NONE labels. Limitations remain explicit: the governance audit reports 299 MAJOR violations across 169 papers, including 261 metric-plane violations and 38 metric-aliasing violations. Section V therefore closes on a deliberately conservative conclusion: the field already contains strong governed exemplars, but reliable design generalization still depends on expanding the CRQ-valid, medium-balanced evidence base.

Lesson (V): governed trade-off synthesis is already informative for bounded engineering interpretation, but frontier-level generalization remains limited by sparse valid support and uneven reporting discipline.


## drafts/section_06_draft.md

# VI. Enabling Technologies and System-Level Co-Design for Optical ISAC

Section VI explains how O-ISAC becomes practically realizable by linking enabling technologies to channel robustness, joint optimization, runtime overhead, and benchmarking discipline. Across the current evidence base, optical phased arrays (OPA), optical reconfigurable intelligent surfaces (ORIS), robustness-aware optimization, and network coordination recur as coupled design levers rather than isolated modules [O_ISAC_008], [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_112], [O_ISAC_127]. Accordingly, this section remains enabler-centric: the named anchors promised in Section I, namely ORIS, OPA, photonics-assisted signal generation, and machine learning integration, are retained here, but they are interpreted through system-level feasibility rather than as a component catalog. In the survey flow, this chapter bridges the measured trade-off logic of Section V to the deployment and application focus of Section VII by asking which enablers create usable design freedom under realistic channel, control, and evaluation constraints. To stay aligned with earlier sections, we preserve Section II measurement governance, reuse the Section IV medium/taxonomy framing, and keep the Section V governed-evidence caution visible when discussing maturity and prevalence. Where the study-level core remains limited, the prose below therefore emphasizes design opportunity and constraint structure rather than deployment maturity.

Throughout this section, we use **ORIS (Optical Reconfigurable Intelligent Surface)** as the canonical umbrella term for optical RIS-style programmable surfaces. We also preserve one shared notation block so that OPA steering, ORIS-assisted links, robustness constraints, and multi-user optimization can be discussed without symbol drift across subsections.

**Table VI-1 defines unified notation for Section VI.**

| Symbol | Meaning | Used in |
|---|---|---|
| $x(t)$ | Optical transmit waveform or equivalent sampled signal | VI-C, VI-E |
| $\ell$ | Link distance in benchmark scenario disclosure | VI-D |
| $\bar P$ | Average optical power budget | VI-C, VI-D |
| $P_{\max}$ | Peak optical power budget | VI-C, VI-D |
| $H$ | End-to-end channel coefficient or gain | VI-B |
| $H_l$ | Deterministic or path-loss component of $H$ | VI-B |
| $H_a$ | Atmospheric or medium-turbulence component of $H$ | VI-B |
| $H_p$ | Pointing or misalignment component of $H$ | VI-B |
| $\gamma$ | Instantaneous reliability proxy evaluated on a fixed detection plane; no cross-plane substitution is implied | VI-B, VI-E |
| $\gamma_{\text{th}}$ | Reliability threshold for outage control | VI-B |
| $\varepsilon$ | Allowed outage probability target | VI-B, VI-C |
| $m_{\text{res}}$ | Role-consistent resolution or granularity metric | VI-D |
| $m_{\text{acc}}$ | Empirical sensing accuracy metric | VI-D |
| $m_{\text{bnd}}$ | Bound-type sensing metric family | VI-D |
| $\sigma_r$ | Estimator-dependent sensing accuracy metric when reported | VI-D |
| $\Theta$ | ORIS diagonal response matrix | VI-A, VI-C, VI-E, VI-F |
| $\beta_n$ | ORIS amplitude coefficient of element $n$ | VI-A |
| $\theta_n$ | ORIS phase of element $n$ | VI-A, VI-E |
| $Q$ | Number of phase-quantization levels | VI-A, VI-E |
| $\mathbf{w}_k$ | Beamforming vector for user $k$ | VI-C, VI-E |
| $\mathrm{SINR}_k$ | User-$k$ communication quality metric | VI-E |
| $\mathrm{CRB}$ | Bound-type sensing metric; not interchangeable with empirical accuracy metrics | VI-C, VI-D, VI-E, VI-F |

> **Model VI-U (Unified Channel/Signal Model).**
>
> $$
> y_k = \left(h_{d,k} + \mathbf{h}_{r,k}^{T}\Theta\mathbf{g}\right)x + n_k,
> $$
> $$
> \Theta = \operatorname{diag}\!\left(\beta_n e^{j\theta_n}\right),
> $$
> $$
> \theta_n \in \left\{0,\frac{2\pi}{Q},\ldots,\frac{2\pi(Q-1)}{Q}\right\}.
> $$
>
> Model VI-U is a compact abstraction reused across VI-A, VI-C, VI-E, and VI-F for notation consistency [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_127].

## VI-A. Programmable Optical Enablers

Programmable optical enablers matter because they convert optical propagation from a mostly fixed channel into a controllable channel. OPA studies expose transmit-side beam agility, angular selectivity, and joint waveform support, whereas ORIS studies expose environment-side path shaping, alignment assistance, and blockage mitigation through reflected or reconstructed paths [O_ISAC_008], [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_112]. This distinction is important: OPA and ORIS should be written as complementary control authorities rather than as interchangeable technologies.

A compact steering anchor for OPA is

$$
AF(\theta)=\sum_{m=0}^{M-1} a_m\exp\!\left(j\left(kdm\sin\theta+\phi_m\right)\right),
$$
$$
\phi_m^{\star}=-kdm\sin\theta_0,
$$

which steers the main lobe toward $\theta_0$ under accurate phase control [O_ISAC_008], [O_ISAC_061], [O_ISAC_091]. In practice, finite receiver FoV, grating-lobe behavior, insertion loss, and channel impairments prevent ideal steering gains from translating directly into reproducible O-ISAC gains [O_ISAC_061], [O_ISAC_091], [O_ISAC_098].

PIC, programmable photonics, and photonics-assisted signal-generation themes belong here only as enabling substrates beneath these control surfaces, not as a detached component inventory. At the current evidence level, Section VI should therefore treat these families conservatively unless they are directly anchored to measurable O-ISAC integration benefits. In this survey, their main value is explanatory: they clarify packaging, integration pathway, and hardware-stack feasibility behind OPA/ORIS-style controllability, but they do not yet carry the same headline evidence weight as the primary programmable-surface and beam-steering narratives. Likewise, prevalence language must remain cautious: structured metric traces for OPA/ORIS are broader than strong study-level evidence of deliberate co-design adoption, so OPA/ORIS discussion in this survey should be read as a high-signal but still limited adoption core rather than as evidence of uniform platform maturity.

**Table VI-A.1 compares programmable optical enabler families by control role, evidence posture, and deployment constraints.**

| Enabler family | Primary control role in O-ISAC | Strongest evidence posture in this survey | Main deployment constraints | Role in Section VI argument |
|---|---|---|---|---|
| OPA | Transmit-side beam agility, angular selectivity, joint communication-sensing steering | Primary evidence core; Section I contribution count is 7 study-level papers, while broader structured traces are treated only as support context | Grating lobes, finite receiver FoV, insertion loss, atmospheric/channel loss sensitivity | Carries the strongest beam-control narrative in VI-A |
| ORIS/OIRS | Environment-side path shaping, blockage mitigation, alignment assistance, NLoS reconstruction | Primary evidence core; Section I contribution count is 8 study-level papers, while broader structured traces are treated only as support context | Refresh latency, attenuation, phase quantization, coherence-time mismatch, control overhead | Carries the strongest propagation-control narrative in VI-A |
| PIC / programmable photonics | Integration substrate for packaging, routing, and scalable optical control | Qualitative/supporting only; used to explain how controllable optics may be integrated, not to claim mature O-ISAC adoption | Calibration burden, packaging complexity, insertion loss, hardware-stack dependence | Supplies integration context beneath OPA/ORIS rather than a separate headline storyline |
| Photonics-assisted signal generation / photonic-THz bridge | Source and distribution pathway for hybrid optical-wireless control chains | Bridge evidence only; relevant for hybrid system interpretation but not a standalone maturity claim in VI-A | Stage-aware modeling, cross-plane reporting, front-end chain complexity | Connects enabler discussion to hybrid and transfer-oriented system views |

Evidence note: OPA/ORIS prevalence wording follows the strict study-level contribution view used in Section I; broader structured traces from the Section 6F dual-view audit remain contextual and are not interpreted here as direct adoption prevalence. In whole-manuscript terms, Table VI-A.1 is the compact enabler-capability artifact that later application and challenge sections can inherit without re-inflating prevalence claims.

These medium-conditioned asymmetries are better read as an enabler landscape than as a flat prevalence ranking, and Fig. VI-1 is intended to summarize that view once the final asset is produced.

<!--
Fig. VI-1 specification
Purpose: visualize the Section VI enabler landscape without inflating adoption claims from raw structured traces.
Placement: after Table VI-A.1 and before the VI-A takeaway.
Primary inputs:
- analysis/VI_evidence_v2/section6E_medium_slices.csv
- analysis/VI_evidence_v2/section6F_dual_view_comparison.csv
- Section I contribution counts already fixed in drafts/section_01_introduction.md
Visual form:
- matrix / heatmap
- rows: Section IV-aligned medium classes (Hybrid systems, cabled fiber, VLC/LiFi, FSO, photonic-THz / terahertz proxy, residual low-support media)
- columns: OPA, ORIS, PIC, ML/AI, photonic_generation, programmable_photonics
- shading: evidence concentration by governed/supportive tier, not by raw count alone
Caption logic:
- emphasize medium-conditioned concentration rather than superiority
- state explicitly that OPA and ORIS headline prevalence follows the strict study-level view, while broader structured traces remain contextual
- note that PIC / photonic-generation / programmable-photonics layers are interpretive/supporting, not co-equal maturity claims
Design note:
- annotate OPA and ORIS with strict study-level counts from Section I
- avoid printing raw 121/124-style counts as the primary visual message
-->

**VI-A takeaway.** OPA evidence is strongest on beam agility and communication-sensing coupling, while ORIS evidence is strongest on alignment robustness and NLoS support. Across modalities, quantized control, insertion loss, and refresh latency remain practical bottlenecks. For the survey narrative, OPA/ORIS therefore carry the primary evidence load in VI-A, while PIC and photonic-integration themes remain supporting context on how those capabilities might be packaged and scaled. The most defensible near-term message is not that programmable optics are uniformly mature, but that they expose a promising yet unevenly validated optical control space whose practical value is still scenario- and impairment-dependent. That conclusion naturally shifts the discussion to VI-B: controllability matters only if it remains useful under the impairment profile of the actual optical channel.

## VI-B. Channel Impairments and Robustness

Robustness is a first-order concern in O-ISAC because the same optical channel impairments degrade communication reliability and sensing fidelity together. Across FSO, VLC/LiFi, and hybrid optical settings, the literature repeatedly models end-to-end gain as a composition of deterministic loss, atmospheric or medium turbulence, and pointing or alignment components [O_ISAC_023], [O_ISAC_035], [O_ISAC_061], [O_ISAC_098], [O_ISAC_199]. Guided-fiber cases remain important, but they require different impairment abstractions and should not be silently collapsed into the same wireless robustness template. This is the point where enabler value becomes conditional: a programmable surface or beam-steering mechanism is only useful insofar as it remains effective under the dominant impairment regime.

A compact robustness anchor is

$$
H=H_l H_a H_p,
$$
$$
P_{\text{out}}=\Pr\!\left(\gamma(H)<\gamma_{\text{th}}\right)\le \varepsilon.
$$

This chance-constrained view links physical impairment statistics directly to reliability targets and is consistent with quantile-robust formulations already used in optical ISAC optimization studies [O_ISAC_023], [O_ISAC_061], [O_ISAC_091]. Here $\gamma$ must stay tied to one declared detection plane per scenario; the expression does not permit implicit OSNR-to-electrical-SNR conversion or blind pooling of coherent and direct observations. Practical mitigation then combines design-time robustness with runtime adaptation through tracking, refresh control, environment-aware reconfiguration, and fallback or diversity mechanisms [O_ISAC_098], [O_ISAC_112], [O_ISAC_127], [O_ISAC_199].

The prose here should stay medium-aware. Turbulence and weather attenuation dominate many FSO and hybrid scenarios, finite FoV and geometry dominate many VLC scenarios, and control latency cuts across most programmable optical platforms. Section VI therefore cannot write "robustness" as if one impairment model covers all optical modalities equally well.

**VI-B takeaway.** Current literature supports robustness-aware optical design, but cross-paper outage definitions and confidence reporting remain heterogeneous. The survey-level lesson is that controllability becomes meaningful only after impairment-aware conditioning, not before it. The main open issue is therefore no longer whether robustness matters, but how to compare robustness claims under common impairment and reporting contracts. Once that conditioning is made explicit, the next question becomes how communication, sensing, and robustness constraints should be optimized jointly, which motivates VI-C.

## VI-C. Joint Co-Design and Resource Optimization

Joint co-design is required because waveform, beam, power, and ORIS controls share physical constraints. In IM/DD implementations, feasible signaling must satisfy nonnegativity and optical power bounds, while coherent or programmable settings add quantization, steering, and update constraints [O_ISAC_009], [O_ISAC_023], [O_ISAC_054], [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. Model VI-U is useful here because it keeps transmitter, ORIS, and sensing terms in one variable structure.

A minimal feasible-set and objective anchor is

$$
\mathcal U=\{x(t):x(t)\ge 0,\;\mathbb{E}[x(t)]\le \bar P,\;\max_t x(t)\le P_{\max}\},
$$
$$
\max_{\mathbf{w},\Theta,\,x\in\mathcal U}\;\alpha R(\mathbf{w},\Theta)-(1-\alpha)\,\mathrm{CRB}(\mathbf{w},\Theta),\quad \alpha\in[0,1].
$$

The weight $\alpha$ sets the communication-sensing operating point and can be extended with reliability and latency constraints when channel dynamics are explicit [O_ISAC_023], [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. Within this subsection, $\mathrm{CRB}$ is retained as a bound-type sensing term; it should not be read as interchangeable with empirical accuracy metrics such as $\sigma_r$ or with bandwidth-limited resolution terms. However, this subsection must preserve two maturity caveats. First, Section VI contains more structured OPA/ORIS metric traces than strong study-level evidence of deliberate full-stack co-design adoption. Second, many reported formulations remain exemplar-driven studies under controlled assumptions rather than reproducibly benchmarked integrated stacks. It is therefore safer to say that the literature exposes a structured control space for co-design than to say that metric-bearing OPA/ORIS papers already establish mature multi-objective O-ISAC practice.

**VI-C takeaway.** Evidence is strongest for structured optimization in a limited set of well-specified OPA, DCO-OFDM, and dynamic underwater exemplars. The main gap is not the absence of optimization methods, but the absence of harmonized disclosure of constraints, runtime burden, operating assumptions, and replication quality across papers. In survey terms, VI-C shows that the co-design space is already nontrivial, yet still weakly comparable across studies. That comparability problem is exactly why VI-D becomes the hinge subsection of the chapter.

## VI-D. Experimental Validation, Benchmarking, and Reporting Contract

The literature now contains both experimental demonstrations and simulation-heavy studies, but cross-paper comparability remains weak because scenario definitions, baselines, and KPI contracts differ. This makes benchmarking the hinge of Section VI: the earlier subsections show that the control space is rich, but this subsection explains why that richness does not automatically translate into cumulative scientific maturity [O_ISAC_023], [O_ISAC_035], [O_ISAC_054], [O_ISAC_061], [O_ISAC_091], [O_ISAC_112], [O_ISAC_127].

A minimal benchmark contract can be written as

$$
\mathbf{s}=\{\ell,\,C_n^2,\,\sigma_{\text{jitter}},\,\lambda,\,B,\,N_{\text{ORIS}},\,M_{\text{OPA}},\,\bar P,\,P_{\max},\,T_{\text{update}}\},
$$
$$
\mathbf{m}=(R,\,\mathrm{BER},\,m_{\text{res}},\,m_{\text{acc}},\,m_{\text{bnd}},\,P_{\text{out}},\,\text{latency},\,\text{energy}).
$$

Here $\ell$ denotes link distance, $m_{\text{res}}$ denotes a role-consistent resolution or granularity metric, $m_{\text{acc}}$ denotes an empirical accuracy metric such as $\sigma_r$, and $m_{\text{bnd}}$ denotes a bound-type metric such as $\mathrm{CRB}$ or CRLB. For Section II consistency, $m_{\text{res}}$ may be instantiated by $\Delta r_{\min}$ in bandwidth-limited ranging settings or by $\Delta z$ in fiber spatial-granularity settings, but these are not interchangeable and should never be collapsed into a single pooled number without task and medium conditioning. The contract makes scenario assumptions explicit before gains are interpreted and prevents comparisons across incompatible operating conditions.

**Table VI-2 lists the reporting fields needed for reproducible O-ISAC experiments and simulations.**

| Item | Minimum required fields | Why it matters |
|---|---|---|
| Scenario vector disclosure | Full $\mathbf{s}$ values, mobility profile, channel model family | Prevents hidden scenario drift across papers |
| KPI contract disclosure | Full $\mathbf{m}$ values with units, confidence intervals, and metric-role notes | Supports fair comparison of communication and sensing quality without role aliasing |
| Baseline taxonomy | At least one separated baseline and one practical baseline | Prevents inflated gains from weak references |
| Runtime and control budget | Solver runtime, $T_{\text{update}}$, hardware timing, feedback overhead | Distinguishes deployable from offline-only designs |
| Reproducibility package | Parameter files, script versions, data provenance, random seeds | Enables external replication and audit |
| Safety and operating envelope | Optical power settings and safety-margin reporting method | Necessary for translation to certified deployments |

The benchmark chain in VI-D is also the structural backbone of the section as a whole, and Fig. VI-2 is intended to capture that systems-level coupling from enabler choice to deployment-ready evaluation. In whole-manuscript terms, Table VI-2 is the reporting and constraint contract that later deployment-oriented discussion in Section VII and challenge synthesis in Section VIII can inherit directly.

<!--
Fig. VI-2 specification
Purpose: show the Section VI systems chain that links enablers, channel impairments, control/optimization layers, and deployment/benchmark requirements.
Placement: after Table VI-2 and before the VI-D takeaway.
Primary inputs:
- current Section VI prose in drafts/section_06_draft.md
- benchmark contract in Table VI-2
- analysis/VI_evidence_v2/section6E_summary_table.csv for network/overhead cues
Visual form:
- left-to-right layered systems diagram
- Layer 1: programmable enablers (OPA, ORIS, supporting PIC / photonic integration)
- Layer 2: medium and impairment filters (FSO turbulence/weather, VLC geometry/FoV, hybrid transfer constraints, guided-fiber special cases)
- Layer 3: control stack (robustness constraints, co-design optimization, multi-user coordination, AI/security overlay)
- Layer 4: evaluation/deployment gate (runtime, update latency, KPI role separation, benchmark contract, reproducibility)
Caption logic:
- explain that Section VI is not a hardware catalog but a coupled feasibility-to-deployment pipeline
- state that benchmark discipline is the hinge that determines whether enabler gains remain comparable beyond single-paper demonstrations
- prepare the handoff to Section VII by highlighting coordination cost and application absorbability
Design note:
- keep the visual argumentative, not decorative
- use arrows to show dependency, not chronology alone
-->

**VI-D takeaway.** The strongest immediate need is a shared benchmark contract rather than more isolated case studies. Benchmark discipline is what turns promising enablers into cumulative evidence and determines which claims remain credible once the discussion moves beyond single-link exemplars. With that reporting contract in place, Section VI can shift from feasibility to scale, which is the purpose of VI-E.

## VI-E. Networked and Multi-User O-ISAC

Networked O-ISAC introduces burdens that do not appear in single-link settings: multi-user interference, feedback overhead, sensing-fusion consistency, and coordination delay. The corpus already reports explicit FoV and grating-lobe interference effects in multi-user OPA settings, tracking burden growth with user count in mobile ORIS systems, and protocol-level overhead sensitivity in VLC-based networked settings [O_ISAC_009], [O_ISAC_061], [O_ISAC_091], [O_ISAC_098], [O_ISAC_303].

A compact network objective anchor is

$$
\max_{\{\mathbf{w}_k\},\Theta}\;\sum_{k}\omega_k\log\!\left(1+\mathrm{SINR}_k\right)-\lambda\,\mathrm{CRB}(\Theta)
$$
$$
\text{s.t.}\quad \sum_k\|\mathbf{w}_k\|_2^2\le P,\quad \theta_n\in\mathcal Q.
$$

This formulation makes communication, sensing, and ORIS quantization constraints explicit in one multi-user program [O_ISAC_061], [O_ISAC_091], [O_ISAC_127]. Its interpretation still requires fixed detection semantics for $\mathrm{SINR}_k$ and a role-consistent sensing objective rather than a mixed resolution-accuracy score. More importantly for the survey narrative, this subsection is where Section VI begins to connect directly to Section VII: once user count, fusion policy, fairness, and control overhead become dominant, the question is no longer whether an enabler exists but whether a deployment setting can absorb its coordination cost.

**VI-E takeaway.** Multi-user optical O-ISAC is supported by a growing set of targeted studies, but network-level overhead metrics, control-plane timing, and cooperative benchmark contracts remain under-standardized. For the survey narrative, this is the point where enabler analysis becomes deployment analysis: coordination cost, fairness, and sensing-fusion policy begin to shape whether an otherwise promising design is application-ready. Those same pressures also explain why adaptive and security-aware control enters the discussion in VI-F.

## VI-F. AI/ML and Security-Aware Adaptation

AI-assisted adaptation and security-aware design are emerging layers in O-ISAC, especially in dynamic channels where static policies may underperform. At the study-level tag view fixed in Section I, machine learning appears in 53 studies, but only a more limited subset supports direct interpretation as reproducible adaptation or security-aware control in Section VI. The available literature therefore contains targeted reports of learning-driven adaptation for nonstationary environments together with secrecy, authentication, and resilience formulations, but jointly validated AI-plus-security optical benchmarks remain limited [O_ISAC_127], [O_ISAC_145], [O_ISAC_156], [O_ISAC_163]. In the survey flow, this subsection is not meant to compete with the physical enabler evidence in VI-A; it functions as a forward-looking systems layer that explains how controllable optical platforms may later absorb adaptation, trust, and resilience requirements.

A compact secrecy and robust-control anchor is

$$
R_s=[R_b-R_e]^+,
$$
$$
\max_{\mathbf{u}}\;\min_{a\in\mathcal A}\;\alpha R(\mathbf{u})+\beta R_s(\mathbf{u},a)-(1-\alpha-\beta)\,\mathrm{CRB}(\mathbf{u}),
$$
$$
\alpha\ge 0,\;\beta\ge 0,\;\alpha+\beta\le 1,
$$

where $\mathbf{u}$ includes transmitter and ORIS controls inherited from Model VI-U [O_ISAC_127], [O_ISAC_145], [O_ISAC_163]. This framing captures the central tension of this subsection: adaptation gains are only meaningful if they survive uncertainty, overhead, and adversarial pressure rather than only nominal channels. Here again, $R$, $R_s$, and $\mathrm{CRB}$ must be interpreted as role-specific quantities rather than as mutually convertible scores. In most cases, the current evidence should be read as focused demonstrations of learning or secrecy mechanisms, not yet as reproducible proof of mature end-to-end AI-secure O-ISAC stacks.

This is also the place where Section VI must keep maturity asymmetry visible. OPA and ORIS mechanics are presently better evidenced than long-horizon AI adaptation, trust, and adversarial robustness under reproducible protocols. That should be written as a maturity signal, not as a dismissal of the topic, because this distinction helps keep Section VIII grounded later in the manuscript. Put differently, AI/security belongs in Section VI as an emerging overlay on top of better-evidenced optical controllability, not yet as a co-equal maturity tier.

**VI-F takeaway.** AI/ML and security are relevant emerging directions in optical O-ISAC, but current evidence is uneven and should be synthesized cautiously. The field still needs reproducible attack models, overhead-aware reporting, and benchmark-quality evaluation of adaptation under domain shift before strong maturity claims are warranted. Within the survey architecture, VI-F should therefore be read as a bounded forward layer on top of better-evidenced optical controllability, not as the new center of gravity of current evidence. That bounded reading prepares a cleaner handoff to Section VII, where the question becomes which application settings can realistically absorb these layered design choices.

## Section VI Synthesis and Transition

Taken together, VI-A to VI-F suggest that one of the main bottlenecks in optical ISAC is no longer the absence of promising enablers, but the absence of stable reporting and benchmarking contracts that let the community compare those enablers under common assumptions. Read in sequence, the chapter develops a layered argument: OPA and ORIS broaden controllability, robustness models determine whether that controllability survives real channels, co-design methods organize the resulting trade space, benchmarking decides which gains are actually comparable, and networked plus adaptive layers reveal what is required for deployment-facing viability. Supporting substrate themes such as PIC and photonic integration help explain how these levers may be packaged, but they currently play a secondary interpretive role rather than carrying the section's strongest evidence claims. This same layered reading is also what Section VIII later needs: Section VI contributes enabler-linked hardware, control, benchmarking, and deployment constraints, but it deliberately stops short of claiming a standalone roadmap. Yet without explicit disclosure of control overhead, update latency, benchmark assumptions, and sensing-quality definitions, these advances remain difficult to stack into a reproducible system narrative.

This framing gives Section VII a clean handoff: the next question is no longer "what enabling components exist?" but "which deployment patterns and application settings can absorb these coupled design choices in a defensible way?"


## analysis/VII_camera_ready_merge_v1/section_07_camera_ready.md

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


## analysis/VIII_camera_ready_merge_v1/section_08_camera_ready.md

# VIII. Open Challenges and Research Roadmap

Section VIII synthesizes open challenges and frames a deployment-facing research roadmap for optical integrated sensing and communication. In this survey, the challenge map is treated as an organizational taxonomy and is scoped with five exact domains: `standardization_interoperability`, `hardware_scalability_efficiency`, `channel_modeling_evaluation`, `security_privacy_reliability`, and `deployment_convergence_roadmap`. This structure is used to consolidate heterogeneous findings into a consistent challenge lens, not to assert closed-form completeness. Representative evidence indicates that standards alignment and interoperability remain active issues in subsea-integrated settings [O_ISAC_220], while shared-waveform designs continue to expose hardware and implementation complexity tradeoffs in communication-plus-ranging pipelines [O_ISAC_035]. This prioritization supports a traceable transition from challenge diagnosis to roadmap planning.

The evidence policy for this section is intentionally strict. DIRECT support is restricted to text-anchored excerpt rows in the subsection evidence CSVs, whereas upstream bridge rows linking Sections V/VI/VII are treated as INDIRECT by design and interpreted cautiously. Under this policy, representative works show persistent channel-modeling and evaluation consistency gaps in deterministic high-frequency sensing studies [O_ISAC_115], and they also indicate security-facing reliability concerns when sensing and communication functions are co-integrated on the same transmission substrate [O_ISAC_202]. For roadmap framing, deployment convergence is treated as an open issue tied to technology-readiness and multi-constraint rollout planning, with representative survey evidence emphasizing practical integration dependencies [O_ISAC_163].

At the manuscript level, this section operationalizes protocol RQ3 by translating the evidence pack into methodological gaps, 6G-facing integration pressure, and a conservative research agenda. Consistent with the review's TQAF-aware synthesis policy, prioritization is interpreted cautiously whenever support remains indirect, weak, or FLAGGED, and any implication for optical RIS, ORIS, or optical phased arrays is treated only as a forward-looking architectural implication rather than as a separate evidence-bearing challenge domain.

## VIII-A. Standardization and Interoperability Challenges

### Context

VIII-A (Standardization and Interoperability Challenges) frames the `standardization_interoperability` domain as a deployment-facing bottleneck rather than a closed technical problem. Evidence from representative studies indicates that interoperability pressure already appears where sensing and communication must co-exist on shared infrastructure. In SMART subsea settings, standardization is explicitly tied to joint-task-force framing and integrated sensing-communication operation over telecommunication cables [O_ISAC_220]. In optical transport support for ISAC, architecture-level interconnection across RAN, MEC, and SDN-controlled transport highlights practical interoperability requirements spanning radio, transport, and sensing workflows [O_ISAC_025]. A hardware-centric ISAC transceiver review further indicates that emerging standardization efforts and early commercial prototypes are moving the field from isolated demonstrations toward implementation-oriented integration [O_ISAC_161]. Accordingly, this subsection treats `standardization_interoperability` as an open issue focused on interface alignment, cross-domain control consistency, and implementation-ready integration boundaries, with cautious interpretation of any upstream bridge evidence because Section V/VI/VII links are INDIRECT by design.

### Challenge Case 1: Standards Vocabulary and Reference-Model Divergence
**Failure mode.** Without aligned standardization vocabulary and reference-model assumptions, implementations can expose incompatible expectations for integrated sensing-communication operation, which limits cross-system comparability and deployment transferability [O_ISAC_220] [O_ISAC_161].

**Affected interfaces/layers.** The most exposed points are control-plane terminology alignment, sensing-metadata semantics, timing/synchronization assumptions, and transceiver-to-orchestration interface consistency across multi-domain deployments [O_ISAC_220] [O_ISAC_161].

**Evidence snippet summary.** Evidence indicates that SMART-oriented integrated operation is explicitly tied to a standardized framing under a joint task-force context [O_ISAC_220]. A hardware-centric transceiver survey also reports intensified industry activity around standardization and prototype transition, indicating that interface consistency has shifted from conceptual discussion to implementation pressure [O_ISAC_161].

**Practical implication for roadmap.** The roadmap should treat reference-model and terminology alignment as a prerequisite gating item for credible cross-platform evaluation in this domain [O_ISAC_220] [O_ISAC_161].

### Challenge Case 2: Cross-Domain Interoperability Friction in Transport-Supported ISAC
**Failure mode.** When communication and sensing flows are jointly carried but interoperability assumptions differ across transport, orchestration, and sensing-processing stages, routing and capacity decisions can become brittle under operational variability [O_ISAC_025].

**Affected interfaces/layers.** Friction appears at data-plane IQ stream handling, control-plane orchestration and SDN policy exchange, sensing metadata exchange, and timing/latency coordination between access and aggregation segments [O_ISAC_025].

**Evidence snippet summary.** A transport-oriented ISAC architecture shows explicit RAN-core/MEC interconnection requirements and a joint optimization workflow for communication-plus-sensing flows, indicating nontrivial multi-interface coupling [O_ISAC_025].

**Practical implication for roadmap.** Evidence indicates that interoperability profiling across joint sensing/communication transport workflows should remain a first-order roadmap risk item [O_ISAC_025].

### Challenge Case 3: PtMP Branch-Attribution and Measurement-Semantics Misalignment
**Failure mode.** In point-to-multipoint access deployments, sensing pipelines can fail to provide unambiguous branch-level attribution when monitoring assumptions are not aligned with deployment topology and loss conditions, weakening interoperability at the measurement-contract level [O_ISAC_104].

**Affected interfaces/layers.** The main pressure points are sensing-metadata semantics (which branch/event a stream represents), evaluation/reporting contracts for anomaly attribution, and control-layer interpretation of branch-specific sensing quality under splitter loss [O_ISAC_104].

**Evidence snippet summary.** INDIRECT evidence indicates that PtMP structure is described as a practical challenge for fiber-based sensing in deployed access infrastructure, and that splitter-induced link-budget loss can drive sensing failure conditions [O_ISAC_104].

**Practical implication for roadmap.** The roadmap should treat branch-attribution semantics and reporting consistency as a first-class interoperability checkpoint before cross-vendor scaling in access scenarios [O_ISAC_104].

### Challenge Case 4: Sensing-Payload Formatting and DSP-Compatibility Contract Gaps
**Failure mode.** When sensing payload placement and frequency-allocation assumptions are not explicitly aligned with communication signal structure, interoperability can break at receiver processing boundaries and low-interference joint operation becomes fragile [O_ISAC_220].

**Affected interfaces/layers.** Critical interfaces include data-plane sensing-payload formatting, frequency/timing alignment between sensing joints and shore transceivers, and receiver-side DSP interface contracts used for joint demodulation [O_ISAC_220].

**Evidence snippet summary.** Evidence indicates that SMART-oriented dense integration must address precise allocation of sensing information into communication frequency blanks, and that communication-compatible DSP is treated as a compatibility condition [O_ISAC_220].

**Practical implication for roadmap.** Roadmap staging should prioritize explicit format-and-DSP conformance checks for sensing payload interoperability in dense integrated links [O_ISAC_220].

### Math Anchor
Decision variables are profile/format selection, sensing-payload placement policy, and receiver DSP processing mode:

$$
\begin{aligned}
u &= (u_{\mathrm{profile}},u_{\mathrm{placement}},u_{\mathrm{dsp}}),\\
\max_{u}\quad & J_{\mathrm{perf}}(u),\\
\text{s.t.}\quad 
& u_{\mathrm{profile}} \in \mathcal{U}_{\mathrm{SMART\_conform}},\\
& (u_{\mathrm{placement}},u_{\mathrm{profile}}) \in \mathcal{U}_{\mathrm{blank\_allocation}},\\
& (u_{\mathrm{dsp}},u_{\mathrm{placement}}) \in \mathcal{U}_{\mathrm{dsp\_compatible}},\\
& u \in \mathcal{U}_{\mathrm{PtMP\_attribution}},\quad J_{\mathrm{perf}}(u) \in \mathcal{J}_{\mathrm{QoS\_acceptable}}.
\end{aligned}
$$

This anchor uses Option-2 because the available evidence is constraint-centric rather than weight-tuning-centric: SMART is explicitly presented as a standardized configuration, and dense operation is explicitly tied to precise placement of sensing information into communication frequency blanks [O_ISAC_220]. The compatibility requirement is also textual and direct, since sensing transmission format design is linked to communication-compatible DSP behavior, so the feasible set must jointly constrain placement policy and DSP processing mode [O_ISAC_220]. For access-network interoperability, PON evidence reports both standards-linked spectral-occupancy requirements and PtMP ambiguity risk under simultaneous interrogation of multiple drop fibers, which motivates an explicit attribution-integrity constraint [O_ISAC_104]. Finally, the symbolic objective \(J_{\mathrm{perf}}\) is retained as a communication-plus-sensing QoS proxy because spectral-efficiency degradation and sensing-failure risk are both documented in the evidence base [O_ISAC_220] [O_ISAC_104].

### Key Takeaways and Research Priorities
- Interoperability risk in VIII-A is not only a standards-label issue; it also appears in branch-level sensing semantics and attribution contracts under PtMP operation [O_ISAC_104].
- Format compatibility between sensing payloads and communication-oriented DSP flows is a deployment-facing interoperability dependency in dense integrated links [O_ISAC_220].
- Evidence indicates that evaluation/reporting contracts and signal-format contracts should be prioritized separately because they fail at different interfaces [O_ISAC_104] [O_ISAC_220].
- working hypothesis: a compact conformance profile coupling branch-attribution semantics with DSP-interface checks may reduce cross-platform integration ambiguity.

## VIII-B. Hardware Scalability and Efficiency Challenges
### Context
Section VIII-B defines `hardware_scalability_efficiency` as a cross-cutting bottleneck because hardware-plane burdens accumulate even when integrated waveforms improve joint operation [O_ISAC_035][O_ISAC_162]. Evidence indicates that complexity growth is driven by extra baseband processing, filtering, and coordination overhead as integration depth increases [O_ISAC_162]. Representative works also report power/SWaP pressure at edge hardware, including sub-watt energy budgets with delays beyond tens of milliseconds for complex processing pipelines [O_ISAC_093]. A further friction point is implementation scaling in beamforming hardware: fine steering granularity is achievable, but control-system and fabrication burdens increase with larger arrays and tighter precision requirements [O_ISAC_171]. Communication-plane outcomes (rate/BER) and sensing-plane outcomes (resolution/accuracy) are relevant but secondary in this context; the primary blocker is hardware-plane feasibility under scaling, power, and implementation constraints [O_ISAC_093][O_ISAC_162][O_ISAC_171].
### Challenge Case 1: Front-End Co-Design Scalability Bottleneck

1) **Failure mode.** Evidence indicates that independently operated sensing and communication stacks increase hardware complexity, cost, and spectrum inefficiency [O_ISAC_237]. Evidence also indicates that bistatic sensing support can become infeasible on common communication receivers because required analogue FMCW hardware is unavailable [O_ISAC_237].

2) **Affected layers/resources.** The primary impact is hardware-plane: RF front-end sharing, receiver-chain composition, and implementation burden in sensing-aided estimation and interference-cancellation pipelines [O_ISAC_237]. Evidence further indicates that reducing RF hardware complexity and simplifying the FMCW receiver remains a central implementation pressure [O_ISAC_035].

3) **Evidence snippet summary.** Representative texts report both baseline hardware-duplication burden and explicit computational stacks for channel estimation, interference cancellation, and sensing algorithms [O_ISAC_237]. Complementary evidence reports simplified receiver design as a hardware-efficiency target [O_ISAC_035].

4) **Practical implication for roadmap.** For VIII-B, evidence indicates an implementation bottleneck where hardware simplification must keep pace with added receiver processing blocks [O_ISAC_237][O_ISAC_035].

### Challenge Case 2: Edge Energy-Latency Hardware Ceiling

1) **Failure mode.** Evidence indicates that edge deployments face strict hardware feasibility limits because energy budgets are often below 1 watt and processing delays can exceed 50 milliseconds [O_ISAC_093].

2) **Affected layers/resources.** The primary impacts are hardware-plane power/SWaP budgets, edge inference latency budgets, and terminal DSP burdens [O_ISAC_093][O_ISAC_095]. Evidence also indicates increased computational complexity for a single ORIS unit during localization [O_ISAC_112].

3) **Evidence snippet summary.** Representative evidence reports sub-watt edge budgets and delay escalation for complex tasks [O_ISAC_093], and reports that FOE-free processing is used to reduce terminal complexity and power consumption [O_ISAC_095]. Additional evidence reports higher localization-stage complexity for ORIS-aided processing [O_ISAC_112].

4) **Practical implication for roadmap.** Communication-plane and sensing-plane metric gains remain conditional on hardware-plane energy and latency envelopes in edge and terminal implementations [O_ISAC_093][O_ISAC_095][O_ISAC_112].
### Challenge Case 3: Integration-Level Hardware Co-Design and Baseband Cost Escalation

1) **Challenge title.** Integration-level hardware co-design and baseband cost escalation under `hardware_scalability_efficiency`.

2) **Failure mode.** Evidence indicates that optimizing one shared transceiver for sensing and communication is highly challenging because requirements conflict at architecture level [O_ISAC_161]. Evidence also indicates that high mobility and severe path loss can push beam-steering demands beyond economically viable conventional antenna designs [O_ISAC_142].

3) **Affected layers/resources.** The dominant impact is hardware-plane: antenna/RF architecture choices that require continuous trade-off balancing during development [O_ISAC_161]. A second impact is baseband resource pressure, where reused OFDM signals may introduce additional processing complexity and cost [O_ISAC_162].

4) **Evidence snippet summary.** Representative texts report that many architectural/electrical parameters require careful balancing [O_ISAC_161], and that integration level governs extra baseband cost exposure [O_ISAC_162]. Related evidence also reports unresolved analogue front-end drift effects in practical operation [O_ISAC_162].

5) **Practical implication for roadmap.** The VIII-B roadmap should treat integration-level complexity accounting as a hardware gate before scale-out to path-loss-constrained deployments [O_ISAC_161][O_ISAC_142][O_ISAC_162].

### Challenge Case 4: Beam-Control Scalability, FLOP Growth, and Latency Envelope Limits

1) **Challenge title.** Beam-control scalability, FLOP growth, and latency envelope limits in large-array operation.

2) **Failure mode.** Evidence indicates that communication-plane beamforming overhead becomes large in highly mobile cells [O_ISAC_134]. Evidence also indicates that conventional delay-line beam control can require substantial switching/control burden as steering granularity tightens [O_ISAC_171].

3) **Affected layers/resources.** The primary impacts are hardware-plane beam-control complexity and compute-plane FLOP/latency budgets in multimodal beam prediction pipelines [O_ISAC_134][O_ISAC_171]. Representative measurements report millisecond-level processing latency and model-stage complexity concentration [O_ISAC_134].

4) **Evidence snippet summary.** Representative studies report communication-overhead pressure [O_ISAC_134], MMT-dominated complexity and measurable processing latency [O_ISAC_134], and beam-control complexity reduction with scalable frequency-comb steering [O_ISAC_171].

5) **Practical implication for roadmap.** The VIII-B roadmap should co-design steering granularity, model complexity, and hardware budget jointly, rather than scaling them independently [O_ISAC_134][O_ISAC_171].
### Math Anchor
Selected form: Option-2 (resource-constrained performance optimization).

$$
\begin{aligned}
\max_{u=(u_{arch},u_{proc},u_{ctrl})} \quad & U_{perf}(u;s)=\beta_c U_{comm}(u;s_{comm})+\beta_s U_{sens}(u;s_{sens}) \\
\text{s.t.} \quad & C_{hw}(u;s) \le C_{max}, \\
& L_{hw}(u;s) \le L_{max}, \\
& P_{hw}(u;s) \le P_{max}, \\
& O_{ctrl}(u;s) \le O_{max}.
\end{aligned}
$$

This anchor adopts Option-2 because direct evidence supports four distinct hardware constraints for VIII-B: computational burden, processing-latency envelope, energy constraint, and beam-control overhead [O_ISAC_134][O_ISAC_161][O_ISAC_171]. The decision variable tuple $u=(u_{arch},u_{proc},u_{ctrl})$ captures architecture choice, processing schedule, and control-update policy under scenario context $s=(s_{shared},s_{mob},s_{array})$, where shared transceiver use, high mobility, and large-array steering pressure are explicitly evidenced [O_ISAC_134][O_ISAC_161][O_ISAC_171]. Plane separation is explicit in $U_{perf}$: $U_{comm}$ denotes comm-plane utility (beamforming/communication efficiency), while $U_{sens}$ denotes sensing-plane utility (sensing/imaging capability). Constraint $C_{hw}$ bounds compute and baseband complexity, $L_{hw}$ bounds delay, $P_{hw}$ bounds hardware energy demand, and $O_{ctrl}$ bounds steering/control overhead. This keeps hardware scalability and efficiency primary, while permitting performance optimization only inside hardware-feasible regions.
### Key Takeaways and Research Priorities

- Build integration-level complexity ledgers that jointly track RF architecture constraints and baseband-cost escalation before deployment decisions [O_ISAC_161][O_ISAC_162].
- Prioritize hardware-plane beam-control schemes that avoid switch-count explosion while preserving fine steering granularity for large arrays [O_ISAC_171].
- Add calibration-aware front-end drift handling as a first-class hardware requirement for sustained field performance [O_ISAC_162].
- Co-design multimodal pipeline FLOPs, latency envelopes, and beam-pruning strategy to reduce communication-plane overhead without destabilizing beam quality [O_ISAC_134].

## VIII-C. Channel Modeling and Evaluation Challenges

### Context
Evidence indicates that channel modeling and evaluation are foundational for O-ISAC credibility because conclusions are not transferable without validated propagation assumptions across environments and implementations [O_ISAC_005][O_ISAC_327]. Turbulence, pointing, and blockage factors remain a core bottleneck: weather-dependent attenuation and alignment-sensitive behavior can shift effective channel conditions across deployments [O_ISAC_005][O_ISAC_327]. NLoS geometry and intermittency are also unresolved, since multipath and scatterer-dependent effects require explicit modeling and estimation rather than fixed simplifications [O_ISAC_050]. Evaluation practice further needs metric-plane alignment: comm-plane indicators such as BER/capacity should be interpreted together with sensing-plane estimation outcomes, not in isolation [O_ISAC_381][O_ISAC_050]. Finally, benchmarking and reproducibility depend on consistent channel-model disclosure and measurement-campaign comparability, which remains an open issue for reliable cross-study roadmap decisions [O_ISAC_327].

### Challenge Case 1: Weather-Conditioned Channel-Model Transferability Gap

1) **Challenge title.** Weather-conditioned channel-model transferability gap in O-ISAC evaluation.

2) **Failure mode.** Evidence indicates that adverse weather can materially change channel behavior, so assumptions tuned under one condition can fail under another condition [O_ISAC_005]. Evidence also indicates that sensing feedback is tied to the back-scattered signal relation with forward channel gain, creating model drift risk when this relation changes [O_ISAC_005].

3) **Affected interfaces/assumptions.** The most affected interfaces are atmospheric attenuation assumptions, back-scattered-feedback-to-channel-gain mapping, and scenario conditioning for channel-state estimation [O_ISAC_005].

4) **Evidence snippet summary.** Representative text reports that adverse weather reduces FSO link reliability and that evaluation is performed using a realistic channel model with climatic data [O_ISAC_005]. This indicates that portability of conclusions depends on environmental conditioning, not only algorithm selection [O_ISAC_005].

5) **Practical implication for roadmap.** The VIII-C roadmap should treat climate-conditioned model validation as a prerequisite before cross-scenario comparison claims [O_ISAC_005].

### Challenge Case 2: LOS/NLOS Decomposition and Scatterer-State Identifiability Gap

1) **Challenge title.** LOS/NLOS decomposition and scatterer-state identifiability gap in channel evaluation.

2) **Failure mode.** Evidence indicates that practical modeling must decouple LOS and NLOS paths and jointly estimate scattering-related states; otherwise, model mismatch remains likely under multipath conditions [O_ISAC_050].

3) **Affected interfaces/assumptions.** The key interfaces are LOS/NLOS decomposition assumptions, equivalent NLOS channel-state representation, and estimation burden in non-convex settings [O_ISAC_050].

4) **Evidence snippet summary.** Representative text reports an equivalent discrete channel remodeling method that decouples LOS and NLOS paths and a joint estimation strategy for scattering states [O_ISAC_050]. Conclusion text further indicates multipath-interference and random-fading sensitivity in evaluation [O_ISAC_050].

5) **Practical implication for roadmap.** The VIII-C roadmap should prioritize explicit reporting of decomposition assumptions and estimation scope before claiming robust cross-study comparability [O_ISAC_050].

### Challenge Case 3: Comm-Plane Metric Interface Coupling Under Evaluation Conditions

1) **Challenge title.** Comm-plane metric interface coupling under evaluation conditions.

2) **Failure mode.** Evidence indicates that evaluation pipelines rely on comm-plane BER and comm-plane capacity outcomes, and these outcomes shift with transmission-distance settings [O_ISAC_381]. This creates a comparability risk when studies report metrics without a harmonized condition contract [O_ISAC_381].

3) **Affected assumptions/interfaces.** The affected interfaces are metric-definition choices, measurement-condition declarations, and channel-capacity interpretation boundaries across test distances and hardware capture constraints [O_ISAC_381].

4) **Evidence snippet summary.** Representative text reports BER-to-capacity evaluation and distance-conditioned BER/rate behavior [O_ISAC_381]. Additional text indicates capacity degradation with distance growth, reinforcing condition-sensitive evaluation outcomes [O_ISAC_381].

5) **Practical implication for roadmap.** The VIII-C roadmap should treat condition-tagged comm-plane reporting as mandatory before cross-paper ranking claims [O_ISAC_381].

### Challenge Case 4: Benchmark Contract Fragmentation Across Channel Modeling Studies

1) **Challenge title.** Benchmark contract fragmentation across channel modeling studies.

2) **Failure mode.** Evidence indicates that channel-modeling evidence is distributed across heterogeneous measurement campaigns, scenario types, and model families, reducing direct comparability across studies [O_ISAC_327]. Evidence also indicates that new technologies and applications introduce additional modeling challenges that invalidate static benchmark assumptions [O_ISAC_327].

3) **Affected assumptions/interfaces.** The affected interfaces are reporting contracts for channel-model class, measurement-campaign provenance, and framework compatibility for standardization-oriented evaluation [O_ISAC_327].

4) **Evidence snippet summary.** Representative text reports broad survey coverage of measurement campaigns and model families, and explicitly states that a standard VLC channel model is needed for 6G evaluation workflows [O_ISAC_327].

5) **Practical implication for roadmap.** The VIII-C roadmap should treat benchmark-contract normalization as a prerequisite for reproducible evidence aggregation [O_ISAC_327].

### Math Anchor
Selected form: Option-B (benchmark-contract constrained evaluation).

$$
\max_{\pi}\; U_{\mathrm{eval}}(\pi)
$$
$$
\text{s.t.}\; \pi \in \Pi_{\mathrm{contract}},\quad
\Pi_{\mathrm{contract}} = \{\kappa_{\mathrm{cond}},\,\gamma_{\mathrm{geom}},\,\mu_{\mathrm{metric}},\,\delta_{\mathrm{prov}}\}
$$

This anchor maps VIII-C to benchmark-contract constrained evaluation by forcing each result protocol to carry channel-condition tags and scenario-geometry descriptors before cross-paper comparison, which directly follows weather-conditioned channel behavior and geometry-dependent reporting contexts [O_ISAC_005, O_ISAC_327]. The term $\mu_{\mathrm{metric}}$ is comm-plane specific and binds BER-capacity definitions to evaluation conditions (for example distance-conditioned reporting), while sensing-plane metrics are intentionally not instantiated because direct sensing-plane evidence is not present in the locked evidence subset [O_ISAC_381]. The term $\delta_{\mathrm{prov}}$ encodes measurement-campaign and dataset/testbed provenance so that the documented need for a standard model becomes an enforceable contract item rather than a narrative recommendation [O_ISAC_327].

### Key Takeaways and Research Priorities

- Define an evaluation-contract minimum that records channel-model class plus measurement-campaign lineage before any cross-study synthesis step [O_ISAC_327].
- Require comm-plane metric declarations to be bound to measurement conditions in result tables to reduce hidden comparability drift [O_ISAC_381].
- Add a standard-framework compatibility field in benchmarks to align evidence with shared 6G evaluation baselines [O_ISAC_327].
- working hypothesis: a compact reporting card will reduce audit friction in Section VIII-C evidence integration.

## VIII-D. Security, Privacy, and Reliability Challenges

### Context

For VIII-D under security_privacy_reliability, evidence indicates that O-ISAC links couple security, privacy, and reliability because sensing increases observability while communication paths keep exploitable attack surfaces [O_ISAC_145][O_ISAC_039]. Physical-layer threat exposure remains a core motif: wireless transmissions can be susceptible to eavesdropping, so robust protection assumptions should be treated as conditional rather than guaranteed [O_ISAC_145]. A second motif is privacy leakage via sensing-enabled learning pipelines, where confidential user information can be involved and requires controlled data-handling practices [O_ISAC_039]. A third motif concerns authentication/trust posture, which remains tied to physical-layer security mechanisms and legitimacy checks in hybrid deployments [O_ISAC_145]. A fourth motif is fail-safe integrity monitoring, where transport-network ISAC evidence reports real-time warning pathways that can reduce service-interruption risk under disruptive vibration events [O_ISAC_041]. Together, these motifs frame VIII-D as a coupled risk-governance challenge, not a single-metric security problem.

### Challenge Case 1: Physical-Layer Confidentiality and Trust Exposure in Hybrid Links

1) **Challenge title.** Physical-layer confidentiality and trust exposure in hybrid RF-OWC security operation.

2) **Failure mode.** Evidence indicates that wireless links can remain susceptible to eavesdropping, and trust in received sensing/communication outputs can degrade when adversaries manipulate observations [O_ISAC_145].

3) **Affected interfaces/layers.** The affected interfaces include physical-layer signal confidentiality, jammer-aware channel behavior, and trust interpretation in edge decision loops that consume sensing-assisted communication outputs [O_ISAC_145].

4) **Evidence snippet summary.** Representative text states that wireless transmissions are susceptible to eavesdropping and require robust security treatment [O_ISAC_145]. Additional text reports attacker-side falsification risk that can undermine output trustworthiness in hybrid sensing/communication contexts [O_ISAC_145].

5) **Practical implication for roadmap.** The VIII-D roadmap should treat confidentiality-integrity checks as a coupled risk surface that requires safeguards before cross-scenario security claims [O_ISAC_145].

### Challenge Case 2: Privacy Leakage Pressure in Multi-User Sensing-Learning Pipelines

1) **Challenge title.** Privacy leakage pressure in federated multi-user sensing-learning pipelines.

2) **Failure mode.** Evidence indicates that distributed VIPAC training can involve sensitive location/trajectory information, so privacy exposure can increase if update exchange and aggregation boundaries are weakly specified [O_ISAC_039].

3) **Affected interfaces/layers.** The affected layers include metadata/privacy governance at user agents, model-update interfaces between agents and server, and orchestration policies that separate local datasets from shared parameters [O_ISAC_039].

4) **Evidence snippet summary.** Representative text reports explicit privacy-preservation intent in federated training and highlights confidential data-leakage concern in centralized handling [O_ISAC_039]. Additional text reports that only model weights are transmitted while local datasets remain local at user agents [O_ISAC_039].

5) **Practical implication for roadmap.** The VIII-D roadmap should treat privacy controls and update-interface constraints as mandatory context tags for reliability and trust evaluation across studies [O_ISAC_039].

### Challenge Case 3: Authentication and Trust Exposure Under Dense, Heterogeneous Connectivity

1) **Challenge title.** Authentication and trust exposure under dense, heterogeneous connectivity in security_privacy_reliability.

2) **Failure mode.** Evidence indicates that key-based encryption and authentication may be less well-tailored at massive scale, and dynamic key management can become a trust bottleneck [O_ISAC_156].

3) **Affected interfaces/layers.** Affected layers include physical-layer confidentiality/authentication primitives, key-management and distribution interfaces, and edge trust loops that depend on message legitimacy and integrity checks [O_ISAC_156].

4) **Evidence snippet summary.** Representative text states that dense-network operation raises dynamic key-management concerns, while authentication and integrity remain crucial security processes [O_ISAC_156]. The same source treats confidentiality, authentication, and malicious-node detection as coupled targets [O_ISAC_156].

5) **Practical implication for roadmap.** The VIII-D roadmap should treat authentication and trust as lifecycle constraints requiring explicit safeguards and conservative claims across heterogeneous deployments [O_ISAC_156].

### Challenge Case 4: Fail-Safe Integrity Monitoring for Co-Route Fiber Disruption Risk

1) **Challenge title.** Fail-safe integrity monitoring for co-route fiber disruption risk in transport-network operation.

2) **Failure mode.** Evidence indicates that co-route fiber faults can propagate into service interruption, and sudden failures can degrade reliability when warning response is delayed [O_ISAC_041].

3) **Affected interfaces/layers.** Affected interfaces include transport physical infrastructure, sensing-communication coexistence paths, SDN-linked monitoring loops, and edge orchestration decisions for service continuity [O_ISAC_041].

4) **Evidence snippet summary.** Representative text states that interruption events can significantly impede IoE operation and that real-time monitoring/warning is necessary under sudden failures [O_ISAC_041]. Additional text reports SDN-linked timely alerting and service adjustment steps to avoid interruption propagation [O_ISAC_041].

5) **Practical implication for roadmap.** The VIII-D roadmap should prioritize integrity-monitoring readiness in fail-safe loops before claiming reliability under disruption [O_ISAC_041].

### Math Anchor
Selected form: Option-1 (risk-constrained service utility).
- Why Option-2 is weaker: explicit overhead and availability constraint semantics are not directly grounded in the selected evidence subset.

\[
\begin{aligned}
\max_{u=(u_{\mathrm{auth}},u_{\mathrm{mon}},u_{\mathrm{priv}})} \quad & U_{\mathrm{service}}(u) \\
\text{s.t.} \quad & R_{\mathrm{int}}(u) \le \varepsilon_{\mathrm{int}}, \\
& L_{\mathrm{priv}}(u) \le \varepsilon_{\mathrm{priv}}, \\
& A_{\mathrm{auth}}(u) \ge \tau_{\mathrm{auth}}.
\end{aligned}
\]

Evidence indicates that service utility is exposed when network interruption events occur and when falsification risks degrade trustworthiness, so `R_int` is linked to interruption and integrity-monitoring risk under SDN alerting and service-adjustment workflows [O_ISAC_041; O_ISAC_145]. Evidence also reports confidential-data leakage concern and a model-update exchange rule, which directly supports the privacy-leakage constraint `L_priv` and the `u_priv` policy component [O_ISAC_039]. For authentication feasibility, evidence indicates that dense heterogeneous connectivity raises dynamic key-management burden while authentication and integrity remain central security processes, supporting `A_auth` and the `u_auth` policy component [O_ISAC_156]. The monitoring component `u_mon` maps to real-time warning, alert-routing, and service-adjustment evidence [O_ISAC_041]. All thresholds are kept symbolic (`ε_int`, `ε_priv`, `τ_auth`) because no bound values are fixed in the extracted source text.

### Key Takeaways and Research Priorities

- Dense heterogeneous operation can stress key-management assumptions; reliability evaluation should expose trust-loop dependencies rather than assuming static credential logistics [O_ISAC_156].
- Confidentiality, authentication, and malicious-node detection are coupled; fail-safe reliability studies should keep integrity checks as first-class evaluation artifacts [O_ISAC_156].
- Co-route fiber disruption risk is operationally significant; security/privacy framing should be tied to continuity and survivability checks [O_ISAC_041].
- SDN-linked alerting and service adjustment are central to fail-safe behavior; reliability roadmaps should require integrity-monitoring hooks in control loops [O_ISAC_041].

## VIII-E. Deployment Convergence and Roadmap Challenges

### Context

For VIII-E under `deployment_convergence_roadmap`, evidence suggests that deployment convergence remains a distinct bottleneck beyond standards, hardware, channel modeling, and security, because sensing and communication functions may remain insufficiently co-integrated in practice [O_ISAC_039]. Across the micro-evidence set, four motifs recur: coupling between sensing-positioning and communication-channel-estimation tasks, orchestration and state-fusion stress, staged roll-out and readiness gating, and governance for transferability through compatibility, model validity, and provenance controls [O_ISAC_039; O_ISAC_151; O_ISAC_163; O_ISAC_200].

### Roadmap Case 1: Coupled deployment dependency between sensing and communication tasks
When convergence is assumed too early, separate task pipelines may keep bottlenecks at deployment interfaces [O_ISAC_039]. Affected layers include sensing-positioning interfaces, channel-estimation interfaces, and orchestration loops coordinating shared model states in nonstationary contexts [O_ISAC_039]. Source text reports both isolated-design limits and a unified architecture coupling these tasks, suggesting that convergence assumptions require explicit interface-level gating before portability interpretation [O_ISAC_039].

### Roadmap Case 2: Staged roll-out and readiness gating under multi-issue integration pressure
If convergence is treated as immediate, deployment planning may understate coordination requirements across multiple design issues, and readiness interpretation can remain unstable across settings [O_ISAC_163]. Affected layers include deployment orchestration, readiness signaling, and governance interfaces mapping application expectations to implementation constraints [O_ISAC_163]. Evidence indicating that practical implementation and eventual roll-out require issues to be addressed together supports symbolic staged roll-out framing [O_ISAC_163].

### Roadmap Case 3: Orchestration and state-fusion fragility in multimodal context loops
If orchestration assumptions are fixed before interfaces stabilize, multimodal sensing states and context annotations may drift across update loops under resource stress [O_ISAC_151]. Affected layers include orchestration APIs for multimodal inputs, context metadata interfaces (location/time), encoder update loops, and policy gates for state handoff [O_ISAC_151]. Evidence on multimodal physical quantities, contextual enrichment, and encoder-based semantic representations, together with edge-compute and bandwidth stress statements, suggests that context-bearing fusion contracts require readiness-oriented gating [O_ISAC_151].

### Roadmap Case 4: Open-source governance and transferability risk across heterogeneous stacks
If convergence is inferred from isolated implementations, transferability may weaken because infrastructure compatibility conditions and model-validity assumptions can vary across deployments [O_ISAC_200]. Affected layers include reference-stack governance, interoperability with standard DSP pipelines, provenance policy, and audit pathways for deployment claims [O_ISAC_200]. Evidence reports open-source hooks, compatibility pathways, incompatibility risk in some infrastructures, and a realistic time-varying model gap, indicating that governed validation traces remain necessary for portability interpretation [O_ISAC_200].

### Math Anchor

Selected form: readiness-gated deployment utility.

\[
\begin{aligned}
\max_{u=(u_{\mathrm{arch}},u_{\mathrm{api}},u_{\mathrm{stack}},u_{\mathrm{model}},u_{\mathrm{audit}})} \quad & U_{\mathrm{deploy}}(u) \\
\text{s.t.} \quad & g_{\mathrm{ready}}(u) \ge 0, \\
& \operatorname{compat}_{\mathrm{infra}}(u)=1, \\
& \operatorname{budget}_{\mathrm{edge}}(u) \le B_{\mathrm{edge}},\; \operatorname{budget}_{\mathrm{bw}}(u) \le B_{\mathrm{bw}}, \\
& \operatorname{valid}_{\mathrm{model}}(u)=1,\; \operatorname{prov}_{\mathrm{audit}}(u)=1.
\end{aligned}
\]

Here, `U_deploy` and `g_ready` map to coupling and staged deployment pressure [O_ISAC_039; O_ISAC_163], `u_api` with budget constraints captures context-fusion orchestration stress under edge/bandwidth limitations [O_ISAC_151], and governance constraints map to compatibility, model-validity, and provenance evidence from open-source and model-gap statements [O_ISAC_200]. Symbolic `B_edge` and `B_bw` are retained because no numeric deployment budgets are fixed in the cited excerpts.

### Key Takeaways and Research Priorities

- Deployment evaluation can require minimum interface contracts that bind sensing-positioning and channel-estimation coupling with explicit orchestration handoff checks [O_ISAC_039; O_ISAC_151].
- Roadmap claims can require staged readiness gates rather than immediate convergence assumptions when multi-issue integration pressure is present [O_ISAC_163].
- Governance baselines can require compatibility checks, model-validity checks, and provenance/audit traces before transferability interpretation [O_ISAC_200].
- Open-source reference stacks can support reproducibility, but deployment portability may still depend on explicit validation boundaries [O_ISAC_200].

The discussion now shifts from domain-wise challenge clusters to a cross-domain capstone synthesis layer.

## VIII-F. Capstone Dependency Synthesis and Prioritized Research Agenda

Section VIII-F acts as a capstone synthesis rather than a new Axis-2 domain: it summarizes cross-domain dependency coverage and then organizes a prioritized agenda linked to those dependencies. Table VIII-F-1 is derived from linkage counts across Sections V-VII and should be read as an observational co-linkage summary, not as a causal graph. Existing IVLCS/ISAC evidence indicates that shared sensing and communication resources can tighten coordination pressure [O_ISAC_049], repeatable calibration routines can remain restrictive when transfer is attempted across settings [O_ISAC_107], and power-limited OWC integration can add bandwidth and noise-management pressure [O_ISAC_133]. Within the current evidence pack, domains A and C appear as the densest linkage hubs, while domain E appears underlinked; VIII-F treats that pattern as a linkage-gap and governance observation, not as a statement of lower importance.

Table VIII-F-1. Dependency Coverage Summary across A-E domains (observational linkage counts).

| domain | linked_section5 | linked_section6 | linked_section7 | status |
|---|---:|---:|---:|---|
| standardization_interoperability | 55 | 55 | 55 | covered |
| channel_modeling_evaluation | 54 | 54 | 54 | covered |
| hardware_scalability_efficiency | 25 | 25 | 25 | covered |
| security_privacy_reliability | 18 | 18 | 18 | covered |
| deployment_convergence_roadmap | 0 | 0 | 0 | isolated |

Table VIII-F-2 converts these observations into an organizational shortlist. The cite-key-supported agenda items remain explicit: F-AG01 aligns interoperability and evaluation baselines under the A/C hotspot [O_ISAC_133], F-AG02 keeps A/B/C resource contention in scope [O_ISAC_049], F-AG03 retains conservative wording for a hybrid security-evaluation thread that may require a unified analytical framework [O_ISAC_156], and F-AG04 retains conservative wording for prototype-to-scale coordination under calibration overhead [O_ISAC_107]. These rows remain tied to their source papers and are not generalized beyond the cited evidence.

The remaining rows preserve artefact-derived agenda slots rather than new literature claims. F-AG05 is carried by the lower but nonzero D coverage signal, F-AG06 explicitly addresses the E-domain linkage gap as a convergence and governance problem, and F-AG07 preserves balanced A-E coverage under limited editorial or research bandwidth. Accordingly, P1, P2, and P3 are organizational labels assigned from observed co-linkage density, summary coverage, and FLAGGED-evidence concentration rather than scientific rankings. The prioritization anchor below is included only as a survey-level editorial scaffold.

Within this capstone layer, any optical RIS, ORIS, or optical phased array implication remains a forward-looking architectural hook for future integration under RQ3, not a sixth challenge domain and not a direct claim of deployment readiness.

Table VIII-F-2. Prioritized Research Agenda (dependency-aware, evidence-linked, non-causal synthesis).

| agenda_id | title | linked_domains | dependency_tags | evidence_keys | priority_tier | wording_mode |
|---|---|---|---|---|---|---|
| F-AG01 | Align interoperability rules with evaluation baselines | A,C | A55-C54 hub; S5/S6/S7 dense | O_ISAC_133; map:O_ISAC_133; depcov:A,C | P1 | normal |
| F-AG02 | Reduce multi-slot resource contention in optical ISAC | A,B,C | ABC multi-challenge; resource coupling | O_ISAC_049; map:O_ISAC_049; depcov:A,B,C | P1 | normal |
| F-AG03 | Hybrid stacks may require a unified security-evaluation framework | A,C,D | ACD triad; cross-layer security | O_ISAC_156; map:O_ISAC_156; depcov:A,C,D | P1 | conservative |
| F-AG04 | Prototype calibration may require hardware-scaling coordination | A,B,D | ABD triad; prototype-to-scale | O_ISAC_107; map:O_ISAC_107; depcov:A,B,D | P2 | conservative |
| F-AG05 | Keep low-coverage security threads in scope | D | D18 bridge; coverage guardrail | agenda:D; depcov:D | P2 | normal |
| F-AG06 | Bridge E isolation through convergence/governance hooks | A,C,E | E0 linkage gap; governance bridge | agenda:E; depcov:E; summary:n_deployment_convergence_roadmap_papers | P2 | normal |
| F-AG07 | Maintain balanced A-E coverage under fixed bandwidth | A,B,C,D,E | coverage floor; flagged-risk cap | summary_table:all; violations:used_keys | P3 | normal |

### VIII-F Math Anchor (Survey-Level Organizational Prioritization Scaffold)

\[
\begin{aligned}
\max_{x \in \{0,1\}^N}\quad & \sum_{i=1}^{N} w_i x_i \\
\text{s.t.}\quad & \sum_{i=1}^{N} c_i x_i \le B,\\
& \mathrm{cover}_d(x) \ge z_d,\quad d \in \{A,B,C,D,E\}_{\mathrm{selected}},\\
& \mathrm{risk\_flag}(x) \le R_{\max}.
\end{aligned}
\]

Here, `x_i` marks whether agenda item `i` is prioritized; `w_i` is an evidence or dependency weight drawn from the VIII-F artefacts; `c_i` is a symbolic editorial or research bandwidth cost; `cover_d` is a domain-coverage indicator; and `risk_flag` limits the concentration of FLAGGED-evidence items. This is a survey-level organizational scaffold, not a validated scientific law and not a claim of deployment certainty.

The section then closes with an alignment and traceability audit layer across the established domains.

## VIII-G. Cross-Section Alignment and Evidence-Consistency Check

Section VIII-G functions as a capstone cross-section alignment audit rather than a new Axis-2 challenge domain. It checks whether strict Section VIII challenge evidence is reflected in the upstream linkage signals inherited from Sections V, VI, and VII. Under the fixed A-E challenge inventory, this layer serves as a traceability and evidence-consistency check across the established domains, not as an extension of the domain set.

The current artefacts show a fully matched pattern for the A-D domains: `standardization_interoperability`, `hardware_scalability_efficiency`, `channel_modeling_evaluation`, and `security_privacy_reliability` each have equal strict and upstream counts, with `strict_without_upstream_count = 0`. For `deployment_convergence_roadmap`, both strict and upstream counts remain zero, so the row should be read only as a zero/underlinked evidence state within the current pack. The alignment indicates continuity across the existing challenge inventory and does not show completeness of the survey, maturity of a domain, or any importance ranking.

Table VIII-G-1. Cross-section alignment summary between strict Section VIII evidence and upstream linkage signals.

| domain | strict_evidence_count | linked_any_upstream_count | strict_without_upstream_count | interpretation |
|---|---:|---:|---:|---|
| standardization_interoperability | 55 | 55 | 0 | perfectly aligned |
| hardware_scalability_efficiency | 25 | 25 | 0 | perfectly aligned |
| channel_modeling_evaluation | 54 | 54 | 0 | perfectly aligned |
| security_privacy_reliability | 18 | 18 | 0 | perfectly aligned |
| deployment_convergence_roadmap | 0 | 0 | 0 | zero-row; appears underlinked in the current evidence pack |

Methodological caution remains necessary when the alignment pack is interpreted beyond aggregate continuity. In the current example set, every row is labeled `strict_without_upstream`, but the `paper_ids` field is empty throughout, so payload is absent for all five domains. This is consistent with an audit that can validate continuity at the aggregate level and can confirm that no discrepancy rows are populated with paper-level payload.

Because the example payload is absent, VIII-G cannot instantiate paper-level discrepancy narratives from the current artefacts. For final roadmap integration, VIII-G strengthens traceability, not causal inference, and it should remain a continuity check across the established challenge inventory rather than a completeness or maturity claim.

Table VIII-G-2. Example-availability and interpretation limits in the current cross-section alignment pack.

| domain | discrepancy_group | paper_ids_available | interpretation_limit |
|---|---|---|---|
| standardization_interoperability | strict_without_upstream | no | payload is absent; aggregate continuity only |
| hardware_scalability_efficiency | strict_without_upstream | no | payload is absent; aggregate continuity only |
| channel_modeling_evaluation | strict_without_upstream | no | payload is absent; aggregate continuity only |
| security_privacy_reliability | strict_without_upstream | no | payload is absent; aggregate continuity only |
| deployment_convergence_roadmap | strict_without_upstream | no | payload is absent; zero-row remains aggregate-only |

