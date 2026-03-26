# VII-F Integration QA

## Checklist PASS/FAIL
- Placeholders (`TODO/TBD/FIXME/ELLIPSIZATION`): PASS (0 hits).
- Intent discipline (applications and use-case synthesis only): PASS.
- Cross-domain discipline: PASS (context and all four scenarios remain macro-tagged and transfer-oriented).
- ORIS canon: PASS (no `OIRS` or standalone `IRS` variants; only O-ISAC and ORIS terminology where needed).
- Bracket-safe math: PASS (no square-bracket math tokens; square brackets are citation-only).
- Word count: PASS (`814` words in `analysis/VII_app_sub_v1/VII-F.md`, target 560-900).

## Cite-Key Integrity (`analysis/VII_app_sub_v1/VII-F.md`)
Cite keys found:
- `O_ISAC_011`
- `O_ISAC_074`
- `O_ISAC_108`
- `O_ISAC_143`
- `O_ISAC_164`
- `O_ISAC_187`

Bibliography existence check (`data/references.bib`):
- `O_ISAC_011`: FOUND
- `O_ISAC_074`: FOUND
- `O_ISAC_108`: FOUND
- `O_ISAC_143`: FOUND
- `O_ISAC_164`: FOUND
- `O_ISAC_187`: FOUND

## No-New-Cite-Key Check
- Cite-key set in integrated file exactly matches the cite-key set already present across VII-F micro-parts used for integration.
- Result: PASS, no new cite keys introduced.

## Decision Trace
Anchor-B is preserved in the integrated subsection, consistent with the Run4 decision that VII-F should use coverage and transfer-structure optimization rather than a single-scenario trade-off. Decision source: `analysis/VII_app_sub_v1_micro/VII-F_MATH_ANCHOR_DECISION.md`.

## SHA256
- `analysis/VII_app_sub_v1/VII-F.md`
  - `dff804a800df795eeaa012e6e9d628cd34d7583f087b503e764b7bd1e22e8ced`
- `analysis/VII_app_sub_v1/VII-F_supp.md`
  - `0ba65916ceb84989343e65f8765746ed118b5f5989d4f87b05aecb7f55b98d84`
