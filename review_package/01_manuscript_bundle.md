# Review Bundle\n\n## drafts/section_01_introduction.md\n\n# I. INTRODUCTION

## A. The Convergence of Sensing and Communication: A 6G Imperative

The escalating complexity of the electromagnetic environment has intensified demands for ultra-reliable wireless connectivity, driving significant interest in Integrated Sensing and Communication (ISAC) systems [O_ISAC_070:1]. This integrated approach enables ultra-efficient spectrum utilization and significantly reduces hardware costs, and more importantly, establishes a foundational framework for achieving seamless connectivity in future wireless networks [O_ISAC_070:2]. ISAC has now emerged as a core enabler in 6G networks and is recognized as one of the six key usage scenarios by both the ITU-R IMT-2030 framework [O_ISAC_162:1] and 3GPP [O_ISAC_162:2], spanning the coexistence, cooperation, and co-design of communication and sensing functionalities [O_ISAC_070:3].

The intelligence of future society necessitates an immediate requirement for ultra-high-speed communication and ultra-resolution sensing in the 6G era [O_ISAC_016]. As intelligent applicationsâ€”including robot navigation, augmented reality, autonomous driving, and humanâ€“machine interactionâ€”continue to proliferate, these emerging services require the capability of highly-reliable wireless communication and high-accuracy environment sensing simultaneously [O_ISAC_351]. Wireless communication frequency bands are gradually transitioning to higher frequency rangesâ€”encompassing millimeter-wave (mmWave) and terahertz (THz)â€”to fulfill the ultra-high data rate requirements of this vision. **Despite significant progress in RF-based ISAC**, the conventional independent design of communication and sensing systems generally occupies disjoint spectral resources, profoundly aggravating spectrum congestion [O_ISAC_351]. Moreover, using traditional all-electronic approaches to generate mmWave or THz signals will inevitably encounter challenges such as high complexity and **bandwidth limitation**, which will increase the system costs significantly [O_ISAC_286]. To the best of our knowledge, conventional RF-ISAC systems face three fundamental constraints:

1. **Spectrum Congestion**: With the rapid advances of wireless mobile devices, RF communication and sensing systems face challenges such as spectrum congestion, limited bandwidth, and susceptibility to electromagnetic interference [O_ISAC_068]. The exponentially growing demand for mobile data, coupled with stringent sensing resolution requirements of emerging applications (holographic telepresence, digital twins, autonomous navigation), has created significant pressure on the congested RF spectrum [O_ISAC_161].

2. **Limited Resolution and Bandwidth**: The spatial resolution achievable in the mmWave band is fundamentally limited to approximately centimeter-level, insufficient for millimeter-precision applications [O_ISAC_021]. Furthermore, RF-ISAC systems commonly suffer from **spectrum scarcity, high power consumption, and limited sensing capabilities** [O_ISAC_203].

3. **Hardware Constraints**: Purely electrical THz systems struggle to achieve the wide bandwidth and flexible reconfigurability demanded by 6G [O_ISAC_070]. The construction of mmWave/THz ISAC systems using purely electrical means is associated with bandwidth and frequency adjustability limitations that increase overall system complexity [O_ISAC_286].

**Recent advances in photonic THz techniques have opened new opportunities** for transcending these RF limitations. **Optical Integrated Sensing and Communication (O-ISAC)** has emerged as a transformative paradigm that unifies perception, transmission, and processing on optical carriers [O_ISAC_021]. **Fig. 1** illustrates this paradigm evolution through three distinct phases: **(A)** the fundamental spectral and bandwidth constraints of conventional RF-ISAC; **(B)** the transformative opportunities of the optical domain, leveraging the 28.3â€“845 THz spectrum to enable Tbps-class capacity and mm-scale resolution; and **(C)** the unified taxonomy of this survey, which branches O-ISAC into fiber-based, wireless (FSO/THz), and VLC modalities. Our systematic analysis of **221 peer-reviewed O-ISAC studies (2020â€“2025)** reveals that optical ISAC prototypes have pushed these limits: photonic-terahertz integration has achieved **120 Gbps wireless throughput with 2.5 mm sensing resolution** [O_ISAC_105], corresponding to $\text{CRQ}_{\Delta} \approx 4.8\times10^{13}$ bps/m [O_ISAC_105]. Earlier photonic sub-THz demonstrations report $\text{CRQ}_{\Delta}$ on the order of $1.0\times10^{13}$ bps/m [O_ISAC_016].

![Fig. 1. The O-ISAC paradigm evolution. (A) RF-ISAC systems in sub-6 GHz/mmWave bands often face deployment-constrained spectrum and hardware limits, motivating a transition toward photonic carriers to pursue Tbps-class capacity and mm-scale sensing targets. (B) Optical-ISAC leverages the broad photonic spectrum (â‰ˆ28.3â€“845 THz), with implementations clustering in operational windows (telecom for fiber and NIR/visible/photonic-THz for wireless). The survey taxonomy branches Optical-ISAC into fiber-based, free-space/photonic-THz, and VLC/LiFi modalities, each characterized by distinct signal models and dominant impairments.](fig1.png)


Recent photonic and fiber demonstrations illustrate the rateâ€“resolution frontier: a 275 GHz LFM-QAM system reports 120 Gbps with a (two-way) bandwidth-limited range resolution $\Delta r_{\min} \approx 2.5$ mm, yielding $\text{CRQ}_{\Delta} := R / \Delta r_{\min} = 4.8\times10^{13}$ bps/m (equivalently 480 Gbps/cm) [O_ISAC_105]; a D-band sub-THz FDM link delivers 251.03 Gbps with $\Delta r_{\min}=2.5$ cm [O_ISAC_016]; and co-wavelength DAS/DSM over a 38 km seven-core fiber sustains 241.85 Tb/s while sensing 0.1 Hz vibrations with 20 m spatial granularity [O_ISAC_046]. These exemplars highlight the bandwidth advantages of optical carriers and motivate a systematic question.

*These demonstrations motivate a fundamental question: What unique properties of the optical domain enable such performance gains, and how can these advantages be systematically exploited for next-generation ISAC systems?* To address this question, we now examine the physical foundations that position the optical spectrum as the natural substrate for high-performance ISAC.

Table I previews the axis-based comparison of related survey-style works discussed in Section I-D.

### Table I: Axis-Based Comparison of This Survey with Existing Related Survey-Style Works

| Ref. | Year | Tier | Modality Scope (F / FSO / VLC / THz) | Int. Depth | Methodology | Taxonomy | Metrics | Benchmark | Transfer | Enablers |
|:---:|:----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [O_ISAC_161] | 2025 | 2 | â—‹ / â—‹ / â—‹ / â—‹ | â— | Review | â— | â€“ | â€“ | â€“ | â€“ |
| [O_ISAC_068] | 2023 | 2 | â—‹ / â—‹ / â— / â—‹ | â— | Narrative | â€“ | â€“ | â€“ | â€“ | â€“ |
| [O_ISAC_327] | 2024 | 2 | â—‹ / â—‹ / â— / â—‹ | â— | Survey | â— | â€“ | â€“ | â€“ | â€“ |
| [O_ISAC_006] | 2024 | 2 | â— / â—‹ / â—‹ / â—‹ | â— | Review | â€“ | â— | â€“ | â€“ | â€“ |
| [O_ISAC_368] | 2023 | 2 | â— / â—‹ / â—‹ / â—‹ | â— | Review | â€“ | â€“ | â€“ | â€“ | â€“ |
| [O_ISAC_021] | 2023 | 2 | â—‹ / â— / â—‹ / â—‹ | â— | Tutorial | â— | â— | â€“ | â€“ | â— |
| [O_ISAC_070] | 2025 | 2 | â—‹ / â—‹ / â—‹ / â— | â— | Narrative | â— | â€“ | â€“ | â€“ | â€“ |
| [O_ISAC_163] | 2025 | 2 | â—‹ / â—‹ / â—‹ / â—‹ | â— | Survey | â— | â€“ | â€“ | â— | â— |
| [O_ISAC_303] | 2024 | 1 | â—‹ / â—‹ / â— / â—‹ | â— | Review | â— | â— | â€“ | â€“ | â€“ |
| **This Survey** | **2026** | **â€“** | **â— / â— / â— / â—** | **â—** | **PRISMA 2020** | **â—** | **â—** | **â—** | **â—** | **â—** |

*Legend: â— = strong/explicit (Score 1); â— = partial/within-modality (Score 0.5); â€“ = absent (Score 0); â—‹ = out-of-scope. Modality Scope uses (â—‹/â—/â—) only. F = Fiber, FSO = Free-Space Optics, VLC = Visible Light, THz = Photo-THz. THz denotes photonic-THz / opticalâ€“THz bridging O-ISAC (not generic RF THz-ISAC hardware surveys).*
*Scoring Criteria: Symbols are mapped via $s_a(p) \in \{0, 1/2, 1\}$ to $\{â€“, â—, â—\}$ based on evidence strength: **â—** = Systematic/Cross-modal (e.g., unified taxonomy, defined benchmark suite); **â—** = Partial/Single-modality; **â€“** = Absent/Unaddressed.*

## B. The Optical Opportunity: A Vast and Untapped Frontier

Moving from the RF spectrum crisis to a potential solution, the optical domainâ€”spanning the infrared (IR), visible, and ultraviolet bandsâ€”presents an opportunity of transformative scale. While RF-ISAC operates within a congested spectrum below 300 GHz, O-ISAC nominally spans approximately **28.3 THz to 845 THz** (corresponding to wavelengths from 355 nm to 10.6 Î¼m), though practical systems cluster within established atmospheric transmission windows and fiber telecom bands [O_ISAC_021]. In this survey, Photo-THz O-ISAC refers to photonics-enabled architectures where optical carriers are used for generation/LO/distribution, while the wireless propagation carrier resides in the sub-THz/THz bandâ€”thus forming an opticalâ€“THz bridging modality. This section elucidates the fundamental physical advantages that position the optical domain as the natural substrate for next-generation ISAC systems.

### B.1 Quantitative Comparison: RF-ISAC vs. O-ISAC

To ground our analysis in empirical data, Table II presents a head-to-head comparison between RF-ISAC modalities (WiFi, mmWave) and O-ISAC, synthesized from our systematic corpus analysis of 221 peer-reviewed studies [O_ISAC_021].

**Table II: RF-ISAC vs. O-ISAC Performance Comparison [O_ISAC_021]**

| Characteristic | RF-ISAC (Sub-6 GHz / mmWave) | Wireless O-ISAC (FSO / VLC / Photo-THz) | Wired O-ISAC (Fiber Sensing) |
| :--- | :--- | :--- | :--- |
| **Carrier Frequency** | 2.4â€“100 GHz | 0.1â€“10 THz (Photo-THz) + 28.3â€“845 THz (FSO/VLC) | 193 THz (C-Band / L-Band) |
| **Physics Model** | Diffuse Multipath (Rich) | Line-of-Sight (LoS) Dominated | Guided Mode (Low Loss, Dispersive) |
| **Signal Type** | Complex (I/Q) | Real (IM/DD) or Complex (Coherent FSO) | Complex (Coherent Phase/Polarization) |
| **Key Impairments** | Interference, Multi-path Fading | Ambient Light, Turbulence, Pointing Error | Nonlinearity (Kerr), PMD, Phase Noise |
| **Sensing Task** | Radar (Range/Doppler) | Localization, Gesture, Surface Profiling | DAS (Vibration), Strain, Temperature |
| **Peak Data Rate** | ~10â€“20 Gbps | **~100â€“120 Gbps** [O_ISAC_105] | **> 200 Tbps** (Aggregate) [O_ISAC_046] |
| **Resolution** | cm-level | **mm-level (2.5 mm)** [O_ISAC_105] | m-level (Spatial) / nÎµ (Strain) |

### B.2 Three Competitive Advantages of O-ISAC

Drawing from the generalized O-ISAC system architecture proposed in [O_ISAC_021], we identify three fundamental advantages that differentiate optical approaches from their RF counterparts. **Fig. 2** provides a technical "zoom-in" on the physical mechanisms underlying these advantages, contrasting optical physics with RF constraints.

![Fig. 2. Physical mechanisms behind the three competitive advantages of O-ISAC. (Left) Capacity scaling is achieved via dense Multiplexing (WDM/SDM), enabling aggregate rates of 241.85 Tb/s (wired) [O_ISAC_046] and dense parallel channels (wireless) [O_ISAC_021]. (Center) Sensing precision is driven by ultra-wide effective bandwidth, enabling wireless range resolution down to $\Delta r_{\min} = 2.5$ mm and $\text{CRQ}_{\Delta}$ of $4.8\times10^{13}$ bps/m (480 Gbps/cm) [O_ISAC_105]. (Right) Spatial isolation is inherent to narrow optical beams, reducing multi-user interference and RF-EMI susceptibility compared to wide RF sectors.](fig2.png)


#### Advantage 1: Capacity Scaling Through Spectral Abundance and Multiplexing

The optical spectrum (spanning **28.3 THz to 845 THz** [O_ISAC_021]) offers massive resources for dense multiplexing. Unlike RF systems limited by sub-6 GHz blocks, optical carriers support massive parallelism as illustrated in **Fig. 2 (Left)**:
- **Wireless Parallelism:** Experimental demonstrations of Mode Division Multiplexing (MDM) combined with WDM have realized **64 parallel channels** (16 wavelengths Ã— 4 OAM modes) to scale wireless throughput [O_ISAC_021].
- **Wired Aggregate Capacity:** In the cabled domain, Space Division Multiplexing (SDM) using 7-core fiber has achieved an aggregate capacity of **241.85 Tbps** (96 WDM channels Ã— 7 cores) over 38 km [O_ISAC_046].
*These independent demonstrations validate the scalability of optical multiplexing beyond single-link RF limits.*

#### Advantage 2: Enhancing Sensing Precision via Ultra-Wide Bandwidth

Range resolution ($\Delta r_{\min}$) is bandwidth-limited in two-way sensing according to $\Delta r_{\min} = v/(2B_{\text{eff}})$ (two-way ranging convention). The ultra-wide bandwidths available in the optical domain enable millimeter-level resolution that is physically difficult for narrowband RF systems to match (**Fig. 2, Center**):
- **Wireless Ranging:** Photonic-THz systems have demonstrated a **range resolution of 2.5 mm** alongside 120 Gbps data transmission [O_ISAC_105].
- **Capacity-Resolution Quotient (CRQ$_{\Delta}$):** This combination yields $\text{CRQ}_{\Delta} := R / \Delta r_{\min}$ of $4.8\times10^{13}$ bps/m (480 Gbps/cm) for wireless ranging [O_ISAC_105].
*Note: We strictly distinguish bandwidth-limited range resolution ($\Delta r_{\min}$) from SNR-dependent range accuracy ($\sigma_r = \sqrt{\mathbb{E}[(\hat r - r)^2]}$). While fiber DAS achieves meter-level spatial granularity ($\Delta z \approx 20$ m [O_ISAC_046]), its sensing value lies in ultra-sensitive vibration detection rather than high-resolution ranging.*

#### Advantage 3: Spatial Isolation and Reduced RF-EMI Coupling
The high directionality of optical beams provides deployment-dependent spatial isolation, significantly reducing Multi-User Interference (MUI) compared to wide-beam RF sectors in clear line-of-sight scenarios [O_ISAC_021]. While wireless O-ISAC links remain susceptible to atmospheric turbulence and ambient light [O_ISAC_003], their reduced susceptibility to conventional RF Electromagnetic Interference (EMI) and narrow beam divergence (typically on the order of milliradians [O_ISAC_021]) enable dense spatial reuse in deployment scenarios with favorable propagation conditions.

### B.3 Unified O-ISAC Taxonomy

Having established the physical mechanisms behind the three optical advantagesâ€”capacity scaling via multiplexing, bandwidth-limited ranging resolution, and directional spatial isolationâ€”we next formalize the scope of this survey. Specifically, the O-ISAC literature does not constitute a single monolithic system class; rather, it clusters into distinct modalities determined by the propagation medium and the associated signal/impairment models. **Fig. 3** summarizes the resulting evidence-based taxonomy from our PRISMA-compliant 2020â€“2025 corpus, organizing O-ISAC into four modalities (fiber, free-space optical, VLC/LiFi, and photonic-THz) with their representative operating windows, dominant techniques, and canonical sensingâ€“communication metrics.

![Fig. 3. The unified taxonomy of O-ISAC modalities derived from a systematic PRISMA-compliant analysis of 221 primary studies (2020â€“2025). (Top-Left) Fiber O-ISAC (Cabled) leveraging existing DAS/DSCM infrastructure for long-haul (>100 km) sensing and Tb/s-scale data transmission. (Top-Right) Free-Space Optical (FSO) O-ISAC for outdoor inter-building links utilizing coherent detection and atmospheric compensation. (Bottom-Left) Visible Light Communication (VLC) O-ISAC for indoor environments using LED infrastructure for joint illumination, high-speed connectivity, and sub-centimeter positioning. (Bottom-Right) Photonic Terahertz (Photo-THz) O-ISAC bridging the optical and wireless THz domains to achieve the highest reported $\text{CRQ}_{\Delta}$ metrics (>100 Gbps/cm, i.e., >$1.0\times10^{13}$ bps/m).](fig3.png)


1. **Fiber O-ISAC (Cabled):** Integration of DAS/DFOS with coherent optical transmission over single-mode/few-mode fibers. Key techniques include Ï†-OTDR, DSCM, and WDM-based sensing-communication multiplexing.

2. **Free-Space Optical (FSO) O-ISAC:** Outdoor/inter-building links using 1550 nm laser transmission with atmospheric channel compensation. Achieved ranges: <1 km with 100 Gbps capacity.

3. **Visible Light Communication (VLC) O-ISAC:** Indoor systems leveraging LED illumination infrastructure for simultaneous lighting, communication, and positioning. Key modulations: DCO-OFDM, CE-OFDM, OOK.

4. **Photo-THz O-ISAC:** Photonic-assisted sub-THz (100â€“300 GHz) systems bridging optical generation with wireless THz transmission. This emerging modality offers the highest reported $\text{CRQ}_{\Delta}$ values (>100 Gbps/cm, i.e., >$1.0\times10^{13}$ bps/m) [O_ISAC_016].

This unified taxonomy bridges the previously disjoint communities of optical communications, distributed fiber sensing, and optical wireless researchâ€”providing a coherent framework for cross-domain technology transfer. This taxonomy provides a common reference frame; however, the same modality boundaries also expose a deeper issueâ€”terminology, metrics, and evaluation protocols remain inconsistent across communities, motivating the fragmentation challenge discussed next in Section I-C.

## C. The Fragmentation Challenge: A Landscape Without Unity

Despite the compelling physical advantages outlined above, the O-ISAC research landscape remains highly fragmented. Our systematic analysis of **221 peer-reviewed O-ISAC studies (2020â€“2025)** reveals four intertwined manifestations of this fragmentationâ€”(i) inconsistent terminology, (ii) non-standardized sensing metrics, (iii) siloed modality communities, and (iv) limited cross-domain technology transferâ€”together impeding reproducibility, cross-study comparability, and ultimately the maturation of a unified 6G optical sensingâ€“communication framework.

**Terminology Proliferation.** A foundational barrier to synthesis is the proliferation of synonymous and near-synonymous terms for closely related concepts. For instance, a single work may frame ISAC under an umbrella of aliases such as *"radar-communication (RadCom), joint radar-communication (JRC), and other related terms"* [O_ISAC_161], while VLC-centric studies describe *"Joint Communication and Sensing (JCS), also known as Integrated Sensing And Communication (ISAC), [and] Sensing-Communication Integration (SCI)"* [O_ISAC_068]. In the fiber community, the vocabulary further diverges into "ISAC-OF" (ISAC in optical fiber), "fiber-ISAC," and "photonic ISAC" [O_ISAC_041], [O_ISAC_033]. This aliasing is not merely cosmetic: it complicates systematic discovery, inflates perceived novelty through re-labeling, and obscures conceptual linkages across modalities and hardware assumptions.

**Metric Non-Isomorphism.** Equally problematic is the absence of a shared sensing-performance language. A first-order example is the recurrent conflation of **physical resolution limits** with **estimator-dependent accuracy** and **information-/estimation-theoretic bounds**. For ranging, the bandwidth-limited (two-way) physical resolution is governed by
$$
\Delta r_{\min}=\frac{v}{2B_{\text{eff}}},
$$
where $v=c$ in free space and $v\approx c/n_g$ in guided media (with group index $n_g$), hence representing a modality-dependent propagation speed but a common bandwidth principle. In contrast, reported "accuracy" metricsâ€”RMSE, $\sigma_r = \sqrt{\mathbb{E}[(\hat r - r)^2]}$, or "localization error"â€”are inherently SNR-dependent and estimator-dependent, while CRB/FIM-based quantities characterize information-/estimation-theoretic bounds under an explicitly stated observation model [O_ISAC_013], [O_ISAC_050], [O_ISAC_056]. The practical consequence is that papers can report "resolution" in incommensurate senses: fiber DAS studies may report "spatial resolution" as a minimum resolvable segment length [O_ISAC_013], whereas FSO ranging papers may report "range resolution" via bandwidth-derived definitions [O_ISAC_035]. Additionally, "signal quality" is not referenced to a consistent measurement plane: coherent fiber systems often report OSNR in the optical domain [O_ISAC_028], whereas VLC systems typically report electrical SNR after photodetection [O_ISAC_009], complicating direct cross-modality comparisons without an explicit normalization convention.

**Sub-Domain Siloing and Limited Cross-Citation.** The literature has evolved along several largely independent trajectoriesâ€”fiber DAS/communication co-design, FSO rangingâ€“communication integration, VLC positioningâ€“data links, and photonic-THz ISACâ€”each anchored in distinct channel models (guided vs. turbulent vs. LoS-dominated), transceiver paradigms (coherent DSP-driven optics vs. IM/DD LEDs), and evaluation benchmarks, with limited cross-pollination [O_ISAC_033], [O_ISAC_050], [O_ISAC_082]. Consequently, what appears as a "trade-off frontier" in one modality is often not directly comparable to another without carefully harmonized assumptions and metrics. This siloing is echoed in recent assessments: *"VLC and VLP systems are usually designed separately... mutual benefits between positioning and communication have not been utilized effectively"* [O_ISAC_039], and *"interoperability and certification across sectors remain a significant barrier"* [O_ISAC_161].

**Weak Cross-Domain Technology Transfer.** Beyond vocabulary and metrics, fragmentation manifests as limited portability of methods and abstractions. Waveform and probing strategies developed in fiber-ISAC contexts (e.g., LFM-embedded training structures [O_ISAC_042], polarization-based sensing probes [O_ISAC_074]) are only rarely transferred to free-space or VLC channels, while VLC-driven approaches (e.g., multi-carrier localization with m-CAP [O_ISAC_022], learning-enabled joint positioning [O_ISAC_039]) seldom reappear in FSO or photonic-THz settings. Hardware constraints further impede transfer: coherent fiber transceivers rely on DSP-intensive equalization and phase-sensitive reception [O_ISAC_033], whereas IM/DD LED-based O-ISAC is amplitude-constrained and often bandwidth-limited [O_ISAC_054]. In the absence of shared benchmarks and reporting protocols, it remains difficult to distinguish what is fundamentally modality-specific from what is transferable across optical platforms [O_ISAC_068], [O_ISAC_067].

**The Missing Unifying Framework.** Collectively, these issues point to a critical gap: the absence of a unified physical-layer taxonomy, a standardized performance-reporting contract, and a cross-modality benchmark suite. A minimal reporting contract should at least specify: (i) communication performance (rate, BER/FEC margin), (ii) sensing performance separated into physical resolution $\Delta r_{\min}$, estimator-level error (RMSE/$\sigma_r$), and information-/estimation-theoretic bounds (CRB/FIM), (iii) signal quality defined at an explicit reference plane (electrical SNR vs. OSNR), and (iv) channel/scenario assumptions that govern comparability. Recent calls for *"a standard VLC channel model... following the modeling methodology of 3GPP"* [O_ISAC_327] and for *"standardization efforts for facilitating interoperability"* [O_ISAC_068], [O_ISAC_082] underscore the urgency of this unification. Without such a framework, O-ISAC risks continued siloing, duplicated effort, and missed opportunities for cross-domain synergyâ€”an observation that directly motivates the next section, where we systematically position existing surveys and identify the gaps that our PRISMA-based unified treatment addresses.

## D. Related Surveys and Gap Analysis

The rapid maturation of RF-based ISAC has given rise to a well-developed survey landscape in the radio-frequency domain, where comprehensive tutorials address waveform design, beamforming strategies, and information-theoretic limits for dual-function radar-communication systems. Hardware-centric ISAC transceiver surveys (RF-oriented) provide useful background but do not address optical modalities [O_ISAC_161]. In contrast, the optical ISAC domain remains comparatively underserved: existing review-style works are distributed across disjoint modality communitiesâ€”VLC positioning, distributed fiber sensing, FSO channel modeling, and photonic-THz transmissionâ€”with limited cross-pollination and no unifying systematic treatment. This section maps the current landscape of related survey-style works, organized into Tier-1 (true O-ISAC surveys within our corpus) and Tier-2 (feeder/adjacent works that inform but do not unify the O-ISAC narrative), and identifies the critical gaps that motivate the present systematic review.

**VLC Positioning and Indoor Optical Surveys.** A growing body of work examines visible light communication for indoor positioning and data transmission. Studies exploring joint communication and sensing prospects through visible light highlight the potential of VLC for simultaneous high-speed data links and localization, while noting that spectrum scarcity, interference management, and hardware limitations remain significant barriers [O_ISAC_068]. Channel characterization surveys for VLC-IoE applications in 6G provide detailed modeling of indoor optical propagation but focus primarily on the communication link rather than integrated sensing functionality [O_ISAC_327]. Experimental works on integrated VLC positioning and communicationâ€”including 6-DoF location-and-pose estimation algorithms [O_ISAC_062] and photonic W-band ISAC demonstrations [O_ISAC_044]â€”advance individual system designs but do not consolidate findings into a unified cross-modality framework.

**Distributed Fiber Sensing and Fiber-ISAC Reviews.** In the cabled domain, distributed fiber optic sensing (DFOS) techniquesâ€”particularly Ï†-OTDR-based distributed acoustic sensing (DAS)â€”have reached commercial maturity for infrastructure monitoring. Recent works addressing integrated sensing and communication in optical fiber present the current development status and representative system architectures [O_ISAC_006], while experimental demonstrations of co-route fiber recognition and status diagnosis based on ISAC principles [O_ISAC_041] and high-precision vibration localization in bidirectional transmission systems [O_ISAC_090] illustrate the growing interest in fiber-ISAC integration. Ultra-large dynamic vibration sensing with fronthaul analog radio-over-fiber transmission further extends the sensingâ€“communication co-design paradigm [O_ISAC_189]. However, these works remain largely anchored in fiber-specific channel models and DSP paradigms, with limited consideration of how insights might transfer to wireless optical or hybrid fiber-wireless scenarios.

**FSO Channel Modeling and Photonic-THz Surveys.** Free-space optical (FSO) and photonic-terahertz research constitutes a third cluster of related work. Conceptual overviews of optical integrated sensing and communication discuss architectures, potentials, and challenges for FSO-ISAC [O_ISAC_021], while emerging demonstrations of MIMO FSO with fiber Bragg grating sensors illustrate 6G IoT application potential [O_ISAC_199]. Waveform-centric studiesâ€”including OCDM-based FMCW design for FSO ISAC [O_ISAC_035] and photonic-based flexible ISAC with multiple targets detection capability [O_ISAC_058]â€”advance signal processing techniques but do not synthesize findings across the FSOâ€“fiberâ€“VLC divide. In the photonic-THz domain, survey-style treatments exploring integrated waveforms for THz-ISAC systems summarize recent worldwide research efforts and extrapolate technological evolution tendencies [O_ISAC_070], complemented by demonstrations achieving 251 Gbps real-time communication with cm-scale sensing [O_ISAC_016] and THz-over-fiber systems based on orthogonal chirp division multiplexing [O_ISAC_077]. These works collectively highlight photonic-THz as the highest-CRQ$_{\Delta}$ modality but do not bridge to VLC or fiber sensing communities.

**True O-ISAC Surveys (Tier-1).** Within our systematic corpus of 221 studies, only one work explicitly frames optical ISAC as its primary subject: the VLC-based LiSAC review [O_ISAC_303]. A separate RIS-for-ISAC survey [O_ISAC_163] provides enabling-technology context but remains RF/THz-centric and is therefore treated as Tier-2 in Table I. Notably, the VLC review does not apply a systematic methodology (e.g., PRISMA) and remains anchored to a single modality rather than spanning the full fiberâ€“FSOâ€“VLCâ€“photo-THz spectrum under a unified physical-layer abstraction.

**Gap Synthesis.** Within the optical-ISAC corpus considered in this review, our analysis reveals five critical gaps that distinguish the current landscape from a unified framework. First, no cross-modality, modality-agnostic taxonomy spanning fiberâ€“FSOâ€“VLC/LiFiâ€“photo-THz under a single PHY abstraction is available; existing survey-style works typically remain medium-centric (e.g., [O_ISAC_303] for VLC, [O_ISAC_006] for fiber), often with overlapping or inconsistent definitions. Second, among the identified survey-style works in the considered corpus, PRISMA-aligned systematic methodology is not adopted; most contributions employ narrative or tutorial-style treatments that limit reproducibility and evidence-traceable synthesis. Third, metric normalization remains unresolved: no standardized reporting contract consistently separates bandwidth-limited physical resolution (e.g., $\Delta r_{\min} = v/(2B_{\text{eff}})$) from estimator-dependent accuracy (e.g., RMSE/$\sigma_r = \sqrt{\mathbb{E}[(\hat r - r)^2]}$) and information-/estimation-theoretic bounds (CRB/FIM), nor does a common convention exist for signal-quality reporting across modalities (electrical SNR after photodetection versus optical OSNR/power-budget conventions). Fourth, cross-domain technology transfer is underexplored, with limited explicit evaluation of portability of waveform/probing strategies and DSP abstractions across media (e.g., from coherent fiber sensing to FSO/VLC). Fifth, emerging enabling technologiesâ€”such as optical RIS and optical phased arraysâ€”are treated in a fragmented, technology-centric manner rather than through a systematic synthesis of integration pathways and modality-agnostic design abstractions. Table I summarizes these limitations by comparing this survey against representative Tier-1 and Tier-2 survey-style works; it reports *context descriptors* (Tier, modality scope, integration depth, methodology) and evaluates **five gap axes** (taxonomy, metrics, benchmarking, transfer, enablers).

These gaps collectively establish the rationale for this survey: a PRISMA-compliant systematic review that unifies O-ISAC across all four modalities, establishes a standardized taxonomy and reporting contract, and synthesizes quantitative trade-off frontiers to guide future research.

> **Lesson 1:** Without axis-aligned reporting (scopeâ€“taxonomyâ€“metricsâ€“benchmarksâ€“transfer), the existing survey landscape cannot be converted into a defensible cross-modality O-ISAC research gap.





## E. Contributions of This Survey

To close the five gaps identified in Section I-D, we provide evidence-backed contributions grounded in the PRISMA corpus and extraction schema; each item includes a compact Contribution-Gap-Section mapping:

1. **PRISMA evidence base and quality scoring (Gap 2):** We apply the PRISMA 2020 protocol [14] to a unified corpus of 221 studies with bibliographic year metadata available for 219 records (210 in 2020-2025), and we report complete 5-dimension TQAF scores for 208 studies. *Contribution-Gap-Section:* Gap 2 -> Section III.

2. **Cross-modality taxonomy with measured coverage (Gap 1):** We construct a unified taxonomy spanning fiber, FSO, VLC/visible-light, photo-THz, and hybrid O-ISAC; the extracted medium labels include 46 fiber, 19 FSO, 26 VLC/visible-light/UV, 1 photo-THz, and 116 hybrid studies (optical-THz bridging can appear under hybrid depending on the extraction label ontology). *Contribution-Gap-Section:* Gap 1 -> Section IV.

3. **Standardized reporting contract and trade-off synthesis (Gap 3):** We normalize reporting using $\Delta r_{\min}$, $\sigma_r$, and $\text{CRQ}_{\Delta}$ and quantify coverage: 217 studies report data-rate metrics, 213 report a resolution-type metric ($\Delta r_{\min}$ in ranging or $\Delta z$/spatial granularity in fiber), 208 report $\sigma_r$, and 171 report CRB/CRLB values; 213 studies report both rate and a resolution-type metric, enabling $\text{CRQ}_{\Delta}$ comparisons where $\Delta r_{\min}$ is available (N_rate_and_resType = 213; N_rate_and_Drmin = 160). *Contribution-Gap-Section:* Gap 3 -> Section V.

4. **Enabler-centric synthesis across optical platforms (Gap 5):** We quantify enabling-technology prevalence to ground Section VI, including machine learning (53 studies), optical RIS (ORIS, 8 studies), and optical phased arrays (OPA, 7 studies), and relate these tags to the integration pathways discussed in the enabler section. *Contribution-Gap-Section:* Gap 5 -> Section VI.

5. **Cross-domain transfer map tied to applications (Gap 4):** We build a modality-application transfer map in Section VII; 15 application domains appear in >=2 modality classes (8 domains in >=3), with high-frequency domains including industrial manufacturing (65), vehicular (60), indoor positioning (56), and 6G networking (46). *Contribution-Gap-Section:* Gap 4 -> Section VII.

> **Lesson 2:** A systematic, PRISMA-based methodology enables reproducible evidence synthesis and uncovers research gaps that are invisible in narrative reviews.

## F. Organization of This Paper

The remainder of this survey is organized as follows, and an overview is illustrated in Fig. 4:

- **Section II (Technical Fundamentals)**: Provides the physical-layer foundations of optical sensing and communication, covering modulation schemes, channel models, and hardware architectures.

- **Section III (Methodology)**: Details the PRISMA 2020-compliant systematic review methodology, including search strategy, eligibility criteria, study selection process, and the 5-dimensional Technical Quality Assessment Form (TQAF).

- **Section IV (Unified O-ISAC Taxonomy)**: Presents the proposed cross-domain taxonomy, organizing 221 studies by medium, integration mechanism, and signal dimension.

- **Section V (Performance Trade-off Analysis)**: Synthesizes quantitative performance metrics to characterize rate-resolution trade-offs and Pareto-optimal operating regions.

- **Section VI (Enabling Technologies)**: Analyzes key enabling technologies including ORIS, OPA, photonics-assisted signal generation, and machine learning integration.

- **Section VII (Applications and Use Cases)**: Discusses O-ISAC applications across smart infrastructure, transportation, healthcare, and industrial IoT domains.

- **Section VIII (Open Challenges and Research Roadmap)**: Identifies critical gaps and outlines a future research agenda toward 6G integration.

- **Section IX (Conclusions)**: Summarizes the key findings and provides closing remarks.

[*Insert Fig. 4: Survey organization and structure overview*]

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
| **Ï†-OTDR** | Phase-Sensitive Optical Time-Domain Reflectometry |
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
| **CRB** | CramÃ©r-Rao Bound |

---

# REFERENCES

[1] ITU-R, "Framework and overall objectives of the future development of IMT for 2030 and beyond," Recommendation ITU-R M.2160-0, Nov. 2023.

[2] C. de Lima *et al.*, "Convergent Communication and Sensing in 6G: Visions, Prospects, and Challenges," *IEEE Communications Magazine*, vol. 59, no. 1, pp. 12â€“18, Jan. 2021.

[3] F. Liu *et al.*, "Integrated Sensing and Communications: Towards Dual-Functional Wireless Networks for 6G and Beyond," *IEEE J. Sel. Areas Commun.*, vol. 40, no. 6, pp. 1631â€“1652, Jun. 2022.

[4] IEEE 802.11 Working Group, "Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specificationsâ€”Amendment: Enhancements for WLAN sensing," IEEE Std 802.11bf (Draft), 2024.

[5] Z. Zhang *et al.*, "6G Wireless Networks: Vision, Requirements, Architecture, and Key Technologies," *IEEE Veh. Technol. Mag.*, vol. 14, no. 3, pp. 28â€“41, Sep. 2019.

[6] M. Z. Chowdhury *et al.*, "Optical Wireless Hybrid Networks for 5G and Beyond Communicationsâ€”A Survey," *IEEE Commun. Surveys Tuts.*, vol. 22, no. 2, pp. 1090â€“1121, Secondquarter 2020.

[7] H. Haas, "LiFi is a Paradigm-Shifting 5G Technology," *Reviews in Physics*, vol. 3, pp. 26â€“31, 2018.

[8] M. A. Khalighi and M. Uysal, "Survey on Free Space Optical Communication: A Communication Theory Perspective," *IEEE Commun. Surveys Tuts.*, vol. 16, no. 4, pp. 2231â€“2258, Fourthquarter 2014.

[9] F. Liu *et al.*, "Integrated Sensing and Communication: Towards Dual-Functional Wireless Networks for 6G," *IEEE Commun. Surveys Tuts.*, vol. 24, no. 3, pp. 1726â€“1767, Thirdquarter 2022.

[10] A. Liu *et al.*, "A Survey on Fundamental Limits of Integrated Sensing and Communication," *IEEE Commun. Surveys Tuts.*, vol. 24, no. 2, pp. 994â€“1034, Secondquarter 2022.

[11] Y. Zhuang *et al.*, "A Survey of Positioning Systems Using Visible LED Lights," *IEEE Commun. Surveys Tuts.*, vol. 20, no. 3, pp. 1963â€“1988, Thirdquarter 2018.

[12] X. Bao and L. Chen, "Recent Progress in Distributed Fiber Optic Sensors," *Sensors*, vol. 12, no. 7, pp. 8601â€“8639, 2012.

[13] M. A. Esmail, H. Fathallah, and M.-S. Alouini, "A Survey on the Impact of Rain and Fog on Free Space Optical Communication," *IEEE Commun. Surveys Tuts.*, vol. 19, no. 2, pp. 1194â€“1222, Secondquarter 2017.

[14] M. J. Page *et al.*, "The PRISMA 2020 Statement: An Updated Guideline for Reporting Systematic Reviews," *BMJ*, vol. 372, p. n71, Mar. 2021.

---

*Note: Corpus paper identifiers [O_ISAC_XXX] refer to studies in the systematic review database. Full bibliographic details are provided in the Supplementary Material.*
\n\n## drafts/section_02A_fundamentals.md\n\n# II. TECHNICAL FUNDAMENTALS OF O-ISAC

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

Evidence alignment: Representative works explicitly report OSNR in the optical plane (e.g., "optical signal-to-noise ratio (O-SNR)/(OSNR)") [O_ISAC_056], [O_ISAC_080]. <!-- evidence: ⟦O_ISAC_056 | # Optical ISAC: Fundamental Performance Limits and Transceiver Design | L7-L11 | strength_final=strong | plane_final=OPTICAL_PLANE⟧; ⟦O_ISAC_080 | # Integrated Communication and In-band Spectrum Polarization-Based Sensing via Fraction-Division Non-Orthogonal Multiple Access | L5-L9 | strength_final=strong | plane_final=OPTICAL_PLANE⟧ -->
Electrical SNR is explicitly reported as a post-detection (electrical) quantity for communication performance [O_ISAC_061], [O_ISAC_023]. <!-- evidence: ⟦O_ISAC_061 | # *A. Convergence of BCD Algorithm* > #### *B. Optimal Beampattern and C&S Tradeoff* > #### <span id="page-11-3"></span>*C. Practical C&S Performance Metrics* | L638-L642 | strength_final=strong | plane_final=ELECTRICAL_PLANE⟧; ⟦O_ISAC_023 | # Free-Space Optical Integrated Sensing and Communication Based on DCO-OFDM: Performance Metrics and Resource Allocation > ## *C. Computational Complexity and Scalability* > ### <span id="page-11-1"></span><span id="page-11-0"></span>D. Robustness to Channel Variations | L751-L755 | strength_final=strong | plane_final=ELECTRICAL_PLANE⟧ -->

### A.2 Integration Paradigms (Communication-centric / Sensing-centric / Joint Design)
Design rationale: To avoid modality-locked taxonomies, we classify integration by mechanisms: shared waveform, shared hardware, shared time/frequency resources, and shared processing. This mechanism-first view aligns heterogeneous implementations under a single abstraction while keeping the physical constraints of each modality intact.

**Communication-centric:** The primary objective is communication performance while sensing is constrained to operate within communication-driven resource limits. A minimal objective-form exemplar is: maximize \(R\) subject to \(J_{\text{sense}}(\boldsymbol{\theta})\le \varepsilon\).

**Sensing-centric:** The primary objective is sensing fidelity while communication is constrained to meet a minimum service level. A minimal objective-form exemplar is: minimize \(J_{\text{sense}}(\boldsymbol{\theta})\) subject to \(R\ge R_0\) (and/or BER \(\le \beta\)).

**Joint design:** Communication and sensing are co-optimized via explicit multi-objective trade-offs with an operating-point interpretation. A minimal objective-form exemplar is: minimize \([J_{\text{sense}}(\boldsymbol{\theta}),\; -R]\) (Pareto) or minimize \(\alpha J_{\text{sense}}(\boldsymbol{\theta})-(1-\alpha)R\), where \(R\) denotes throughput and \(J_{\text{sense}}\) denotes a sensing loss (e.g., estimation MSE or a ranging-error proxy).

Paradigm-to-mechanism bridge:
- Communication-centric -> shared processing / shared resources -> sensing piggybacks on communication signaling.
- Sensing-centric -> shared waveform / shared hardware -> communication is embedded under sensing-driven constraints.
- Joint design -> shared waveform + shared processing -> explicit co-optimization couples both objectives.

We define an integration depth variable
\[
d_{\text{int}}\in\{0,\;1/2,\;1\},
\]
where \(d_{\text{int}}=0\) corresponds to coexistence, \(d_{\text{int}}=1/2\) to partial sharing/cooperation, and \(d_{\text{int}}=1\) to full co-design. This abstraction provides the axis used later to align taxonomy and trade-off synthesis without rewriting modality-specific models.

Evidence alignment: A.2 introduces a survey-internal taxonomy for organizing later sections; no paper-specific performance claims are asserted here, and thus no additional evidence anchors are required.

**Lesson (A):** A unified system model combined with explicit measurement-plane mapping is necessary to make later taxonomy and trade-off statements falsifiable rather than narrative.
\n\n## drafts/section_02B_channel_models.md\n\n## B. Propagation and Channel Models Across Modalities
This subsection abstracts each modality's propagation as an operator/channel mapping consistent with the observation models in Section II-A, while emphasizing that dominant impairments differ across media. The measurement-plane contract remains binding: channel modeling does not justify OSNR-to-SNR conversion, and plane separation is preserved throughout (Metric Governance).

### B.1 Fiber Channel (Guided Medium)
Design rationale: A guided fiber link is well captured by a linear dispersive baseband model for coherent communication, with a nonlinear wave equation as a conceptual extension when power or length scales demand it. This separation provides a minimal, modality-consistent abstraction while allowing later sections to specialize the impairment regime.

A linear dispersive baseline is
\[
\mathbf{y}(t)=\mathbf{G}_{\text{disp}}(t)\ast \mathbf{s}(t)+\mathbf{w}(t),
\]
where \(\mathbf{s}(t)\) is the transmitted baseband signal, \(\mathbf{G}_{\text{disp}}(t)\) is the dispersive impulse response, and \(\mathbf{w}(t)\) is additive noise. As a conceptual extension, the nonlinear Schrodinger equation (NLSE) captures loss, dispersion, and Kerr nonlinearity:
\[
\frac{\partial A(z,t)}{\partial z}= -\frac{\alpha}{2}A - j\frac{\beta_2}{2}\frac{\partial^2 A}{\partial t^2} + j\gamma|A|^2A + \eta(z,t),
\]
where \(A(z,t)\) is the optical field envelope, \(\alpha\) is attenuation, \(\beta_2\) is group-velocity dispersion, and \(\gamma\) is the nonlinear coefficient. For sensing, the effective channel is the distributed backscatter/impulse response along the fiber, whereas the communication view typically emphasizes the forward transmission path. Fiber sensing spatial granularity is reported as \(\Delta z\) (gauge/segment length), not \(\Delta r_{\min}\) (Metric Governance).

Evidence alignment: This subsection presents theory-standard channel abstractions and does not assert paper-specific modeling choices; hence no evidence anchors are invoked here.

### B.2 FSO Channel (Atmosphere + Pointing)
Design rationale: Free-space optical channels are dominated by multiplicative impairments (turbulence and pointing) and path attenuation, which are naturally expressed in an IM/DD-friendly intensity model. This abstraction keeps the optical nonnegativity constraint explicit while isolating the dominant propagation factors.

A compact IM/DD-friendly form is
\[
y = h_{\text{turb}}\,h_{\text{point}}\,x + n,\qquad x\ge 0,
\]
where \(x\) is the transmitted optical intensity, \(h_{\text{turb}}\) captures turbulence-induced fading, \(h_{\text{point}}\) captures pointing/misalignment loss, and \(n\) is additive noise. A standard attenuation factor is the Beer-Lambert law,
\[
h_{\text{att}}=\exp(-\kappa d),
\]
with \(\kappa\) as the extinction coefficient and \(d\) the propagation distance. Turbulence statistics are commonly represented by lognormal or Gamma-Gamma distributions as theory-standard options.

Evidence alignment: Representative FSO works compute atmospheric loss using Beer-Lambert attenuation in their channel modeling and simulation setup [O_ISAC_035], [O_ISAC_034]. <!-- evidence: ⟦O_ISAC_035 | ### II. SYSTEM MODEL AND METHODOLOGY > # B. FSO Channel | L75-L79 | strength_final=strong | claim_tag=attenuation_beer_lambert | context-verified=YES⟧; ⟦O_ISAC_034 | # IV. NUMERICAL RESULTS | L205-L205 | strength_final=strong | claim_tag=attenuation_beer_lambert | context-verified=YES⟧ -->

### B.3 VLC Channel (Lambertian + Multipath + Ambient Light)
Design rationale: VLC channels are geometry-driven and are naturally modeled by Lambertian emission with an intensity impulse response that captures both direct and reflected paths. This abstraction preserves IM/DD constraints while enabling later sections to compare sensing and communication performance under common channel primitives.

A compact representation uses an intensity impulse response \(h(t)\) with a Lambertian DC gain for the LoS path, while NLoS reflections are captured by additional impulse-response components. Multipath/NLoS effects are thus expressed through \(h(t)\) rather than an equivalent complex baseband model. Shot noise, thermal noise, and ambient-light-induced noise are standard components in VLC receiver models.

Evidence alignment: Representative VLC/OWC works model the channel impulse response as a sum of LOS and NLOS components, explicitly framing multipath via LoS/NLoS impulse-response components [O_ISAC_022], [O_ISAC_039]. <!-- evidence: ⟦O_ISAC_022 | ## <span id="page-3-0"></span>D. The Optical Wireless Channel | L136-L136 | strength_final=strong | claim_tag=multipath_nlos_impulse_response | context-verified=YES⟧; ⟦O_ISAC_039 | # 2 VISIBLE LIGHT INTEGRATED POSITIONING AND COMMUNICATION FRAMEWORK > ## 2.1 System Model of Indoor Visible Light Positioning and Communication | L67-L71 | strength_final=strong | claim_tag=multipath_nlos_impulse_response | context-verified=YES⟧ -->

### B.4 Photonic-THz Bridging (Optical Generation/Distribution + THz Propagation)
Design rationale: Photonic-THz links are hybrid by construction: optical carriers are used for signal generation, distribution, and local-oscillator delivery, while the wireless propagation occurs in the THz band. A split-channel abstraction therefore cleanly separates optical-domain impairments from THz wireless propagation effects.

We treat the link as an optical generation/distribution stage feeding a THz wireless channel, which enables consistent modeling of end-to-end performance without conflating measurement planes. In representative photonic-THz links, laser-induced phase noise and frequency offset are treated as dominant impairments that shape performance and system design choices.

Evidence alignment: Photonic-THz works explicitly discuss laser-induced phase noise and frequency-offset effects in their experimental or system-performance analyses [O_ISAC_044], [O_ISAC_077]. <!-- evidence: ⟦O_ISAC_044 | #### I. INTRODUCTION | L41-L41 | strength_final=strong | claim_tag=phase_noise_freq_offset | context-verified=YES⟧; ⟦O_ISAC_077 | ### III. PHOTONIC THZ ISAC LINK > #### A. Experimental Setup | L58-L58 | strength_final=strong | claim_tag=phase_noise_freq_offset | context-verified=YES⟧ -->

**Lesson (B):** Channel models differ in dominant impairments, but the reporting contract and measurement-plane separation remain invariant across modalities.
\n\n## drafts/section_02C_transceiver_hardware.md\n\n## C. Transceiver and Hardware Abstractions (What is Common, What is Modality-Specific)

### C.1 Sources and Modulators
Design rationale: Transceiver abstraction begins at the optical source and modulation interface, because these elements determine whether the system operates coherently or under IM/DD constraints and set the effective bandwidth and waveform interface used by sensing/communication co-design. A compact source–modulator view also supports cross-modality comparison without over-committing to device-specific implementations.

Evidence alignment: Representative photonic-THz hardware chains explicitly modulate external cavity laser (ECL) light using an IQ modulator composed of MZMs, reflecting a coherent source–modulator stack [O_ISAC_029]. <!-- evidence: ⟦O_ISAC_029 | # THz Integrated Sensing and Communication With Full-Photonic Direct LFM Reception and De-Chirping for D-Band Fiber-Wireless Network > ### <span id="page-2-2"></span>II. PRINCIPLE | L100-L100 | strength_final=strong | plane_final=OPTICAL_PLANE | context-verified=YES⟧ -->
In contrast, IM/DD-oriented VLC transmitter chains can be realized by adding a DC bias to an electrical waveform and using it to modulate a laser diode (LD), which enforces a nonnegative optical intensity interface [O_ISAC_001]. <!-- evidence: ⟦O_ISAC_001 | # Modulation Strategies for Robust Optical Wireless Communications and Sensing in 6G > #### II. VLC SYSTEM EMPLOYING CE-OFDM > #### A. VLC CE-OFDM Transmitter | L70-L70 | strength_final=strong | plane_final=OPTICAL_PLANE | context-verified=YES⟧ -->

### C.2 Receivers and Detection
Design rationale: Receiver architecture determines the measurement plane and, therefore, which signal-quality metrics are meaningful. Coherent receivers with an optical LO recover complex field information, whereas IM/DD receivers implement square-law detection and operate on optical intensity, mapping observations to the electrical plane.

We restate the measurement-plane contract for receiver design: 
\[
\pi(m)\in\{\text{OPTICAL\_PLANE},\;\text{ELECTRICAL\_PLANE},\;\text{AMBIGUOUS}\},
\]
where OSNR is an optical-plane metric and electrical SNR/ESNR is a post-detection electrical-plane metric; OSNR-to-SNR conversion is prohibited without an explicit receiver model, and generic “SNR” without plane cues remains AMBIGUOUS (Metric Governance). At the receiver interface, ranging metrics reflect bandwidth-limited sensing tasks via \(\Delta r_{\min}=v/(2B_{\text{eff}})\), whereas fiber systems report spatial granularity via \(\Delta z\) (gauge/segment length), not \(\Delta r_{\min}\) (Metric Governance).

Evidence alignment: Representative optical-plane reporting explicitly uses OSNR (optical signal-to-noise ratio) [O_ISAC_028], [O_ISAC_029]. <!-- evidence: ⟦O_ISAC_028 | # Performance Improvement for Symmetric Carrierassisted Differential Detection Receiver by Pairwise Coding | L11-L11 | strength_final=strong | plane_final=OPTICAL_PLANE | context-verified=YES⟧; ⟦O_ISAC_029 | # THz Integrated Sensing and Communication With Full-Photonic Direct LFM Reception and De-Chirping for D-Band Fiber-Wireless Network > ## <span id="page-0-1"></span>I. INTRODUCTION | L47-L47 | strength_final=strong | plane_final=OPTICAL_PLANE | context-verified=YES⟧ -->
Electrical SNR is explicitly reported in post-detection performance analysis [O_ISAC_061], [O_ISAC_023], consistent with the electrical-plane interpretation of IM/DD receivers. <!-- evidence: ⟦O_ISAC_061 | # *A. Convergence of BCD Algorithm* > #### *B. Optimal Beampattern and C&S Tradeoff* > #### <span id="page-11-3"></span>*C. Practical C&S Performance Metrics* | L638-L642 | strength_final=strong | plane_final=ELECTRICAL_PLANE | context-verified=YES⟧; ⟦O_ISAC_023 | # Free-Space Optical Integrated Sensing and Communication Based on DCO-OFDM: Performance Metrics and Resource Allocation > ## *C. Computational Complexity and Scalability* > ### <span id="page-11-1"></span><span id="page-11-0"></span>D. Robustness to Channel Variations | L751-L755 | strength_final=strong | plane_final=ELECTRICAL_PLANE | context-verified=YES⟧ -->
Hardware-level receiver implementations in photonic-THz systems explicitly describe PD/BPD-based O/E conversion after photonic down-conversion [O_ISAC_029], while VLC receivers detect optical signals with a photodiode and convert them to electrical waveforms [O_ISAC_001]. <!-- evidence: ⟦O_ISAC_029 | # THz Integrated Sensing and Communication With Full-Photonic Direct LFM Reception and De-Chirping for D-Band Fiber-Wireless Network > ### <span id="page-2-2"></span>II. PRINCIPLE | L157-L157 | strength_final=strong | plane_final=ELECTRICAL_PLANE | context-verified=YES⟧; ⟦O_ISAC_001 | # Modulation Strategies for Robust Optical Wireless Communications and Sensing in 6G > ## B. VLC CE-OFDM Receiver | L74-L74 | strength_final=strong | plane_final=ELECTRICAL_PLANE | context-verified=YES⟧ -->

### C.3 Beamforming/Wavefront Control Enablers
Design rationale: Spatial control elements (e.g., OPA, optical RIS/metasurfaces, and integrated photonics) are treated as front-end enablers that shape beam directionality and angular sensitivity while remaining compatible with the source–modulator–channel–detector abstraction. A generic array response for angle sensing/beam steering can be written as
\[
\mathbf{a}(\phi)=\left[1,\;e^{j k d \sin\phi},\;\ldots,\;e^{j k d (N-1)\sin\phi}\right]^{\top}.
\]

Evidence alignment: This subsection provides theory-standard enabler abstractions; the current II-C evidence layer does not include dedicated, context-verified anchors for OPA/optical-RIS usage, so no paper-specific adoption claims are asserted here.

**Lesson (C):** Hardware commonality exists at the abstraction level (source–modulator–channel–detector), not at the implementation level.
\n\n
