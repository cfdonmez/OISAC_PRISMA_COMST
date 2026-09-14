# 01 - Tarama ve Secim Talimati

Bu talimat, O-ISAC icin PRISMA-grounded narrative systematic review ve scoping-style PCC component kapsaminda baslik/ozet taramasi ile tam metin uygunluk degerlendirmesinde ayni kurallari uygulamak icin kullanilir.

Kaynak baglam:

- Population: peer-reviewed O-ISAC / Optical Integrated Sensing and Communication calismalari.
- Concept: cross-modality O-ISAC architectures, taxonomy, sensing/communication metric reporting, rate-sensing tradeoff synthesis, validation maturity ve benchmark readiness.
- Context: 6G-oriented fiber, FSO, VLC/LiFi, photonic-THz ve hybrid optical communication-sensing systems.
- Search window: January 1, 2020 - June 30, 2026.
- Search freeze date: planned search freeze date: June 30, 2026.
- Language: English only.

Date filter notu: Database year filters may retrieve all 2026 records; records published or made available after June 30, 2026 will be excluded during date eligibility screening.

O-ISAC operational definition:

> In this review, O-ISAC refers to optical or photonic systems in which sensing and communication functions are jointly considered, integrated, co-designed, co-optimized, or evaluated within the same architecture, optical link, waveform/resource framework, hardware platform, channel model, or application scenario.

Corpus distinction:

- Primary technical evidence corpus: peer-reviewed journal articles, early-access journal articles, and full-length conference/proceedings papers.
- Contextual corpus: review/survey papers and pre-2020 foundational studies used only for background, terminology, taxonomy cross-checking, or technology lineage.
- Contextual records must not be counted as primary technical evidence.

## 1. Inclusion Criteria

Bir kayit, asagidaki kosullari karsiliyorsa full-text eligibility icin veya nihai dahil etme icin uygun adaydir:

1. Ana corpus icin calisma peer-reviewed journal article, early-access journal article veya full-length conference/proceedings paper niteligindedir. Book chapter ana corpus'a dahil edilmez; yalnizca gerekli gorulurse contextual/background olarak etiketlenir, aksi halde cikarilir.
2. Calisma English dilindedir.
3. Calisma January 1, 2020 - June 30, 2026 search window icindedir; foundational pre-2020 kaynaklar yalnizca "other sources/foundational pre-2020" olarak ayri izlenir.
4. Calisma optical/photonic component iceren O-ISAC, optical ISAC, joint optical sensing and communication veya communication-enabled optical sensing yaklasimi sunar.
5. En az bir optical modality ile iliskilidir: fiber, FSO, VLC/LiFi, photonic-THz veya hybrid optical systems.
6. Hem sensing hem communication tarafina iliskin integrated objective, architecture, evaluation, metric, tradeoff veya validation unsuru icerir.
7. Primary technical evidence olarak kullanilacak calismalarda teknik veri cikarimina uygun alan bulunur: sistem mimarisi, sensing task, communication metric, sensing metric, validation method, measurement plane, rate-sensing tradeoff veya benchmark/validation bilgisi.

## 2. Exclusion Criteria

Bir kayit, asagidaki durumlardan biri ana neden olarak gecerlise dislanir. Dusuk methodological/reporting quality tek basina dislama nedeni degildir; bu durum TQAF-style technical quality assessment ile kanit gucu olarak nitelendirilir.

| Code | Exclusion reason |
| --- | --- |
| E1 | RF-only ISAC, optical/photonic component yok |
| E2 | Pure optical communication, sensing relevance yok |
| E3 | Pure sensing/LiDAR, communication relevance yok |
| E4 | Optical link yalnizca auxiliary alignment/maintenance icin kullanilmis ve ISAC objective yok |
| E5 | Peer-reviewed degil |
| E6 | Short abstract/poster/editorial/opinion |
| E7 | English degil |
| E8 | Full text erisilemedi |
| E9 | Extraction icin kullanilabilir teknik alan yok |
| E10 | Duplicate record |
| E11 | Book chapter veya kitap bolumu; ana corpus icin uygun degil, yalnizca contextual/background olarak tutulabilir |

## 3. Title/Abstract Screening Rules

Amac, acikca uygun olmayan kayitlari elemek ve belirsiz kayitlari tam metne tasimaktir.

Kararlar:

- `include_primary`: Kayit primary technical evidence corpus icin uygun adaydir; tam metin degerlendirmesine gider.
- `include_contextual`: Kayit review/survey veya pre-2020 foundational/contextual role icin uygun adaydir; primary technical evidence sayilmaz.
- `exclude`: Kayit exclusion criteria kapsaminda acikca uygun degildir; uygun exclusion code atanir.
- `unclear_full_text_needed`: Baslik/ozet belirsizdir, ancak optical modality, sensing veya communication entegrasyonu ihtimali vardir; tam metne gider veya ikinci degerlendiriciye isaretlenir.
- `duplicate`: Ayni kaydin veya ayni calismanin duplicate versiyonudur.
- `date_uncertain`: Gun/ay bilgisi belirsizdir veya 2026 icinde June 30 cutoff kontrolu icin netlestirme gerekir.

`study_selection_log.csv` icinde title/abstract ve full-text secim sureci reviewer1_decision, reviewer2_decision, conflict_status, adjudication_decision ve final_corpus_role alanlariyla izlenir. `corpus_role_candidate`, `six_g_relevance_candidate`, `publication_available_date` ve `date_eligibility_status` alanlari nihai karar oncesi aday kodlamayi denetlenebilir tutmak icin kullanilir.

Baslik/ozet kurallari:

1. Suphe varsa baslik/ozette eleme; tam metne tasima daha guvenlidir.
2. Abstract sadece communication performansi anlatiyor ve sensing relevance belirtmiyorsa `E2` dusunulur.
3. Abstract sadece sensing/LiDAR anlatiyor ve communication relevance belirtmiyorsa `E3` dusunulur.
4. RF-only ISAC kayitlari optical/photonic component icermiyorsa `E1` ile dislanir.
5. Optical beam tracking/alignment calismalari yalnizca integrated sensing-and-communication objective, evaluation veya metric iceriyorsa dahil edilebilir; aksi durumda `E4` ile dislanir.
6. Review/survey papers dislanmaz; uygunlarsa `contextual corpus` olarak etiketlenir.
7. Primary technical evidence ile contextual review/survey papers title/abstract asamasindan itibaren ayri tutulur.
8. 6G relevance strict keyword-only inclusion requirement olarak kullanilmaz; direct / inferred / weak / not applicable olarak kodlanir.

## 4. Full-Text Eligibility Rules

Amac, nihai dahil/disla kararini ve calismanin evidence rolunu belirlemektir.

Tam metin kurallari:

1. Her dislama icin tek ana exclusion code secilir ve gerekce kisa ama denetlenebilir yazilir.
2. Full text erisilemiyorsa `E8` atanir; record PRISMA flow icinde "reports not retrieved" olarak izlenir.
3. Tam metin peer-reviewed olmadigini gosterirse `E5` atanir.
4. Short abstract, poster, editorial veya opinion turleri `E6` ile dislanir.
5. English olmayan tam metinler `E7` ile dislanir.
6. Ayni calismaya ait duplicate record varsa kayitlar baglanir, calisma tek sayilir ve tekrar kayit `E10` ile isaretlenir.
7. Teknik veri cikarimina uygun minimum alan yoksa `E9` atanir.
8. Book chapter veya kitap bolumu ana corpus icin uygun degildir; yalnizca gerekli gorulurse contextual/background olarak etiketlenir, aksi halde `E11` atanir.
9. 2026 kayitlari icin publication date veya available date June 30, 2026 sonrasindaysa date eligibility asamasinda dislanir.
10. Gun/ay bilgisi belirsiz 2026 kayitlari `date_uncertain` olarak isaretlenir ve nihai eligibility karari icin dogrulanir.
11. Dahil edilen primary technical evidence, veri cikarim ve synthesis tablolarinda review/survey contextual corpus'tan ayri tutulur.
12. Review/survey papers, taxonomy, terminology, research gap ve background sentezi icin contextual corpus olarak korunabilir; primary technical evidence sayimina karistirilmaz.
13. Optical beam tracking/alignment calismalari icin tam metinde integrated sensing-and-communication objective, evaluation veya metric bulunmuyorsa `E4` atanir.

## 5. Calisma Turu Etiketleme

`document_type`, `corpus_role` ve `screening_decision` alanlari asagidaki ayrimi korumak icin kullanilir:

- `primary technical evidence`: O-ISAC sistem, model, deney, simulation, prototype veya metric-governed technical evaluation sunan calisma.
- `contextual`: Review, survey, tutorial, roadmap veya pre-2020 foundational kaynak olup taxonomy, terminology, background, gap mapping veya technology lineage icin tutulan kayit.
- `excluded`: Exclusion criteria kapsaminda dislanan kayit.

## 6. Pilot Tarama

Pilot set boyutu:

- [ ] 25 kayit
- [ ] 50 kayit
- [ ] 100 kayit
- [ ] Diger:

Pilot amaci:

- Kriterler anlasiliyor mu?
- Degerlendiriciler benzer karar veriyor mu?
- Belirsiz durumlar icin ek kural gerekiyor mu?
- Review/survey contextual corpus ile primary technical evidence ayrimi tutarli mi?

Pilot sonrasi revizyon:

## 7. Uyusmazlik Cozumu

- Birinci degerlendirici:
- Ikinci degerlendirici:
- Ucuncu hakem / nihai karar verici:
- Cozum yontemi:

Uyusmazliklarda karar gunlugune not eklenir; inclusion/exclusion gerekcesi ve varsa exclusion code izlenebilir tutulur.

## 8. PRISMA Icin Kaydedilecek Sayilar

- Records identified from IEEE Xplore: TBD
- Records identified from Scopus: TBD
- Records identified from ScienceDirect: TBD
- Records identified from SpringerLink: TBD
- Records identified from Wiley Online Library: TBD
- Records identified from Taylor & Francis Online: TBD
- Records identified from other sources/foundational pre-2020: TBD
- Records after duplicate removal: TBD
- Records screened by title/abstract: TBD
- Records excluded: TBD
- Reports sought for retrieval: TBD
- Reports not retrieved: TBD
- Reports assessed for eligibility: TBD
- Reports excluded with reasons: TBD
- Studies included in review: TBD
- Contextual review/survey papers retained: TBD
- Primary technical studies included: TBD
