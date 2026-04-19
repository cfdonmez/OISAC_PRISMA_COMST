# PRISMA 2020 Reporting Checklist

Source:

- `PRISMA 2020 Checklist`
- `PRISMA 2020 Expanded Checklist`
- `PRISMA-S`
- `screening/prisma_flow_counts.csv`
- `screening/excluded_fulltext_log.csv`
- `screening/included_studies_canonical.csv`
- `screening/fulltext_assessed_reconstruction.csv`
- `search/search_log.csv`
- `search/upstream_prisma_reconstruction_20260310.csv`
- `search/dedup_external_overlap_support_20260411.csv`
- `screening/section3_evidence_reconstruction.md`
- `screening/README.md`
- `manuscript/finalShortened/kontrol_listeleri/11_section3_impact_matrix.md`

## Review Identity

- [x] The manuscript clearly identifies itself as a systematic review.
  Note: The title/abstract/keywords explicitly identify the work as a systematic review.
- [x] The review objective is stated explicitly and consistently across abstract, introduction, and methodology.
  Note: The objective is now stated in the abstract, introduction, and Section III methodology.
- [x] The review scope is clearly bounded and aligned with the protocol.
  Note: The modality scope, optical-domain boundary, and protocol-facing review scope are now stated consistently.
- [x] The time window, domain scope, and source types are stated without ambiguity.
  Note: The manuscript now distinguishes the 2020--2025 synthesis core window from the broader protocol-eligible coverage window and states the source-type boundary clearly.

## Protocol and Registration

- [x] Protocol registration is reported with registry name, ID, and access path.
  Note: The manuscript reports OSF, registration ID `7f6wb`, and the registry access URL.
- [x] The manuscript states where the protocol can be accessed.
  Note: The OSF registry path is stated directly in Section III.
- [x] Any deviations from the registered protocol are disclosed and explained.
  Note: The manuscript now states that no substantive amendments were made after registration and that later wording changes were reporting-level clarifications only.
- [x] The protocol description in the manuscript matches the frozen review workflow.
  Note: Upstream search-stage counts remain reconstruction-supported rather than fully row-backed, but the current manuscript wording now reflects that limitation without overstating evidence strength.

## Information Sources

- [x] All formal databases used for the canonical PRISMA flow are listed.
- [x] The last search date is reported for each formal source.
  Note: The manuscript reports a shared last-search date for all three canonical databases (`November 30, 2025`), and `search/search_log.csv` records the same date per source.
- [x] Supplementary or monitoring-only sources are clearly separated from canonical PRISMA sources.
  Note: The manuscript explicitly distinguishes canonical formal databases from `arXiv` / `TechRxiv` monitoring templates and states that these supplementary sources did not add separate records to the canonical flow.
- [x] The manuscript does not imply that non-canonical sources contributed records if they did not.
  Note: The current wording explicitly states `other_sources_results = 0` and the flow figure reports identification from databases only.

## Search Strategy

- [x] The search logic is reported with enough detail to be reproducible.
  Note: The manuscript reports the concept-block logic, and the source-specific executable query templates are preserved in `search/search_strings.md`.
- [x] Any limits or filters are declared and justified.
  Note: The manuscript now states the English-language, document-type, and coverage-window limits together with their rationale, and `search/search_strings.md` records the corresponding filter policy for the frozen search stage.
- [x] Search terms, field restrictions, or query templates are available in the manuscript or supplement.
  Note: `search/search_strings.md` preserves source-specific executable query templates, field tags, and platform-level filter notes for IEEE Xplore, Scopus, and Web of Science.
- [x] PRISMA-S expectations for search transparency are satisfied.
  Note: The manuscript and supplement now report the information sources, search date, concept-block logic, limits/filters, source-specific query templates, and reconstructed search log needed for a transparent frozen search record.

## Eligibility Criteria

- [x] Inclusion criteria are explicit, technical, and domain-specific.
  Note: The manuscript defines optical-domain scope, integration logic, publication/content boundaries, and a technical-content threshold (at least one sensing metric and one communication metric) in both text and Table III-1.
- [x] Exclusion criteria are explicit, non-overlapping, and operational.
  Note: The manuscript separates RF-only studies, disjoint sensing-only/communication-only systems, non-eligible publication types, and insufficient-technical-depth papers into operational exclusion classes, with examples in both the text and Table III-1.
- [x] The manuscript explains how borderline cases were handled.
  Note: The manuscript now states the decision rule for borderline photonic-THz, hybrid, and functionally O-ISAC records and excludes optical links whose “sensing” role was limited to auxiliary channel-estimation/alignment/beam-tracking functions.
- [x] The criteria distinguish true target studies from adjacent but out-of-scope studies.
  Note: The current criteria explicitly separate true O-ISAC/coexistence studies from RF-only THz, pure sensing, pure communication, and communication-maintenance-only optical links.

## Selection Process

- [x] The number of reviewers at title/abstract screening is stated.
  Note: The manuscript states that two reviewers conducted title/abstract screening.
- [x] The number of reviewers at full-text eligibility assessment is stated.
  Note: The manuscript states that the same two reviewers conducted full-text eligibility assessment.
- [x] The manuscript explains whether reviewers worked independently.
  Note: Section III states that title/abstract screening and full-text assessment were conducted independently.
- [x] The disagreement-resolution process is described.
  Note: Disagreements were resolved by consensus discussion and, where required, third-reviewer arbitration.
- [x] Pilot calibration or reviewer alignment is reported if used.
  Note: The manuscript reports an initial calibration on a pilot sample of 50 records before formal screening.

## PRISMA Flow Integrity

- [x] The PRISMA flow diagram is present and readable.
  Note: The manuscript contains an explicit PRISMA flow figure (`Fig. III-1`) with all major stages and counts visible, and the current PDF build (`bare_jrnl_new_sample4.pdf`) compiles with the figure present.
- [x] The manuscript counts match `screening/prisma_flow_counts.csv`.
  Note: The figure and Section III flow accounting align with `screening/prisma_flow_counts.csv` on `980 / 280 / 700 / 478 / 222 / 2 / 220`.
- [x] The identification, deduplication, screening, eligibility, and inclusion counts are internally consistent.
  Note: The reported chain is arithmetically consistent: `980 - 280 = 700`, `700 - 478 = 222`, and `222 - 2 = 220`.
- [x] The text and the figure report the same final included-study count.
  Note: Section III reports `N = 220` in the flow accounting text and the PRISMA figure reports `Studies included in review (n = 220)`.
- [x] The upstream reconstruction limits are not overstated as stronger evidence than the archive actually supports.
  Note: Section III now explicitly describes identification, deduplication, and title/abstract totals as canonical aggregate counts supported by reconstructed search-stage evidence, while reserving “directly row-backed” language for the later eligibility and inclusion stages only.

## Full-Text Exclusions

- [x] Full-text exclusions are listed with study identifiers.
  Note: The reconciled exclusions are listed by study ID in `screening/excluded_fulltext_log.csv` and mirrored in `prisma_evidence_pack/05_appendix/fulltext_exclusions_appendix.tex`.
- [x] Each excluded full-text study has a concrete exclusion reason.
  Note: `O_ISAC_087` is excluded as `EXC-PURE-COMM`, and `O_ISAC_347` is excluded as `EXC-UNVERIFIED-FULLTEXT`, with reviewer-facing reasons preserved in the exclusion log and appendix.
- [x] The manuscript explains the transition from full-text assessed to final included.
  Note: Section III explicitly reports `222` full-text assessed, `2` excluded at full text, and `220` included, and now anchors those two exclusions to the structured exclusion log and supplementary appendix.
- [x] PRISMA 2020 Item 16b is satisfied by citing or listing excluded near-eligible studies with reasons.
  Note: The frozen review package now includes an explicit appendix table listing the two full-text exclusions with identifiers and reasons.

## Included Studies Ledger

- [x] The final included corpus is explicitly defined.
  Note: Section III explicitly defines the final included corpus as `N = 220`.
- [x] The manuscript states where the full included-study ledger can be found.
  Note: Section III now states that the complete 220-study ledger is mirrored in the supplementary included-studies appendix.
- [x] All included studies are traceable through a ledger, appendix, supplement, or equivalent archive.
  Note: The frozen review package contains both `screening/canonical_included_corpus_ledger.csv` and `prisma_evidence_pack/05_appendix/included_studies_appendix.tex` for the full 220-study corpus.
- [x] The included-study ledger is synchronized with `screening/included_studies_canonical.csv`.
  Note: `screening/included_studies_canonical.csv` and `screening/canonical_included_corpus_ledger.csv` both contain the same `220` unique `track_id` values with no duplicates or set mismatch.
- [x] Study identifiers used in the manuscript are stable and consistent.
  Note: The included-study records use stable `O_ISAC_###` study IDs consistently across the canonical included list, the ledger, and the appendix package.

## Included Studies vs Main References

- [x] If the number of included studies exceeds the number of references in the main bibliography, the manuscript explains why.
  Note: Section III now explicitly states that the compressed main text cites only the narratively discussed subset of included studies, so the main bibliography is shorter than the full 220-study corpus.
- [x] The manuscript distinguishes between the full included corpus and the subset of studies cited narratively in the main text.
  Note: The manuscript now distinguishes the full `N = 220` included corpus from the smaller narrative-citation subset reflected in the main bibliography.
- [x] The full set of included studies is available in a supplement or appendix if not all appear in the main bibliography.
  Note: The full included corpus is available in `prisma_evidence_pack/05_appendix/included_studies_appendix.tex` and the canonical included-study ledger files.
- [x] The wording does not imply that only the bibliography-visible studies were included in the review.
  Note: Section III now explicitly states that the full included set is documented in the supplementary appendix and canonical ledger rather than duplicated in the main reference list.
- [x] PRISMA 2020 Item 17 is satisfied through main text, appendix, or supplementary material.
  Note: The included-study appendix provides a study-oriented ledger for the full 220-study corpus, allowing PRISMA Item 17 to be satisfied without requiring every included study to appear in the compressed main-text bibliography.

## Study Characteristics

- [x] Key characteristics of included studies are presented in a structured table, ledger, appendix, or figure.
  Note: The included-studies appendix provides a structured ledger for all 220 studies, and Section III/IV report grouped study characteristics through the extraction schema and taxonomy views.
- [x] The reported study-characteristic fields are enough to support synthesis decisions.
  Note: The reported fields include medium/modality coverage, integration depth, quantitative sensing and communication metrics, and validation level, which are the same characteristic dimensions used to drive later synthesis.
- [x] The manuscript makes clear how studies were grouped for later syntheses.
  Note: Section III states the structured extraction variables, and Section IV explicitly groups studies by medium class, integration class, detection/observability class, and sensing-task class for later conditioned synthesis.
- [x] Representative studies are not presented in a way that hides the full study pool.
  Note: The manuscript uses representative exemplars in the narrative, but the full 220-study corpus remains visible through the included-studies appendix, canonical ledger, and corpus-level count reporting.

## Data Collection and Extraction

- [x] The manuscript explains how data were extracted from included studies.
  Note: Section III now describes a standardized schema-driven extraction procedure linked to the later taxonomy and synthesis workflow.
- [x] The number of reviewers involved in extraction is reported.
  Note: The manuscript now states that two reviewers verified the core study descriptors, taxonomy-critical classifications, and synthesis-critical performance fields.
- [x] Any reconciliation or adjudication process is described.
  Note: Ambiguous extraction decisions are now described as being reconciled by consensus review rather than silent inference.
- [x] Any assumptions made for incomplete or unclear data are disclosed.
  Note: The manuscript now states that values not explicitly reported in the source study were left as unfilled/NR-type fields rather than imputed from conjecture.

## Quality Assessment

- [x] The quality or risk-of-bias framework is clearly defined.
  Note: Section III defines a bespoke Technical Quality Assessment Form (`TQAF`) tailored to O-ISAC engineering studies.
- [x] The assessment dimensions are explained.
  Note: The manuscript lists the five formal TQAF dimensions: modelling fidelity, experimental validity, metric completeness, reproducibility, and clarity.
- [x] The manuscript states how many reviewers performed the assessment.
  Note: Section III states that each included study was evaluated independently by two reviewers.
- [x] The scoring or judgment logic is reproducible.
  Note: Each TQAF dimension is scored on a `0--2` scale with disagreements resolved by consensus discussion or third-party arbitration.
- [x] The coverage of quality assessment across the included corpus is reported accurately.
  Note: The manuscript reports complete five-dimension TQAF scores for `208` studies and does not imply full-coverage scoring beyond that reported count.

## Synthesis Transparency

- [x] The manuscript explains how studies were grouped into each synthesis.
  Note: Section III links extraction variables to later synthesis, and Sections IV--VII explicitly group evidence by medium, integration, detection/observability, sensing task, and governed scenario subsets.
- [x] It is clear which studies contribute to which tables, taxonomies, or evidence summaries.
  Note: The manuscript distinguishes corpus-level taxonomy counts, raw scenario pools, governed subsets, CRQ-valid subsets, and later application/domain summaries rather than treating them as a single undifferentiated evidence layer.
- [x] Quantitative coverage statements are traceable to the included corpus.
  Note: Coverage statements are tied to explicit corpus sizes such as the `220`-study corpus and the derived `225` scenario-point set, with later filters and subset sizes reported transparently.
- [x] Narrative synthesis claims are not presented as if they covered more studies than they actually did.
  Note: The manuscript repeatedly distinguishes raw coverage from governed or admissible subsets and uses conservative wording when support contracts from the full corpus to smaller evidence slices.
- [x] The manuscript distinguishes representative examples from corpus-wide evidence.
  Note: Representative exemplars are used illustratively, while corpus-wide claims are separately anchored to explicit count statements and conditioned subset descriptions.

## Data Availability and Audit Trail

- [x] Screening records, exclusion logs, and included-study ledgers are archived and traceable.
  Note: The frozen package includes structured screening logs, `screening/excluded_fulltext_log.csv`, `screening/canonical_included_corpus_ledger.csv`, and the corresponding appendix artifacts.
- [x] The manuscript states where supporting data or materials can be accessed.
  Note: Section III now points readers to the supplementary evidence package, supplementary exclusion appendix, and supplementary included-studies appendix.
- [x] File-level evidence used for the review is consistent with the manuscript text.
  Note: The current manuscript references match the archived file-level evidence for the search stage, exclusions, and included-study ledger.
- [x] Audit or reconstruction limitations are acknowledged where relevant.
  Note: Section III explicitly acknowledges that the upstream search-stage support includes reconstructed aggregate logs and audit notes where original freeze-time raw exports were incomplete.

## Manuscript-Specific Risk Flags

- [x] The reader can understand how the review moved from screened records to the final included corpus.
  Note: Section III now explains the `700 -> 222 -> 2 -> 220` selection path, distinguishes upstream reconstructed stages from later row-backed stages, and anchors the exclusions and included ledger to supplementary artifacts.
- [x] The reader can understand why the final included count may be larger than the main bibliography count.
  Note: Section III explicitly states that the compressed main text cites only the narratively discussed subset, while the full 220-study corpus is documented in the supplementary included-studies appendix and canonical ledger.
- [x] The manuscript does not leave ambiguity about whether uncited included studies were actually analyzed.
  Note: The manuscript now states that the full included set was retained in the supplementary included-studies appendix and canonical ledger rather than being limited to the main-text bibliography-visible subset.
- [x] Any appendix or supplementary ledger referenced in the methodology is actually present in the submission package.
  Note: The methodology now references supplementary appendix artifacts that are present in the frozen package, including the included-studies appendix and full-text exclusions appendix.
- [x] No unresolved PRISMA-related cross-reference remains in the final PDF build.
  Note: The current build log shows no unresolved reference warnings for the PRISMA figure or related methodology cross-references.

## Acceptance Gate

- [x] The PRISMA counts, exclusion log, and included corpus are mutually consistent.
  Note: The frozen package now aligns the PRISMA flow counts, the two-item full-text exclusion log, and the final `N = 220` included-study ledger.
- [x] The manuscript is defensible under PRISMA 2020 Items 16a, 16b, 17, 24, and 27.
  Note: The current package covers flow counts, full-text exclusions with reasons, the full included-study ledger, protocol registration/access, and archived supporting materials, while acknowledging the reconstruction-limited status of the upstream search stages.
- [x] A reviewer can trace the evidence path from flow diagram to included-study ledger without guessing.
  Note: Section III now points from the flow to the exclusion appendix and included-studies appendix, and the evidence pack preserves the corresponding CSV ledgers and audit notes.
- [x] The review package is ready for PRISMA-focused editorial scrutiny.
  Note: The package is now submission-grade and reviewer-traceable, with the remaining sensitivity confined to openly acknowledged upstream reconstruction limits rather than hidden inconsistencies.
