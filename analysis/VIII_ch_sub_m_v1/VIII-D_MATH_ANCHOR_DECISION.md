# VIII-D Math Anchor Decision Memo

1. Axis lock confirmed: `security_privacy_reliability`.
2. Candidate term pool evaluated: `R_int`, `L_priv`, `A_auth`, `U_service`, `C_overhead`, `availability`.
3. SUPPORTED by direct excerpts: `R_int` (interruption risk, falsification/trustworthiness risk) [O_ISAC_041, O_ISAC_145].
4. SUPPORTED by direct excerpts: `L_priv` (confidential data leakage concern; model-weight exchange policy) [O_ISAC_039].
5. SUPPORTED by direct excerpts: `A_auth` (authentication/integrity centrality; key-management burden in dense heterogeneous networks) [O_ISAC_156].
6. `U_service` support exists via interruption impact and service-adjustment monitoring loop [O_ISAC_041].
7. `C_overhead` is not explicitly bounded in the selected evidence set for a weighted co-design objective.
8. `availability` is discussed qualitatively, but no direct bound-ready variable statement is provided.
9. Decision: **Option-1 (risk-constrained service utility)**.
10. Why Option-2 is weaker: it requires explicit overhead and availability constraint semantics not directly grounded for weighted optimization in this evidence subset.
