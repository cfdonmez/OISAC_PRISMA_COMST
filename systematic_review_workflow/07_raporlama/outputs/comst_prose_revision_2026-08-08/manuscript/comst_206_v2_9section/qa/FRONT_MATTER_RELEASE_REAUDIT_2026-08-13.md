# Front Matter, Abstract, and Release Re-audit — 2026-08-13

Overall status: `PASS_CONTENT_WITH_AUTHOR_DECISION_BLOCKERS`  
Submission ready: **no**  
Public release ready: **no**

## Outcome

The active candidate now has a survey-first title proposal that explicitly
identifies a systematic review, source-verified author and affiliation
metadata, a 250-word PRISMA-informed narrative abstract, the approved support
and competing-interest declarations, and the retrospective OSF registration
statement. These corrections close the factual front-matter gaps that could be
resolved without inventing author roles or exercising publication rights.

The result is still a candidate. Final title approval, CRediT roles, creator
scope, rights holder and year, license grants, repository route, release URL,
version, and archive DOI remain author decisions. The local evidence
supplements are materialized manuscript artifacts, not a public release.

## Files created or corrected

- `FRONT_MATTER_CANDIDATE_2026-08-13.md`: candidate title, verified article
  metadata, copy-ready IEEEtran fragment, approved declarations, release
  boundary, and explicit author-decision fields.
- `sections/00_ABSTRACT.tex`: replaced with a 250-word narrative abstract.
- `README.md`: removed the stale claim that electronic supplements had not
  been materialized and separated local materialization from public release.

No standalone driver was created, no LaTeX compilation was run, and no public
repository or release was changed.

## PRISMA for Abstracts content gate

| Abstract item | Status after correction | Evidence in candidate |
| --- | --- | --- |
| A1 Title | `CANDIDATE_COMPLETE` | Candidate title contains both “Systematic Review” and “Survey”; final author approval remains open. |
| A2 Objectives | `COMPLETE` | Explains the comparison problem and the purpose of the framework. |
| A3 Eligibility | `COMPLETE_COMPACT` | Publication from 2020, peer review, sufficient English technical content, and joint optical sensing and communication are stated. |
| A4 Information sources | `COMPLETE` | All six source names and the 22 June 2026 search cutoff are stated. |
| A5 Risk of bias or appraisal | `COMPLETE_WITH_BOUNDARY` | No conventional risk-of-bias instrument; review-specific TQAF is named. |
| A6 Synthesis methods | `COMPLETE` | Structured narrative synthesis, metric governance, and no meta-analysis are stated. |
| A7 Included studies | `COMPLETE` | 227 eligible reports mapped to 206 studies. |
| A8 Main results | `COMPLETE_COMPACT` | Integration locations and 402 substantive tradeoff records from 168 studies are reported. |
| A9 Evidence limitations | `COMPLETE` | Field evidence and reported open data/code scarcity are stated. |
| A10 Interpretation | `COMPLETE` | Interpretation is bounded and does not rank optical platforms. |
| A11 Funding | `COMPLETE` | No specific financial or nonfinancial support. |
| A12 Registration | `COMPLETE` | Retrospective OSF registration `7f6wb` and DOI are stated. |

This is a content gate, not a claim that the final journal title or front matter
has been author approved.

## Abstract deterministic checks

- word count: **250**, counting the escaped `\&` as “and”;
- maximum: **250**;
- unescaped ampersands: **0**;
- `\begin`/`\end` counts: **2/2**;
- opening/closing brace counts: **4/4**;
- hyphenated lexical tokens: `O-ISAC` and `meta-analysis` only;
- protected evidence anchors present: six sources, `22 June 2026`, 227
  eligible reports, 206 studies, 402 substantive records, 168 studies, TQAF,
  no conventional risk-of-bias instrument, no meta-analysis, no support, and
  retrospective OSF registration.

## Verified article metadata

| Field | Verified candidate value |
| --- | --- |
| Author order | Fatih Dönmez; Ahmet Altuncu; Mustafa Namdar |
| Corresponding author | Fatih Dönmez |
| Fatih Dönmez ORCID | `0000-0003-0553-4418` |
| Coauthor ORCIDs | not provided; omitted |
| Afyon Kocatepe University authors | Fatih Dönmez and Ahmet Altuncu |
| Kütahya Dumlupınar University author | Mustafa Namdar |
| Emails | `fatih.donmez@usr.aku.edu.tr`; `aaltuncu@aku.edu.tr`; `mustafa.namdar@dpu.edu.tr` |

The emails are historically source verified but were not delivery tested.
IEEE membership grades were omitted because they were not re-verified.

## Resolved without an author decision

1. A compliant candidate title was drafted without making PRISMA the
   scientific center of the survey.
2. The historical author order, affiliations, correspondence, emails, and the
   one verified ORCID were recovered without inventing coauthor ORCIDs.
3. The abstract now carries the compact method and registration disclosures
   required for transparent interpretation while preserving the survey
   findings as its center.
4. Approved no-support and no-competing-interests wording is recorded for a
   future driver.
5. The README now distinguishes materialized local supplements from a public,
   licensed, DOI-bearing release.

## Author-decision blockers

The following fields remain explicitly `AUTHOR_DECISION_REQUIRED`:

1. final manuscript title;
2. CRediT roles for every author;
3. public dataset/software creator list;
4. copyright year;
5. exact rights holder or rights holders;
6. final CC BY 4.0 grant for derived data and author-owned documentation;
7. final MIT grant for author-owned code;
8. clean package-only GitHub route and release URL;
9. release version or tag; and
10. Zenodo or equivalent archive DOI.

Current public correspondence details should also be reconfirmed before
submission. This is a confirmation need, not permission to invent a different
address.

## Release truth audit

- The 2026-08-07 release README says `STAGING DRAFT — DO NOT PUBLISH`.
- `LICENSE_DECISION_REQUIRED.md` states that no license is granted by the
  staging draft.
- The GitHub release URL and Zenodo DOI remain placeholders.
- The active v2 supplements are materialized locally, with QA and checksums,
  but no public repository release or DOI was found in the authoritative
  release metadata.
- The previously recorded draft PR is not a clean, licensed, package-only
  public release and does not close PRISMA Item 27.
- The PDF-bearing monorepo must not be released wholesale.

Therefore no text in this pass calls the data “publicly available,” “released,”
or DOI bearing.

## Remaining downstream work outside this audit

- assemble the final IEEEtran driver only after author approval;
- materialize and insert the remaining planned figures and Tables II–VIII;
- run a new global manuscript, citation, cross-reference, supplement-pointer,
  and denominator gate after all current edits;
- compile and inspect the rendered document only in the later dedicated pass;
  and
- create a public release only after the author-owned rights and repository
  decisions are complete.

## Hash evidence

- corrected abstract:
  `E9BAF5041071AF0B9D97E679457B26CD2856BEFA9C3555A09B412B68E1FC8477`;
- front-matter candidate before this QA report:
  `92B089A90164CFC14E7F64574C4F528F81EB23056EDE3E5B33299A40D2041111`;
- corrected root README before this QA report:
  `D1DA87A9BDB3DAC8E9CCA3588F005AA550E805DB62537F290CA2B86419F2473F`;
- evidence-supplement manifest:
  `47ADB7A9D02D8635445D39FC0531E2326645CE1029A4F004D4B70285774D4000`;
- reporting-supplement manifest:
  `E3F22E20E9513DBFA66BDD93A50F83C5AFEF852CF2C577C924787A0E22D602B4`;
- public-release staging README:
  `244D78AC6B9F666BB45B03056DD161F300B6D2D72B28B8B70CDA6D4D0F48F8A4`;
- license-decision gate:
  `04DE6356F5880DF48FFC3AAFA095085B31AF08F74B93AE48E91F5138DA2C1CAB`.
