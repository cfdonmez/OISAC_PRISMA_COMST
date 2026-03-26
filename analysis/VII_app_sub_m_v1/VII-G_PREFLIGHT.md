# VII-G Preflight (Plan + Cite-Key Shortlist)

## VII-G Title + Scope Statement
- **Title used for VII-G:** `Section 7G Dual-View Comparison` (from `analysis/VII_ev_v2/section7G_dual_view_report.md`).
- **Axis-derived scope keywords:** `Application macro domains`, `Application metadata`, `Evidence gate` (from `analysis/VII_ev_v2/axis_definitions.md` Axis-2/3/4).
- **VII-G scope statement:** compare **structured study-level application tags** against **extracted evidence-row assignments** under both **raw** and **strict** evidence views across Section VII macro domains.

## Dual-View Axes Definition
- **View-1 (Structured tag view):** study-level JSON/domain flag counts (`study_flag_count`).
- **View-2 (Evidence-row view):** extracted evidence counts in two gates (`raw_evidence_count`, `strict_evidence_count`) plus contrast deltas (`raw_only_vs_flag`, `strict_only_vs_flag`).

## Scenario Shortlist (4 Representative Dual-View Contrasts)
| scenario_id/title | view_contrast_tag | cite_keys | evidence_source (G artifact + row/locator) | processed_markdown_paths | representativeness_note |
|---|---|---|---|---|---|
| G-S1: Automotive raw-evidence expansion | automotive_transportation: `flag_vs_raw` (high raw-only delta) | `O_ISAC_010; O_ISAC_024` | `s7g_dual_view_ex.csv:9` (raw_only list), `s7g_dual_view_cmp.csv:4` (`raw_only_vs_flag=137`) | `data/proc_markdowns/O_ISAC_010/O_ISAC_010.md; data/proc_markdowns/O_ISAC_024/O_ISAC_024.md` | This case captures the largest raw-vs-flag expansion in VII-G, making it a primary example of dual-view discrepancy. |
| G-S2: Underwater raw-only asymmetry | underwater_harsh: `flag_vs_raw` (high raw-only, low strict-only) | `O_ISAC_017; O_ISAC_021` | `s7g_dual_view_ex.csv:12` (raw_only list), `s7g_dual_view_cmp.csv:5` (`raw_only_vs_flag=107`, `strict_only_vs_flag=7`) | `data/proc_markdowns/O_ISAC_017/O_ISAC_017.md; data/proc_markdowns/O_ISAC_021/O_ISAC_021.md` | This scenario is representative because underwater shows a strong raw-only expansion but a small strict-only increment, highlighting view sensitivity. |
| G-S3: Smart-infrastructure strict-only surplus | smart_infrastructure: `flag_vs_strict` (high strict-only delta) | `O_ISAC_058; O_ISAC_071` | `s7g_dual_view_ex.csv:4` (strict_only list), `s7g_dual_view_cmp.csv:2` (`strict_only_vs_flag=101`) | `data/proc_markdowns/O_ISAC_058/O_ISAC_058.md; data/proc_markdowns/O_ISAC_071/O_ISAC_071.md` | Smart infrastructure provides the strongest strict-view surplus, making it a core representative for strict-gated contrast. |
| G-S4: Space strict-view uplift | space_satellite: `flag_vs_strict` (strict uplift over flags) | `O_ISAC_070; O_ISAC_356` | `s7g_dual_view_ex.csv:16` (strict_only list), `s7g_dual_view_cmp.csv:6` (`study_flag_count=17`, `strict_evidence_count=34`) | `data/proc_markdowns/O_ISAC_070/O_ISAC_070.md; data/proc_markdowns/O_ISAC_356/O_ISAC_356.md` | Space-satellite shows strict evidence counts exceeding flag baseline, representing a second strict-view contrast pattern distinct from raw-only cases. |
