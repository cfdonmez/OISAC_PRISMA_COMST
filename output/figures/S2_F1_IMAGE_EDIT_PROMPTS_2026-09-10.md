# Section II-A icon figure correction

Date: 2026-09-10
Method: Built-in imagegen, two targeted image edits.
Source: C:/Users/fatih/AppData/Local/Temp/codex-clipboard-37bc06fe-0142-4953-bf0f-7122f0d8edc7.png
Output: S2_F1_SIGNAL_PATHS_CORRECTED_2026-09-10.png

The output is a raster PNG. No editable vector artwork was generated. The figure is saved separately for review and has not been inserted into the manuscript.

## Initial edit prompt

```text
Use case: precise-object-edit.
Edit target: the supplied two-panel scientific icon diagram. Make a surgical edit of this image, preserving its existing icons, all panel titles, white background, aspect ratio, layout, typography, and all other labels and connections. Do not redesign the figure.

Apply exactly these three corrections.

1. In the UPPER panel (a), the LOWER photodetector in the "Coherent option" branch currently has no output connection. Add a dark gray electrical connector from the RIGHT side of this lower photodetector to the BOTTOM input of the existing "Processing" chip directly above/right. Use a short horizontal segment followed by an upward vertical segment with an arrowhead entering the Processing chip. Keep this connection inside the optical-reception enclosure, clear of text. The upper direct-detection input already connected to Processing must remain. The word "or" must remain, so these are alternative receiver modes, not two simultaneously summed signals.

The amber "Electrical SNR" dot and its label currently sit only on the direct-detection branch. Remove that dot, leader and label from the direct-only segment, leaving the electrical connector intact. Place one amber "Electrical SNR" measurement dot on the COMMON dark gray electrical OUTPUT line immediately after the Processing chip and before that line splits toward Data recovery and Parameter estimate. Put its label and a short leader in nearby clear space with no collisions. This shows the electrical SNR measurement location for either receiver mode. Preserve the separate BER dot on the data branch.

2. In the LOWER panel (b), recolor ONLY the dark gray connector from the COMMUNICATION receiving antenna to the "Communication receiver" chip to the same RF BLUE used on the sensing antenna-to-receiver connector directly below. Thus BOTH receiving-antenna-to-receiver connections are RF blue. Both receiver-chip-to-output connections remain dark gray. Do not change optical green paths, blue wireless paths, or the legend.

3. In the UPPER panel coherent branch, replace the label "Local oscillator (optional)" with exactly "Local oscillator", arranged on two lines if needed. Remove "(optional)" completely. Preserve the local-oscillator icon and its dashed green optical connection to the optical mixing symbol.

Preserve everything else in the original image. In particular preserve the two alternative optical paths and their complete connections, all five measurement labels, the direct communication path bypassing the target, the reflected target path, the optical reference-tone input to photomixing, and the existing connector legend.

Render crisp, clean engineering lines and readable English lettering. Keep arrowheads and line weights consistent with the existing figure. Do not add explanatory paragraphs, callouts about the edit, extra hardware, new colors, watermarks, shadows or decorative elements. Deliver the corrected diagram alone.
```

## Targeted connector correction

```text
Use case: precise-object-edit. The input image is the edit target. Make ONE tiny local correction in the upper panel's optical reception area, preserving all other pixels, labels, colors, icons and connections.

There is a newly drawn dark-gray L-shaped electrical connector from the LOWER coherent photodetector right edge upward toward the existing Processing chip. Its arrow currently stops beneath the word "Processing", so it DOES NOT actually reach the chip. Correct that endpoint.

Move the text label "Processing" to an empty nearby location to the LEFT or RIGHT of the vertical connector, remaining clearly associated with the same chip and not touching any line. Then EXTEND the vertical dark-gray connector upwards until its arrowhead TOUCHES a BOTTOM INPUT PIN of the existing Processing chip. The photodetector output and the chip input must form one continuous visibly connected electrical path. It must not end at text, at an invisible boundary, or in empty space. Keep the top direct-detection input connected to the same chip and keep the word "or" between the alternative receiving modes. Do not draw a connector across any text.

Preserve the amber Electrical SNR point on the common output after Processing and before the data/sensing split. Preserve the corrected blue RF line between communication receiving antenna and receiver. Preserve "Local oscillator" without "(optional)". Preserve all other content, panel layout, aspect ratio, font style, icon positions, line weights and colors. No redesign or extra hardware. Return only the corrected full image.
```

