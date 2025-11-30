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

This systematic review aims to go beyond a simple cataloguing of optical integrated sensing and communication (O-ISAC) studies by constructing a **unified physical-layer framework** that jointly covers cabled (fibre-based) and wireless (FSO/VLC/LiDAR-like/retroreflective) implementations. The review emphasises (i) how sensing and communication functions are physically integrated on optical carriers, (ii) how their performance is quantified and traded off across heterogeneous optical media and models, and (iii) how these insights inform future 6G-oriented O-ISAC architectures.

### 3.1 Research Questions

To structure this objective, the review is organised around the following research questions:

- **RQ1 (Physical Integration and Architectures):**  
  How are sensing and communication functions jointly realised in cabled and wireless optical systems in terms of shared hardware, spectrum, and waveforms, and to what extent can these architectures be described within a unified physical-layer model?

- **RQ2 (Signal, Channel, and Trade-off Modelling):**  
  What classes of signal and channel models are used to describe optical ISAC operation, and how do existing works quantify and manage the trade-off between communication performance (e.g., rate, BER, reliability) and sensing performance (e.g., range, resolution, detection/estimation accuracy), including—where available—links to information-theoretic and estimation-theoretic limits?

- **RQ3 (Gaps, 6G Context, and Enabling Technologies):**  
  Which methodological gaps and open problems emerge when cabled and wireless O-ISAC studies are viewed through a common 6G physical-layer lens, and what implications do these have for emerging enabling technologies such as optical reconfigurable intelligent surfaces and optical phased arrays?

> **Note.** RIS/OPA are treated as *enabling-platform implications* of the O-ISAC evidence base. Studies that do not satisfy the O-ISAC eligibility criteria (Section 4) are not targeted for inclusion solely on the basis of RIS/OPA content.

### 3.2 Specific Objectives

To answer these questions, the review pursues the following specific objectives:

1. **Systematic identification and classification**
   - To systematically identify and classify optical ISAC studies into
     (i) cabled O-ISAC (fibre-based integrated sensing and communication) and
     (ii) wireless O-ISAC (FSO, VLC, LiDAR-like, retroreflective systems),
     based on the shared use of optical hardware, spectrum, and/or waveforms for both sensing and communication.

2. **Unified physical-layer taxonomy**
   - To develop a unified physical-layer taxonomy that organises O-ISAC systems jointly by
     - medium (fibre vs free-space),
     - integration mechanism (e.g., resource-division vs fully joint waveforms), and
     - signal dimension (intensity-only vs coherent field processing, single-aperture vs multi-aperture/array-based designs).

3. **Sensing–communication performance and trade-offs**
   - To synthesise reported performance metrics and trade-offs between communication (e.g., data rate, spectral efficiency, BER, latency, reliability) and sensing (e.g., range, resolution, sensitivity, detection probability, estimation error) in existing O-ISAC experiments and simulations, and to relate these trade-offs to known information-theoretic and estimation-theoretic limits where such comparisons are meaningful.

4. **Mapping traditional optical techniques into an O-ISAC framework**
   - To map how traditional optical communication and sensing techniques (e.g., coherent and IM/DD fibre links, distributed fibre sensing, VLC positioning, LiDAR and retroreflective schemes) have been adapted or reinterpreted under an O-ISAC framework, including systems that are functionally O-ISAC but not explicitly labelled as such.

5. **Comparative analysis of cabled vs wireless O-ISAC**
   - To comparatively analyse cabled and wireless O-ISAC systems along common dimensions (waveform design, channel modelling assumptions, hardware constraints, robustness to fibre nonlinearities and atmospheric/propagation impairments), in order to identify structural similarities, fundamental differences, and opportunities for cross-fertilisation between fibre and optical wireless communities.

6. **Gaps, open problems, and implications for 6G optical ISAC**
   - To identify methodological gaps, modelling inconsistencies, and open research problems that arise when bridging fibre sensing, optical wireless, and RF-ISAC perspectives, and to outline a research agenda for O-ISAC in 6G and beyond, including implications for programmable photonic platforms such as optical reconfigurable intelligent surfaces and optical phased arrays.

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

To capture both the communication-theoretic and optoelectronic physical-layer aspects of optical integrated sensing and communication (O-ISAC), the literature search will draw on a broad set of bibliographic databases and supplementary sources. All information sources, search strategies, and search dates will be documented in detail in line with PRISMA 2020 and the PRISMA-S extension for reporting literature searches.

### 5.1 Electronic Databases

The primary search will be conducted in the following databases and publisher platforms:

1. **IEEE Xplore (IEEE)**  
   *Focus:* Core source for communications, signal processing, radar/ISAC, and optical networking/FSO/VLC engineering literature (e.g., IEEE Transactions on Communications, IEEE Transactions on Wireless Communications, IEEE Journal on Selected Areas in Communications, Journal of Lightwave Technology, Journal of Optical Communications and Networking).
   *Rationale:* Captures the majority of RF/ISAC and optical communication work, including many O-ISAC and RO-ISAC papers published in IEEE venues.

2. **Scopus (Elsevier)**  
   *Focus:* Broad multidisciplinary coverage across engineering, physics, and applied optics, indexing major optical and photonics journals from multiple publishers.  
   *Rationale:* Ensures that O-ISAC-relevant work appearing in non-IEEE journals (e.g., optical physics, photonic device papers) is not missed.

3. **Web of Science Core Collection (Clarivate)**  
   *Focus:* High-quality citation indexing for science and engineering journals.  
   *Rationale:* Provides an independent cross-check on key O-ISAC publications and facilitates structured forward and backward citation tracking.

4. **Optica Publishing Group (formerly OSA) platform**
   *Focus:* Optics and photonics journals such as *Optics Express*, *Optics Letters*, *Optica*, *Optical Materials Express*, *Chinese Optics Letters*, and the *Journal of Optical Communications and Networking* (co-published with IEEE).  
   *Rationale:* Essential for fundamental photonics, fibre sensing (e.g., φ-OTDR/DAS, Brillouin/Raman-based schemes), and optical wireless device work that underpin cabled and wireless O-ISAC architectures.

5. **SPIE Digital Library** 
   *Focus:* Conference proceedings in optics and photonics, including LiDAR, electro-optical remote sensing, and optical engineering (e.g., *Lidar and Optical Remote Sensing for Environmental Monitoring*, *Electro-Optical Remote Sensing* series).  
   *Rationale:* Critical for early experimental demonstrations of LiDAR-like and optical sensing hardware that may implement O-ISAC-like functionality before appearing in journal form.

Where platforms permit multi-database searching (e.g., Scopus and Web of Science indexing overlapping content), the specific database(s) and platform(s) used will be clearly specified in the final review, together with the date of the last search for each source, as recommended by PRISMA-S.

### 5.2 Preprints and Grey Literature

Given the rapid development of 6G ISAC and O-ISAC research, preprint servers will be searched to identify emerging, highly recent work and to trace the peer-reviewed versions of influential manuscripts:

- **arXiv**  
  *Scope:* Categories `eess.SP` (Signal Processing), `cs.IT` (Information Theory), and `physics.optics` (Optics).  
  *Rationale:* Many ISAC, RO-ISAC, and optical radar/communication manuscripts initially appear as arXiv preprints before journal publication.

- **TechRxiv (IEEE preprint server)**  
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
  - *Photonics/optics conferences:* OFC (Optical Fiber Communication Conference), ECOC (European Conference on Optical Communication), CLEO, and selected SPIE conferences on LiDAR, electro-optical remote sensing, and optical engineering.
  - *Communications conferences:* IEEE ICC, IEEE Globecom, IEEE WCNC, and selected ISAC/6G-focused workshops co-located with these events.

The details of each supplementary search (venue, years covered, access route, and date searched) will be recorded in a structured search log to support reproducibility.

### 5.4 Documentation and Transparency

For every information source (databases, platforms, preprint servers, conference proceedings, and citation searches), the following will be reported in the final review:

- the full name of the source and platform,  
- the exact search strategy or browsing method used,  
- any date limits or filters applied,  
- the date when the source was last searched.

This level of detail follows PRISMA 2020 and PRISMA-S guidance on reporting the “what, when, and how” of information sources, and is intended to facilitate future updating of the review and independent assessment of its completeness. :contentReference

<!-- TODO: Add links to the archived search log (e.g., OSF) and record final search dates once the searches are executed. -->


---

## 6. Search Strategy  

The search strategy is designed to retrieve optical integrated sensing and communication (O-ISAC) studies across both cabled (fibre-based) and wireless (FSO/VLC/LiDAR-like) domains, with explicit emphasis on physical-layer architectures, signal and channel models, and joint sensing–communication performance. Search methods will be planned and reported in accordance with PRISMA 2020 and the PRISMA-S extension for reporting literature searches.

### 6.1 Conceptual Framework and Block Logic  

The search strategy is built around three conceptual blocks:

1. **Block A – Integrated sensing and communication concepts**  
   Terms capturing joint sensing–communication functionality, for example:  
   - "integrated sensing and communication", ISAC,  
   - "joint sensing and communication", "joint communication and sensing",  
   - "joint radar-communication", "dual-function radar-communication", DFRC,  
   - "simultaneous sensing and communication", "simultaneous ranging and communication",  
   - fibre-specific or VLC-specific phrases such as "communication and sensing on fiber", "fibre sensing and communication", "VLC localisation and communication".

2. **Block B – Optical media (cabled and wireless)**  
   Terms restricting the search to optical carriers and hardware, for example:  
   - optical, photonic,  
   - "optical fibre", "optical fiber", fibre, fiber,  
   - "free-space optical", FSO,  
   - "visible light", "visible light communication", VLC, LiFi,  
   - LiDAR, LIDAR, "optical radar",  
   - laser, LED, "optical wireless".

3. **Block C – Physical-layer emphasis (optional refinement)**  
   Terms emphasising physical-layer and hardware aspects, which may be added in sensitivity searches or when the volume of results is very large, for example:  
   - waveform, modulation, "signal model", "channel model",  
   - "physical layer", transceiver, beamforming, "optical front-end".

The **core Boolean structure** used for the main searches will be:

> (Block A) AND (Block B)

Block C will be used as an **optional refinement** when needed (e.g., in Scopus or Web of Science) to reduce clearly off-topic records while maintaining high recall. Exclusion terms (e.g., for purely seismic fibre sensing without any communication function) will be used cautiously and only after checking that they do not remove any records in the validation set (Section 6.3).

### 6.2 Database-Specific Search Strategies  

Database-specific syntax (field tags, proximity operators, wildcards, and filters) will be used for each information source listed in Section 5. The full, exact search strings for each database will be archived (e.g., as an appendix or OSF file) to ensure reproducibility.

#### 6.2.1 IEEE Xplore  

In IEEE Xplore, the search will target metadata fields (Abstract, Title, Keywords) and restrict results to journal articles and conference papers in English. A generic template is:

```text
( "integrated sensing and communication" OR ISAC 
  OR "joint sensing and communication" 
  OR "joint communication and sensing"
  OR "joint radar-communication" 
  OR "dual-function radar-communication" 
  OR DFRC
  OR "simultaneous sensing and communication"
)
AND
( optical OR photonic 
  OR "optical fibre" OR "optical fiber" OR fibre OR fiber
  OR "free-space optical" OR FSO
  OR "visible light" OR "visible light communication" OR VLC OR LiFi
  OR LiDAR OR LIDAR OR "optical radar"
)
```

Where feasible, proximity operators (e.g., NEAR/n) will be used in secondary runs to ensure that sensing/communication terms appear in the same local context as the optical medium terms (for example, "sensing" NEAR/5 "communication").

#### 6.2.2 Scopus and Web of Science

In Scopus and Web of Science, the search will be applied to titles, abstracts, and author keywords. Wildcards will be used to capture spelling variants and related terms. A representative Scopus-style query is:

```text
TITLE-ABS-KEY (
   ( "integrated sensing and communication" 
     OR ISAC 
     OR "joint sensing and communication" 
     OR "joint communication and sensing"
     OR "dual-function" W/3 (radar OR communication)
     OR "simultaneous" W/3 (sensing OR ranging) W/3 communication
   )
   AND
   ( optical* OR photonic* 
     OR "optical fibre" OR "optical fiber" OR fibre* OR fiber*
     OR "free-space optical" OR FSO
     OR "visible light" OR "visible light communication" OR VLC OR LiFi
     OR lidar* OR "optical radar"
   )
)
AND ( LIMIT-TO ( LANGUAGE, "English" ) )
```

For Web of Science, equivalent field tags (e.g., TS= for Topic) and filters (document type = Article OR Proceedings Paper; language = English) will be used.

#### 6.2.3 Optica Publishing Group and SPIE Digital Library

For Optica and SPIE platforms, whose interfaces may differ from IEEE Xplore and Scopus, searches will be configured to target at least the title and abstract fields, using combinations of Block A and Block B terms. When supported, proximity operators will be used to link sensing/communication concepts with optical media (e.g., "communication" NEAR/5 "distributed fiber sensing"; "LiDAR" NEAR/5 "communication"). Where platform limitations prevent full replication of the generic query, the exact syntax and any restrictions will be documented.

#### 6.2.4 Preprint Servers (arXiv, TechRxiv)

For arXiv (categories eess.SP, cs.IT, physics.optics) and TechRxiv, simplified queries will be used, for example:

```text
("integrated sensing and communication" OR "joint sensing and communication" OR ISAC)
AND
(optical OR "optical fiber" OR "optical fibre" OR FSO OR VLC OR LiFi OR LiDAR OR "optical radar")
```

Searches will be filtered by subject area when possible and limited to English-language manuscripts.

### 6.3 Piloting and Validation of the Search Strategy

To evaluate and refine the sensitivity and precision of the search:

1. A validation (“golden”) set of approximately 8–12 known O-ISAC papers will be assembled in advance, covering:
   - cabled (fibre-based) O-ISAC systems, and
   - wireless (FSO, VLC, LiDAR-like, retroreflective) O-ISAC systems.

2. Draft search strings will be iteratively adjusted until all validation-set papers are retrieved in each of the core databases (IEEE Xplore, Scopus, Web of Science). Any missed validation paper will trigger the addition or modification of functional keywords in Block A or Block B.

3. Where candidate exclusion terms (e.g., for purely seismic fibre sensing) are introduced, they will be tested against the validation set and a small random sample of potentially relevant records to ensure that true O-ISAC studies are not inadvertently removed.

4. The final search strategies will be peer reviewed by a second reviewer (e.g., supervisor or information specialist) for completeness and syntactic correctness before being executed.

### 6.4 Limits, Filters, and Search Updating

The following limits and filters will be applied consistently across databases, subject to the capabilities of each platform:

- **Language:** restricted to English.
- **Document type:** peer-reviewed journal articles and peer-reviewed conference papers (including short letters/communications where they contain sufficient technical detail).
- **Publication date:** database searches will be run from 2000 up to the final search date, in order to capture early optical systems that are functionally O-ISAC but predate the ISAC terminology. In line with the eligibility criteria (Section 4.4), the synthesis will place particular emphasis on approximately the last five years (e.g., 2020 onwards), while still including earlier foundational works that clearly implement joint sensing and communication on optical carriers.

If more than twelve months elapse between the initial search and completion of data synthesis, all database and preprint server searches will be updated using the same strategies, restricted to records added after the previous search date. Newly identified studies that meet the eligibility criteria will be incorporated into the screening, extraction, and synthesis processes, and the updated search date will be reported in the final review.

Full search strategies for all databases and information sources will be provided in an appendix or supplementary file and deposited in an open repository together with the search log.

---

## 7. Study Selection Process

The study selection process will follow the PRISMA 2020 flow, consisting of identification (deduplication), screening (title/abstract), and eligibility (full-text) phases. To ensure reproducibility and an auditable decision trail, all selection steps (including deduplication rules, screening decisions, and full-text exclusion reasons) will be executed and logged through the review’s GitHub-based workflow (e.g., Python notebooks/scripts and structured CSV logs).

### 7.1 Data Management and Deduplication (Identification)

Search results from all sources will be exported in standard bibliographic formats (e.g., RIS/CSV) and merged into a master dataset. Deduplication will be conducted in a **semi-automated** manner using a custom Python pipeline archived in the repository (e.g., `analysis/notebooks/01_search_and_dedup.ipynb`), with the following procedure:

1. **Automated Matching:** Duplicate candidates will be detected using a hierarchy of keys:
   - Exact/near-exact DOI matches (when available),
   - Normalised title similarity (case/punctuation removed; whitespace normalised),
   - Publication year consistency and, where available, author overlap.
2. **Manual Verification:** Candidate duplicates with metadata discrepancies (e.g., differing titles due to subtitles, preprint vs. publisher version, conference vs. journal extension) will be flagged for manual inspection by one reviewer, with the decision recorded in the screening log.
3. **Precedence Rule (Multiple Reports):** When the same study exists in multiple versions, the **most complete peer-reviewed version** (typically the journal article) will be prioritised as the primary record. Earlier versions (e.g., preprints or conference papers) will be retained as linked supplementary reports where relevant.

After deduplication, each unique record will be assigned a persistent identifier (`record_id`) and imported into the screening log for subsequent phases.

### 7.2 Screening Phases

Study selection will be conducted by two independent reviewers to minimise selection bias and improve methodological rigor.

#### Phase 1: Title and Abstract Screening
- **Calibration Exercise:** Prior to formal screening, both reviewers will independently screen a random sample of 50 records to calibrate the interpretation of the eligibility criteria (Section 4). Discrepancies will be discussed and the operational definitions refined before proceeding to the full screening set.
- **Process:** Each reviewer will classify records as **Include**, **Exclude**, or **Unsure** based on titles/abstracts against the predefined eligibility criteria.
- **Decision Rule (Conservative):** Any record marked as *Include* or *Unsure* by at least one reviewer will advance to the full-text stage, to reduce the probability of premature exclusion.

#### Phase 2: Full-Text Eligibility Assessment
- **Process:** Full texts of all potentially eligible records will be retrieved and assessed independently by both reviewers against Section 4.
- **Standardised Exclusion Coding:** Records excluded at full-text stage will be assigned a predefined exclusion code to enable transparent reporting and quantitative breakdowns in the PRISMA flow, for example:
  - `EXC-WRONG-DOMAIN`: RF/mmWave ISAC without an optical carrier.
  - `EXC-PURE-SENSING`: Optical sensing/imaging without a co-designed data communication function.
  - `EXC-PURE-COMM`: Optical communication without an explicit sensing task beyond routine channel estimation.
  - `EXC-NO-PHY`: Conceptual/system-level discussion lacking sufficient physical-layer models/parameters for extraction.
  - `EXC-TYPE`: Non-eligible publication type (e.g., thesis, white paper, non-peer-reviewed report).

### 7.3 Resolution of Disagreements

Disagreements will be handled using a staged resolution process:
1. **Consensus discussion** between the two reviewers.
2. **Third-reviewer arbitration** (e.g., supervisor) if consensus cannot be reached.

All adjudications will be documented in the screening log for auditability.

### 7.4 Transparency and PRISMA 2020 Reporting

The selection results will be reported using a PRISMA 2020 flow diagram, including:
- Records identified per source,
- Duplicates removed,
- Records excluded at title/abstract stage,
- Full-text articles assessed and excluded (with exclusion-code breakdown),
- Final included studies.

All screening decisions and full-text exclusion reasons will be archived in a structured CSV file (e.g., `screening/screening_log.csv`) and version-controlled in the repository, enabling independent verification and future updating of the review.

---

## 8. Data Collection Process

Data collection will follow a rigorous, schema-driven procedure designed to map each included study $s$ to a structured feature vector $\mathbf{x}(s)$, comprising both numerical physical-layer parameters (e.g., data rate, wavelength, sensing range, resolution) and categorical design choices (e.g., waveform family, detection type, channel/turbulence model). The procedure is designed to satisfy PRISMA 2020 (Item 9) and PRISMA-P recommendations on piloting and duplicate extraction.

### 8.1 Extraction Instrument and Data Dictionary

Data will be extracted using a predefined, version-controlled **O-ISAC Extraction Schema** (e.g., `extraction/schema/oisac_extraction_schema.yaml`). The schema functions as a strict data dictionary by defining, for each variable:

- **Data type:** float, integer, string, or constrained category (e.g., `turbulence_model` $\in$ {Log-Normal, Gamma–Gamma, Málaga, ...}).
- **Units:** standardised units (e.g., nm for wavelength, Gbps for rate) to ensure comparability.
- **Missing-data policy:** explicit distinction between **NR** (“Not Reported”) and **NA** (“Not Applicable”).
- **Provenance fields:** each extracted value will be linked to a source pointer (page/figure/table) to enable audit and re-checking.

### 8.2 Pilot Extraction and Refinement

Prior to the main extraction phase, a **pilot calibration** will be conducted on a diverse sample of 5–10 studies (covering fibre, FSO, and VLC domains). The objectives are:

1. To test schema coverage under real-world reporting heterogeneity.
2. To refine operational definitions for borderline or subjective fields (e.g., what qualifies as an explicit “joint” trade-off analysis).
3. To ensure consistent interpretation across reviewers before scaling to the full corpus.

Any substantive modifications to the schema resulting from the pilot will be recorded in the repository changelog and, if the protocol has been registered, in the protocol amendment history (Section 1.4).

### 8.3 Main Extraction Strategy

To balance methodological rigor with feasibility, a **hybrid double-extraction strategy** will be employed:

1. **Core bibliometrics and classification:** two reviewers will independently extract high-level metadata, medium/system classification (cabled vs. wireless), and primary sensing/communication performance metrics.
2. **Deep technical parameters:** complex model parameters (e.g., channel-equation coefficients, turbulence parameters, hardware constraints) will be extracted by one reviewer and explicitly verified by a second reviewer against the full text.

Extraction will be conducted using structured CSV forms (schema-validated at entry) and/or a custom Python-based interface to enforce controlled vocabularies, unit normalisation, and mandatory provenance fields.

### 8.4 Discrepancy Resolution and Agreement Monitoring

Disagreements between reviewers will be resolved through:

1. **Consensus discussion** with explicit citation of the relevant page/figure/table in the full text.
2. **Third-reviewer arbitration** (e.g., supervisor) if consensus cannot be reached.

Inter-rater reliability for categorical classification fields will be monitored during the pilot and early extraction phases using **Cohen’s Kappa ($\kappa$)**:

$$\kappa = \frac{p_o - p_e}{1 - p_e}$$

where $p_o$ denotes observed agreement and $p_e$ denotes chance agreement. Persistently low agreement (e.g., $\kappa < 0.6$ as a pragmatic “re-calibration” trigger) will prompt refinement of field definitions and an additional calibration round.

### 8.5 Handling Missing or Unclear Data

- **Explicit missingness:** values not stated in the report will be coded as **NR**.
- **Figure-only quantities:** when quantitative values are available only in plots, a digitisation tool (e.g., WebPlotDigitizer) may be used. Digitised values will be flagged (e.g., `EST-FIG`), accompanied by the figure reference, and **verified by a second reviewer**.
- **Author queries:** for seminal studies where critical physical-layer parameters are missing, corresponding authors may be contacted with a structured request. If the information cannot be obtained, the field will remain NR and be treated accordingly in synthesis.

### 8.6 Automation and Audit Trail

Python scripts will be used to parse bibliographic metadata, manage the extraction database, and enforce schema validation; however, extraction of non-trivial technical values will remain **human-in-the-loop** to preserve context-aware accuracy. All extraction artefacts (screening IDs, schema versions, changelogs, and the final dataset) will be version-controlled and archived in the project repository to provide a transparent, reproducible audit trail.

---

## 9. Data Items

The review will extract a structured set of variables (“data items”) from each included report, using the version-controlled extraction schema and data dictionary described in Section 8 (including explicit **NR** = Not Reported and **NA** = Not Applicable coding). The data items are designed to support (i) a unified physical-layer taxonomy across cabled and wireless optical media and (ii) a rigorous characterisation of sensing–communication coupling and reported trade-offs, spanning analytical, simulation, experimental, and hybrid evidence.

### 9.0 Unit of Extraction and Record Structure

Because many O-ISAC papers report multiple operating points (e.g., multiple distances, SNR regimes, turbulence levels, or modulation orders), extraction will be performed at two levels:

- **Study-level record (one per paper):** bibliographic information, high-level classification, architecture and modelling choices, and qualitative claims.
- **Scenario-level record (one-to-many per study):** each scenario corresponds to a distinct configuration under which quantitative sensing and/or communication outcomes are reported (e.g., a particular channel model/parameter set, link distance, waveform setting, or experimental condition). Scenario-level records enable faithful capture of curves and trade-off surfaces without arbitrary down-selection.

Where a study reports only one operating point, the study has a single scenario-level record.

### 9.1 Bibliographic and Administrative Information (Study-level)

- **record_id** (string): persistent identifier assigned after deduplication.
- **title** (string).
- **authors** (string).
- **year** (integer).
- **venue** (string): journal/conference name.
- **publisher/platform** (string; NR/optional).
- **doi** (string; NR/optional).
- **document_type** (enum): {journal, conference, letter/short communication}.
- **peer_review_status** (enum): {peer-reviewed, accepted, other}; primary synthesis targets peer-reviewed/accepted.

### 9.2 O-ISAC System and Medium Classification (Study-level)

- **oisac_medium_class** (enum): {cabled_fibre, wireless_fso, wireless_vlc, wireless_lidar_like, wireless_retroreflective, hybrid}.
- **carrier_band** (enum; NR/optional): {visible, NIR, SWIR, C-band, other}.
- **operational_environment** (enum; NR/optional): {indoor, outdoor, lab, field_trial, mixed}.
- **link_topology** (enum; NR/optional): {monostatic, bistatic, multistatic, distributed_fibre}.
- **mobility_context** (enum; NR/optional): {static, quasi_static, mobile, not_specified}.

### 9.3 Application Scenario and Use-case Taxonomy (Study-level)

- **application_domain** (enum; multi-label allowed): {vehicular, industrial_manufacturing, indoor_positioning, environmental_monitoring, critical_infrastructure, fibre_network_monitoring, robotics_autonomy, aerospace_space, uav_aerial, maritime_underwater, security_surveillance, other}.
- **scenario_description** (string; NR/optional): free-text summary of the intended use case.
- **requirements_claimed** (string; NR/optional): any explicit application targets (e.g., latency bounds, safety constraints, coverage/range requirements).

### 9.4 Evidence Type and Validation Strength (Study-level + Scenario-level)

- **evidence_type** (enum; multi-label allowed): {analytical, simulation, experimental, hybrid}.
- **validation_baselines_present** (boolean; NR/optional): whether explicit baselines/comparators are provided.
- **reproducibility_artifacts** (enum; NR/optional): {code_available, data_available, parameters_sufficient, insufficient}.

Scenario-level (if applicable):
- **num_trials_runs** (integer; NR/optional): Monte Carlo runs / experimental repetitions.
- **confidence_reporting** (enum; NR/optional): {ci_reported, std_reported, none_reported, not_applicable}.

### 9.5 Physical-layer Architecture (Tx/Rx) (Study-level + Scenario-level)

**Transmitter**
- **tx_source_type** (enum): {laser, led, frequency_comb, other}.
- **tx_modulation_type** (enum): {imd_d, coherent, mixed, not_specified}.
- **tx_external_modulator** (enum; NA/optional): {mzm, eam, none, other}.
- **wavelength_nm** (float; nm; NR/optional).
- **optical_bandwidth_hz** (float; Hz; NR/optional).
- **tx_power_dbm** (float; dBm; NR/optional) and/or **tx_power_mw** (float; mW; NR/optional).
- **aperture_diameter_m** (float; m; NA/NR/optional) for free-space systems.
- **beam_divergence_deg** (float; degrees; NA/NR/optional).
- **array_tx_elements** (integer; NA/NR/optional): number of emitters (if array/OPA).

**Receiver**
- **rx_detection_type** (enum): {direct, coherent, imaging, spad, other}.
- **rx_detector** (enum; NR/optional): {pin_pd, apd_pd, balanced_pd, camera_cmos, camera_ccd, spad_array, other}.
- **rx_aperture_diameter_m** (float; m; NA/NR/optional).
- **rx_optics_notes** (string; NR/optional): filters, lenses, telescopes.

**Shared hardware / integration**
- **hardware_sharing_mode** (enum; NR/optional): {shared_frontend, partially_shared, separate_frontends}.
- **duplexing_mode** (enum; NR/optional): {full_duplex, half_duplex, tdm, fdm, wdm, code_domain, spatial_domain, other}.

### 9.6 Signal and Waveform Design (Study-level + Scenario-level)

- **comm_waveform_family** (enum; NR/optional): {ook, pam, pam4, ofdm, dmt, ppm, qam, psk, chirp_fmcw, pulse_train, other}.
- **comm_modulation_order** (integer; NA/NR/optional).
- **comm_line_coding_fec** (string; NR/optional): FEC type/code rate if provided.
- **sensing_waveform_family** (enum; NR/optional): {pulse_tof, fmcw_chirp, lfm_chirp, ofdm_sensing, backscatter_probe, reflectometry, other}.
- **isac_waveform_relationship** (enum): {single_dual_function_waveform, comm_embedded_in_sensing, sensing_embedded_in_comm, multiplexed_separate_waveforms, not_specified}.
- **resource_partition_parameters** (string; NR/optional): time/frequency/wavelength/power splits, weights (e.g., α).

### 9.7 Channel and Propagation Models (Scenario-level where applicable)

**Fibre (if applicable)**
- **fibre_length_km** (float; km; NA/NR/optional).
- **attenuation_db_per_km** (float; dB/km; NA/NR/optional).
- **dispersion_ps_per_nm_km** (float; ps/(nm·km); NA/NR/optional).
- **nonlinearity_model** (enum; NA/NR/optional): {gn_model, nls_equation, kerr_only, ignored, other}.
- **backscatter_sensing_type** (enum; NA/NR/optional): {rayleigh_phi_otdr, das, brillouin, raman, fbg, other}.

**Free-space / VLC / LiDAR-like (if applicable)**
- **link_distance_m** (float; m; NA/NR/optional).
- **path_loss_model** (string; NR/optional).
- **turbulence_model** (enum; NA/NR/optional): {lognormal, gamma_gamma, malaga, h_k, other}.
- **turbulence_strength_parameters** (string; NA/NR/optional): e.g., Cn^2, Rytov variance, scintillation index.
- **pointing_error_model** (enum; NA/NR/optional): {zero, gaussian_jitter, beckmann, other}.
- **weather_impairments** (string; NA/NR/optional): fog/rain/snow visibility parameters if provided.
- **ambient_light_noise_model** (string; NA/NR/optional).
- **multipath_reflection_model** (string; NA/NR/optional) for VLC.

### 9.8 Communication Outcomes (Scenario-level)

- **data_rate_bps** (float; bps; NR/optional).
- **spectral_efficiency_bps_per_hz** (float; bits/s/Hz; NR/optional).
- **ber** (float; NR/optional).
- **fer_bler** (float; NR/optional).
- **snr_db** (float; dB; NR/optional).
- **outage_probability** (float; NR/optional).
- **latency_s** (float; seconds; NR/optional).

**Information-theoretic quantities (optional)**
- **capacity_bps_per_hz** (float; bits/s/Hz; NA/NR/optional).
- **capacity_assumptions** (string; NA/NR/optional): channel model, CSI assumption, input constraints.

### 9.9 Sensing Outcomes (Scenario-level)

- **sensing_task_type** (enum; multi-label allowed): {ranging, localization, imaging, vibration_displacement, strain_temperature, environment_state, target_detection, obstacle_detection, turbulence_characterization, other}.
- **sensing_range_m** (float; m; NR/optional).
- **range_resolution_m** (float; m; NR/optional).
- **angular_resolution_deg** (float; degrees; NA/NR/optional).
- **velocity_resolution_mps** (float; m/s; NA/NR/optional).
- **rmse** (float; unit + context in notes; NR/optional).
- **mae** (float; unit + context in notes; NR/optional).
- **pd** (float; NA/NR/optional): probability of detection.
- **pfa** (float; NA/NR/optional): probability of false alarm.

**Estimation-theoretic quantities (optional)**
- **crb_crlb_value** (float; unit depends on parameter; NA/NR/optional).
- **crb_parameter** (enum; NA/NR/optional): {range, angle, delay, doppler, position, other}.
- **crb_assumptions** (string; NA/NR/optional): observation model, noise model, priors.

### 9.10 Joint ISAC Coupling and Trade-off Characterisation (Scenario-level)

- **coupling_mode** (enum; NR/optional): {resource_division, joint_waveform, joint_receiver_processing, shared_hardware_only, other}.
- **tradeoff_type** (enum; multi-label allowed): {rate_vs_rmse, rate_vs_range_resolution, ber_vs_detection, throughput_vs_localization_error, power_split_tradeoff, sensing_time_vs_comm_time, other}.
- **tradeoff_representation** (enum; NR/optional): {single_point, curve, pareto_front, table, not_explicit}.
- **tradeoff_control_parameter** (string; NR/optional): name of α/β/time split/power split etc.
- **tradeoff_control_values** (string; NR/optional): numeric values or ranges as reported.

### 9.11 Enabling Technologies: Optical RIS / Metasurfaces and OPA (Study-level + Scenario-level)

These fields are extracted **only within included O-ISAC studies when reported**; they are not independent inclusion targets.

**Optical RIS / metasurface**
- **ris_present** (boolean).
- **ris_type** (enum; NA/NR/optional): {reflective, transmissive, hybrid, slm_equivalent, other}.
- **ris_num_elements_N** (integer; NA/NR/optional).
- **ris_element_pitch_m** (float; m; NA/NR/optional).
- **ris_phase_resolution_bits** (integer; NA/NR/optional).
- **ris_control_update_rate_hz** (float; Hz; NA/NR/optional).
- **ris_placement_geometry** (string; NA/NR/optional): Tx–RIS–Rx distances/angles if stated.
- **ris_role** (enum; NA/NR/optional): {link_enabler_nlos, beam_shaping, interference_management, sensing_assist, other}.

**Optical phased array (OPA)**
- **opa_present** (boolean).
- **opa_num_emitters** (integer; NA/NR/optional).
- **opa_steering_range_deg** (float; degrees; NA/NR/optional).
- **opa_beamwidth_deg** (float; degrees; NA/NR/optional).
- **opa_scan_rate_hz** (float; Hz; NA/NR/optional).
- **opa_role** (enum; NA/NR/optional): {beamforming_for_comm, scanning_for_sensing, joint_beamforming_scanning, other}.

### 9.12 Data Provenance, Digitisation Flags, and Decision Rules

- **source_pointer** (string): mandatory provenance reference to where each quantitative value was extracted (page/figure/table/equation).
- **value_origin_flag** (enum): {reported_text, reported_table, digitised_figure, computed_from_reported, inferred_not_allowed}.
- **digitisation_tool** (enum; NA/NR/optional): {webplotdigitizer, other}.

**Multiple-results handling (pre-specified decision rules):**
- **Scenario-level capture is the default:** when a paper reports multiple operating points (e.g., multiple distances, turbulence levels, SNR values), each is captured as a separate scenario-level record.
- **Curves and surfaces:** if outcomes are reported primarily as curves or Pareto fronts, representative points may additionally be recorded using a clearly defined rule (e.g., the authors’ default operating point, or the operating point associated with a stated target constraint such as BER ≤ 10^-3), while retaining the underlying curve via digitised samples when feasible.
- **No “silent” inference:** quantities not explicitly reported (or not recoverable via transparent digitisation) remain NR; model-class assignment is not guessed.

**Unit normalisation and derived variables:**
- All reported quantities will be converted to schema-standard units (e.g., nm, m, km, Hz, bps, dB).
- Where meaningful and sufficiently specified, derived variables (e.g., spectral efficiency from rate and bandwidth) may be computed and flagged as `computed_from_reported`.

---

## 10. Risk of Bias / Methodological Quality Assessment

Given the engineering nature of O-ISAC studies, conventional clinical risk-of-bias tools (e.g., QUADAS-2, ROBINS-I) are not applicable. Instead, methodological quality will be assessed using a bespoke **Technical Quality Appraisal Framework (TQAF)** tailored to physical-layer research. The framework prioritises **internal validity** (i.e., whether conclusions follow from realistic, explicitly stated models and sufficiently rigorous validation), while still recording external-validity constraints (e.g., narrow scenario choices) as secondary considerations.

The appraisal will be conducted at the **study level** for each included report. Ratings will be assigned independently by two reviewers during extraction (Section 8), recorded in the extraction dataset alongside provenance pointers (Section 9.12), and resolved via consensus (Section 7.3).

### 10.0 Core Principle: Engineering “Bias” as Systematic Optimism

In optical ISAC, the dominant source of systematic bias is **methodological optimism**: performance appears “too good” because the model, assumptions, validation regime, or reporting practices under-represent real impairments or uncertainty. Accordingly, TQAF primarily checks whether a paper:

- uses **physically plausible channel/impairment models** (Section 9.7),
- quantifies outcomes with **appropriate uncertainty handling** (Section 9.4, 9.12),
- validates performance against **relevant baselines and stress cases** (Section 9.4), and
- reports both **communication and sensing** outcomes consistently when ISAC is claimed (Section 9.8–9.10).

### 10.1 Modelling Fidelity and Assumption Realism (Internal Validity)

This dimension assesses whether the adopted signal/channel/hardware models are explicit, justified, and sufficiently realistic for the claimed contribution.

We will evaluate:
- **Model explicitness:** clear specification of waveform, transceiver, and observation model(s) enabling audit (Sections 9.5–9.6).
- **Channel realism (medium-specific):**
  - *Fibre:* treatment of attenuation/dispersion/nonlinearities and the sensing mechanism (φ-OTDR/DAS/Brillouin/Raman/FBG) where relevant (Section 9.7).
  - *Wireless:* turbulence/fading, pointing errors, ambient noise, and propagation assumptions consistent with the stated environment (Section 9.7).
- **Stochastic impairments:** whether randomness sources (noise, fading, speckle, jitter) are explicitly modelled and whether results are reported as averages/percentiles where appropriate (Section 9.4; 9.7–9.9).
- **Assumption disclosures:** clarity regarding CSI assumptions, synchronization, perfect alignment, ideal detectors, unbounded dynamic range, or other “idealities” that can materially inflate performance.

A study will be rated lower if it relies on overly idealised models without justification or if key parameters required to interpret the regime are missing (NR) in ways that affect conclusions.

### 10.2 Validation Strength and Comparative Rigor

This dimension evaluates whether the paper’s evidence (analytical, simulation, experimental, or hybrid) is strong enough to support its claims.

We will evaluate:
- **Baseline comparisons:** presence of meaningful comparators (e.g., sensing-only / comm-only variants, prior ISAC baselines, or ablations of the joint mechanism) (Section 9.4).
- **Scenario coverage:** whether results are reported across non-trivial operating ranges (e.g., distance/SNR/turbulence regimes; fibre length; modulation orders) rather than a single favourable operating point (Section 9.0).
- **Stress testing / sensitivity:** whether conclusions are robust to parameter variation or model mismatch (e.g., worse turbulence, increased jitter, bandwidth constraints).
- **Analytical correctness/closure (when applicable):** whether theoretical developments specify assumptions and boundary conditions and whether results connect to measurable quantities.

A study will be rated lower when the evaluation is narrow (single regime), lacks baselines, or does not substantively validate the claimed trade-off improvements.

### 10.3 Experimental Validity and Measurement Quality (When Experiments Exist)

For studies containing experiments or field trials, we will assess whether measurement methodology supports the reported outcomes.

We will evaluate:
- **Hardware and setup transparency:** sufficient detail to reproduce the measurement chain (Section 9.5).
- **Calibration/controls:** description of alignment, calibration, environmental controls, and instrumentation limits.
- **Repetition and variability:** reporting of trial counts, repeatability, and uncertainty (e.g., standard deviation, confidence intervals, error bars) (Section 9.4).
- **Confounding factors:** discussion of background light, weather/visibility, mechanical vibration coupling, detector saturation, and other effects that can systematically bias results.

Experimental studies with a single uncharacterised run, missing uncertainty reporting, or unclear setup will be rated lower.

### 10.4 Metric Completeness and ISAC Consistency (Cherry-picking Detection)

Because O-ISAC claims inherently involve joint performance, this dimension checks whether evaluation metrics are complete and aligned with the asserted ISAC contribution.

We will evaluate:
- **Dual-metric reporting:** whether at least one communication metric and one sensing metric are reported under the same scenario, or whether the paper provides an explicit, defensible rationale when one side is not applicable (Sections 9.8–9.10).
- **Trade-off explicitness:** whether the sensing–communication coupling is quantified (power/time/frequency split, shared waveform, joint receiver processing) and whether trade-offs are shown as points/curves/Pareto fronts with clear control parameters (Section 9.10).
- **Claim–evidence alignment:** whether the reported metrics and scenarios truly support the paper’s stated claims (e.g., “long-range” claims evaluated only at short range).

Papers that report strong results for only one function while asserting integrated ISAC capability (without the corresponding counterpart metrics) will be flagged for elevated risk of reporting bias.

### 10.5 Reproducibility and Reporting Completeness

This dimension evaluates whether the study provides sufficient information for independent reproduction or meaningful comparison.

We will evaluate:
- **Parameter sufficiency:** completeness of the parameter set required to interpret outcomes (Sections 9.5–9.9).
- **Uncertainty reporting:** presence of confidence intervals / standard deviations / run counts for stochastic results (Section 9.4).
- **Provenance and extraction feasibility:** whether key values are explicitly reported in text/tables, or must be digitised from figures (Section 9.12).
- **Availability of artefacts:** code/data availability or otherwise sufficiently described algorithms and setup (Section 9.4).

### 10.6 Rating Scheme, Visualisation, and Use in Synthesis

Each dimension (10.1–10.5) will be rated using an ordinal scale:
- **0 = low / unclear quality** (high risk of methodological optimism or insufficient reporting),
- **1 = moderate quality**,
- **2 = high quality** (well-specified model, robust validation, complete reporting).

Ratings will not be used as hard exclusion criteria. Instead, they will:
- inform domain-level confidence assessments (Section 13),
- guide interpretation and strength of recommendations in the narrative synthesis (Section 11), and
- support sensitivity-style checks (e.g., whether key conclusions are driven primarily by low-quality evidence).

To improve interpretability for readers, we will visualise the **quality landscape** of the O-ISAC literature using summary charts (e.g., stacked bar charts showing the distribution of low/moderate/high ratings across dimensions, and/or heatmaps by domain such as fibre vs FSO vs VLC). These visualisations will highlight recurrent weaknesses (e.g., systematic under-reporting of uncertainty or poor reproducibility) and will be reported alongside the synthesis.

### 10.7 Reviewer Agreement for Quality Ratings

To ensure rating consistency, inter-rater agreement will be monitored during the pilot extraction (Section 8.2) and early main extraction. For ordinal dimension ratings, agreement will be summarised using appropriate chance-corrected statistics (e.g., Cohen’s kappa for categorical/ordinal agreement with pragmatic interpretation thresholds). Persistent disagreement will trigger re-calibration of the operational definitions for the affected dimension(s).

## 11. Data Synthesis

### 11.1 Qualitative Synthesis

A structured, narrative synthesis will be undertaken, aiming to go beyond a mere listing of studies and instead construct a **unified framework** of O-ISAC designs and trade-offs (in line with the comprehensive approach expected in an IEEE COMST-style survey). The primary organisational scheme will be by **medium**:

- **Cabled O-ISAC (Fiber-based):** Integrated sensing–communication systems over optical fibers.
- **Wireless O-ISAC:** Free-space optical (FSO), visible light (VLC), and LiDAR-like systems (including retroreflective links), potentially further subdivided by application (e.g. VLC indoor localization vs. FSO ranging).

Within each medium-based category, studies will be compared and synthesized according to key design aspects and context, including:

- **Sensing tasks and application context:** (e.g. vibration sensing vs. imaging vs. positioning),
- **Signal and channel models:** (waveform families, modulation, optical channel characteristics),
- **Hardware architectures:** (type of transmit/receive optics, use of **programmable optics** like RIS/OPA if applicable), and
- **Joint strategies:** How sensing and communication functions are integrated or resource-shared (waveform multiplexing, power/time allocation, etc).

To unify these diverse findings, we will develop a hierarchical **physical-layer taxonomy** of O-ISAC systems covering both cabled and wireless implementations. This taxonomy will be visualized as a **sunburst chart** (a concentric ring diagram): the innermost ring represents the transmission **Medium** (e.g., **Fiber**, **FSO**, **VLC**), while successive outer rings represent **design feature categories** (for example, waveform type, channel model, integration strategy, etc.). In this visualization, each segment’s position and hierarchy show how a given study fits into the overall O-ISAC landscape – for instance, a segment in the Fiber inner-sector might branch into sub-segments for that study’s specific waveform (chirp vs. OFDM), which further branch into the channel model or hardware used. This sunburst diagram will thus illustrate clusters and overlaps across domains, highlighting common architectures (e.g. similar waveforms or channel assumptions appearing in both fiber and FSO regimes) as well as domain-specific niches.

**Taxonomy tables and figures** (including the sunburst chart) will be used to:

- **Visualize the O-ISAC design space** across cabled and wireless media, showing the hierarchical categorization of approaches in a single view (as described above).
- **Summarize typical metrics and operating regimes** associated with each category – for example, indicating representative ranges of data rate, sensing range, and resolution achieved by fiber-ISAC vs FSO vs VLC systems. Such summaries will help identify the **rate–range–resolution** regimes that different O-ISAC implementations operate in.
- **Highlight common trade-offs and design trends:** The taxonomy will make clear where different approaches share design principles (e.g. many VLC-ISAC studies using LED modulation techniques akin to those in fiber links) and where they diverge. Any cross-cutting trends (such as a preference for certain waveform types or co-design strategies) will be noted, providing a narrative thread through the otherwise heterogeneous literature.

This qualitative synthesis will thus produce a cohesive narrative that links studies under a common framework. The use of hierarchical taxonomy (visual and tabular) ensures that insights are framed generally (at the level of categories or patterns) rather than as isolated paper-by-paper summaries. Throughout the narrative, special attention will be given to points of integration between domains (e.g. how techniques from distributed fiber sensing inspire wireless optical methods, or vice versa), laying the groundwork for identifying gaps and opportunities discussed later in Section 11.3.

### 11.2 Quantitative Synthesis

A formal statistical meta-analysis (e.g. pooling effect sizes) is **not** planned, due to the high heterogeneity in performance metrics and evaluation scenarios across the included studies. The engineering studies in O-ISAC report diverse outcome measures (capacity, BER, range, accuracy, etc.) under varied conditions, making direct quantitative aggregation infeasible. Instead, we will perform a **quantitative descriptive analysis** of key performance relationships and trends to complement the qualitative synthesis.

**Key performance trade-off relations** to be analyzed include:

- **Capacity vs. Estimation Accuracy:** Where data is available, we will examine how communication throughput or capacity (in bps or bits/s/Hz) trades off against sensing accuracy, typically quantified by estimation error bounds or metrics (e.g., Cramér–Rao bound or RMSE of a measured parameter). This will elucidate the fundamental tension between maximizing data rate and maintaining precise sensing – for example, how adding communication payload might degrade ranging accuracy, or vice versa, in a given system.
- **Data Rate vs. Sensing Range:** We will compile instances where extending the sensing range (distance over which targets or events can be detected) impacts the achievable data rate. Many wireless O-ISAC systems must balance power and waveform design between long-range sensing and high-rate communication; plotting these two metrics against each other will highlight the design frontier (e.g., how a free-space optical link’s throughput drops as the required sensing distance grows, or how retroreflective O-ISAC can extend range at the cost of data rate).
- **Spectral Efficiency vs. Hardware Complexity:** We will qualitatively and quantitatively assess whether achieving higher spectral efficiency in O-ISAC (bits/s/Hz) correlates with increased hardware complexity. For instance, systems employing advanced photonic components, complex modulation, or multiple optical elements (mirrors, beam scanners, dual comb sources, etc.) might attain higher efficiency. By contrast, simpler hardware (e.g., direct modulation with a single LED) might limit spectral efficiency. We will document such correlations to infer if the state-of-the-art pushes complexity for performance or finds simpler trade-offs.

To **visualize these trade-offs**, we will employ multi-dimensional charts. In particular, **bubble charts** will be used to depict the joint relationships among three variables at once. For example, we will create a 2D plot of communication **data rate vs. sensing range**, and use the bubble color or size to encode a third metric such as sensing resolution (or estimation error). This will produce an intuitive visual of the **rate–range–resolution** interplay: one might observe, for instance, clusters of studies where short-range systems achieve very high rates and fine resolution, versus others where long-range sensing is achieved at lower data rates. Each bubble can represent a study or a specific experimental data point from a study, with distinct colors to denote different mediums or system types (e.g., fiber-based vs FSO vs VLC), thereby showing how the trade-off envelope might differ by sub-domain. Likewise, **3D scatter plots or interactive graphics** may be considered to explore capacity vs error vs SNR trade-spaces if enough data points exist.

We will also use **frequency distributions and trend charts** to summarize technological trends. For instance, **stacked bar charts** (grouped by publication year) will illustrate the prevalence of certain design choices over time. This could include showing the proportion of studies each year that use particular **modulation formats** (e.g., OOK, OFDM, Chirp-LFM, PAM4, etc.) or specific **hardware platforms** (such as those employing coherent detection, or using photonic integrated circuits, or incorporating RIS/OPA components). Such plots will reveal temporal patterns (e.g., a rise in the adoption of OFDM in recent years, or an increasing fraction of works using optical phased arrays post-2020) and help contextualize the evolution of the field.

All quantitative synthesis results will be presented as **descriptive evidence** to support the narrative, rather than as formal inferential statistics. Where subsets of studies are sufficiently comparable, we may report basic descriptive statistics (e.g., typical ranges, medians for data rate or sensing accuracy within that subset) and use **normalized metrics** to enable fair comparison (for example, normalizing spectral efficiency by optical bandwidth, or sensing error by distance or aperture). These analyses will be clearly marked as exploratory. They serve to map out performance envelopes and trade-offs, helping to answer *where* current O-ISAC designs lie in multi-dimensional performance space, rather than to produce a single aggregate “effect size.”

**Integration of quality appraisal:** In interpreting quantitative findings, we will factor in the **methodological quality scores** from Section 10. As part of the narrative, any striking performance claims that stem from studies rated low in technical quality (e.g., due to unclear models or lack of validation) will be **flagged as potentially unreliable**. Conversely, patterns or trade-offs observed consistently across multiple high-quality studies will be given greater weight in our conclusions. This effectively provides a *weighted narrative synthesis*: for example, if a particular rate-vs-range trend is only reported by papers with noted bias risks, we will caution the reader that this trend is tentative. On the other hand, a trade-off supported by rigorously validated studies will be highlighted as robust. By explicitly coupling the synthesis to the quality appraisal, we ensure that the review’s conclusions reflect not just the reported data, but also the credibility of that data.

### 11.3 Gap Analysis and Architectural Implications (RIS/OPA)

In a dedicated subsection of the synthesis, we will examine the **gaps and limitations** revealed by current O-ISAC implementations and discuss **architectural implications** of emerging programmable optical technologies – notably, **reconfigurable intelligent surfaces (RIS)** and **optical phased arrays (OPA)** – as potential solutions. This forward-looking analysis directly addresses the review’s objectives regarding open challenges and future directions (see Section 3), ensuring that our synthesis not only catalogues existing work but also maps how the field can evolve to overcome present limitations.

Specifically, we will identify critical pain points in present O-ISAC systems and map them to the capabilities of RIS/OPA-enabled architectures, for example:

- **Non-line-of-sight (NLoS) vulnerability in FSO links:** Free-space optical ISAC links typically require strict line-of-sight, making them susceptible to blockage by obstacles or pointing misalignment. Optical RIS (metasurface mirrors) offer a way to **reconfigure the propagation path**, effectively creating virtual mirrors in the environment to bend or relay optical signals around obstructions. By reflecting and focusing the beam in steps, RIS nodes can mitigate pointing errors through improved alignment and extend coverage to NLoS scenarios. Our synthesis will highlight how such RIS-assisted architectures could address one of the chief limitations of current FSO-based O-ISAC (which today struggle with reliability in dynamic or blocked environments), and will discuss any early studies or models that demonstrate this concept.

- **Limited beam steering speed and single-target focus:** Many optical sensing systems (e.g. LiDAR-like ISAC) rely on mechanical beam steering (galvanometric mirrors, gimbals) which are **slow, bulky, and limited in agility**, constraining how quickly a system can scan or track multiple objects. **Optical Phased Arrays (OPA)** represent a programmable solution: they can steer beams electronically with no moving parts, enabling **fast, multi-target beam steering**. By replacing or augmenting mechanical scanners with OPAs, O-ISAC systems could drastically improve their sensing refresh rates and cover multiple directions/users at once. This subsection will connect such OPA capabilities to the identified needs of current systems (e.g., rapid beam reconfiguration for vehicular LiDAR-communication or dynamic indoor VLC networks), and will also identify unresolved challenges and missing experimental validations.

Through these examples (and others as appropriate), we will discuss how **RIS/OPA-enabled architectures** could expand O-ISAC capabilities – for instance, enabling NLoS **coverage extension**, dynamic environment adaptation, or seamless integration of optical ISAC with smart surfaces in 6G networks. This subsection will also loop back to the earlier taxonomy and trade-offs: we will indicate where in our taxonomy such RIS/OPA-inclusive studies would fit, and what performance trade-off shifts they might allow (e.g., maintaining high data rate even in NLoS, or improving the rate-resolution trade-off via dynamic beam sharing). The goal is to identify **open research gaps** (e.g., the lack of experimental O-ISAC demonstrations using RIS or OPA so far, or unresolved challenges in their implementation) and to outline the **architectural implications** – how incorporating programmable optics could redefine the design space of optical ISAC.

In summary, the data synthesis (qualitative, quantitative, and gap analysis) will yield a comprehensive, PRISMA-aligned narrative that maps out the O-ISAC domain. It will present a **unified taxonomy**, extract and illustrate **performance trade-offs**, and critically discuss how emerging technologies like RIS and OPA can address current limitations. This approach is expected to deliver deeper insights and a cohesive understanding, as opposed to a superficial inventory of papers, thereby adding value in guiding both current practitioners and future research in optical ISAC.

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

