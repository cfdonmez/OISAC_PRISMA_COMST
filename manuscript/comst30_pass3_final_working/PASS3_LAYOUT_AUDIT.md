# PASS-3 Layout Audit

## Baseline vs Final

| Metric | Baseline | Final |
|---|---:|---:|
| Page count | 26 | 26 |
| Overfull hbox | 0 | 0 |
| Underfull hbox | 100 | 17 |
| Underfull vbox | 5 | 6 |
| Undefined citations | 0 | 0 |
| Undefined references | 0 | 0 |

## Layout Changes

| Object | Issue | Fix | Result |
|---|---|---|---|
| Main-text `tabularx` tables | Narrow justified p-columns generated many underfull hbox warnings | Added local `L{}` ragged-right p-column type and applied it to fixed-width table columns | Underfull hbox count reduced from 100 to 17 without changing table values. |
| Compact taxonomy table | `39 photonic-THz anchors` could be read as a conflicting medium count | Reworded to `39 direct photonic-THz anchors`; added clarifying prose | Numeric interpretation is clearer. |
| Figure/table references | Several retained figures/tables were not explicitly cited in prose | Added short references to all retained figures/tables | All main figures and tables are cited in order. |
| Running header | `Draft Manuscript` was submission-rough wording | Changed to neutral COMST submission header | Cleaner submission-facing build. |

## Remaining Underfull Warnings

| Warning type | Source lines | Notes |
|---|---|---|
| Underfull hbox | 87--90 | Short Introduction transition/contribution paragraphs. Harmless in IEEE two-column layout. |
| Underfull hbox | 206--207 | Methodology search-block sentence in a narrow column. Left unchanged to preserve wording. |
| Underfull hbox | 269--318 | Methodology/TQAF prose. Harmless paragraph-level warnings. |
| Underfull hbox | 363--386 | Taxonomy prose around long waveform acronyms and phrase breaks. Left unchanged. |
| Underfull hbox | 508--509 | Section V benchmark implication prose. Left unchanged to protect core meaning. |
| Underfull hbox | 569--570, 618--627, 719--720 | Enabler/roadmap prose with compound technical terms. Left unchanged. |
| Underfull vbox | pages around major figures/floats | IEEE float balancing artifact; no overfull boxes. |

## Figure/Table Audit

Figures cited in order:

1. `fig:fig1`
2. `fig:fig_ii_1`
3. `fig:fig_iii_1`
4. `fig:fig_iv_1`
5. `fig:fig_v_1`
6. `fig:fig_vi_2`
7. `fig:fig_viii_1`

Tables cited in order:

1. `tab:axis_comparison`
2. `tab:ii1`
3. `tab:ii2`
4. `tab:iii1`
5. `tab:taxonomy_compact`
6. `tab:governance_attrition`
7. `tab:comparative_slices`
8. `tab:vi_a_enablers`
9. `tab:vi_d_reporting`
10. `tab:section7_portfolio`
11. `tab:challenge_compact`
12. `tab:viii_f_2`

No duplicate labels, missing label references, or references to removed figures/tables were found.
