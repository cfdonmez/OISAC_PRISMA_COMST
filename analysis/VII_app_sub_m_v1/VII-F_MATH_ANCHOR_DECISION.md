# VII-F Run4 Decision Memo
1. Decision scope: choose one family between Anchor-A and Anchor-B for VII-F cross-domain applications synthesis.
2. Step D1 (Anchor-A feasibility): feasible, because prior run evidence includes comm-plane BER and sensing-plane MSE or RMSE in the same indoor O-ISAC studies (`O_ISAC_108`, `O_ISAC_011`).
3. Anchor-A support references: `VII-F_SCENARIOS_34_TAKEAWAYS_supp.md` locators `O_ISAC_108` line 31 and `O_ISAC_011` lines 145 and 153.
4. Step D2 (Anchor-B feasibility): feasible with direct summary artifacts for coverage, domain incidence, and transfer structure.
5. Coverage terms are directly supported by macro counts in `s7f_macro_med_cov.csv` rows 2-6 and micro counts in `s7f_micro_dom_cnts.csv` rows 2-5.
6. Portfolio incidence terms are supported by `section7F_paper_macro_map.csv` schema row 1 and paper-domain rows such as 12, 108, 143, 164, 173, and 191.
7. Transfer terms are supported by shared-medium structure in `section7F_transfer_map.csv`, including `hybrid` rows 3, 15, 25, 32, 36 and `wireless_vlc` rows 13, 23, 30, 39.
8. Global cardinality support is available from `section7F_summary.json` keys `n_total_papers=221` and `n_unique_micro_domains=48`.
9. Step D3 selection: Anchor-B is selected because VII-F is explicitly cross-domain and the artifact support is concrete rather than speculative.
10. Anchor-A is not selected although feasible, because a single-scenario trade-off does not encode coverage breadth and transfer structure central to VII-F.
