# Supplementary Material for Section VI (Appendix VI-S)

## VI-S.1 Purpose and Scope

This appendix contains material relocated from the draft to keep the main Section VI narrative publication-ready: artifact mapping notes, condensed evidence mapping, and evidence-gap items that are useful for internal traceability but not suitable for camera-ready flow.

## VI-S.2 Relocated Structural Blocks from `drafts/section_06_draft.md`

| Relocated block type | Original location in draft | Action in camera-ready section |
|---|---|---|
| Artifact map (global) | `drafts/section_06_draft.md:1` | Removed from main text and summarized here |
| Evidence table (VI-A) | `drafts/section_06_draft.md:43` | Replaced by narrative synthesis with inline citations |
| Artifact map (VI-B) | `drafts/section_06_draft.md:202` | Relocated to this appendix |
| Evidence table (VI-B) | `drafts/section_06_draft.md:238` | Replaced by compact robustness synthesis |
| Artifact map (VI-C) | `drafts/section_06_draft.md:436` | Relocated to this appendix |
| Evidence table (VI-C) | `drafts/section_06_draft.md:479` | Replaced by optimization narrative anchors |
| Artifact map (VI-D) | `drafts/section_06_draft.md:693` | Relocated to this appendix |
| Evidence table (VI-D) | `drafts/section_06_draft.md:735` | Replaced by benchmark contract and checklist |
| Artifact map (VI-E) | `drafts/section_06_draft.md:947` | Relocated to this appendix |
| Evidence table (VI-E) | `drafts/section_06_draft.md:984` | Replaced by cross-layer synthesis narrative |
| Artifact map (VI-F) | `drafts/section_06_draft.md:1224` | Relocated to this appendix |
| Evidence table (VI-F) | `drafts/section_06_draft.md:1263` | Replaced by conservative AI/security synthesis |

## VI-S.3 Condensed Evidence Map Used in Camera-Ready VI-A to VI-F

| Subsection | Core evidence-backed points retained in main text | Representative source keys |
|---|---|---|
| VI-A (OPA and ORIS) | OPA steering and joint waveform gains; ORIS alignment offloading and NLoS support; communication-sensing coupling | `O_ISAC_008`, `O_ISAC_061`, `O_ISAC_091`, `O_ISAC_098`, `O_ISAC_112` |
| VI-B (Robustness) | Composite impairment modeling and outage-constrained design; turbulence, weather, and pointing impacts | `O_ISAC_023`, `O_ISAC_035`, `O_ISAC_061`, `O_ISAC_098`, `O_ISAC_199` |
| VI-C (Co-design) | IM/DD-constrained feasible sets; weighted rate-CRB optimization; dynamic adaptation constraints | `O_ISAC_009`, `O_ISAC_023`, `O_ISAC_054`, `O_ISAC_061`, `O_ISAC_091`, `O_ISAC_127` |
| VI-D (Benchmarking) | Parameter disclosure exists but benchmark contracts are heterogeneous; reproducibility and timing fields are uneven | `O_ISAC_023`, `O_ISAC_035`, `O_ISAC_054`, `O_ISAC_061`, `O_ISAC_091`, `O_ISAC_112`, `O_ISAC_127` |
| VI-E (Networked systems) | Multi-user interference and control overhead dominate scaling; cross-layer coupling required | `O_ISAC_009`, `O_ISAC_061`, `O_ISAC_068`, `O_ISAC_091`, `O_ISAC_098`, `O_ISAC_303` |
| VI-F (AI and security) | Learning adaptation and secrecy-aware design are both present; joint verification protocols remain limited | `O_ISAC_127`, `O_ISAC_145`, `O_ISAC_156`, `O_ISAC_163` |

## VI-S.4 Relocated Evidence-Gap Ledger (Removed from Main Narrative)

These items were removed from camera-ready Section VI because the current corpus snapshot does not provide sufficiently consistent support for formal claims:

1. Direct phase-noise measurements for OPA and ORIS controllers in shared reporting formats.
2. Broad, reproducible ADMM/manifold complexity-versus-accuracy tables specific to optical O-ISAC.
3. Cross-paper eye-safety margin reporting jointly with BER, CRB (or RMSE), and latency in one template.
4. Public benchmark suites with unified network overhead fields (feedback bits, control symbols, fronthaul timing).
5. Standardized fairness reporting (for example, common fairness indices) across networked optical O-ISAC studies.
6. Unified domain-shift benchmark protocols for AI-enabled optical O-ISAC adaptation.
7. Reproducible optical attack testbeds with open scripts and full evaluation metadata.

## VI-S.5 Source Paths Used During Refactoring

- Primary draft: `drafts/section_06_draft.md`
- Bibliography: `data/references.bib`
- Processed corpus examples:
  - `data/proc_markdowns/O_ISAC_008/O_ISAC_008.md`
  - `data/proc_markdowns/O_ISAC_009/O_ISAC_009.md`
  - `data/proc_markdowns/O_ISAC_011/O_ISAC_011.md`
  - `data/proc_markdowns/O_ISAC_023/O_ISAC_023.md`
  - `data/proc_markdowns/O_ISAC_035/O_ISAC_035.md`
  - `data/proc_markdowns/O_ISAC_054/O_ISAC_054.md`
  - `data/proc_markdowns/O_ISAC_061/O_ISAC_061.md`
  - `data/proc_markdowns/O_ISAC_091/O_ISAC_091.md`
  - `data/proc_markdowns/O_ISAC_098/O_ISAC_098/O_ISAC_098.md`
  - `data/proc_markdowns/O_ISAC_112/O_ISAC_112/O_ISAC_112.md`
  - `data/proc_markdowns/O_ISAC_127/O_ISAC_127/O_ISAC_127.md`
  - `data/proc_markdowns/O_ISAC_199/O_ISAC_199.md`
  - `data/proc_markdowns/O_ISAC_303/O_ISAC_303.md`

