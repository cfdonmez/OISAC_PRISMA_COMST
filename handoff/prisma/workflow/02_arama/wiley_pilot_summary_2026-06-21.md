# Wiley Online Library Pilot Summary - 2026-06-21

Bu dosya, Wiley Online Library supplementary platform pilot search ciktisini workflow icinde izlenebilir kilmak icin olusturuldu. Bu kayitlar pilot/audit kayitlaridir; final search execution, formal screening karari veya PRISMA flow count degildir.

## Genel Bilgi

- Platform: Wiley Online Library
- Source role: supplementary platform source
- Search/export date: 2026-06-21
- Search freeze label: planned search freeze date: June 30, 2026
- Raw exported rows: 57
- Unique deduplicated records: 49
- Duplicate groups: 7

## Dosya Konumlari

Ham Wiley pilot dosyalari:

```text
systematic_review_workflow/02_arama/raw_exports/wiley/pilot_2026-06-21/
```

Bu klasorde bulunan dosyalar:

- `wiley.zip`
- `wly_pilot_p1a.txt`
- `wly_pilot_p1b.txt`
- `wly_pilot_p2a.txt`
- `wly_pilot_p2b.txt`
- `wly_pilot_p2c.txt`
- `wly_pilot_p2d.txt`
- `wly_pilot_p2e.txt`

Audit dosyalari:

```text
systematic_review_workflow/02_arama/audits/wiley/pilot_2026-06-21/
```

Bu klasorde bulunan audit dosyalari:

- `wiley_pilot_audit_package_2026-06-21.zip`
- `wiley_pilot_all_rows_audit_2026-06-21.csv`
- `wiley_pilot_unique_records_audit_2026-06-21.csv`
- `wiley_pilot_query_summary_2026-06-21.csv`
- `wiley_pilot_audit_summary_2026-06-21.md`

## Pilot Sorgular

### WLY-PILOT-P1A

```text
"optical integrated sensing and communication"
```

Exported rows: 1.

### WLY-PILOT-P1B

```text
"optical ISAC" OR "O-ISAC" OR OISAC
```

Exported rows: 5.

### WLY-PILOT-P2A

```text
("integrated sensing and communication" OR ISAC) AND ("free-space optical" OR "optical wireless")
```

Exported rows: 16.

### WLY-PILOT-P2B

```text
("integrated sensing and communication" OR ISAC) AND ("visible light communication" OR LiFi OR VLC)
```

Exported rows: 11.

### WLY-PILOT-P2C

```text
("integrated sensing and communication" OR ISAC) AND ("optical fiber" OR "fiber optic")
```

Exported rows: 19.

### WLY-PILOT-P2D

```text
("integrated sensing and communication" OR ISAC) AND ("photonic THz" OR "photonic terahertz" OR "THz-over-fiber")
```

Exported rows: 3.

### WLY-PILOT-P2E

```text
(ISAC OR "joint radar and communication") AND ("photonic-assisted" OR "microwave photonic")
```

Exported rows: 2.

## Decision Summary

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

## Preliminary Observation

Wiley produced a small and manageable supplementary set, with some strong O-ISAC / photonic-assisted / THz ISAC candidates but also false positives and general communication or sensing noise. Review/survey/chapter/contextual records are not primary technical evidence under the current protocol.

## Guardrails

- Pilot counts are not PRISMA flow counts.
- Audit files are not formal screening decisions.
- Wiley pilot records must not be treated as included studies.
- Final source counts, deduplication counts, screening decisions and included-study counts remain TBD until formal search execution, deduplication and screening.
