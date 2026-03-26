# IE QA Report

## Before -> After Change Log (Section I-E)
- Replaced generic five-point contribution list with evidence-backed, quantified contributions tied to the PRISMA extraction corpus.
- Added explicit Contribution-Gap-Section mapping to each item, aligned to Sections III-VII and Gaps 1-5.
- Added metric-contract coverage counts for Delta r_min, sigma_r, and CRQ_Delta feasibility; added modality and application coverage counts.
- Added enabler frequency counts for ORIS/OPA/ML based on extraction tags.
- Preserved the Lesson 2 statement verbatim.

## Checklist
- No Delta R or sigma_R in file: Delta R count = 0; sigma_R count = 0.
- No new citation keys introduced in I-E: only [14] remains.
- Each contribution maps to >=1 Gap and >=1 Section: yes (C1-C5).
- Any numbers in I-E are backed by computed stats: see IE_ev_map.md rows C1-C5.

## Final Section I-E (verbatim)
```markdown
## E. Contributions of This Survey

To close the five gaps identified in Section I-D, we provide evidence-backed contributions grounded in the PRISMA corpus and extraction schema; each item includes a compact Contribution-Gap-Section mapping:

1. **PRISMA evidence base and quality scoring (Gap 2):** We apply the PRISMA 2020 protocol [14] to a unified corpus of 221 studies with bibliographic year metadata available for 219 records (210 in 2020-2025), and we report complete 5-dimension TQAF scores for 208 studies. *Contribution-Gap-Section:* Gap 2 -> Section III.

2. **Cross-modality taxonomy with measured coverage (Gap 1):** We construct a unified taxonomy spanning fiber, FSO, VLC/visible-light, photo-THz, and hybrid O-ISAC; the extracted medium labels include 46 fiber, 19 FSO, 26 VLC/visible-light/UV, 1 photo-THz, and 116 hybrid studies. *Contribution-Gap-Section:* Gap 1 -> Section IV.

3. **Standardized reporting contract and trade-off synthesis (Gap 3):** We normalize reporting using $\Delta r_{\min}$, $\sigma_r$, and $\text{CRQ}_{\Delta}$ and quantify coverage: 217 studies report data-rate metrics, 213 report $\Delta r_{\min}$, 208 report $\sigma_r$, and 171 report CRB/CRLB values; 213 studies report both rate and $\Delta r_{\min}$, enabling $\text{CRQ}_{\Delta}$ comparisons. *Contribution-Gap-Section:* Gap 3 -> Section V.

4. **Enabler-centric synthesis across optical platforms (Gap 5):** We quantify enabling-technology prevalence to ground Section VI, including machine learning (53 studies), optical RIS (ORIS, 8 studies), and optical phased arrays (OPA, 7 studies), and relate these tags to the integration pathways discussed in the enabler section. *Contribution-Gap-Section:* Gap 5 -> Section VI.

5. **Cross-domain transfer map tied to applications (Gap 4):** We build a modality-application transfer map in Section VII; 15 application domains appear in >=2 modality classes (8 domains in >=3), with high-frequency domains including industrial manufacturing (65), vehicular (60), indoor positioning (56), and 6G networking (46). *Contribution-Gap-Section:* Gap 4 -> Section VII.

> **Lesson 2:** A systematic, PRISMA-based methodology enables reproducible evidence synthesis and uncovers research gaps that are invisible in narrative reviews.
```
