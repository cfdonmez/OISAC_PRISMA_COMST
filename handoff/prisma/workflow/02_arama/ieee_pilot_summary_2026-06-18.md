# IEEE Xplore Pilot Summary - 2026-06-18

Bu dosya Step 2A IEEE Xplore pilot search kayitlarini ozetler. Bu kayitlar pilot search sonuclaridir; final search execution, deduplication, screening veya PRISMA flow count olarak kullanilmayacaktir. Search freeze etiketi `planned search freeze date: June 30, 2026` olarak kalir.

Step 2B guncelleme notu: IEEE-PILOT-S1F-R2 2026-06-19 tarihinde calistirildi ve IEEE-PILOT-S1F-R1'in yerine candidate photonic-THz/mmWave IEEE pilot query olarak kaydedildi. Guncel candidate pilot package icin `combined_ieee_scopus_pilot_summary_2026-06-19.md` dosyasina bakilmalidir.

## Raw Export Dosya Eslesmeleri

Disk uzerindeki raw export dosya adlari pilot ID'lerle birebir eslesmiyor gorunmektedir. Eslestirme satir sayisi ve icerik sinyaliyle yapildi; ham dosyalar yeniden adlandirilmadi veya degistirilmedi.

| Pilot ID | Gorevde beklenen count | Diskteki raw export file | Parsed CSV rows | Eslesme notu |
|---|---:|---|---:|---|
| IEEE-PILOT-S1A | 31 | `raw_exports/ieee_xplore/pilot_2026-06-18/ieee_pilot_s1f-r1_export_2026-06-18.csv` | 31 | Exact O-ISAC phrase search icin count ile eslesiyor. |
| IEEE-PILOT-S1B-R2 | 239 | `raw_exports/ieee_xplore/pilot_2026-06-18/ieee_pilot_s1a_export_2026_06_18.csv` | 239 | Document Title + Abstract controlled ISAC+optical candidate count ile eslesiyor. |
| IEEE-PILOT-S1F-R1 | 110 | `raw_exports/ieee_xplore/pilot_2026-06-18/ieee_pilot_s1b_R2export_2026_06_18.csv` | 110 | photonic-THz/microwave photonic pilot count ile eslesiyor. |

## Pilot Kayit Sayilari ve Prelim Kararlar

| Search ID | Scope / descriptor | Raw records | Exported records | Prelim karar |
|---|---|---:|---:|---|
| IEEE-PILOT-S1A | exact O-ISAC phrase search | 31 | 31 | retained; candidate for final package |
| IEEE-PILOT-S1B | All Metadata generic ISAC+optical | 1195 | not_exported | too broad; rejected in current form |
| IEEE-PILOT-S1B-R1 | refined All Metadata ISAC+optical+sensing | 780 | not_exported | still too broad |
| IEEE-PILOT-S1B-R2 | Document Title + Abstract controlled ISAC+optical | 239 | 239 | retained as candidate; needs inspection |
| IEEE-PILOT-S1C-R1 | VLC/LiFi broad | >1000 | not_exported | too broad; rejected/refinement needed |
| IEEE-PILOT-S1D-R1 | FSO/OWC broad | 1000 | not_exported | too broad; rejected/refinement needed |
| IEEE-PILOT-S1E-R1 | fiber broad | >3000 | not_exported | too broad; rejected/refinement needed |
| IEEE-PILOT-S1F-R1 | photonic-THz/microwave photonic | 110 | 110 | valuable but noisy; refine to S1F-R2 |

## Query String Durumu

Tam pilot query string'ler repo icinde bulunamadi. Bu nedenle `search_log.csv` icinde pilot satirlarinin `search_string` alani `query_string_pending_from_chat_log` olarak isaretlendi. Query string uydurulmadi.

TODO:

- Chat log veya IEEE Xplore search history uzerinden exact pilot query string'leri geri al.
- S1A ve S1B-R2 candidate sorgularini final package oncesi inspect et.
- S1F-R1 icin daha kontrollu IEEE-PILOT-S1F-R2 sorgusunu calistir.
- S1F-R2 sonrasinda Scopus pilot search asamasina gec.

## Deduplication ve PRISMA Notu

- Duplicate removal / deduplication final yapilmadi.
- Title/abstract screening yapilmadi.
- Included studies, contextual records ve primary technical evidence sayilari belirlenmedi.
- Review/survey papers contextual corpus olarak isaretlenecek; primary technical evidence sayilmayacak.
- Pilot count degerleri PRISMA flow dosyasina final count olarak yazilmadi; PRISMA flow alanlari TBD kalmalidir.

## Next Action

1. S1A, S1B-R2 ve S1F-R2 aday paketini inspect et.
2. Scopus S1B ve S1F count mismatch kontrollerini tamamla.
3. Supplementary platform pilots baslatilmadan once core candidate package'i netlestir.
