# Flow figure production and QA

Four original vector illustrations replace the selected baseline explanatory
figures. The source is `figures.py`; its primitive geometry emits both editable
SVG text/shapes and searchable PDF with embedded Arial / Arial Bold. No image
generation, raster icon assets, downloaded content, or manuscript build was used.

| Asset | Width x height (pt) | Minimum type (pt) | Function |
|---|---:|---:|---|
| paths | 516 x 358 | 7.5 | Physical signal routes, receiver alternatives and measurement planes |
| sharing | 516 x 185 | 7.5 | Three allocations and their distinct design constraints |
| coupling | 516 x 240 | 7.5 | Two allocation costs and a sensing-guided feedback benefit |
| validation | 516 x 199 | 7.5 | Exclusive highest settings and nested both-domain field reporting |

`dimensions.json` records source bounds. `figures_checks.json` records output
dimensions, PDF and SVG hashes, searchable text, embedded fonts, zero raster
objects and successful SVG parsing. Standalone PNGs were rendered with Poppler
at 145 dpi and inspected. The paths figure was corrected to separate its local
oscillator lead and coherent-receiver annotation, and to move the photomixing
label off the optical-reference lead. All four final renders have legible
labels and no observed clipping or text/line collisions.
The concrete VLC steering row in `coupling` also uses an optical source,
lens and directed light rays; the earlier generic antenna icon was removed.

Scientific scope retained:

- `paths`: laser/modulator, fiber and free-space alternatives, direct/coherent
  receiver alternatives, then a distinct photonic-to-RF path. Green remains
  optical, blue RF, navy electrical/digital and amber a measurement plane.
  Caption must describe an intensity-driven LED as an alternative transmitter;
  the figure does not claim all optical transmitters use a laser/modulator.
- `sharing`: conceptual dimensions do not assert equal occupied bandwidth,
  delivered rates, or equal sensing performance.
- `coupling`: the root's reviewed illustrative cases are SCR00007 (fixed-grid
  pilot allocation, pilot-error proxy rather than target error), SCR00057
  (probe-power change at fixed communication launch power) and SCR00196
  (estimated position feeds illumination steering). The proxy is deliberately
  described as changing, without an unverified direction. The last row does
  not claim improved localization error or a same-run joint gain. References
  and full conditions belong in the manuscript caption and adjacent text.
- `validation`: 32 + 18 + 78 + 66 + 12 = 206. The 12 field/deployment studies
  contain six with reported outcomes in both domains. This is not a statement
  of concurrent operation. It uses a nested set panel, not a second bar scale.

Root requested and reviewed the revised physical/coupling design. This record
documents technical and visual QA, not independent scientific author approval.
The completed assembled-manuscript review is recorded in `paper/visual_checks.json`.
