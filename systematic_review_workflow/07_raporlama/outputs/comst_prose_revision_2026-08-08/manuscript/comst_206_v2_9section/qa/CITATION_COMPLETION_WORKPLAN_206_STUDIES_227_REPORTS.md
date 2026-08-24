# Citation Completion Work Plan: 206 Studies and 227 Reports

**Status: COMPLETE (2026-08-16).** The starting-point counts below are retained
as an audit baseline; the completion record at the end gives the active state.

## Objective

Make every included study visible through at least one scientifically matched citation in the main article, while preserving the distinction between 206 unique studies and 227 eligible reports. Citations will be attached to claims, synthesis categories, or main-table rows; they will not be added through `\nocite`, manual reference numbers, inventory footnotes, or undifferentiated citation dumps.

## Frozen starting point

- Included studies: 206.
- Eligible reports: 227, comprising 206 primary reports and 21 companion reports across 19 multi-report studies.
- Included studies currently cited in the active manuscript: 77.
- Included studies not yet cited in the active manuscript: 129.
- Current included-study key uses: 171, comprising 128 prose uses and 43 table uses.
- Context, method, standard, and tool sources currently cited: 29.
- Current claim-fit audit: 73 included studies have a suitable prose context; four appear only in scientifically matching application-table rows; no clear claim-to-citation mismatch was found.
- Missing studies by modality: photonic THz 54, fiber 32, VLC/LiFi 22, FSO 17, hybrid optical 4, other optical 0.

## Editorial rules

1. Every included study receives one required primary narrative citation home.
2. Existing citations are retained only when the surrounding claim matches the study evidence.
3. A study may be cited again only when it supports a genuinely different synthesis, such as validation maturity or paired-function evidence.
4. Citation clusters are formed by one shared technical proposition. A cluster will normally contain three to seven studies and will be split when the studies differ in mechanism, measurement plane, validation setting, or application requirement.
5. No citation is added solely to trigger a bibliography entry.
6. No manual `[n]` numbers, citation-only footnotes, or `\nocite` commands are used.
7. Counts and prevalence remain study based. Companion reports never create additional studies.
8. The 402-row substantive tradeoff view, not the two audit-sentinel rows in the 404-row governed ledger, controls tradeoff-support claims.

## Phase 1: Build the placement crosswalk

Create a 206-row crosswalk with these fields:

- stable study ID and citation key;
- canonical modality and integration mechanisms;
- substantive tradeoff family, when present;
- validation maturity and validation methods;
- enabling technologies, applications, and 6G relevance;
- current citation locations;
- required primary narrative home;
- optional secondary home and justification;
- exact sentence or table-row claim to be supported;
- companion report IDs and source-specific provenance flags;
- implementation and QA status.

Placement priority for an uncited study:

1. Section V when the study contributes a substantive, condition-preserving tradeoff record;
2. Section VI when its distinguishing contribution is validation maturity, field evidence, artifact availability, or benchmark design;
3. Section VII when its strongest contribution is an enabling technology, application bundle, deployment setting, or 6G relationship;
4. Section IV when its strongest contribution is the physical platform, signal path, or integration mechanism.

Section IV remains the canonical modality traceability anchor for all 206 studies, but the same study is not repeated there when a stronger primary narrative citation already exists elsewhere.

## Phase 2: Design claim-linked clusters

For each target subsection:

1. identify the proposition already made by the prose;
2. identify every study that genuinely supports that proposition;
3. divide heterogeneous studies by mechanism, operating condition, or evidence type;
4. revise the prose only as much as needed to explain the grouping;
5. attach the citations to the narrowest valid sentence or table row;
6. replace overused examples when a broader set supplies the same evidence.

Primary implementation order:

1. Section IV: platform and integration gaps;
2. Section V: metrics and substantive tradeoff families;
3. Section VI: maturity, field evidence, artifacts, and benchmarks;
4. Section VII: technologies, applications, and 6G implications;
5. Section II and Section VIII: only evidence-specific anchors that cannot be placed more naturally in Sections IV--VII.

Introduction, Methods, and Conclusion will not carry completeness citation trains.

## Phase 3: Complete report-level provenance

The 21 companion reports contribute 95 primary-evidence rows, 123 metric rows, and nine tradeoff rows. They therefore require report-level bibliographic visibility.

Actions:

1. assign a unique report citation key to every one of the 227 eligible reports;
2. create a 227-entry report bibliography for ST-01;
3. retain 206 study rows in ST-01, but display the primary report and all companion report citations on the relevant study row;
4. add a source-report citation key to the evidence and metric ledgers;
5. cite a companion report in the main article only when the specific claim or value comes from that report;
6. preserve report-specific definitions, conditions, and conflicts beside any companion-derived result;
7. correct manuscript wording to `227 eligible reports`, comprising 206 primary and 21 companion reports.

Fourteen companion-derived metric rows carry report-specific guardrails. These rows require the exact companion citation and the corresponding condition; they cannot be attributed generically to the study's primary report.

## Phase 4: Human-resolution evidence gate

No row with an unresolved `pending_human` state may support narrative, table, or synthesis text. A retained historical token does not reopen a row whose adjudication is explicitly `resolved_approved`; the final gate evaluates the adjudication state and verification record together. The SCR-00083/SCR-00553 multi-report study receives a dedicated audit because its primary and companion evidence require report-specific guardrails.

For each unresolved row:

1. inspect the source locator and the full report;
2. resolve the value, condition, and report role;
3. retain it with an exact citation and guardrail, quarantine it, or exclude it from synthesis;
4. record the decision in the crosswalk and QA report.

## Phase 5: Automated and manual QA

Hard automated gates:

- semantic main-article citations cover 206 of 206 study keys;
- 227 unique reports map to 206 studies;
- 206 primary reports and 21 companion reports;
- 227 unique report citation keys resolve to 227 bibliography entries;
- every evidence-source report maps to exactly one lineage row and the correct study;
- undefined citations, orphan reports, and duplicate report keys equal zero;
- `\nocite` is absent;
- audit-sentinel tradeoff rows do not support substantive claims;
- unresolved `pending_human` rows do not enter prose, tables, or synthesis, while resolved approvals remain traceable;
- study-level counts deduplicate on stable study ID.

Manual gates:

- every citation cluster supports one explicit proposition;
- titles, tasks, modality, integration, validation, and application fields agree with the sentence or table row;
- no study is cited as a demonstration when it supplies only a model, simulation, contextual condition, or absence record;
- no cluster masks conflicting definitions or operating conditions;
- paragraph cadence remains survey-like rather than catalogue-like;
- repeated citations are justified by a distinct reader function.

## Deliverables

- `qa/CITATION_PLACEMENT_CROSSWALK_206.csv`
- `supplements/st01/ST01_COMPANION_REPORT_PROVENANCE_21.csv`
- `qa/FINAL_MAIN_CITATION_COVERAGE_206.json`
- `qa/FINAL_MAIN_CITATION_COVERAGE_206.md`
- updated Section IV--VII TeX files and any evidence-specific anchors elsewhere;
- updated main bibliography;
- updated 227-report ST-01 bibliography, lineage, table, and PDF;
- a reproducible citation-coverage QA script;
- a final compiled-manuscript integrity report.

## Completion condition

The task is complete only when all 206 studies are meaningfully cited in the main article, every report-specific result points to the correct primary or companion report, ST-01 exposes all 227 reports without inflating the 206-study denominator, and both automated and close-read claim-fit audits pass.

## Completion record

- Main semantic study coverage: 206/206; missing 0.
- Included-study citation uses: 368 across 176 citation commands.
- Largest included-study citation cluster: 7; clusters above 7: 0.
- Main bibliography: 243 entries, comprising 206 included studies, 29
  contextual or methodological sources, and eight companion reports used for
  report-specific claims.
- Main companion citations: eight exact report keys attached only to claims
  derived from those reports.
- ST-01: 206 study rows, 227 eligible reports, 227 resolvable report keys, and
  227 bibliography entries.
- Companion provenance: 21 reports, 95 evidence rows, 123 metric rows, nine
  tradeoff rows, and 14 report-specific guardrail metrics.
- Unresolved pending-human evidence: 0; all 59 retained historical tokens have
  resolved or approved adjudication.
- Undefined citations, orphan reports, duplicate report keys, `\nocite`,
  manual numeric citations, and citation-bearing inventory footnotes: 0.
- Independent prose audit: PASS after two terminology corrections and a
  cadence pass that preserved the citation multiset.
