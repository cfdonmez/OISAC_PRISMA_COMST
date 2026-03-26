# Section VIII-D Preflight

**Subsection Title:** security_privacy_reliability
**Subsection Axis Label:** security_privacy_reliability
**Scope Keywords (axis-locked):** security_privacy_reliability; physical_layer_security_eavesdropping_jamming; privacy_leakage_via_sensing; key_management_authentication_trust_edge; reliability_integrity_monitoring_fail_safe

## Selection Plan

1. Gate lock: `section_VIII_intent == Open Challenges and Research Roadmap`; axis lock `security_privacy_reliability`.
2. Candidate pool: `section8D_evidence.csv` rows with `match_type != upstream_bridge` and `llm_label_pass2 != NONE`.
3. Dedup lock: `cluster_map.csv` present but no cluster-id field; fallback applied: no duplicate cite-key sets across cases.
4. Diversity lock: 4 cases with >=3 distinct motif signatures.
5. Evidence checks per key: `references.bib` existence, markdown path resolution (`file_index.csv` else `II_markdown_inventory.csv`), `contract_violations.csv` presence and mitigation note.

## 4-Case Shortlist

| case_id/title | motif_signature | cite_keys | evidence_row_locators | markdown_paths | violations_flag | note |
|---|---|---|---|---|---|---|
| Case_1: eavesdropping/jamming physical-layer threat surface | physical_layer_security_eavesdropping_jamming | O_ISAC_145 | section8D_evidence.csv:R172 | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_145\O_ISAC_145\O_ISAC_145.md [HIT_FALLBACK] | Y | downgrade claim |
| Case_2: federated sensing-data privacy leakage risk | privacy_leakage_via_sensing_federated_learning | O_ISAC_039 | section8D_evidence.csv:R43 | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_039\O_ISAC_039.md [HIT_FALLBACK] | Y | downgrade claim |
| Case_3: authentication/trust exposure in keyless PLS landscape | key_management_authentication_trust_edge | O_ISAC_156 | section8D_evidence.csv:R196 | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_156\O_ISAC_156\O_ISAC_156.md [HIT_FALLBACK] | Y | downgrade claim |
| Case_4: fail-safe integrity monitoring under disruptive events | reliability_integrity_monitoring_fail_safe | O_ISAC_041 | section8D_evidence.csv:R49 | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_041\O_ISAC_041.md [HIT_FALLBACK] | N | NONE |
