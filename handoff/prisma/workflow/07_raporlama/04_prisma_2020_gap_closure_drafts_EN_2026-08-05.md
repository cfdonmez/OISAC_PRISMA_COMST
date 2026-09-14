# PRISMA 2020 Gap-Closure Draft Bank

Created: 2026-08-05  
Last updated: 2026-08-07 — retrospective OSF registration and registration-lineage amendment verified  
Language: English manuscript text  
Status: Working drafts only; not integrated into the protected active manuscript

## Use rule

These passages close identified PRISMA reporting gaps without changing the locked review corpus, eligibility decisions, extraction data, TQAF results, or S1–S7 synthesis. Bracketed placeholders require author input, verified citations, or final supplement/repository identifiers. They must not be guessed or silently removed.

The following terminology is mandatory throughout the manuscript:

- `206 included studies represented by 227 eligible reports`;
- `investigator-supervised, AI-assisted, user-delegated, and claim-governed`;
- `review-specific technical evidence and reporting appraisal (TQAF)`, not a validated conventional risk-of-bias tool;
- `review-specific certainty classification`, not GRADE;
- `structured, taxonomy-based, metric-governed narrative synthesis without meta-analysis`.

## Item 2 — Structured abstract gap closure

Candidate integrated Methods/limitations wording:

> We searched Scopus, IEEE Xplore, ScienceDirect, SpringerLink, Wiley Online Library, and Taylor & Francis Online through 22 June 2026 for English-language, peer-reviewed O-ISAC journal and full-conference reports. Eligible reports evaluated genuinely integrated optical or photonic sensing and communication; RF-only, single-function, abstract-only, and insufficient-English reports were excluded. Study selection and source-located extraction followed a single-investigator-supervised, AI-assisted workflow; routine independent duplicate human review was not performed. Evidence was appraised using a review-specific deterministic eight-dimension TQAF and synthesized using structured, taxonomy-based, metric-governed narrative methods without meta-analysis. Heterogeneous metrics and validation contexts, limited open artifacts, the absence of a formal missing-results-bias assessment, and the absence of independent duplicate full-corpus human verification constrain cross-study inference. The review was retrospectively registered on the Open Science Framework on 12 February 2026 (7f6wb; DOI: 10.17605/OSF.IO/7F6WB). This review received no specific financial or non-financial support.

Final abstract assembly must still respect the target journal word limit and preserve the already prepared objectives, included-study count, main results, interpretation, and limitations.

## Item 7 — Search strategy and unreconstructable Taylor & Francis queries

> Complete source-specific strategies, fields, limits, execution dates, and export counts are reported in [SUPPLEMENT ID TO ASSIGN]. The exact query strings associated with two low-yield Taylor & Francis exports could not be reconstructed from the audit trail; these files are therefore reported as unmapped supplementary exports, and no query wording was inferred retrospectively.

## Item 8 — Selection process

> Title-and-abstract and full-text selection used a single-investigator-supervised, AI-assisted workflow. Generative AI systems prepared records, located source passages, and generated non-binding eligibility suggestions. The investigator reviewed or explicitly delegated defined decision packages, while deterministic checks validated identifiers, permitted codes, counts, exclusion reasons, and report-to-study links. The process was not blinded and did not use routine independent duplicate human screening or third-reviewer arbitration. Tool and model identifiers were retained where reconstructable; otherwise, the version was recorded as unknown rather than inferred.

## Item 9 — Data collection process

> Data collection was performed at study, report, and claim levels through one investigator-supervised, AI-assisted workflow and was not independently duplicated by two human extractors. AI systems generated source-grounded candidate fields and locators; the extraction form was piloted before corpus-wide use, and specified adjudication packages were investigator-approved or investigator-delegated. Deterministic QA checked schema validity, identifiers, units, missingness codes, provenance, report-to-study lineage, and claim counts but did not make scientific judgments. Missing or ambiguous information was retained as missing, and no project-level graph digitization or newly derived performance value was introduced. Authors of the included studies were not contacted for additional or clarifying data. Weekly project meetings supported internal review-team discussion and verbal verification of methodological interpretations; the participants were not authors of the included studies, and these meetings were not treated as study-author data verification.

## Item 11 — TQAF framing

> Because the corpus comprised heterogeneous analytical, simulation, laboratory, prototype, and field studies, no single intervention-oriented risk-of-bias instrument was applicable. We therefore applied the review-specific deterministic TQAF (`phase_e_tqaf_deterministic_v1.0_2026-08-04`) to eight technical evidence and reporting dimensions: technical relevance, metric clarity, reporting completeness, validation maturity, reproducibility, benchmark readiness, comparison admissibility, and limitation transparency. TQAF is a technical evidence and reporting appraisal rather than a validated conventional risk-of-bias instrument. Its scores qualified synthesis language and did not determine study inclusion. The assessment was investigator-supervised and AI-assisted and was not independently duplicated by two human assessors.

## Item 12 — Effect measures

> No common effect measure was prespecified because the review did not estimate a pooled intervention effect. Source-reported operational metrics, units, measurement planes, operating conditions, and validation contexts were retained without conversion to standardized effects. No effect-size transformation or cross-modality pooling was performed; numerical comparisons were allowed only within explicitly compatible evidence strata.

## Item 13c — Presentation methods

> Individual-study characteristics were tabulated once per study cluster while preserving eligible-report lineage. Synthesis tables reported claim counts and unique-study counts separately. Mutually exclusive study-level distributions used 206 studies as the denominator, whereas multi-label axes permitted category totals to exceed 206. No forest plots or funnel plots were produced because no pooled effect estimate was calculated.

## Item 13e — Heterogeneity investigation methods

> Heterogeneity was explored descriptively through prespecified stratification by optical modality, architecture and integration mechanism, metric family and role, measurement plane, operating scenario, validation type and maturity, enabling technology, and application domain. Comparisons were restricted to compatible metric-definition, measurement-plane, scenario, and validation strata. Statistical heterogeneity measures and meta-regression were not applicable because no effect-size meta-analysis was performed.

## Item 13f — Sensitivity analysis: justified non-applicability

> No review-level sensitivity analysis was performed because the review did not produce a pooled effect estimate or model-dependent primary analysis. Operational robustness was instead governed through source-location requirements, comparability rules, context-only restrictions, and claim-level quarantine; these controls were not treated as sensitivity analyses.

## Item 14 — Bias due to missing results: methods limitation

> We did not apply funnel plots, small-study-effect tests, or a formal outcome-reporting-bias instrument because no common effect measure was pooled and accessible study protocols or analysis plans were not available as a consistent corpus-wide assessment source. Unreported or ambiguous results were retained as missing rather than imputed; however, this procedure does not eliminate selective reporting. The risk of bias due to missing results therefore remains unquantified and is treated as a limitation of the review.

## Item 15 — Evidence-body certainty method

> Evidence-body certainty was classified using a review-specific deterministic scheme rather than GRADE. For each contributing study, the median across all eight TQAF dimensions was first calculated. For non-S7 evidence bodies, certainty was limited when fewer than three studies contributed or the median of those study-level medians was below 1.5; high certainty required at least five studies, a median of study-level medians of at least 2.5, and at least 75% of contributing studies to have an eight-dimension median of at least 2; all remaining bodies were moderate. For S7 gap bodies, high certainty required at least ten studies across three modalities, moderate certainty at least five studies across two modalities, limited certainty at least two studies, and otherwise unclear certainty. Predefined non-substantive `other` fallback bodies for communication or sensing metrics, enabling technology, or application domain were assigned unclear certainty. The assessment was deterministic, investigator-supervised, AI-assisted, and not independently duplicated by two human assessors.

Technical correction: any existing wording that says the non-S7 median used only “core appraisal dimensions” must be replaced; the implemented algorithm used all eight TQAF dimensions.

## Item 16a — Study-selection flow

> Figure [PRISMA FIGURE NUMBER] presents the locked PRISMA 2020 study-selection flow. Retrieval and eligibility counts use unique reports, while the final inclusion stage distinguishes 227 eligible reports from the 206 underlying studies they represent.

## Item 16b — Full-text exclusions

> [SUPPLEMENT ID TO ASSIGN] lists all 39 reports excluded after full-text assessment, including the complete citation, one primary exclusion reason, and a report-specific evidence note. The six contextual-only reports were retained separately and were not counted as full-text exclusions.

## Item 17 — Included-study characteristics

> [SUPPLEMENT ID TO ASSIGN] reports the characteristics of all 206 included study clusters, including full citation, primary and companion-report lineage, publication year and venue, optical modality, integration mechanism, sensing task, communication function, validation design, and survey-use status.

Release prerequisite: resolve bibliography keys/citations for all 206 study clusters before using this sentence.

## Item 18 — Conventional risk of bias not applicable; study-level technical appraisal reported separately

> Because this review synthesizes heterogeneous engineering-system studies rather than intervention-effect estimates, a conventional study-level risk-of-bias assessment was not performed and PRISMA Item 18 is treated as not applicable with justification. Study-level technical evidence and reporting characteristics were instead appraised using the review-specific TQAF. [SUPPLEMENT ID TO ASSIGN] reports all TQAF dimensions for each included study; these ratings qualify evidence use and must not be interpreted as risk-of-bias judgments.

Publication-facing table/file label: `Study-level TQAF technical evidence and reporting appraisal`; do not expose `risk_of_bias.csv` as if it were a conventional RoB dataset.

## Item 19 — Individual-study results

> Study-level reported outcomes are provided in [SUPPLEMENT ID TO ASSIGN]. Each record preserves the study and report identifiers, metric definition and role, reported value and unit, measurement plane, operating condition, validation context, reported uncertainty where available, and source locator. No pooled effect estimate or project-derived performance value was calculated.

The verified source dataset is the `04_METRIC_RESULTS` worksheet of the canonical Phase-D survey-ready workbook: 4,861 metric-result rows, of which 4,779 enter the primary synthesis universe.

## Item 20a — Contributors to each synthesis

> For each S1–S7 evidence body, [SUPPLEMENT ID TO ASSIGN] identifies the contributing studies and summarizes their optical modalities, validation contexts, TQAF profiles, overall evidence contribution, and body-level certainty. Multi-label memberships are reported without summing category-specific study counts.

## Item 20b — Statistical synthesis: justified non-applicability

> No effect-size meta-analysis or model-based statistical synthesis was conducted. Numerical results are descriptive study counts, proportions, and governed claim counts; pooled estimates, confidence intervals, and statistical heterogeneity measures are therefore not applicable.

## Item 20c — Descriptive heterogeneity results

> Heterogeneity was characterized descriptively across optical modality, architecture, metric definition and role, measurement plane, scenario, and validation tier. These dimensions structured the S1–S7 syntheses but were not tested as causal moderators.

## Item 20d — Sensitivity results: justified non-applicability

> No sensitivity analysis of a pooled result was performed because the review produced neither a pooled statistical model nor a universal cross-study performance ranking.

## Item 21 — Bias due to missing results: results limitation

> Formal assessment of bias due to missing results was not feasible because the review dataset lacked harmonized prespecified outcome sets and did not contain accessible protocols or analysis plans as a consistent corpus-wide assessment source. TQAF reporting-completeness scores were used only to characterize transparency and were not interpreted as a publication-bias test. Publication and selective-outcome-reporting bias therefore cannot be excluded.

## Item 22 — Evidence-body certainty results

> Certainty was assessed for 115 S1–S7 evidence bodies: 54 were rated high, 47 moderate, 10 limited, and 4 unclear. [SUPPLEMENT ID TO ASSIGN] reports the rating and contributing studies for each body. The four unclear bodies were non-substantive fallback categories and were not used to support survey conclusions.

Publication pointer must use the canonical `systematic_review_workflow/05_kalite_kanit/certainty_grade.csv`, not the stale draft filename retained in the frozen Phase-E synthesis matrix.

## Item 23a — Interpretation in the context of other evidence

> These findings extend earlier modality-specific O-ISAC reviews by showing that barriers to cross-study inference recur across measurement-plane definition, benchmark design, and validation maturity rather than being confined to one optical platform [INSERT VERIFIED REVIEW CITATIONS]. They are also consistent with the broader ISAC literature in treating resource allocation and hardware co-design as coupled constraints [INSERT VERIFIED CITATIONS].

No citation may be inserted until the cited source has been opened and verified to support the exact comparison.

## Item 23d — Practice, policy, and future research

> For standards bodies, funders, and 6G programme coordinators, these findings support minimum reporting requirements for measurement plane, operating conditions, validation tier, uncertainty, and artifact availability. Cross-modality performance claims should be accepted only when task definitions and operating constraints are equivalent.

## Item 24a — Registration

> The review was retrospectively registered on the Open Science Framework on 12 February 2026 (OSF registration 7f6wb; https://osf.io/7f6wb; DOI: 10.17605/OSF.IO/7F6WB). At the time of registration, search and screening had already been completed and the review was in synthesis and manuscript drafting; the record therefore constitutes retrospective registration and should not be interpreted as a prospective preregistration.

PRISMA for Abstracts A12:

> Retrospectively registered on the Open Science Framework (7f6wb; DOI: 10.17605/OSF.IO/7F6WB) on 12 February 2026.

## Item 24b — Protocol access

> The internally versioned protocol, decision log, and dated amendment are available in [SUPPLEMENT IDs TO ASSIGN] and at [PERSISTENT REPOSITORY URL OR DOI].

## Item 24c — Protocol amendments

> The OSF record was frozen retrospectively during synthesis and manuscript drafting and captured a legacy review state: its last recorded search date was 30 November 2025, it described 222 full-text reports assessed with one excluded and 221 included, and it specified a different source set and independent duplicate human processes. Its frozen materials were internally inconsistent about the date window: the registration description characterized the corpus as 2020–2025, whereas an attached protocol proposed searching from 2000 and retaining eligible pre-2020 functional O-ISAC studies. The review was subsequently re-baselined in June–August 2026, with the primary-evidence window fixed at 1 January 2020–22 June 2026 and pre-2020 material restricted to contextual/background use. The executed final search covered Scopus, IEEE Xplore, ScienceDirect, SpringerLink, Wiley Online Library, and Taylor & Francis Online; the final flow comprised 272 full-text reports assessed, 39 full-text exclusions, six contextual reports, and 227 eligible reports mapped to 206 included studies. Planned routine independent duplicate human review and third-reviewer arbitration were not performed across the final corpus. The implemented TQAF was a deterministic review-specific eight-dimension appraisal, and no formal missing-results/publication-bias assessment or formal sensitivity analysis was performed. The planned cross-study rate–range–resolution scatter/frontier analysis was not implemented because heterogeneous tasks, units, measurement planes, and conditions did not support a single admissible frontier; trade-offs were instead synthesized as 404 source-grounded, condition-aware records grouped into prespecified families. The executed workflow was investigator-supervised, AI-assisted, user-delegated, and claim-governed. These departures and their rationales are reported transparently; the OSF 221-study figure is a superseded legacy snapshot with different denominators and is not presented as direct attrition to the final 206-study universe.

## Item 25 — Support

Investigator confirmation recorded on 2026-08-06: no financial or non-financial support was received for this review.

> This review received no specific financial or non-financial support. No funder or sponsor had any role in the design, conduct, analysis, interpretation, manuscript preparation, or decision to submit.

## Item 26 — Competing interests

Investigator confirmation recorded on 2026-08-06: the review authors have no competing interests to declare.

> The authors declare no competing interests.

## Item 27 — Availability of data, code, and materials

> The review protocol and amendments, executed search logs, screening and full-text decision records, report-to-study mappings, extraction forms and derived extraction tables, TQAF outputs, synthesis tables, and analysis and QA scripts are available at [PERSISTENT REPOSITORY URL OR DOI; RELEASE TAG OR VERSION; LICENSE]. Publisher PDFs and other copyrighted full texts are not redistributed. [RESTRICTED MATERIALS, IF ANY] are available from [CORRESPONDING AUTHOR AND EMAIL] on reasonable request, subject to [CONDITIONS].

Before integration, confirm the public scope, persistent identifier, release/tag, license, restricted-material list, request contact, and request conditions.

## Separate journal gate — Author contributions

Author contributions are not PRISMA Item 27, but most target journals require a separate CRediT statement. AI systems must not be listed as authors or CRediT contributors.

> Author contributions (CRediT): [AUTHOR INITIALS]—[ROLES]; [AUTHOR INITIALS]—[ROLES].

## Integration gate

This draft bank becomes manuscript-ready only after:

1. the investigator resolves all bracketed author-owned declarations;
2. external citations in Item 23a are source-verified;
3. supplement identifiers and publication-facing filenames are frozen;
4. the repository/DOI, version, license, and availability scope are frozen;
5. the approved passages are inserted into the active manuscript without mechanically replacing legacy denominators; and
6. manuscript section/page references are entered in the final PRISMA checklist after render QA.
