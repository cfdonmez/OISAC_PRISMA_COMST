# Build Contract Manifest (v1)

## 1) Pipeline orientation (Markdown-first vs LaTeX-first)

Finding: repository is Markdown-first for manuscript drafting; LaTeX template is currently a placeholder.

Evidence:
- Active manuscript sections are `.md` files in `drafts/` (`section_01` ... `section_06`):
  - `drafts/section_01_introduction.md:1`
  - `drafts/section_02_fundamentals_draft.md:1`
  - `drafts/section_03_methodology.md:1`
  - `drafts/section_04_taxonomy.md:1`
  - `drafts/section_05_template.md:1`
- `manuscript/comst_template.tex` contains only placeholder lines: `manuscript/comst_template.tex:1-2`.
- Operational workflow documented around notebooks and PDF->MD extraction, not manuscript compilation: `docs/daily_flow.md:25-31`.

## 2) Citation conventions observed

### 2.1 In-text citation syntax currently in use

- Bracketed project keys with optional locator suffix are the dominant manuscript style:
  - `drafts/section_01_introduction.md:5` (e.g., `[O_ISAC_070:1]`)
  - `drafts/section6_20260217_143141/section_06_camera_ready.md:3` (e.g., `[O_ISAC_008]`)
- Additional non-O_ISAC key usage exists:
  - `drafts/section6_20260217_143141/section_06_camera_ready.md:162` (`[openai_codex_2026]`)
- Numeric bracket references are also present in the manually written references block:
  - `drafts/section_01_introduction.md:238-266` (e.g., `[1]...[14]`)

Contract status: mixed citation modes are present simultaneously.

### 2.2 Bibliography files and source-of-truth status

Discovered bib files:
- `data/references.bib`
- `analysis/refs.bib`

Evidence of operational writer target:
- Bib generator appends to `data/references.bib`: `scripts/generate_bibtex.py:9`, `scripts/generate_bibtex.py:69`, `scripts/generate_bibtex.py:125`.
- `data/references.bib` includes O_ISAC keys and the extra key `openai_codex_2026`: `data/references.bib:8`, `data/references.bib:1354-1356`.

Evidence of conflicting documentation:
- `analysis/README.md` calls `analysis/refs.bib` the central bibliography: `analysis/README.md:28`.
- `analysis/refs.bib` itself states recommended key format `O_ISAC_XXX`: `analysis/refs.bib:1-4`.

Inference (explicit): `data/references.bib` is the operational source-of-truth for current workflows; `analysis/refs.bib` is a secondary/legacy copy.

## 3) Bracket-safety rule (square bracket usage)

Observed behavior:
- Square brackets are used for citations (e.g., `[O_ISAC_...]`): `drafts/section_01_introduction.md:5`.
- Square brackets are also used in mathematical notation: `drafts/section6_20260217_143141/section_06_camera_ready.md:146` (`[R_b-R_e]^+`).

Contract implication:
- Square brackets are not citation-reserved-only.
- Any Markdown/post-processing step must avoid globally rewriting bracketed tokens without context (citation vs math).

## 4) Figure and table numbering policy

Observed numbering in manuscript files:
- Intro uses global figure numbering (`Fig. 1`, `Fig. 2`, `Fig. 3`) and Roman table numbering (`Table I`, `Table II`, etc.):
  - `drafts/section_01_introduction.md:15`, `drafts/section_01_introduction.md:66`, `drafts/section_01_introduction.md:90`
  - `drafts/section_01_introduction.md:26`, `drafts/section_01_introduction.md:52`, `drafts/section_01_introduction.md:187`, `drafts/section_01_introduction.md:201`
- Section VI camera-ready uses section-prefixed table numbering (`Table VI-1`, `Table VI-2`):
  - `drafts/section6_20260217_143141/section_06_camera_ready.md:7`, `drafts/section6_20260217_143141/section_06_camera_ready.md:109`

Contract status: mixed numbering conventions (Roman-global vs section-prefixed-hybrid) are currently coexisting.

## 5) Build entry points discovered

- Data/extraction pipeline entrypoint: `analysis/nb/CoT_Master_Pipeline.ipynb` via `docs/daily_flow.md:26-31`.
- Documentation index includes writing guide and project status, but no manuscript compile command: `docs/README.md:9-13`.
- LaTeX manuscript entrypoint is not yet operational (`manuscript/comst_template.tex:1-2`).

Contract conclusion:
- Manuscript build/compile path is currently implicit and not fully formalized in repo docs.
- Immediate contractual dependencies for citation integrity are bib-file unification and citation-mode normalization.
