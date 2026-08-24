# PRISMA 2020 Item 17 and companion-lineage hard-gate QA

Status: **PASS**

## Governed units

- Unique included studies: 206
- Eligible reports: 227
- Primary reports: 206
- Eligible companion reports: 21
- Multi-report studies: 19
- Unique resolvable report citation keys: 227
- Bibliography entries: 227
- Orphan evidence source IDs: 0

## Companion provenance

- Exact companion provenance rows: 21
- Companion-sourced evidence rows: 95
- Companion-sourced metric rows: 123 across 20 reports
- Companion-sourced governed tradeoffs: 9 across 8 reports
- Report-specific companion metric guardrails: 14

## Adjudication-aware pending gate

SCR-00083 retains 40 historical pending-human tokens and SCR-00553 retains 19. All 59 rows record resolved or approved adjudication, so none is automatically quarantined. The hard gate is conjunctive: a pending-human token blocks synthesis only when the row lacks resolved or approved adjudication. Report-specific conflict guardrails remain in force.

## Citation architecture

ST-01A remains a 206-study table. Each row cites its designated primary report and every eligible companion report. ST-01B exposes the 21 companion reports and their exact evidence, metric, tradeoff, guardrail, and adjudication provenance. The standalone supplement resolves all 227 keys through ST01_REFERENCES_227.bib; the main manuscript loads the separate duplicate-free 21-entry companion carrier.
