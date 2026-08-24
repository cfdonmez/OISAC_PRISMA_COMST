# Protocol amendment — actual reviewer and adjudication workflow

Date: 2026-08-04  
Applies to: O-ISAC PRISMA review, Phases A–G  
Status: prospective reporting correction and retrospective workflow clarification

## Reason for amendment

The planned protocol language referred to independent duplicate human review and third-reviewer arbitration. The completed audit trail does not document that process across the full corpus. Retaining the planned wording as if it had occurred would overstate reviewer independence and conflict with the provenance records.

## Actual workflow

The completed workflow was investigator supervised and claim governed:

1. Structured eligibility, report-to-study mapping and extraction rules were fixed in versioned forms and codebooks.
2. Record preparation, PDF-grounded extraction, consistency checks and proposed adjudication were completed under investigator supervision.
3. The investigator approved specified decision packages and authorized survey-scope processing.
4. Deterministic QA checked identifiers, counts, report/study denominators, provenance fields, conflict handling and workbook integrity.
5. Source conflicts were preserved. No preferred number was invented, averaged or silently substituted when the source did not support a unique value.
6. Claim-level survey use was assigned as qualitative, quantitative, contextual or quarantined.
7. A deterministic, fully audited TQAF was applied to all 206 studies. Prespecified caps prevented quarantined claims, low metric clarity/validation, absent author-reported limitations or weak benchmark evidence from receiving unsupported strong scores.
8. S1–S7 synthesis used 8,203 primary claims. Context-only and quarantined claims were excluded from primary numerical synthesis; mutually exclusive dimensions were frozen in one 206-study crosswalk and multi-label fallback categories were audited separately.

This process must be reported as `investigator supervised and claim governed`. It must not be described as independent duplicate human screening, independent full-corpus human PDF verification, or third-reviewer arbitration.

## Independence boundary

`independent_human_status = not_documented`

Investigator authorization and adjudication are valid workflow decisions, but they are not equivalent to a second independent reviewer personally reading every report. Historical filenames or status labels containing `human_adjudicated` or `human_locked` are preserved for hash lineage and are not evidence of independent verification.

## Effect on review validity and reporting

- Eligibility and extraction decisions remain auditable through source/report IDs, locators, decision notes, manifests and hashes.
- Reviewer-process limitations will be stated explicitly in the Methods and Limitations sections.
- No inter-rater agreement statistic will be reported unless it is supported by a genuinely independent, documented double-review subset.
- Technical quality scores will describe evidence/reporting properties and will not be presented as a substitute for reviewer independence.
- Study inclusion is not reversed solely because independent duplicate review was not performed.
- Claims with unresolved source conflict are excluded only at claim level; unaffected study evidence remains usable.

## Corpus state at amendment

- 1,733 records identified;
- 1,259 records screened;
- 330 unique reports sought;
- 58 reports not retrieved;
- 272 full-text reports assessed;
- 227 included reports;
- 206 included studies;
- 8,306 extracted claims;
- 72 exact claims quarantined from quantitative synthesis;
- 175 studies survey-ready and 31 survey-ready with claim restrictions.
- Phase-E TQAF overall contribution: 6 low, 75 adequate and 125 strong; 115 evidence bodies with 54 high, 47 moderate, 10 limited and 4 unclear certainty;
- Phase-F primary synthesis: 8,203 claims (3,020 evidence, 4,779 metric and 404 trade-off), excluding 31 context-only and 72 quarantined claims from primary numerical synthesis.

The actual final search cutoff is 22 June 2026. Any earlier planned 30 June 2026 freeze date is superseded for reporting.
