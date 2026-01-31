# ID_QA_report

## Rules Applied
- COMST_master_recipe.md: Table I reserved for related-survey comparison; keep Intro lean and gap-focused.
- master_writing_guide.md: COMST headings, table/figure references before appearance, avoid superlatives.
- introduction_templates.md: comparison-table placement and gap-selling structure in the Introduction.
- body_section_templates.md: synthesis-first tone (no paper-by-paper listing).
- methodology_template.md: PRISMA framing consistency for systematic-review claims.
- abstract_templates.md: tone discipline and formal academic phrasing guardrails.
- surveyOutline.md: notation/acronym table placement and metric-contract emphasis.
- systemPatterns.md: canonical paths for extraction JSONs and processed markdowns.
- goldenModel.md: requirement for explicit gap positioning via comparison table.

## Evidence Log
| Key | JSON path | MD path | Sections read | Verified facts (<=2) | Final table decision |
| --- | --- | --- | --- | --- | --- |
| O_ISAC_161 | data/extraction_results_v4/O_ISAC_161_v4.json | data/processed_markdowns/O_ISAC_161/O_ISAC_161.md | Abstract, Introduction | Hardware-centric ISAC transceiver review focused on RF/mmWave/THz front-ends. <br> JSON classification lists carrier_band mmW. | Modality scope ○/○/○/○; Tier-2; Methodology Review. |
| O_ISAC_068 | data/extraction_results_v4/O_ISAC_068_v4.json | data/processed_markdowns/O_ISAC_068/O_ISAC_068/O_ISAC_068.md | Abstract, Keywords, Introduction | JCS overview with explicit focus on RF-JCS and VL-JCS. <br> JSON classification carrier_band visible. | Modality scope ○/○/●/○; Tier-2; Methodology Narrative. |
| O_ISAC_327 | data/extraction_results_v4/O_ISAC_327_v4.json | data/processed_markdowns/O_ISAC_327/O_ISAC_327.md | Abstract, Index Terms | Survey of VLC channel characterization/modeling for 6G IoE. | Modality scope ○/○/●/○; Tier-2; Methodology Survey. |
| O_ISAC_006 | data/extraction_results_v4/O_ISAC_006_v4.json | data/processed_markdowns/O_ISAC_006/O_ISAC_006/O_ISAC_006.md | Abstract, Introduction | Review of ISAC in optical fiber (forward and backscattered light). | Modality scope ●/○/○/○; Tier-2; Methodology Review. |
| O_ISAC_368 | data/extraction_results_v4/O_ISAC_368_v4.json | data/processed_markdowns/O_ISAC_368/O_ISAC_368.md | Abstract, Introduction | Technical review of ISAC in optical transmission systems; fiber-centric schemes. | Modality scope ●/○/○/○; Tier-2; Methodology Review. |
| O_ISAC_021 | data/extraction_results_v4/O_ISAC_021_v4.json | data/processed_markdowns/O_ISAC_021/O_ISAC_021/O_ISAC_021.md | Abstract, Introduction | O-ISAC article integrating FSO communication and optical sensing; architectures/opportunities. | Modality scope ○/●/○/○; Tier-2; Methodology Tutorial. |
| O_ISAC_070 | data/extraction_results_v4/O_ISAC_070_v4.json | data/processed_markdowns/O_ISAC_070/O_ISAC_070/O_ISAC_070.md | Abstract, Index Terms | Photonic THz-ISAC waveform article; THz band emphasis. | Modality scope ○/○/○/●; Tier-2; Methodology Narrative. |
| O_ISAC_163 | data/extraction_results_v4/O_ISAC_163_v4.json | data/processed_markdowns/O_ISAC_163/O_ISAC_163.md | Abstract, Index Terms | Survey of multi-functional/hybrid RIS for ISAC in RF/mmWave/THz context. | Modality scope ○/○/○/○; Tier-2; Methodology Survey. |
| O_ISAC_303 | data/extraction_results_v4/O_ISAC_303_v4.json | data/processed_markdowns/O_ISAC_303/O_ISAC_303.md | Abstract, Introduction | Review of VLC-based LiSAC (lighting, sensing, communication). | Modality scope ○/○/●/○; Tier-1; Methodology Review. |
| O_ISAC_105 | data/extraction_results_v4/O_ISAC_105_v4.json | data/processed_markdowns/O_ISAC_105/O_ISAC_105/O_ISAC_105.md | Abstract, Results | 120 Gbps with 2.5 mm range resolution; CRQ_Δ 480 Gbps/cm (4.8×10^13 bps/m). | Used in exemplar prose (not a Table I row). |
| O_ISAC_016 | data/extraction_results_v4/O_ISAC_016_v4.json | data/processed_markdowns/O_ISAC_016/O_ISAC_016.md | Abstract, Results | 251.03 Gbps with 2.5 cm resolution; CRQ_Δ ~100 Gbps/cm (1.0×10^13 bps/m). | Used in exemplar prose (not a Table I row). |
| O_ISAC_046 | data/extraction_results_v4/O_ISAC_046_v4.json | data/processed_markdowns/O_ISAC_046/O_ISAC_046.md | Abstract, Experimental setup | 241.85 Tb/s aggregate capacity and 20 m spatial granularity at 0.1 Hz vibration sensing. | Used in exemplar prose and Fig. 2 (not a Table I row). |

## Table Captions (final numbering)
- Table I: Axis-Based Comparison of This Survey with Existing Related Survey-Style Works.
- Table II: RF-ISAC vs. O-ISAC Performance Comparison [O_ISAC_021].
- Table III: Mathematical Notation Conventions.
- Table IV: List of Frequently Used Acronyms.

## Post-Edit QA (final file)
- I-A sentence with [O_ISAC_105] (verbatim): Recent photonic and fiber demonstrations illustrate the rate–resolution frontier: a 275 GHz LFM-QAM system reports 120 Gbps with a (two-way) bandwidth-limited range resolution $\Delta r_{\min} \approx 2.5$ mm, yielding $\text{CRQ}_{\Delta} := R / \Delta r_{\min} = 4.8\times10^{13}$ bps/m (equivalently 480 Gbps/cm) [O_ISAC_105]; a D-band sub-THz FDM link delivers 251.03 Gbps with $\Delta r_{\min}=2.5$ cm [O_ISAC_016]; and co-wavelength DAS/DSM over a 38 km seven-core fiber sustains 241.85 Tb/s while sensing 0.1 Hz vibrations with 20 m spatial granularity [O_ISAC_046]. These exemplars highlight the bandwidth advantages of optical carriers and motivate a systematic question.
- Table I legend (verbatim): *Legend: ● = strong/explicit (Score 1); ◐ = partial/within-modality (Score 0.5); – = absent (Score 0); ○ = out-of-scope. Modality Scope uses (○/◐/●) only. F = Fiber, FSO = Free-Space Optics, VLC = Visible Light, THz = Photo-THz. THz denotes photonic-THz / optical–THz bridging O-ISAC (not generic RF THz-ISAC hardware surveys).*
- Token checks: "\\Delta R" = 0; "\\sigma_R" = 0; "### Table I:" = 1.
- Citation keys unchanged.

## Token Checks (final file)
- "**Table I** summarizes state-of-the-art": 0
- "### Table I:": 1
- "\\Delta R": 0
- "\\sigma_R": 0
- "–" inside Modality Scope cells: 0

## Final Table I Row for O_ISAC_161 (verbatim)
| [O_ISAC_161] | 2025 | 2 | ○ / ○ / ○ / ○ | ● | Review | ◐ | – | – | – | – |

## Citation Keys
All citation keys retained; no renaming performed.
