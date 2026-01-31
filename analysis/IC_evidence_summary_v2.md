# Evidence Summary v2 (Patch Run)

## Statistical Overview
- **Total Evidence Items**: 101
- **C4 (Tech Transfer Gap) Evidence**: 26 items (Target > 10 met)
- **C1 (Terminology)**: 30 items
- **C2 (Metrics)**: 45 items

## Modality Distribution
- **VLC**: 43
- **Fiber**: 24
- **Photo-THz**: 16
- **FSO**: 5
- **Other/Generic**: 13

## Identified Conflicts (Fragmentation)
5 explicit fragmentation conflict types identified in `IC_term_metric_conflicts_v2.csv`:

1.  **Terminology Fragmentation**:
    - *Concept*: **Integrated Sensing in Fiber**
    - *Conflict*: 'ISAC-OF' (Paper O_ISAC_006) vs 'photonic ISAC' (Paper O_ISAC_020)
    - *Analysis*: Papers use different terms for essentially the same Integrated Sensing in Fiber concept, hindering searchability.

2.  **Terminology Fragmentation**:
    - *Concept*: **VLC ISAC**
    - *Conflict*: 'VLC' (Paper O_ISAC_022) vs 'LiFi' (Paper O_ISAC_070) - *Note: LiFi often implies VLC subset but used interchangeably.*

3.  **Metric Inconsistency**:
    - *Concept*: **Ranging Accuracy**
    - *Conflict*: 'RMSE' (Paper O_ISAC_009) vs 'CRB' (Paper O_ISAC_056)
    - *Analysis*: Inconsistent evaluation of Ranging Accuracy: One uses 'RMSE' (approx), another uses 'CRB' (bound). Makes direct comparison impossible.

4.  **Metric Inconsistency**:
    - *Concept*: **Ranging Resolution**
    - *Conflict*: 'range resolution' (Paper O_ISAC_011) vs '\Delta R' (Paper O_ISAC_013)
    - *Analysis*: Inconsistent evaluation of Ranging Resolution: One uses 'range resolution', another uses '\Delta R'.

## Top Terminology (Normalized)
- **VLC**: 17 papers
- **photonic ISAC**: 11 papers
- **RO-ISAC**: 8 papers
- **ISAC-OF**: 5 papers

## Next Steps
Use `IC_evidence_claims_v2.csv` to cite specific "Tech Transfer Gap" statements (C4) in the Introduction.
Use `IC_term_metric_conflicts_v2.csv` to construct the "Table I: Fragmentation Matrix" in Section I-C.
