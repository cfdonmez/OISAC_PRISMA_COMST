# PRISMA Evidence Pack

Purpose:

- This package is a ready-to-upload evidence pack for the PRISMA 2020 study-selection flow reported in the O-ISAC review manuscript.
- It is designed for `OSF`, `Zenodo`, or journal supplementary-material submission.
- It contains derived audit files and protocol/search documentation.

What this pack is for:

- support the PRISMA flow diagram counts
- document the search strategy and source policy
- expose the full-text exclusion trail
- expose the final included-study ledger
- separate row-backed stages from reconstructed upstream stages

What this pack is not:

- It is not a redistribution bundle for proprietary raw database exports.
- It does not claim that the full upstream `980 -> 280 -> 700` chain is completely row-backed in the current repo snapshot.

## Recommended public-sharing policy

Safe to share publicly:

- protocol text
- search strings
- PRISMA flow counts
- full-text exclusion log
- full-text assessed reconstruction
- included-study canonical ledger
- reconstruction notes
- evidence-map notes

Do not upload blindly without checking license terms:

- raw IEEE Xplore exports
- raw Scopus exports
- raw Web of Science exports
- publisher-platform exports downloaded under platform-specific terms

## Current evidence boundary

The current repository strongly supports the late-stage PRISMA chain:

- `222 full-text assessed`
- `2 full-text excluded`
- `220 included studies`

The earlier stages remain reconstruction-supported rather than fully row-backed in the current snapshot:

- `980 identified`
- `280 duplicates removed`
- `700 screened`
- `478 title/abstract exclusions`

This boundary should be stated honestly in the manuscript or supplement.

## Package structure

- `01_protocol/`
  - protocol and search-strategy files
- `02_search_and_flow/`
  - formal search-stage reconstruction and PRISMA flow files
- `03_screening_and_inclusion/`
  - exclusion logs, assessed-set files, included-study ledgers
- `04_audit_notes/`
  - narrative reconstruction notes and evidence map
- `05_appendix/`
  - included-studies appendix artifact for supplement packaging

## Suggested manuscript linkage

Methods sentence:

`The PRISMA audit package underlying the study-selection flow, including the flow counts, search-strategy documentation, full-text exclusion log, and included-study ledger, is provided in the supplementary materials and archived in an open repository.`

Data-availability sentence:

`Derived audit materials supporting the PRISMA 2020 flow are publicly available in the review evidence pack. Because some source-platform exports may be subject to database-specific redistribution restrictions, the public archive provides derived audit files rather than redistributing proprietary raw-search exports.`

## Most important files in this pack

- `02_search_and_flow/prisma_flow_counts.csv`
- `03_screening_and_inclusion/excluded_fulltext_log.csv`
- `03_screening_and_inclusion/fulltext_assessed_reconstruction.csv`
- `03_screening_and_inclusion/included_studies_canonical.csv`
- `03_screening_and_inclusion/canonical_included_corpus_ledger.csv`
- `04_audit_notes/section3_evidence_reconstruction.md`
- `04_audit_notes/10_prisma_flow_evidence_map.md`

