# O-ISAC COMST Compression Repository Audit

## 0. Executive Summary

- Repository root path: `C:/Users/fdonmez/Documents/githubRepos`
- Git branch: `codex/finalize-manuscript-updates`
- Git commit: `6660072`
- Working tree: clean (`git status --short` returned no output)
- Likely primary manuscript source: `manuscript_submission/bare_jrnl_new_sample4.tex`
- Identical active source copy: `manuscript/finalShortened/bare_jrnl_new_sample4.tex` has the same SHA-256 as the submission `.tex`
- Likely compiled PDF: `manuscript_submission/bare_jrnl_new_sample4.pdf` at 44 pages; same page count as `manuscript/finalShortened/bare_jrnl_new_sample4.pdf`
- Earlier longer compiled PDF: `manuscript/finalManuscript/bare_jrnl_new_sample4.pdf` at 50 pages
- Likely bibliography files: `manuscript_submission/references.bib`, `manuscript/finalShortened/references.bib`
- Likely figure directory: `manuscript_submission/figures/`
- Likely data/supplementary directories: `manuscript/finalShortened/prisma_evidence_pack/`, `manuscript/finalShortened/O-ISAC_Supplementary_Material/`, `screening/`, `search/`, `data/ext_res_v4/`, `analysis/V_ev_v2/`, `analysis/IV_ev_v2/`, `analysis/II_ev_v3/`
- Sufficiency for 44 -> 30 page compression pass: yes. The repo contains the 44-page IEEE source/PDF, bibliography, all included figures, build logs, PRISMA/TQAF/protocol artifacts, 220-study corpus ledgers, and scripts/data for taxonomy and trade-off plots.

## 1. Top-Level Repository Tree

```text
.
├── analysis/                         # extraction, evidence synthesis, section-specific notebooks/scripts
│   ├── II_ev_v3/                     # Section II evidence, metric/channel governance
│   ├── IV_ev_v2/                     # taxonomy evidence and figure generation
│   ├── V_ev_v2/                      # trade-off/CRQ/Pareto evidence and figure generation
│   ├── nb/                           # notebooks for PRISMA, extraction, sections 2/4/5/6/7/8
│   └── ...                           # many archived/intermediate evidence folders
├── data/                             # corpus, extraction JSON/CSV, generated/processed paper data
│   ├── ext_res_v4/                   # unified extraction dataset
│   ├── proc_md/                      # large per-study markdown corpus; summarized, not expanded
│   └── corp_std/                     # large standardized corpus; summarized, not expanded
├── docs/                             # workflow and pipeline notes
├── drafts/                           # earlier markdown section drafts
├── legacy_archive/                   # old migration/build snapshots; summarized only
├── manuscript/
│   ├── current_bundle/               # section-split LaTeX preview bundle
│   ├── finalManuscript/              # older 50-page IEEE build
│   └── finalShortened/               # active 44-page shortened source plus supplement packs
├── manuscript_submission/            # final submission-style flat IEEE package
├── memory-bank/                      # project context and writing state
├── protocol/                         # PRISMA/OSF protocol files
├── reference_compendium/             # writing templates and reference notes
├── review_package/                   # bundled manuscript/evidence/audit markdowns
├── screening/                        # PRISMA screening, inclusion/exclusion ledgers
├── scripts/                          # small utility scripts
├── search/                           # search strings, logs, dedup/freeze reconstruction
├── writing_recipes/                  # COMST writing recipes
├── README.md
└── manuscript_submission.zip
```

Excluded/summarized from full expansion: `.git/`, `legacy_archive/`, `data/proc_md/`, `data/proc_md_cprev/`, `data/corp_std/`, caches, and old archived snapshots.

## 2. Manuscript Candidate Files

Search terms used included: `Optical Integrated Sensing and Communication`, `O-ISAC`, `PRISMA`, `TQAF`, `CRQ`, `metric contract`, `Delta r`, `Delta r_min`, `sigma_r`, `Cram`, `Fisher`, `fiber`, `FSO`, `VLC`, `LiFi`, `photonic-THz`, `ORIS`, `OPA`, `COMST`.

| Path | Type | Size | Modified date | Why it may matter |
|---|---:|---:|---|---|
| `manuscript_submission/bare_jrnl_new_sample4.tex` | tex | 249006 | 2026-04-18 16:07:50 | Most likely primary 44-page IEEE source; exact title and all figures/tables/equations inline |
| `manuscript_submission/bare_jrnl_new_sample4.pdf` | pdf | 8039631 | 2026-04-18 16:18:06 | 44-page compiled manuscript matching user context |
| `manuscript_submission/references.bib` | bib | 137423 | 2026-04-18 15:32:16 | Active bibliography; 221 entries, 220 cited |
| `manuscript_submission/IEEEtran.cls` | cls | 288451 | 2026-04-05 23:50:36 | Local IEEE class used by submission build |
| `manuscript_submission/bare_jrnl_new_sample4.bbl` | bbl | 94836 | 2026-04-18 16:18:04 | Built reference list; 220 `\bibitem`s |
| `manuscript_submission/bare_jrnl_new_sample4.log` | log | 37298 | 2026-04-18 16:18:06 | Build warnings and overfull/underfull diagnostics |
| `manuscript_submission/bare_jrnl_new_sample4.aux` | aux | 47156 | 2026-04-18 16:18:06 | Citation/ref state; 220 citation keys |
| `manuscript_submission/bare_jrnl_new_sample4.fls` | fls | 17130 | 2026-04-18 16:18:06 | Exact build input/output dependency trace |
| `manuscript/finalShortened/bare_jrnl_new_sample4.tex` | tex | 249006 | 2026-04-18 16:07:50 | Same SHA-256 as submission `.tex`; active working source copy |
| `manuscript/finalShortened/bare_jrnl_new_sample4.pdf` | pdf | 8039631 | 2026-04-18 16:07:52 | 44-page active compiled copy |
| `manuscript/finalShortened/references.bib` | bib | 137423 | 2026-04-18 15:32:16 | Same SHA-256 as submission bibliography |
| `manuscript/finalManuscript/bare_jrnl_new_sample4.tex` | tex | 276867 | 2026-04-07 18:55:45 | Older longer manuscript source; useful for diff/compression history |
| `manuscript/finalManuscript/bare_jrnl_new_sample4.pdf` | pdf | 34049603 | 2026-04-07 18:57:05 | 50-page earlier compiled version |
| `manuscript/current_bundle/main.tex` | tex | 1900 | 2026-04-05 23:50:37 | Section-split preview driver using `\input{section*.tex}` |
| `manuscript/current_bundle/section1.tex` | tex | 41495 | 2026-04-05 23:50:37 | Split Introduction source |
| `manuscript/current_bundle/section2.tex` | tex | 26539 | 2026-04-05 23:50:37 | Split Technical Fundamentals source |
| `manuscript/current_bundle/section3.tex` | tex | 10750 | 2026-04-05 23:50:37 | Split PRISMA methodology source |
| `manuscript/current_bundle/section4.tex` | tex | 47678 | 2026-04-05 23:50:37 | Split taxonomy source |
| `manuscript/current_bundle/section5.tex` | tex | 35087 | 2026-04-05 23:50:37 | Split trade-off synthesis source |
| `manuscript/current_bundle/section6.tex` | tex | 26695 | 2026-04-05 23:50:37 | Split enablers source |
| `manuscript/current_bundle/section7.tex` | tex | 20552 | 2026-04-05 23:50:37 | Split applications source |
| `manuscript/current_bundle/section8.tex` | tex | 55321 | 2026-04-05 23:50:37 | Split challenges/roadmap source |
| `manuscript/current_bundle/section9.tex` | tex | 3282 | 2026-04-05 23:50:37 | Split conclusion source |
| `manuscript/current_bundle/references.bib` | bib | 138291 | 2026-04-05 23:50:37 | Earlier bibliography; 224 entries |
| `manuscript/current_bundle/included_studies_appendix.tex` | tex | 44748 | 2026-04-05 23:50:37 | Long included-studies appendix/supplement material |
| `protocol/prisma_proto.md` | md | 87903 | 2026-04-05 23:50:37 | PRISMA/OSF protocol |
| `protocol/osf_reg_pack.md` | md | 16022 | 2026-04-05 23:50:37 | OSF registration/support pack |
| `screening/canonical_included_corpus_ledger.csv` | csv | 98275 | 2026-04-05 23:50:38 | 220-study canonical ledger |
| `review_package/01_manuscript_bundle.md` | md | 282050 | 2026-04-05 23:50:37 | Markdown manuscript bundle |
| `review_package/04_evidence_audit_bundle.md` | md | 213039 | 2026-04-05 23:50:37 | Evidence/audit bundle |
| `manuscript/finalShortened/prisma_evidence_pack/MANIFEST.csv` | csv | 4132 | 2026-04-10 16:54:49 | Supplement/evidence pack manifest |

Most likely primary manuscript source: `manuscript_submission/bare_jrnl_new_sample4.tex`, because it is the flat IEEEtran source packaged with `IEEEtran.cls`, `references.bib`, figures, `.aux/.bbl/.fls/.log`, and the 44-page PDF matching the current draft.

## 3. LaTeX Build and Dependency Tree

- Main `.tex` file: `manuscript_submission/bare_jrnl_new_sample4.tex`
- Document class: `\documentclass[letterpaper,journal]{IEEEtran}`
- Packages used:
  - `amsmath`, `amsfonts`
  - `algorithmic`, `algorithm`
  - `array`
  - `subfig` with `caption=false,font=normalsize,labelfont=sf,textfont=sf`
  - `textcomp`
  - `stfloats`
  - `url`
  - `verbatim`
  - `graphicx`
  - `cite`
  - `tabularx`
  - `booktabs`
- `\input` / `\include`: none in `manuscript_submission/bare_jrnl_new_sample4.tex`
- Bibliography:
  - `\bibliographystyle{IEEEtran}`
  - `\bibliography{IEEEabrv, references}`
  - Repo contains `manuscript_submission/references.bib`
  - Repo does not contain `IEEEabrv.bib` or `IEEEtran.bst`; build likely resolves them from local TeX installation.
- `\graphicspath`: none found; all graphics use explicit relative paths such as `figures/fig1.jpg`.
- Build inferred from artifacts/logs: pdfTeX/latexmk-style flow with BibTeX. `bare_jrnl_new_sample4.fdb_latexmk` and `.fls` exist; PDF producer is `pdfTeX-1.40.29`.

ASCII dependency tree:

```text
manuscript_submission/bare_jrnl_new_sample4.tex
├── manuscript_submission/IEEEtran.cls
├── manuscript_submission/references.bib
├── TeX distribution dependency: IEEEabrv.bib
├── TeX distribution dependency: IEEEtran.bst
├── manuscript_submission/figures/fig1.jpg
├── manuscript_submission/figures/fig2.jpg
├── manuscript_submission/figures/fig3.jpg
├── manuscript_submission/figures/fig_ii_1.png
├── manuscript_submission/figures/fig_ii_2.jpg
├── manuscript_submission/figures/fig_iv_1.jpg
├── manuscript_submission/figures/fig_iv_2.jpg
├── manuscript_submission/figures/fig_v_1.png
├── manuscript_submission/figures/fig_v_2.png
├── manuscript_submission/figures/fig_vi_1.jpg
├── manuscript_submission/figures/fig_vi_2.jpg
├── manuscript_submission/figures/fig_vii_1.jpg
├── manuscript_submission/figures/fig_viii_1.jpg
├── manuscript_submission/figures/foto_fatih.jpg
├── manuscript_submission/figures/foto_ahmet.jpg
└── manuscript_submission/figures/foto_mustafa.jpg
```

Section-split preview dependency tree:

```text
manuscript/current_bundle/main.tex
├── manuscript/current_bundle/section1.tex
├── manuscript/current_bundle/section2.tex
├── manuscript/current_bundle/section3.tex
├── manuscript/current_bundle/section4.tex
├── manuscript/current_bundle/section5.tex
├── manuscript/current_bundle/section6.tex
├── manuscript/current_bundle/section7.tex
├── manuscript/current_bundle/section8.tex
├── manuscript/current_bundle/section9.tex
├── manuscript/current_bundle/included_studies_appendix.tex
└── manuscript/current_bundle/references.bib
```

## 4. Section Hierarchy with Source Locations

Source file for the active 44-page manuscript: `manuscript_submission/bare_jrnl_new_sample4.tex`.

| Section no. | Heading | Source file | Line range | Approx. role | Compression priority |
|---|---|---|---:|---|---|
| I | Introduction | `manuscript_submission/bare_jrnl_new_sample4.tex` | 43-358 | Motivation, related surveys, optical opportunity, taxonomy preview | COMPRESS |
| I-A | The Convergence of Sensing and Communication: A 6G Imperative | same | 43-142 | 6G/RF motivation and survey comparison | COMPRESS |
| I-B | The Optical Opportunity: A Vast and Untapped Frontier | same | 143-244 | RF vs O-ISAC contrast and optical advantages | COMPRESS |
| I-C | Unified O-ISAC Taxonomy | same | 245-265 | Preview taxonomy | MERGE |
| I-D | The Fragmentation Challenge: A Landscape Without Unity | same | 266-358 | Problem framing and contributions | COMPRESS |
| II | TECHNICAL FUNDAMENTALS OF O-ISAC | same | 359-739 | System/channel/hardware/metric fundamentals | COMPRESS |
| II-A | Unified O-ISAC System Model and Integration Paradigms | same | 360-431 | Canonical model and integration patterns | COMPRESS |
| II-B | Propagation and Channel Models Across Modalities | same | 432-493 | Fiber/FSO/VLC/photo-THz channel models | COMPRESS |
| II-C | Transceiver and Hardware Abstractions | same | 494-589 | Sources, receivers, beam/wavefront controls | COMPRESS |
| II-D | Accuracy and CRB/FIM Bounds | same | 590-607 | Metric governance foundation | KEEP CORE |
| II-E | Fiber Spatial Granularity vs Wireless Range Resolution | same | 608-614 | Δz vs Δr_min distinction | KEEP CORE |
| II-F | Capacity-Resolution Quotient | same | 615-716 | CRQ definition and admissibility | KEEP CORE |
| II-G | ISAC Coupling and Trade-off Foundations | same | 717-739 | Optimization bridge to Section V | COMPRESS |
| III | REVIEW METHODOLOGY (PRISMA 2020) | same | 740-867 | Protocol, search, eligibility, TQAF | COMPRESS |
| III-A | Protocol and Registration | same | 743-747 | OSF/registration credibility | COMPRESS |
| III-B | Information Sources and Search Strategy | same | 748-761 | Search sources and freeze | COMPRESS |
| III-C | Eligibility Criteria | same | 762-813 | Inclusion/exclusion table | KEEP CORE |
| III-D | Study Selection and PRISMA Flow | same | 814-849 | PRISMA counts and flow figure | KEEP CORE |
| III-E | Data Extraction and Taxonomical Classification | same | 850-852 | Extraction protocol | COMPRESS |
| III-F | Quality Appraisal (TQAF) | same | 853-864 | TQAF credibility | KEEP CORE |
| III-G | Data Synthesis Strategy | same | 865-867 | Synthesis method | COMPRESS |
| IV | UNIFIED O-ISAC TAXONOMY | same | 868-1309 | Cross-modality taxonomy | KEEP CORE |
| IV-A | Taxonomy Design Principles | same | 872-963 | Taxonomy vector and mapping rules | KEEP CORE |
| IV-B | Medium-Based Classes | same | 964-1054 | Fiber/FSO/VLC/photo-THz/hybrid classes | KEEP CORE |
| IV-C | Integration Mechanisms | same | 1055-1113 | Shared waveform/hardware/resources/processing | MERGE |
| IV-D | Signal Dimension and Detection | same | 1131-1208 | IM/DD/coherent/observability/metric implications | KEEP CORE |
| IV-E | Taxonomy Summary Views | same | 1209-1309 | Taxonomy figure/table | MERGE |
| V | COMMUNICATION-SENSING TRADEOFF SYNTHESIS | same | 1310-1514 | Governed metric/trade-off synthesis | KEEP CORE |
| V-A | Communication Metrics | same | 1314-1359 | Communication metric coverage | KEEP CORE |
| V-B | Sensing Metrics | same | 1360-1417 | Sensing metric coverage | KEEP CORE |
| V-C | Sensing-Communication Trade-off | same | 1418-1442 | Rate-resolution and sparse governed subset | KEEP CORE |
| V-D | Comparative Analysis: Fiber vs Wireless | same | 1443-1508 | Cross-modality slices | KEEP CORE |
| V-E | Section V closeout synthesis | same | 1509-1514 | Section synthesis | COMPRESS |
| VI | ENABLING TECHNOLOGIES AND SYSTEM-LEVEL CO-DESIGN FOR OPTICAL ISAC | same | 1515-1811 | ORIS/OPA/ML/photonic generation/enablers | COMPRESS |
| VI-A | Programmable Optical Enablers | same | 1578-1651 | OPA/ORIS landscape | MERGE |
| VI-B | Channel Impairments and Robustness | same | 1652-1669 | Robustness constraints | COMPRESS |
| VI-C | Joint Co-Design and Resource Optimization | same | 1670-1691 | Optimization math | COMPRESS |
| VI-D | Experimental Validation, Benchmarking, and Reporting Contract | same | 1692-1760 | Reporting contract | KEEP CORE |
| VI-E | Networked and Multi-User O-ISAC | same | 1761-1782 | Multi-user systems | COMPRESS |
| VI-F | AI/ML and Security-Aware Adaptation | same | 1783-1806 | ML/security | COMPRESS |
| VI-G | Synthesis and Transition | same | 1807-1811 | Transition | COMPRESS |
| VII | APPLICATIONS AND USE CASES ACROSS DOMAINS | same | 1812-2120 | Application portfolio/transfer map | COMPRESS |
| VII-A | Smart Infrastructure & Outdoor Urban Sensing-Communication | same | 1923-1947 | Outdoor use cases | COMPRESS |
| VII-B | Indoor Environments | same | 1948-1963 | Indoor/VLC use cases | COMPRESS |
| VII-C | Automotive Transportation | same | 1964-1986 | Vehicular use cases | COMPRESS |
| VII-D | Underwater and Harsh-Environment OWC | same | 1987-2006 | Harsh environment use cases | COMPRESS |
| VII-E | Space and Satellite Networks | same | 2007-2027 | Space/satellite use cases | COMPRESS |
| VII-F | Cross-Domain Application Synthesis | same | 2028-2058 | Transfer synthesis | MERGE |
| VII-G | Dual-View Consistency Layer | same | 2059-2120 | Audit/consistency layer | MOVE TO SUPPLEMENT |
| VIII | OPEN CHALLENGES AND RESEARCH ROADMAP | same | 2121-2557 | Challenges and roadmap | COMPRESS |
| VIII-A | Standardization and Interoperability Challenges | same | 2136-2175 | Standards/interoperability | COMPRESS |
| VIII-B | Hardware Scalability and Efficiency Challenges | same | 2176-2212 | Hardware constraints | COMPRESS |
| VIII-C | Channel Modeling and Evaluation Challenges | same | 2213-2248 | Evaluation model challenges | COMPRESS |
| VIII-D | Security, Privacy, and Reliability Challenges | same | 2249-2283 | Security/reliability | COMPRESS |
| VIII-E | Deployment Convergence and Roadmap Challenges | same | 2284-2322 | Deployment roadmap | COMPRESS |
| VIII-F | Capstone Dependency Synthesis and Prioritized Research Agenda | same | 2323-2462 | Agenda tables | MERGE |
| VIII-G | Cross-Section Alignment and Evidence-Consistency Check | same | 2463-2557 | Audit tables | MOVE TO SUPPLEMENT |
| IX | CONCLUSIONS | same | 2558-2592 | Closing summary | COMPRESS |

## 5. Figure Inventory and Graphics Tree

| Fig label | Caption short name | Source file | Line no. | Graphics path | File exists? | Page/section likely | Compression action |
|---|---|---|---:|---|---|---|---|
| `fig:fig1` | Evolution of O-ISAC | `manuscript_submission/bare_jrnl_new_sample4.tex` | 56 | `figures/fig1.jpg` | yes | Introduction | MERGE WITH ANOTHER FIGURE |
| `fig:fig2` | Physical basis of optical advantages | same | 214 | `figures/fig2.jpg` | yes | Introduction | REMOVE CANDIDATE |
| `fig:fig3` | Preview of four modality families | same | 236 | `figures/fig3.jpg` | yes | Introduction | MERGE WITH ANOTHER FIGURE |
| `fig:fig_ii_1` | Unified O-ISAC system abstraction | same | 425 | `figures/fig_ii_1.png` | yes | Section II | SHRINK |
| `fig:fig_ii_2` | Metric contract and comparison map | same | 710 | `figures/fig_ii_2.jpg` | yes | Section II | KEEP |
| `fig:fig_iii_1` | PRISMA 2020 flow diagram | same | 827 | in-source LaTeX/TikZ-like figure, no external graphic | n/a | Section III | KEEP |
| `fig:fig_iv_1` | Semantic taxonomy map | same | 1214 | `figures/fig_iv_1.jpg` | yes | Section IV | KEEP |
| `fig:fig_iv_2` | Medium-task specialization view | same | 1303 | `figures/fig_iv_2.jpg` | yes | Section IV | MERGE WITH ANOTHER FIGURE |
| `fig:fig_v_1` | Governed operating clouds | same | 1421 | `figures/fig_v_1.png` | yes | Section V | KEEP |
| `fig:fig_v_2` | Sparse CRQ-valid frontier | same | 1432 | `figures/fig_v_2.png` | yes | Section V | KEEP |
| `fig:fig_vi_1` | Enabler landscape | same | 1642 | `figures/fig_vi_1.jpg` | yes | Section VI | MERGE WITH ANOTHER FIGURE |
| `fig:fig_vi_2` | Enablers to deployment-ready O-ISAC | same | 1751 | `figures/fig_vi_2.jpg` | yes | Section VI | MERGE WITH ANOTHER FIGURE |
| `fig:fig_vii_1` | Cross-domain deployment synthesis | same | 1911 | `figures/fig_vii_1.jpg` | yes | Section VII | SHRINK |
| `fig:fig_viii_1` | Challenge-to-roadmap dependency map | same | 2127 | `figures/fig_viii_1.jpg` | yes | Section VIII | KEEP |

Graphics directory tree:

```text
manuscript_submission/figures/
├── fig1.jpg
├── fig2.jpg
├── fig3.jpg
├── fig_ii_1.png
├── fig_ii_2.jpg
├── fig_iv_1.jpg
├── fig_iv_2.jpg
├── fig_v_1.png
├── fig_v_2.png
├── fig_vi_1.jpg
├── fig_vi_2.jpg
├── fig_vii_1.jpg
├── fig_viii_1.jpg
├── foto_ahmet.jpg
├── foto_fatih.jpg
└── foto_mustafa.jpg
```

| Path | Size | Dimensions | Used in TeX? | Notes |
|---|---:|---:|---|---|
| `manuscript_submission/figures/fig1.jpg` | 1246771 | 2816x1359 | yes | Intro evolution figure |
| `manuscript_submission/figures/fig2.jpg` | 1296457 | 2816x1444 | yes | Intro optical-advantage figure; likely redundant with Fig. 1/3 |
| `manuscript_submission/figures/fig3.jpg` | 1226285 | 2816x1374 | yes | Intro taxonomy preview |
| `manuscript_submission/figures/fig_ii_1.png` | 195905 | 1893x738 | yes | System abstraction |
| `manuscript_submission/figures/fig_ii_2.jpg` | 310435 | 1598x784 | yes | Metric contract |
| `manuscript_submission/figures/fig_iv_1.jpg` | 657613 | 2752x1536 | yes | Taxonomy map |
| `manuscript_submission/figures/fig_iv_2.jpg` | 801768 | 2816x1536 | yes | Medium-task specialization |
| `manuscript_submission/figures/fig_v_1.png` | 368492 | 4154x1619 | yes | Rate vs metric governed clouds |
| `manuscript_submission/figures/fig_v_2.png` | 225711 | 3118x1560 | yes | Sparse CRQ frontier |
| `manuscript_submission/figures/fig_vi_1.jpg` | 134374 | 1408x585 | yes | Enabler landscape |
| `manuscript_submission/figures/fig_vi_2.jpg` | 203650 | 1408x677 | yes | Deployment chain |
| `manuscript_submission/figures/fig_vii_1.jpg` | 251369 | 1408x650 | yes | Application map |
| `manuscript_submission/figures/fig_viii_1.jpg` | 216489 | 1408x638 | yes | Roadmap/challenge map |
| `manuscript_submission/figures/foto_ahmet.jpg` | 209139 | 1074x1309 | yes | IEEE biography photo |
| `manuscript_submission/figures/foto_fatih.jpg` | 154988 | 1052x1024 | yes | IEEE biography photo |
| `manuscript_submission/figures/foto_mustafa.jpg` | 147727 | 329x405 | yes | IEEE biography photo |

Likely redundant visual pairs:

- Landscape/evolution figures: `fig1.jpg`, `fig2.jpg`, `fig3.jpg`
- Modality taxonomy preview vs taxonomy figure: `fig3.jpg`, `fig_iv_1.jpg`
- Metric contract table vs metric contract figure: `fig_ii_2.jpg`, `tab:ii2`
- Enabler landscape vs deployment chain: `fig_vi_1.jpg`, `fig_vi_2.jpg`
- Application map vs application table: `fig_vii_1.jpg`, `tab:section7_portfolio`
- Challenge roadmap vs audit tables: `fig_viii_1.jpg`, `tab:viii_f_1`, `tab:viii_f_2`, `tab:viii_g_1`, `tab:viii_g_2`

## 6. Table Inventory

| Table label | Caption short name | Source file | Line range | Approx. size | Compression action |
|---|---|---|---:|---|---|
| `tab:axis_comparison` | Related survey comparison | `manuscript_submission/bare_jrnl_new_sample4.tex` | 67-137 | rows~15, lines 71 | SHRINK |
| `tab:performance_comparison` | RF-ISAC vs O-ISAC comparison | same | 145-208 | rows~8, lines 64 | REMOVE CANDIDATE |
| `tab:math_notation` | Mathematical notation conventions | same | 292-312 | rows~10, lines 21 | MOVE TO SUPPLEMENT |
| `tab:acronyms` | Frequently used acronyms | same | 314-355 | rows~31, lines 42 | MOVE TO SUPPLEMENT |
| `tab:ii1` | Channel and transceiver abstraction | same | 534-578 | rows~9, lines 45 | SHRINK |
| `tab:ii2` | Metric contract and comparability guard | same | 628-706 | rows~11, lines 79 | KEEP CORE |
| `tab:iii1` | Eligibility criteria | same | 782-811 | rows~5, lines 30 | KEEP CORE |
| `tab:taxonomy_contract` | Operational contract for taxonomy synthesis | same | 899-958 | rows~10, lines 60 | KEEP CORE |
| `tab:medium_classes` | Medium-based taxonomy classes | same | 969-1034 | rows~11, lines 66 | MERGE |
| `tab:integration_mechanisms` | Integration mechanisms | same | 1059-1110 | rows~6, lines 52 | MERGE |
| `tab:detection_observability` | Detection and observability classes | same | 1135-1186 | rows~9, lines 52 | MERGE |
| `tab:taxonomy_clusters` | Taxonomy summary views | same | 1226-1298 | rows~18, lines 73 | MERGE |
| `tab:comm_metrics` | Communication metric coverage | same | 1317-1356 | rows~5, lines 40 | KEEP CORE |
| `tab:sensing_metrics` | Sensing metric coverage | same | 1364-1409 | rows~6, lines 46 | KEEP CORE |
| `tab:comparative_slices` | Governed fiber/wireless/hybrid slices | same | 1447-1496 | rows~6, lines 50 | KEEP CORE |
| `tab:section6_notation` | Unified notation for Section VI | same | 1524-1557 | rows~23, lines 34 | MOVE TO SUPPLEMENT |
| `tab:vi_a_enablers` | Programmable optical enabler families | same | 1595-1634 | rows~5, lines 40 | SHRINK |
| `tab:vi_d_reporting` | Reproducible reporting fields | same | 1712-1746 | rows~7, lines 35 | KEEP CORE |
| `tab:section7_portfolio` | Application portfolio matrix | same | 1816-1909 | rows~15, lines 94 | SHRINK |
| `tab:section7_dualview` | Dual-view discrepancy summary | same | 2062-2114 | rows~7, lines 53 | MOVE TO SUPPLEMENT |
| `tab:viii_f_1` | Dependency coverage summary | same | 2326-2361 | rows~9, lines 36 | MERGE |
| `tab:viii_f_2` | Prioritized research agenda | same | 2366-2447 | rows~9, lines 82 | SHRINK |
| `tab:viii_g_1` | Cross-section alignment summary | same | 2470-2511 | rows~9, lines 42 | MOVE TO SUPPLEMENT |
| `tab:viii_g_2` | Paper-level discrepancy examples availability | same | 2517-2554 | rows~7, lines 38 | MOVE TO SUPPLEMENT |

Specifically identified table classes:

- Related survey comparison: `tab:axis_comparison`
- RF-ISAC vs O-ISAC comparison: `tab:performance_comparison`
- Notation/acronyms: `tab:math_notation`, `tab:acronyms`, `tab:section6_notation`
- Eligibility criteria: `tab:iii1`
- Metric contract/reporting contract: `tab:ii2`, `tab:vi_d_reporting`
- Taxonomy operational contract: `tab:taxonomy_contract`
- Medium taxonomy: `tab:medium_classes`
- Integration mechanisms: `tab:integration_mechanisms`
- Detection/observability: `tab:detection_observability`
- Metric coverage/sensing coverage: `tab:comm_metrics`, `tab:sensing_metrics`, `tab:comparative_slices`
- Enabler table: `tab:vi_a_enablers`
- Application map/table: `tab:section7_portfolio`, `tab:section7_dualview`
- Challenge/audit/roadmap tables: `tab:viii_f_1`, `tab:viii_f_2`, `tab:viii_g_1`, `tab:viii_g_2`

## 7. Equation and Math Object Inventory

Detected 56 `equation` environments in `manuscript_submission/bare_jrnl_new_sample4.tex`.

| Eq no./label | Source file | Line range | Short purpose | Compression action |
|---|---|---:|---|---|
| unlabeled | `manuscript_submission/bare_jrnl_new_sample4.tex` | 252-254 | `\Delta r_{\min}=v/(2B_eff)` intro preview | KEEP NUMBERED |
| unlabeled | same | 366-368 | canonical observation model `y(t)=H(t;theta)s(t)+w(t)` | INLINE |
| unlabeled | same | 372-374 | IM/DD observation model | INLINE |
| `eq:measurement_plane_contract` | same | 379-385 | OSNR/SNR plane contract | KEEP NUMBERED |
| unlabeled | same | 415-417 | integration-depth variable | INLINE |
| `eq:fiber_linear_model` | same | 439-442 | fiber linear channel | INLINE |
| `eq:nlse_conceptual` | same | 446-457 | conceptual NLSE | MOVE TO SUPPLEMENT |
| unlabeled | same | 466-472 | FSO attenuation/pointing model | INLINE |
| unlabeled | same | 481-483 | VLC LoS/NLoS impulse response | INLINE |
| `eq:receiver_plane_contract` | same | 506-512 | receiver-plane contract | KEEP NUMBERED |
| unlabeled | same | 522-527 | OPA steering vector | INLINE |
| unlabeled | same | 583-585 | bandwidth-limited range resolution | KEEP NUMBERED |
| unlabeled | same | 594-596 | RMSE/accuracy definition | KEEP NUMBERED |
| unlabeled | same | 598-603 | CRB/FIM-style variance bound | KEEP NUMBERED |
| unlabeled | same | 619-621 | `CRQ_\Delta = R / \Delta r_min` | KEEP NUMBERED |
| unlabeled | same | 879-881 | taxonomy vector `T(p)` | KEEP NUMBERED |
| unlabeled | same | 889-894 | taxonomy metric-plane mapping | KEEP NUMBERED |
| unlabeled | same | 1197-1206 | plane mapping and `\Delta r_min != sigma_r` | KEEP NUMBERED |
| unlabeled | same | 1565-1573 | ORIS/RIS channel and phase matrix | INLINE |
| unlabeled | same | 1583-1588 | OPA array factor and steering phase | INLINE |
| unlabeled | same | 1657-1662 | impairment/outage model | INLINE |
| unlabeled | same | 1675-1686 | enabler multiobjective optimization | MOVE TO SUPPLEMENT |
| unlabeled | same | 1697-1708 | reporting state/metric tuple | INLINE |
| unlabeled | same | 1766-1777 | multi-user resource optimization | MOVE TO SUPPLEMENT |
| unlabeled | same | 1788-1799 | secrecy/security-aware optimization | MOVE TO SUPPLEMENT |
| unlabeled | same | 1928-2051 | application-domain optimization blocks | MOVE TO SUPPLEMENT |
| unlabeled | same | 2156-2459 | roadmap/utility/governance optimization blocks | REMOVE CANDIDATE |

Flagged as organizational scaffolding rather than necessary technical contribution: equations at lines `1928-2051`, `2156-2169`, `2196-2206`, `2233-2242`, `2269-2277`, `2304-2316`, and `2452-2459`.

## 8. Bibliography and Citation Tree

- Active bibliography file: `manuscript_submission/references.bib`
- Total `.bib` entries: 221
- Unique `.bib` keys: 221
- Cited keys in active TeX source: 220 unique keys, 666 total citation mentions
- Uncited `.bib` entries: 1
- Likely reference count in compiled manuscript: 220 (`bare_jrnl_new_sample4.bbl` has 220 `\bibitem`s)
- Bibliography style: `IEEEtran`
- Duplicate keys: none
- Missing keys: none
- Citations present in `.aux` but absent from source: none
- Citations present in source but absent from `.aux`: none
- Citations present in `.bbl` but absent from source: none

| Bib file | Entries | Used keys | Unused keys | Notes |
|---|---:|---:|---:|---|
| `manuscript_submission/references.bib` | 221 | 220 | 1 | Active submission bibliography |
| `manuscript/finalShortened/references.bib` | 221 | 220 | 1 | Same SHA-256 as submission bib |
| `manuscript/finalManuscript/references.bib` | 223 | not fully rechecked | n/a | Older 50-page build bibliography |
| `manuscript/current_bundle/references.bib` | 224 | not fully rechecked | n/a | Earlier section-bundle bibliography |
| `data/references.bib` | 222 | not fully rechecked | n/a | Data-side bibliography export |
| `analysis/refs.bib` | 10 | n/a | n/a | Small analysis bibliography |

Unused key:

```text
openai_codex_2026
```

Cited keys grouped by top-level section:

| Section | Line range | Unique cited keys | Notes |
|---|---:|---:|---|
| Introduction | 43-358 | 54 | Survey framing, RF/O-ISAC comparison, modality motivation |
| Technical Fundamentals | 359-739 | 43 | Channel, metric, CRB/FIM, CRQ foundations |
| Review Methodology | 740-867 | 31 | PRISMA inclusion/exclusion references |
| Unified O-ISAC Taxonomy | 868-1309 | 69 | Heaviest citation concentration |
| Communication-Sensing Tradeoff Synthesis | 1310-1514 | 0 | Uses governed tables/figures; no direct `\cite` detected in this section |
| Enabling Technologies | 1515-1811 | 26 | OPA/ORIS/ML/security/enabler evidence |
| Applications | 1812-2120 | 37 | Use-case portfolio evidence |
| Open Challenges and Roadmap | 2121-2557 | 29 | Standards, hardware, channel, security, deployment evidence |
| Conclusions | 2558-2592 | 0 | No direct citations |

Duplicate or suspicious entries:

- No duplicate BibTeX keys detected.
- `openai_codex_2026` is uncited and likely non-core/audit-tail.
- `\bibliography{IEEEabrv, references}` references `IEEEabrv`, but `IEEEabrv.bib` is not in the repo; likely resolved from TeX installation.

Audit-tail references that may be moved to supplementary/corpus ledger:

- The 220-study corpus is fully cited in the manuscript. For a 30-page COMST compression, the full corpus should be retained in `screening/canonical_included_corpus_ledger.csv` and/or `manuscript/finalShortened/prisma_evidence_pack/03_screening_and_inclusion/canonical_included_corpus_ledger.csv`, while the in-manuscript reference list may need representative citation reduction plus supplement/Zenodo ledger.

## 9. PRISMA / TQAF / Dataset / Supplementary Evidence Tree

```text
manuscript/finalShortened/prisma_evidence_pack/
├── 01_protocol/
│   ├── prisma_proto.md
│   └── search_strings.md
├── 02_search_and_flow/
│   ├── dedup_external_overlap_support_20260411.csv
│   ├── dedup_log.csv
│   ├── formal_identification_reconstruction_20251130.csv
│   ├── prisma_flow_counts.csv
│   ├── search_log.csv
│   └── freeze_bundle_reconstructed_20251130/
├── 03_screening_and_inclusion/
│   ├── canonical_included_corpus_ledger.csv
│   ├── included_studies_canonical.csv
│   ├── fulltext_assessed_reconstruction.csv
│   ├── excluded_fulltext_log.csv
│   └── title_abstract_screening_reconstruction.csv
├── 04_audit_notes/
│   ├── 10_prisma_flow_evidence_map.md
│   └── section3_evidence_reconstruction.md
├── 05_appendix/
│   ├── fulltext_exclusions_appendix.tex
│   └── included_studies_appendix.tex
├── 06_external_candidates/
├── DATA_AVAILABILITY_STATEMENT.md
├── MANIFEST.csv
├── METHODS_AND_SUPPLEMENT_SNIPPETS.md
├── OSF_UPLOAD_CHECKLIST.md
└── README.md
```

| Path | Type | Rows/columns if readable | Likely role | Needed for compression? |
|---|---|---:|---|---|
| `screening/canonical_included_corpus_ledger.csv` | csv | 220 x 17 | Canonical 220-study corpus ledger | YES, cite in Methods |
| `screening/included_studies_canonical.csv` | csv | 220 x 10 | Included-study list | YES, move table content here |
| `screening/prisma_flow_counts.csv` | csv | 1 x 8 | PRISMA flow counts | YES, cite in Methods |
| `screening/screening_log.csv` | csv | 441 x 18 | Screening decisions | YES, cite in Methods |
| `screening/fulltext_assessed_reconstruction.csv` | csv | 222 x 11 | Full-text assessment reconstruction | YES, cite in Methods |
| `search/search_log.csv` | csv | 3 x 7 | Search source/date log | YES, cite in Methods |
| `search/search_strings.md` | md | n/a | Search strings | YES, cite in Methods |
| `protocol/prisma_proto.md` | md | n/a | PRISMA/OSF protocol | YES, cite in Methods |
| `protocol/osf_reg_pack.md` | md | n/a | OSF registration support | OPTIONAL |
| `manuscript/finalShortened/prisma_evidence_pack/MANIFEST.csv` | csv | 24 x 5 | Evidence-pack manifest | YES, move table content here |
| `manuscript/finalShortened/O-ISAC_Supplementary_Material/03_Included_Studies/canonical_included_corpus_ledger.csv` | csv | 220 x 17 | Submission supplement ledger | YES, move table content here |
| `data/ext_res_v4/extraction_v4_summary.csv` | csv | 222 x 5 | Unified extraction summary | YES, move table content here |
| `data/ext_res_v4/extraction_v4_unified.json` | json | 221 x 5 | Unified extraction dataset | YES, move table content here |
| `analysis/IV_ev_v2/section4E_summary_table.csv` | csv | 220 x 9 | Taxonomy summary evidence | YES, move table content here |
| `analysis/V_ev_v2/section5C_tradeoff_points.csv` | csv | 226 x 23 | Trade-off / rate-resolution points | YES, cite in Methods |
| `analysis/V_ev_v2/section5E_pareto_points.csv` | csv | 2 x 23 | Sparse governed Pareto/CRQ subset | YES, cite in Methods |

TQAF/quality-appraisal related files detected by content/path include:

- `protocol/prisma_proto.md`
- `manuscript/finalShortened/O-ISAC_Supplementary_Material/01_PRISMA_Checklist/PRISMA_2020_Reporting_Checklist.md`
- `manuscript/finalShortened/kontrol_listeleri/09_prisma_2020_reporting_checklist.md`
- `review_package/02_templates_methodology_bundle.md`
- `review_package/prisma_protocol.md`
- `screening/section3_evidence_reconstruction.md`

## 10. Script / Notebook / Reproducibility Tree

| Path | Purpose inferred | Inputs | Outputs | Used by manuscript? |
|---|---|---|---|---|
| `analysis/nb/generate_prisma_flowchart.py` | PRISMA flow chart generation | `data/status/prisma_metrics.json` | PRISMA flow image/diagram | Likely supports Section III |
| `analysis/nb/PRISMA_Flowchart_Generator.ipynb` | PRISMA flow notebook | `data/status/prisma_metrics.json` | PRISMA flow artifact | Likely supports Section III |
| `analysis/IV_ev_v2/generate_section4_figures.py` | Section IV taxonomy figures | `included_studies_canonical.csv`, `section4E_summary_table.csv` | `fig_iv_1.png`, `fig_iv_2.png` | Yes, figure source lineage |
| `analysis/V_ev_v2/generate_section5_figures.py` | Section V trade-off/CRQ figures | `section5C_tradeoff_points.csv`, `section5E_pareto_points.csv`, `included_studies_canonical.csv` | `fig_v_1.png`, `fig_v_2.png` | Yes, core figures |
| `analysis/nb/Section5_Tradeoff_Evidence_Lab.ipynb` | Section V evidence lab | `extraction_v4_unified.json`, metric governance files | trade-off evidence/tables | Yes, core governed synthesis |
| `analysis/nb/Section5_Tradeoff_Evidence_Lab_local.py` | Local Section V pipeline | `extraction_v4_unified.json`, `variant_cache.json` | Section V evidence summaries | Yes |
| `analysis/nb/Section4_Taxonomy_Evidence_Lab.ipynb` | Taxonomy evidence lab | `extraction_v4_unified.json` | taxonomy mappings/tables | Yes |
| `analysis/nb/Section6_Enablers_Evidence_Lab.ipynb` | Enabler evidence lab | `extraction_v4_unified.json`, taxonomy rules | enabler evidence | Yes |
| `analysis/nb/Section7_Applications_Evidence_Lab.ipynb` | Application evidence lab | `extraction_v4_unified.json` | application portfolio | Yes |
| `analysis/nb/Section8_OpenChallenges_Roadmap_Evidence_Lab.ipynb` | Challenges/roadmap evidence lab | `data/ext_v4_uni.csv` | roadmap evidence | Yes |
| `analysis/nb/section2_v3_pipeline.py` | Section II evidence pipeline | Section II evidence CSVs | metric/channel governance reports | Yes |
| `analysis/II_ev_v2/run_channel_governance.py` | Channel governance | `section2B_evidence.csv` | `II_channel_governance.md` | Yes |
| `screening/validate_section3_freeze.py` | PRISMA freeze validation | screening CSVs, flow counts | anomalies/validation reports | Yes, Methods credibility |
| `screening/query_excluded_studies_folder.py` | Exclusion log query | exclusion/fulltext CSVs | exclusion query reports | Supplement |
| `manuscript/current_bundle/generate_included_studies_appendix.py` | Included studies appendix generation | included studies/scopus candidates | `included_studies_appendix.tex` | Supplement |
| `manuscript/finalShortened/create_submission_zip.ps1` | Submission zip packaging | `.tex`, `references.bib`, figures | submission archive | Build/package only |
| `scripts/generate_bibtex.py` | BibTeX generation | per-study markdown / response JSON | `references.bib`, bib log | Bibliography lineage |
| `generate_screening_log.py` | Screening log generation | Scopus/included lists | `screening_log.csv` | PRISMA support |
| `check_duplicates.py` | Duplicate checking | exports/included lists | duplicate report | PRISMA support |
| `consolidate_studies.py` | Study consolidation | screening candidates/logs | included-study lists | PRISMA support |
| `process_scopus.py` | Scopus processing | Scopus export CSV | candidates/screening entries | Search support |

No `Makefile`, `latexmkrc`, `requirements.txt`, `environment.yml`, `pyproject.toml`, or `package.json` was reported in the focused build/config scan.

## 11. Compiled PDF / Build Artifact Analysis

| Path | Pages | File size | Modified date | Likely source | Notes |
|---|---:|---:|---|---|---|
| `manuscript_submission/bare_jrnl_new_sample4.pdf` | 44 | 8039631 | 2026-04-18 16:18:06 | `manuscript_submission/bare_jrnl_new_sample4.tex` | Current submission package |
| `manuscript/finalShortened/bare_jrnl_new_sample4.pdf` | 44 | 8039631 | 2026-04-18 16:07:52 | `manuscript/finalShortened/bare_jrnl_new_sample4.tex` | Active working copy |
| `manuscript/finalShortened/buildtmp/bare_jrnl_new_sample4.pdf` | 42 | 34011647 | 2026-04-18 15:13:07 | buildtmp copy | Conflicting intermediate page count |
| `manuscript/finalManuscript/bare_jrnl_new_sample4.pdf` | 50 | 34049603 | 2026-04-07 18:57:05 | `manuscript/finalManuscript/bare_jrnl_new_sample4.tex` | Older longer build |
| `manuscript/arch/ieee_photonics_review_staging.pdf` | 55 | 35273269 | 2026-04-05 23:50:37 | archived staging source | Old target/journal staging |
| `manuscript/arch/IEEE-Transactions-LaTeX2e-templates-and-instructions/oisac_review_working.pdf` | 32 | 35365787 | 2026-04-05 23:50:36 | archived working source | Old archive, not active |
| `manuscript/finalShortened/cover_letter.pdf` | 1 | 103100 | 2026-04-18 16:43:17 | `cover_letter.tex` | Submission cover letter, not manuscript |

PDF text first page confirms the active title:
`Optical Integrated Sensing and Communication: A Systematic Review of Fiber, Free-Space, VLC/LiFi, and Photonic-THz Platforms`.

Log analysis:

| Log | Overfull hboxes | Underfull boxes | Undefined citations | Undefined references | Float warnings |
|---|---:|---:|---:|---:|---:|
| `manuscript_submission/bare_jrnl_new_sample4.log` | 20 | 87 | 0 | 0 | 0 |
| `manuscript/finalShortened/bare_jrnl_new_sample4.log` | 20 | 87 | 0 | 0 | 0 |
| `manuscript/finalManuscript/bare_jrnl_new_sample4.log` | 24 | 155 | 0 | 0 | 0 |

Overfull lines in the active build concentrate around source lines:

- `705` near `tab:ii2` metric contract
- `1185` near detection/observability table
- `1297` near taxonomy summary table
- `1355`, `1408`, `1495` near Section V metric/comparative tables
- `1908` near application portfolio table
- `2179-2180` near hardware scalability prose/table area

Large floats likely contributing to page inflation:

- `tab:axis_comparison` lines 67-137
- `tab:performance_comparison` lines 145-208
- `tab:ii2` lines 628-706
- `tab:taxonomy_clusters` lines 1226-1298
- `tab:section7_portfolio` lines 1816-1909
- `tab:viii_f_2` lines 2366-2447

## 12. Compression Readiness Matrix

| Compression target | Source paths involved | Figures/tables involved | Data files involved | Risk level | Notes |
|---|---|---|---|---|---|
| 1. Merge Fig. 1 + Fig. 3 / remove Fig. 2 if present. | `manuscript_submission/bare_jrnl_new_sample4.tex` lines 56, 214, 236 | `fig:fig1`, `fig:fig2`, `fig:fig3` | none | LOW | Intro has three conceptual visuals before core methods/taxonomy. |
| 2. Move notation/acronym tables to supplement. | same lines 292-355; supplement paths under `manuscript/finalShortened/O-ISAC_Supplementary_Material/` | `tab:math_notation`, `tab:acronyms`, `tab:section6_notation` | supplement manifest | LOW | Clear supplement candidates. |
| 3. Compress Technical Fundamentals from ~6 pages to ~3 pages. | same lines 359-739; `manuscript/current_bundle/section2.tex` | `fig_ii_1`, `fig_ii_2`, `tab:ii1`, `tab:ii2` | `analysis/II_ev_v3/*`, `analysis/II_ev_v2/*` | MEDIUM | Protect metric-governance core while shrinking channel/hardware review. |
| 4. Keep Metric Contract but remove duplicate metric figure/table redundancy. | same lines 590-716 | `fig:fig_ii_2`, `tab:ii2` | `analysis/II_ev_v3/contract_violations.csv`, `analysis/II_ev_v3/section2D_evidence_v3.csv` | MEDIUM | Keep one authoritative contract; avoid duplicate explanations. |
| 5. Merge taxonomy tables and keep one taxonomy figure. | same lines 868-1309 | `fig_iv_1`, `fig_iv_2`, `tab:taxonomy_contract`, `tab:medium_classes`, `tab:integration_mechanisms`, `tab:detection_observability`, `tab:taxonomy_clusters` | `analysis/IV_ev_v2/section4E_summary_table.csv` | MEDIUM | Core taxonomy must survive; tables are merge-heavy. |
| 6. Preserve Section V governed trade-off result. | same lines 1310-1514 | `fig_v_1`, `fig_v_2`, `tab:comm_metrics`, `tab:sensing_metrics`, `tab:comparative_slices` | `analysis/V_ev_v2/section5C_tradeoff_points.csv`, `analysis/V_ev_v2/section5E_pareto_points.csv` | HIGH | Scientific core; do not flatten metric-governance nuance. |
| 7. Move large coverage/audit tables to supplement. | same lines 2062-2114, 2470-2554 | `tab:section7_dualview`, `tab:viii_g_1`, `tab:viii_g_2` | `manuscript/finalShortened/prisma_evidence_pack/04_audit_notes/*` | LOW | These are audit traceability tables, not main narrative. |
| 8. Compress enablers section and keep one compact enabler table/figure. | same lines 1515-1811 | `fig_vi_1`, `fig_vi_2`, `tab:vi_a_enablers`, `tab:vi_d_reporting` | `analysis/nb/Section6_Enablers_Evidence_Lab.ipynb` | MEDIUM | Preserve ORIS/OPA/ML/photonic generation as compact synthesis. |
| 9. Compress applications to one portfolio table. | same lines 1812-2120 | `fig_vii_1`, `tab:section7_portfolio`, `tab:section7_dualview` | `analysis/nb/Section7_Applications_Evidence_Lab.ipynb` | LOW | Use one application portfolio and push dual-view audit out. |
| 10. Compress roadmap/challenges to one figure + one agenda table. | same lines 2121-2557 | `fig_viii_1`, `tab:viii_f_1`, `tab:viii_f_2`, `tab:viii_g_1`, `tab:viii_g_2` | `analysis/nb/Section8_OpenChallenges_Roadmap_Evidence_Lab.ipynb` | MEDIUM | Keep roadmap figure plus compact agenda. |
| 11. Reduce reference list by moving full 220-study corpus to supplementary/Zenodo ledger. | `manuscript_submission/references.bib`, source citations throughout | bibliography and all `\cite{}` | `screening/canonical_included_corpus_ledger.csv`, `prisma_evidence_pack/03_screening_and_inclusion/canonical_included_corpus_ledger.csv` | HIGH | Must preserve systematic-review credibility and traceability. |

## 13. Critical Files ChatGPT Must See Next

| Priority | Path | Why ChatGPT needs it | Must upload full file? |
|---:|---|---|---|
| 1 | `manuscript_submission/bare_jrnl_new_sample4.tex` | Active 44-page source; all text/tables/equations inline | yes |
| 1 | `manuscript_submission/bare_jrnl_new_sample4.pdf` | Visual/page-count reference for 44-page compiled state | yes |
| 1 | `manuscript_submission/references.bib` | Citation and reference compression decisions | yes |
| 1 | `manuscript_submission/bare_jrnl_new_sample4.log` | Overfull/page-inflation diagnostics | yes |
| 1 | `screening/canonical_included_corpus_ledger.csv` | 220-study evidence base ledger | yes |
| 1 | `manuscript/finalShortened/prisma_evidence_pack/MANIFEST.csv` | Supplement/evidence-pack map | yes |
| 1 | `analysis/V_ev_v2/section5C_tradeoff_points.csv` | Governed rate-resolution/trade-off data | yes |
| 1 | `analysis/V_ev_v2/section5E_pareto_points.csv` | Sparse governed CRQ/Pareto subset | yes |
| 2 | `analysis/IV_ev_v2/section4E_summary_table.csv` | Taxonomy table evidence | yes |
| 2 | `analysis/V_ev_v2/generate_section5_figures.py` | Figure V provenance | yes |
| 2 | `analysis/IV_ev_v2/generate_section4_figures.py` | Taxonomy figure provenance | yes |
| 2 | `manuscript_submission/figures/` | All included graphics | no, directory list plus key images is enough initially |
| 2 | `protocol/prisma_proto.md` | PRISMA/TQAF/protocol credibility | yes |
| 2 | `manuscript/finalShortened/prisma_evidence_pack/03_screening_and_inclusion/included_studies_canonical.csv` | Included corpus summary | yes |
| 2 | `manuscript/finalShortened/prisma_evidence_pack/02_search_and_flow/search_log.csv` | Search source/date support | yes |
| 3 | `manuscript/current_bundle/section*.tex` | Section-split copy, useful if editing by section | optional |
| 3 | `review_package/04_evidence_audit_bundle.md` | Evidence audit details | optional |
| 3 | `manuscript/finalShortened/shortening_master_tracker.csv` | Existing shortening tracker | optional |
| 3 | `manuscript/finalShortened/section8_compression_map.md` | Existing Section VIII compression notes | optional |

## 14. Exact Commands You Ran

```text
Get-Location
Get-ChildItem -Force
git rev-parse --show-toplevel
git status --short
git branch --show-current
git rev-parse --short HEAD
Get-ChildItem -Directory -Recurse -Depth 2 -Force | Where-Object { $_.FullName -notmatch '\\.git(\\|$)' } | Sort-Object FullName | ForEach-Object { $_.FullName.Substring((Get-Location).Path.Length + 1) }
Get-ChildItem -File -Recurse -Depth 2 -Force | Where-Object { $_.FullName -notmatch '\\.git(\\|$)' } | Sort-Object FullName | ForEach-Object { $_.FullName.Substring((Get-Location).Path.Length + 1) }
git status --short
git branch --show-current
git rev-parse --short HEAD
@' ... directory-depth Python walk, excluding .git/node_modules/venv/__pycache__ ... '@ | python -
@' ... file-depth Python walk, excluding .git/node_modules/venv/__pycache__ ... '@ | python -
Get-ChildItem -Force -Recurse -Depth 2 manuscript,manuscript_submission | Select-Object FullName,Length,LastWriteTime,Mode | Format-Table -AutoSize
rg --files -g '!.git/**' -g '!data/proc_md/**' -g '!data/proc_md_cprev/**' -g '!data/corp_std/**' -g '!legacy_archive/**' | rg '(?i)\.(tex|bib|cls|sty|bst|md|txt|docx|pdf|aux|bbl|log|out|toc|fls|fdb_latexmk)$'
rg -n -i "Optical Integrated Sensing and Communication|O-ISAC|PRISMA|TQAF|CRQ|metric contract|Delta r|Delta r_min|sigma_r|Cram|Fisher|fiber|FSO|VLC|LiFi|photonic-THz|ORIS|OPA|COMST" manuscript manuscript_submission review_package protocol screening search analysis scripts README.md CODEX_START_HERE.md
pdfinfo manuscript/finalManuscript/bare_jrnl_new_sample4.pdf
pdfinfo manuscript/finalShortened/bare_jrnl_new_sample4.pdf
pdfinfo manuscript_submission/bare_jrnl_new_sample4.pdf
rg -n "\\documentclass|\\title|\\input\{|\\include\{|\\bibliography|\\graphicspath|\\includegraphics" manuscript/finalManuscript/bare_jrnl_new_sample4.tex manuscript/finalShortened/bare_jrnl_new_sample4.tex manuscript_submission/bare_jrnl_new_sample4.tex manuscript/current_bundle/main.tex
rg -n "\\section|\\subsection|\\caption|\\label|\\cite|\\ref" manuscript/finalManuscript/bare_jrnl_new_sample4.tex manuscript/finalShortened/bare_jrnl_new_sample4.tex manuscript_submission/bare_jrnl_new_sample4.tex manuscript/current_bundle/main.tex manuscript/current_bundle/section*.tex
Get-FileHash manuscript/finalShortened/bare_jrnl_new_sample4.tex, manuscript_submission/bare_jrnl_new_sample4.tex, manuscript/finalManuscript/bare_jrnl_new_sample4.tex -Algorithm SHA256 | Format-Table -AutoSize
Get-FileHash manuscript/finalShortened/references.bib, manuscript_submission/references.bib, manuscript/finalManuscript/references.bib -Algorithm SHA256 | Format-Table -AutoSize
Get-FileHash manuscript/finalShortened/bare_jrnl_new_sample4.pdf, manuscript_submission/bare_jrnl_new_sample4.pdf, manuscript/finalManuscript/bare_jrnl_new_sample4.pdf -Algorithm SHA256 | Format-Table -AutoSize
@' ... Python parser for primary TeX sections, figures, tables, equations, includegraphics, citations, bib stats ... '@ | python -
@' ... Python graphics inventory using PIL when available ... '@ | python -
@' ... Python PRISMA/TQAF/supplement/data inventory with CSV/JSON row counts ... '@ | python -
@' ... Python script/notebook/reproducibility inventory ... '@ | python -
rg -l -i "Optical Integrated Sensing and Communication|O-ISAC|PRISMA|TQAF|CRQ|metric contract|Delta r|Delta r_min|sigma_r|Cram|Fisher|fiber|FSO|VLC|LiFi|photonic-THz|ORIS|OPA|COMST" -g '!.git/**' -g '!data/proc_md/**' -g '!data/proc_md_cprev/**' -g '!data/corp_std/**' -g '!legacy_archive/**' -g '!*.pdf'
@' ... Python PDF inventory invoking pdfinfo ... '@ | python -
pdftotext -f 1 -l 1 manuscript_submission/bare_jrnl_new_sample4.pdf -
@' ... Python log parser for Overfull/Underfull/Warning/undefined refs/citations ... '@ | python -
rg -n "Overfull|Underfull|Warning|Citation.*undefined|Reference.*undefined|undefined references|Float too large|Too many unprocessed floats" manuscript_submission/bare_jrnl_new_sample4.log manuscript/finalShortened/bare_jrnl_new_sample4.log manuscript/finalManuscript/bare_jrnl_new_sample4.log
@' ... Python focused manuscript candidate table, first run errored on relative path handling ... '@ | python -
@' ... Python TeX command-count/package scan ... '@ | python -
@' ... Python Makefile/latexmkrc/config and .fls dependency scan ... '@ | python -
@' ... Python concise tree for manuscript/screening/search/analysis roots ... '@ | python -
@' ... Python focused manuscript candidate table, fixed absolute path handling ... '@ | python -
rg --files -g '!.git/**' | rg '(^|/)(IEEEtran\.bst|IEEEabrv\.bib|IEEEtran\.cls|references\.bib|.*\.sty|.*\.bst)$'
@' ... Python bibliography entry-count scan across bib files ... '@ | python -
@' ... Python row/column counts for key data files ... '@ | python -
@' ... Python TQAF/quality-appraisal content-path scan ... '@ | python -
Get-ChildItem -Recurse -File -Include IEEEtran.bst,IEEEabrv.bib,IEEEtran.cls,references.bib,*.sty,*.bst | Where-Object { $_.FullName -notmatch '\\.git(\\|$)' } | ForEach-Object { $_.FullName.Substring((Get-Location).Path.Length + 1) } | Sort-Object
@' ... Python top-level section citation-count scan ... '@ | python -
```

Notes on command outcomes:

- The first parallel git/tree scan timed out at 10 seconds; rerun with longer timeouts succeeded.
- The `rg` command using `manuscript/current_bundle/section*.tex` hit a Windows wildcard path error for that operand; later Python parsing and focused scans covered the required content.
- The first candidate-table Python run failed due to relative/absolute path handling; fixed rerun succeeded.
- The `rg --files | rg` style-file command returned no output because of Windows path separator matching; `Get-ChildItem -Include` confirmed available class/bib/style files.

## 15. Open Questions / Ambiguities

- Multiple active-looking manuscript locations exist:
  - `manuscript_submission/bare_jrnl_new_sample4.tex`
  - `manuscript/finalShortened/bare_jrnl_new_sample4.tex`
  - These two `.tex` files are identical by SHA-256; `manuscript_submission/` appears to be the clean handoff package.
- Conflicting page counts exist:
  - Active/submission PDF: 44 pages
  - `manuscript/finalShortened/buildtmp/bare_jrnl_new_sample4.pdf`: 42 pages
  - Older final manuscript: 50 pages
  - Archived staging: 55 pages
- `IEEEabrv.bib` and `IEEEtran.bst` are referenced/needed but not stored in the repo; likely resolved from TeX installation.
- Section V has core governed trade-off tables/figures but no direct `\cite{}` detected inside top-level Section V lines 1310-1514; citations may be carried by upstream tables/data or earlier context.
- `fig:fig_iii_1` is declared as a figure without an external `\includegraphics` path; it appears to be generated in-source.
- Figure source scripts are clear for Section IV and V, but source-generation scripts for all JPEG-converted submission figures are not fully proven from the flat submission package alone.
- `finalShortened` is named as if already shortened, but the compiled active PDF remains 44 pages, so the requested 29-30 page compression is still not reflected in the active compiled artifact.
- `openai_codex_2026` is the only uncited `.bib` entry in the active bibliography.
- No destructive commands were run and no files were modified.
