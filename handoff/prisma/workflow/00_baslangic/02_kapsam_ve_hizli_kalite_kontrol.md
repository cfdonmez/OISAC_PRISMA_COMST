# 02 - Kapsam ve Hizli Kalite Kontrol

Bu dosya, O-ISAC PRISMA calismasinin kapsam olarak cok genis veya cok dar kalmamasini ve kalite kararlarinin review amaciyla uyumlu tutulmasini saglar. Workflow notlari Turkce, manuscript-ready akademik ifadeler English yazilir.

## 1. Kapsam Ozeti

Calisma konusu:

- Optical Integrated Sensing and Communication (O-ISAC) for 6G.

Review tipi:

- PRISMA-grounded narrative systematic review with a scoping-style PCC component.

Framework:

- PCC - Population / Concept / Context.

Kapsam dahilindeki optical modalities:

- Fiber.
- FSO.
- VLC/LiFi.
- Photonic-THz.
- Hybrid optical systems.

Search window:

- January 1, 2020 - June 30, 2026.

Search freeze date:

- planned search freeze date: June 30, 2026.

O-ISAC operational definition:

> In this review, O-ISAC refers to optical or photonic systems in which sensing and communication functions are jointly considered, integrated, co-designed, co-optimized, or evaluated within the same architecture, optical link, waveform/resource framework, hardware platform, channel model, or application scenario.

Corpus distinction:

- Primary technical evidence corpus: peer-reviewed journal articles, early-access journal articles, and full-length conference/proceedings papers.
- Contextual corpus: review/survey papers and pre-2020 foundational studies used for background, terminology, taxonomy cross-checking, or technology lineage.
- Contextual records must not be counted as primary technical evidence.

Pre-2020 rule:

- The primary systematic corpus is limited to January 1, 2020 - June 30, 2026.
- Pre-2020 foundational studies may be cited for background, terminology, or technology lineage, but will be labeled separately and excluded from primary technical evidence synthesis unless explicitly justified.

## 2. PCC Kapsam Testi

1. Population net mi?
   - Peer-reviewed studies on Optical Integrated Sensing and Communication / O-ISAC systems.
2. Concept net mi?
   - Taxonomy, metric reporting, metric comparability, comparison admissibility, rate-sensing tradeoff synthesis, validation maturity ve benchmark readiness.
3. Context net mi?
   - 6G-oriented optical platforms: fiber, FSO, VLC/LiFi, photonic-THz ve hybrid optical systems.
4. PICO comparator gerekmiyor mu?
   - Evet. Bu calisma intervention-effect sorusu degildir; karsilastirma modaliteler, metrikler, validation types ve reporting completeness uzerinden yapilir.
5. Primary synthesis domains veri cekme tablosuna kodlanabilir mi?
   - Evet: O-ISAC modality taxonomy, architecture and integration mechanisms, communication metric reporting, sensing metric reporting, measurement-plane mapping, metric comparability, rate-sensing tradeoff, validation maturity, benchmark readiness ve research gaps / 6G roadmap kodlanabilir.
6. Meta-analysis icin heterojenlik gerekcesi acik mi?
   - Evet. Optical modality, system architecture, sensing task, communication metric, sensing metric, validation method ve measurement plane heterojendir.
7. Review katki noktasi PRISMA-grounded ve 6G odakli mi?
   - Evet. Calisma structured narrative synthesis ve scoping-style mapping ile alanin karsilastirilabilirligini artirmayi hedefler.

## 3. Kapsam Daraltma Kollari

Kayit sayisi cok fazla cikarsa sirayla sunlar degerlendirilir:

- Search query icinde O-ISAC / optical ISAC / integrated sensing and communication terimlerinin optik baglamla birlikte gecmesini zorunlu tut.
- 6G relevance kodlamasini direct / inferred / weak / not applicable olarak daha belirgin hale getir; strict keyword-only inclusion requirement yapma.
- Optical modality disi kayitlari disla; RF-only ISAC sonuclari kapsama alma.
- Outcome aramasini communication metric + sensing metric raporlamasina yakinlastir.
- Review, survey ve perspective makalelerini ana veri setinden ayir; gerekirse yalnizca background/context icin kullan.
- Search window kararini degistirme; January 1, 2020 - June 30, 2026 araligi korunur.
- Dahil edilen calismalarda en az taxonomy coding veya validation maturity coding yapilabilecek teknik bilgi bulunmasini zorunlu tut.

## 4. Kapsam Genisletme Kollari

Kayit sayisi cok az cikarsa sirayla sunlar degerlendirilir:

- O-ISAC es anlamli terimlerini genislet: optical ISAC, optical integrated sensing and communication, integrated optical sensing and communication, joint communication and sensing, joint sensing and communication.
- Modality terimlerini genislet: fiber-optic, optical fiber, FSO, free-space optical, VLC, visible light communication, LiFi, photonic THz, terahertz photonics, hybrid optical.
- Sensing task terimlerini genislet: localization, positioning, ranging, detection, monitoring, imaging, perception, channel sensing.
- Communication metric terimlerini arama sorgusunda daha gevsek kullan; metrikleri veri cekme asamasinda kodla.
- Backward/forward citation chasing ve included studies reference checks kullanmayi planla.
- Core primary databases disinda supplementary arama kaynaklari gerekiyorsa bunu protokolde ayrica gerekcelendir.

## 5. Hizli Kalite ve Raporlama Kontrolu

Dusuk methodological/reporting quality tek basina dislama nedeni degildir. Uygunluk karari once konu ve kapsam uygunluguna gore verilir; teknik kanit gucu daha sonra TQAF-style technical quality assessment ile nitelendirilir.

Hizli kontrol sorulari:

1. Calisma O-ISAC veya optik communication-sensing integration ile dogrudan ilgili mi?
2. Hedef optical modalities icinden en az birine giriyor mu?
3. Communication ve sensing taraflari birlikte ele aliniyor mu?
4. Sensing task ve communication function aciklanmis mi?
5. En az bir communication metric veya communication-relevant performance indicator raporlanmis mi?
6. En az bir sensing metric veya sensing-relevant performance indicator raporlanmis mi?
7. Validation type belirlenebiliyor mu?
8. Measurement plane veya evaluation environment kodlanabiliyor mu?
9. Rate-sensing tradeoff acikca analiz edilmis, ima edilmis veya veri uzerinden tartisilabilir mi?
10. Benchmark readiness veya reproducibility acisindan veri, kod, testbed, parameter set veya karsilastirma zemini var mi?

6G relevance coding:

- direct
- inferred
- weak
- not applicable

Date eligibility rule:

- If database filters retrieve the full 2026 publication year, records published or made available after June 30, 2026 will be excluded during date eligibility screening.
- Records with unclear day/month information will be flagged as `date_uncertain`.

Screening decision categories:

- `include_primary`
- `include_contextual`
- `exclude`
- `unclear_full_text_needed`
- `duplicate`
- `date_uncertain`

## 6. TQAF-Style Technical Quality Sinyalleri

Veri cekme ve kalite degerlendirmesinde su sinyaller izlenir:

- Problem definition clarity.
- O-ISAC integration clarity.
- Optical modality and architecture clarity.
- Communication metric completeness.
- Sensing metric completeness.
- Rate-sensing tradeoff reporting.
- Validation method maturity.
- Baseline or comparator-of-reporting availability.
- Reproducibility support: dataset, code, parameter set, testbed detail.
- Limitation reporting.
- 6G relevance and deployment plausibility.

Bu sinyaller dislama icin otomatik esik degildir; evidence strength ve reporting completeness yorumunu desteklemek icin kullanilir.

## 7. Sentez Uygunlugu

Planlanan sentez yaklasimi:

- Structured narrative synthesis.
- Scoping-style taxonomy mapping.
- Evidence tabulation.
- Metric-governed comparison.
- Validation maturity mapping.
- Benchmark readiness assessment.
- Research roadmap synthesis.

Manuscript-ready synthesis statement (English):

> Because O-ISAC studies differ across optical modality, architecture, sensing task, communication metric, sensing metric, validation method, and measurement plane, the review will not perform a meta-analysis. Instead, evidence will be synthesized through structured narrative synthesis, scoping-style taxonomy mapping, metric-governed comparison, validation maturity mapping, benchmark readiness assessment, and research roadmap synthesis.

## 8. Devam/Kilit Karari

- [x] Soru PCC framework ile net.
- [x] Kapsam fiber, FSO, VLC/LiFi, photonic-THz ve hybrid optical systems olarak tanimli.
- [x] Search window tanimli: January 1, 2020 - June 30, 2026.
- [x] Search freeze date planli olarak etiketli: planned search freeze date: June 30, 2026.
- [x] Meta-analysis yapilmama gerekcesi tanimli.
- [x] Katki gerekcesi taxonomy, metric-governed comparison, rate-sensing tradeoff synthesis, validation maturity, benchmark readiness ve roadmap uzerinden tanimli.
- [x] Corpus distinction tanimli: primary technical evidence ve contextual corpus ayrildi.
- [x] 6G relevance strict keyword-only inclusion requirement degil; direct / inferred / weak / not applicable olarak kodlanacak.
- [x] Date eligibility rule tanimli; June 30, 2026 sonrasi 2026 kayitlari dislanacak, belirsiz tarih `date_uncertain` olacak.
- [x] RQ1-RQ7 yapisi tanimli; RQ3 metric comparability / comparison admissibility icin ayrildi.
- [x] Registration/protocol decision tanimli; external registration target journal gerektirmedikce planlanmiyor.
- [x] Protokol yazimina gecilebilir.

Karar:

- Baslangic kapsam kilidi O-ISAC for 6G uzerinden yapildi. PICO yerine PCC kullanilacak. Search fiilen yurutulene kadar search freeze tarihi planli tarih olarak kalacak.

Gerekce:

- Alandaki heterojenlik nicel pooling yerine structured narrative synthesis ve scoping-style mapping gerektiriyor. Buna ragmen PRISMA-grounded workflow, search, eligibility, screening, data extraction ve reporting kararlarinin izlenebilir kalmasini saglayacak.
