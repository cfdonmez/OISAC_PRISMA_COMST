# VIII-G Supplement

## Artefact Evidence Block

### axis_definitions.md

- locator: `analysis/VIII_ev_v1/axis_definitions.md:L4`
  used_for: Axis-2 lock; A-E remain the only challenge domains
  excerpt: `Axis-2 Challenge domains: standardization_interoperability, hardware_scalability_efficiency, channel_modeling_evaluation, security_privacy_reliability, deployment_convergence_roadmap.`

### section8G_cross_section_report.md

- locator: `analysis/VIII_ev_v1/section8G_cross_section_report.md:L3`
  used_for: VIII-G alignment-audit purpose
  excerpt: `This report compares strict Section VIII challenge evidence with upstream Section V/VI/VII linkage signals.`
- locator: `analysis/VIII_ev_v1/section8G_cross_section_report.md:L5-L8`
  used_for: `standardization_interoperability` aggregate continuity
- locator: `analysis/VIII_ev_v1/section8G_cross_section_report.md:L10-L13`
  used_for: `hardware_scalability_efficiency` aggregate continuity
- locator: `analysis/VIII_ev_v1/section8G_cross_section_report.md:L15-L18`
  used_for: `channel_modeling_evaluation` aggregate continuity
- locator: `analysis/VIII_ev_v1/section8G_cross_section_report.md:L20-L23`
  used_for: `security_privacy_reliability` aggregate continuity
- locator: `analysis/VIII_ev_v1/section8G_cross_section_report.md:L25-L28`
  used_for: `deployment_convergence_roadmap` zero-row state

### s8g_xsec_align.csv

- locator: `analysis/VIII_ev_v1/s8g_xsec_align.csv:L2`
  used_for: `standardization_interoperability` row
  row: `standardization_interoperability,55,55,55,55,55,0`
- locator: `analysis/VIII_ev_v1/s8g_xsec_align.csv:L3`
  used_for: `hardware_scalability_efficiency` row
  row: `hardware_scalability_efficiency,25,25,25,25,25,0`
- locator: `analysis/VIII_ev_v1/s8g_xsec_align.csv:L4`
  used_for: `channel_modeling_evaluation` row
  row: `channel_modeling_evaluation,54,54,54,54,54,0`
- locator: `analysis/VIII_ev_v1/s8g_xsec_align.csv:L5`
  used_for: `security_privacy_reliability` row
  row: `security_privacy_reliability,18,18,18,18,18,0`
- locator: `analysis/VIII_ev_v1/s8g_xsec_align.csv:L6`
  used_for: `deployment_convergence_roadmap` row
  row: `deployment_convergence_roadmap,0,0,0,0,0,0`

### s8g_xsec_ex.csv

- locator: `analysis/VIII_ev_v1/s8g_xsec_ex.csv:L2`
  used_for: example-payload status for `standardization_interoperability`
  row: `standardization_interoperability,strict_without_upstream,`
- locator: `analysis/VIII_ev_v1/s8g_xsec_ex.csv:L3`
  used_for: example-payload status for `hardware_scalability_efficiency`
  row: `hardware_scalability_efficiency,strict_without_upstream,`
- locator: `analysis/VIII_ev_v1/s8g_xsec_ex.csv:L4`
  used_for: example-payload status for `channel_modeling_evaluation`
  row: `channel_modeling_evaluation,strict_without_upstream,`
- locator: `analysis/VIII_ev_v1/s8g_xsec_ex.csv:L5`
  used_for: example-payload status for `security_privacy_reliability`
  row: `security_privacy_reliability,strict_without_upstream,`
- locator: `analysis/VIII_ev_v1/s8g_xsec_ex.csv:L6`
  used_for: example-payload status for `deployment_convergence_roadmap`
  row: `deployment_convergence_roadmap,strict_without_upstream,`

## Notes

- source mode: artefact-only
- paper-level cite-key mode not used in VIII-G due to empty examples payload
- aggregate continuity finding used: A-D rows remain matched at `strict_without_upstream_count = 0`
- zero-row finding used: `deployment_convergence_roadmap` remains `0/0/0`
- example-availability finding used: payload is absent across all current rows
