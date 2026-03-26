# VIII-F Supplement (Merged, Deduplicated Excerpts)

## Deduplicated Excerpt Registry

- id: EX01
  cite_key: O_ISAC_049
  locator: data/proc_markdowns/O_ISAC_049/O_ISAC_049/O_ISAC_049.md:L39
  excerpt: "both sensing and communication systems lead to a competition of limited resources"

- id: EX02
  cite_key: O_ISAC_107
  locator: data/proc_markdowns/O_ISAC_107/O_ISAC_107/O_ISAC_107.md:L456
  excerpt: "requires the prior acquisition of a set of measurements that should ideally be repeated when using a new UE"

- id: EX03
  cite_key: O_ISAC_107
  locator: data/proc_markdowns/O_ISAC_107/O_ISAC_107/O_ISAC_107.md:L456
  excerpt: "requires the prior acquisition of a set of measurements ... restrictive for a large-scale deployment"

- id: EX04
  cite_key: O_ISAC_133
  locator: data/proc_markdowns/O_ISAC_133/O_ISAC_133/O_ISAC_133.md:L35
  excerpt: "the transmission of additional OFDM blocks increases bandwidth consumption and intensifies channel noise"

- id: EX05
  cite_key: O_ISAC_133
  locator: data/proc_markdowns/O_ISAC_133/O_ISAC_133/O_ISAC_133.md:L35
  excerpt: "necessitating a careful balance between mitigating clipping distortion and limiting noise enhancement"

- id: EX06
  cite_key: O_ISAC_156
  locator: data/proc_markdowns/O_ISAC_156/O_ISAC_156/O_ISAC_156.md:L978
  excerpt: "requires parallel development of a unified analytical framework"

## VIII-F Artefact Evidence

- artifact: axis-domain list (A-E only)
  locator: analysis/VIII_ev_v1/axis_definitions.md:L4
  excerpt: "Axis-2 Challenge domains: standardization_interoperability, hardware_scalability_efficiency, channel_modeling_evaluation, security_privacy_reliability, deployment_convergence_roadmap."

- artifact: E isolated observation
  locator: analysis/VIII_ev_v1/s8f_dep_cov.csv:L6
  excerpt: "deployment_convergence_roadmap,0,0,0"

- dependency coverage rows used: `standardization_interoperability=55/55/55`, `channel_modeling_evaluation=54/54/54`, `hardware_scalability_efficiency=25/25/25`, `security_privacy_reliability=18/18/18`, `deployment_convergence_roadmap=0/0/0`
- research_agenda row IDs used: `standardization_interoperability`, `channel_modeling_evaluation`, `hardware_scalability_efficiency`, `security_privacy_reliability`, `deployment_convergence_roadmap`
- paper_challenge_map rows used: `O_ISAC_049`, `O_ISAC_107`, `O_ISAC_133`, `O_ISAC_156`
- summary.json key paths used: `n_standardization_interoperability_papers`, `n_hardware_scalability_efficiency_papers`, `n_channel_modeling_evaluation_papers`, `n_security_privacy_reliability_papers`, `n_deployment_convergence_roadmap_papers`, `n_multi_challenge_papers`
- summary_table rows used: all five challenge-domain rows in `section8F_summary_table.csv`
- contract_violations rows used: `O_ISAC_107`, `O_ISAC_156`
- duplicate-path decision: `O_ISAC_049` had inventory hits at `analysis/II_md_inv.csv:L50` and `analysis/II_md_inv.csv:L266`; the nested path `data/proc_markdowns/O_ISAC_049/O_ISAC_049/O_ISAC_049.md` was selected deterministically to match the preflight convention
