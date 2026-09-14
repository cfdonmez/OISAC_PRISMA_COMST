# Phase E final-workbook invariance audit — 2026-08-04

**Status: PASS**

## Purpose

The frozen normalization crosswalk declares the immediately preceding Phase D workbook. This audit tests whether every Phase E/F/appendix normalization input remained invariant in the final authoritative survey-ready workbook and whether the frozen canonical fields can be reproduced from that final workbook.

Both workbooks were imported with `@oai/artifact-tool` (`SpreadsheetFile.importXlsx`). The audit contains no absolute host paths; source identity is recorded by filename and SHA-256.

## Source identity

| Artifact | Filename | SHA-256 |
|---|---|---|
| Predecessor workbook | OISAC_PHASE_D_FULL_CORPUS_HUMAN_ADJUDICATED_2026-08-03.xlsx | `e0ea51c332483f0e7150b25ecfae9a1b1c19232a74b1f484d1277fd8a46da55c` |
| Final authoritative workbook | OISAC_PHASE_D_SURVEY_READY_2026-08-04.xlsx | `c1b3b89789c6ed3e20da5a6283e480875c1913e21af88ff59ac747a6aa949348` |
| Frozen crosswalk | PHASE_E_TQAF_NORMALIZATION_CROSSWALK_DRAFT_2026-08-04.json | `41d6f8f574bdd0d6eba04806b2930ade8fa1d3d56e28b083de3d56bb13e7d122` |
| Phase E risk output | risk_of_bias.csv | `e5e43476f2c01b3d820005134a6d0f4a696c52c78347b8da2832b1b10e9604a8` |

## Result

- Study IDs: 206; predecessor, final, crosswalk, survey-use, and Phase E risk sets are identical: **yes**.
- Per-study predecessor→final raw/fingerprint checks: 12 check families; mismatches: **0**.
- Final-workbook→frozen-crosswalk recomputations: 17 check families; mismatches: **0**.
- Phase E consumption checks: 12 check families; mismatches: **0**.
- Total evaluated per-study comparisons: 9,476; failed studies: **0**.

The final workbook is therefore invariant for all frozen normalization fields used by Phase E, Phase F, and appendix reporting. The predecessor hash in the crosswalk is retained as lineage metadata; the final-workbook audit is the explicit release bridge to the authoritative Phase D artifact.

## Fields covered

- Study and report identity fields, including study cluster ID and primary/canonical screening IDs.
- Raw and canonical optical modality.
- Validation raw tokens, canonical categories, and maximum maturity.
- Raw and canonical 6G relevance.
- Raw and canonical dataset availability, code/model availability, and repeatability.
- Metric comparability and admissibility category sets.
- Baseline summary, metric baseline-row count, canonical baseline class/value consumption, and relevant metric-input fingerprints.
- Final-only survey-use status, comparison-use gate, quarantine count, validation/TQAF eligibility, and independent-human provenance status.

## Canonical distributions reproduced from the final workbook

- Modality: photonic_THz=69; fiber=56; VLC_LiFi=38; FSO=31; hybrid_optical=9; other_optical=3
- Validation maturity maximum: 2=32; 3=18; 4=78; 5=66; 6=12
- 6G relevance: direct=138; inferred=64; not_applicable=3; weak=1
- Dataset availability: unavailable_or_NR=145; on_request=41; open=13; NA=7
- Code/model availability: unavailable_or_NR=197; on_request=7; NA=1; partial_components=1
- Repeatability: complete_or_substantial=106; partial=99; insufficient_or_NR=1
- Baseline: internal=132; external_or_common=61; none=13

## Final-only survey-use governance

- Survey-use status: survey_ready=175; survey_ready_with_claim_restrictions=31.
- Cross-study comparison use: descriptive_only=191; allowed_for_admissible_claims_only=15.
- Validation/TQAF eligibility: eligible_for_TQAF_scoring=206.
- Independent human status: not_documented=206.

Survey-use governance did not exist in the predecessor workbook. It is not mislabelled as predecessor-invariant; it is validated as a complete final-only authority and reconciled exactly to the values consumed by Phase E.

## Release decision

No frozen-field difference was detected. The existing Phase E/F normalization crosswalk may be used with the final authoritative workbook when this audit accompanies it.
