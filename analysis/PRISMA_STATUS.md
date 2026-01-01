# 📊 O-ISAC Systematic Review Status (PRISMA)

**Last Updated:** 2026-01-02 01:21
**Status:** Phase 2 (Extraction) In Progress


## 1. PRISMA Flow Diagram

```mermaid
graph TD
    A[Identification] --> B[Screening]
    B --> C[Eligibility]
    C --> D[Included]
    D --> E2[Extraction Complete<br/>k=221]


    subgraph Identification
    A1[Records Identified from Scopus<br/>k=416] --> A
    end

    subgraph Screening
    A --> E[Duplicates Removed<br/>k=152]
    A --> F[Records Screened<br/>k=264]
    F --> G[Excluded by AI/Criteria<br/>k=175]
    end

    subgraph Eligibility
    F --> H[Sought for Retrieval<br/>k=243]
    H --> I[Not Retrieved<br/>(No Full Text/Missing PDF)<br/>k=23]
    end

    subgraph Included
    H --> J[Studies Included for<br/>Extraction & Synthesis<br/>k=221]

    end
```

## 2. Phase Breakdown

### Phase 1: Identification & Screening (✅ Complete)
- **Total Records Logged:** 416
- **Duplicates Found:** 152
- **Screened by AI (Llama 3.3):** 225 Candidates
- **Excluded by AI:** ~148
- **Date Check Before 2020:** 11

### Phase 2: Retrieval & Eligibility (✅ Complete)
- **Target for Retrieval:** 243
- **PDFs Successfully Retrieved:** 220 (90.5%)
- **Missing/Unretrievable:** 23 (Excluded)

### Phase 3: Extraction (🚀 In Progress)
- **Ready for Processing:** 221 Studies
- **Visual Analysis Completed:** 221/221 (100%)
- **Tracker File:** `analysis/phase2_extraction/extraction_tracker.md` (To be initialized)


## 3. Key Files
- **Master Log:** `analysis/phase1_screening/screening_log.csv`
- **Included List:** `analysis/phase1_screening/included_studies_list.csv`
- **PDF Folder:** `data/retrieved_docs/`
