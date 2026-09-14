# Bilgi Notu 03 - Arama Stratejisi Know-how

Bu not, O-ISAC for 6G review icin arama stratejisini sistematik ve tekrarlanabilir tutmak amaciyla guncellenmistir. Arama henuz yurutulmedigi icin sonuc sayisi veya final search date yazilmaz.

## Calisma Icin Sabit Kararlar

- Search window: January 1, 2020 - June 30, 2026.
- Search freeze etiketi: planned search freeze date: June 30, 2026.
- Core primary databases: Scopus, IEEE Xplore.
- Selected supplementary sources: ScienceDirect, SpringerLink, Wiley Online Library, Taylor & Francis Online.
- Language: English only.
- Kayit sayilari: TBD until searches are executed.

## Ana Kavram Bloklari

Arama sorgusu en az uc kavram ailesini kapsamalidir:

1. Integrated sensing and communication kavramlari:
   - "integrated sensing and communication"
   - ISAC
   - "joint communication and sensing"
   - "joint sensing and communication"
   - "dual-function sensing and communication"
   - "communication sensing integration"
2. Optical platform kavramlari:
   - optical
   - photonic
   - fiber
   - "free space optical"
   - FSO
   - VLC
   - LiFi
   - "visible light communication"
   - "photonic THz"
   - "terahertz photonic"
3. 6G ve gelecek nesil baglam:
   - 6G
   - "sixth generation"
   - "beyond 5G"
   - B5G
   - "next generation network"

## Taslak Ana Sorgu Mantigi

```text
("integrated sensing and communication" OR ISAC OR "joint communication and sensing" OR "joint sensing and communication" OR "dual-function sensing and communication")
AND
(optical OR photonic OR fiber OR "free space optical" OR FSO OR VLC OR LiFi OR "visible light communication" OR "photonic THz" OR "terahertz photonic")
AND
(6G OR "sixth generation" OR "beyond 5G" OR B5G OR "next generation network")
```

Bu sorgu database/source-specific syntax'a cevrilmelidir. Scopus, IEEE Xplore, ScienceDirect, SpringerLink, Wiley Online Library ve Taylor & Francis Online alan etiketleri ve filtreleme imkanlari farkli oldugu icin nihai sorgular her kaynak icin ayri kaydedilmelidir.

## Database-Specific Kayit Disiplini

Her veri tabani icin su bilgiler kaydedilmelidir:

- database name
- exact query string
- searched fields
- date searched
- filters and limits
- language restriction
- year range
- number of records retrieved
- export format
- export file name

## Export Formatlari

Tercih edilen export formatlari:

- RIS
- BibTeX
- CSV

Bu formatlar alinmadan `search completed` durumu verilmemelidir.

## Kalite Kontrol Sorulari

1. Bilinen anahtar O-ISAC calismalari sorgu ile yakalaniyor mu?
2. Ilk 50-100 kayit konuya yeterince yakin mi?
3. Optical modality terimleri aramayi asiri daraltiyor mu?
4. 6G terimleri gerekli calismalari disarida birakiyor mu?
5. Review/survey papers contextual corpus icinde ayri tutuldu mu?
6. Search execution date, planned search freeze date olan June 30, 2026 sonrasinda mi kaydedildi?

## PRISMA Icin Not

Final manuscript icinde "databases were searched" ifadesi tek basina yeterli degildir. Her database icin tam sorgu, tarih, filtreler, sonuc sayisi ve export bilgisi raporlanmalidir. Arama yurutulene kadar yalnizca `planned search freeze date: June 30, 2026` ifadesi kullanilmalidir.
