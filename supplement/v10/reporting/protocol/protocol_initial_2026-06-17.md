# 01 - O-ISAC PRISMA Review Protokol Sablonu

Bu protokol, O-ISAC for 6G calismasi icin arama yurutulmeden once metodolojik kararlari sabitlemek amaciyla hazirlanmistir. Aciklamalar Turkce tutulur; manuscript-ready akademik metinler English yazilir. Protokol sonrasi her kapsam, arama, secim, veri cekme, kalite degerlendirmesi veya sentez degisikligi `09_kayitlar/decision_log.md` dosyasina tarihli olarak kaydedilecektir.

## 1. Review Type

**Durum:** drafted

**Karar:** PRISMA-grounded narrative systematic review with a scoping-style PCC component.

Bu calisma meta-analysis hedefleyen klasik nicel pooling calismasi olarak degil, O-ISAC literaturunu PRISMA temelli secim ve raporlama disipliniyle derleyen; taxonomy, metric reporting, validation maturity ve benchmark readiness boyutlarini scoping-style PCC mapping ile haritalayan narrative systematic review olarak konumlandirilir.

## 2. Working Title

**Durum:** drafted

**Manuscript-ready draft:**

Optical Integrated Sensing and Communication for 6G: A PRISMA-Grounded Systematic Review and Metric-Governed Cross-Modality Survey

## 3. Background/Rationale

**Durum:** drafted

**Manuscript-ready draft:**

Optical Integrated Sensing and Communication (O-ISAC) is emerging as a candidate technology family for 6G systems in which optical communication infrastructures are also used to support sensing, localization, monitoring, or environmental perception functions. The field spans fiber-based systems, free-space optical links, VLC/LiFi platforms, photonic-THz architectures, and hybrid optical systems. These modalities differ substantially in propagation channel, hardware constraints, sensing target, communication objective, measurement plane, and validation method.

Existing O-ISAC studies report diverse communication metrics, sensing metrics, experimental setups, simulation assumptions, and technology-specific constraints. This makes direct cross-study comparison difficult and limits the readiness of the field for benchmarking, reproducibility assessment, and system-level roadmap development. A PRISMA-grounded narrative systematic review with a scoping-style PCC component is therefore needed to map the peer-reviewed O-ISAC evidence base, compare cross-modality reporting practices, and identify gaps in validation maturity and benchmark readiness for 6G-oriented optical systems.

## 4. Objectives

**Durum:** drafted

**Manuscript-ready draft:**

The objective of this review is to systematically identify, screen, and synthesize peer-reviewed studies on O-ISAC for 6G-oriented optical platforms, and to develop a cross-modality evidence map covering taxonomy, sensing and communication metric reporting, metric comparability, comparison admissibility, rate-sensing tradeoffs, enabling technologies, application domains, validation maturity, benchmark readiness, and open research gaps.

**Primary research question:**

How has Optical Integrated Sensing and Communication (O-ISAC) been investigated across fiber, free-space optical, VLC/LiFi, photonic-THz, and hybrid optical platforms, and what do existing peer-reviewed studies reveal about cross-modality taxonomy, sensing and communication metric reporting, metric comparability, comparison admissibility, rate-sensing tradeoffs, enabling technologies, application domains, validation maturity, benchmarking readiness, and remaining research gaps for 6G-oriented O-ISAC systems?

## 4A. Operational Definition

**Durum:** complete

**Manuscript-ready definition:**

In this review, O-ISAC refers to optical or photonic systems in which sensing and communication functions are jointly considered, integrated, co-designed, co-optimized, or evaluated within the same architecture, optical link, waveform/resource framework, hardware platform, channel model, or application scenario.

## 4B. Research Questions

**Durum:** drafted

RQ1:

What optical modalities, system architectures, integration levels, sensing tasks, and application domains define the current O-ISAC literature for 6G-oriented systems?

RQ2:

How consistently do O-ISAC studies report communication metrics and sensing metrics across fiber, FSO, VLC/LiFi, photonic-THz, and hybrid optical systems?

RQ3:

To what extent are reported O-ISAC metrics comparable across modalities, measurement planes, validation methods, and reporting conditions, and when is cross-study comparison admissible?

RQ4:

What rate-sensing tradeoffs are analyzed or experimentally demonstrated in O-ISAC studies, and how are these tradeoffs shaped by modality, architecture, waveform design, resource sharing, and measurement plane?

RQ5:

What enabling technologies, signal processing methods, channel models, hardware assumptions, and system design strategies are used to support integrated optical sensing and communication?

RQ6:

What is the validation maturity and benchmark readiness of the O-ISAC evidence base, including theoretical analysis, simulation, laboratory validation, field testing, prototyping, dataset availability, reproducibility support, and benchmark-based evaluation?

RQ7:

What benchmark readiness gaps, reporting limitations, reproducibility barriers, and research roadmap priorities remain for 6G-oriented O-ISAC systems?

## 5. PCC Framework

**Durum:** complete

PICO/PECO/PICo yerine PCC secilmistir; cunku calisma klinik mudahale-etki sorusu degil, heterojen teknoloji literaturunde kapsam, kavram ve uygulama baglami haritalama sorusudur.

| PCC bileseni | Protokol tanimi |
|---|---|
| Population | Peer-reviewed studies on Optical Integrated Sensing and Communication / O-ISAC systems. |
| Concept | Cross-modality O-ISAC architectures, taxonomy, sensing/communication metric reporting, metric comparability, comparison admissibility, metric-governed comparison, rate-sensing tradeoff synthesis, enabling technologies, application mapping, validation maturity, and benchmarking readiness. |
| Context | 6G-oriented optical platforms, including fiber, free-space optical / FSO, VLC/LiFi, photonic-THz, and hybrid optical communication-sensing systems. |

## 6. Eligibility Criteria

**Durum:** drafted

### Inclusion Criteria

- Peer-reviewed journal articles, early-access journal articles, and full-length conference/proceedings papers.
- Studies focused on Optical Integrated Sensing and Communication, integrated optical communication-sensing, optical ISAC, or closely equivalent optical joint communication and sensing systems.
- Studies addressing at least one optical platform relevant to the review context: fiber, FSO, VLC, LiFi, photonic-THz, or hybrid optical systems.
- Studies reporting at least one communication-relevant metric, sensing-relevant metric, tradeoff result, system architecture, validation method, or benchmark-relevant evaluation element.
- English-language publications.
- Publication date within January 1, 2020 - June 30, 2026.

6G relevance will be coded as direct, inferred, weak, or not applicable. It will not be used as a strict keyword-only inclusion requirement.

Date eligibility rule:

- If database filters retrieve the full 2026 publication year, records published or made available after June 30, 2026 will be excluded during date eligibility screening.
- Records with unclear day/month information will be flagged as `date_uncertain`.

### Exclusion Criteria

- Non-optical ISAC studies without an optical communication or optical sensing component.
- Pure communication studies with no sensing, localization, monitoring, imaging, detection, or perception component.
- Pure sensing studies with no integrated or co-designed communication component.
- Non-peer-reviewed grey literature in the main corpus, including theses, white papers, standards drafts, preprints without peer-reviewed version, slide decks, blog posts, patents, and vendor material.
- Non-English records.
- Records outside the planned search window.
- Book chapters or book sections are not part of the primary technical evidence corpus; if needed, they may be labeled contextual/background only.
- Studies for which the full text cannot be obtained after documented retrieval attempts.
- Duplicate records; the most complete peer-reviewed version will be retained.

### Corpus Distinction

**Durum:** complete

- Primary technical evidence corpus: peer-reviewed journal articles, early-access journal articles, and full-length conference/proceedings papers.
- Contextual corpus: review/survey papers and pre-2020 foundational studies used for background, terminology, taxonomy cross-checking, or technology lineage.
- Contextual records must not be counted as primary technical evidence.

### Pre-2020 Rule

**Durum:** complete

The primary systematic corpus is limited to January 1, 2020 - June 30, 2026. Pre-2020 foundational studies may be cited for background, terminology, or technology lineage, but will be labeled separately and excluded from primary technical evidence synthesis unless explicitly justified.

## 7. Information Sources

**Durum:** drafted / expanded source pool

Core primary databases:

- Scopus
- IEEE Xplore

Selected supplementary publisher/platform sources:

- ScienceDirect
- SpringerLink
- Wiley Online Library
- Taylor & Francis Online

Web of Science is not part of the current selected source set. It may be re-added only through a documented decision.

Formal information sources sentence:

> Information sources: The systematic search will be conducted in Scopus and IEEE Xplore as the primary bibliographic and engineering databases. Supplementary platform searches will be conducted in ScienceDirect, SpringerLink, Wiley Online Library, and Taylor & Francis Online. Web of Science and ACM Digital Library will not be included because institutional access was not available during the search planning stage.

Grey literature will be excluded from the main corpus. Grey literature may be noted only as contextual background if needed, but it will not be counted as eligible evidence in PRISMA flow, evidence tables, or synthesis conclusions.

## 8. Search Strategy Summary

**Durum:** drafted

Arama stratejisi O-ISAC kavram ailesini optik platform terimleriyle birlestirecek bicimde kurulacaktir. Nihai database-specific ve source-specific sorgular arama yurutulmeden once `02_arama/01_arama_plani.md`, `02_arama/database_source_pool.md` ve search log icinde ayrica izlenmelidir.

Core concept terms:

- "integrated sensing and communication"
- ISAC
- "joint communication and sensing"
- "joint sensing and communication"
- "dual-function communication and sensing"

Optical platform terms:

- optical
- fiber
- "free-space optical" OR FSO
- VLC
- LiFi
- photonic
- terahertz OR THz

Indicative query structure:

```text
("integrated sensing and communication" OR ISAC OR "joint communication and sensing" OR "joint sensing and communication" OR "dual-function communication and sensing")
AND
(optical OR fiber OR "free-space optical" OR FSO OR VLC OR LiFi OR photonic OR terahertz OR THz)
```

Limits:

- Language: English.
- Search window: January 1, 2020 - June 30, 2026.
- Source type: peer-reviewed journal articles and peer-reviewed conference papers.
- Main corpus: grey literature excluded.

## 9. Planned Search Freeze Date

**Durum:** complete

Planned search freeze date: June 30, 2026.

Arama gercekten yurutulene kadar bu ifade `planned search freeze date` olarak kalacaktir; `final search date` ifadesi kullanilmayacaktir.

## 10. Selection Process

**Durum:** drafted

- Records will be exported from Scopus, IEEE Xplore, ScienceDirect, SpringerLink, Wiley Online Library, and Taylor & Francis Online.
- Duplicates will be identified and removed before title/abstract screening.
- Title/abstract screening will apply the PCC-aligned inclusion and exclusion criteria.
- Full-text screening will confirm optical O-ISAC relevance, peer-review status, English language, date eligibility, and extractable evidence items.
- Exclusion reasons at full-text stage will be recorded in a traceable table.
- Disagreements or uncertain cases will be resolved by documented reviewer discussion or a senior methodological decision.
- AI-assisted screening or tagging may be used only as a support tool; final inclusion/exclusion decisions require human verification.

Screening decision categories:

- `include_primary`
- `include_contextual`
- `exclude`
- `unclear_full_text_needed`
- `duplicate`
- `date_uncertain`

## 11. Data Extraction Process

**Durum:** drafted

- A structured data extraction form will be used.
- Pilot extraction will be performed on a small sample before full extraction.
- Extraction fields will be revised only through documented protocol amendment or decision log entry.
- Missing or ambiguous information will be marked explicitly rather than inferred without support.
- Author contact may be considered for critical missing information, but the default synthesis will rely on information available in the peer-reviewed full text.

## 12. Data Items

**Durum:** drafted

Planned data extraction items:

- Bibliographic identity: author, year, title, venue, DOI, database source.
- Optical modality: fiber, FSO, VLC, LiFi, photonic-THz, hybrid optical systems, or other optical category.
- System architecture: transmitter/receiver design, waveform, modulation, optical front-end, network setting, co-design structure.
- Sensing task: localization, ranging, detection, imaging, monitoring, environmental perception, or other reported task.
- Communication metrics: data rate, BER, capacity, throughput, spectral efficiency, latency, SNR, OSNR, ESNR, link budget, coverage, or related metrics.
- Sensing metrics: range accuracy, localization error, detection probability, false alarm rate, resolution, CRB, FIM, estimation error, or related metrics.
- Rate-sensing tradeoff evidence: explicit tradeoff curve, optimization, constraint analysis, qualitative discussion, or absent.
- Metric comparability and comparison admissibility: directly comparable, conditionally comparable, not comparable, or descriptive only.
- Validation method: theory, simulation, numerical analysis, testbed, laboratory experiment, field experiment, prototype, dataset-based validation.
- Measurement plane: device/component, link, channel, network, application, or system-level plane.
- Application domain: 6G access, indoor positioning, vehicular, industrial, security, environment monitoring, underwater, aerospace, or other.
- 6G relevance: direct, inferred, weak, or not applicable.
- Enabling technologies: beamforming, MIMO, OFDM, coherent optics, photonic integration, ML/AI, reconfigurable surfaces, digital twins, or other.
- Benchmark readiness: dataset availability, repeatable parameters, code/model availability, baseline comparison, standardized metrics, reproducibility indicators.
- Limitations and research gaps reported by the authors.
- Funding and conflicts of interest where reported.

### 12A. Metric Comparability Adjudication Rule

**Durum:** drafted

Metric comparability will be adjudicated with four final categories:

| Category | Decision rule |
|---|---|
| directly comparable | Same metric, same measurement plane, similar scenario, and similar validation condition. |
| conditionally comparable | Same general metric family but different scenario or assumption; comparison is possible only when conditions are explicitly stated. |
| not comparable | Metric name may be similar, but measurement plane, definition, or validation context differs. |
| descriptive only | The study reports a metric, but information is insufficient for numerical or operational comparison. |

Uncertain cases will be resolved through reviewer notes and adjudication before assigning the final metric comparability label.

## 13. TQAF-Style Technical Quality Assessment

**Durum:** drafted

TQAF-style technical quality assessment will qualify evidence strength rather than automatically exclude studies. The assessment will focus on technical reporting and validation maturity, not only generic methodological quality.

Planned assessment dimensions:

- O-ISAC problem definition clarity.
- Optical modality and system architecture reporting completeness.
- Communication metric reporting completeness.
- Sensing metric reporting completeness.
- Rate-sensing tradeoff reporting.
- Validation maturity and reproducibility.
- Benchmark readiness.
- Baseline or comparator adequacy.
- Assumption transparency.
- Limitation reporting.

Each study will be assigned a qualitative technical evidence strength label such as high, moderate, limited, or unclear, with reasons recorded in the extraction or quality table.

## 14. Synthesis Approach

**Durum:** drafted

The synthesis will combine:

- Structured narrative synthesis.
- Scoping-style taxonomy mapping.
- Evidence tabulation.
- Metric comparability and comparison admissibility assessment.
- Metric-governed comparison.
- Validation maturity mapping.
- Benchmark readiness assessment.
- Research roadmap synthesis.

The synthesis will avoid unsupported direct numerical pooling across incompatible optical modalities. Cross-modality interpretation will be governed by what each study reports about metrics, validation plane, assumptions, and benchmark readiness.

## 15. No Meta-Analysis Justification

**Durum:** complete

**Required manuscript-ready method sentence:**

Meta-analysis was not planned because the eligible O-ISAC literature is expected to be heterogeneous across optical modality, system architecture, sensing task, communication metric, sensing metric, validation method, and measurement plane. Therefore, the study will use structured narrative synthesis, taxonomy mapping, metric-governed comparison, and evidence-tabulation methods.

## 16. Handling of Review/Survey Papers and Contextual Records

**Durum:** complete

Review and survey papers will not be included as primary evidence in the main corpus. They may be used contextually to identify terminology, background framing, taxonomy cross-checks, and potential seed references, but they will not contribute study-level technical evidence, metric comparison, validation maturity scoring, or benchmark readiness conclusions.

If a review/survey identifies potentially eligible primary studies, those primary studies must be independently retrieved, screened, and assessed under the same eligibility criteria.

Pre-2020 foundational studies may be cited for background, terminology, or technology lineage, but they must be labeled separately and excluded from primary technical evidence synthesis unless explicitly justified.

## 17. Handling of Low-Quality Studies

**Durum:** complete

Low methodological/reporting quality will not automatically exclude a study if it otherwise meets eligibility criteria. Instead, technical evidence strength will be qualified using the TQAF-style assessment. Low-quality, incomplete, or weakly validated studies may remain in the map but will be clearly marked so that synthesis claims do not overstate their evidential weight.

## 18. Registration and Internal Protocol

**Durum:** complete

External registration is not planned unless required by the target journal. An internal protocol, decision log, and progress tracker will be maintained before search execution and updated through documented amendments.

## 19. Reporting Standards

**Durum:** drafted

The review will follow PRISMA 2020 reporting principles. Search reporting should also remain compatible with PRISMA-S style transparency where feasible, especially for database names, search dates, query strings, limits, deduplication, and record management.

## 20. Protocol Amendments

**Durum:** complete

All protocol amendments after this draft must be recorded in `09_kayitlar/decision_log.md` with date, stage, decision, rationale, expected impact, and responsible actor.

Amendments requiring explicit tracking include:

- Search window changes.
- Planned search freeze date changes.
- Database additions or removals.
- Eligibility criteria changes.
- Review/survey handling changes.
- Grey literature handling changes.
- Data item changes.
- TQAF-style assessment changes.
- Synthesis approach changes.
- Any shift from planned narrative synthesis to another synthesis method.

## 21. Current TODO Items Before Search Execution

- Finalize database-specific search strings for Scopus and IEEE Xplore.
- Finalize source-specific search strings for ScienceDirect, SpringerLink, Wiley Online Library, and Taylor & Francis Online.
- Decide whether search strategy peer review will be performed.
- Create or update the structured data extraction table for O-ISAC-specific fields.
- Create or update the TQAF-style technical quality assessment table.
- Define exact duplicate-removal workflow and record-management tool.
- Run pilot screening and pilot extraction before full screening/extraction.
- Record the actual search execution date only after searches are performed.
