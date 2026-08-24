# Nine-Section Manuscript Architecture

## Why the architecture changed

The 76-paper COMST close reading found a median of eight main sections and an
interquartile range of seven to nine. The former 13-section candidate sat near
the 98.7th percentile and repeatedly reset the reader between evidence axes
that answer the same scientific question. The new structure uses nine main
sections. No evidence family is deleted; related jobs are placed under one
reader-facing container.

| New file | Reader job | Source material | Main visual carriers | Prose target |
|---|---|---|---|---:|
| `00_ABSTRACT.tex` | State the problem, scale, findings, and survey value | v1 Abstract | none | 190--240 |
| `01_INTRODUCTION.tex` | Motivate O-ISAC, define the gap, position prior surveys, and state contributions | v1 Sections I--II | Table I | 1,250--1,750 plus table |
| `02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex` | Teach system boundaries and what must remain visible before comparison | v1 Section III | Figs. 1--2; Table II | 1,100--1,500 |
| `03_REVIEW_METHOD_AND_EVIDENCE_BASE.tex` | Briefly establish corpus construction, evidence use, and appraisal boundaries without making PRISMA the topic | v1 Sections IV--V | Figs. 3--4; Table III | 500--700 |
| `04_OPTICAL_PLATFORMS_AND_INTEGRATION_ARCHITECTURES.tex` | Explain how physical platforms and coupling mechanisms shape one another | v1 Sections VI--VII | Table IV; Fig. 5 | 2,200--2,800 |
| `05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex` | Connect measurement meaning to recurring design tradeoffs | v1 Sections VIII--IX | Table V; Fig. 6 | 2,300--2,900 |
| `06_VALIDATION_REPRODUCIBILITY_AND_BENCHMARK_READINESS.tex` | Test how far reported claims travel beyond their source setting | v1 Section X | Fig. 7; Table VI | 1,000--1,400 |
| `07_ENABLING_TECHNOLOGIES_APPLICATIONS_AND_6G.tex` | Relate enabling mechanisms to application requirements and 6G implications | v1 Section XI plus the network-evidence discussion | Fig. 8; Table VII | 1,400--1,800 |
| `08_DISCUSSION_ROADMAP_AND_LIMITATIONS.tex` | Synthesize lessons, convert gaps into testable priorities, and disclose limitations | v1 Section XII after 6G deduplication | Table VIII | 1,100--1,500 |
| `09_CONCLUSION.tex` | Return to the central comparison problem without introducing new evidence | v1 Section XIII | none | 200--280 |

The ranges are reader-load guides, not instructions to add filler. Tables and
figures should carry repeated inventories; prose should explain mechanisms,
conditions, implications, and boundaries.

The final static extraction contains 14,652 prose words when TeX comments and
table bodies are excluded; the integrity audit counts 15,153 words when the
implemented Table I is retained. These counts are intentionally below the
local COMST median and are not repaired with filler. Section V exceeds its
initial guide because the eleven governed tradeoff families require distinct
conditions and boundaries; its repeated inventory is assigned to the planned
three-panel Figure 6 rather than duplicated in additional prose.

## Merge rules

- Table I and prior-survey positioning remain in the Introduction, but the
  source rows are not restated in prose.
- Method and corpus profile form one section because their joint reader job is
  to define the evidence and its inferential limits.
- Modalities and integration mechanisms form one section because they are two
  views of the same 206 systems.
- Metrics and tradeoffs form one section because a tradeoff is interpretable
  only after its quantities and measurement planes are defined.
- Validation remains separate because evidence maturity and benchmark
  readiness are substantive contributions.
- 6G interpretation appears once, with applications and network evidence.
- Limitations remain with the discussion and roadmap.

## Visual contract

The main text retains eight figures and eight tables. Table I is implemented;
all other carriers remain design specifications until the dedicated production
and visual-QA pass. No visual may repeat the complete prose inventory, rank
incompatible systems, or imply precision unsupported by the governed data.
