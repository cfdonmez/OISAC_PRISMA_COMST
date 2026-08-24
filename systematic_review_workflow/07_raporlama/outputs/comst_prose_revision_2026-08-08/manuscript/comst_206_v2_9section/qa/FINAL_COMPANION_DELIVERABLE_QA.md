# Final companion-report deliverable QA

Status: **PASS**

## Governed counts

- Unique included studies: 206
- Eligible reports: 227
- Designated primary reports: 206
- Eligible companion reports: 21
- Unique report citation keys: 227
- Combined ST-01 BibTeX entries: 227
- Main-manuscript companion carrier entries: 21
- Standalone ST-01 bibliography items: 227
- Evidence-source orphans: 0

## Companion provenance

- Companion-sourced evidence rows: 95
- Companion-sourced metric rows: 123 across 20 reports
- Companion-sourced governed tradeoffs: 9 across 8 reports
- Report-specific companion metric guardrails: 14

Every companion row carries its study ID, report and screening IDs, report citation key, source URL, evidence/metric/tradeoff record IDs, source-workbook hash, and synthesis-use gate.

## Adjudication-aware hard gate

The hard gate is conjunctive: a historical pending-human token blocks synthesis only when the same row lacks resolved or approved adjudication. SCR-00083 retains 40 historical tokens and SCR-00553 retains 19; all 59 rows record resolved or approved adjudication, so unresolved rows equal zero. Report-specific conflict guardrails remain active.

## Duplicate and lineage audit

- Duplicate report keys: 0
- Duplicate populated DOIs: 0
- Duplicate report identities (DOI, or stable URL when DOI is absent): 0
- Bibliography metadata mismatches: 0
- Study-lineage mismatches: 0

One exact title is legitimately shared by two distinct reports in the same study: OISAC_SCR00993 (journal DOI 10.1109/jlt.2023.3311645) and OISAC_SCR01149 (conference DOI 10.1109/oecc56963.2023.10209717). The title was not falsified to manufacture uniqueness; distinct DOI, report ID, citation key, role, and same-study lineage establish separate report identities.

## Artifact verification

- ST01_SUPPLEMENT_DRIVER.pdf: 42 pages; TeX Live/latexmk and BibTeX exit 0; 227 bibliography items; zero undefined or multiply-defined citation warnings.
- ST01_INCLUDED_STUDIES_206.xlsx: six sheets; persisted artifact-tool inspection PASS; formula-error scan found zero matches; 206/227/21/14 counts reconcile.
- main.pdf: TeX Live/latexmk and BibTeX exit 0 after loading references_companion_21_candidate.bib; zero undefined or multiply-defined citation warnings.
- Visual PDF review sampled the title page, first and last ST-01A pages, first and last ST-01B pages, and first and last bibliography pages. No clipping, overlap, missing glyph, or unresolved citation was observed.

## Final SHA-256

- ST01_SUPPLEMENT_DRIVER.pdf: B04EEA78405FEE091E7CB62206F76311AC4002CBE9C2B4C9A8E1C59A4BDA4992
- ST01_INCLUDED_STUDIES_206.xlsx: F7E304D25EA9E7A6CA477121C5E4BDB6428C71DE036A0396514C26486CDACDB5
- ST01_REFERENCES_227.bib: A075D7AB476CAF39596AD413EF34582F442D44299EC0C17E2EEA27776BC4C5D5
- references_companion_21_candidate.bib: 5C88E4EA73E7F48187244BCC90A56D557382A78D894E96FC7602AF7172DD72E2
