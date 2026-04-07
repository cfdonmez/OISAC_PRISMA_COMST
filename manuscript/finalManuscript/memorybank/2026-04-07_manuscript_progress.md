# Manuscript Progress Memory

Date: 2026-04-07
Repository: `OISAC_PRISMA_COMST`
Working file: `bare_jrnl_new_sample4.tex`

## Completed in this session

- Front matter was converted from the IEEE template to the real manuscript title and three-author block.
- Author affiliations, emails, first-author ORCID, and corresponding-author note were added.
- Figure references in the main body were normalized to automatic `Fig.~\ref{...}` form.
- Table references in the main body were normalized to automatic `Table~\ref{...}` form.
- Long display equations were reformatted into multiline IEEE-friendly layouts where needed.
- References used in the manuscript were checked against `references.bib`.
- Broken bibliography entries were repaired:
  - `O_ISAC_199` replaced with the correct article metadata.
  - `O_ISAC_304` replaced with the correct article metadata.
  - `O_ISAC_166` was removed and its text usage was replaced with the semantically correct cited source.
- Checklist and audit files were created under `kontrol_listeleri/` for:
  - front matter
  - body sections
  - figures
  - tables
  - references and citations
  - equations and math
  - final pass

## Latest table decisions

- In `tab:section7_dualview`, forced multiline row-reference cells were removed so domain rows can stay on one line where possible.
- In `tab:viii_f_1`, the layout was widened so domain rows do not break unnecessarily.
- In `tab:viii_g_1`, the misleading duplicate dual-view table was replaced with a challenge-domain alignment table that matches the surrounding Section VIII-G text.

## Validation state

- Repeated `pdflatex -draftmode` checks completed successfully after the latest table updates.
- Current log state after the latest pass:
  - undefined citations: `0`
  - undefined references: `0`
  - remaining overfull `\hbox`: `24`
  - remaining underfull `\hbox`: `139`

## Current repo intent

- Commit only the manuscript, bibliography, checklist/audit material, and this memory note.
- Leave unrelated image-file modifications and temporary LaTeX byproducts out of the commit unless explicitly requested later.

## Suggested next steps

- Review the remaining non-blocking table typography warnings one by one if visual polish is needed.
- Fill the biography/back-matter section later when final author bios are ready.
