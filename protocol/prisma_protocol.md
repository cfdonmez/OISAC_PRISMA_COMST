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

The primary research question of this systematic review is:

- What are the physical-layer architectures, signal and channel models, and demonstrated sensing–communication performance trade-offs of optical integrated sensing and communication (O-ISAC) systems across cabled (fibre-based) and wireless (FSO, VLC, LiDAR-like, and retroreflective) optical domains?

The review focuses on modern O-ISAC literature, with particular emphasis on works published in approximately the last five years, while also including earlier optical systems that are functionally O-ISAC even if not explicitly labelled as such.


### 3.2 Specific Objectives

To answer the primary research question, this review pursues the following specific objectives:

1. **Systematic identification and classification**
   - To systematically identify and classify optical ISAC studies into
     (i) cabled O-ISAC (fibre-based integrated sensing and communication), and
     (ii) wireless O-ISAC (FSO, VLC, LiDAR-like, and retroreflective systems),
     based on the shared use of optical hardware, spectrum, and/or waveforms for both sensing and communication.

2. **Unified physical-layer taxonomy**
   - To develop a unified physical-layer taxonomy of O-ISAC signal models, channel models, and transceiver / hardware architectures that applies consistently to both fibre-based and wireless optical implementations.

3. **Performance metrics and trade-offs**
   - To synthesise reported performance metrics and trade-offs between communication (e.g., data rate, BER, capacity, latency) and sensing (e.g., range, resolution, sensitivity, detection probability) in existing O-ISAC experiments and simulations, highlighting common design patterns and resource-sharing strategies.

4. **Mapping traditional optical techniques into an O-ISAC framework**
   - To map how traditional optical communication and sensing techniques (e.g., coherent and IM/DD fibre links, distributed fibre sensing, VLC positioning, LiDAR and retroreflective O-ISAC) have been adapted or reinterpreted under an O-ISAC framework, including systems that are functionally O-ISAC but not explicitly labelled as such.

5. **Comparative analysis of cabled vs wireless O-ISAC**
   - To comparatively analyse cabled and wireless O-ISAC along common dimensions (waveform design, channel modelling assumptions, hardware constraints, robustness to impairments such as fibre nonlinearities and atmospheric turbulence), in order to identify similarities, fundamental differences, and cross-fertilisation opportunities.

6. **Gaps, challenges, and open research problems**
   - To identify methodological gaps, modelling inconsistencies, and open research problems that arise when bridging fibre sensing, optical wireless, and RF-ISAC perspectives, and to outline future research directions and benchmark scenarios for O-ISAC in 6G and beyond networks.

---

## 4. Eligibility Criteria

The eligibility criteria are defined a priori to ensure consistent selection of studies and tight alignment with the primary research question and specific objectives of the review. They operationalise the notion of optical integrated sensing and communication (O-ISAC) at the physical layer across cabled and wireless optical domains.

### 4.1 Types of studies

**Inclusion**

- Peer-reviewed **journal articles** and **full-length peer-reviewed conference papers** that present original analytical, simulation-based, experimental, or field-trial work on optical integrated sensing and communication.
- Studies that describe **physical-layer or link-layer** designs in which sensing and communication functions are jointly realised using shared optical hardware, spectrum, and/or waveforms.
- System-level or architectural papers that include **sufficient technical detail** on signal models, channel models, or transceiver/hardware architectures to support classification under the proposed physical-layer O-ISAC taxonomy.

**Exclusion**

- Non–peer-reviewed material (theses, book chapters, white papers, technical reports, magazine articles) and purely conceptual vision or position papers that do not provide concrete physical-layer models, architectures, or quantitative performance results.
- Standards and roadmap documents that mention ISAC or O-ISAC but lack sufficient technical detail for data extraction.

### 4.2 O-ISAC domain and system scope

**Inclusion**

- **Cabled O-ISAC (fibre-based):** Optical fibre systems where both
  - a **communication function** (e.g., coherent or IM/DD data transmission), and  
  - a **sensing function** (e.g., distributed vibration, temperature, strain, intrusion, infrastructure monitoring)  
  are realised on the same fibre infrastructure, and at least one of the following holds:
  - sensing and communication share the same optical wavelength, time slots, subcarriers, or power budget; or  
  - sensing backscatter/nonlinear effects are intentionally exploited while a communication channel coexists on the same fibre.

- **Wireless O-ISAC:** Free-space optical (FSO), visible light communication (VLC) / optical wireless (OWC), LiDAR-like, or retroreflective optical systems in which:
  - the same optical transmitter/receiver or optical front-end is used both to convey user data and to probe the environment (e.g., range, localisation, imaging, turbulence/obstacle sensing); or  
  - waveforms and resources (e.g., OFDM subcarriers, pulses, chirps) are jointly designed or allocated for simultaneous sensing and communication performance.

- Optical systems that are **functionally O-ISAC but not explicitly labelled as such**, including “joint sensing and communication on fibre,” “integrated communication and sensing in DSCM,” “hybrid gas sensing and FSO links,” or “VLC localisation with concurrent data,” provided they meet the shared-hardware/spectrum/waveform criterion above.

**Exclusion**

- Pure **optical communication** systems (fibre, FSO, VLC, LiDAR-like) that only provide data transmission and do not perform any explicit sensing or measurement task beyond standard channel estimation or tracking for equalisation/beamforming.
- Pure **optical sensing or imaging** systems (e.g., classical LiDAR, φ-OTDR/DAS, distributed temperature/strain sensing) that do not support or co-design a data communication channel on the same optical infrastructure.
- RF and millimetre-wave ISAC works without an optical carrier, even if conceptually similar.

### 4.3 Outcomes and reported information

**Inclusion**

- Studies that report at least one **communication-related metric** (e.g., achievable rate, spectral efficiency, BER, SNR, capacity, latency) **and** at least one **sensing-related metric** (e.g., range, spatial or temporal resolution, sensitivity, detection probability, estimation error, localisation accuracy), or provide sufficient detail for such metrics to be inferred.
- Studies that specify **signal models, channel models, and/or transceiver/hardware architectures** in enough detail to be mapped into the unified physical-layer O-ISAC taxonomy (e.g., waveform families, modulation/detection schemes, fibre or atmospheric channel models, key hardware constraints such as dynamic range or aperture).

**Exclusion**

- Studies that describe sensing or communication purely qualitatively, without quantitative performance, model parameters, or architectural detail sufficient for taxonomy and trade-off analysis.

### 4.4 Time frame

- **Primary window:** The core search will focus on studies published approximately in the **last five years** (e.g., 2020 onwards), reflecting the rapid emergence of explicitly framed optical ISAC work in both fibre and wireless optical domains.
- **Earlier foundational works:** Older studies (pre-2020) will also be considered **if** they clearly realise joint sensing and communication on optical carriers under the functional O-ISAC definition above (for example, early joint distributed sensing–communication fibre links, VLC positioning with concurrent data, or retroreflective optical links combining data and ranging).

The exact cut-off dates will be specified and justified in the search strategy, in light of the evolution of O-ISAC terminology and architectures.

### 4.5 Language and publication status

- Only studies published in **English** will be included, to ensure consistent technical interpretation and feasibility of screening.
- Peer-reviewed and formally accepted articles will form the primary evidence base. High-quality preprints (e.g., arXiv) may be tracked during screening for forward citation and, where appropriate, linked to subsequent peer-reviewed versions identified during updated searches.

### 4.6 Study design and setting

- No restriction will be imposed on setting (laboratory, field trial, industrial testbed, indoor/outdoor) as long as the optical ISAC criteria above are satisfied.
- Simulation-only, analytical, experimental, and hybrid (analysis + experiment) studies are all eligible, provided they report sufficient model detail and performance metrics for inclusion in the taxonomy and trade-off analysis.

---

## 5. Information Sources

To capture both the communication-theoretic and optoelectronic physical-layer aspects of optical integrated sensing and communication (O-ISAC), the literature search will draw on a broad set of bibliographic databases and supplementary sources. All information sources, search strategies, and search dates will be documented in detail in line with PRISMA 2020 and the PRISMA-S extension for reporting literature searches. :contentReference[oaicite:6]{index=6}

### 5.1 Electronic Databases

The primary search will be conducted in the following databases and publisher platforms:

1. **IEEE Xplore (IEEE)**  
   *Focus:* Core source for communications, signal processing, radar/ISAC, and optical networking/FSO/VLC engineering literature (e.g., IEEE Transactions on Communications, IEEE Transactions on Wireless Communications, IEEE Journal on Selected Areas in Communications, Journal of Lightwave Technology, Journal of Optical Communications and Networking). :contentReference[oaicite:7]{index=7}  
   *Rationale:* Captures the majority of RF/ISAC and optical communication work, including many O-ISAC and RO-ISAC papers published in IEEE venues.

2. **Scopus (Elsevier)**  
   *Focus:* Broad multidisciplinary coverage across engineering, physics, and applied optics, indexing major optical and photonics journals from multiple publishers.  
   *Rationale:* Ensures that O-ISAC-relevant work appearing in non-IEEE journals (e.g., optical physics, photonic device papers) is not missed.

3. **Web of Science Core Collection (Clarivate)**  
   *Focus:* High-quality citation indexing for science and engineering journals.  
   *Rationale:* Provides an independent cross-check on key O-ISAC publications and facilitates structured forward and backward citation tracking.

4. **Optica Publishing Group (formerly OSA) platform** :contentReference[oaicite:8]{index=8}  
   *Focus:* Optics and photonics journals such as *Optics Express*, *Optics Letters*, *Optica*, *Optical Materials Express*, *Chinese Optics Letters*, and the *Journal of Optical Communications and Networking* (co-published with IEEE).  
   *Rationale:* Essential for fundamental photonics, fibre sensing (e.g., φ-OTDR/DAS, Brillouin/Raman-based schemes), and optical wireless device work that underpin cabled and wireless O-ISAC architectures.

5. **SPIE Digital Library** :contentReference[oaicite:9]{index=9}  
   *Focus:* Conference proceedings in optics and photonics, including LiDAR, electro-optical remote sensing, and optical engineering (e.g., *Lidar and Optical Remote Sensing for Environmental Monitoring*, *Electro-Optical Remote Sensing* series).  
   *Rationale:* Critical for early experimental demonstrations of LiDAR-like and optical sensing hardware that may implement O-ISAC-like functionality before appearing in journal form.

Where platforms permit multi-database searching (e.g., Scopus and Web of Science indexing overlapping content), the specific database(s) and platform(s) used will be clearly specified in the final review, together with the date of the last search for each source, as recommended by PRISMA-S. :contentReference[oaicite:10]{index=10}

### 5.2 Preprints and Grey Literature

Given the rapid development of 6G ISAC and O-ISAC research, preprint servers will be searched to identify emerging, highly recent work and to trace the peer-reviewed versions of influential manuscripts:

- **arXiv**  
  *Scope:* Categories `eess.SP` (Signal Processing), `cs.IT` (Information Theory), and `physics.optics` (Optics).  
  *Rationale:* Many ISAC, RO-ISAC, and optical radar/communication manuscripts initially appear as arXiv preprints before journal publication.

- **TechRxiv (IEEE preprint server)** :contentReference[oaicite:11]{index=11}  
  *Scope:* Open, moderated repository for unpublished and pre-review research in electrical engineering, computer science, and related technologies.  
  *Rationale:* Provides early access to O-ISAC-related manuscripts submitted to IEEE journals and conferences.

Preprints will be **tracked and documented** but, consistent with the eligibility criteria (Section 4.5), only peer-reviewed or formally accepted versions will be included in the primary evidence base whenever such versions are available. Where a preprint is the only available version, this will be explicitly flagged and its influence on the synthesis discussed.

No clinical or trial registries will be searched, as O-ISAC is an engineering domain where such registries are not relevant.

### 5.3 Supplementary Search Methods

To minimise the risk of missing relevant O-ISAC studies, the following supplementary search methods will be employed:

- **Backward and forward citation chasing (snowballing):**  
  - *Backward snowballing:* Reference lists of all included full-text articles and key review papers will be screened for additional O-ISAC-relevant studies.  
  - *Forward snowballing:* Citation indices in Scopus, Web of Science, and Google Scholar will be used to identify subsequent articles citing the core O-ISAC papers.

- **Targeted venue and proceedings searches:**  
  Focused manual searches will be performed in recent (e.g., last 3–5 years) proceedings and issues of venues where optical sensing, photonics hardware, and communications/ISAC work intersect, including but not limited to:
  - *Photonics/optics conferences:* OFC (Optical Fiber Communication Conference), ECOC (European Conference on Optical Communication), CLEO, and selected SPIE conferences on LiDAR, electro-optical remote sensing, and optical engineering. :contentReference[oaicite:12]{index=12}  
  - *Communications conferences:* IEEE ICC, IEEE Globecom, IEEE WCNC, and selected ISAC/6G-focused workshops co-located with these events.

The details of each supplementary search (venue, years covered, access route, and date searched) will be recorded in a structured search log to support reproducibility.

### 5.4 Documentation and Transparency

For every information source (databases, platforms, preprint servers, conference proceedings, and citation searches), the following will be reported in the final review:

- the full name of the source and platform,  
- the exact search strategy or browsing method used,  
- any date limits or filters applied,  
- the date when the source was last searched.

This level of detail follows PRISMA 2020 and PRISMA-S guidance on reporting the “what, when, and how” of information sources, and is intended to facilitate future updating of the review and independent assessment of its completeness. :contentReference[oaicite:13]{index=13}

<!-- TODO: Add links to the archived search log (e.g., OSF) and record final search dates once the searches are executed. -->


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

