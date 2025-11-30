# O-ISAC Systematic Review - Search Strings
**Date:** 2025-11-30
**Protocol Section:** 6.2

Use these strings to search the respective databases. Export results as CSV or RIS and place them in `data/raw_search_results/`.

## 1. IEEE Xplore
**Fields:** Metadata (Title, Abstract, Keywords)
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

## 4. arXiv / TechRxiv
**Command:**
```text
("integrated sensing and communication" OR "joint sensing and communication" OR ISAC) AND (optical OR "optical fiber" OR "optical fibre" OR FSO OR VLC OR LiFi OR LiDAR OR "optical radar")
```
