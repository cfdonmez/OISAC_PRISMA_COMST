# II High-Confidence Summary

Counts by resolution_defensibility_label:
- AMBIGUOUS: 203
- DRMIN_DEFENSIBLE: 18

Counts by snr_plane_label:
- AMBIGUOUS: 200
- ESNR_PLANE: 20
- OSNR_PLANE: 1

eligible_CRQ_highconf = 18

Reconciliation (Section I-E proxy vs high-confidence):
- proxy_count_from_SectionI (N_rate_and_Drmin) = 160
- eligible_CRQ_highconf = 18
- Explanation: proxy reflects availability of rate+resolution fields, while high-confidence requires defensible Δr_min semantics; therefore eligible_CRQ_highconf <= proxy.

Rule: CRQ_Δ synthesis must be restricted to eligible_CRQ_highconf subset.