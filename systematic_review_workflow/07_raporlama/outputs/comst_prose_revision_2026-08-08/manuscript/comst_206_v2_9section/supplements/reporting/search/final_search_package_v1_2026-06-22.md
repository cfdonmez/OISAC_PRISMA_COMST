# O-ISAC Final Search Package V1

## Status

Bu dosya final search execution degildir. Bu dosya Step 2D kapsaminda final search package draft ve execution readiness hazirligi icin olusturuldu.

- actual final search cutoff: June 22, 2026
- Previous planned search freeze date June 30, 2026 was advanced by user decision on 2026-06-22.
- Final search execution basladi; export collection henuz tamamlanmadi.
- Deduplication henuz baslamadi.
- Title/abstract screening veya full-text assessment henuz baslamadi.
- Included studies listesi olusturulmadi.
- Pilot counts final PRISMA flow count degildir.

## Core Sources

### IEEE Xplore

Final core candidate queries:

- IEEE-FINAL-S1A derived from IEEE-PILOT-S1A
- IEEE-FINAL-S1B derived from IEEE-PILOT-S1B-R2
- IEEE-FINAL-S1F derived from IEEE-PILOT-S1F-R2

IEEE final query strings, Step 2B icinde chat log/search_log uzerinden kaydedilen IEEE pilot query stringlerinden turetilmistir.

#### IEEE-FINAL-S1A

Derived from IEEE-PILOT-S1A.

```text
"All Metadata":"O-ISAC" OR "All Metadata":OISAC OR "All Metadata":"optical ISAC" OR "All Metadata":"optical integrated sensing and communication" OR "All Metadata":"integrated optical sensing and communication" OR "All Metadata":"joint optical communication and sensing" OR "All Metadata":"optical joint communication and sensing"
```

#### IEEE-FINAL-S1B

Derived from IEEE-PILOT-S1B-R2.

```text
("Document Title":"integrated sensing and communication" OR "Document Title":"integrated sensing and communications" OR "Document Title":ISAC OR "Document Title":"joint sensing and communication" OR "Document Title":"joint communication and sensing" OR "Document Title":"sensing-communication" OR "Document Title":"communication-sensing" OR "Abstract":"integrated sensing and communication" OR "Abstract":"integrated sensing and communications" OR "Abstract":ISAC OR "Abstract":"joint sensing and communication" OR "Abstract":"joint communication and sensing" OR "Abstract":"sensing-communication" OR "Abstract":"communication-sensing")
AND
("Document Title":optical OR "Document Title":photonic OR "Document Title":"free-space optical" OR "Document Title":FSO OR "Document Title":VLC OR "Document Title":LiFi OR "Document Title":"visible light communication" OR "Document Title":"optical wireless" OR "Document Title":"optical fiber" OR "Document Title":"photonic THz" OR "Abstract":optical OR "Abstract":photonic OR "Abstract":"free-space optical" OR "Abstract":FSO OR "Abstract":VLC OR "Abstract":LiFi OR "Abstract":"visible light communication" OR "Abstract":"optical wireless" OR "Abstract":"optical fiber" OR "Abstract":"photonic THz")
```

#### IEEE-FINAL-S1F

Derived from IEEE-PILOT-S1F-R2.

```text
("Document Title":"photonic THz" OR "Document Title":"photonic terahertz" OR "Document Title":"photonic mmWave" OR "Document Title":"photonic millimeter wave" OR "Document Title":"microwave photonic" OR "Document Title":"THz-over-fiber" OR "Document Title":"photonics-assisted" OR "Document Title":"photonic-assisted" OR "Document Title":"photonic-aided" OR "Abstract":"photonic THz" OR "Abstract":"photonic terahertz" OR "Abstract":"photonic mmWave" OR "Abstract":"photonic millimeter wave" OR "Abstract":"microwave photonic" OR "Abstract":"THz-over-fiber" OR "Abstract":"photonics-assisted" OR "Abstract":"photonic-assisted" OR "Abstract":"photonic-aided")
AND
("Document Title":"integrated sensing and communication" OR "Document Title":"integrated sensing and communications" OR "Document Title":ISAC OR "Document Title":"joint radar communication" OR "Document Title":"joint radar-communication" OR "Document Title":"joint radar and communication" OR "Document Title":"joint communication and radar" OR "Abstract":"integrated sensing and communication" OR "Abstract":"integrated sensing and communications" OR "Abstract":ISAC)
```

### Scopus

Final core candidate queries:

- SCO-FINAL-S1A - canonical exact O-ISAC phrase query
- SCO-FINAL-S1B - recovered generic optical ISAC query
- SCO-FINAL-S1F - recovered photonic THz / microwave photonic query

Not: SCO-FINAL-S1A planned canonical final query olarak tanimlanmistir; SCO-PILOT-S1A exact query Scopus history'den recovered pilot query olarak alinmamistir. Bu nedenle SCO-FINAL-S1A bagimsiz metodolojik inceleme gerektirir.

Scopus pilot count mismatch artik Step 2D pilot consolidation icin bloklayici degildir. Final search execution sirasinda on-screen count ve exported row count birlikte kaydedilecektir.

#### SCO-FINAL-S1A

```text
TITLE-ABS-KEY(
  (
    "O-ISAC"
    OR OISAC
    OR "optical ISAC"
    OR "optical integrated sensing and communication"
    OR "integrated optical sensing and communication"
    OR "joint optical communication and sensing"
    OR "optical joint communication and sensing"
  )
)
```

#### SCO-FINAL-S1B

```text
TITLE-ABS-KEY(
  (
    "integrated sensing and communication"
    OR "integrated sensing and communications"
    OR ISAC
    OR "joint sensing and communication"
    OR "joint communication and sensing"
    OR "sensing-communication"
    OR "communication-sensing"
  )
  AND
  (
    optical
    OR photonic
    OR "free-space optical"
    OR FSO
    OR "optical wireless"
    OR OWC
    OR VLC
    OR LiFi
    OR "visible light communication"
    OR "visible light communications"
    OR "optical camera communication"
    OR OCC
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
    OR "THz-over-fiber"
    OR "terahertz-over-fiber"
    OR "microwave photonic"
    OR "microwave photonics"
  )
)
```

#### SCO-FINAL-S1F

```text
TITLE-ABS-KEY(
  (
    "photonic THz"
    OR "photonic terahertz"
    OR "photonic mmWave"
    OR "photonic millimeter wave"
    OR "microwave photonic"
    OR "microwave photonics"
    OR "THz-over-fiber"
    OR "terahertz-over-fiber"
    OR "photonics-assisted"
    OR "photonic-assisted"
    OR "photonic-aided"
  )
  AND
  (
    "integrated sensing and communication"
    OR "integrated sensing and communications"
    OR ISAC
    OR "joint radar communication"
    OR "joint radar-communication"
    OR "joint radar and communication"
    OR "joint communication and radar"
    OR "joint sensing and communication"
    OR "joint communication and sensing"
  )
)
```

## Supplementary Platform Sources

### ScienceDirect

Recommended:

- SD-PILOT-P2D
- SD-PILOT-P2E

Rescue/sensitivity:

- SD-PILOT-P1
- SD-PILOT-P2A
- SD-PILOT-P2B
- SD-PILOT-P2C

Pending/drop unless recovered:

- SD-PILOT-P3
- SD-PILOT-P4

### SpringerLink

Recommended:

- SPR-PILOT-P2C
- SPR-PILOT-P2D
- SPR-PILOT-P2E

Rescue:

- SPR-PILOT-P1B
- SPR-PILOT-P2A
- SPR-PILOT-P2B

Drop/pending:

- SPR-PILOT-P1A

### Wiley Online Library

Recommended:

- WLY-PILOT-P2D
- WLY-PILOT-P2E

Rescue/sensitivity:

- WLY-PILOT-P1B
- WLY-PILOT-P2A
- WLY-PILOT-P2C

Rescue-only:

- WLY-PILOT-P2B

Drop/deprioritize:

- WLY-PILOT-P1A

### Taylor & Francis Online

Overall role: optional tight exact-phrase supplementary source only.

Use only if final team decides extra tight phrase coverage is needed. Broad P2B/P2C style queries are deprioritized.

## Dropped or Rejected Pilot Queries

- IEEE-PILOT-S1B
- IEEE-PILOT-S1B-R1
- IEEE-PILOT-S1C-R1
- IEEE-PILOT-S1D-R1
- IEEE-PILOT-S1E-R1
- IEEE-PILOT-S1F-R1
- WLY-PILOT-P1A
- TF-PILOT-P2B
- TF-PILOT-P2C
- SD-PILOT-P3 and SD-PILOT-P4 unless exact query strings are recovered and explicitly retained
- SPR-PILOT-P1A unless export/query is recovered

## Filters

Use:

- Years: 2020-2026
- Language: English
- Document types: journal article, early-access article, full-length conference/proceedings paper; review/survey contextual only.
- Date eligibility: records published or made available after June 22, 2026 will be excluded during date eligibility screening.

Review/survey/chapter records must not be counted as primary technical evidence. They may be handled only as contextual corpus if later justified.

## Method-ready English note

> "The final search will be conducted in Scopus and IEEE Xplore as core sources, supplemented by controlled platform searches in ScienceDirect, SpringerLink, Wiley Online Library, and Taylor & Francis Online. Pilot searches were used only to refine query specificity and source roles; pilot counts were not used as PRISMA flow counts."

## Not Yet Done

- final export collection completion
- deduplication
- title/abstract screening
- full-text screening
- included studies list
- PRISMA flow counts
- data extraction
