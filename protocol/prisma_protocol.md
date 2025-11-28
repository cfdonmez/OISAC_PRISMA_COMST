# Optical ISAC Systematic Review Protocol  
_Prepared in accordance with PRISMA 2020, PRISMA-P 2015, and PRISMA-S_

---

## 1. Administrative Information

### 1.1 Title  

**Optical Integrated Sensing and Communication (O-ISAC) over Cabled and Wireless Optical Channels: A Systematic Review Protocol**

This protocol describes the planned methodology for a systematic review of optical integrated sensing and communication (O-ISAC) systems, with a primary focus on **cabled (fibre-optic)** and **wireless optical (FSO/VLC/LiDAR-like)** implementations at the physical layer.

### 1.2 Registration  

The protocol will be prospectively registered on the **Open Science Framework (OSF)** under a dedicated project for optical ISAC (O-ISAC) systematic review. The OSF registration ID and DOI will be added here once available.

### 1.3 Support and Roles  

- **Funding / Support:**  
  Any funding bodies or institutional support (e.g., university, government agency, defence organisation) will be declared in the final review. Funders will not influence the design, study selection, analysis, or reporting.

- **Roles and Contributions:**  
  - Conceptualisation, methodology, and supervision: *[Supervisor / PI names]*  
  - Search strategy and data extraction: *[Name of PhD candidate]*  
  - Analysis and synthesis: *[Names as appropriate]*  
  - Manuscript drafting and critical revision: *[All authors]*  

### 1.4 Protocol Amendments  

Any substantial modification to the objectives, eligibility criteria, search strategy, or synthesis methods after registration will be documented with:  
(i) date of change,  
(ii) description of the amendment, and  
(iii) rationale.  

Amendments will be recorded in the OSF registration and summarised in a “Protocol Amendments” subsection of the final published review.

---
## 2. Background and Rationale

Integrated sensing and communication (ISAC) has been widely recognized as a key enabling technology for 6G and beyond networks, allowing the same hardware, spectrum, and waveforms to serve both data communication and environment sensing functions. A rich body of work now exists on radio-frequency (RF) and millimeter-wave ISAC, including joint radar–communications and dual-function radar–communications (DFRC) architectures, waveform design, and information-theoretic performance limits. These studies have firmly established ISAC as a spectrum- and cost-efficient paradigm in the RF and microwave domains. However, existing ISAC surveys and tutorial-style overviews overwhelmingly focus on RF-centric systems and only marginally touch upon optical bands, if at all.

In parallel, optical integrated sensing and communication (O-ISAC) has begun to emerge as a complementary paradigm that exploits the very large, largely license-free bandwidth of optical carriers, their inherent immunity to electromagnetic interference, and their potential for fine spatial and temporal resolution. Recent works have proposed O-ISAC architectures in which the same optical waveform and hardware are used to support both high-rate data transmission and high-resolution sensing, including ranging, vibration monitoring, localisation, and imaging. These efforts span both wired (fibre-based) and wireless (free-space and visible-light) optical domains and demonstrate that optical carriers can, in many scenarios, outperform RF ISAC in terms of achievable throughput and sensing accuracy.

On the cabled side, fibre-based O-ISAC (or fibre-ISAC) builds upon decades of research in distributed fibre-optic sensing, including Rayleigh-, Brillouin-, and Raman-based schemes such as φ-OTDR, DAS, and distributed temperature/strain sensing. While traditional distributed fibre sensing systems were deployed as standalone sensing links, recent contributions explicitly integrate high-speed coherent or intensity-modulated communication channels with distributed sensing on the same fibre, often sharing the wavelength channel and exploiting nonlinear or backscattering effects for both functions. A prominent example is the demonstration of integrated sensing and communication in an optical fibre (ISAC-OF), where periodic linear frequency-modulated light serves simultaneously as a carrier for PAM4 data and as a probe for distributed vibration sensing along tens of kilometres of fibre. Related advances extend this concept to digital subcarrier multiplexing (DSCM) systems and field trials where real-time fibre sensing coexists with 400 GbE coherent transmission in dense urban environments.

On the wireless side, wireless O-ISAC encompasses free-space optical (FSO), visible light communication (VLC), and LiDAR-like systems in which optical beams or illumination sources jointly convey user data and probe the environment. In FSO-based O-ISAC, pulsed, chirped, or OFDM-based optical waveforms have been used to enable simultaneous high-throughput links and sensing tasks such as target ranging, turbulence characterisation, and obstacle detection, including recent designs based on linear frequency modulation (LFM), continuous phase modulation (CPM), and multi-carrier waveforms. VLC-based O-ISAC systems, in turn, exploit LED luminaires to provide both indoor broadband communication and localisation/positioning, motion tracking, or contextual sensing. More recent work on retroreflective O-ISAC (RO-ISAC) uses corner-cube reflectors and carefully engineered hybrid waveforms to significantly extend sensing range and improve link robustness, with experimental demonstrations of full-duplex and bidirectional RO-ISAC links that trade off communication rate against ranging accuracy through flexible waveform design and power allocation.

Despite this growing activity, the O-ISAC literature remains fragmented across several largely disjoint communities: optical communications and photonics, distributed fibre sensing, LiDAR and optical remote sensing, VLC and optical wireless, and the broader ISAC/radar–communications community. Many optical systems that are functionally O-ISAC are not explicitly framed as such (e.g., “integrated communication and sensing in DSCM systems”, “optical covert sensing and communication”, “hybrid gas sensing and FSO communication”), and there is currently no unified taxonomy that jointly covers cabled versus wireless O-ISAC under a common physical-layer perspective. Existing overview-type papers either provide high-level architectural discussions of O-ISAC or focus on specific subdomains (e.g., fibre-based integrated sensing and communication, LED-based O-ISAC for IoT, or retroreflective O-ISAC), but do not systematically map the space of signal models, channel models, hardware architectures, and performance trade-offs across the full optical spectrum.

This review is motivated by the absence of a systematic, PRISMA-based survey that treats optical integrated sensing and communication as a coherent field and explicitly organises it along two main physical-layer axes: (i) **cabled O-ISAC**, where sensing and communication share fibre infrastructure and possibly spectrum, and (ii) **wireless O-ISAC**, where FSO, VLC, and LiDAR-like links realise joint sensing–communication in free space. By adopting a unified O-ISAC lens across these domains, the survey aims to bridge the vocabulary and modelling gaps between fibre sensing, optical wireless, and ISAC communities; highlight common waveform and channel-modelling structures; and identify cross-cutting design challenges and open research problems that are not apparent when these subfields are considered in isolation.
---


## 3. Objectives  

### 3.1 Primary Research Question  

> **How have optical integrated sensing and communication (O-ISAC) systems been implemented over cabled (fibre-optic) and wireless optical (FSO/VLC/LiDAR-like) channels at the physical layer, in terms of signal models, channel models, hardware architectures, and joint sensing–communication performance trade-offs?**

### 3.2 Specific Objectives  

1. **Mapping and classification**  
   To systematically identify and classify **cabled (fibre-based)** and **wireless optical (FSO/VLC/LiDAR-like)** O-ISAC systems reported in the peer-reviewed literature.

2. **Unified physical-layer model comparison**  
   To compare physical-layer signal models, channel models, transmitter/receiver structures, and resource allocation strategies of O-ISAC systems under a unified optical ISAC framework.

3. **Performance synthesis and trade-off characterisation**  
   To synthesise reported communication metrics (e.g., data rate, spectral efficiency, BER) and sensing metrics (e.g., resolution, accuracy, detection probability), and to characterise fundamental trade-offs between rate, reliability, coverage, and sensing accuracy in optical media.

4. **Separation of cabled vs wireless optical regimes**  
   To contrast fibre-based O-ISAC with wireless optical O-ISAC in terms of achievable sensing–communication trade-offs, channel constraints (dispersion, turbulence, multipath), and typical application scenarios.

5. **RIS/OPA-enabled and NLoS O-ISAC**  
   To identify and characterise optical RIS- and OPA-based O-ISAC architectures, with particular emphasis on **NLoS optical links** and turbulence-robust, beamforming-based O-ISAC designs.

---

## 4. Eligibility Criteria  

Eligibility criteria are defined in terms of optical medium, integrated functionality, study type, and reporting detail.

### 4.1 Inclusion Criteria  

A record will be included if it satisfies **all** of the following:

1. **Optical medium:**  
   The system uses optical carriers as the main physical medium, including at least one of:
   - Cabled fibre-optic links (single-mode or multi-mode),  
   - Free-space optical (FSO) links,  
   - Visible light communication (VLC) or other indoor optical wireless systems,  
   - LiDAR-like optical systems with explicit communication capability.

2. **Integrated sensing and communication (ISAC nature):**  
   The optical system implements **both sensing and communication functions** using shared or tightly coupled physical-layer resources, such as:
   - A common optical transmitter (e.g., laser, LED, OPA) and/or waveform used jointly for sensing and data transmission, or  
   - A common optical link (e.g., fibre) where distributed sensing and communication operate concurrently with non-negligible interaction or design coupling.

   Systems where sensing is purely incidental (e.g., channel estimation only for equalisation) without an explicit sensing task will **not** be considered O-ISAC.

3. **Cabled vs wireless optical classification:**  
   The study explicitly or implicitly fits into:
   - **Cabled O-ISAC:** fibre-based joint sensing–communication systems, or  
   - **Wireless O-ISAC:** FSO, VLC, or LiDAR-like O-ISAC systems (LOS or NLoS).

4. **Study type and level of detail:**  
   - Peer-reviewed journal articles or full conference papers.  
   - Provides sufficient technical detail on system and/or channel models, algorithms, or hardware to enable meaningful physical-layer interpretation.

5. **Language and time window:**  
   - Published in English.  
   - From the year **2000** up to the final search date, to capture both early joint optical sensing–communication concepts and modern O-ISAC terminology.

### 4.2 Exclusion Criteria  

Records will be excluded if any of the following hold:

- **Pure RF ISAC:**  
  Joint radar–communication or ISAC systems exclusively in RF/microwave bands, with no optical carrier or optical hardware component.

- **Pure optical communication (no sensing):**  
  FSO, VLC, or fibre-optic communication systems in which:
  - No explicit sensing task is performed, or  
  - Sensing is limited to channel estimation strictly for communication performance (without environment sensing, localisation, or target/state inference).

- **Pure optical sensing (no communication):**  
  Fibre sensing, LiDAR, or optical radar systems without any user data transmission or communication function.

- **Optical RIS/OPA without ISAC relevance:**  
  Optical RIS/metasurface or OPA-based systems that focus purely on communication or purely on sensing, with no integrated sensing–communication function or explicit O-ISAC perspective.

- **Non-primary or insufficiently detailed works:**  
  - Theses, books, patents, white papers, editorials, extended abstracts without full technical content (unless a corresponding full paper is available).  
  - Papers that mention O-ISAC or optical sensing/communication only at a high level without explicit system/channel model, architecture, or performance metrics.

---

## 5. Information Sources  

The following electronic databases will be searched:

- **IEEE Xplore** (journals and conferences in communications, photonics, radar/ISAC, and related fields).  
- **Scopus** (broad indexing of engineering and physics literature).  
- **Web of Science Core Collection**.  
- **arXiv** (for preprints; used to identify emerging O-ISAC works, clearly flagged as preprints and matched to peer-reviewed versions when possible).

Additional sources and techniques:

- **Backward and forward citation chasing** of key O-ISAC and optical sensing/communication papers.  
- **Targeted searches** in optical and photonics journals and conferences (e.g., JLT, IEEE Photonics Journal, JOCN, Light: Science & Applications) known to publish fibre sensing and optical wireless works.  

Searches and reporting will be aligned with the PRISMA-S checklist for literature searches.

---

## 6. Search Strategy  

### 6.1 Conceptual Blocks  

The search strategy will combine three main conceptual blocks:

1. **ISAC / joint sensing–communication concepts**  
   - "integrated sensing and communication" OR ISAC OR "joint sensing and communication" OR "joint radar-communication" OR "dual-function radar-communication" OR DFRC

2. **Optical media (cabled and wireless)**  
   - optical OR photonic OR "visible light" OR VLC OR "free-space optical" OR FSO OR "optical fibre" OR "optical fiber" OR LiDAR OR LIDAR

3. **Physical-layer emphasis (optional refinement)**  
   - waveform OR modulation OR "channel model" OR "physical layer" OR "signal model" OR transceiver OR beamforming

These blocks will be combined with Boolean logic. A generic IEEE Xplore-style query could be:

```text
(("integrated sensing and communication" OR ISAC OR "joint sensing and communication" 
  OR "joint radar-communication" OR "dual-function radar-communication" OR DFRC)
 AND
 (optical OR photonic OR "visible light" OR VLC OR "free-space optical" OR FSO 
  OR "optical fibre" OR "optical fiber" OR LiDAR OR LIDAR))
Database-specific syntax (field tags, proximity operators, wildcards) and filters (e.g., document type = article or conference, language = English) will be applied and documented. Where necessary, additional optical ISAC-specific terms (e.g., "LiDAR-communication", "illumination and communication", "fibre sensing and communication") will be added to ensure recall of earlier works that predate the “ISAC” acronym.
'''
### 6.2 Search Limits and Updates

- **Language:** English only.  
- **Publication date:** 2000–[final search date].  

**Search updates:**  
If the review extends beyond 12 months from the initial search, an updated search will be performed before final analysis. New records will be screened and extracted using the same procedures.

Full search strategies for all databases and information sources will be reported in an appendix or supplementary file.

---

## 7. Study Selection Process

A two-stage screening process will be followed:

### 7.1 Title/Abstract Screening

- Two reviewers will independently screen titles and abstracts against the eligibility criteria.  
- Records clearly unrelated to optical media or without any indication of integrated sensing and communication will be excluded.

### 7.2 Full-Text Screening

- Potentially relevant records will be assessed in full text by two independent reviewers.  
- Disagreements will be resolved by discussion; if unresolved, a third reviewer (e.g., supervisor) will arbitrate.

For each record, inclusion/exclusion decisions and reasons for exclusion at full-text stage will be documented in a structured log (e.g., `screening_log` table). The final review will present a **PRISMA 2020 flow diagram** summarising the selection process and counts at each stage.

---

## 8. Data Collection Process

Data extraction will be based on a predefined O-ISAC extraction schema and implemented using structured tables (e.g., CSV files) for:

- **Cabled O-ISAC studies** (fibre-based), and  
- **Wireless O-ISAC studies** (FSO/VLC/LiDAR-like).

**Key procedures:**

- A **pilot extraction** on 5–10 studies will be conducted to refine field definitions (e.g., distinguishing sensing vs communication metrics, channel model categories).  
- Two reviewers will independently extract core items (bibliographic data, system classification, main models and metrics). Extended technical details may be extracted by one reviewer and checked by another.  
- Discrepancies will be resolved by consensus, consulting the full text.  
- If critical information is missing or ambiguous (e.g., unclear joint nature of sensing and communication), authors may be contacted where practical.

---

## 9. Data Items

The following categories of data will be extracted for each included study (the exact field names and types are defined in the underlying extraction schema):

### 9.1 Bibliographic and Administrative Information

- Authors, year, venue, DOI, article type (journal / conference), research area.

### 9.2 High-level O-ISAC Classification

- Cabled vs wireless optical: fibre / FSO / VLC / LiDAR-like / hybrid.  
- Application context (e.g., distributed structural monitoring, indoor localisation, vehicular, autonomous systems), when specified.

### 9.3 Block-level Taxonomy (for Synthesis Alignment)

- **Block-1 (Optical ISAC):** Systems explicitly integrating sensing and communication in the optical domain (primary focus of this review).  
- **Block-2 (Optical RIS / metasurface):** Optical RIS/metasurface-assisted systems that enable or discuss integrated sensing–communication or are directly used as enabling components in O-ISAC architectures.  
- **Block-3 (Optical phased arrays, OPA):** OPA-based transmitters/receivers with joint beamforming and sensing capabilities used for or proposed as O-ISAC platforms.

This classification will support cross-referencing with broader optical wireless taxonomies and highlight RIS/OPA-enabled O-ISAC regimes.

### 9.4 Physical-layer Models and Architectures

- **Transmitter:**  
  - Laser vs LED vs OPA  
  - Intensity modulation vs coherent  
  - Wavelength(s)  
  - Power constraints  
  - Aperture and array configurations  

- **Receiver:**  
  - Direct vs coherent detection  
  - PD arrays vs imaging sensors  
  - Fibre sensing topologies (e.g., reflectometry configurations)  

- **Signal model:**  
  - Baseband/optical waveform  
  - Modulation format (OOK, PAM, OFDM, PPM, etc.)  
  - Multiple access or beamforming schemes  

- **Channel model:**
  - **Fibre:** attenuation, dispersion, nonlinearity models, crosstalk, etc.  
  - **FSO:** turbulence models (e.g., lognormal, Gamma–Gamma), pointing errors, weather impairments.  
  - **VLC:** LOS/NLoS impulse response, reflections, shot/thermal noise models.

### 9.5 Sensing Tasks and Metrics

- **Task type:** range, velocity, displacement/vibration, strain/temperature, localisation, imaging, environmental state estimation, etc.  
- **Metrics:** resolution, RMSE, CRLB/estimation bounds, detection probability, false alarm rate, sensing range/coverage, etc.

### 9.6 Communication Tasks and Metrics

- Data rate  
- Spectral efficiency  
- SNR/SCNR regimes  
- BER/FER  
- Outage probability  
- Latency  
- Reliability metrics (e.g., BLER), etc.

### 9.7 Joint Design Aspects (ISAC Coupling)

- Shared vs partitioned resources (time, frequency, wavelength, power, spatial beams).  
- Joint waveform and resource allocation strategies for sensing and communication.  
- Explicit trade-off analyses (e.g., sensing accuracy vs throughput, sensing range vs link margin).

### 9.8 Hardware and Implementation Details

- Simulation-only vs experimental vs hybrid.  
- Hardware platforms, prototypes, testbeds.  
- Channel conditions and scenarios (indoor/outdoor, atmospheric conditions, fibre length/regime).

### 9.9 Quality and Validation Aspects

- Presence of baselines or comparative methods.  
- Sensitivity analyses, robustness to channel/model mismatch.

---

## 10. Risk of Bias / Methodological Quality Assessment

Given the engineering nature of O-ISAC studies, a bespoke technical quality framework will be used rather than clinical tools.

Each study will be assessed along the following dimensions:

### 10.1 Model Transparency

- Clarity and explicitness of signal and channel models.  
- Clear separation and definition of sensing and communication roles.

### 10.2 Reproducibility

- Availability of sufficient system parameters, channel assumptions, and algorithmic details to enable reproduction or meaningful comparison.

### 10.3 Validation Strength

- **Simulations:** diversity and realism of parameter ranges, presence of baselines.  
- **Experiments:** clarity of hardware description, setup, measurement conditions, trial counts, and uncertainty or variability reporting.

### 10.4 Metric Completeness and Consistency

- Reporting of both sensing and communication metrics when ISAC is claimed.  
- Consistency between claimed contributions and the reported metrics and scenarios.

### 10.5 Bias Indicators

- Selective reporting of favourable results.  
- Omission of relevant baselines.  
- Lack of discussion of limitations.

Each dimension will be rated using a simple ordinal scale (e.g., 0 = low / unclear, 1 = moderate, 2 = high quality). These quality assessments **will not** be used as hard exclusion criteria but will:

- Inform domain-level confidence assessments (Section 13), and  
- Be explicitly considered when interpreting which O-ISAC design patterns are supported by stronger or weaker evidence.

---

## 11. Data Synthesis

### 11.1 Qualitative Synthesis

A structured, narrative synthesis will be performed, with primary grouping by **medium**:

- **Cabled O-ISAC:** fibre-based integrated sensing–communication systems.  
- **Wireless O-ISAC:** FSO/VLC/LiDAR-like systems, further subdivided if appropriate (e.g., VLC localisation vs FSO ranging).

Within each group, studies will be organised according to:

- Sensing tasks and application contexts,  
- Signal and channel models,  
- Hardware architectures (including RIS/OPA where relevant),  
- Joint sensing–communication strategies and resource allocation schemes.

**Taxonomy tables and figures** will be used to:

- Visualise the space of cabled vs wireless O-ISAC systems,  
- Summarise typical metrics and operating regimes (e.g., rate vs range vs resolution),  
- Highlight common trade-offs and design trends.

### 11.2 Quantitative Elements

A formal meta-analysis in the statistical sense (e.g., pooled effect sizes) is **not** planned, due to:

- Strong heterogeneity in performance metrics, scenarios, and channel conditions, and  
- Diverse design goals across engineering studies.

However, where subsets of studies are sufficiently homogeneous (e.g., similar scenarios and metrics), **descriptive statistics** and **normalised plots** may be used, such as:

- Ranges and typical values for data rates, spectral efficiencies, sensing resolutions, and SNR/SCNR.  
- Normalised performance indicators (e.g., bits/s/Hz vs sensing resolution scaled by aperture or wavelength).

These quantitative elements will be clearly presented as **descriptive** rather than inferential synthesis.

---

## 12. Meta-bias Assessment (Publication and Reporting Biases)

Traditional tools for assessing publication bias (e.g., funnel plots) are not directly applicable. Instead, meta-bias will be qualitatively assessed by considering:

- **Venue/community concentration:** dominance of certain research groups or venues for specific O-ISAC architectures.  
- **Result orientation:** preference for publishing only positive ISAC gains vs neutral or negative findings.  
- **Metric asymmetry:** tendency to report only communication metrics (or only sensing metrics) while claiming integrated ISAC functionalities.

These aspects will be discussed as limitations in the final review and linked to the domain-level confidence assessments.

---

## 13. Certainty of Evidence / Confidence in the Body of Evidence

An informal but structured **confidence-in-evidence** assessment will be carried out at the **domain level**, e.g.:

- Fibre-based O-ISAC,  
- FSO-based O-ISAC,  
- VLC-based O-ISAC,  
- RIS/OPA-enabled O-ISAC.

For each domain, confidence will be judged based on:

- Number and independence of studies and consistency of reported trends,  
- Methodological quality and risk-of-bias profiles (Section 10),  
- Alignment between simulation and experimental evidence when both exist.

Each domain will be assigned a qualitative rating (e.g., **high**, **moderate**, **low** confidence) with justification, which will guide:

- The strength of design recommendations, and  
- The identification of open problems.

---

## 14. Dissemination

The completed systematic review is intended for submission to a **high-impact communications journal**, such as *IEEE Communications Surveys & Tutorials*, or a comparable venue in communications/optics.

To promote transparency and re-use:

- The full set of **search strategies**,  
- **Screening and extraction tables**, and  
- Any scripts used for analysis and figure generation  

will be made available via **OSF** and/or a public code repository, subject to journal policies.

The review will also serve as a **core chapter** in an ongoing PhD thesis on optical ISAC and RIS/OPA-enabled NLoS optical wireless systems, ensuring close integration between:

- The taxonomy established in this review, and  
- Subsequent original research contributions.


