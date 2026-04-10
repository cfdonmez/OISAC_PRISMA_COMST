# OSF Upload Checklist

Use this checklist when publishing the PRISMA evidence pack on OSF or Zenodo.

## 1. Upload these folders

- `01_protocol`
- `02_search_and_flow`
- `03_screening_and_inclusion`
- `04_audit_notes`
- `05_appendix`

## 2. In the repository description, say this

`This repository contains the derived PRISMA 2020 audit package for the O-ISAC systematic review, including protocol/search documentation, flow counts, full-text exclusion records, full-text assessed reconstruction, and the final included-study ledger.`

## 3. Add these tags

- `PRISMA 2020`
- `systematic review`
- `O-ISAC`
- `optical ISAC`
- `study selection`
- `evidence pack`

## 4. Mark these points clearly in the README or description

- canonical formal sources are `IEEE Xplore`, `Scopus`, and `Web of Science`
- supplementary monitoring sources did not add separate records to the frozen PRISMA flow
- late-stage counts are row-backed
- upstream counts are reconstruction-supported in the current snapshot

## 5. Do not upload these unless redistribution is explicitly allowed

- raw IEEE Xplore export files
- raw Scopus export files
- raw Web of Science export files
- any platform-origin file with unclear redistribution terms

## 6. Minimum public package if you want a lean release

- `prisma_flow_counts.csv`
- `excluded_fulltext_log.csv`
- `included_studies_canonical.csv`
- `canonical_included_corpus_ledger.csv`
- `fulltext_assessed_reconstruction.csv`
- `search_strings.md`
- `prisma_proto.md`
- `section3_evidence_reconstruction.md`
- `10_prisma_flow_evidence_map.md`

## 7. If the journal asks for supplement-only instead of OSF

- submit `included_studies_appendix.tex` or a journal-formatted appendix table
- submit the exclusion log as a supplementary CSV or PDF table
- keep the full derived evidence pack on OSF or Zenodo and cite the link in the data-availability statement

