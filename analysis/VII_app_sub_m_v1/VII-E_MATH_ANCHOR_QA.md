# VII-E MATH_ANCHOR QA

## PASS/FAIL Checklist
- Placeholders (`TODO/TBD/FIXME/ELLIPSIZATION`): PASS
- Intent gate (Section VII = "Applications and Use Cases"): PASS
- Scope lock (`space_satellite` proven in `analysis/VII_app_sub_v1_micro/VII-E_PREFLIGHT_QA_PATCH_v2.md`): PASS
- Bracket-safe math (no square-bracket math tokens): PASS
- Plane separation (comm-plane vs sensing-plane explicitly separated): PASS
- Enabling-tech honesty (no ORIS/OPA/RIS phase variables introduced): PASS
- No-ghost-parameter safety (only excerpt-supported `s` elements used): PASS
- Numeric-claim safety (no unsupported numeric thresholds introduced in anchor): PASS
- Word count for D1 (target 90–190): PASS (`95` words)

## Cite-Key Existence (`data/references.bib`)
- `O_ISAC_187`: FOUND
- `O_ISAC_195`: FOUND

## Processed Markdown Validation Log
- `O_ISAC_187` -> `data/proc_markdowns/O_ISAC_187/O_ISAC_187.md`
  - Opened: `Abstract` (`7`), `1. Introduction` (`13`, `23`), `2. Principle` (`25+`), `6. Conclusion` (`402`)
  - D2 locators recorded: `Abstract:7-7`, `1. Introduction:13-13`, `1. Introduction:23-23`
- `O_ISAC_195` -> `data/proc_markdowns/O_ISAC_195/O_ISAC_195.md`
  - Opened: `Abstract` (`5`), `1. Introduction` (`11`), `2. Framework of ISAC systems based on multi-beamforming` (`43`), `3.2. Verification test of the ISAC system` (`120`), `4. Conclusion` (`126-128`)
  - D2 locators recorded: `2. Framework...:43-43`, `3.2. Verification test...:120-120`

## Path Resolution Method
- Primary source: `analysis/man_v1/file_index.csv`
- Primary hits for used cite-keys: `0/2`
- Fallback source: `analysis/II_md_inv.csv`
- Fallback used: `Y`
- Fallback hits: `2/2`

## Decision Trace (Option Selection + Supported Items)
- Selected anchor form: **Option-1 (Joint trade-off)**.
- Comm-plane supported items: communication rate evidence and BER evidence (`O_ISAC_187`, lines `7`, `23`).
- Sensing-plane supported items: range-resolution evidence (`O_ISAC_187`, line `7`; `O_ISAC_195`, line `120`).
- Deployment constraints retained in `s`: LEO space context and shared multi-beam payload topology (`O_ISAC_187`, line `13`; `O_ISAC_195`, line `43`).
- Omitted as unsupported in this anchor: explicit pointing-jitter equation terms.

## SHA256
- `analysis/VII_app_sub_v1_micro/VII-E_MATH_ANCHOR_DECISION.md`: `cea2057fd1c457dd7f168933d8356f7921e6ff1194f63110dd96dba84f202952`
- `analysis/VII_app_sub_v1_micro/VII-E_MATH_ANCHOR.md`: `eb9b2eaf14dad193c48c9f1408ac507d5a55fba86a5f6163902098c6000b9d89`
- `analysis/VII_app_sub_v1_micro/VII-E_MATH_ANCHOR_supp.md`: `2d508ac78e08f07facee8a3b2f6af63f7ee8c75f92d67c18b2c08744949a556d`
