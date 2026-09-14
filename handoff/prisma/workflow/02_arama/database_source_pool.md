# 02 - Veritabani Kaynak Havuzu

Son guncelleme: 2026-06-18

Bu dosya, O-ISAC PRISMA calismasi icin erisilebilir veritabani ve yayin platformu havuzunu izler. Amac, aramayi yalnizca uc core database ile sinirlamamak; fakat eklenecek her kaynagi konu uygunlugu, PRISMA izlenebilirligi ve export edilebilirlik acisindan gerekcelendirmektir.

## Kullanici Tarafindan Bildirilen Erisim Kaynaklari

- Milli Kutuphane veritabani listesi: `https://mk.gov.tr/veritabanlari/Veritabanlar%C4%B1%20Listesi/liste`
- TOBB ETU Kutuphane veritabanlari: `https://www.etu.edu.tr/tr/kutuphane/veritabanlari`

Not: 2026-06-18 Codex kontrolunde TOBB ETU listesi okunabildi. Milli Kutuphane listesi bu turda web timeout nedeniyle tam dogrulanamadi; kullanici erisimi oldugu icin kaynak havuzunda `to_verify` olarak tutulur.

## Kaynak Katmanlari

### Tier 1 - Core primary bibliographic databases

Bu kaynaklar ana bibliographic coverage icin core kalir:

- Scopus
- IEEE Xplore

### Tier 2 - Selected supplementary publisher/platform sources

Kullanici tarafindan secilen ve aramada kullanilacak supplementary publisher/platform kaynaklari:

- ScienceDirect
- SpringerLink
- Wiley Online Library
- Taylor & Francis Online

### Tier 3 - Not included due to access unavailability during search planning

Bu kaynaklar current search source set icine alinmayacaktir; gerekce methods/protocol icinde acik raporlanacaktir:

- Web of Science
- ACM Digital Library

Reason:

> Web of Science and ACM Digital Library will not be included because institutional access was not available during the search planning stage.

### Tier 4 - Candidate sources not currently selected

Bu kaynaklar erisim havuzunda bulunabilir; ancak mevcut secili arama setine dahil degildir. Eklenmeleri gerekirse once proje baglami, karar gunlugu ve search plan guncellenir:

- IOP Science
- American Institute of Physics Journals / AIP
- American Physical Society Journals / APS
- IET Digital Library or IET content where separately searchable/exportable
- Academic Search Ultimate / EBSCO
- DOAJ
- TR Dizin
- Milli Kutuphane listesinden dogrulanacak ilgili engineering / optics / telecommunications kaynaklari

### Tier 5 - Retrieval, contextual, or background-only sources

Bu kaynaklar tam metin erisimi, contextual background, terminology check veya citation chasing icin kullanilabilir; primary technical evidence corpus'a otomatik girmez:

- Publisher full-text pages
- Library discovery tools
- Review/survey reference lists
- Pre-2020 foundational studies
- E-books, standards, reports, theses, patents, and non-peer-reviewed materials

## Secim Kurali

Bir supplementary source aramaya eklenmeden once su sorular cevaplanir:

1. O-ISAC, optics/photonics, electrical-electronics engineering, computer science, telecommunications veya multidisciplinary peer-reviewed literature icin konu uygunlugu var mi?
2. Exact query kaydedilebiliyor mu?
3. Tarih, dil ve document type filtreleri uygulanabiliyor veya screening asamasinda izlenebiliyor mu?
4. Raw record count ve exported record count kaydedilebiliyor mu?
5. RIS, BibTeX, CSV veya baska izlenebilir export alinabiliyor mu?
6. Sonuclar core database kayitlariyla deduplicate edilebiliyor mu?
7. Review/survey, book chapter, thesis, standard, patent veya grey literature primary technical evidence corpus'tan ayri tutulabiliyor mu?

## PRISMA Kayit Disiplini

Supplementary search kullanilirsa her kaynak icin `search_log.csv` icinde ayri `search_id` acilir. En az su alanlar doldurulur:

- source name
- search stage: supplementary / sensitivity / full-text retrieval / citation chasing
- exact search string
- limits
- raw records
- records exported
- export file name
- deduplication notes

PRISMA flow counts icinde core database records ve supplementary source records ayri izlenir; deduplication sonrasi tek corpus'a alinabilir.

## Mevcut Durum

- Source pool tanimlandi.
- TOBB ETU listesi ilk kontrol icin okundu.
- Milli Kutuphane listesi kullanici erisimi olarak kaydedildi; ayrintili kaynak adlari daha sonra dogrulanacak.
- Secili supplementary kaynaklar: ScienceDirect, SpringerLink, Wiley Online Library, Taylor & Francis Online.
- Web of Science ve ACM Digital Library institutional access olmadigi icin search planning asamasinda dahil edilmeyecektir.
- Supplementary kaynaklarda search execution henuz yapilmadi.
- Count veya inclusion sonucu yazilmadi.
