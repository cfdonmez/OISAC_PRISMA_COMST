# Ideal O-ISAC Survey Outline - Implementation Plan

**Amaç:** IEEE COMST standartlarında, "ilk kapsamlı Optical ISAC survey" olarak konumlandırılacak bir makale outline'ı oluşturmak.

**Temel:** 76 COMST makalesinin Golden Model analizi + 221 O-ISAC çalışmasından çıkarılan veriler

---

## 📋 Proposed Survey Outline

### 0. ABSTRACT (~250 words)
> *COMST Standardı: 200-250 kelime, 4 Bloklu Yapı (Context → Gap → Solution → Result)*
- **Context:** 6G/IoT trendlerine atıf (1-2 cümle)
- **Gap:** "However" ile başlayan problem tanımı (1 cümle)
- **Solution:** "In this paper..." ile katkı özeti (1-2 cümle)
- **Result:** "Finally" ile gelecek vizyonu (1 cümle)
- **Keywords:** Integrated Sensing and Communication (ISAC), Optical Wireless Communication (OWC), Fiber Sensing, 6G.

### I. INTRODUCTION (~4,500 words)
> *COMST Standardı: Geniş bağlam → Problem → Gap → Contributions → Organization*

#### A. The Convergence of Sensing and Communication (6G Vision)
- Neden ISAC önemli? 6G, autonomous systems, smart cities
- RF-ISAC'ın başarıları ve sınırları

#### B. The Optical Opportunity
- Optical spectrum avantajları (bandwidth, interference immunity, security)
- "Untapped potential" argümanı

#### C. The Fragmentation Problem
- **Fiber sensing** → DAS, φ-OTDR topluluğu (ayrı)
- **Wireless optical** → VLC, FSO topluluğu (ayrı)
- Terminoloji tutarsızlığı ("fiber sensing with comms" vs "O-ISAC")

#### D. Existing Surveys and Limitations
- **Table I: Comparison with Existing Surveys** (GAP SELLING - Zorunlu)
- RF-dominant ISAC surveys incelemesi
- "To the best of our knowledge, no survey provides a unified physical-layer framework..."

#### E. Contributions and Paper Organization
- **Fig. 1: Survey Structure Diagram** (Zorunlu)
- Explicit contribution listesi (numaralı)
- Section-by-section roadmap

---

### II. FUNDAMENTALS OF OPTICAL SENSING AND COMMUNICATION (~5,000 words)
> *COMST Gereksinimi: Tutorial-style background*

#### A. Optical Channel Models
1. **Fiber Channel:** Attenuation, dispersion, nonlinearity, Rayleigh backscattering
2. **FSO Channel:** Path loss, turbulence (Rytov, Gamma-Gamma), pointing errors
3. **VLC Channel:** LoS/NLoS, multipath, ambient light interference

#### B. Key Hardware Components
1. **Sources:** LED, LD, VCSEL, THz photonic sources
2. **Modulators:** MZM, TFLN-MZM, direct modulation
3. **Detectors:** PD, APD, SPAD, coherent receivers
4. **Emerging:** OPA (Optical Phased Array), Photonic Integrated Circuits

#### C. Sensing Principles in Optical Systems
1. **Time-of-Flight (ToF) / FMCW / LFM** — Range & velocity
2. **Phase-based (DAS, φ-OTDR)** — Vibration, acoustic
3. **Intensity-based** — Proximity, gesture recognition

#### D. ISAC Fundamentals
1. **Integration Paradigms:** Communication-centric, Sensing-centric, Joint Design
2. **Trade-off Dimensions:** Spectral efficiency, power allocation, waveform design

---

### III. METHODOLOGY: PRISMA 2020 SYSTEMATIC REVIEW (~2,500 words)
> *COMST + PRISMA Hybrid — Unique Differentiator*

#### A. Search Strategy
- Databases: IEEE Xplore, Scopus, Web of Science
- Search strings (Appendix'te detay)
- Temporal scope: 2010-2025

#### B. Eligibility Criteria
- **Inclusion:** Physical-layer optical sensing + communication
- **Exclusion:** RF-only, pure sensing, pure comms

#### C. Study Selection Process
- **Fig. 2: PRISMA Flow Diagram** (Zorunlu)
- Screening stages, duplicate removal

#### D. Data Extraction Framework
- Extraction schema (Appendix'te v2.1 schema referansı)
- Quality appraisal criteria

---

### IV. TAXONOMY OF O-ISAC SYSTEMS (~8,000 words)
> *Survey'in "kalbi" — Ana contribution*

#### A. Proposed Unified Taxonomy
- **Fig. 3: Sunburst/Hierarchical Taxonomy Diagram** (Zorunlu)

```
O-ISAC
├── Cabled (Fiber-based)
│   ├── Distributed Sensing + Telecom
│   │   ├── DAS-ISAC
│   │   ├── BOTDA-ISAC
│   │   └── OTDR-ISAC
│   ├── Fiber Bragg Grating + Comms
│   └── Hybrid Fiber-Wireless
│
└── Wireless (Free-Space)
    ├── VLC-ISAC (Indoor)
    │   ├── LED-based positioning + comms
    │   ├── Camera-based (OCC)
    │   └── LiFi + sensing
    ├── FSO-ISAC (Outdoor)
    │   ├── Atmospheric FSO + ranging
    │   ├── LiDAR-Communication hybrid
    │   └── THz photonic systems
    └── Underwater OWC + sensing
```

#### B. Cabled O-ISAC: Fiber-Based Systems
- Table II: Summary of Fiber-ISAC Approaches
- Subsections by sensing modality (vibration, temperature, acoustic)
- Integration strategies: Same-fiber vs Separate, WDM multiplexing

#### C. Wireless O-ISAC: VLC and Indoor Systems
- Table III: Summary of VLC-ISAC Approaches
- Positioning + communication trade-offs
- LED dimming vs data rate constraints

#### D. Wireless O-ISAC: FSO and Outdoor Systems
- Table IV: Summary of FSO-ISAC Approaches
- LiDAR + communication co-design
- Atmospheric effects on joint performance

#### E. Cross-Cutting Analysis
- **Waveform families across domains:** OFDM, Chirp/FMCW, Pulse
- Common enablers: RIS, IRS, machine learning

---

### V. PERFORMANCE METRICS AND TRADE-OFF ANALYSIS (~4,000 words)
> *Quantitative descriptive synthesis*

#### A. Communication Metrics
- Data rate, BER/SER, SNR, spectral efficiency
- **Table V: Performance Summary (Comm)**

#### B. Sensing Metrics
- Range resolution, accuracy, velocity estimation, spatial resolution
- **Table VI: Performance Summary (Sensing)**

#### C. The Sensing-Communication Trade-off
- **Fig. 4: Bubble Chart / Scatter Plot** (Data Rate vs Sensing Resolution)
- **Fig. 5: Pareto Frontier Analysis**
- Resource allocation strategies: TDM, FDM, joint waveform

#### D. Comparative Analysis: Fiber vs Wireless
- **Table VII: Head-to-Head Comparison**
- Strengths/weaknesses by application scenario

---

### VI. ENABLING TECHNOLOGIES AND HARDWARE (~3,500 words)

#### A. Photonic Integrated Circuits (PICs)
- Miniaturization, cost reduction
- Silicon photonics for ISAC

#### B. Optical Phased Arrays (OPAs)
- Beam steering without mechanical parts
- LiDAR + communication potential

#### C. Optical RIS/IRS
- Programmable metasurfaces
- Signal enhancement for both functions

#### D. AI/ML in O-ISAC
- Deep learning for joint optimization
- Channel estimation, resource allocation

---

### VII. APPLICATIONS AND USE CASES (~3,000 words)

#### A. Smart Infrastructure
- Pipeline monitoring + telecom (Fiber-ISAC)
- Structural health monitoring

#### B. Indoor Environments
- VLC positioning + data in retail/hospitals
- Smart lighting systems

#### C. Automotive and Transportation
- LiDAR-communication for V2V/V2I
- Autonomous vehicle sensing + connectivity

#### D. Underwater and Harsh Environments
- Underwater OWC + oceanographic sensing

#### E. Space and Satellite
- Inter-satellite optical links + debris sensing

---

### VIII. OPEN CHALLENGES AND FUTURE DIRECTIONS (~4,500 words)
> *COMST'ta %93 sıklık — Kritik section*

#### A. Standardization Gaps
- No unified O-ISAC protocol
- Need for industry-academia collaboration

#### B. Hardware Limitations
- Cost, power consumption, integration complexity
- Need for CMOS-compatible solutions

#### C. Channel Modeling Challenges
- Joint sensing-communication channel models lacking
- Atmospheric turbulence + comms modeling

#### D. Security and Privacy
- Eavesdropping in VLC/FSO
- Sensing data privacy

#### E. Integration with RF-ISAC
- Hybrid RF-Optical systems
- Seamless handover

### IX. CONCLUSION (~500 words)
> *COMST Standardı: Intro'nun Aynası (Restatement → Summary → Vision)*
- **Restatement:** "In this survey..." ile başlayıp amacı hatırlat (Past Tense).
- **Summary:** Bölüm bölüm (Section II-VIII) nelerin anlatıldığını özetle.
- **Vision:** "Hopefully..." ile bitir.

### X. REFERENCES
*(Otomatik oluşturulacak)*
- End-to-end learning
- Digital twin for O-ISAC

#### G. 6G and Beyond
- THz-optical convergence
- Holographic communications + sensing

---

### IX. CONCLUSION (~500 words)

- Summary of key findings
- Reiteration of contributions
- Call to action for the community

---

## 📊 Visual Budget (Target: 18-22 figures, 10-12 tables)

| Type | Count | Examples |
|------|-------|----------|
| System/Architecture | 3 | Fig 1 (Survey structure), Fig 3 (Taxonomy) |
| PRISMA Flow | 1 | Fig 2 |
| Performance Charts | 4 | Bubble chart, Pareto, trends |
| Technology Diagrams | 3 | Hardware, OPA, RIS |
| Application Scenarios | 2 | Use case illustrations |
| Summary Tables | 7 | Tables I-VII |
| Comparison Tables | 3 | Fiber vs Wireless vb. |

**Total: ~16 figures + 10 tables** (within COMST range)

---

## 📏 Word Budget (Target: ~36,000 words)

| Section | Words | % |
|---------|-------|---|
| I. Introduction | 4,500 | 12.5% |
| II. Fundamentals | 5,000 | 13.9% |
| III. Methodology | 2,500 | 6.9% |
| IV. Taxonomy | 8,000 | 22.2% |
| V. Performance | 4,000 | 11.1% |
| VI. Enabling Tech | 3,500 | 9.7% |
| VII. Applications | 3,000 | 8.3% |
| VIII. Future | 4,500 | 12.5% |
| IX. Conclusion | 500 | 1.4% |
| **Total** | **35,500** | 98.5% |

---

## 🎯 Unique Positioning (Gap Selling Arguments)

1. **First unified physical-layer O-ISAC survey** — Fiber + Wireless in one framework
2. **PRISMA 2020 compliant** — Rigorous systematic review methodology
3. **Quantitative synthesis** — 221 studies with extracted metrics
4. **Cross-domain taxonomy** — Bridges DAS/VLC/FSO communities
5. **Golden Model quality** — COMST standards reverse-engineered

---

## ✅ Verification Plan

### User Review Required
1. [ ] Overall section structure approval
2. [ ] Taxonomy hierarchy validation
3. [ ] Visual budget appropriateness
4. [ ] Missing sections feedback

### No Automated Tests (Documentation task)
This is a planning/documentation task. Verification is through user review and iteration.

---

> [!IMPORTANT]
> Bu outline, Golden Model standartlarına uygun olarak hazırlanmıştır.
> Kullanıcı feedback'i alındıktan sonra `memory-bank/surveyOutline.md` olarak kaydedilecektir.
