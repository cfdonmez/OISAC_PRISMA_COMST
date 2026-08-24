# Electronic Supplement ST-01

ST-01 implements the PRISMA 2020 study/report distinction for this survey. The inclusion unit is 206 unique studies; those studies are represented by 227 eligible reports (206 primary and 21 companion reports).

## Files

- ST01_INCLUDED_STUDIES_206.csv and .tex: one row per included study; each row cites all eligible reports linked to the study.
- ST01_ELIGIBLE_REPORT_LINEAGE_227.csv: one row per eligible report with a unique report_citation_key, direct source URL, extracted-data counts, and synthesis gate.
- ST01_COMPANION_REPORT_PROVENANCE_21.csv and .tex: exact report-level provenance for all 21 companions.
- ST01_COMPANION_GUARDRAIL_METRICS_14.csv: the 14 companion metrics that must remain report specific.
- ST01_REFERENCES_227.bib: standalone bibliography resolving all 227 report keys.
- ST01_REFERENCES_206.bib: synchronized primary-report-only compatibility bibliography.
- INCLUDED_STUDIES_206_EXPLICIT_BIBLIOGRAPHY.tex: explicit enumeration of all 227 eligible-report keys; no wildcard inclusion.
- ST01_INCLUDED_STUDIES_206.xlsx: styled workbook view of the governed tables.
- ST01_SUPPLEMENT_DRIVER.tex and .pdf: standalone electronic supplement.

## Adjudication-aware synthesis gate

A pending-human token triggers exclusion only when the same row lacks resolved or approved adjudication. The 59 historical tokens in SCR-00083 and SCR-00553 are resolved or approved; they are not automatically quarantined. Report-specific conflict guardrails remain active, and any future unresolved pending row cannot support numerical, tradeoff, or prevalence synthesis.

## Bibliography carriers

The manuscript-level primary carrier is ../../references_206_candidate.bib; the duplicate-free companion carrier is ../../references_companion_21_candidate.bib. The standalone ST-01 driver uses the combined 227-entry ST01_REFERENCES_227.bib.
