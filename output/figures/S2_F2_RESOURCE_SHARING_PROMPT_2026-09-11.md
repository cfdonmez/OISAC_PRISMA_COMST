# Figure 3 / S2-F2 production prompt

Date: 2026-09-11
Mode: built-in image_gen, new figure using the approved Figure 2 as a style reference.
Output: raster PNG. Intended manuscript location: Section II-B, fig:resource_sharing. Designed for approximately 172 mm full text width so the three panels and icons remain readable.

## Exact prompt

```text
Use case: scientific-educational.
Create a NEW high-quality publication figure for an optical integrated sensing and communication survey. Use the supplied image only as a STYLE REFERENCE for the navy typography, crisp thin outlines, white background, and recognizable data-document and target-reticle icons. Do not redraw its signal path diagram. This new figure explains time-frequency resource allocation.

Output a wide landscape raster illustration at the highest available resolution, approximately 2400 by 1000 pixels, aspect ratio around 2.4:1. Design for about 172 mm printed width with readable typography, minimum small text about 42 pixels at 2400-wide. Make it look professionally assembled in draw.io from clean flat vector symbols. Pure white background, no textures, gradients, shadows, 3D, photo effects, watermark, outer border or global title. Three equally sized panels left-to-right, balanced spacing, same chart dimensions. Subtle short light-gray vertical separators only BETWEEN panels if helpful. Use Arial/Helvetica-like sans-serif; bold navy panel headings.

Scientific meaning: This is a conceptual allocation diagram, not data, measured spectra, physical waveforms, a device block diagram or a performance comparison. Axes have no numeric ticks, units or grids. Every panel MUST have a horizontal navy arrow axis pointing RIGHT with exact label "Time t", and a vertical navy arrow axis pointing UP with exact label "Frequency f". Rotate Frequency f 90 degrees and place left of its axis with clear spacing. Keep axes and all labels outside the allocation areas. Rectangle areas below are essential time-frequency allocations, not equipment boxes. All three charts have identical schematic extents.

Panel 1 exact heading "(a) Time sharing".
Inside the axes draw TWO tall nonoverlapping allocation rectangles side by side. Both rectangles have EXACTLY the same bottom and top frequency bounds. Left rectangle is communication with a pale blue flat fill and medium-blue outline. Right rectangle is sensing with pale green flat fill and green outline. Leave a narrow horizontal gap between them. In the blue area place a real recognizable outline data-document icon with a folded corner and a tiny "01" bit pair, and a clearly separated large letter "C" below the icon. In the green area place a real recognizable concentric target-reticle icon with four crosshair ticks and a clearly separated large letter "S" below it. Center each icon and its letter inside its allocation. Do not add arrows between allocations. Under the chart write exact text "Different time slots".

Panel 2 exact heading "(b) Frequency sharing".
Inside the axes draw TWO wide nonoverlapping allocation rectangles one above the other. Both have EXACTLY the same left and right time bounds. Lower rectangle is blue for C, upper rectangle green for S, matching panel 1. Keep a clearly visible white horizontal strip BETWEEN the two bands. In the lower band place the same small data-document icon and large letter "C" alongside it, centered as a group; in the upper band place the same target-reticle icon and large letter "S" alongside it, centered as a group. These icons must not encroach on the gap. To the RIGHT of the chart, put the exact two-line label "Guard band" with a short plain horizontal leader pointing into the white gap from the right. The leader has NO ARROWHEAD and MUST end IN the white gap, not inside either band. Reserve space for this label so it does not run into the next panel or any axis. Under the chart write exact text "Separate frequency bands", wrapping into two balanced lines if necessary.

Panel 3 exact heading "(c) Joint waveform".
Inside the axes draw exactly ONE uninterrupted large allocation rectangle with a pale lavender flat fill and a purple outline, spanning the chart's schematic time and frequency range. There must be NO internal subdivision, no two-color split, no seam, and no separate rectangles inside it. In its upper middle place the data-document and target-reticle outline icons side by side as a compact pair, both in purple, with NO boxes around the icons and NO connecting arrows. Beneath the icon pair place a large centered exact label "C + S". Beneath that place the exact text "One waveform". Under the chart write exact text "Shared time-frequency allocation", wrapped into two balanced lines if necessary.

Use sufficient row height so band icons and text are legible and spacious. Keep all three panel headings aligned along the top and all horizontal axes on the same baseline. Panel underlines/explanatory texts occupy a consistent height.

One compact centered legend along the bottom, separated by a fine pale gray horizontal rule. Include a small blue data-document icon followed by exact text "C  Communication", and a small green target-reticle icon followed by exact text "S  Sensing". On a separate centered footer line use exact text "Conceptual allocations only". Legend text dark navy. Use only these two functional icons throughout; do not invent circuit devices or decorative antennas, cars, lasers, buildings, clocks or pseudo-scientific squiggles.

Critical checks before finalizing: in (a) separation is along time and equal frequency extents; in (b) separation is along frequency, equal time extents, white guard-band gap; in (c) exactly one shared unpartitioned resource area. Icons supplement labels and must not replace them. All linework is sharp, consistent and has orthogonal geometry. Reproduce all text exactly, avoid colons and semicolons. Never add numerical values, bandwidth savings, efficiency rankings, superiority claims, wave spectra, signal propagation arrows or experimental results. Equal panel sizes do not imply equal actual bandwidth, energy or performance. Keep all margins and labels uncut.
```

## Proposed manuscript caption

Conceptual time-frequency allocations for communication and sensing. Panel (a) assigns different time slots to the two functions. Panel (b) assigns separate frequency bands, with a guard band shown in this example. Panel (c) uses one waveform within a shared allocation. The axes t and f denote time and frequency, and C and S denote communication and sensing. Icons identify the functions, while rectangles indicate allocated resources. Equal panel dimensions serve the illustration and do not assert equal bandwidth or performance.

The colors in this figure identify communication, sensing, and joint allocation, as defined by its own labels. They do not carry the optical/RF signal-domain meanings used in Figure 2.
