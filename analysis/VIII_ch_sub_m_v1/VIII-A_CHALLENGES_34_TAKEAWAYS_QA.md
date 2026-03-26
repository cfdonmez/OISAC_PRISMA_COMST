# VIII-A Challenges 3-4 + Takeaways QA

## PASS/FAIL Checklist
- placeholders=0 (D1): PASS (count=0)
- placeholders=0 (D2): PASS (count=0)
- intent check (`Open Challenges and Research Roadmap`): PASS (`analysis/man_v1/section_intent_manifest.yaml`)
- G2 dependency files PASS (`VIII_PREFLIGHT_QA`, `VIII-A_CONTEXT_QA`, `VIII-A_CHALLENGES_12_QA`): PASS
- axis label exact (`standardization_interoperability`): PASS (present exactly once in D1)
- cite-key lock (must be in VIII-A preflight shortlist and section8A evidence): PASS (`O_ISAC_104`, `O_ISAC_220`)
- evidence excerpts present per new case in D2: PASS (Case 3=3 excerpts, Case 4=3 excerpts)
- takeaways discipline (3-5 bullets, evidence-backed or working hypothesis): PASS (4 bullets total; 3 cited + 1 labeled `working hypothesis`)
- bridge-policy honesty: PASS (no upstream S5/S6/S7 bridge claim used in D1; one INDIRECT label retained for evidence strength)
- length target 260-380 words: PASS (D1 words=356)
- ORIS canon + bracket-safe math: PASS (no OIRS/standalone IRS forms introduced; no bracket-unsafe math introduced)

- Overall verdict: **PASS**

## Cite-Key Existence List
- Keys used in D1: `O_ISAC_104`, `O_ISAC_220`
- `O_ISAC_104` in `data/references.bib`: present
- `O_ISAC_220` in `data/references.bib`: present
- Missing keys: none

## Contract-Violations Check (selected keys/rows)
- Source: `analysis/VIII_ev_v1/contract_violations.csv`
- `O_ISAC_104` with section `8A`: 0 rows
- `O_ISAC_220` with section `8A`: 0 rows
- resolution required: none

## Processed Markdown Validation Log
- Rule check: for each cited key, Abstract/Intro + relevant section + Conclusion/Limitations were opened.
- `O_ISAC_104` -> method=`inventory_fallback` -> path=`data/proc_markdowns/O_ISAC_104/O_ISAC_104/O_ISAC_104.md`
  - intro locator: `I. INTRODUCTION`, line 47
  - relevant locator: `I. INTRODUCTION`, line 53
  - conclusion locator: `III. CONCLUSIONS`, line 77
- `O_ISAC_220` -> method=`inventory_fallback` -> path=`data/proc_markdowns/O_ISAC_220/O_ISAC_220.md`
  - intro locator: `1. INTRODUCTION`, line 13
  - relevant locator: `1. INTRODUCTION`, line 23
  - conclusion locator: `5. CONCLUSION`, line 182

## Path Resolution Method
- Primary: `analysis/man_v1/file_index.csv`
- Fallback: `analysis/II_md_inv.csv`
- primary hits: 0/2
- fallback hits: 2/2

## SHA256
- `VIII-A_CHALLENGES_34_TAKEAWAYS.md`: `e019381bcc4af1609a91cdb752834e8b1adc0d4e30c5c0aea672bb958bf326c8`
- `VIII-A_CHALLENGES_34_TAKEAWAYS_supp.md`: `1b3d9136ae83693931b4516f769c7e8835e5ac141dfb820111558bcdf4dde0c0`
