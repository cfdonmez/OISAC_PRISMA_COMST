# O-ISAC Systematic Review - Search Strings
**Date:** 2025-11-30
**Protocol Section:** 6.2

Formal PRISMA identification stage for the current freeze:
- `IEEE Xplore`
- `Scopus`
- `Web of Science`

The three sources above define the canonical identification counts reported in `screening/prisma_flow_counts.csv`.

Supplementary monitoring note:
- A template for `arXiv / TechRxiv` is retained below for version tracing and future updates.
- It is not part of the current canonical PRISMA flow unless separately executed and logged.

Applied limits and filters for the current freeze:
- `Language:` English
- `Document type:` peer-reviewed journal articles and proceedings papers, implemented through platform filters where supported
- `Coverage window:` 2000-11-30 to 2025-11-30, with the final synthesis centered on 2020 onwards while retaining earlier protocol-eligible foundational studies

Use the formal-database strings below to search the respective sources. Export results as CSV or RIS and place them in `data/raw_search_results/`.

## 1. IEEE Xplore
**Fields:** Metadata (Title, Abstract, Keywords)
**Platform filters:** English-language journal and conference records
**Command:**
```text
("integrated sensing and communication" OR ISAC OR "joint sensing and communication" OR "joint communication and sensing" OR "joint radar-communication" OR "dual-function radar-communication" OR DFRC OR "simultaneous sensing and communication") AND (optical OR photonic OR "optical fibre" OR "optical fiber" OR fibre OR fiber OR "free-space optical" OR FSO OR "visible light" OR "visible light communication" OR VLC OR LiFi OR LiDAR OR LIDAR OR "optical radar")
```

## 2. Scopus
**Fields:** Title, Abstract, Keywords
**Command:**
```text
TITLE-ABS-KEY ( ( "integrated sensing and communication" OR ISAC OR "joint sensing and communication" OR "joint communication and sensing" OR "dual-function" W/3 (radar OR communication) OR "simultaneous" W/3 (sensing OR ranging) W/3 communication ) AND ( optical* OR photonic* OR "optical fibre" OR "optical fiber" OR fibre* OR fiber* OR "free-space optical" OR FSO OR "visible light" OR "visible light communication" OR VLC OR LiFi OR lidar* OR "optical radar" ) ) AND ( LIMIT-TO ( LANGUAGE, "English" ) )
```

## 3. Web of Science
**Fields:** Topic (TS)
**Command:**
```text
TS=( ("integrated sensing and communication" OR ISAC OR "joint sensing and communication" OR "joint communication and sensing" OR "dual-function radar-communication" OR "simultaneous sensing and communication") AND (optical* OR photonic* OR "optical fibre" OR "optical fiber" OR fibre* OR fiber* OR "free-space optical" OR FSO OR "visible light" OR "visible light communication" OR VLC OR LiFi OR lidar* OR "optical radar") )
```
*Filter by: Document Types: (Article OR Proceedings Paper) AND Language: (English)*

## 4. arXiv / TechRxiv (Supplementary Monitoring Template)
**Command:**
```text
("integrated sensing and communication" OR "joint sensing and communication" OR ISAC) AND (optical OR "optical fiber" OR "optical fibre" OR FSO OR VLC OR LiFi OR LiDAR OR "optical radar")
```
