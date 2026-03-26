# Section VIII-E Preflight

**Subsection Title:** deployment_convergence_roadmap
**Subsection Axis Label:** deployment_convergence_roadmap
**Scope Keywords (axis-locked):** deployment_convergence_roadmap; system_convergence_comm_sensing_control; scaling_orchestration_multinode_integration; maturity_readiness_rollout_staging; cross_domain_transferability_governance

## Selection Plan

1. Gate lock: `section_VIII_intent == Open Challenges and Research Roadmap`; axis lock `deployment_convergence_roadmap`.
2. Candidate pool: `section8E_evidence.csv` rows for section `8E`; prioritize non-`upstream_bridge` rows.
3. Dedup lock: `cluster_map.csv` exists but no cluster-id column; fallback applied: no duplicate cite-key sets across cases.
4. Diversity lock: 4 cases with >=3 distinct motif signatures.
5. Evidence checks per key: `references.bib` existence, markdown path resolution (`file_index.csv` else `II_markdown_inventory.csv`), `contract_violations.csv` presence and mitigation note.

## 4-Case Shortlist

| case_id/title | motif_signature | cite_keys | evidence_row_locators | markdown_paths | violations_flag | note |
|---|---|---|---|---|---|---|
| Case_1: comm+sensing deployment coupling in unified workflow | system_convergence_comm_sensing_coupling | O_ISAC_039 | section8E_evidence.csv:R43 | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_039\O_ISAC_039.md [HIT_FALLBACK] | Y | downgrade claim |
| Case_2: multimodal context orchestration for deployment state fusion | scaling_orchestration_multimodal_llm_context | O_ISAC_151 | section8E_evidence.csv:R155 | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_151\O_ISAC_151\O_ISAC_151.md [HIT_FALLBACK] | Y | downgrade claim |
| Case_3: practical roll-out readiness and TRL-style staging signal | maturity_readiness_rollout_trl_staging | O_ISAC_163 | section8E_evidence.csv:R167 | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_163\O_ISAC_163.md [HIT_FALLBACK] | Y | downgrade claim |
| Case_4: open-source implementation hooks for convergence transferability | transferability_governance_open_source_impl_hooks | O_ISAC_200 | section8E_evidence.csv:R183,R184 | c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns\O_ISAC_200\O_ISAC_200.md [HIT_FALLBACK] | Y | downgrade claim |
