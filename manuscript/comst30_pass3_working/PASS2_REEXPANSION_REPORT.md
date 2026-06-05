# PASS2 Re-Expansion Report

## Phase 0 Baseline Build

- Working directory: `manuscript/comst30_pass2_working/`
- Copied source: `manuscript/comst30_working/bare_jrnl_new_sample4.tex`
- Baseline build command: `latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl_new_sample4.tex`
- Baseline page count: 16
- Baseline references start page: 7
- Baseline compiled bibliography items: 220
- Baseline overfull hbox count: 0
- Baseline underfull hbox count: 83
- Baseline underfull vbox count: 5
- Baseline undefined citations: 0
- Baseline undefined references: 0

The baseline confirms the Pass-1 diagnosis: the manuscript body ends too early, references start on page 7, and `\nocite{*}` forces the full corpus into the main bibliography.

## Final Build Summary

- Final build command: `latexmk -C; latexmk -pdf -interaction=nonstopmode -halt-on-error bare_jrnl_new_sample4.tex`
- Final PDF: `manuscript/comst30_pass2_working/bare_jrnl_new_sample4.pdf`
- Final page count: 27
- References start page: 22
- Bibliography length: approximately 6 pages (pages 22-27)
- Compiled bibliography items: 132
- Main figures: 7
- Main tables: 12
- Numbered equation environments: 3
- Actual `\nocite{*}` commands: 0
- IEEE biography blocks in main source: 0
- IEEE biography blocks preserved in `biographies_moved_for_submission.tex`: 3
- Overfull hbox count: 0
- Underfull hbox count: 99
- Underfull vbox count: 8
- Undefined citations: 0
- Undefined references: 0
- LaTeX warning lines after final converged build: 0
- BibTeX warning lines: 0

The final build is inside the requested 27-29 page target and stays below the 30-page ceiling. The source compiles cleanly with no undefined citations or references. Remaining underfull warnings are concentrated in narrow IEEE table cells and a few dense paragraphs; they do not block the build.

## Page Budget Achieved

| Section | Source line start | Approx. body words | Approx. achieved role |
|---|---:|---:|---|
| Title/Abstract/Introduction | 1 / 45 | 1911 intro words | Re-expanded motivation, optical-vs-RF distinction, related-survey gap, and five contributions. |
| Background + Metric Contract | 136 | 1725 | Re-expanded metric-governance explanation while keeping only compact core math. |
| PRISMA/TQAF Methodology | 236 | 1866 | Re-expanded credibility, database/search blocks, eligibility, extraction, and corpus-ledger policy. |
| Taxonomy | 354 | 2354 | Re-expanded medium, integration, detection, task axes and modality paragraphs. |
| Trade-off Synthesis | 472 | 2619 | Strongest re-expansion; preserves governed attrition and sparse CRQ-valid subset. |
| Enablers | 581 | 1816 | Re-expanded ORIS/OPA/PIC/photonics-assisted high-frequency generation/ML-security synthesis. |
| Applications | 683 | 738 | Kept compact as five deployment motifs to protect page budget. |
| Roadmap | 730 | 1023 | Kept as COMST-style roadmap with one figure, challenge table, and agenda table. |
| Conclusion | 814 | 165 | Kept compact. |
| References | 821 | 132 bibitems | Representative/load-bearing references only; full corpus remains in ledger/supplement. |

## Restored or Re-Expanded Blocks

- Introduction: restored a fuller 6G/O-ISAC motivation, optical-vs-RF distinction, fragmentation argument, related-survey gap, and contribution structure.
- Background: re-expanded coherent vs IM/DD observability, guided/wireless/photonic-THz split, OSNR/SNR plane distinction, fiber `\Delta z` versus wireless `\Delta r_{\min}`, CRB/FIM interpretation, and CRQ admissibility.
- Methodology: re-expanded PRISMA 2020 / PRISMA-S, OSF registration, database/search logic, eligibility rationale, TQAF scoring, extraction schema, and corpus-ledger traceability.
- Taxonomy: re-expanded the four-axis taxonomy and modality paragraphs for fiber, FSO, VLC/LiFi, and photonic-THz/hybrid evidence.
- Section V: re-expanded the governed trade-off synthesis while preserving 225 scenario points, 20 rate + `\Delta r_{\min}`, 16 rate + `\sigma_r`/RMSE, 13 full triplet, and sparse illustrative CRQ subset.
- Enablers: re-expanded ORIS/optical RIS, OPA, PIC/photonic integration, photonics-assisted mmWave/THz generation, ML/security-aware adaptation, and benchmark/reporting implications.
- Applications and roadmap: lightly re-expanded enough to preserve deployment motifs and roadmap logic without reintroducing the original audit layer.

## Blocks Still Kept Out of Main Text

- Full notation and acronym tables.
- Full RF-ISAC vs O-ISAC comparison table.
- Duplicate original optical-advantage and taxonomy figures removed in Pass 1.
- Duplicate metric figure, secondary taxonomy figure, secondary trade-off/CRQ figure, secondary enabler figure, and application figure.
- Large taxonomy contract and medium/integration/detection/cluster tables.
- Full 15-row application table and dual-view consistency layer.
- Long cross-section audit tables.
- Roadmap utility/governance optimization equations.
- Full biography section, preserved separately for possible production-stage restoration.

## Reference Architecture

- `\nocite{*}` was removed from the active source.
- `references.bib` still retains the full bibliography pool for traceability.
- The compiled main bibliography now contains 132 actually cited items, within the requested ideal range of 100-140.
- The methodology section now states that the complete 220-study included-corpus ledger, extraction sheet, and supplementary evidence records are provided in the public repository / Zenodo package.
- `reference_policy_pass2.md` documents the rule: representative and load-bearing studies in the main text; audit-tail/component-only records remain in the corpus ledger and supplement.

## Scientific-Risk Check

- PRISMA `N=220` is preserved.
- The 225/20/16/13 governed-subset result is preserved.
- `\Delta r_{\min}`, `\sigma_r`/RMSE, CRB/FIM, `\Delta z`, and OSNR/SNR/ESNR measurement-plane distinctions are preserved.
- CRQ remains admissible only for matched scenario records and is described as sparse/illustrative, not as a stable design envelope.
- Applications remain framed as deployment motifs, not a maturity scorecard.
- The roadmap retains reporting contracts, reproducible workflows, benchmarks, scalable hardware, and deployment validation.

## Remaining Risks and Pass-3 Recommendation

- The final manuscript is at the lower edge of the target band (27 pages). It is safe for the 30-page ceiling, but a Pass-3 polish could add a little Section V or taxonomy prose if the author wants a denser COMST narrative.
- Underfull table warnings remain, mainly from narrow columns in compact IEEE tables. A later layout pass should tune column widths and line breaks.
- Some restored prose is intentionally compact and may benefit from a human academic style pass for transitions and paragraph rhythm.
- References start on page 22, which is acceptable for a 27-page draft with a 132-item representative bibliography, but the body should be checked visually before submission if COMST formatting or author metadata changes.
