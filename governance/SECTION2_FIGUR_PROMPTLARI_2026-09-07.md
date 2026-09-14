# Section II — dış üretim için figüre özel promptlar

Tarih: 2026-09-07
Durum: Dış üretime hazır üç bağımsız İngilizce prompt. Her kod bloğu tek başına
kopyalanabilir ve amaç, yerleşim, tam etiketler, çizim kuralları, öneri caption
ve üretim sonrası kontrol listesini içerir. Bu dosyanın tamamlanması yeni
görsellerin üretildiği, yerleştirildiği veya doğrulandığı anlamına gelmez.
Mevcut görsel dosyaları değiştirilmemiştir.

Üç görselin görevleri birbirini tamamlar. S2-F1, II-A'da işaret yolunu ve ölçüm
noktasını gösterir. S2-F2, II-B'de zaman ve frekans tahsislerini açıklar.
S2-F3, II-C'de nominal çözünürlüğün bant genişliğiyle değişimini hesapla
gösterir. II-D için ek görsel gerekmiyor. Mevcut sayısal tablo ölçüleri kendi
test koşullarıyla birlikte okumayı, kısıtlı optimizasyon denklemi ise ortak
tasarım değişkenleri altında korunacak hizmet koşullarını açıklıyor.
Doğrulanmış eşlenik işletim noktaları olmadan Pareto eğrisi çizmek yeni bir
bilimsel ilişki uydurmak olur.

| Prompt | Subsection | Mevcut görsel etiketi | Önerilen genişlik |
|---|---|---|---|
| S2-F1 | II-A | fig:joint_evidence_anatomy | Çift sütun, yaklaşık 172 mm |
| S2-F2 | II-B | fig:resource_sharing | Tek sütun, yaklaşık 84 mm |
| S2-F3 | II-C | fig:bandwidth_resolution | Tek sütun, yaklaşık 84 mm |

Ölçüler tasarım önerisidir, IEEE zorunluluğu değildir. Aşağıdaki caption'lar
yeni üretim için öneridir. Makale, mevcut figürlerde henüz bulunmayan yeni
etiketlere veya öğelere atıf yapamaz. Dışarıdan sağlanan görsellerin fiziksel
anlamı, metin uyumu ve sayısal doğruluğu kontrol edilmeden yerleştirme
tamamlandı diye raporlanmaz.

## S2-F1 — Signal paths and measurement locations

```text
Create an original editable scientific schematic for subsection II-A,
"Signal Paths and Sensing Observations", in an optical integrated sensing
and communication survey. O-ISAC means optical integrated sensing and
communication. Its purpose is to connect physical interactions to receiver
observations and measurement locations. Place it after the subsection's
opening explanation of communication and sensing observations, before the
intensity-channel equation. The manuscript reference label for this role is
fig:joint_evidence_anatomy.

Status and layout:
This is a conceptual schematic. It has no axes or numeric data and specifies
no performance units, measured spectra, or distances. Use two horizontal panels
stacked vertically, a white background, simple vector blocks and consistent
line weights. Aim for about 172 mm width and 80 mm height for a two-column
layout. These dimensions are design suggestions, not mandatory IEEE sizes.
Use readable text at final size, preferably at least 8 pt. Keep the two
physical domains and all receiver connections clear when printed in grayscale.

Panel (a) and exact text:
Title this panel "(a) Optical propagation and observation". Arrange these
stages from left to right:
"Optical waveform and front-end"
"Fiber or free-space interaction"
"Detection and processing"

Show an input labeled "Data" and a separate dashed input labeled
"Optional probe or reference" entering the front-end. A dedicated probe is
optional and must not appear mandatory. Draw the principal signal arrows
from the front-end through the interaction to detection and processing.
Place "Physical parameters θ" beside the interaction, with a short arrow
showing that the parameters affect the observation. Typeset θ as a bold
mathematical vector. Add the explanatory text "θ is the physical parameter
vector" in a compact symbol key.

Beside the interaction-to-detection connection, show a compact group headed
"Alternative observation paths" with the exact labels "Forward signal",
"Backscatter", "Reflection", and "Spatial intensity". These are alternatives
chosen for the physical task, not four required simultaneous observations.
Do not force all alternatives through a reflected radar path. If a branch
or return arrow is drawn, it must terminate at an identified receiver in
the detection area.

The detection area must explicitly show "Direct or coherent detection" and
"Shared or separate receivers". These labels identify alternatives. They
must not imply a cascade of direct and coherent detectors, a universal
single receiver, or identical samples for both functions. Branch the
processing outputs into "Data recovery" and "Parameter estimate θ̂".
Typeset θ̂ as the estimate of the same bold vector θ. In the symbol key add
"θ̂ is the estimated physical parameter vector".

Place measurement markers on the signal path with these exact labels:
"Launch power" after the optical front-end.
"Received optical power" before optical detection.
"OSNR where applicable" before optical detection.
"Electrical SNR" after optical detection.
"BER" at the recovered-data output.
The markers identify measurement locations, not additional components.
Add these exact acronym expansions in a compact key or immediately below
the relevant labels, without colon or semicolon punctuation:
"OSNR  Optical signal-to-noise ratio"
"SNR  Signal-to-noise ratio"
"BER  Bit error rate"

Panel (b) and exact text:
Title this panel "(b) Photonics-enabled wireless propagation". Arrange
"Optical tones and modulation", "Photomixing", "mmWave or THz propagation",
and "RF reception and processing" from left to right. Put a visible domain
boundary after photomixing. Label the left domain "Optical generation" and
the right domain "RF propagation and reception". Photomixing is the
representative conversion shown here, not a requirement for every photonic
wireless implementation. If the two optical tones are depicted, label them
f₁ and f₂ and define them with "f₁ and f₂ are optical frequencies". Do not
draw numerical frequency axes or assign unprovided frequencies.

Inside the RF propagation domain, identify "Communication path" and
"Target response path". Connect their observations to the identified
"RF reception and processing" area, which must also carry the label
"Shared or separate receivers". An optional target-response arrow must
reach an explicitly identified sensing receiver within that area. Never
leave a return arrow pointing to a transmitter or radiator alone. Output
"Data recovery" and "Sensing estimate" from the appropriate processing
paths. This is a functional diagram, not a prescribed monostatic geometry.
Include these exact expansions in the key:
"RF  Radio frequency"
"mmWave  Millimeter wave"
"THz  Terahertz"

Arrow and styling rules:
Use solid blue arrows for transmitted signals and recovered-data flow,
dashed green arrows for optional probes or sensing observations, and short
amber arrows for a physical parameter's effect on an observation. Amber
measurement dots may use plain leaders without arrowheads. Include a small
legend with "Signal flow", "Sensing observation", "Parameter effect", and
"Measurement location". Distinguish meanings by line style and labels as
well as color. A branch depicts a possible functional connection, not an
assertion of identical observations or simultaneous tests.

Prohibitions:
Do not depict RF propagation as visible light. Do not equate optical OSNR
with electrical or RF SNR. Do not imply that fiber sensing always uses a
discrete target reflection. Do not add performance numbers, rankings, or
claims that sharing guarantees improvement. Do not add unprovided symbols,
decorative equipment, logos, gradients, or photorealistic scenes. Do not
put colons or semicolons in artwork prose labels or in the proposed caption.

Output:
Deliver editable vector artwork, preferably SVG plus vector PDF, with
editable text and a separate caption. Provide a legible final-size preview
for inspection. Do not insert the artwork into the manuscript or describe
production as complete before the artwork has actually been delivered.

Proposed caption:
Signal paths and measurement locations in representative O-ISAC systems.
Optical propagation and observation are distinguished from optical
generation followed by RF propagation. Alternative sensing observations
and shared or separate receivers determine where the communication and
sensing quantities are measured.

Postproduction checklist:
- Follow every principal arrow from generation through interaction to an
  identified receiver and output.
- Verify that θ affects the interaction and θ̂ labels its estimated value.
- Check that the optional probe and alternative observation paths appear
  optional and that shared resources do not imply identical receivers.
- Confirm that optical power and OSNR markers precede photodetection,
  electrical SNR follows detection, and BER labels recovered data.
- Verify the optical-to-RF boundary and each RF target-response endpoint.
- Check all acronym expansions, exact labels, and grayscale legibility.
- Inspect the artwork and caption for unsupported numerical or superiority
  claims and for colon or semicolon punctuation in visible prose.
- Confirm the actual panel content against the final II-A text before any
  subsequent manuscript insertion.
```

## S2-F2 — Time, frequency and joint-waveform sharing

```text
Create an original editable conceptual diagram for subsection II-B,
"Shared Resources and Optical Signal Constraints", in an optical integrated
sensing and communication survey. O-ISAC means optical integrated sensing
and communication. Its purpose is to explain the geometry of three
resource-sharing choices before the text introduces optical waveform
constraints. Place it after the opening paragraph defining time sharing,
frequency sharing, and a joint waveform. The manuscript reference label
for this role is fig:resource_sharing.

Status and layout:
This is a conceptual resource-allocation schematic, not a measured spectrum
or a comparison of performance. Arrange three equal-size panels from left
to right. Aim for about 84 mm width for a single-column layout, using enough
height to keep text legible. The width is a design suggestion, not a
mandatory IEEE size. Prefer at least 8 pt text at final size. Use a white
background, consistent thin lines and lightly shaded flat rectangles.

Exact panel titles and axes:
"Time sharing"
"Frequency sharing"
"Joint waveform"
Every panel has a horizontal axis labeled "Time t" and a vertical axis
labeled "Frequency f". Axis arrows indicate increasing time to the right
and increasing frequency upward. Include no numerical ticks or physical
units because no particular allocation duration or bandwidth is specified.
The symbols t and f mean time and frequency. There are no measured data.

Panel contents:
In "Time sharing", draw two non-overlapping time intervals occupying the
same schematic frequency range. Label the first rectangle "C" and the
second "S". Under this panel write "Different time slots".

In "Frequency sharing", draw separate frequency bands extending over the
same schematic time interval. Label the lower band "C" and the upper band
"S". Leave a narrow visible gap and identify it using the label "Guard band"
and a plain leader without an arrowhead. Under this panel write
"Separate frequency bands". The guard band belongs to this illustration,
not to every frequency-sharing implementation.

In "Joint waveform", draw one rectangle for the common allocation. Label
it "C + S" and add the second line "One waveform". Under this panel write
"Shared time-frequency allocation". Do not divide this rectangle into two
separate function-specific allocations.

Use blue for communication, green for sensing and purple for the joint
waveform. Add the exact legend text "C  Communication" and "S  Sensing".
The plus sign in "C + S" denotes two functions using the allocation, not an
arithmetic sum of rates or powers. Rectangular outlines and letter labels
must retain the meaning in grayscale. Apart from the axes, this diagram
uses no directional arrows. The guard-band leader only locates a gap.

Interpretation and prohibitions:
The equal plotting areas are a schematic convention. They do not establish
equal occupied bandwidth, unchanged bandwidth after integration, equal
energy, matched experimental conditions, or equal performance. Do not add
measured spectral profiles, numerical allocation ratios, efficiency scores,
ranking arrows, bandwidth savings, Pareto curves, or superiority claims.
Do not imply that every O-ISAC system uses a common waveform. Shared
infrastructure may support any of the three allocations. Do not put colons
or semicolons in artwork prose labels or in the proposed caption. Add no
decorative equipment or icons that obscure the resource geometry.

Output:
Deliver editable vector artwork, preferably SVG plus vector PDF, with
editable text and a separate caption. Provide a legible final-size preview.
Do not insert the artwork into the manuscript or describe production as
complete before the artwork has actually been delivered.

Proposed caption:
Conceptual resource allocations for communication and sensing. Time and
frequency sharing separate their allocations, whereas a joint waveform
uses one allocation for both functions. Equal panel dimensions serve the
illustration and do not assert equal bandwidth or performance.

Postproduction checklist:
- Verify that time separation is horizontal and frequency separation is
  vertical, with axis arrows and t and f labels in the correct directions.
- Confirm that C and S are defined and that the guard-band label locates
  the gap in the frequency-sharing example.
- Check that the joint-waveform rectangle shows a common allocation and
  does not look like two separate resources.
- Confirm the absence of numerical data, physical tick units, measured
  spectral shapes, ranking arrows, and bandwidth-invariance claims.
- Inspect all labels at single-column size and in grayscale.
- Check the caption and artwork prose for colons or semicolons.
- Compare the actual drawing with the final II-B explanation before any
  subsequent manuscript insertion.
```

## S2-F3 — Calculated nominal range resolution

```text
Produce a deterministic mathematical plot for subsection II-C,
"Communication and Sensing Measures", in an optical integrated sensing and
communication survey. Its purpose is to explain how sensing sweep
bandwidth sets the nominal range-resolution scale before the text compares
that scale with estimation error. Place it after the two-way range and
nominal-resolution equation and before the RMSE definition. The manuscript
reference label for this role is fig:bandwidth_resolution.

Status and physical model:
This is an analytical illustration of an ideal bandwidth-limited two-way
measurement in air. It is not experimental data. Use c = 299792458 m/s as
the propagation-speed approximation for air. Do not present that constant
as an exact refractive-index correction. Define Δr as nominal range
resolution and B_s as sensing sweep bandwidth. Typeset the s as a subscript.
The nominal relation is Δr ≃ c / (2 B_s). Generate the plotted curve by
evaluating Δr = c / (2 B_s) under these ideal assumptions.

Unit conversion:
With B_s in GHz and Δr in cm, calculate
Δr (cm) = 14.9896229 / B_s (GHz).
GHz means gigahertz and cm means centimeter. The factor of two represents
two-way propagation. Do not transfer this formula unchanged to fiber.

Exact plotting settings:
Use a single panel and one blue analytical curve. Both axes are logarithmic.
Set the horizontal limits to 0.5 and 8 GHz and the vertical limits to 1 and
40 cm. Set horizontal ticks to 0.5, 1, 2, 4 and 8. Set vertical ticks to
2, 5, 10, 20 and 40. Display those numerical tick labels without scientific
notation. Use major gridlines only and no minor ticks. Use 100 formula
samples over the domain 0.5 to 8 GHz, matching the existing analytical
illustration. Use exact axis labels
"Sensing sweep bandwidth B_s (GHz)"
"Nominal range resolution (cm)".

Verification coordinates:
0.5 GHz gives 29.9792458 cm.
1 GHz gives 14.9896229 cm.
2 GHz gives 7.49481145 cm.
4 GHz gives 3.747405725 cm.
6.2 GHz gives 2.4176811129 cm.
8 GHz gives 1.8737028625 cm.
These coordinates verify the formula. Do not plot them as an experimental
series or add markers at all six coordinates.

Highlight only the calculated point at 6.2 GHz and 2.417681113 cm using a
filled blue marker. Draw a vertical dashed guide from the lower plot limit
at 1 cm to this marker. The guide identifies the selected bandwidth and is
not a measured trajectory. Use no arrowheads. Place the annotation
"6.2 GHz gives approximately 2.4 cm" near the marker, wrapping it over two
lines if needed. An appropriate text anchor is near 5.9 GHz and 3.4 cm.
Place "Δr ≃ c/(2B_s)" near 0.8 GHz and 17 cm without obscuring the curve.
Add the exact analytical-status label "Calculated nominal resolution" in
a clear area of the panel. Do not add a second curve or an inset panel.

Source context:
The 6.2 GHz sweep is the value used in the survey's photonic-THz example
with the existing citation key OISAC_SCR00083. It corresponds to about
2.4 cm under the stated nominal model. That citation key is authoring
metadata and must not be printed as an artwork label. Do not invent a
numbered reference. The final manuscript caption can use the existing
source citation when the actual artwork is inserted.

Prohibitions:
Do not approximate the curve artistically. Use deterministic mathematical
plotting rather than visual imitation. The curve describes a nominal
two-target separation scale, not measured root mean square error (RMSE),
maximum error, or guaranteed practical resolution. Do not plot the source
experiment's 0.55 cm maximum ranging error on this curve. Do not replace the
6.2 GHz sensing sweep by the approximately 36.2 GHz total occupied
bandwidth. Add no experimental points, error bars, confidence bands, fitted
trends, rankings, or fabricated comparison data. Do not put colons or
semicolons in artwork prose labels or in the proposed caption.

Output and readability:
Use a white background, subtle major gridlines and legible typography at
about 84 mm width and 52.5 mm height. These single-column dimensions are
design suggestions, not mandatory IEEE sizes. Prefer text of at least
8 pt at final size and inspect all annotations for overlap. Deliver editable
vector artwork, preferably SVG plus vector PDF, with a separate caption,
the mathematical generation source and the exact formula/settings used.
Provide a final-size preview for inspection. Do not insert the artwork into
the manuscript or describe production as complete before the artwork has
actually been delivered and the numerical checks have been performed.

Proposed caption:
Calculated nominal range resolution for an ideal two-way, bandwidth-limited
measurement in air. The 6.2 GHz marker corresponds to approximately 2.4 cm
and illustrates the separation scale associated with the sensing sweep.
The curve is an analytical calculation rather than measured ranging error.

Postproduction checklist:
- Recalculate the GHz-to-cm coefficient from c/(2B_s) and check all six
  verification coordinates, including the 6.2 GHz marker.
- Verify that both axes are logarithmic and that their limits, tick values,
  tick labels and absence of minor ticks match the specified settings.
- Confirm that the single curve comes from 100 formula samples and that
  the only highlighted point is the calculated 6.2 GHz point.
- Check the dashed guide, the equation annotation, and the analytical-status
  label for correct meaning and unobstructed placement.
- Verify that neither 0.55 cm measured maximum error nor 36.2 GHz occupied
  bandwidth has been substituted for the plotted nominal quantities.
- Check that no experimental points, error bars or fitted trends appear.
- Inspect final-size readability and artwork/caption prose punctuation.
- Match the actual plot and caption to the final II-C text before any
  subsequent manuscript insertion.
```

Bu görevde yalnız prompt dosyası güncellendi. Dış görsellerin üretimi, üretim
sonrası denetimi ve makaleye yerleştirilmesi henüz gerçekleştirilmedi.
