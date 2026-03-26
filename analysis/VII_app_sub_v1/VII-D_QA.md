# VII-D Integration QA

## Checklist (PASS/FAIL)
- Placeholder markers: **PASS** (none found in `analysis/VII_app_sub_v1/VII-D.md` and `analysis/VII_app_sub_v1/VII-D_supp.md`).
- Intent discipline (Applications and Use Cases): **PASS** (`analysis/man_v1/section_intent_manifest.yaml` confirms Section VII intent).
- Plane separation (comm-plane vs sensing-plane): **PASS** (explicitly preserved in context, scenarios, and math-anchor mapping text).
- ORIS canon: **PASS** (no `OIRS` or standalone `IRS` variants detected; ORIS-only terminology retained where component-dominance is discussed).
- Bracket-safe math: **PASS** (no square-bracket math tokens detected; display math uses `$$...$$`, citation brackets only).
- Word count target (520-820): **PASS** (`625` words in `analysis/VII_app_sub_v1/VII-D.md`).

## Cite-Key Integrity
Cite keys found in `analysis/VII_app_sub_v1/VII-D.md`:
- `O_ISAC_020`
- `O_ISAC_027`
- `O_ISAC_127`
- `O_ISAC_220`

Bibliography existence check (`data/references.bib`):
- `O_ISAC_020`: FOUND (`data/references.bib:132`)
- `O_ISAC_027`: FOUND (`data/references.bib:174`)
- `O_ISAC_127`: FOUND (`data/references.bib:780`)
- `O_ISAC_220`: FOUND (`data/references.bib:1128`)

No-new-cite-key check against preflight shortlist (`analysis/VII_app_sub_v1_micro/VII-D_PREFLIGHT.md`):
- **PASS** (final set exactly matches preflight set: `O_ISAC_020`, `O_ISAC_027`, `O_ISAC_127`, `O_ISAC_220`).

## Decision Trace
RUN4 selected **Option-1 (joint trade-off)**, and the integrated subsection preserves that decision without modification. Decision source: `analysis/VII_app_sub_v1_micro/VII-D_MATH_ANCHOR_DECISION.md`.

## SHA256
- `analysis/VII_app_sub_v1/VII-D.md`: `53a3e09a561b1b859a7e57a5db96480806a7f6681abb561ad2092be1168b8758`
- `analysis/VII_app_sub_v1/VII-D_supp.md`: `074a1b23962147f9997934a9d7f708c4e6eb5e17c0326e596381d4671a21cb21`
