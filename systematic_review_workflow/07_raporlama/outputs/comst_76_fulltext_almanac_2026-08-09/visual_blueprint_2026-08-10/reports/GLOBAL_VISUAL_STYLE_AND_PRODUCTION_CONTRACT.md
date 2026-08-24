# O-ISAC survey: global visual style and production contract

Status: specification contract with one live carrier. Table I is implemented in Section II as a `table*` and awaits layout review; the other 15 main-text carriers remain pending. No external PNG/PDF/SVG asset has been created.

## 1. Governing principle

Every visual must do one scientific job that prose cannot do as efficiently. A visual is retained only when it does at least one of the following:

1. exposes a relationship or sequence;
2. reconciles denominators or counting units;
3. externalizes a reusable taxonomy or comparison contract;
4. compresses a study or evidence inventory without hiding provenance; or
5. makes a cross-section distinction visible and prevents later repetition.

Decorative illustrations, generic 6G artwork, word clouds, and plots added only to imitate the number of figures in published surveys are prohibited.

## 2. Evidence hierarchy

Visual content must be generated from the following sources, in order:

1. frozen public/canonical CSV projections and Phase-F synthesis tables;
2. locked PRISMA and report-to-study artifacts;
3. the final 206-study extraction and TQAF artifacts;
4. manuscript prose only as an explanation layer, never as the numeric authority;
5. the 76-paper COMST corpus only as a functional and rhetorical exemplar, never as a source of O-ISAC facts.

No value may be read from a published plot, digitized, estimated by eye, or inferred from a neighboring study. No figure from a reviewed paper or COMST exemplar may be copied or redrawn closely. Exemplar use is restricted to visual function, placement, and reader guidance.

## 3. Planned density and balance

The main-text architecture contains 16 visual carriers: 8 figures and 8 tables. With 15,391 narrative words, this is 1.040 visuals per 1,000 words. The 76-paper COMST corpus has a median of 0.938 visuals per 1,000 words and an interquartile range of approximately 0.754--1.284. The architecture remains inside the corpus density range without imitating its raw median of 13 figures and 8 tables. One table is implemented in TeX; seven tables and eight figures remain pending.

The plan deliberately uses more tables than the typical figure-to-table ratio because this survey must preserve definitions, denominators, provenance, and non-comparability conditions. A graph is preferred only when position, contrast, distribution, or sequence is the reader's primary task.

## 4. Placement contract

For every visual:

- the first explicit callout must occur before the float;
- the lead-in sentence must state the question the visual answers, not merely say "shown in Fig.";
- the first paragraph after the float must interpret the main pattern and its boundary;
- the visual must be placed in the section that owns its scientific job;
- a visual may be referenced elsewhere but must not be re-explained in full;
- a new section must not open with an unexplained float;
- two full-width floats should not be placed consecutively without interpretive prose between them;
- the Abstract and Conclusion receive no new visual;
- the Introduction remains visual-free; the first visual is the Section II native-evidence-object figure, while the detailed comparison framework remains owned by Section III;
- the PRISMA flow remains in Corpus and Appraisal Results, not at the front of the article, so review mechanics do not eclipse the survey contribution.

## 5. Figure grammar

### 5.1 Allowed archetypes

- original conceptual framework or signal-path schematic;
- flow/reconciliation diagram with explicit counting units;
- horizontal bar, lollipop, or 100% stacked profile for governed categorical counts;
- small multiples when panels have the same unit and scale;
- non-weighted conceptual layer map whose arrows are explicitly labelled as conceptual;
- direct-label matrix when pairwise data are actually available.

### 5.2 Prohibited or restricted archetypes

- pie/donut charts;
- 3-D bars, surfaces, or perspective effects;
- dual y-axes;
- rainbow or red--green-only palettes;
- word clouds;
- radar/spider charts;
- Sankey or chord diagrams when link weights are not extracted;
- UpSet or network diagrams when normalized study-level combinations are not frozen;
- stacked bars for multi-label categories when the stack would imply a partition;
- a Pareto frontier assembled from heterogeneous studies;
- a cross-platform performance leaderboard;
- truncated count axes, decorative gradients, drop shadows, or pictograms scaled by area.

### 5.3 Axis and label rules

- count axes start at zero;
- percentages use one decimal place when reported in prose and captions;
- every axis states the unit and analysis unit;
- direct labels are preferred to legends;
- categories follow a scientific order fixed in the specification, not an arbitrary software default;
- multi-label and mutually exclusive distributions are identified next to the data, not only in distant prose;
- panels are labelled (a), (b), and so on in the upper-left corner;
- no statistical uncertainty interval is added to a complete-corpus descriptive count;
- frequency is never described as effect size, importance, quality, or causal strength.

## 6. Table grammar

- table captions appear above the table and are self-contained;
- no vertical rules; use restrained horizontal rules and grouped headers;
- do not use `\resizebox` to force dense prose below a readable size;
- final type should remain approximately 9--10 pt where feasible;
- cells contain controlled phrases rather than paragraphs;
- column order follows the reader's decision sequence;
- every count column identifies its denominator and whether categories are exclusive or multi-label;
- abbreviations and non-obvious codes are defined below the table;
- representative citations do not substitute for the electronic 206-study inventory;
- a long inventory belongs in a repeated-header supplementary table or machine-readable file, not a compressed main-text table;
- blank, not reported, not applicable, and zero remain distinct states.

## 7. Global color and encoding system

Two palettes are kept separate.

### 7.1 Modality palette

- photonic-THz: blue `#0072B2`;
- fiber: bluish green `#009E73`;
- VLC/LiFi: orange `#E69F00`;
- FSO: sky blue `#56B4E9`;
- hybrid optical: purple `#CC79A7`;
- other optical: neutral gray `#7F7F7F`.

The same modality color must be reused wherever modality is encoded. Every color also receives a text label and, when needed, a marker or pattern.

### 7.2 Status palette

- supported/strong/open: dark blue plus solid fill;
- adequate/conditional/on request: amber plus diagonal pattern or distinct marker;
- low/restricted/unavailable-or-not-reported: dark gray or vermillion plus cross-hatch;
- not applicable: white fill with gray outline.

The status palette must not be interpreted as the modality palette. Red and green are never the sole differentiators. Every figure must remain interpretable in grayscale.

## 8. Caption contract

Each caption must state, in this order:

1. the reader question or visual subject;
2. the unit of analysis and denominator;
3. the meaning of panels, encodings, or columns;
4. whether categories are exclusive or multi-label;
5. the canonical data source/version;
6. the principal non-claim (for example, frequency is not performance strength);
7. abbreviations not already obvious from the article.

Captions should not merely repeat the section text. The figure/table is introduced before placement and interpreted after placement.

## 9. Accessibility contract

- verify all figures in grayscale;
- combine color with line style, marker, label, or pattern;
- maintain strong text/background contrast;
- avoid yellow text or thin pale lines on white;
- provide concise alt text describing the relationship and main pattern, not every printed value;
- preserve a machine-readable source table for every data-driven plot;
- use direct labels where space permits;
- do not encode meaning only by position in a legend;
- keep acronym density low inside figures.

## 10. IEEE production contract

- preferred delivery is vector PDF or EPS with embedded fonts;
- accepted IEEE graphic formats include PS, EPS, PDF, PNG, and TIFF;
- raster fallback: greater than 300 dpi for color/grayscale and greater than 600 dpi for black-and-white line art;
- target widths: 3.5 in (88.9 mm) for one column and 7.16 in (182 mm) for two columns;
- target type appearance: approximately 9--10 pt at final size;
- use an IEEE-supported font such as Arial, Helvetica, Times New Roman, Cambria, or Symbol;
- do not rasterize text in charts;
- keep the editable source plus the submitted vector/raster export;
- use consistent figure file naming and sequential numbering.

Official references:

- [IEEE COMST policies and guidelines](https://www.comsoc.org/publications/journals/ieee-comst/policies-guidelines)
- [IEEE Author Center: create graphics for a journal article](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/)
- [IEEE Author Center: resolution and size](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/resolution-and-size/)
- [IEEE Author Center: file formatting](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/file-formatting/)

## 11. Reproducible production route

Every data-driven figure must have:

- a named canonical input file;
- an explicit row filter and analysis unit;
- assertions for all locked denominators;
- a generated plot-data CSV;
- a deterministic script with no hard-coded display values that bypass the input;
- a source-file checksum and software-version record;
- vector PDF output and a raster QA preview;
- a grayscale QA render;
- an automated check for missing labels, category drift, and count reconciliation.

Matplotlib exports should embed TrueType fonts (`pdf.fonttype=42`, `ps.fonttype=42`) and use the final publication width during design. Conceptual diagrams should be stored as editable vector source and exported to PDF; their arrows, widths, and spatial proximity must not imply evidence strength unless a frozen data relation supports that encoding.

## 12. Numeric integrity gates

At implementation time the following checks must pass:

- modality families: 69 + 56 + 38 + 31 + 9 + 3 = 206;
- claim-use partition: 3,206 + 4,997 + 31 + 72 = 8,306;
- primary synthesis: 3,206 + 4,997 = 8,203 and 3,020 + 4,779 + 404 = 8,203;
- trade-off ledger: 218 + 186 = 404; two qualitative rows are absence-status sentinels; the substantive set is 402 records from 168 studies and comprises 218 quantitative plus 184 qualitative records; conditional rows reconcile as 373/404 for the governed ledger and 371/402 after the two conditional sentinels are removed;
- maximum validation tier: 32 + 18 + 78 + 66 + 12 = 206;
- data availability: 145 + 41 + 13 + 7 = 206;
- code/model availability: 197 + 7 + 1 + 1 = 206;
- every TQAF dimension and the overall contribution profile sum to 206;
- multi-label mechanisms, validation methods, technologies, and applications must not be summed as though they partition 206 studies.

Any failed gate blocks visual generation and manuscript insertion.

## 13. Review and sign-off gates

For each visual, sign-off is separate for:

1. scientific job;
2. source and denominator;
3. encoding and non-claims;
4. caption and prose integration;
5. accessibility and grayscale behavior;
6. publication-size legibility;
7. author approval.

The blueprint freezes specifications for all 16 carriers. Table I has status `implemented_in_tex_pending_layout_review`; the other 15 carriers remain `pending_not_created`. Author review remains pending for all 16, and the live table is not considered complete until float placement, wrapping, and final-size legibility are inspected.
