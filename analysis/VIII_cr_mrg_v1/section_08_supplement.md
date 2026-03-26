# Section VIII Supplement

## Overview supplement

# VIII Overview Supplement (Source-Text Validation)

## Verbatim Excerpts (<=25 words each)
- Cite key: `O_ISAC_220`
  - Excerpt: "standardized in 2018 by a joint task force including ITU"
  - Locator: `data/proc_markdowns/O_ISAC_220/O_ISAC_220.md`, HeadingPath: `Advanced SMART network: empowering subsea monitoring with dense photonic integrated sensing and communication > 1. INTRODUCTION`, line 19

- Cite key: `O_ISAC_035`
  - Excerpt: "we propose an OCDM-based multi-carrier modulation strategy exploiting the Fresnel transform to enhance the capacity"
  - Locator: `data/proc_markdowns/O_ISAC_035/O_ISAC_035.md`, HeadingPath: `OCDM-Based FMCW Waveform Design for FSO Integrated Sensing and Communications > I. INTRODUCTION`, line 52

- Cite key: `O_ISAC_115`
  - Excerpt: "The channel modeling approaches, requirements, and challenges for communication cases and sensing cases are summarized and discussed."
  - Locator: `data/proc_markdowns/O_ISAC_115/O_ISAC_115/O_ISAC_115.md`, HeadingPath: `Integrated Sensing and Communication in 6G: the Deterministic Channel Models for THz Imaging`, line 9

- Cite key: `O_ISAC_202`
  - Excerpt: "this approach reveals the presence of a transmission link, potentially drawing the unwanted attention of an attacker."
  - Locator: `data/proc_markdowns/O_ISAC_202/O_ISAC_202.md`, HeadingPath: `Integrated optical covert sensing and communication > 1. Introduction`, line 23

- Cite key: `O_ISAC_163`
  - Excerpt: "for a practical RIS implementation and the eventual roll-out, it is necessary to address all of them at once."
  - Locator: `data/proc_markdowns/O_ISAC_163/O_ISAC_163.md`, HeadingPath: `II. BACKGROUND AND STUDY > E. Contributions of This Survey`, line 90

## VIII-artefact evidence
- Axis-2 domain list source:
  - `analysis/VIII_ev_v1/axis_definitions.md:4`
  - "Axis-2 Challenge domains: standardization_interoperability, hardware_scalability_efficiency, channel_modeling_evaluation, security_privacy_reliability, deployment_convergence_roadmap."

- INDIRECT bridge policy source:
  - `analysis/VIII_ev_v1/mapping_rules.md:4`
  - "Upstream bridge rows (Section5/6/7) are INDIRECT by design and cannot replace DIRECT textual evidence."

- Contract-violations summary line:
  - `analysis/VIII_ev_v1/contract_violations.csv` has 242 rows; category=`EVIDENCE_WEAK` (242), severity=`MINOR` (242).

## VIII-A supplement

# VIII-A Consolidated Supplement (Deduplicated)

Deduplication policy: identical entries were merged when `cite key + excerpt + locator` matched exactly. Source coverage is retained via `used_in` tags.

## Context and Cases 1-2 Evidence

1) **Cite key:** `O_ISAC_220`
- **Excerpt:** "standardized in 2018 by a joint task force including ITU"
- **Locator:** `data/proc_markdowns/O_ISAC_220/O_ISAC_220.md`, `1. INTRODUCTION`, line 19
- **used_in:** `CONTEXT`, `CASE1`

2) **Cite key:** `O_ISAC_220`
- **Excerpt:** "SMART network, proposed and standardized in 2018 by a joint task force including ITU"
- **Locator:** `data/proc_markdowns/O_ISAC_220/O_ISAC_220.md`, `1. INTRODUCTION`, line 19
- **used_in:** `MATH_ANCHOR`

3) **Cite key:** `O_ISAC_025`
- **Excerpt:** "exploits an optoelectronic transport network interconnecting the RAN with the core functions located at the MEC."
- **Locator:** `data/proc_markdowns/O_ISAC_025/O_ISAC_025/O_ISAC_025.md`, `2. System Architecture`, line 23
- **used_in:** `CONTEXT`

4) **Cite key:** `O_ISAC_025`
- **Excerpt:** "interconnecting the RAN with the core functions located at the MEC"
- **Locator:** `data/proc_markdowns/O_ISAC_025/O_ISAC_025/O_ISAC_025.md`, `2. System Architecture`, line 23
- **used_in:** `CASE2`

5) **Cite key:** `O_ISAC_025`
- **Excerpt:** "minimize the number of network links used by identifying the optimal routing and network capacity allocation policies"
- **Locator:** `data/proc_markdowns/O_ISAC_025/O_ISAC_025/O_ISAC_025.md`, `3. ISAC based transport network optimization`, line 41
- **used_in:** `CASE2`

6) **Cite key:** `O_ISAC_161`
- **Excerpt:** "industry interest in ISAC has intensified, as demonstrated by emerging standardization efforts and the development of commercial prototypes"
- **Locator:** `data/proc_markdowns/O_ISAC_161/O_ISAC_161.md`, `Integrated Sensing and Communication (ISAC) Transceiver: Hardware Architectures, Enabling Technologies, and Emerging Trends`, line 45
- **used_in:** `CONTEXT`

7) **Cite key:** `O_ISAC_161`
- **Excerpt:** "industry interest in ISAC has intensified, as demonstrated by emerging standardization efforts"
- **Locator:** `data/proc_markdowns/O_ISAC_161/O_ISAC_161.md`, `Integrated Sensing and Communication (ISAC) Transceiver: Hardware Architectures, Enabling Technologies, and Emerging Trends`, line 45
- **used_in:** `CASE1`

## Cases 3-4 and Math-Anchor Evidence

8) **Cite key:** `O_ISAC_104`
- **Excerpt:** "standard PONs are built on a Point-to-Multipoint (PtMP) architecture: this peculiar structure is a real challenge"
- **Locator:** `data/proc_markdowns/O_ISAC_104/O_ISAC_104/O_ISAC_104.md`, `I. INTRODUCTION`, line 53
- **used_in:** `CASE3`

9) **Cite key:** `O_ISAC_104`
- **Excerpt:** "the high link budget loss caused by the typical splitting ratio at the remote node (RN) can lead to sensing failure."
- **Locator:** `data/proc_markdowns/O_ISAC_104/O_ISAC_104/O_ISAC_104.md`, `I. INTRODUCTION`, line 53
- **used_in:** `CASE3`

10) **Cite key:** `O_ISAC_104`
- **Excerpt:** "The already deployed PONs show useful capabilities to be exploited for sensing, even presenting some challenges for the usual fiber sensors"
- **Locator:** `data/proc_markdowns/O_ISAC_104/O_ISAC_104/O_ISAC_104.md`, `III. CONCLUSIONS`, line 79
- **used_in:** `CASE3`

11) **Cite key:** `O_ISAC_104`
- **Excerpt:** "conventional sensing methods based on fiber backscattering, struggle with the simultaneous and unambiguous interrogation of all drop fibers."
- **Locator:** `data/proc_markdowns/O_ISAC_104/O_ISAC_104/O_ISAC_104.md`, `I. INTRODUCTION`, line 53
- **used_in:** `MATH_ANCHOR`

12) **Cite key:** `O_ISAC_104`
- **Excerpt:** "the PON must operate with the different standards in terms of spectral occupancy."
- **Locator:** `data/proc_markdowns/O_ISAC_104/O_ISAC_104/O_ISAC_104.md`, `I. INTRODUCTION`, line 53
- **used_in:** `MATH_ANCHOR`

13) **Cite key:** `O_ISAC_220`
- **Excerpt:** "there is the main challenge in the SMART configuration to precisely allocate the sensing information into the frequency blanks of communication signals"
- **Locator:** `data/proc_markdowns/O_ISAC_220/O_ISAC_220.md`, `1. INTRODUCTION`, line 23
- **used_in:** `CASE4`

14) **Cite key:** `O_ISAC_220`
- **Excerpt:** "main challenge in the SMART configuration to precisely allocate the sensing information into the frequency blanks of communication signals"
- **Locator:** `data/proc_markdowns/O_ISAC_220/O_ISAC_220.md`, `1. INTRODUCTION`, line 23
- **used_in:** `MATH_ANCHOR`

15) **Cite key:** `O_ISAC_220`
- **Excerpt:** "the special design of the sensing transmission format is made to enable the compatible DSP with DSCM communications"
- **Locator:** `data/proc_markdowns/O_ISAC_220/O_ISAC_220.md`, abstract block, line 9
- **used_in:** `CASE4`, `MATH_ANCHOR`

16) **Cite key:** `O_ISAC_220`
- **Excerpt:** "the perfect compatibility is also exhibited using communication-compatible DSP to process the sensing information."
- **Locator:** `data/proc_markdowns/O_ISAC_220/O_ISAC_220.md`, `5. CONCLUSION`, line 184
- **used_in:** `CASE4`

17) **Cite key:** `O_ISAC_220`
- **Excerpt:** "uses different wavelength bands for sensing data transmissions, wastes WDM channel resources and reduces the spectral efficiency of optical communications."
- **Locator:** `data/proc_markdowns/O_ISAC_220/O_ISAC_220.md`, `1. INTRODUCTION`, line 21
- **used_in:** `MATH_ANCHOR`

## VIII-B supplement

# VIII-B Merged Supporting Excerpts

## Deduplicated Excerpts (Context + Challenges + Math Support)

| cite_key | excerpt | locator | source_blocks |
|---|---|---|---|
| O_ISAC_035 | "enabling reduced RF hardware complexity and a simplified FMCW receiver design." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_035\O_ISAC_035.md :: OCDM-Based FMCW Waveform Design for FSO Integrated Sensing and Communications > I. INTRODUCTION :: L44-L44 | VIII-B_CHALLENGES_12_supp; VIII-B_CONTEXT_supp |
| O_ISAC_093 | "Edge devices typically have limited energy budgets, often below 1 watt for small IoT sensors" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_093\O_ISAC_093.md :: IV. CHALLENGES :: L158-L158 | VIII-B_CHALLENGES_12_supp |
| O_ISAC_093 | "Edge devices typically have limited energy budgets, often below 1 watt for small IoT sensors, and processing delays can exceed 50 milliseconds" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_093\O_ISAC_093.md :: III. LLMs > IV. CHALLENGES :: L158-L158 | VIII-B_CONTEXT_supp |
| O_ISAC_093 | "processing delays can exceed 50 milliseconds for complex LLM tasks, significantly hindering real-time performance." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_093\O_ISAC_093.md :: IV. CHALLENGES :: L158-L158 | VIII-B_CHALLENGES_12_supp |
| O_ISAC_095 | "the four sidebands originate from a shared laser, so FOE algorithms are not required." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_095\O_ISAC_095\O_ISAC_095.md :: I. INTRODUCTION :: L53-L53 | VIII-B_CHALLENGES_12_supp |
| O_ISAC_095 | "thereby reducing the complexity and power consumption of the DSP at the UE." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_095\O_ISAC_095\O_ISAC_095.md :: II. NETWORK ARCHITECTURE AND PRINCIPLE :: L108-L108 | VIII-B_CHALLENGES_12_supp |
| O_ISAC_112 | "results in an increased computational complexity for a single IRS unit during the localization phase" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_112\O_ISAC_112\O_ISAC_112.md :: IV. OPTICAL IRS-AIDED LOCALIZATION ALGORITHM > C. Complexity Analysis :: L371-L371 | VIII-B_CHALLENGES_12_supp |
| O_ISAC_134 | "The hidden problem is the large communication overhead associated with the beamforming in cells with many highly mobile users." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_134\O_ISAC_134\O_ISAC_134.md :: ABSTRACT :: L21-L21 | VIII-B_CHALLENGES_34_TAKEAWAYS_supp |
| O_ISAC_134 | "the last stage involving the MMT dominates the overall complexity." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_134\O_ISAC_134\O_ISAC_134.md :: V. NUMERICAL RESULTS > D. LATENCY AND DATASET SIZE :: L549-L549 | VIII-B_CHALLENGES_34_TAKEAWAYS_supp |
| O_ISAC_134 | "The overall average data processing latency of 8.3 ms was obtained." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_134\O_ISAC_134\O_ISAC_134.md :: V. NUMERICAL RESULTS > D. LATENCY AND DATASET SIZE :: L541-L541 | VIII-B_CHALLENGES_34_TAKEAWAYS_supp |
| O_ISAC_142 | "the high mobility of LEO satellites and the severe path loss pose challenges on antenna technologies" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_142\O_ISAC_142\O_ISAC_142.md :: III. A D V A N C E D I S A R C H I T E C T U R E S > C. Holographic ISs > 1) LEO satellite communications :: L645-L645 | VIII-B_CHALLENGES_34_TAKEAWAYS_supp |
| O_ISAC_161 | "Numerous architectural and electrical parameter choices involve trade-offs that must be carefully balanced during development." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_161\O_ISAC_161.md :: FUNDAMENTALS AND DEFINITIONS :: L121-L121 | VIII-B_CHALLENGES_34_TAKEAWAYS_supp |
| O_ISAC_161 | "optimize performance for both sensing and communication operations is highly challenging" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_161\O_ISAC_161.md :: FUNDAMENTALS AND DEFINITIONS :: L121-L121 | VIII-B_CHALLENGES_34_TAKEAWAYS_supp |
| O_ISAC_162 | "In summary, while reusing OFDM signals for ISAC can be efficient, it may introduce extra baseband costs due to increased processing complexity" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_162\O_ISAC_162.md :: A Unified Future: Integrated Sensing and Communication (ISAC) in 6G > Waveform Design and Baseband Complexity :: L328-L328 | VIII-B_CONTEXT_supp |
| O_ISAC_162 | "it may introduce extra baseband costs due to increased processing complexity" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_162\O_ISAC_162.md :: LB, WAVEFORM DESIGN, BEAMFORMING ASPECTS, AND HARDWARE ISSUES FOR ISAC > Waveform Design and Baseband Complexity :: L328-L328 | VIII-B_CHALLENGES_34_TAKEAWAYS_supp |
| O_ISAC_162 | "temperature-induced effects on the analogue frontends of the RUs which are not fully compensated" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_162\O_ISAC_162.md :: LB, WAVEFORM DESIGN, BEAMFORMING ASPECTS, AND HARDWARE ISSUES FOR ISAC > POC SYSTEMS :: L358-L358 | VIII-B_CHALLENGES_34_TAKEAWAYS_supp |
| O_ISAC_171 | "16 Hz frequency adjustment for a 0.1° beam steering, can also be easily achieved by modifying the microwave source frequency." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_171\O_ISAC_171.md :: Principle of frequency-comb-steered linear quasi-TTD beamformer > Seamless squint-free beamforming of ultra-wideband LFM signals :: L108-L108 | VIII-B_CONTEXT_supp |
| O_ISAC_171 | "Large-scale antenna arrays can thus be supported without a significant increase in hardware complexity." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_171\O_ISAC_171.md :: Discussion :: L158-L158 | VIII-B_CHALLENGES_34_TAKEAWAYS_supp |
| O_ISAC_171 | "This straightforward tunability, coupled with ultra-high resolution, greatly reduces the complexity of the beam control system." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_171\O_ISAC_171.md :: Results > Seamless squint-free beamforming of ultra-wideband LFM signals :: L108-L108 | VIII-B_CHALLENGES_34_TAKEAWAYS_supp |
| O_ISAC_237 | "a common communication receiver does not have the transmitted analogue FMCW signal and the required hardware." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_237\O_ISAC_237.md :: III. BISTATIC SENSING WITH THE SUPERPOSED FMCW > B. DMD Sensing Algorithm :: L188-L188 | VIII-B_CHALLENGES_12_supp |
| O_ISAC_237 | "operating these systems independently leads to increased hardware complexity, cost, and inefficient spectrum usage." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_237\O_ISAC_237.md :: I. INTRODUCTION :: L11-L11 | VIII-B_CHALLENGES_12_supp |
| O_ISAC_237 | "we provide a complexity analysis of the sensing-aided channel estimation, the interference cancellation, the FCCR sensing, and the DMD algorithm." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_237\O_ISAC_237.md :: IV. SENSING-AIDED CHANNEL ESTIMATION AND INTERFERENCE CANCELLATION > E. The computational complexity :: L351-L351 | VIII-B_CHALLENGES_12_supp |

## Math-Anchor Term Support Labels (Preserved)

| label | cite_key | excerpt | locator |
|---|---|---|---|
| supports `s_shared` (shared transceiver context) | O_ISAC_161 | "By unifying sensing and communication functions within a shared transceiver framework" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_161\O_ISAC_161.md :: ABSTRACT :: L17-L17 |
| supports `C_hw` (compute/architecture complexity) | O_ISAC_161 | "Numerous architectural and electrical parameter choices involve trade-offs that must be carefully balanced during development." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_161\O_ISAC_161.md :: FUNDAMENTALS AND DEFINITIONS :: L121-L121 |
| supports `L_hw` (latency constraint) | O_ISAC_134 | "The overall average data processing latency of 8.3 ms was obtained." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_134\O_ISAC_134\O_ISAC_134.md :: V. NUMERICAL RESULTS > D. LATENCY AND DATASET SIZE :: L541-L541 |
| supports `P_hw` (power/energy constraint) | O_ISAC_161 | "Energy consumption is a critical constraint for ISAC hardware, especially in battery-powered or energy-harvesting applications" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_161\O_ISAC_161.md :: CHALLENGES AND FUTURE RESEARCH DIRECTIONS > Energy Efficiency :: L602-L602 |
| supports `O_ctrl` (beam-control overhead) | O_ISAC_134 | "The hidden problem is the large communication overhead associated with the beamforming in cells with many highly mobile users." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_134\O_ISAC_134\O_ISAC_134.md :: ABSTRACT :: L21-L21 |
| supports `s_array` and scalable steering control context | O_ISAC_171 | "This straightforward tunability, coupled with ultra-high resolution, greatly reduces the complexity of the beam control system." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_171\O_ISAC_171.md :: Results > Seamless squint-free beamforming of ultra-wideband LFM signals :: L108-L108 |
| supports `U_comm` (comm-plane utility) | O_ISAC_134 | "These results translate directly into improved beamforming and communication efficiency." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_134\O_ISAC_134\O_ISAC_134.md :: ABSTRACT :: L21-L21 |
| supports `U_sens` (sensing-plane utility) | O_ISAC_171 | "demonstrate integrated sensing and communication capabilities, including inverse synthetic aperture radar imaging" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_171\O_ISAC_171.md :: ABSTRACT :: L15-L15 |

## VIII-C supplement

# VIII-C Merged Supporting Excerpts

## Deduplicated Excerpts (Context + Challenges + Math Support)

| label | cite_key | excerpt | locator | source_blocks |
|---|---|---|---|---|
| kappa_cond | O_ISAC_005 | "adverse weather can significantly reduce FSO link reliability due to atmospheric attenuation." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_005\O_ISAC_005.md :: *Abstract* :: L5-L5 | VIII-C_CONTEXT_supp; VIII-C_CHALLENGES_12_supp; VIII-C_MATH_ANCHOR_supp |
| gamma_geom | O_ISAC_005 | "for a UAV positioned along its circular trajectory" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_005\O_ISAC_005.md :: II. SYSTEM MODEL > A. FSO Backhaul Communication :: L52-L52 | VIII-C_MATH_ANCHOR_supp |
| mu_metric_comm_plane | O_ISAC_381 | "The BER was used to evaluate the channel capacity" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_381\O_ISAC_381.md :: 3.2. Data Transmission Performance :: L151-L151 | VIII-C_CONTEXT_supp; VIII-C_CHALLENGES_34_TAKEAWAYS_supp; VIII-C_MATH_ANCHOR_supp |
| mu_metric_comm_plane | O_ISAC_381 | "the BER performance and the data transmission rate with the data transmission distance are evaluated." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_381\O_ISAC_381.md :: 3.2. Data Transmission Performance :: L157-L157 | VIII-C_CHALLENGES_34_TAKEAWAYS_supp; VIII-C_MATH_ANCHOR_supp |
| delta_prov | O_ISAC_327 | "a comprehensive review of optical wireless communications channel measurement campaigns and channel models is given." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_327\O_ISAC_327.md :: I. INTRODUCTION > D. Related Surveys :: L59-L59 | VIII-C_CONTEXT_supp; VIII-C_CHALLENGES_34_TAKEAWAYS_supp; VIII-C_MATH_ANCHOR_supp |
| delta_prov | O_ISAC_327 | "a standard VLC channel model is needed, which follows the modeling framework in ITU M. 2412." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_327\O_ISAC_327.md :: II. VLC CHANNEL MODELING METHODS > C. Summary and Prospects :: L198-L198 | VIII-C_CHALLENGES_34_TAKEAWAYS_supp; VIII-C_MATH_ANCHOR_supp |
| - | O_ISAC_050 | "An OFDM-based equivalent discrete channel remodeling method is proposed to decouple LOS and NLOS paths" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_050\O_ISAC_050.md :: I. INTRODUCTION > B. Contributions :: L43-L43 | VIII-C_CONTEXT_supp; VIII-C_CHALLENGES_12_supp |
| - | O_ISAC_005 | "the level of the back-scattered light is inversely related to the forward FSO channel gain" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_005\O_ISAC_005.md :: II. SYSTEM MODEL > B. FSO Backhaul Sensing :: L60-L60 | VIII-C_CHALLENGES_12_supp |
| - | O_ISAC_005 | "evaluate the performance of the proposed model using a realistic channel model that uses climatic data" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_005\O_ISAC_005.md :: IV. RESULTS AND SYSTEM PERFORMANCE :: L211-L211 | VIII-C_CHALLENGES_12_supp |
| - | O_ISAC_050 | "jointly estimate UD location parameters and scattering channel states." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_050\O_ISAC_050.md :: Abstract :: L5-L5 | VIII-C_CHALLENGES_12_supp |
| - | O_ISAC_050 | "alleviate multipath interference and random channel fading" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_050\O_ISAC_050.md :: VI. CONCLUSION :: L586-L586 | VIII-C_CHALLENGES_12_supp |
| - | O_ISAC_381 | "the performance of the system would degrade with the decline in channel capacity as the distance increases" | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_381\O_ISAC_381.md :: 3.2. Data Transmission Performance :: L175-L175 | VIII-C_CHALLENGES_34_TAKEAWAYS_supp |
| - | O_ISAC_327 | "new technologies and application scenarios appear in 6G, which bring new characteristics and modeling challenges for VLC channels." | C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_327\O_ISAC_327.md :: I. INTRODUCTION > D. Related Surveys :: L61-L61 | VIII-C_CHALLENGES_34_TAKEAWAYS_supp |

## VIII-D supplement

# VIII-D Supplement (Merged, Deduplicated)

## Deduplicated Excerpt Bank

- excerpt_id: E01
  cite_key: O_ISAC_145
  excerpt: "Wireless transmissions are inherently susceptible to eavesdropping, making robust security measures essential."
  locator: C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_145\O_ISAC_145\O_ISAC_145.md :: **1 INTRODUCTION** :: L23-L23

- excerpt_id: E02
  cite_key: O_ISAC_145
  excerpt: "an attacker can eavesdrop on communications and sensing by falsifying the results, making them no longer trustworthy."
  locator: C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_145\O_ISAC_145\O_ISAC_145.md :: **1.1 Motivation** :: L37-L37

- excerpt_id: E03
  cite_key: O_ISAC_039
  excerpt: "To preserve the data privacy of the UE agents and prevent from confidential data leakage"
  locator: C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_039\O_ISAC_039.md :: 4 MULTI-TASK FEDERATED LEARNING FRAMEWORK FOR MULTI-USER COOPERATIVE VIPAC :: L278-L278

- excerpt_id: E04
  cite_key: O_ISAC_039
  excerpt: "only the learnt model weights are transmitted between the UE agents and the server"
  locator: C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_039\O_ISAC_039.md :: 4 MULTI-TASK FEDERATED LEARNING FRAMEWORK FOR MULTI-USER COOPERATIVE VIPAC :: L324-L324

- excerpt_id: E05
  cite_key: O_ISAC_039
  excerpt: "to preserve the data privacy of the UE agents and prevent from confidential data leakage"
  locator: C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_039\O_ISAC_039.md :: 4 MULTI-TASK FEDERATED LEARNING FRAMEWORK FOR MULTI-USER COOPERATIVE VIPAC :: L324-L324

- excerpt_id: E06
  cite_key: O_ISAC_156
  excerpt: "the adoption of key-based encryption and authentication techniques seems not well-tailored to cope with the forecasted massive connectivity and high network heterogeneity"
  locator: C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_156\O_ISAC_156\O_ISAC_156.md :: I. INTRODUCTION > *A. Motivation* :: L191-L191

- excerpt_id: E07
  cite_key: O_ISAC_156
  excerpt: "raises a concern about dynamic key management and distribution in such dense networks"
  locator: C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_156\O_ISAC_156\O_ISAC_156.md :: I. INTRODUCTION > *A. Motivation* :: L191-L191

- excerpt_id: E08
  cite_key: O_ISAC_156
  excerpt: "authentication and integrity are crucial processes in wireless communications security"
  locator: C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_156\O_ISAC_156\O_ISAC_156.md :: I. INTRODUCTION :: L187-L187

- excerpt_id: E09
  cite_key: O_ISAC_156
  excerpt: "provided a holistic overview of PLS techniques for achieving confidentiality, authentication, and malicious node detection"
  locator: C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_156\O_ISAC_156\O_ISAC_156.md :: VIII. CONCLUSION :: L1008-L1008

- excerpt_id: E10
  cite_key: O_ISAC_041
  excerpt: "Any interruption in network connectivity could significantly impede the development of IoE"
  locator: C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_041\O_ISAC_041.md :: I. INTRODUCTION :: L23-L23

- excerpt_id: E11
  cite_key: O_ISAC_041
  excerpt: "real-time monitoring and warning of fiber status are necessary"
  locator: C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_041\O_ISAC_041.md :: IV. RESULTS AND ANALYSIS :: L215-L215

- excerpt_id: E12
  cite_key: O_ISAC_041
  excerpt: "timely alerts are sent to the SDN controller."
  locator: C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_041\O_ISAC_041.md :: IV. RESULTS AND ANALYSIS > *C. Fiber Vibration Pattern Recognition* :: L363-L363

- excerpt_id: E13
  cite_key: O_ISAC_041
  excerpt: "promptly adjust services on the alerted fibers, thereby avoiding service interruptions"
  locator: C:\Users\Süleyman\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_041\O_ISAC_041.md :: IV. RESULTS AND ANALYSIS > *C. Fiber Vibration Pattern Recognition* :: L363-L363

## Source Coverage Map

- context_supp source: E01, E05, E12
- challenges_12_supp source: E01, E02, E03, E04
- challenges_34_takeaways_supp source: E06, E07, E08, E09, E10, E11, E12, E13
- math_anchor_supp source: E10, E02, E11, E12, E13, E03, E04, E07, E08

## Math-Anchor Term-Support Labels (Preserved)

- R_int: E02
- L_priv: E03
- A_auth: E07, E08
- u_mon: E11, E12, E13

## VIII-E supplement

# VIII-E Supplement (Merged, Deduplicated Excerpts)

## Deduplicated Excerpt Registry

- id: EX01
  cite_key: O_ISAC_039
  locator: data/proc_markdowns/O_ISAC_039/O_ISAC_039.md:L5
  excerpt: "the isolated design of positioning and communication has limited the system efficiency and performance."

- id: EX02
  cite_key: O_ISAC_039
  locator: data/proc_markdowns/O_ISAC_039/O_ISAC_039.md:L5
  excerpt: "the positioning task for the sensing service and the channel estimation task for the communication service are integrated into a unified architecture"

- id: EX03
  cite_key: O_ISAC_039
  locator: data/proc_markdowns/O_ISAC_039/O_ISAC_039.md:L43
  excerpt: "The MTFL framework is further formulated to improve the spatiotemporal generalization capability of the global model."

- id: EX04
  cite_key: O_ISAC_163
  locator: data/proc_markdowns/O_ISAC_163/O_ISAC_163.md:L90
  excerpt: "for a practical RIS implementation and the eventual roll-out, it is necessary to address all of them at once."

- id: EX05
  cite_key: O_ISAC_163
  locator: data/proc_markdowns/O_ISAC_163/O_ISAC_163.md:L5
  excerpt: "It considers applications for MF-RISs and the challenges associated with their deployment."

- id: EX06
  cite_key: O_ISAC_163
  locator: data/proc_markdowns/O_ISAC_163/O_ISAC_163.md:L588
  excerpt: "promising, but not mature enough to have a high TRL score."

- id: EX07
  cite_key: O_ISAC_151
  locator: data/proc_markdowns/O_ISAC_151/O_ISAC_151/O_ISAC_151.md:L126
  excerpt: "Semantic information is derived from the multimodal physical quantities sensed by smart fabric sensors"

- id: EX08
  cite_key: O_ISAC_151
  locator: data/proc_markdowns/O_ISAC_151/O_ISAC_151/O_ISAC_151.md:L126
  excerpt: "By incorporating additional contextual information, such as the sensor's deployment location and the current time"

- id: EX09
  cite_key: O_ISAC_151
  locator: data/proc_markdowns/O_ISAC_151/O_ISAC_151/O_ISAC_151.md:L124
  excerpt: "we utilize the encoder of the large language model to obtain a high-dimensional space representation of the semantic information"

- id: EX10
  cite_key: O_ISAC_151
  locator: data/proc_markdowns/O_ISAC_151/O_ISAC_151/O_ISAC_151.md:L242
  excerpt: "challenges remain regarding the computational power of edge devices and network bandwidth"

- id: EX11
  cite_key: O_ISAC_151
  locator: data/proc_markdowns/O_ISAC_151/O_ISAC_151/O_ISAC_151.md:L242
  excerpt: "challenges remain regarding the computational power of edge devices"

- id: EX12
  cite_key: O_ISAC_151
  locator: data/proc_markdowns/O_ISAC_151/O_ISAC_151/O_ISAC_151.md:L242
  excerpt: "and network bandwidth"

- id: EX13
  cite_key: O_ISAC_200
  locator: data/proc_markdowns/O_ISAC_200/O_ISAC_200.md:L41
  excerpt: "are often incompatible with existing telecom infrastructure such as optical amplifiers"

- id: EX14
  cite_key: O_ISAC_200
  locator: data/proc_markdowns/O_ISAC_200/O_ISAC_200.md:L282
  excerpt: "Open-source implementations are provided at https://github.com/kit-cel/pol\_sensing\_communication."

- id: EX15
  cite_key: O_ISAC_200
  locator: data/proc_markdowns/O_ISAC_200/O_ISAC_200.md:L332
  excerpt: "Open-source implementations are provided at https://github.com/Mohammadfarsi1994/physics-based-distributed-polarization-sensing."

- id: EX16
  cite_key: O_ISAC_200
  locator: data/proc_markdowns/O_ISAC_200/O_ISAC_200.md:L286
  excerpt: "It is therefore compatible with the standard DSP approaches based on adaptive equalization or VAEs"

- id: EX17
  cite_key: O_ISAC_200
  locator: data/proc_markdowns/O_ISAC_200/O_ISAC_200.md:L358
  excerpt: "A critical gap in the literature is the lack of realistic time-varying channel models"

## Term-Support Labels (Math Anchor)

- label: g_ready
  support_ids: EX04

- label: compat_infra
  support_ids: EX13

- label: budget_edge
  support_ids: EX11

- label: budget_bw
  support_ids: EX12

- label: valid_model
  support_ids: EX17

- label: prov_audit
  support_ids: EX14

## Coverage Map (Narrative Sections)

- section: Context
  support_ids: EX02, EX04, EX14

- section: Case_1
  support_ids: EX01, EX02, EX03

- section: Case_2
  support_ids: EX04, EX05, EX06

- section: Case_3
  support_ids: EX07, EX08, EX09, EX10

- section: Case_4
  support_ids: EX13, EX14, EX15, EX16, EX17

## VIII-F supplement

# VIII-F Supplement (Merged, Deduplicated Excerpts)

## Deduplicated Excerpt Registry

- id: EX01
  cite_key: O_ISAC_049
  locator: data/proc_markdowns/O_ISAC_049/O_ISAC_049/O_ISAC_049.md:L39
  excerpt: "both sensing and communication systems lead to a competition of limited resources"

- id: EX02
  cite_key: O_ISAC_107
  locator: data/proc_markdowns/O_ISAC_107/O_ISAC_107/O_ISAC_107.md:L456
  excerpt: "requires the prior acquisition of a set of measurements that should ideally be repeated when using a new UE"

- id: EX03
  cite_key: O_ISAC_107
  locator: data/proc_markdowns/O_ISAC_107/O_ISAC_107/O_ISAC_107.md:L456
  excerpt: "requires the prior acquisition of a set of measurements ... restrictive for a large-scale deployment"

- id: EX04
  cite_key: O_ISAC_133
  locator: data/proc_markdowns/O_ISAC_133/O_ISAC_133/O_ISAC_133.md:L35
  excerpt: "the transmission of additional OFDM blocks increases bandwidth consumption and intensifies channel noise"

- id: EX05
  cite_key: O_ISAC_133
  locator: data/proc_markdowns/O_ISAC_133/O_ISAC_133/O_ISAC_133.md:L35
  excerpt: "necessitating a careful balance between mitigating clipping distortion and limiting noise enhancement"

- id: EX06
  cite_key: O_ISAC_156
  locator: data/proc_markdowns/O_ISAC_156/O_ISAC_156/O_ISAC_156.md:L978
  excerpt: "requires parallel development of a unified analytical framework"

## VIII-F Artefact Evidence

- artifact: axis-domain list (A-E only)
  locator: analysis/VIII_ev_v1/axis_definitions.md:L4
  excerpt: "Axis-2 Challenge domains: standardization_interoperability, hardware_scalability_efficiency, channel_modeling_evaluation, security_privacy_reliability, deployment_convergence_roadmap."

- artifact: E isolated observation
  locator: analysis/VIII_ev_v1/s8f_dep_cov.csv:L6
  excerpt: "deployment_convergence_roadmap,0,0,0"

- dependency coverage rows used: `standardization_interoperability=55/55/55`, `channel_modeling_evaluation=54/54/54`, `hardware_scalability_efficiency=25/25/25`, `security_privacy_reliability=18/18/18`, `deployment_convergence_roadmap=0/0/0`
- research_agenda row IDs used: `standardization_interoperability`, `channel_modeling_evaluation`, `hardware_scalability_efficiency`, `security_privacy_reliability`, `deployment_convergence_roadmap`
- paper_challenge_map rows used: `O_ISAC_049`, `O_ISAC_107`, `O_ISAC_133`, `O_ISAC_156`
- summary.json key paths used: `n_standardization_interoperability_papers`, `n_hardware_scalability_efficiency_papers`, `n_channel_modeling_evaluation_papers`, `n_security_privacy_reliability_papers`, `n_deployment_convergence_roadmap_papers`, `n_multi_challenge_papers`
- summary_table rows used: all five challenge-domain rows in `section8F_summary_table.csv`
- contract_violations rows used: `O_ISAC_107`, `O_ISAC_156`
- duplicate-path decision: `O_ISAC_049` had inventory hits at `analysis/II_md_inv.csv:L50` and `analysis/II_md_inv.csv:L266`; the nested path `data/proc_markdowns/O_ISAC_049/O_ISAC_049/O_ISAC_049.md` was selected deterministically to match the preflight convention

## VIII-G supplement

# VIII-G Supplement

## Artefact Evidence Block

### axis_definitions.md

- locator: `analysis/VIII_ev_v1/axis_definitions.md:L4`
  used_for: Axis-2 lock; A-E remain the only challenge domains
  excerpt: `Axis-2 Challenge domains: standardization_interoperability, hardware_scalability_efficiency, channel_modeling_evaluation, security_privacy_reliability, deployment_convergence_roadmap.`

### section8G_cross_section_report.md

- locator: `analysis/VIII_ev_v1/section8G_cross_section_report.md:L3`
  used_for: VIII-G alignment-audit purpose
  excerpt: `This report compares strict Section VIII challenge evidence with upstream Section V/VI/VII linkage signals.`
- locator: `analysis/VIII_ev_v1/section8G_cross_section_report.md:L5-L8`
  used_for: `standardization_interoperability` aggregate continuity
- locator: `analysis/VIII_ev_v1/section8G_cross_section_report.md:L10-L13`
  used_for: `hardware_scalability_efficiency` aggregate continuity
- locator: `analysis/VIII_ev_v1/section8G_cross_section_report.md:L15-L18`
  used_for: `channel_modeling_evaluation` aggregate continuity
- locator: `analysis/VIII_ev_v1/section8G_cross_section_report.md:L20-L23`
  used_for: `security_privacy_reliability` aggregate continuity
- locator: `analysis/VIII_ev_v1/section8G_cross_section_report.md:L25-L28`
  used_for: `deployment_convergence_roadmap` zero-row state

### s8g_xsec_align.csv

- locator: `analysis/VIII_ev_v1/s8g_xsec_align.csv:L2`
  used_for: `standardization_interoperability` row
  row: `standardization_interoperability,55,55,55,55,55,0`
- locator: `analysis/VIII_ev_v1/s8g_xsec_align.csv:L3`
  used_for: `hardware_scalability_efficiency` row
  row: `hardware_scalability_efficiency,25,25,25,25,25,0`
- locator: `analysis/VIII_ev_v1/s8g_xsec_align.csv:L4`
  used_for: `channel_modeling_evaluation` row
  row: `channel_modeling_evaluation,54,54,54,54,54,0`
- locator: `analysis/VIII_ev_v1/s8g_xsec_align.csv:L5`
  used_for: `security_privacy_reliability` row
  row: `security_privacy_reliability,18,18,18,18,18,0`
- locator: `analysis/VIII_ev_v1/s8g_xsec_align.csv:L6`
  used_for: `deployment_convergence_roadmap` row
  row: `deployment_convergence_roadmap,0,0,0,0,0,0`

### s8g_xsec_ex.csv

- locator: `analysis/VIII_ev_v1/s8g_xsec_ex.csv:L2`
  used_for: example-payload status for `standardization_interoperability`
  row: `standardization_interoperability,strict_without_upstream,`
- locator: `analysis/VIII_ev_v1/s8g_xsec_ex.csv:L3`
  used_for: example-payload status for `hardware_scalability_efficiency`
  row: `hardware_scalability_efficiency,strict_without_upstream,`
- locator: `analysis/VIII_ev_v1/s8g_xsec_ex.csv:L4`
  used_for: example-payload status for `channel_modeling_evaluation`
  row: `channel_modeling_evaluation,strict_without_upstream,`
- locator: `analysis/VIII_ev_v1/s8g_xsec_ex.csv:L5`
  used_for: example-payload status for `security_privacy_reliability`
  row: `security_privacy_reliability,strict_without_upstream,`
- locator: `analysis/VIII_ev_v1/s8g_xsec_ex.csv:L6`
  used_for: example-payload status for `deployment_convergence_roadmap`
  row: `deployment_convergence_roadmap,strict_without_upstream,`

## Notes

- source mode: artefact-only
- paper-level cite-key mode not used in VIII-G due to empty examples payload
- aggregate continuity finding used: A-D rows remain matched at `strict_without_upstream_count = 0`
- zero-row finding used: `deployment_convergence_roadmap` remains `0/0/0`
- example-availability finding used: payload is absent across all current rows

