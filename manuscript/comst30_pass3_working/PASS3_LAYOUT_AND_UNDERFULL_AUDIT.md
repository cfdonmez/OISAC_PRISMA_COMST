# PASS3 Layout and Underfull Audit

## Build Context

- Working source: `manuscript/comst30_pass3_working/bare_jrnl_new_sample4.tex`
- Baseline build: 27 pages, 0 overfull hbox, 99 underfull hbox, 8 underfull vbox
- Final clean build: 27 pages, 0 overfull hbox, 16 underfull hbox, 7 underfull vbox
- No global `\sloppy` or package-heavy layout workaround was introduced.

## Top Warning Locations After Cleanup

| Warning type | Badness | Source line | Nearby object | Proposed fix |
|---|---:|---:|---|---|
| Underfull hbox | 10000 | 355--356 | TQAF scoring paragraph | Left as harmless narrow-column paragraph; further rewrite would be style-level rather than layout-critical. |
| Underfull hbox | 8189 | 243--245 | Methodology/search-block paragraph | Left after adding Table III reference; the line is dense but readable. |
| Underfull hbox | 5637 | 355--356 | TQAF scoring paragraph | Left; no overfull or visible table break risk. |
| Underfull hbox | 4954 | 355--356 | TQAF scoring paragraph | Left; compact IEEE column behavior. |
| Underfull hbox | 4316 | 402--403 | Shared-waveform taxonomy prose | Left; contains long waveform acronym sequence. |
| Underfull hbox | 3668 | 88--89 | Introduction fragmentation paragraph | Left; opening contribution prose remains readable. |
| Underfull hbox | 3503 | 618--619 | ML/security paragraph | Left; multi-term enabler list is unavoidable without heavier rewrite. |
| Underfull hbox | 3058 | 768--769 | Hardware scalability paragraph | Left; acceptable narrow-column line. |
| Underfull vbox | 10000 | output routine | Float pages around main figures | Left as harmless IEEE float-placement artifact. |

## Layout Fixes Applied

| Area | Change | Effect |
|---|---|---|
| Table column behavior | Added `L{}` and `Y` ragged-right column types for `tabularx` tables. | Reduced underfull hbox warnings from 99 to 16 without changing values or table order. |
| Related survey table | Converted paragraph-like columns to ragged-right table columns. | Reduced narrow-column justification stress. |
| Modality table | Shortened several long cells and converted columns to ragged-right. | Preserved governance meaning while improving table fit. |
| Metric contract table | Shortened OSNR/SNR disclosure wording. | Preserved plane distinction. |
| Eligibility table | Converted columns to ragged-right and added explicit text reference. | Improved citation/order clarity. |
| Taxonomy table | Converted columns to ragged-right and shortened one task cell. | Preserved counts and warnings. |
| Governed attrition and comparative slices tables | Converted columns to ragged-right; shortened selected slice wording. | Reduced table-induced badness while preserving Section V core. |
| Enabler/reporting tables | Converted columns to ragged-right; shortened reporting-risk cells. | Kept enabler categories and benchmark contract intact. |
| Application and roadmap tables | Converted columns to ragged-right; shortened challenge/agenda cells. | Preserved page count and readability. |

## Figure and Citation Order Check

| Object | Status | Notes |
|---|---|---|
| Main figures | OK | Seven figure environments remain. No new figures were added and no removed figures were restored. |
| Main tables | OK | Twelve table environments remain. No large moved tables were restored. |
| Figure references | OK | Added/verified explicit references for PRISMA and taxonomy figures where needed. |
| Table references | OK | Added/verified explicit references for `tab:ii1`, `tab:iii1`, `tab:challenge_compact`, and `tab:viii_f_2`. |
| Removed figures/tables | OK | No active reference to original removed Fig. 2/Fig. 3 was found during the Pass-3 source scan. |

## Remaining Harmless Warnings

The remaining underfull warnings are mostly paragraph-level narrow-column artifacts and float-placement vboxes. They are not overfull boxes, undefined references, or broken floats. Further reduction would require heavier prose rewriting or float restructuring, which was outside the controlled Pass-3 scope.
