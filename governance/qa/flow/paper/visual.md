# Integrated paper visual QA

Audited source: `manuscript/main.pdf`, 20 pages.

SHA-256: `38b21adb5a55126176d3006ab6f80c059d9c6efd490093b5778a98664ee4a6b0`.

All pages were rendered with Poppler at 110 dpi. Four contact sheets were
reviewed, followed by complete detailed inspection of every figure/table page:
3, 4, 5, 7, 10, 11, 12, 13, 15 and 16. The final-build refresh also inspected
page 14's new equations and page 20's final references. The underlying figures
were inspected in standalone renders at 145 dpi during production.

Five figures and seven tables are legible at their article dimensions. No
clipped elements, overlapping text, black replacement glyphs, or blank body
columns were observed. The baseline's half-empty right column before Section
III is resolved. Searchable word bounds remain within all 20 page canvases.
`page_map.json` and `visual_checks.json` record the exact output checked.

Final-build changes checked:

- Equations (6) and (7), including the complete observation-age sum, fit the
  left column on page 14 without collision or clipping. Their assumptions and
  definitions remain adjacent and readable.
- The Conclusion heading now begins within page 16's right column with its
  full text beneath it. The earlier two-line opening at the left-column foot
  is resolved by content reflow.
- The last page carries references 130-134, leaving substantial unused space.
  There is no wholly blank page. This residual bibliography whitespace does
  not justify another layout intervention within this bounded review.

Caption and topology checks:

- Paths caption distinguishes alternative receiver paths and the LED option;
  optical, RF and electrical/digital colors agree with the drawn signal stages.
- Sharing caption now identifies source/detector icons as the common optical
  link and describes the written Time/Frequency axes correctly.
- Coupling caption cites the three concrete configurations, distinguishes a
  pilot proxy from target estimation error, and avoids pooled trend claims.
- Validation is independently consistent with frozen S7 CSVs: 206 unique
  study rows; highest tiers 2/3/4/5/6 count 32/18/78/66/12. Of 12 field rows,
  six have both-domain outcomes. All 12 relationship-timing fields are NR in
  the audited projection, consistent with the explicit concurrency limitation.

Result: PASS with minor final-reference whitespace. This record covers the
stated PDF hash; a later build must be checked for changed pages before
inheriting this visual QA result.

Final EOF-only rebuild: 19 pages pixel-identical at 110 dpi; page 2 re-inspected with no clipping, collision or poor heading placement. Contact sheets and page renders match the final PDF.
