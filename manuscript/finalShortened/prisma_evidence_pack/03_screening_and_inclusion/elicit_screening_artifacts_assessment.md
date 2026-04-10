# Elicit Screening Artifacts Assessment

Purpose

- This note evaluates whether the copied `Elicit` CSV files can help support the PRISMA workflow narrative.
- The goal is not to treat them as the canonical frozen PRISMA ledger.
- The goal is to determine whether they can be used as auxiliary screening artifacts for workflow transparency.

## Files assessed

### Main screening artifact

- `reivew_2__datalar__Elicit - screen-results-review-226c619b-1930-4d4f-b156-ad106a003375.csv`

Observed structure:

- `695` records
- explicit `Screening judgement` column
- explicit reasoning fields for multiple criteria

Observed screening distribution:

- `590 Exclude`
- `105 Include`

Observed domain-specific flags:

- `Optical Domain (not RF)`: `102 yes`, `16 maybe`, `577 no`
- `OPA Present (optical phased array)`: `18 yes`, `1 maybe`, `676 no`
- `Free-Space Optical Systems`: `82 yes`, `19 maybe`, `594 no`

Observed overlap with the current canonical included corpus:

- `10` DOI-level matches
- `45` title-level matches

Interpretation:

- This file is clearly a structured screening-stage artifact.
- It is not identical to the current canonical O-ISAC corpus.
- However, it is not unrelated noise either; it contains a meaningful partial overlap with the current review universe.
- Therefore, it can be used as an auxiliary screening artifact, but not as the canonical PRISMA flow ledger.

### Earlier screening snapshot

- `reivew_2__adım1__Elicit - screen-results-review-226c619b-1930-4d4f-b156-ad106a003375.csv`

Observed structure:

- `578` records
- explicit `Screening judgement` column

Observed screening distribution:

- `493 Exclude`
- `85 Include`

Interpretation:

- This appears to be an earlier or smaller screening snapshot.
- It is useful for showing that a structured title/abstract decision layer existed before the later `695`-row variant.

### Gather-stage candidate pool

- `reivew_2__adım1__Elicit - gather-results-review-226c619b-1930-4d4f-b156-ad106a003375.csv`

Observed structure:

- `578` records
- bibliographic candidate fields only

Interpretation:

- This looks like a pre-screen candidate pool.
- It is useful as an upstream discovery artifact, not as a screening-decision ledger.

### Extraction-stage derivatives

- `reivew_2__datalar__Elicit - extract-results-review-226c619b-1930-4d4f-b156-ad106a003375.csv`
- `reivew_2__Elicit - extract-results-review-226c619b-1930-4d4f-b156-ad106a003375 (1).csv`

Observed structure:

- `105` extracted records in each visible extract file

Interpretation:

- These are useful for showing a downstream extraction-oriented stage.
- They are not screening logs by themselves.

## What this means for PRISMA Item 8

These files help with workflow plausibility, not with canonical-count proof.

They can support statements like:

- a structured candidate gathering stage existed
- a structured screening stage with include/exclude judgments existed
- criteria-based screening reasoning was documented in tabular form

They should not be used to claim:

- that the current frozen PRISMA counts were fully generated from these files alone
- that the `695`-row screen file is the canonical screening ledger behind the published `700` count
- that the final `220` included corpus is fully identical to the Elicit screening pool

## Safe usage recommendation

Use these files as:

- `auxiliary_noncanonical_screening_artifacts`

Do not use these files as:

- `canonical_frozen_prisma_flow_ledger`

## Safe wording for the manuscript or supplement

`In addition to the canonical reconstructed screening ledger retained for the frozen review, earlier structured screening artifacts from an Elicit-assisted candidate triage workflow were preserved as auxiliary materials. These files document criteria-based include/exclude judgments and support the reproducibility of the screening workflow narrative, but they are not treated as the canonical source of the final frozen PRISMA counts.`

