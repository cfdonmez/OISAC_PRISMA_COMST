# Section 4 Mapping Rules (v2)

1. Primary axis assignment uses structured JSON field when available.
2. If JSON missing, use strongest anchor evidence (DIRECT > INDIRECT > NONE).
3. For multi-task labels, split by `|` and retain all; primary is first token.
4. Hybrid media remain `hybrid`; no forced decomposition.
5. Label normalization applies before clustering (`NORMALIZE_LABELS=True`).
6. Contradictory anchors are kept and flagged via `contract_violations.csv`.