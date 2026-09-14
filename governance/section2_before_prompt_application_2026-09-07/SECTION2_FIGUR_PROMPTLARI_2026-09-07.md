# Section II — dış üretim için figüre özel promptlar

Tarih: 2026-09-07
Durum: Üç başlangıç tasarım brifi. Bu dosya bir görsel üretimi veya yeni
figürlerin makaleye yerleştirilmesi değildir. Section II revizyonunu yapan ajan,
brifleri nihai metne göre kontrol edip gerekiyorsa güncelleyecektir.
Şimdilik üç ayrı işlev yeterlidir; yeni bir figür ancak ek bilimsel gerekçeyle
önerilir. Her İngilizce prompt diğerlerinden bağımsız kullanılabilir.

Mevcut karşılıklar:
- S2-F1 → II-A → fig:joint_evidence_anatomy
- S2-F2 → II-B → fig:resource_sharing
- S2-F3 → II-C → fig:bandwidth_resolution

Aşağıdaki caption'lar öneridir. Yeni görseller üretilip incelenmeden makalede
varmış gibi kullanılmaz. Bu dosyada yalnız dış üretim brifleri hazırlanır.
Mevcut görsel dosyaları değiştirilmez. Yeni görseller ancak kullanıcı tarafından
sağlandıktan, kontrol edildikten ve ayrı yerleştirme yetkisi verildikten sonra
makaleye alınır.

## S2-F1 — Signal paths and measurement locations

Amaç: Section I'in fiziksel tasarım seçimi katkısını II-A'da teknik olarak açmak.
Üretim, fiziksel etkileşim ve alıcı/ölçüm aşamalarını ayırarak II-B/C'ye bağlanmak.
Önerilen yerleşim: çift sütun genişliği, iki yatay panel. Boyut önerisi yaklaşık
17.2 × 8 cm; kesin IEEE zorunluluğu değildir.

### English production prompt

Create an original, publication-quality scientific schematic for the technical
foundations section of an optical integrated sensing and communication survey.
Use a white background, flat vector shapes, consistent line weights, generous
spacing, and legible typography at approximately 172 mm final width. Use blue
signal-flow arrows, green sensing-observation arrows, and amber measurement
markers. Preserve meaning in grayscale through labels and line styles. No
photorealistic scenes, gradients, decorative equipment, logos, or 3D effects.

Use two clearly separated horizontal panels.

Panel (a), titled "Optical propagation and observation", should show the
logical stages "Optical waveform and front-end", "Fiber or free-space
interaction", and "Detection and processing". Branch the outputs into
"Data recovery" and "Parameter estimate". Show "Data" and an optional
"Probe / reference" input without implying that every implementation requires
a dedicated probe. Place the physical quantity theta at the interaction
stage, with an arrow indicating that it affects the observation.

Add a concise annotation explaining that sensing observations can use
"Forward signal", "Backscatter", "Reflection", or "Spatial intensity".
These are alternative mechanisms, not four mandatory simultaneous paths.
The processing area must allow "Shared or separate receivers" so the drawing
does not claim a universal single-receiver or identical-sample architecture.
Label the detection options "Direct or coherent detection".

Locate "Launch power" after the optical front-end, "Received optical power"
before optical detection, "OSNR, where applicable" at the optical measurement
stage, and "Electrical SNR" after detection. Put "BER" at the data-recovery
output. Measurement markers are observation locations, not extra components.

Panel (b), titled "Photonics-enabled wireless example", should show
"Optical tones and modulation" followed by "Photomixing", then a clearly
separated "mmWave / THz propagation" stage and "RF reception and processing".
Provide "Data recovery" and "Sensing estimate" outputs. Label the two broad
domains "Optical generation" and "RF propagation and reception". Photomixing
is a representative implementation, not a requirement for every photonic
wireless system. Use a generic link/target-response block. Do not draw a
return arrow to a transmitter without identifying the receiving path.

Do not depict THz propagation as visible light. Do not equate optical OSNR
with electrical or RF SNR. Do not imply that fiber sensing always relies on
a target reflection, or that shared resources guarantee joint performance
improvement. Include no performance numbers or rankings.

Deliver editable vector artwork with editable labels, preferably SVG or PDF.
Keep the explanatory caption separate from the artwork.

### Proposed caption

Signal paths and measurement locations in representative O-ISAC systems.
Optical propagation and observation are distinguished from optical generation
followed by RF propagation. The sensing mechanism and receiver architecture
determine where communication and sensing quantities are measured.

### Üretim sonrası kontrol

- Kaynak → fiziksel etkileşim → alıcı yönü anlaşılır mı?
- Optik üretim ve RF yayılımı fiziksel olarak ayrılmış mı?
- OSNR, elektriksel SNR ve BER etiketleri doğru aşamada mı?
- Ortak kaynak ile ortak alıcı/aynı örnekler eşitleniyor mu?
- Ana metin, görselin gerçekten gösterdiği panelleri mi anlatıyor?
- Tek alıcı ya da radar dönüşü bütün platformlara dayatılmış mı?

## S2-F2 — Time, frequency and joint-waveform sharing

Amaç: II-B'de kaynak paylaşımının somut geometrisini öğretmek ve II-D'deki ortak
tasarım değişkeninin anlamına temel oluşturmak. Grafik başarı kıyaslaması değildir.
Önerilen yerleşim: tek sütun, yaklaşık 8.4 cm genişlik, yan yana üç küçük panel.

### English production prompt

Create an original, compact vector diagram for an IEEE-style technical survey
on optical integrated sensing and communication. The figure must explain
three conceptual time-frequency resource allocations, not compare measured
performance. Use a white background, thin consistent axes, flat lightly
shaded rectangles, and readable labels at approximately 84 mm final width.
Use blue for communication, green for sensing, and purple for a shared
communication-and-sensing waveform. Retain C, S, and C+S labels so color is
not the only distinction.

Arrange three equal-size panels from left to right with these exact titles:
"Time sharing", "Frequency sharing", and "Joint waveform".

Every panel has a horizontal axis labeled "Time" and a vertical axis labeled
"Frequency". Use the same conceptual plotting area in all three panels.
Do not include numerical tick values because no measured allocation is being
reported.

In "Time sharing", draw two adjacent, non-overlapping time intervals occupying
the same frequency range. Label the first rectangle "C" and the second "S".
Below the panel write "Different time slots".

In "Frequency sharing", draw two separate frequency bands extending over the
same time interval. Label one band "C" and the other "S". Leave a narrow
visible gap between them and label it "Guard band" with a short leader.
Below the panel write "Separate frequency bands".

In "Joint waveform", draw one rectangle spanning the common allocation and
label it "C + S" with the second line "One waveform".
Below the panel write "Shared time-frequency allocation".

Include a compact legend reading "C  Communication" and "S  Sensing".
Equal panel sizes and illustrative rectangle areas do not establish equal
energy, throughput, sensing accuracy, or experimental conditions.

Do not add ranking arrows, efficiency scores, bandwidth-gain percentages,
Pareto curves, or claims that a joint waveform is always superior. Do not
imply that all O-ISAC systems must use one waveform. Shared infrastructure
can support any of the three illustrated allocations. The guard band belongs
to the displayed frequency-sharing example, not a universal mandatory rule.

Deliver editable vector artwork with editable text. Keep the caption outside
the artwork and avoid decorative icons.

### Proposed caption

Conceptual resource allocations for communication and sensing.
Time and frequency sharing separate their allocations, whereas a joint
waveform uses the same time-frequency allocation for both functions.

### Üretim sonrası kontrol

- Zaman paylaşımında ayrım yatayda, frekans paylaşımında dikeyde mi?
- Ortak dalga biçimi panelinde iki ayrı tahsis varmış izlenimi oluşuyor mu?
- C/S tanımı ve guard band okunabiliyor mu?
- Bir performans üstünlüğü veya sayısal verim iddiası eklenmiş mi?
- Kaynak işgali çizimi ölçülmüş spektrum gibi gösterilmiş mi?

## S2-F3 — Calculated nominal range resolution

Amaç: II-C'de tarama bant genişliğinin nominal iki hedef ayırma ölçeğiyle
ilişkisini öğretmek. Bu, ölçülen hata grafiği değildir.
Önerilen yerleşim: tek sütun, yaklaşık 8.4 × 5.3 cm.

Bu prompt dışarıdaki bir grafik/vektör çizim aracına veya tasarımcıya
verilebilir. Sayısal eğri deterministik olarak hesaplanmalıdır. Bir görüntü
üreticisinin benzer görünen eğri çizmesi matematiksel doğrulama sayılmaz.

### English production prompt

Produce a publication-quality scientific plot for the technical foundations
of an optical integrated sensing and communication survey. Use deterministic
mathematical plotting and editable vector output. Do not approximate the
curve artistically and do not invent experimental data.

Plot the calculated nominal range resolution for an ideal, bandwidth-limited,
two-way measurement in air. Use the propagation-speed approximation
c = 299792458 m/s and the relationship

Delta r = c / (2 B_s).

With B_s expressed in GHz and Delta r expressed in cm, evaluate exactly

Delta r (cm) = 14.9896229 / B_s (GHz).

Use a white background and a single blue line. Both axes are logarithmic.
Set the horizontal limits to 0.5 and 8 GHz, and the vertical limits to 1 and
40 cm. Use horizontal ticks at 0.5, 1, 2, 4 and 8. Use vertical ticks at
2, 5, 10, 20 and 40. Label the axes exactly as follows:
"Sensing sweep bandwidth B_s (GHz)"
"Nominal range resolution (cm)".

Evaluate the curve densely from the formula. For verification, the following
coordinate pairs must lie on the curve:
0.5 GHz gives 29.9792458 cm.
1 GHz gives 14.9896229 cm.
2 GHz gives 7.49481145 cm.
4 GHz gives 3.747405725 cm.
6.2 GHz gives 2.4176811129 cm.
8 GHz gives 1.8737028625 cm.

Highlight only the calculated point at 6.2 GHz with a filled marker and a
subtle guide line. Use the annotation "6.2 GHz gives approximately 2.4 cm".
Place the formula in an unobtrusive area without covering the curve.

Make the analytical status explicit with a small label "Calculated nominal
resolution". Use light major gridlines and readable typography at roughly
84 mm final width. Keep the caption outside the plotting area.

The plot is a nominal two-target separation scale, not measured RMSE,
maximum error, accuracy, or guaranteed practical resolution. Do not add the
0.55 cm maximum ranging error from the source experiment to this curve.
Do not use the 36.2 GHz total occupied bandwidth as the 6.2 GHz sensing sweep.
Do not extrapolate the air-propagation formula to fiber without changing the
physical model. Do not add experimental points, error bars, fitted confidence
bands, or comparison series.

Deliver editable vector artwork and the formula/settings used for generation.
This is an analytical illustration, not an experimental result.

### Proposed caption

Calculated nominal range resolution for an ideal two-way, bandwidth-limited
measurement in air. The 6.2 GHz marker corresponds to approximately 2.4 cm
and illustrates the separation scale associated with the sensing sweep.

Kaynak bağlantısı: 6.2 GHz çapası güncel metindeki OISAC_SCR00083 örneğinden
gelir. Kaynak atfı daha sonra mevcut cite anahtarıyla LaTeX'te eklenir; grafik
üreticisi numaralı kaynak veya deney verisi uydurmamalıdır.

### Üretim sonrası kontrol

- Denklem, GHz/cm dönüşümü ve 6.2 GHz noktası sayısal olarak doğru mu?
- Her iki eksen gerçekten logaritmik mi; tick konumları doğru mu?
- Çizgi analitik hesap olarak mı etiketlenmiş?
- Nominal çözünürlük ile 0.55 cm ölçülen maksimum hata karışmış mı?
- 6.2 GHz tarama bandı, 36.2 GHz işgal edilen bantla değiştirilmiş mi?
- Görselin iddiası güncel II-C metniyle aynı mı?

## Dış üretimden sonraki ortak adım

Kullanıcı görselleri sağladıktan sonra fiziksel anlam, metin/caption uyumu,
etiketler ve varsa sayısal eksenler kontrol edilir. Ardından ayrı yetkiyle
makaleye yerleştirilir. Bu briflerin hazır olması, görsellerin üretilmiş veya
doğrulanmış olması anlamına gelmez.
