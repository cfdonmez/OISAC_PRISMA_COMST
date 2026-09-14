# Supplementary review methods

This supplement describes the search, selection, extraction, appraisal, and synthesis supporting the O-ISAC survey. The [supplement index](index.md) maps the named supporting records to their source files.

## Review scope and eligibility

The review examined communication and sensing within a shared optical or photonic system. Its population, concept, and context framework covered peer-reviewed O-ISAC studies; system architectures, reported performance, and support for comparison; and fiber, free-space optical, VLC/LiFi, photonic-THz, and hybrid optical platforms. Relevance to 6G was characterized without making the presence of a 6G keyword an eligibility requirement.

Eligible reports were peer-reviewed journal articles, including early-access articles, or full conference papers with sufficient full technical content in English and assessable evidence for at least one survey domain. An English abstract alone was insufficient. Reports had to describe an integrated or co-designed communication and sensing function and provide technical evidence such as an architecture, metric, tradeoff, validation method, or benchmark-relevant evaluation. Eligibility was assessed separately from support for a joint quantitative comparison. Weak reporting or validation did not by itself exclude an otherwise eligible study.

The primary publication window was 1 January 2020 through 22 June 2026, using the date when a report first became publicly available. The executed cutoff superseded the earlier planned 30 June 2026 freeze. Pure communication, pure sensing, and RF-only ISAC without a relevant optical or photonic component were outside scope. Abstracts, posters, editorials, non-full papers, book chapters, and non-peer-reviewed grey literature did not enter the primary technical corpus. Reviews, surveys, and pre-2020 foundational publications could inform background and field positioning, with separate contextual status. These criteria and their amendments are documented in [S-Protocol](index.md#s-protocol).

## Search sources and execution

Scopus and IEEE Xplore were the core sources. ScienceDirect, SpringerLink, Wiley Online Library, and Taylor & Francis Online supplied additional platform searches. Web of Science and ACM Digital Library were outside the formal source set because institutional access was unavailable. Strategies combined O-ISAC phrases and joint sensing–communication terms with optical or photonic platform terms. All final searches were executed on 22 June 2026.

| Source | Executed runs | Exported records |
|---|---:|---:|
| Scopus | 3 | 1,273 |
| IEEE Xplore | 3 | 329 |
| ScienceDirect | 3 | 24 |
| SpringerLink | 4 | 75 |
| Wiley Online Library | 4 | 29 |
| Taylor & Francis Online | 2 | 3 |
| Total | 19 | 1,733 |

The execution record preserves source-specific year, language, and document-type limits. Interface filters differed in availability and scope, so the full eligibility criteria were also applied during screening. [S-Search](index.md#s-search) contains the available or reconstructed query strings, limits, exported counts, and provenance status for each run. Scopus strategies were reconstructed from the final search package; IEEE Xplore strategies were reconstructed from recorded pilot strings used for the final runs. ScienceDirect, SpringerLink, and Wiley strings were recorded in their final source summaries. The query-to-export mapping for the two Taylor & Francis exports was not recorded at execution and could not be reconstructed. No replacement query was inferred.

Interface on-screen result counts were not recorded for the 19 runs; the preserved counts are exported rows. Mappings from generic export filenames to query identifiers were reconstructed for three supplementary platforms and are recorded as such. These limits constrain exact replication of the search interfaces.

## Selection and report-to-study reconciliation

Selection proceeded through cross-source deduplication, title and abstract screening, retrieval, and full-text assessment. Of 1,733 identified records, 1,259 entered title and abstract screening. Consolidating two bibliographic aliases converted the 332-record retrieval route to 330 unique reports sought. Fifty-eight reports were not retrieved, leaving 272 full texts assessed. Full-text assessment yielded 39 exclusions, six contextual reports, and 227 eligible reports. [S-Exclusions](index.md#s-exclusions) identifies each of the 39 excluded full texts and its primary reason.

| Primary full-text exclusion reason | Reports |
|---|---:|
| Abstract, poster, editorial, opinion, or non-full paper | 4 |
| Communication only without sensing | 2 |
| Insufficient English full technical content | 12 |
| No genuine sensing–communication integration | 5 |
| Non-optical or RF-only ISAC | 4 |
| Sensing only without communication | 12 |
| Total | 39 |

Reports describing the same underlying study were linked before synthesis. The 227 eligible reports comprise 206 primary reports and 21 companion reports mapped to 206 unique studies. Companion reports retain their bibliographic and extracted-result provenance; they are neither additional studies nor exclusions. [ST-01](index.md#st-01) provides the study inventory, report-to-study lineage, and companion provenance.

The executed selection workflow retained 67 contextual records for field positioning, outside the 206-study technical denominator. A subsequent bounded manuscript-stage search for contextual syntheses added seven sources outside the executed exports. These additions did not change primary eligibility, report lineage, or technical synthesis counts. The contextual amendments in S-Protocol document this separate use.

## Review conduct and registration history

The review was investigator supervised and AI assisted. AI tools supported record preparation, source-grounded extraction, consistency checks, and proposed eligibility or claim-use decisions. The investigator approved or delegated specified decision sets and authorized the review processing. Rule-based checks examined identifiers, counts, source links, report-to-study units, and conflicting claims. These checks and authorizations do not constitute a second independent reviewer reading each report. Routine independent duplicate human screening, extraction, and appraisal, and third-reviewer arbitration were not performed. No inter-rater agreement statistic is claimed. Authors of included or unretrieved reports were not contacted. S-Protocol records the executed workflow and the departures from earlier plans.

The review was retrospectively registered on the Open Science Framework on 12 February 2026 under record `7f6wb` (DOI `10.17605/OSF.IO/7F6WB`). Search and screening had already been completed in that earlier review state, and synthesis and manuscript drafting were underway. The registration described 221 included studies. Its description used a 2020–2025 window, whereas an attached protocol proposed searching from 2000 and retaining eligible pre-2020 functional O-ISAC studies. The June–August 2026 revision established the final 1 January 2020–22 June 2026 primary window, source set, and report-to-study reconciliation. The earlier 221-study value and the final 206-study value belong to different search states and are not an attrition sequence.

The initial June protocol and dated amendments preserve this history. The 4 August amendment describes actual review conduct; the 7 August amendment clarifies the retrospective registration lineage; and the deviation register records changes to the cutoff, appraisal, and synthesis. Earlier plans for independent duplicate review, formal publication-bias and sensitivity assessments, and a cross-study rate–range–resolution frontier are not reported as completed procedures.

## Extraction and units of analysis

A study could contribute several results under different conditions. Each extracted item retained its report and source location. Metric records preserved the quantity, definition, unit, measurement point, result representation, and evaluation setting. Operating conditions, baselines, and validation settings were retained where reported. The 446-entry [S-Data Dictionary](index.md#s-data-dictionary) defines fields, codes, and missing-data rules.

Communication and sensing measurements remained separate unless the source linked them to a shared setting. Relationship records described design factors or objectives, constraints, and reported effects. A common study identifier or appearance in one table did not itself establish a jointly measured operating point.

### Table S1. Units of analysis and their roles in the technical synthesis

| Analysis unit | Count | Meaning of one entry | Use in the survey |
|---|---:|---|---|
| Included study | 206 | An underlying study after reconciliation of its eligible reports. | Study-level platform, integration, and validation profiles. |
| Primary coding record | 8,203 | An extracted evidence item, metric record, or tradeoff record retained for primary synthesis. | Source-linked technical analysis preserving each record's unit and conditions. |
| Metric record | 4,779 | A reported measure with its definition and evaluation setting. | Communication, sensing, and implementation performance. |
| Substantive relationship | 402 | A source-described relation among design factors, objectives, or outcomes. | Mechanisms and condition-dependent tradeoffs. |
| Synthesis group | 115 | A set of studies grouped for thematic synthesis. | 111 theme-specific groups support synthesis; four broad classification groups retain coverage information. |

These counts refer to different analysis levels and are not independent experiment counts. The 8,203 primary coding records comprise 3,020 evidence items, 4,779 metric records, and 404 tradeoff records. Of the latter, 402 describe substantive relationships and two record the absence of a reported tradeoff. The substantive table is a projection of the 404-record table, not an additional set to be added to it. A study may contribute to several synthesis groups.

Extraction retained numerical values explicitly stated by the source. Graphs supported interpretation in their reported form; they were not digitized to create numerical measurements. Missing values were not inferred, and conflicting values were not averaged or silently replaced. Source conflicts were handled at the individual-claim level so that unaffected evidence from the same study remained usable. The complete register contained 8,306 records: 8,203 primary records, 31 contextual items, and 72 items with source conflicts outside the primary synthesis. [S-Evidence](index.md#s-evidence) supplies the primary evidence, metric, and tradeoff records with source locators; S-Protocol describes the contextual and conflict rules.

## Technical appraisal

All 206 included studies were assessed using the Technical Quality Assessment Framework (TQAF) developed for this review. Deterministic rules scored eight technical and reporting dimensions from 0 to 3: technical relevance, metric clarity, reporting completeness, validation maturity, reproducibility, benchmark readiness, comparison admissibility, and limitation transparency. Overall evidence contribution was recorded separately, rather than as a ninth dimension of the profile.

TQAF characterizes the support a report provides for interpretation and reuse. It is a review-specific descriptive appraisal whose scoring has not been independently validated. It is neither a conventional study-level risk-of-bias instrument nor GRADE, and its scores do not establish a universal study ranking or reviewer independence. Metric clarity and reporting completeness describe how a result can be understood in its source setting; validation and reproducibility describe testing and reconstruction; benchmark readiness and comparison admissibility describe support for use beyond the original experiment.

An overall contribution score of 3 required technical relevance, metric clarity, reporting completeness, and validation maturity each to reach at least 2. Low metric clarity together with low validation maturity capped overall contribution at 1. A claim withheld for unresolved conflict capped overall contribution at 2; a withheld metric claim capped comparison admissibility at 1. Limitation transparency was capped at 1 when no limitation was reported and at 2 when a material source conflict remained. The conduct-and-reporting record in S-Protocol provides these rules, and [S-Appraisal](index.md#s-appraisal) provides the study-level scores.

## Thematic synthesis and interpretation limits

Studies were grouped by technical theme across seven survey domains. Within each theme, structured narrative synthesis connected recurring mechanisms and reported performance relations while retaining physical setting, task, metric meaning, measurement plane, operating condition, comparator, and validation setting. Numerical examples preserve their original units and conditions. Eligibility, technical appraisal, and admissibility for numerical comparison were separate judgments.

[S-Bodies](index.md#s-bodies) contains 115 review-defined synthesis groups and 4,931 study-to-group membership links. Of these groups, 111 support thematic conclusions and four record broad coverage. Membership links are not additional studies or independent replications. Review-specific group ratings combine contributor counts and study appraisal summaries; evidence-gap groups use coverage and modality spread. The rules are supplied in S-Protocol. These descriptive synthesis categories are not GRADE certainty ratings.

Heterogeneity across optical modalities, architectures, tasks, units, measurement planes, and validation conditions precluded a common effect measure and pooled statistical model. No meta-regression or statistical heterogeneity estimate was performed. Condition-dependent relationships were synthesized by theme without estimating a universal performance frontier or cross-platform ranking. Formal missing-results or publication-bias assessments and formal sensitivity analyses were not performed. Selective reporting cannot be excluded.

The conclusions therefore concern supported mechanisms and bounded performance relations. The restricted source and language coverage, 58 unretrieved reports, incomplete search-interface provenance, absence of routine independent duplicate human review, and nonvalidated appraisal limit completeness, reproducibility, and confidence in the review process. Source-linked records make the reported basis of a conclusion inspectable; they do not remove these limitations.
