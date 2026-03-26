# Section I-D Table III Upgrade QA Note

**Generated:** 2026-01-20 01:55
**Action:** Upgraded Gap Synthesis and Table III to COMST specifications (Assessment: Final).

## 1. Table Composition

- **Total Rows:** 12 (11 Reference Papers + 1 "This Survey" row)
- **Comparator:** "This Survey" vs Tier-1 (True O-ISAC) vs Tier-2 (Feeder)
- **Visuals:** Harvey balls (●, ◐, ○) used for 4 axes.

## 2. Included Papers (Representative Set)

### Tier-1 (True O-ISAC) - 100% Inclusion
- [O_ISAC_163] (Photo-THz RIS, Narrative)
- [O_ISAC_303] (VLC Integrated, Narrative)

### Tier-2 (Feeder) - Strategic Sampling
- **VLC Cluster:** 
  - [O_ISAC_161] (Hardware focus)
  - [O_ISAC_068] (General prospects)
  - [O_ISAC_327] (Channel modeling)
- **Fiber Cluster:**
  - [O_ISAC_006] (Mini-Review)
  - [O_ISAC_041] (Diagnosis)
  - [O_ISAC_090] (Experimental vibration)
- **FSO/THz Cluster:**
  - [O_ISAC_021] (FSO Architecture Tutorial)
  - [O_ISAC_070] (Photo-THz Waveforms)
  - [O_ISAC_016] (Sub-THz High-CRQ Experiment)

## 3. Justification for Logic

1.  **Axis Selection:** 
    - "Modality Scope" (Fiber/FSO/VLC) proves fragmentation.
    - "Methodology" (Narrative vs PRISMA) proves the systematic gap.
    - "Taxonomy Breadth" proves the lack of unified frameworks.
2.  **Sampling Strategy:** 
    - Selected `O_ISAC_090` and `O_ISAC_016` (Experimental) to contrast with `O_ISAC_021` (Tutorial) and `O_ISAC_161` (Narrative), showing the mix of evidence types in the literature.
    - Prioritized papers with explicit scope definitions found in the CSV.
3.  **Prose Scoping:** 
    - Removed "no taxonomy exists" → replaced with "Within the optical-ISAC corpus...".
    - Added specific metric definitions ($\Delta R = c/2B$) to ground the "normalization" claim.

## 4. Compliance Check
- [x] No external [1] citations.
- [x] Gap synthesis is relative/scoped, not absolute.
- [x] Lesson 1 block added at the end.
- [x] Table III legend is explicit.
