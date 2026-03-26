# ID Implementation Plan

- Reset `drafts/section_01_introduction.md` from `drafts/section_01_introduction_backup_20260121.md` to ensure a clean base.
- Remove the SOTA/demo Table I block anchored by "**Table I** summarizes state-of-the-art" and the table header line "| Paper | Modality | Carrier Band | Data Rate | Sensing Metric" and replace it with the exemplar paragraph anchored by "Recent photonic and fiber demonstrations" plus the CRQ_Δ definition and unit conversion.
- Apply the metric contract by targeting the anchors "Δ R", "σ_R", and the displayed equation block starting with `\Delta r=`; replace with `\Delta r_{\min} = v/(2B_{\text{eff}})` and `\sigma_r = \sqrt{E[(\hat r - r)^2]}`; update CRQ_Δ to `CRQ_Δ := R / \Delta r_{\min}` with bps/m units and explicit Gbps/cm conversion.
- Enforce modality-scope symbols in the axis-based table by editing rows anchored by `[O_ISAC_161]`, `[O_ISAC_021]`, `[O_ISAC_070]`, and `[O_ISAC_163]`; replace any "–" in modality-scope cells with ○ and align Tier/Methodology to evidence.
- Renumber tables and references: change the heading anchor "### Table III: Axis-Based..." to "### Table I", replace the in-text anchor "Table III summarizes" with "Table I summarizes", update "Tables IV and V" to "Tables III and IV", and rename the notation/acronym headings from "### Table IV/### Table V" to "### Table III/### Table IV".
- Apply tone fixes by replacing the anchor phrase "a mass of different spectrum resources" with "disjoint spectral resources" and changing "unprecedented pressure" to "significant pressure".

## Evidence files to open (paths found)

- O_ISAC_161
  - JSON: `data/ext_res_v4/O_ISAC_161_v4.json`
  - MD: `data/proc_markdowns/O_ISAC_161/O_ISAC_161.md`
- O_ISAC_068
  - JSON: `data/ext_res_v4/O_ISAC_068_v4.json`
  - MD: `data/proc_markdowns/O_ISAC_068/O_ISAC_068/O_ISAC_068.md`
- O_ISAC_327
  - JSON: `data/ext_res_v4/O_ISAC_327_v4.json`
  - MD: `data/proc_markdowns/O_ISAC_327/O_ISAC_327.md`
- O_ISAC_006
  - JSON: `data/ext_res_v4/O_ISAC_006_v4.json`
  - MD: `data/proc_markdowns/O_ISAC_006/O_ISAC_006/O_ISAC_006.md`
- O_ISAC_368
  - JSON: `data/ext_res_v4/O_ISAC_368_v4.json`
  - MD: `data/proc_markdowns/O_ISAC_368/O_ISAC_368.md`
- O_ISAC_021
  - JSON: `data/ext_res_v4/O_ISAC_021_v4.json`
  - MD: `data/proc_markdowns/O_ISAC_021/O_ISAC_021/O_ISAC_021.md`
- O_ISAC_070
  - JSON: `data/ext_res_v4/O_ISAC_070_v4.json`
  - MD: `data/proc_markdowns/O_ISAC_070/O_ISAC_070/O_ISAC_070.md`
- O_ISAC_163
  - JSON: `data/ext_res_v4/O_ISAC_163_v4.json`
  - MD: `data/proc_markdowns/O_ISAC_163/O_ISAC_163.md`
- O_ISAC_303
  - JSON: `data/ext_res_v4/O_ISAC_303_v4.json`
  - MD: `data/proc_markdowns/O_ISAC_303/O_ISAC_303.md`
