# 02 - O-ISAC Protokol Kontrol Listesi

Bu kontrol listesi, O-ISAC PRISMA review protokolundeki alanlarin durumunu izlemek icindir. Tamamlanan kararlar `complete`, manuscript/metod taslak duzeyinde hazir olan alanlar `drafted`, arama veya uygulama once tamamlanmasi gereken isler `TODO` olarak isaretlenmistir.

## Zorunlu Protokol Alanlari

| Alan | Durum | Not |
|---|---|---|
| Review type | complete | PRISMA-grounded narrative systematic review with a scoping-style PCC component. |
| Background/rationale | drafted | O-ISAC heterojenligi, cross-modality metric reporting, validation maturity ve benchmark readiness gerekcesi yazildi. |
| Objectives | drafted | Ana amac ve ana research question English olarak yazildi. |
| RQ1-RQ7 | complete | Taxonomy, metric reporting, metric comparability / comparison admissibility, rate-sensing tradeoff, enabling technologies/applications, validation maturity/benchmark readiness ve research gaps/6G roadmap tanimli. |
| Operational definition | complete | O-ISAC operational definition English olarak eklendi. |
| PCC framework | complete | PCC, PICO/PECO/PICo yerine secildi. |
| Eligibility criteria | drafted | Inclusion/exclusion kriterleri O-ISAC, peer review, English, search window ve grey literature dislama kararlarina gore yazildi. |
| Corpus distinction | complete | Primary technical evidence corpus ile contextual corpus ayrildi; contextual records primary technical evidence sayilmayacak. |
| Pre-2020 rule | complete | Pre-2020 foundational studies background/terminology/lineage icin ayri etiketlenecek; primary synthesis'e dahil edilmeyecek. |
| 6G relevance coding | complete | 6G relevance direct / inferred / weak / not applicable olarak kodlanacak; strict keyword-only inclusion requirement degil. |
| Screening decision categories | drafted | include_primary, include_contextual, exclude, unclear_full_text_needed, duplicate, date_uncertain. |
| Registration/protocol decision | complete | External registration target journal gerektirmedikce planlanmiyor; internal protocol, decision log ve progress tracker surdurulecek. |
| Information sources | drafted / selected source set updated | Scopus ve IEEE Xplore core; ScienceDirect, SpringerLink, Wiley Online Library ve Taylor & Francis Online supplementary publisher/platform search olarak kullanilacak. Web of Science ve ACM Digital Library institutional access olmadigi icin dahil edilmeyecek. |
| Search strategy summary | drafted | Ana kavram aileleri ve indicative query structure yazildi. |
| Planned search freeze date | complete | Planned search freeze date: June 30, 2026. |
| Selection process | drafted | Deduplication, title/abstract screening, full-text screening, disagreement handling ve AI destek siniri yazildi. |
| Data extraction process | drafted | Structured form, pilot extraction ve missing data yaklasimi yazildi. |
| Data items | drafted | Bibliographic, modality, architecture, metric, validation, benchmark readiness ve gap alanlari yazildi. |
| Primary synthesis domains | complete | O-ISAC modality taxonomy, architecture/integration mechanisms, communication metric reporting, sensing metric reporting, measurement-plane mapping, metric comparability, rate-sensing tradeoff, validation maturity, benchmark readiness ve research gaps/6G roadmap tanimli. |
| TQAF-style technical quality assessment | drafted | Teknik kanit gucu boyutlari ve nitel etiketleme yaklasimi yazildi. |
| Synthesis approach | drafted | Structured narrative synthesis, taxonomy mapping, evidence tabulation, metric-governed comparison, validation maturity mapping, benchmark readiness assessment ve roadmap synthesis yazildi. |
| No meta-analysis justification | complete | Zorunlu English method cumlesi protokole aynen eklendi. |
| Handling of review/survey papers | complete | Reviews/surveys contextual only olarak tanimlandi. |
| Handling of low-quality studies | complete | Otomatik dislama yok; TQAF-style assessment ile kanit gucu nitelendirilecek. |
| Protocol amendments | complete | Degisiklikler decision_log.md icinde tarihli kaydedilecek. |

## Search Oncesi TODO Listesi

- [TODO] Scopus icin database-specific nihai sorgu yazilacak.
- [TODO] IEEE Xplore icin database-specific nihai sorgu yazilacak.
- [TODO] ScienceDirect icin source-specific nihai sorgu yazilacak.
- [TODO] SpringerLink icin source-specific nihai sorgu yazilacak.
- [TODO] Wiley Online Library icin source-specific nihai sorgu yazilacak.
- [TODO] Taylor & Francis Online icin source-specific nihai sorgu yazilacak.
- [TODO] Secili supplementary kaynaklar icin limit, export ve deduplication kayit kurallari yazilacak.
- [TODO] Arama stratejisi peer review yapilip yapilmayacagi netlestirilecek.
- [TODO] Record-management ve duplicate-removal araci/sureci netlestirilecek.
- [TODO] `date_uncertain` kayitlari icin gun/ay belirsizligi karar kurali netlestirilecek.
- [TODO] 6G relevance coding icin direct / inferred / weak / not applicable karar ornekleri pilot screening oncesi netlestirilecek.
- [TODO] Pilot title/abstract screening yapilacak.
- [TODO] Pilot full-text screening yapilacak.
- [TODO] O-ISAC-specific structured data extraction table guncellenecek.
- [TODO] Pilot data extraction yapilacak.
- [TODO] TQAF-style technical quality assessment table guncellenecek.
- [TODO] Fiili arama yapildiktan sonra actual search date kaydedilecek.
- [TODO] Full-text erisim sorunlari icin kayit yontemi uygulanacak.

## Kirmizi Bayrak Kontrolu

| Kirmizi bayrak | Durum | Not |
|---|---|---|
| Soru cok genis | drafted | PCC ile kapsam genis ama taxonomy/metric/validation eksenlerinde yonetiliyor; pilot screening sonrasi tekrar kontrol edilecek. |
| Primary synthesis domains belirsiz | drafted | Klinik outcome yerine O-ISAC metric families, metric comparability, comparison admissibility ve data items tanimlandi. |
| Dahil/disla kriterleri yoruma cok acik | drafted | Kriterler yazildi; pilot screening sonrasi netlestirme gerekebilir. |
| Arama sorgusu tek kelime ailesine dayaniyor | drafted | ISAC ve optical platform terimleri birlikte kullanildi; nihai database sorgulari TODO. |
| Calisma tasarimlari belirsiz | complete | Primary technical evidence corpus peer-reviewed journal, early-access journal ve full-length conference/proceedings papers; contextual corpus ayri. |
| Sentez yontemi kapsamla uyumsuz | complete | Meta-analysis yerine structured narrative synthesis ve metric-governed comparison planlandi. |
| Kalite degerlendirme yaklasimi uygun degil | drafted | Klinik RoB yerine TQAF-style technical quality assessment planlandi; tablo TODO. |
| Protokol sonrasi degisiklik kaydi yok | complete | decision_log.md kullanilacak. |

## Onay Durumu

Protokol surumu: drafted O-ISAC PRISMA protocol

Tarih: 2026-06-17

Devam karari:

- [ ] Aramaya gecilebilir.
- [x] Once TODO isleri tamamlanmali.

Not:

Protokol ana metodolojik kararlar acisindan drafted/complete durumdadir; fiili arama, nihai database sorgulari, pilot screening, pilot extraction ve TQAF tablosu tamamlanmadan search execution baslatilmamalidir.
