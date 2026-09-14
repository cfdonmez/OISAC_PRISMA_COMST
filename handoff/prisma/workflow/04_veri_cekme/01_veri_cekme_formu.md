# 01 - Veri Cekme Formu

Bu form, Optical Integrated Sensing and Communication (O-ISAC) for 6G calismasi icin PRISMA-grounded narrative systematic review ve scoping-style PCC component baglaminda kullanilacaktir.

## Kullanim Notlari

- Search window: January 1, 2020 - June 30, 2026.
- Search freeze date, arama gercekten yurutulene kadar `planned search freeze date: June 30, 2026` olarak tutulur.
- Core primary databases: Scopus, IEEE Xplore.
- Selected supplementary sources: ScienceDirect, SpringerLink, Wiley Online Library, Taylor & Francis Online.
- Language: English only.
- Form once 3-5 calisma uzerinde pilot olarak denenir; alan tanimlari veya CSV basliklari gerekiyorsa pilot sonrasi izlenebilir sekilde guncellenir.
- Veri cekme, calismanin hem teknik kanit degerini hem de scoping-style taxonomy mapping icindeki yerini gosterecek sekilde yapilir.
- Author contact generally not expected; ancak kritik missing data yayin veya supplementary material icinden cozumlenemezse author_contact_log.csv icinde kayit alani korunur.
- Primary technical evidence corpus: peer-reviewed journal articles, early-access journal articles, and full-length conference/proceedings papers.
- Contextual corpus: review/survey papers and pre-2020 foundational studies; contextual records primary technical evidence sayilmaz.
- If database filters retrieve the full 2026 publication year, records published or made available after June 30, 2026 will be excluded during date eligibility screening; unclear day/month information is coded as `date_uncertain`.

## A. Kaynak ve Kimlik Bilgileri

- Study ID:
- Citation:
- Title:
- Authors:
- Venue:
- DOI:
- Year:
- Publication available date:
- Date eligibility status: eligible / after_2026_06_30 / date_uncertain / unclear
- Database source: Scopus / IEEE Xplore / ScienceDirect / SpringerLink / Wiley Online Library / Taylor & Francis Online / other
- Full text source:
- Document type: journal article / conference paper / early access / review / survey / other
- Extractor ID:
- Extraction date:
- Verifier ID:
- Verification status: not_checked / verified / needs_revision / conflict
- Corpus role: primary technical evidence / contextual / excluded / mixed_to_resolve
- Contextual use reason: background / terminology / taxonomy cross-checking / technology lineage / seed reference / not applicable
- 6G relevance code: direct / inferred / weak / not applicable

## B. Optical Modality ve Mimari

- Optical modality: fiber / FSO / VLC-LiFi / photonic-THz / hybrid / other
- System architecture:
- Integration mechanism:
- Shared hardware/waveform/resource:

## C. Sensing ve Communication Ozellikleri

- Sensing task:
- Communication function:
- Communication metrics:
- Sensing metrics:
- Measurement plane:
- Rate-sensing tradeoff reported: yes / partial / no / unclear
- CRB/FIM reported: yes / no / unclear
- OSNR/SNR/ESNR reported: OSNR / SNR / ESNR / multiple / not reported / unclear

## D. Validation, Scenario ve Uygulama Baglami

- Validation type: analytical / simulation / experiment / prototype / field / mixed
- Scenario/environment:
- Application domain:
- Enabling technologies: ORIS / OPA / PIC / photonic-THz / ML-assisted adaptation / other

## E. Karsilastirilabilirlik ve Benchmark Readiness

- Metric comparability status: directly comparable / conditionally comparable / not comparable / descriptive only
- Comparison admissibility: admissible / conditionally admissible / not admissible / not enough information
- Benchmark readiness:
- Reporting completeness:
- Reproducibility notes:
- TQAF-style assessment notes:

Metric comparability adjudication rule:

| Kategori | Karar kurali |
|---|---|
| directly comparable | Ayni metrik, ayni measurement plane, benzer scenario ve benzer validation condition vardir. |
| conditionally comparable | Ayni genel metrik ailesi vardir, fakat scenario veya assumption farklidir; karsilastirma yalnizca kosullar belirtilerek yapilabilir. |
| not comparable | Metrik adi benzer olsa bile measurement plane, definition veya validation context farklidir. |
| descriptive only | Calisma metrik raporlar, fakat sayisal veya operasyonel karsilastirma icin yeterli bilgi yoktur. |

Belirsiz durumlarda reviewer notu ve adjudication karari tutulur; final metric comparability etiketi yukaridaki dort kategoriden biri olmalidir.

TQAF skorlamasi extraction baslamadan once sabitlenmistir:

- 0 = not reported / insufficient
- 1 = weak or incomplete
- 2 = adequate
- 3 = strong / benchmark-ready
- NA = not applicable

Study-level TQAF alanlari `risk_of_bias.csv` icinde su basliklarla skorlanir: technical relevance, metric clarity, reporting completeness, validation maturity, reproducibility, benchmark readiness, comparison admissibility, limitation transparency, overall evidence contribution. Bu skorlar daha sonra high / moderate / limited / unclear nitel etiketlerine donusturulebilir.

## F. Eksik Veri ve Karar Notlari

- Eksik veri:
- Varsayim:
- Hesaplanan/tahmin edilen veri:
- Missing data icin yazarla iletisim gerekli mi:
- Veri cekme notu:
