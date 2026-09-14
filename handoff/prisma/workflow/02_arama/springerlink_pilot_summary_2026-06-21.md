# SpringerLink Pilot Summary - 2026-06-21

Bu dosya, SpringerLink supplementary platform pilot search ciktisini workflow icinde izlenebilir kilmak icin olusturuldu. Bu kayitlar pilot/audit kayitlaridir; final search execution, formal screening karari veya PRISMA flow count degildir.

## Genel Bilgi

- Platform: SpringerLink
- Source role: supplementary platform source
- Search date/export date: 2026-06-21
- Search freeze label: planned search freeze date: June 30, 2026
- Raw exported rows: 159
- Unique deduplicated records: 126
- Duplicate groups: 29
- Missing export: SPR-PILOT-P1A

## Dosya Konumlari

Ham SpringerLink pilot CSV dosyalari:

```text
systematic_review_workflow/02_arama/raw_exports/springerlink/pilot_2026-06-21/
```

Bu klasorde bulunan dosyalar:

- `SPR-PILOT-P1B.csv`
- `SPR-PILOT-P2A.csv`
- `SPR-PILOT-P2B.csv`
- `SPR-PILOT-P2C.csv`
- `SPR-PILOT-P2D.csv`
- `SPR-PILOT-P2E.csv`

Not: `springer.zip` ve `SPR-PILOT-P1A.csv` local repo kontrolunde bu ham export klasorunde bulunamadi. `SPR-PILOT-P1A` missing/TODO olarak kalir; query/export uydurulmayacaktir.

Audit dosyalari:

```text
systematic_review_workflow/02_arama/audits/springerlink/pilot_2026-06-21/
```

Bu klasorde bulunan audit dosyalari:

- `springer_pilot_audit_package_2026-06-21.zip`
- `springer_pilot_all_rows_audit_2026-06-21.csv`
- `springer_pilot_unique_records_audit_2026-06-21.csv`
- `springer_pilot_query_summary_2026-06-21.csv`
- `springer_pilot_audit_summary_2026-06-21.md`

## Pilot Sorgular

### SPR-PILOT-P1B

```text
"optical ISAC" OR "O-ISAC" OR OISAC
```

Exported rows: 4.

### SPR-PILOT-P2A

```text
("integrated sensing and communication" OR ISAC) AND ("free-space optical" OR "optical wireless")
```

Exported rows: 44.

### SPR-PILOT-P2B

```text
("integrated sensing and communication" OR ISAC) AND ("visible light communication" OR LiFi OR VLC)
```

Exported rows: 40.

### SPR-PILOT-P2C

```text
("integrated sensing and communication" OR ISAC) AND ("optical fiber" OR "fiber optic")
```

Exported rows: 58.

### SPR-PILOT-P2D

```text
("integrated sensing and communication" OR ISAC) AND ("photonic THz" OR "photonic terahertz" OR "THz-over-fiber")
```

Exported rows: 1.

### SPR-PILOT-P2E

```text
(ISAC OR "joint radar and communication") AND ("photonic-assisted" OR "microwave photonic")
```

Exported rows: 12.

### SPR-PILOT-P1A

```text
query_export_pending_not_present_in_uploaded_export
```

Exported rows: TBD. The export was not present in the uploaded SpringerLink package.

## Decision Summary

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

## Preliminary Observation

SpringerLink includes a small number of useful O-ISAC records but is generally noisy, with chapters, general ISAC/6G, and non-optical false positives. Chapter records are not primary technical evidence under the current protocol. Review/survey and chapter records may be retained only as contextual corpus if later screening justifies contextual use.

## Guardrails

- Pilot counts are not PRISMA flow counts.
- Audit files are not formal screening decisions.
- SpringerLink pilot records must not be treated as included studies.
- Final source counts, deduplication counts, screening decisions and included-study counts remain TBD until formal search execution, deduplication and screening.
