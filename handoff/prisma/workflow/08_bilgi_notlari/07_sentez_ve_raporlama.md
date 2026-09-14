# Bilgi Notu 07 - Sentez ve Raporlama

Bu review icin sentez, O-ISAC literaturunu sadece calisma ozetleri halinde siralamak yerine modality, architecture, metric reporting, tradeoff, validation maturity ve benchmark readiness eksenlerinde yapilandirir. Meta-analysis planlanmamistir.

## Planlanan Sentez Yaklasimi

- structured narrative synthesis
- scoping-style taxonomy mapping
- modality-specific evidence mapping
- metric-governed comparison
- rate–sensing tradeoff synthesis
- validation maturity mapping
- benchmark readiness assessment
- research roadmap synthesis

## Neden Meta-Analiz Planlanmiyor?

O-ISAC literaturu optical modality, system architecture, sensing task, communication metric, sensing metric, validation method ve measurement plane acisindan heterojendir. Bu nedenle calismalari tek bir etki olcusunde birlestirmek yerine, kanitlar onceden tanimli sentez basliklari altinda anlatimli ve tablolu olarak degerlendirilecektir.

## Ana Sentez Basliklari

| Kod | Baslik | Raporlama amaci |
|---|---|---|
| S1 | O-ISAC modality taxonomy | Fiber, FSO, VLC/LiFi, photonic-THz ve hybrid optical systems ayrimini netlestirmek |
| S2 | Architecture and integration mechanism synthesis | O-ISAC entegrasyon kaliplarini ve sistem mimarilerini ozetlemek |
| S3 | Sensing/communication metric reporting map | Hangi metriklerin hangi kosullarla raporlandigini gostermek |
| S4 | Rate–sensing and rate–resolution tradeoff synthesis | Communication rate ile sensing accuracy/resolution arasindaki tradeoff kanitlarini yorumlamak |
| S5 | Validation maturity and benchmark readiness | Kanitin simulation, prototype, field trial ve benchmark hazirligi duzeyini haritalamak |
| S6 | Enabling technologies and application domains | 6G O-ISAC icin teknoloji ve uygulama alanlarini gostermek |
| S7 | Research gaps and 6G roadmap | Kalan bosluklari ve gelecek arastirma yonlerini sentezlemek |

## Metric Comparability Classes

| Sinif | Karar kurali |
|---|---|
| directly comparable | Ayni metrik, ayni measurement plane, benzer scenario ve benzer validation condition vardir |
| conditionally comparable | Ayni genel metrik ailesi vardir, fakat scenario veya assumption farklidir; karsilastirma yalnizca kosullar belirtilerek yapilabilir |
| not comparable | Metrik adi benzer olsa bile measurement plane, definition veya validation context farklidir |
| descriptive only | Calisma metrik raporlar, fakat sayisal veya operasyonel karsilastirma icin yeterli bilgi yoktur |

Bu siniflar, calismalari zorla karsilastirmak icin degil, karsilastirmanin sinirlarini seffaf gostermek icin kullanilacaktir. Belirsiz durumlarda reviewer/adjudication notu tutulur; final metric comparability etiketi bu dort kategoriden biri olur.

## Raporlama Disiplini

- Search ve screening tamamlanmadan kayit sayisi yazilmaz.
- Sentez sonuclari sadece veri cikarma tamamlandiktan sonra yazilir.
- Dusuk methodological/reporting quality tek basina dislama nedeni yapilmaz.
- TQAF-style technical quality assessment, kanit gucunu nitelendirmek icin kullanilir.
- Manuscript-ready bolumler English yazilir.
- Workflow notlari, karar gerekceleri ve ara aciklamalar Turkce tutulur.

## Manuscript Sonuc Bolumlerine Esleme

| Manuscript bolumu | Ilgili sentez |
|---|---|
| 4.3 Taxonomy of O-ISAC modalities | S1 |
| 4.4 Architecture and integration mechanisms | S2 |
| 4.5 Sensing and communication metric reporting | S3 |
| 4.6 Rate-sensing tradeoffs | S4 |
| 4.7 Validation maturity and benchmark readiness | S5 |
| 5.3 Enabling technologies | S6 |
| 6. Research Roadmap | S7 |

## Teslimden Once Kontrol

1. `synthesis_matrix.csv` S1-S7 icin dolduruldu mu?
2. Comparability status her sentez alaninda acik mi?
3. Validation maturity ve benchmark readiness ayri ayri raporlandi mi?
4. PRISMA flow counts gercek verilere dayaniyor mu?
5. Result ve discussion bolumlerinde uydurma sonuc yok mu?
