# Scopus Final Search QA Report - 2026-06-22

Bu rapor Step 3-A Scopus final raw export logging için teknik QA kaydıdır. Audit CSV dosyaları formal screening kararı değildir ve burada yer alan raw/audit diagnostic değerleri PRISMA flow count olarak kullanılmamalıdır.

## PASS

- PASS: All three Scopus CSV exports readable.
- PASS: Query mapping clear.
- PASS: Core metadata fields present.
- PASS: DOI/title audit dedup possible.

## WARNING

- WARNING: SCO-FINAL-S1B broad/high-recall with 1128 rows.
- WARNING: Publication date field not present; 2026 records require date eligibility review against 2026-06-22 cutoff.
- WARNING: Some document types outside Article/Conference Paper/Review are present.
- WARNING: Language field not present in exported CSV; English filter must be confirmed from interface/search log.
- WARNING: Article in press records require date/publication-stage review.

## FAIL

- FAIL: None.
