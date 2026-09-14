# 01 - O-ISAC Arama Plani

Bu dosya, Optical Integrated Sensing and Communication (O-ISAC) for 6G calismasi icin PRISMA-grounded narrative systematic review ve scoping-style PCC component arama planini tanimlar. 2026-06-22 protocol amendment ile onceki `planned search freeze date: June 30, 2026` beklenmeden Step 3 final search execution baslatilmistir. Actual final search cutoff: June 22, 2026.

## 1. Temel Search Settings

- Core primary databases: Scopus, IEEE Xplore
- Selected supplementary publisher/platform sources: ScienceDirect, SpringerLink, Wiley Online Library, Taylor & Francis Online
- Source access basis: institutional database lists from Milli Kutuphane and TOBB ETU
- Search window: January 1, 2020 - June 22, 2026
- Search cutoff date: actual final search cutoff: June 22, 2026
- Language: English
- Document types: peer-reviewed journal articles, early-access journal articles, full-length conference papers, review/survey papers for contextual comparison only
- Ana metodolojik cerceve: PCC - Population / Concept / Context
- Ana sentez yaklasimi: structured narrative synthesis, scoping-style taxonomy mapping, evidence tabulation, metric-governed comparison, validation maturity mapping, benchmark readiness assessment, research roadmap synthesis
- Meta-analysis planlanmamistir; O-ISAC literaturu optical modality, system architecture, sensing task, communication metric, sensing metric, validation method ve measurement plane acisindan heterojendir.

Date filter notu: Database year filters may retrieve all 2026 records; records published or made available after June 22, 2026 will be excluded during date eligibility screening.

## 1A. Expanded Source Access

Kullanici, Milli Kutuphane ve TOBB ETU veritabani listelerindeki kaynaklara erisimi oldugunu bildirdi. 2026-06-18 kullanici karariyla secilmis arama kaynaklari Scopus, IEEE Xplore, ScienceDirect, SpringerLink, Wiley Online Library ve Taylor & Francis Online olarak guncellendi.

Scopus ve IEEE Xplore core primary databases olarak kullanilacak. ScienceDirect, SpringerLink, Wiley Online Library ve Taylor & Francis Online supplementary publisher/platform search olarak kullanilacak. Web of Science ve ACM Digital Library, search planning asamasinda institutional access olmadigi icin dahil edilmeyecektir.

Formal information sources sentence:

> Information sources: The systematic search will be conducted in Scopus and IEEE Xplore as the primary bibliographic and engineering databases. Supplementary platform searches will be conducted in ScienceDirect, SpringerLink, Wiley Online Library, and Taylor & Francis Online. Web of Science and ACM Digital Library will not be included because institutional access was not available during the search planning stage.

Supplementary source pool dosyasi:

- `database_source_pool.md`

Supplementary kaynaklarin eklenmesi icin kural:

- O-ISAC, optics/photonics, electrical-electronics engineering, computer science, telecommunications veya multidisciplinary peer-reviewed literature icin konu uygunlugu bulunmali.
- Exact query, limits, search date, raw records, exported records ve export file name `search_log.csv` icinde izlenebilir olmalidir.
- Publisher/platform aramalari core database sonuclariyla deduplicate edilmelidir.
- Review/survey, book chapter, thesis, standard, patent veya grey literature primary technical evidence corpus'a karistirilmamalidir.

Secili supplementary kaynaklar: ScienceDirect, SpringerLink, Wiley Online Library, Taylor & Francis Online.

## 2. Core Search Blocks

### Block A - ISAC / sensing-communication integration

```text
"integrated sensing and communication"
OR "integrated sensing and communications"
OR "O-ISAC"
OR OISAC
OR ISAC
OR "optical ISAC"
OR "optical integrated sensing and communication"
OR "integrated optical sensing and communication"
OR "optical joint communication and sensing"
OR "joint optical communication and sensing"
OR "joint communication and sensing"
OR "joint sensing and communication"
OR "sensing and communication"
OR "communication and sensing"
OR "sensing-communication"
OR "communication-sensing"
OR "dual-function"
OR "dual function"
```

### Block B - Optical modality

```text
optical
OR photonic
OR "free-space optical"
OR FSO
OR VLC
OR LiFi
OR "visible light communication"
OR "visible light communications"
OR "optical wireless"
OR OWC
OR fiber
OR fibre
OR "fiber optic"
OR "fibre optic"
OR "optical fiber"
OR "optical fibre"
OR "photonic THz"
OR "photonic terahertz"
OR "photonic mmWave"
OR "photonic millimeter wave"
OR "optical camera communication"
OR OCC
```

### Block C - 6G / next-generation communication context

```text
6G
OR "sixth generation"
OR "next-generation network"
OR "next generation network"
OR "future network"
OR "wireless network"
OR "communication system"
OR "communication systems"
OR "optical communication"
OR "optical communications"
```

Not: Ana aramada Block C zorunlu yapilmayacaktir; ilgili bazi O-ISAC calismalari 6G terimini veya next-generation network ifadesini kullanmayabilir. Block C, kayitlari etiketleme, kapsam yorumlama veya ikincil duyarlilik aramalari icin kullanilabilir.

### Block D - Sensing / localization / ranging / detection terms

```text
sensing
OR localization
OR localisation
OR positioning
OR ranging
OR detection
OR monitoring
OR imaging
OR perception
OR estimation
```

### Block E - Communication terms

```text
communication
OR communications
OR "data rate"
OR throughput
OR BER
OR "bit error rate"
OR capacity
OR "spectral efficiency"
OR link
OR transmission
OR transceiver
```

## 3. Ana Sorgu Mantigi

Ana arama mantigi:

```text
(Block A) AND (Block B)
```

Block C ana sorguda zorunlu degildir. Tarama sonrasi etiketleme asamasinda calismanin 6G-oriented optical context ile iliskisi Population / Concept / Context cercevesinde degerlendirilecektir.

Outcome, metric veya application terimleri ilk aramaya zorunlu olarak eklenmeyecektir. CRB, FIM, OSNR, SNR, ESNR, rate-sensing tradeoff, positioning, localization, ranging, imaging ve benzeri terimler veri cekme ve ikincil analiz icin kullanilacak; ilk aramada kapsam daraltici filtre olarak kullanilmayacaktir.

## 4. Veri Tabani Bazli Draft Queries

### IEEE Xplore Draft Query

```text
(
  ("All Metadata":"integrated sensing and communication"
   OR "All Metadata":"integrated sensing and communications"
   OR "All Metadata":"O-ISAC"
   OR "All Metadata":OISAC
   OR "All Metadata":ISAC
   OR "All Metadata":"optical ISAC"
   OR "All Metadata":"optical integrated sensing and communication"
   OR "All Metadata":"integrated optical sensing and communication"
   OR "All Metadata":"optical joint communication and sensing"
   OR "All Metadata":"joint optical communication and sensing"
   OR "All Metadata":"joint communication and sensing"
   OR "All Metadata":"joint sensing and communication"
   OR "All Metadata":"sensing and communication"
   OR "All Metadata":"communication and sensing"
   OR "All Metadata":"sensing-communication"
   OR "All Metadata":"communication-sensing"
   OR "All Metadata":"dual-function"
   OR "All Metadata":"dual function")
  AND
  ("All Metadata":optical
   OR "All Metadata":photonic
   OR "All Metadata":"free-space optical"
   OR "All Metadata":FSO
   OR "All Metadata":VLC
   OR "All Metadata":LiFi
   OR "All Metadata":"visible light communication"
   OR "All Metadata":"visible light communications"
   OR "All Metadata":"optical wireless"
   OR "All Metadata":OWC
   OR "All Metadata":fiber
   OR "All Metadata":fibre
   OR "All Metadata":"fiber optic"
   OR "All Metadata":"fibre optic"
   OR "All Metadata":"optical fiber"
   OR "All Metadata":"optical fibre"
   OR "All Metadata":"photonic THz"
   OR "All Metadata":"photonic terahertz"
   OR "All Metadata":"photonic mmWave"
   OR "All Metadata":"photonic millimeter wave"
   OR "All Metadata":"optical camera communication"
   OR "All Metadata":OCC)
)
```

Limits to record: January 1, 2020 - June 22, 2026 search window; English; journal articles, early-access journal articles where identifiable, and conference publications. Full-length conference papers will be confirmed during screening when database filters cannot separate full papers from abstracts.

Date filter note: Database year filters may retrieve all 2026 records; records published or made available after June 22, 2026 will be excluded during date eligibility screening.

### Scopus Draft Query

```text
TITLE-ABS-KEY(
  (
    "integrated sensing and communication"
    OR "integrated sensing and communications"
    OR "O-ISAC"
    OR OISAC
    OR ISAC
    OR "optical ISAC"
    OR "optical integrated sensing and communication"
    OR "integrated optical sensing and communication"
    OR "optical joint communication and sensing"
    OR "joint optical communication and sensing"
    OR "joint communication and sensing"
    OR "joint sensing and communication"
    OR "sensing and communication"
    OR "communication and sensing"
    OR "sensing-communication"
    OR "communication-sensing"
    OR "dual-function"
    OR "dual function"
  )
  AND
  (
    optical
    OR photonic
    OR "free-space optical"
    OR FSO
    OR VLC
    OR LiFi
    OR "visible light communication"
    OR "visible light communications"
    OR "optical wireless"
    OR OWC
    OR fiber
    OR fibre
    OR "fiber optic"
    OR "fibre optic"
    OR "optical fiber"
    OR "optical fibre"
    OR "photonic THz"
    OR "photonic terahertz"
    OR "photonic mmWave"
    OR "photonic millimeter wave"
    OR "optical camera communication"
    OR OCC
  )
)
AND PUBYEAR > 2019
AND PUBYEAR < 2027
AND (LIMIT-TO(LANGUAGE, "English"))
AND (LIMIT-TO(DOCTYPE, "ar") OR LIMIT-TO(DOCTYPE, "cp") OR LIMIT-TO(DOCTYPE, "re"))
```

Not: Scopus `DOCTYPE "re"` review/survey papers icin contextual comparison amaciyla tutulur; primary evidence synthesis icin uygunluk tam metin taramasinda ayrica isaretlenir.

Date filter note: Database year filters may retrieve all 2026 records; records published or made available after June 22, 2026 will be excluded during date eligibility screening.

### Web of Science Draft Query - Not Included

```text
TS=(
  (
    "integrated sensing and communication"
    OR "integrated sensing and communications"
    OR "O-ISAC"
    OR OISAC
    OR ISAC
    OR "optical ISAC"
    OR "optical integrated sensing and communication"
    OR "integrated optical sensing and communication"
    OR "optical joint communication and sensing"
    OR "joint optical communication and sensing"
    OR "joint communication and sensing"
    OR "joint sensing and communication"
    OR "sensing and communication"
    OR "communication and sensing"
    OR "sensing-communication"
    OR "communication-sensing"
    OR "dual-function"
    OR "dual function"
  )
  AND
  (
    optical
    OR photonic
    OR "free-space optical"
    OR FSO
    OR VLC
    OR LiFi
    OR "visible light communication"
    OR "visible light communications"
    OR "optical wireless"
    OR OWC
    OR fiber
    OR fibre
    OR "fiber optic"
    OR "fibre optic"
    OR "optical fiber"
    OR "optical fibre"
    OR "photonic THz"
    OR "photonic terahertz"
    OR "photonic mmWave"
    OR "photonic millimeter wave"
    OR "optical camera communication"
    OR OCC
  )
)
```

Status: not included because institutional access was not available during the search planning stage. This draft is retained only as a historical planning artifact and must not be executed unless a later protocol amendment explicitly changes the source set.

Limits if re-added later: January 1, 2020 - June 22, 2026 search window; language English; document types Article, Proceedings Paper, Review; Early Access will be recorded when available. Reviews/surveys are retained for contextual comparison only.

Date filter note: Database year filters may retrieve all 2026 records; records published or made available after June 22, 2026 will be excluded during date eligibility screening.

### ScienceDirect Draft Query

```text
("integrated sensing and communication" OR "integrated sensing and communications" OR "O-ISAC" OR OISAC OR ISAC OR "optical ISAC" OR "optical integrated sensing and communication" OR "integrated optical sensing and communication" OR "joint communication and sensing" OR "joint sensing and communication" OR "sensing and communication" OR "communication and sensing" OR "sensing-communication" OR "communication-sensing" OR "dual-function" OR "dual function")
AND
(optical OR photonic OR "free-space optical" OR FSO OR VLC OR LiFi OR "visible light communication" OR "visible light communications" OR "optical wireless" OR OWC OR fiber OR fibre OR "fiber optic" OR "fibre optic" OR "optical fiber" OR "optical fibre" OR "photonic THz" OR "photonic terahertz" OR "photonic mmWave" OR "photonic millimeter wave" OR "optical camera communication" OR OCC)
```

Limits to record: January 1, 2020 - June 22, 2026 search window; English; article, review/survey for contextual comparison only, and relevant conference/proceedings content if available on platform.

### SpringerLink Draft Query

```text
("integrated sensing and communication" OR "integrated sensing and communications" OR "O-ISAC" OR OISAC OR ISAC OR "optical ISAC" OR "optical integrated sensing and communication" OR "integrated optical sensing and communication" OR "joint communication and sensing" OR "joint sensing and communication" OR "sensing and communication" OR "communication and sensing" OR "sensing-communication" OR "communication-sensing" OR "dual-function" OR "dual function")
AND
(optical OR photonic OR "free-space optical" OR FSO OR VLC OR LiFi OR "visible light communication" OR "visible light communications" OR "optical wireless" OR OWC OR fiber OR fibre OR "fiber optic" OR "fibre optic" OR "optical fiber" OR "optical fibre" OR "photonic THz" OR "photonic terahertz" OR "photonic mmWave" OR "photonic millimeter wave" OR "optical camera communication" OR OCC)
```

Limits to record: January 1, 2020 - June 22, 2026 search window; English; article, conference paper/proceedings where filterable, and review/survey for contextual comparison only.

### Wiley Online Library Draft Query

```text
("integrated sensing and communication" OR "integrated sensing and communications" OR "O-ISAC" OR OISAC OR ISAC OR "optical ISAC" OR "optical integrated sensing and communication" OR "integrated optical sensing and communication" OR "joint communication and sensing" OR "joint sensing and communication" OR "sensing and communication" OR "communication and sensing" OR "sensing-communication" OR "communication-sensing" OR "dual-function" OR "dual function")
AND
(optical OR photonic OR "free-space optical" OR FSO OR VLC OR LiFi OR "visible light communication" OR "visible light communications" OR "optical wireless" OR OWC OR fiber OR fibre OR "fiber optic" OR "fibre optic" OR "optical fiber" OR "optical fibre" OR "photonic THz" OR "photonic terahertz" OR "photonic mmWave" OR "photonic millimeter wave" OR "optical camera communication" OR OCC)
```

Limits to record: January 1, 2020 - June 22, 2026 search window; English; article, early view where available, and review/survey for contextual comparison only.

### Taylor & Francis Online Draft Query

```text
("integrated sensing and communication" OR "integrated sensing and communications" OR "O-ISAC" OR OISAC OR ISAC OR "optical ISAC" OR "optical integrated sensing and communication" OR "integrated optical sensing and communication" OR "joint communication and sensing" OR "joint sensing and communication" OR "sensing and communication" OR "communication and sensing" OR "sensing-communication" OR "communication-sensing" OR "dual-function" OR "dual function")
AND
(optical OR photonic OR "free-space optical" OR FSO OR VLC OR LiFi OR "visible light communication" OR "visible light communications" OR "optical wireless" OR OWC OR fiber OR fibre OR "fiber optic" OR "fibre optic" OR "optical fiber" OR "optical fibre" OR "photonic THz" OR "photonic terahertz" OR "photonic mmWave" OR "photonic millimeter wave" OR "optical camera communication" OR OCC)
```

Limits to record: January 1, 2020 - June 22, 2026 search window; English; article and review/survey for contextual comparison only.

## 5. Modality-Specific Secondary Searches

Ikincil aramalar, ana aramanin bilinen calismalari yakalamadigi veya belirli optical modality icin yetersiz kaldigi durumlarda calistirilacaktir. Her ikincil arama, ilgili veri tabaninin syntax kurallarina uyarlanacak ve `search_log.csv` icinde ayri search_id ile kaydedilecektir.

Ikincil aramalar yalnizca Block A'ya bagimli tutulmaz. Modality-specific mantik su sekildedir:

```text
(modality terms) AND (Block D sensing/localization/ranging/detection terms) AND (Block E communication terms)
```

Gerekirse bu mantiga Block A exact O-ISAC terimleri ek bir duyarlilik katmani olarak eklenebilir; ancak modality-specific recall kontrolu icin temel kosul modality + sensing + communication eslesmesidir.

### Fiber-S2

```text
(fiber OR fibre OR "fiber optic" OR "fibre optic" OR "optical fiber" OR "optical fibre") AND (Block D) AND (Block E)
```

### FSO-S2

```text
("free-space optical" OR FSO OR "optical wireless" OR OWC) AND (Block D) AND (Block E)
```

### VLC-LiFi-S2

```text
(VLC OR LiFi OR "visible light communication" OR "visible light communications" OR "optical camera communication" OR OCC) AND (Block D) AND (Block E)
```

### Photonic-THz-S2

```text
("photonic THz" OR "photonic terahertz" OR "photonic mmWave" OR "photonic millimeter wave" OR photonic) AND (Block D) AND (Block E)
```

### Hybrid-S2

```text
(hybrid OR "hybrid optical" OR "hybrid optical systems" OR "optical wireless" OR photonic OR fiber OR fibre OR FSO OR VLC OR LiFi) AND (Block D) AND (Block E)
```

## 6. Noise-Control Logic

- Ilk arama asamasinda aggressive NOT block kullanilmayacaktir.
- Radar, RF, microwave, MIMO veya non-optical haberlesme terimleri ilk asamada NOT ile dislanmayacaktir; hybrid optical systems ve photonic-THz literaturunde bu terimler ilgili olabilir.
- Gurultu cok yuksek olursa once field restriction uygulanacaktir: title/abstract/keywords veya all metadata yerine daha dar alanlar.
- Hala gurultu yuksekse modality-specific secondary searches calistirilacak ve sonuclar ana arama ile deduplicate edilecektir.
- Review/survey papers, contextual comparison ve backward/forward citation snowballing icin isaretlenecek; primary evidence ile karistirilmamasi icin veri cekme tablosunda ayri kodlanacaktir.
- Dusuk methodological/reporting quality tek basina dislama nedeni yapilmayacaktir; TQAF-style technical quality assessment ile kanit gucu nitelendirilecektir.

## 7. PRISMA Search Documentation Reminder

Her arama icin asagidakiler `search_log.csv` icinde kaydedilecektir:

- search_id
- search_date; final execution basladigi icin actual execution date veya source/query execution date olarak kaydedilecek; Step 3 start date: `2026-06-22`
- database_or_source
- search_stage
- platform_or_modality
- exact search string
- limits
- raw_records
- records_exported
- export file name
- notes

PRISMA akis diyagrami icin core veri tabanlarindan bulunan kayit sayisi, supplementary kaynaklardan bulunan kayit sayisi, diger kaynaklardan/foundational kaynaklardan bulunan kayit sayisi, tekrar kayit sayisi, otomasyonla elenen kayit sayisi ve baslik/ozet taramasina giren kayit sayisi ayri ve izlenebilir tutulacaktir.

## 8. IEEE Xplore Pilot Search - 2026-06-18

Bu bolum, 2026-06-18 tarihinde IEEE Xplore uzerinde yapilan Step 2A pilot search testlerini kaydeder. Bu pilot sonuclar final search execution degildir ve PRISMA flow count sayilari olarak kullanilmayacaktir. Search freeze date etiketi `planned search freeze date: June 30, 2026` olarak kalir.

### Pilot query karar ozeti

| Search ID | Pilot kapsam | Pilot kayit sayisi | Prelim karar | Not |
|---|---|---:|---|---|
| IEEE-PILOT-S1A | exact O-ISAC phrase search | 31 | retained | Candidate for final package. |
| IEEE-PILOT-S1B | All Metadata generic ISAC+optical | 1195 | rejected in current form | Too broad. |
| IEEE-PILOT-S1B-R1 | refined All Metadata ISAC+optical+sensing | 780 | rejected in current form | Still too broad. |
| IEEE-PILOT-S1B-R2 | Document Title + Abstract controlled ISAC+optical | 239 | retained as candidate | Needs inspection before final package. |
| IEEE-PILOT-S1C-R1 | VLC/LiFi broad | >1000 | rejected/refinement needed | Broad modality search too noisy. |
| IEEE-PILOT-S1D-R1 | FSO/OWC broad | 1000 | rejected/refinement needed | Broad modality search too noisy. |
| IEEE-PILOT-S1E-R1 | fiber broad | >3000 | rejected/refinement needed | Broad modality search too noisy. |
| IEEE-PILOT-S1F-R1 | photonic-THz/microwave photonic | 110 | replaced | Valuable but noisy; replaced by S1F-R2 in Step 2B. |
| IEEE-PILOT-S1F-R2 | photonic-THz/microwave photonic refined | 45 | retained as candidate | Cleaner refined pilot completed on 2026-06-19. |

### Pilot raw export mapping

Raw export dosya adlari disk uzerinde pilot ID'lerle birebir eslesmiyor gorunmektedir. Bu nedenle eslestirme satir sayisi ve icerik sinyaliyle kaydedildi; ham dosyalar degistirilmedi.

| Pilot ID | Expected pilot count | Raw export file on disk | Parsed CSV rows | Mapping note |
|---|---:|---|---:|---|
| IEEE-PILOT-S1A | 31 | `raw_exports/ieee_xplore/pilot_2026-06-18/ieee_pilot_s1f-r1_export_2026-06-18.csv` | 31 | Mapped by 31-row export and exact O-ISAC content signal. |
| IEEE-PILOT-S1B-R2 | 239 | `raw_exports/ieee_xplore/pilot_2026-06-18/ieee_pilot_s1a_export_2026_06_18.csv` | 239 | Mapped by 239-row export and controlled ISAC+optical candidate size. |
| IEEE-PILOT-S1F-R1 | 110 | `raw_exports/ieee_xplore/pilot_2026-06-18/ieee_pilot_s1b_R2export_2026_06_18.csv` | 110 | Mapped by 110-row export and photonic-THz/microwave photonic content signal. |

### Pilot query appendix status

Step 2B cleanup sonrasi IEEE-PILOT-S1A, IEEE-PILOT-S1B-R2 ve IEEE-PILOT-S1F-R2 candidate query stringleri chat log kaydindan geri alinip `search_log.csv` ve asagidaki combined pilot bolumune islendi. Rejected IEEE pilot query stringleri ve Scopus exact query stringleri kesin kaynaklardan geri alinana kadar placeholder olarak kalacaktir; query metinleri uydurulmayacaktir.

TODO:

- IEEE-PILOT-S1B exact query string chat log veya IEEE Xplore search history uzerinden alinacak.
- IEEE-PILOT-S1B-R1 exact query string chat log veya IEEE Xplore search history uzerinden alinacak.
- IEEE-PILOT-S1C-R1, IEEE-PILOT-S1D-R1, IEEE-PILOT-S1E-R1 ve IEEE-PILOT-S1F-R1 exact query string'leri chat log veya IEEE Xplore search history uzerinden alinacak.
- SCO-PILOT-S1A, SCO-PILOT-S1B ve SCO-PILOT-S1F exact query stringleri Scopus history veya kullanici dogrulamasi uzerinden alinacak.
- IEEE pilot package finalize edilmeden once review/survey records contextual corpus olarak isaretlenecek ve primary technical evidence sayilmayacak.

Step 2B notu: IEEE-PILOT-S1F-R2 ve Scopus pilot exportlari 2026-06-19 tarihinde ayri pilot update olarak kaydedildi. Ilgili combined bolum asagidadir.

## 9. IEEE + Scopus Pilot Search - 2026-06-18/19

Bu bolum Step 2B IEEE + Scopus pilot search exportlarini kaydeder. Bu kayitlar pilot search exportlaridir; final search execution, deduplication, screening veya PRISMA flow count olarak kullanilmayacaktir. Search freeze date etiketi `planned search freeze date: June 30, 2026` olarak kalir.

### Canonical raw export klasoru

Step 2B icin canonical raw export klasoru:

- `systematic_review_workflow/02_arama/raw_exports/pilot_2026-06-19/`

Bu klasorde saklanan canonical dosyalar:

| Search ID | Source | Pilot date | Canonical raw export file | Exported rows | Prelim karar |
|---|---|---|---|---:|---|
| IEEE-PILOT-S1A | IEEE Xplore | 2026-06-18 | `IEEE-PILOT-S1A_export_2026-06-18.csv` | 31 | keep candidate |
| IEEE-PILOT-S1B-R2 | IEEE Xplore | 2026-06-18 | `IEEE-PILOT-S1B-R2_export_2026-06-18.csv` | 239 | keep candidate |
| IEEE-PILOT-S1F-R2 | IEEE Xplore | 2026-06-19 | `IEEE-PILOT-S1F-R2_export_2026-06-19.csv` | 45 | keep candidate; replaces S1F-R1 |
| SCO-PILOT-S1A | Scopus | 2026-06-19 | `SCO-PILOT-S1A_export_2026-06-19.csv` | 40 | keep candidate |
| SCO-PILOT-S1B | Scopus | 2026-06-19 | `SCO-PILOT-S1B_export_2026-06-19.csv` | 60 | keep candidate; count mismatch requires verification |
| SCO-PILOT-S1F | Scopus | 2026-06-19 | `SCO-PILOT-S1F_export_2026-06-19.csv` | 104 | keep candidate; minor count mismatch requires verification |

### Count QA notes

| Search ID | Reported records | Exported rows | QA note |
|---|---:|---:|---|
| IEEE-PILOT-S1A | 31 | 31 | Count matches. |
| IEEE-PILOT-S1B-R2 | 239 | 239 | Count matches. |
| IEEE-PILOT-S1F-R2 | 45 | 45 | Count matches; replaces IEEE-PILOT-S1F-R1. |
| SCO-PILOT-S1A | 40 | 40 | Count matches. |
| SCO-PILOT-S1B | 35 | 60 | Reported/export mismatch; verify query/export settings before final search. |
| SCO-PILOT-S1F | 103 | 104 | Minor mismatch; verify before final search. |

SCO-PILOT-S1B export is metadata-light. Future final export should include Year, Source title, Document type, DOI, Abstract, Author keywords, Index keywords, and EID.

### Candidate pilot package

Candidate pilot package for inspection:

- IEEE-PILOT-S1A
- IEEE-PILOT-S1B-R2
- IEEE-PILOT-S1F-R2
- SCO-PILOT-S1A
- SCO-PILOT-S1B
- SCO-PILOT-S1F

Rejected or replaced IEEE pilot records remain documented:

- IEEE-PILOT-S1B = 1195, too broad, rejected.
- IEEE-PILOT-S1B-R1 = 780, too broad, rejected.
- IEEE-PILOT-S1C-R1 = >1000, too broad, rejected/refinement needed.
- IEEE-PILOT-S1D-R1 = 1000, too broad, rejected/refinement needed.
- IEEE-PILOT-S1E-R1 = >3000, too broad, rejected/refinement needed.
- IEEE-PILOT-S1F-R1 = 110, valuable but noisy, replaced by S1F-R2.

### Audit package

Audit zip and extracted audit files are stored under:

- `systematic_review_workflow/02_arama/audits/pilot_2026-06-19/`
- `systematic_review_workflow/02_arama/audits/pilot_2026-06-19/extracted/`

Audit summary reports Scopus total exported rows as 204, Scopus unique records after DOI/title deduplication as 172, combined IEEE + Scopus candidate rows as 519, and combined unique records as 327. These audit numbers are pilot-only deduplication diagnostics and must not be copied into PRISMA flow counts.

### Query String Recovery Status

Candidate query string durumu:

| Search ID | Query string status | Action |
|---|---|---|
| IEEE-PILOT-S1A | available from chat log | Added to IEEE candidate query appendix and `search_log.csv`. |
| IEEE-PILOT-S1B-R2 | available from chat log | Added to IEEE candidate query appendix and `search_log.csv`. |
| IEEE-PILOT-S1F-R2 | available from chat log | Added to IEEE candidate query appendix and `search_log.csv`. |
| SCO-PILOT-S1A | pending exact Scopus history/user confirmation | Keep placeholder; do not reconstruct query. |
| SCO-PILOT-S1B | pending exact Scopus history/user confirmation | Keep placeholder; do not reconstruct query. |
| SCO-PILOT-S1F | pending exact Scopus history/user confirmation | Keep placeholder; do not reconstruct query. |

### IEEE Candidate Query Appendix

Bu appendix yalnizca Step 2B candidate IEEE pilot query stringlerini kaydeder. Query stringler chat log kaydindan aktarilmistir. Pilot query counts final PRISMA flow counts degildir.

#### IEEE-PILOT-S1A

```text
"All Metadata":"O-ISAC" OR "All Metadata":OISAC OR "All Metadata":"optical ISAC" OR "All Metadata":"optical integrated sensing and communication" OR "All Metadata":"integrated optical sensing and communication" OR "All Metadata":"joint optical communication and sensing" OR "All Metadata":"optical joint communication and sensing"
```

#### IEEE-PILOT-S1B-R2

```text
("Document Title":"integrated sensing and communication" OR "Document Title":"integrated sensing and communications" OR "Document Title":ISAC OR "Document Title":"joint sensing and communication" OR "Document Title":"joint communication and sensing" OR "Document Title":"sensing-communication" OR "Document Title":"communication-sensing" OR "Abstract":"integrated sensing and communication" OR "Abstract":"integrated sensing and communications" OR "Abstract":ISAC OR "Abstract":"joint sensing and communication" OR "Abstract":"joint communication and sensing" OR "Abstract":"sensing-communication" OR "Abstract":"communication-sensing")
AND
("Document Title":optical OR "Document Title":photonic OR "Document Title":"free-space optical" OR "Document Title":FSO OR "Document Title":VLC OR "Document Title":LiFi OR "Document Title":"visible light communication" OR "Document Title":"optical wireless" OR "Document Title":"optical fiber" OR "Document Title":"photonic THz" OR "Abstract":optical OR "Abstract":photonic OR "Abstract":"free-space optical" OR "Abstract":FSO OR "Abstract":VLC OR "Abstract":LiFi OR "Abstract":"visible light communication" OR "Abstract":"optical wireless" OR "Abstract":"optical fiber" OR "Abstract":"photonic THz")
```

#### IEEE-PILOT-S1F-R2

```text
("Document Title":"photonic THz" OR "Document Title":"photonic terahertz" OR "Document Title":"photonic mmWave" OR "Document Title":"photonic millimeter wave" OR "Document Title":"microwave photonic" OR "Document Title":"THz-over-fiber" OR "Document Title":"photonics-assisted" OR "Document Title":"photonic-assisted" OR "Document Title":"photonic-aided" OR "Abstract":"photonic THz" OR "Abstract":"photonic terahertz" OR "Abstract":"photonic mmWave" OR "Abstract":"photonic millimeter wave" OR "Abstract":"microwave photonic" OR "Abstract":"THz-over-fiber" OR "Abstract":"photonics-assisted" OR "Abstract":"photonic-assisted" OR "Abstract":"photonic-aided")
AND
("Document Title":"integrated sensing and communication" OR "Document Title":"integrated sensing and communications" OR "Document Title":ISAC OR "Document Title":"joint radar communication" OR "Document Title":"joint radar-communication" OR "Document Title":"joint radar and communication" OR "Document Title":"joint communication and radar" OR "Abstract":"integrated sensing and communication" OR "Abstract":"integrated sensing and communications" OR "Abstract":ISAC)
```

TODO:

- SCO-PILOT-S1A, SCO-PILOT-S1B ve SCO-PILOT-S1F exact query string'leri Scopus database history veya kullanici dogrulamasi uzerinden alinacak.
- SCO-PILOT-S1B reported/export mismatch 35 vs 60 final search oncesi dogrulanacak.
- SCO-PILOT-S1F minor mismatch 103 vs 104 final search oncesi dogrulanacak.
- Rejected IEEE pilot query stringleri gerekiyorsa chat log veya IEEE Xplore search history uzerinden ayrica geri alinacak; uydurulmayacak.
- Review/survey papers contextual corpus olarak isaretlenecek; primary technical evidence sayilmayacak.

Sonraki aksiyon: Candidate pilot package inspect edilecek, Scopus mismatch kontrolleri tamamlanacak ve supplementary platform pilots finalize edilmeden once core + supplementary pilot package netlestirilecektir.

## 10. ScienceDirect Pilot Search - 2026-06-19

Bu bolum ScienceDirect supplementary platform pilot CSV paketini kaydeder. Bu kayitlar pilot search/audit kayitlaridir; final search execution, screening veya PRISMA flow count olarak kullanilmayacaktir.

ScienceDirect original P2 query was not accepted because the platform warned: "Use fewer boolean connectors (max 8 per field)". Therefore, the query was split into smaller exact/modality-specific subqueries.

Bu bolme karari, ScienceDirect arayuz sinirina uyarken O-ISAC exact phrase, FSO/OWC, VLC/LiFi, fiber, photonic-THz ve photonic-assisted/microwave photonic hatlarini ayri ayri test etmek icin alindi. Bu pilot sonuclar supplementary platform source coverage/noise assessment icindir; included studies, screening count veya final PRISMA flow count uretmez.

### Package placement

ScienceDirect pilot paketi icin beklenen kanonik konumlar:

- Raw ScienceDirect txt exports: `systematic_review_workflow/02_arama/raw_exports/sciencedirect/pilot_2026-06-19/`
- Audit CSV package: `systematic_review_workflow/02_arama/audits/sciencedirect/pilot_2026-06-19/`

2026-06-20 repo kontrolunde `SD-PILOT-*.txt` ham export dosyalari bu repo icinde bulunamadi. Mevcut ScienceDirect CSV/audit dosyalari su konumlarda listelendi; bu CSV'ler derived audit files olarak kabul edilir, raw export yerine gecmez:

- `systematic_review_workflow/02_arama/raw_exports/pilot_2026-06-19/sciencedirect/`
- `systematic_review_workflow/02_arama/audits/pilot_2026-06-19/sciencedirect/`
- `systematic_review_workflow/02_arama/sciencedirect_pilot_summary_2026-06-19.md`

### Query-level pilot counts

| Search ID | Input file | Parsed rows | Unique within query | Search string status |
|---|---|---:|---:|---|
| SD-PILOT-P1 | `SD-PILOT-P1.txt` | 9 | 9 | pending exact ScienceDirect history/user confirmation |
| SD-PILOT-P2A | `SD-PILOT-P2A.txt` | 59 | 59 | query text available in package |
| SD-PILOT-P2B | `SD-PILOT-P2B.txt` | 67 | 67 | query text available in package |
| SD-PILOT-P2C | `SD-PILOT-P2C.txt` | 89 | 89 | query text available in package |
| SD-PILOT-P2D | `SD-PILOT-P2D.txt` | 5 | 5 | query text available in package |
| SD-PILOT-P2E | `SD-PILOT-P2E.txt` | 10 | 10 | query text available in package |
| SD-PILOT-P3 | `SD-PILOT-P3.txt` | 11 | 11 | pending exact ScienceDirect history/user confirmation |
| SD-PILOT-P4 | `SD-PILOT-P4.txt` | 100 | 100 | pending exact ScienceDirect history/user confirmation |

Aggregate audit diagnostics:

- ScienceDirect all parsed pilot rows: 350.
- ScienceDirect unique pilot records after DOI/title deduplication: 172.

These are pilot diagnostics only and must not be entered into PRISMA flow counts.

### ScienceDirect pilot query appendix

#### SD-PILOT-P1

```text
"optical integrated sensing and communication" OR "optical ISAC" OR "O-ISAC" OR OISAC
```

#### SD-PILOT-P2A

```text
("integrated sensing and communication" OR ISAC) AND ("free-space optical" OR "optical wireless" OR FSO OR OWC)
```

#### SD-PILOT-P2B

```text
("integrated sensing and communication" OR ISAC) AND ("visible light communication" OR VLC OR LiFi)
```

#### SD-PILOT-P2C

```text
("integrated sensing and communication" OR ISAC) AND ("optical fiber" OR "fiber optic" OR "optical fibre")
```

#### SD-PILOT-P2D

```text
("integrated sensing and communication" OR ISAC) AND ("photonic THz" OR "photonic terahertz" OR "THz-over-fiber")
```

#### SD-PILOT-P2E

```text
(ISAC OR "joint radar and communication") AND ("photonic-assisted" OR "photonics-assisted" OR "microwave photonic")
```

#### SD-PILOT-P3

```text
query_string_pending_from_sciencedirect_raw_txt
```

#### SD-PILOT-P4

```text
query_string_pending_from_sciencedirect_raw_txt
```

### ScienceDirect query string status

Query strings for SD-PILOT-P1, SD-PILOT-P2A, SD-PILOT-P2B, SD-PILOT-P2C, SD-PILOT-P2D and SD-PILOT-P2E were entered into `search_log.csv`.

Exact UI query strings for SD-PILOT-P3 and SD-PILOT-P4 were not available from raw txt files during the 2026-06-20 local check. Their `search_log.csv` search string remains:

```text
query_string_pending_from_sciencedirect_raw_txt
```

TODO:

- Recover or confirm exact ScienceDirect UI query strings for SD-PILOT-P3 and SD-PILOT-P4 from user-provided raw txt exports.
- Restore or place the eight raw ScienceDirect txt exports under `systematic_review_workflow/02_arama/raw_exports/sciencedirect/pilot_2026-06-19/` if they are available outside this repo.
- Decide whether SD-PILOT-P3 and SD-PILOT-P4 should remain supplementary rescue/sensitivity queries or be dropped before final supplementary search.
- Treat automated relevance labels in the package as audit/readiness labels only, not screening decisions.
- Keep review/survey records contextual and outside primary technical evidence.

## 11. SpringerLink Pilot Search - 2026-06-21

Bu bolum SpringerLink supplementary platform pilot search ciktisini kaydeder. SpringerLink supplementary platform source olarak test edildi. Sonuclar pilot kayitlaridir; final search execution, formal screening karari veya PRISMA flow count degildir.

Chapter records primary technical evidence sayilmayacaktir. Review/survey ve chapter kayitlari ancak daha sonra contextual corpus olarak gerekcelendirilirse kullanilabilir.

### Package placement

SpringerLink pilot paketi icin beklenen kanonik konumlar:

- Raw SpringerLink exports: `systematic_review_workflow/02_arama/raw_exports/springerlink/pilot_2026-06-21/`
- Audit CSV package: `systematic_review_workflow/02_arama/audits/springerlink/pilot_2026-06-21/`

Raw export klasorunde bulunan dosyalar:

- `SPR-PILOT-P1B.csv`
- `SPR-PILOT-P2A.csv`
- `SPR-PILOT-P2B.csv`
- `SPR-PILOT-P2C.csv`
- `SPR-PILOT-P2D.csv`
- `SPR-PILOT-P2E.csv`

Not: `springer.zip` ve `SPR-PILOT-P1A.csv` local repo kontrolunde raw export klasorunde bulunamadi. `SPR-PILOT-P1A` missing/TODO olarak kalir; query/export uydurulmayacaktir.

Audit klasorunde bulunan dosyalar:

- `springer_pilot_audit_package_2026-06-21.zip`
- `springer_pilot_all_rows_audit_2026-06-21.csv`
- `springer_pilot_unique_records_audit_2026-06-21.csv`
- `springer_pilot_query_summary_2026-06-21.csv`
- `springer_pilot_audit_summary_2026-06-21.md`

### Query-level pilot counts

| Search ID | Input file | Exported rows | Unique within query | Preliminary decision |
|---|---|---:|---:|---|
| SPR-PILOT-P1B | `SPR-PILOT-P1B.csv` | 4 | 4 | noisy / rescue only; false positives present |
| SPR-PILOT-P2A | `SPR-PILOT-P2A.csv` | 44 | 44 | noisy / rescue query candidate |
| SPR-PILOT-P2B | `SPR-PILOT-P2B.csv` | 40 | 40 | noisy / VLC-LiFi rescue query candidate |
| SPR-PILOT-P2C | `SPR-PILOT-P2C.csv` | 58 | 58 | useful focused fiber/O-ISAC query candidate |
| SPR-PILOT-P2D | `SPR-PILOT-P2D.csv` | 1 | 1 | useful focused photonic-THz candidate |
| SPR-PILOT-P2E | `SPR-PILOT-P2E.csv` | 12 | 12 | useful focused photonic-assisted/microwave photonic candidate |
| SPR-PILOT-P1A | not present | TBD | TBD | missing / TODO |

Aggregate audit diagnostics:

- SpringerLink raw exported rows: 159.
- SpringerLink unique deduplicated records: 126.
- Duplicate groups across SpringerLink pilot exports: 29.

These are pilot diagnostics only and must not be entered into PRISMA flow counts.

### SpringerLink pilot query appendix

#### SPR-PILOT-P1B

```text
"optical ISAC" OR "O-ISAC" OR OISAC
```

#### SPR-PILOT-P2A

```text
("integrated sensing and communication" OR ISAC) AND ("free-space optical" OR "optical wireless")
```

#### SPR-PILOT-P2B

```text
("integrated sensing and communication" OR ISAC) AND ("visible light communication" OR LiFi OR VLC)
```

#### SPR-PILOT-P2C

```text
("integrated sensing and communication" OR ISAC) AND ("optical fiber" OR "fiber optic")
```

#### SPR-PILOT-P2D

```text
("integrated sensing and communication" OR ISAC) AND ("photonic THz" OR "photonic terahertz" OR "THz-over-fiber")
```

#### SPR-PILOT-P2E

```text
(ISAC OR "joint radar and communication") AND ("photonic-assisted" OR "microwave photonic")
```

#### SPR-PILOT-P1A

```text
query_export_pending_not_present_in_uploaded_export
```

### SpringerLink decision summary

Keep candidate:

- SPR-PILOT-P2C
- SPR-PILOT-P2D
- SPR-PILOT-P2E

Noisy / rescue only:

- SPR-PILOT-P1B
- SPR-PILOT-P2A
- SPR-PILOT-P2B

Missing / TODO:

- SPR-PILOT-P1A

### TODO

- Recover or confirm `SPR-PILOT-P1A` query/export if available outside the uploaded package.
- Check SpringerLink overlap against IEEE Xplore, Scopus and ScienceDirect pilot records.
- Decide whether SPR-PILOT-P1B, SPR-PILOT-P2A and SPR-PILOT-P2B should remain rescue/sensitivity queries before final supplementary search.
- Treat automated relevance labels in the audit package as audit/readiness labels only, not screening decisions.
- Keep chapter records outside primary technical evidence.

## 12. Wiley Online Library Pilot Search - 2026-06-21

Bu bolum Wiley Online Library supplementary platform pilot search ciktisini kaydeder. Wiley Online Library supplementary platform source olarak test edildi. Sonuclar pilot kayitlaridir; final search execution, formal screening karari veya PRISMA flow count degildir.

Review/survey/chapter/contextual records primary technical evidence sayilmayacaktir. Bu kayitlar ancak daha sonra contextual corpus olarak gerekcelendirilirse kullanilabilir.

### Package placement

Wiley pilot paketi icin beklenen kanonik konumlar:

- Raw Wiley exports: `systematic_review_workflow/02_arama/raw_exports/wiley/pilot_2026-06-21/`
- Audit CSV package: `systematic_review_workflow/02_arama/audits/wiley/pilot_2026-06-21/`

Raw export klasorunde bulunan dosyalar:

- `wiley.zip`
- `wly_pilot_p1a.txt`
- `wly_pilot_p1b.txt`
- `wly_pilot_p2a.txt`
- `wly_pilot_p2b.txt`
- `wly_pilot_p2c.txt`
- `wly_pilot_p2d.txt`
- `wly_pilot_p2e.txt`

Audit klasorunde bulunan dosyalar:

- `wiley_pilot_audit_package_2026-06-21.zip`
- `wiley_pilot_all_rows_audit_2026-06-21.csv`
- `wiley_pilot_unique_records_audit_2026-06-21.csv`
- `wiley_pilot_query_summary_2026-06-21.csv`
- `wiley_pilot_audit_summary_2026-06-21.md`

### Query-level pilot counts

| Search ID | Input file | Exported rows | Unique within query | Preliminary decision |
|---|---|---:|---:|---|
| WLY-PILOT-P1A | `wly_pilot_p1a.txt` | 1 | 1 | likely false positive / deprioritize |
| WLY-PILOT-P1B | `wly_pilot_p1b.txt` | 5 | 5 | noisy exact-variant query; rescue/sensitivity candidate |
| WLY-PILOT-P2A | `wly_pilot_p2a.txt` | 16 | 16 | useful but mixed/noisy; supplementary candidate with screening |
| WLY-PILOT-P2B | `wly_pilot_p2b.txt` | 11 | 11 | mostly VLC/IRS communication noise; rescue only |
| WLY-PILOT-P2C | `wly_pilot_p2c.txt` | 19 | 19 | mixed; includes IOSAC/fiber-photonic signal; rescue/sensitivity candidate |
| WLY-PILOT-P2D | `wly_pilot_p2d.txt` | 3 | 3 | small focused photonic-THz candidate |
| WLY-PILOT-P2E | `wly_pilot_p2e.txt` | 2 | 2 | small focused photonic-assisted/microwave photonic candidate |

Aggregate audit diagnostics:

- Wiley raw exported rows: 57.
- Wiley unique deduplicated records: 49.
- Duplicate groups across Wiley pilot exports: 7.

These are pilot diagnostics only and must not be entered into PRISMA flow counts.

### Wiley pilot query appendix

#### WLY-PILOT-P1A

```text
"optical integrated sensing and communication"
```

#### WLY-PILOT-P1B

```text
"optical ISAC" OR "O-ISAC" OR OISAC
```

#### WLY-PILOT-P2A

```text
("integrated sensing and communication" OR ISAC) AND ("free-space optical" OR "optical wireless")
```

#### WLY-PILOT-P2B

```text
("integrated sensing and communication" OR ISAC) AND ("visible light communication" OR LiFi OR VLC)
```

#### WLY-PILOT-P2C

```text
("integrated sensing and communication" OR ISAC) AND ("optical fiber" OR "fiber optic")
```

#### WLY-PILOT-P2D

```text
("integrated sensing and communication" OR ISAC) AND ("photonic THz" OR "photonic terahertz" OR "THz-over-fiber")
```

#### WLY-PILOT-P2E

```text
(ISAC OR "joint radar and communication") AND ("photonic-assisted" OR "microwave photonic")
```

### Wiley decision summary

Keep candidate:

- WLY-PILOT-P2D
- WLY-PILOT-P2E

Keep as supplementary/rescue candidate with screening:

- WLY-PILOT-P1B
- WLY-PILOT-P2A
- WLY-PILOT-P2C

Rescue only / noisy:

- WLY-PILOT-P2B

Likely drop or deprioritize:

- WLY-PILOT-P1A

### TODO

- Check Wiley overlap against IEEE Xplore, Scopus, ScienceDirect and SpringerLink pilot records.
- Decide whether WLY-PILOT-P1B, WLY-PILOT-P2A and WLY-PILOT-P2C should remain rescue/sensitivity queries before final supplementary search.
- Keep WLY-PILOT-P2D and WLY-PILOT-P2E as focused candidates for final supplementary search design.
- Keep WLY-PILOT-P2B rescue-only unless final VLC/LiFi coverage is weak.
- Treat automated relevance labels in the audit package as audit/readiness labels only, not screening decisions.

## 13. Known Studies Check

### Taylor & Francis Online Pilot Search — 2026-06-22

- **Platform:** Taylor & Francis Online  
- **Source role:** supplementary platform source  
- **Search/export date:** 2026-06-22  
- **Search status:** pilot only  
- **Raw exports:** TF-PILOT-P2A, TF-PILOT-P2B, TF-PILOT-P2C  
- **Audit package location:** `systematic_review_workflow/02_arama/audits/taylorfrancis/pilot_2026-06-22/`  
- **Note:** Pilot counts are **not** PRISMA flow counts. These results are not formal screening decisions. Taylor & Francis Online produced low‑yield and noisy results in this pilot round.  

## 13. Known Studies Check

`known_studies_check.csv`, formal seed set olarak kullanilmayacaktir. Legacy `included_studies_canonical.csv` formal PRISMA workflow icinde seed set degildir. Gerekirse bu dosya yalnizca sensitivity/known studies check icin, yani sorgunun fiber, FSO, VLC/LiFi, photonic-THz ve hybrid optical systems literaturunu yeterince yakalayip yakalamadigini sinamak amaciyla kullanilacaktir; included studies, screening count veya PRISMA flow count uretmez.
