# Visual and Table Placement Contract for the Nine-Section Survey

## Status and governing rule

This document governs the approved eight-figure and eight-table architecture
for the nine-section survey. Tables I--VIII are implemented in `main.tex` and
their rendered placement has been verified in the current 23-page pre-figure
build. It
does not create a figure asset: Figures 1--8 remain specification only and are
the sole unfinished content carriers. The detailed panel, encoding,
accessibility, and source contracts remain in the versioned visual-blueprint
package. The undated `qa/FINAL_VISUAL_CONTRACT_QA.md` and `.json` files are
superseded pre-closeout snapshots because they record only one live table.

Every carrier must answer a question that prose alone would answer less
clearly. Tables carry structured inventories and exact mappings. Figures carry
relationships, flows, distributions, or mechanisms. Prose introduces the
reader question and interprets the message; it does not repeat every cell,
node, or count.

## Reading-order map

| Order | Visible item | Section and insertion point | Reader question | Core content and message | Nonduplication boundary | Status |
|---:|---|---|---|---|---|---|
| 1 | Table I | I, after the related-synthesis lead-in | What do prior O-ISAC syntheses help the reader do, and what evidence task remains? | Six navigational synthesis families; 24 displayed sources; scope, evidence unit, comparison logic, reader question, and neutral boundary. | No present-review score, checkmarks, quality ranking, or claim that the table is globally exhaustive. The wider source-function register is retained only as an internal audit artifact. | Implemented; layout verified |
| 2 | Fig. 1 | II, after system and native-evidence framing | Why can prior O-ISAC evidence objects not be flattened onto one numerical scale? | Three equal parallel vignettes: model-defined result, medium-native observation, and architecture/deployment object. Meaning remains attached to native context. | Does not repeat Table I families or sources and does not define the comparison-record fields in Fig. 2/Table II. | Specification only; asset pending |
| 3 | Fig. 2 | II, before Table II and the comparison-profile synthesis | How does the survey move from physical system to defensible comparison? | Four equal axes feed one candidate record: physical context, coupling location, measurement contract, and provenance. A gate assigns within-study, conditional cross-study, or descriptive use. | Explains the reasoning path and outcome gate. Table II summarizes the profile groups; the exact schema remains in S-Data Dictionary and S-Evidence. | Specification only; asset pending |
| 4 | Table II | II, immediately after the Fig. 2 specification | What context travels with a reported result, and how can the survey use it? | One compact single-column survey map groups the record into four comparison components and three analytical uses. | Provides the reader-facing profile map. Fig. 2 owns the decision path, S-Data Dictionary and S-Evidence own exact fields, codes, and record-level provenance, and Table I owns prior-survey positioning. | Implemented; layout verified |
| 5 | Fig. 3 | III, after selection and counting-unit prose | How did 1,733 records become 227 reports mapped to 206 studies? | Locked PRISMA flow with report and study denominators separated and contextual records visibly outside the primary study universe. | Shows selection flow only. It does not depict the internal AI/human workflow or technical synthesis taxonomy. | Specification only; source counts locked; asset pending |
| 6 | Table III | III, after the Fig. 3 specification | How is the extracted evidence used in the survey? | One compact five-row table separates quantitative, qualitative, context-only, conflict-restricted, and primary-synthesis use. It exposes 4,997/3,206/31/72 and the 8,203-row primary synthesis while noting the 8,306-row governed ledger. | Fig. 3 owns search-flow denominators. Table III is a reader-facing use map, not a claim-governance audit and not a count of effects. Detailed record types and conflict rules remain in S-Evidence and S-Protocol. | Implemented; layout verified |
| 7 | Fig. 4 | III, after the appraisal interpretation | What does the review-specific appraisal say about technical clarity and comparison readiness? | Horizontal stacked profiles for eight TQAF dimensions plus a visually separate overall evidence-contribution row, with direct labels and the nonvalidated-review-tool qualification. | The overall row is not a ninth input dimension. The figure does not reproduce validation-tier Fig. 7 or turn TQAF into risk of bias, GRADE, or a study ranking. | Specification only; asset pending |
| 8 | Table IV | IV, after the platform-family introduction | How do the six platform families differ in propagation path, observables, communication function, sensing function, constraints, and comparison boundary? | One row per canonical modality family with representative citations and native measurement cautions. | Carries family inventory. Prose explains physical mechanisms; Fig. 5 explains coupling locations. | Implemented; layout verified |
| 9 | Fig. 5 | IV, after the integration-architecture counts and before mechanism subsections | Where are communication and sensing coupled within O-ISAC systems? | Seven overlapping coupling bands are placed along a generic source-to-service signal chain; fixed-size badges carry the multilabel counts. | Does not encode prevalence as maturity, infer intersections, or treat integration labels as mutually exclusive. | Specification only; asset pending |
| 10 | Table V | V, after the measurement-contract subsection | Where is metric evidence concentrated, and how does it enter the survey? | One compact single-column survey map gives the five domain counts and study coverage, followed by the 118/4,661 analytical-role split. The governed 4,861 to primary 4,779 lineage remains in the note. | Section V-B explains metric semantics, S-Evidence carries record-level fields, and Fig. 6 carries tradeoff relationships. The table does not repeat those inventories. | Implemented; compact layout verified |
| 11 | Fig. 6 | V, after ledger and conditionality framing and before mechanism families | What kinds of communication and sensing relations are actually reported? | Three panels: quantitative versus qualitative records; overlapping study participation by mechanism family; conditional share. Governed 404/169/373 lineage and substantive 402/168/371 profile remain distinct. | No Pareto frontier, pooled effect, platform ranking, or implication that overlapping families sum to a study denominator. | Specification only; asset pending |
| 12 | Fig. 7 | VI, after maximum setting and validation-method prose | How far did studies progress, and what evidence methods did they use? | Two panels only: exclusive maximum validation tier; multilabel validation methods. | Evidence for both functions remains in prose and Supplement S7, not a third panel. TQAF reproducibility remains Fig. 4; artifacts remain Table VI. | Specification only; asset pending |
| 13 | Table VI | VI, after the reconstructability lead in | What access routes were reported for data and for code or models? | One compact map gives the four source reported access states for each artifact type. | Reconstruction requirements remain in the linked prose, Section II, and the named supplements. TQAF profiles remain in Fig. 4. | Implemented; compact layout verified |
| 14 | Fig. 8 | VII, after section framing and before detailed synthesis | How do enabling mechanisms connect physical observables to application and 6G requirements? | Six layers connect generation and transport, observables, spatial control, inference, application requirements, and the exclusive 138/64/1/3 6G relevance gate. | No Sankey widths, readiness ranking, or unsupported causal arrows. Exact application rows remain Table VII. | Specification only; asset pending |
| 15 | Table VII | VII, after application-family prose and before the 6G subsection | What operating requirements make each application domain technically consequential? | Thirteen Phase F application-domain rows retain count, sensing target, communication role, geometry, requirements, constraints, citations, and interpretation boundary. | Counts are multilabel and nonadditive; 6G/access remains distinct from the exclusive S7 relevance classification. | Implemented; layout verified |
| 16 | Table VIII | VIII, inside the research-roadmap subsection | How does each observed gap become a testable research action? | Nine columns connect each gap to evidence trace, action, modality-specific stress, baselines, success criterion, artifact, and dependency or risk. | Replaces five repetitive mini-checklists. It is evidence linked, not a generic wish list or timeline prediction. | Implemented; layout verified |

## Stable label registry

`tab:prior_surveys`; `fig:native_evidence_objects`; `fig:comparison_framework`;
`tab:comparison_record`; `fig:prisma_report_study_flow`;
`tab:evidence_reconciliation`; `fig:tqaf_profile`; `tab:modality_map`;
`fig:integration_map`; `tab:metric_admissibility`; `fig:tradeoff_profile`;
`fig:validation_profile`; `tab:artifact_reconstruction`;
`fig:technology_application_chain`; `tab:application_requirements`; and
`tab:research_roadmap`. The detailed v1 blueprint remains authoritative for
panel content, data sources, and accessibility. This v2 contract supersedes its
old file names, section numbers, placements, and visible numbering.

## Figure descriptions and draft captions

### Figure 1: Native evidence objects

Three equally sized, unconnected panels. Panel A places an analytical result
beside its assumptions, objective, and constraints. Panel B places a reported
observation beside optical path, observable, measurement plane, and operating
conditions. Panel C places an architecture or deployment relation beside
shared components, scenario, and validation setting. A directionless bracket
states that each object is meaningful in its native frame.

**Draft caption:** *Native evidence objects represented across prior O-ISAC
syntheses. Model-defined results retain analytical assumptions, medium-native
observations retain their signal path and measurement setting, and architecture
or deployment objects retain their system context. Equal panels denote parallel
examples rather than stages or quality levels.*

### Figure 2: Cross-platform comparison framework

Four equal contextual axes feed a candidate comparison record: physical
context, coupling location, measurement contract, and provenance. A separate
gate assigns one of three uses: interpretation within a study, a conditional
relation across studies, or descriptive retention. The layout is not a quality
sequence, and missing fields remain unknown.

**Draft caption:** *Four-axis framework used to interpret O-ISAC evidence
across platforms. Physical context, coupling location, measurement contract,
and provenance feed a candidate record that supports interpretation within a
study, a conditional relation across studies, or descriptive use. Missing
fields are not inferred, and there is no unconditional comparison category.*

### Figure 3: PRISMA flow

Use the locked Phase-C flow. Report denominators and the final 227-to-206
mapping must be visually separated. Contextual reports sit beside, not inside,
the primary technical denominator.

**Draft caption:** *Selection of reports and mapping to unique O-ISAC studies.
The final 227 eligible reports represent 206 studies; companion reports do not
count as independent demonstrations.*

### Figure 4: TQAF profile

Eight horizontal stacked rows, one per TQAF dimension, plus a separate overall
evidence-contribution row. Strong, adequate, and low counts are printed
directly. Use grayscale-safe patterns or borders. A note states that TQAF is
review specific and nonvalidated; the overall row is not a ninth dimension.

**Draft caption:** *Technical reporting and comparison-readiness profile of
the 206 included studies across the eight review-specific TQAF dimensions.
Categories summarize source reporting and do not constitute conventional risk
of bias or GRADE judgments.*

### Figure 5: Integration architectures

A generic source-to-service path carries parallel communication and sensing
lanes. Seven nonexclusive coupling bands mark hardware, carrier, waveform,
resources, link or channel, joint design, and application at their usual
locations. Fixed-size count badges and a multilabel banner prevent a prevalence
or maturity reading.

**Draft caption:** *Nonexclusive mechanisms through which communication and
sensing are coupled in the included O-ISAC studies. Counts are multilabel and
must not be summed as mutually exclusive study classes.*

### Figure 6: Reported tradeoff structure

Panel A compares 218 quantitative and 184 qualitative substantive records.
Panel B shows study overlap across recurring mechanism families. Panel C shows
371 conditional records among the 402 substantive records. The governed
404-row ledger and two absence-status audit rows are disclosed in the caption
or note.

**Draft caption:** *Structure of the governed communication and sensing
tradeoff evidence. The scientific profile contains 402 substantive records
from 168 studies, while the 404-row governed ledger retains two explicit
absence-status audit rows. Mechanism families overlap and the records are not
effect estimates.*

### Figure 7: Validation profile

Panel A is an exclusive stacked distribution of maximum maturity: basic
simulation, enhanced simulation, laboratory experiment, controlled prototype,
and field/deployment. Panel B shows the nonexclusive validation methods used.

**Draft caption:** *Maximum validation maturity and reported validation
methods across 206 O-ISAC studies. Maximum tiers are exclusive; validation
methods are multilabel and therefore nonadditive.*

### Figure 8: Technology, application, and 6G relationship map

A six-layer map moves from generation and transport to waveform and physical
observables, spatial control, inference, application requirements, and the
exclusive 6G relevance gate. Solid arrows show technical progression and
dashed reverse arrows show requirement feedback. Node size, color, and arrow
width do not encode unverified importance or co-occurrence.

**Draft caption:** *Cross-layer organization of O-ISAC technologies,
observables, application requirements, and 6G evidence. Technology and
application labels overlap; arrows do not encode causal influence. The final
gate separates direct, inferential, weak, and not-applicable relevance
(138/64/1/3) from the evidence required for conformance, interoperability,
paired operation, and deployment.*

## Production gates

1. Recompute every displayed count from the named locked source rather than
   transcribing it from prose.
2. Preserve the 404/169 governed and 402/168 substantive tradeoff lineages.
3. Use the hash-locked modality crosswalk and the Phase-F mechanism
   normalization, never raw public labels as canonical categories.
4. Keep figures editable and vector based; no copied source artwork, AI
   illustration, three-dimensional effects, or color-only encoding.
5. Use at least 8-point text at final size, direct labels where practical,
   grayscale-safe distinctions, and complete alt text.
6. Keep the implemented table labels and references stable. Activate figure
   references and captions only after the corresponding asset passes source,
   semantic, accessibility, and rendered-layout QA.
7. Recompile and perform the final submission-layout pass after all eight
   figures are inserted; the current pre-figure build occupies 23 pages, and
   page optimization is deliberately deferred until the
   figure-inclusive composition exists.
