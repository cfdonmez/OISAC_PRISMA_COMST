# O-ISAC COMST working agreements

Before substantive work, read `handoff/state.md`, then
`governance/V3_ACTIVE_WRITING_RULES.md`. Use `handoff/index.md` to find the
relevant evidence, recipes and historical memory. Do not load the whole history
for every task. Check the live files and Git diff before relying on older notes.

- Current branch: `rev/comst-v3-20260906`. The manuscript has eight main sections;
  Review Methodology is Introduction I-C. Do not restore standalone Section III
  just because an old recipe or memory mentions it.
- Write manuscript prose in English and explain work to the author in Turkish.
  Use readable technical language. Keep new filenames short and links relative.
- Current author instructions and live writing rules supersede historical
  recipes, copied memory, old section numbers and approval states.
- Keep cover-letter claims, journal-fit arguments, internal QA and approval
  bookkeeping outside the scientific manuscript. Preserve truthful methods,
  reporting limitations and reproducibility information in their agreed carriers.
- Preserve study/report/metric/relationship distinctions and original measurement
  conditions. Never turn conditional comparison candidates into verified pooled
  or cross-study results. TQAF is not GRADE or a conventional risk-of-bias tool.
- Preserve user edits and frozen source packages. New scientific content or
  figure work follows the author's task; historical approval is not a blanket
  permission to redraw figures. Retain approved figure assets and editable sources.
- Use local TeX/text and focused searches first. Avoid expensive broad reviews
  without explaining their value to the author; respect the token budget.
- Build from `manuscript/` with
  `latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error main.tex`.
  Use `python handoff/verify.py` from the repository root for transfer integrity.
  A technical PASS does not establish scientific or submission approval.
- The OSF archive update remains an open joint task. A GitHub push does not
  complete it. The current manuscript's author-approved final-state archive
  sentence is not proof that the remote archive has been updated.
- `handoff/history/`, `handoff/prisma/`, `handoff/plans/`, `handoff/style/`, and
  `handoff/rc1/` contain historical records. Read their dates, scopes and caveats.
  Do not execute old scripts or follow old operational instructions blindly.
- Keep account credentials, browser profiles, unrelated personal memories and
  publisher full-text collections outside Git. Maintain project context here;
  do not install or overwrite a global Codex profile from this repository.
