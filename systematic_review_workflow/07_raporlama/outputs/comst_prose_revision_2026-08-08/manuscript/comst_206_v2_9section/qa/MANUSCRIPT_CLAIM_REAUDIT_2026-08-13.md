# Manuscript Claim Re-audit — 2026-08-13

## Sonuç

**Durum: `PASS_AFTER_CORRECTION`**

V2 manuscript içindeki abstract ve Sections I–IX, önceki QA sonuçlarına güvenilmeden aktif prose düzeyinde yeniden denetlendi. Sayısal ifadeler kanonik Phase C–F artefaktlarıyla uzlaştırıldı; kaynak-iddia uyumu, denominator birimi, nedensellik, evrensellik, yenilik, yöntem yürütümü ve bölümler arası tekrar ayrıca kontrol edildi. Denetim sırasında bulunan yüksek, orta ve düşük önem düzeyindeki sorunlar güvenli biçimde düzeltildi.

Kanonik artefaktlarla uzlaştırma sonrasında manuscript içinde düzeltilmemiş bir sayı veya denominator hatası kalmadı. Bununla birlikte bu sonuç, 206 makalenin PDF'lerinin bu görev kapsamında baştan sona yeniden okunmuş olduğu anlamına gelmez; denetim locked extraction, appraisal ve synthesis artefaktlarına ve manuscript'te kullanılan kaynak örneklerinin claim-level kayıtlarına dayanır.

## Kapsam ve bilimsel otorite

Denetlenen dosyalar:

- `sections/00_ABSTRACT.tex`
- `sections/01_INTRODUCTION.tex`
- `sections/02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex`
- `sections/03_REVIEW_METHOD_AND_EVIDENCE_BASE.tex`
- `sections/04_OPTICAL_PLATFORMS_AND_INTEGRATION_ARCHITECTURES.tex`
- `sections/05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex`
- `sections/06_VALIDATION_REPRODUCIBILITY_AND_BENCHMARK_READINESS.tex`
- `sections/07_ENABLING_TECHNOLOGIES_APPLICATIONS_AND_6G.tex`
- `sections/08_DISCUSSION_ROADMAP_AND_LIMITATIONS.tex`
- `sections/09_CONCLUSION.tex`

Bilimsel otorite sırası:

1. Phase C final PRISMA flow report, count CSV ve alias crosswalk.
2. Locked Phase D survey-ready workbook; özellikle Study Master, Evidence Items, Metric Results, Tradeoff Evidence ve Survey Claim Ledger.
3. Phase E TQAF summary, dimension audit, normalization crosswalk ve rule-producing code.
4. Phase F final synthesis JSON ve S1–S7 CSV'leri.
5. Context bibliography ve related-synthesis audit yalnız prior-synthesis positioning için.

76 COMST makalesi yalnız anlatım dili ve manuscript mimarisi için referans kabul edildi; hiçbir bilimsel sayı, mekanizma veya sonuç için içerik otoritesi olarak kullanılmadı.

## Bulgular ve düzeltmeler

### Yüksek

| ID | Bulgu | Sonuç |
|---|---|---|
| H1 | Abstract, corpus'taki integration coding'i üç örüntüye indiriyor ve link/channel, carrier, joint design ile application-scenario mekanizmalarını dışarıda bırakıyordu. | Yedi kanonik coupling konumu hiyerarşi kurmadan ve non-exhaustive bir cümleyle temsil edildi. |
| H2 | Sections IV, V ve VIII'de bazı cümleler observational narrative synthesis'i nedensel bir mekanizma veya causal chain gibi sunuyordu. | İfadeler “reported/coded coupling mechanism”, “associated relationship” ve bounded survey inference olarak yeniden kuruldu; causal estimation iddiası kaldırıldı. |

### Orta

| ID | Bulgu | Sonuç |
|---|---|---|
| M1 | “Integration ladder”, “weaker sharing” ve “tighter coupling” dili, multilabel ve non-hierarchical taxonomy ile çelişiyordu. | Ladder ve strength sıralaması kaldırıldı; location, purpose ve shared-element kapsamı kullanıldı. |
| M2 | Bazı platform cümleleri prevalence, dominance veya bütün aileye yayılan fiziksel sonuç izlenimi veriyordu. | “In the reviewed evidence/configurations/cases” sınırları eklendi; `prevalence` ifadesi `within-corpus coverage` olarak düzeltildi. |
| M3 | Reviewer-boundary metni “user delegation” diliyle investigator conduct ve AI assistance sınırını belirsiz bırakıyordu. | Yürütüm investigator-supervised, AI-assisted ve recorded-governance altında bounded claim-level adjudication olarak açıklandı; independent duplicate review yapılmadığı korunarak belirtildi. |
| M4 | Section VIII, prior syntheses ile sonuç karşılaştırması içermiyordu. | Architecture-centered, medium-specific, model-centered ve deployment-centered prior syntheses ile dört tematik karşılaştırma eklendi. Toplam sekiz citation-key kullanıldı; primary corpus ile contextual reviews karıştırılmadı. |
| M5 | Abstract ve conclusion, artifact erişilebilirliğini “reusable” ve joint operation kapsamını gereğinden geniş anlatıyordu. | Artifact cümlesi source-reported open status ile sınırlandı; joint evaluation study-specific settings altında ifade edildi. |
| M6 | Bazı sonuç ve roadmap cümleleri survey inference olduğunu açıkça göstermiyordu. | “Within this framework”, “within this synthesis”, “on this evidence” ve “across the reviewed evidence” sınırları eklendi. |

### Düşük

| ID | Bulgu | Sonuç |
|---|---|---|
| L1 | Introduction'ın ilk teknik örnekleri içindeki turbulence ifadesinin citation fit'i yeterince doğrudan değildi. | Fiber sensing, visible-light positioning ve turbulence-aware optical link örnekleri doğrudan ilgili üç primary study ile eşleştirildi. |
| L2 | Discussion ile conclusion'ın açılış paragrafları aynı ana çıkarımı benzer sözcüklerle tekrar ediyordu. | Conclusion, integration location ile comparability'yi iki ayrı karar olarak kuracak şekilde yeniden yazıldı; cross-file Jaccard taramasında eşik üstü tekrar kalmadı. |
| L3 | “Answer”, “clear reporting therefore”, “portability was weaker” ve benzeri kesinlik taşıyan geçişler, rule-derived score ile scientific quality'yi karıştırabiliyordu. | Metin review-specific rule ve recorded evidence contribution sınırlarına çekildi. |

Section VI denetlendi ancak substantive hata bulunmadığı için değiştirilmedi. Diğer dokuz section dosyasında yalnız yukarıdaki güvenli düzeltmeler uygulandı.

## Sayı ve denominator uzlaştırması

Aşağıdaki ana ilişkiler kanonik artefaktlarla eşleşti:

- PRISMA flow: 1,733 identified; 1,259 screened; 330 unique reports sought; 58 not retrieved; 272 full texts assessed; 227 eligible reports; 206 unique studies; 67 contextual records.
- Phase D governed evidence model: 8,306 records = 3,041 evidence + 4,861 metric + 404 tradeoff; use partition = 3,206 qualitative + 4,997 quantitative + 31 context + 72 quarantine.
- Phase F primary synthesis: 8,203 records = 3,020 evidence + 4,779 metric + 404 tradeoff-ledger rows; iki absence sentinel çıkarıldığında 402 substantive tradeoff record ve 168 study.
- Canonical modality: 69 photonics-assisted THz + 56 fiber + 38 VLC/LiFi + 31 FSO + 9 hybrid + 3 other = 206.
- Integration counts multilabel olarak 118/117/113/87/72/49/46 ve 3 mixed; toplanmaması manuscript'te açık.
- Metric-domain records: 1,816 sensing; 1,328 communication; 870 joint; 476 implementation. The 4,779 comparison roles comprise 118 record-specific bounded cross-study relations under aligned conditions and 4,661 native-context interpretations.
- Substantive tradeoff partition: 218 quantitative + 184 qualitative = 402; 371 conditional = %92.3.
- Maximum validation maturity: 32/18/78/66/12 = 206. Validation methods multilabel olarak 131/14/104/13/148/83/12/33.
- Reported artifact status: data 145/41/13/7; code/model 197/7/1/1 = 206.
- Phase E TQAF study-level ve 115-body distributions manuscript'teki değerlerle eşleşti.
- Technology, application ve 6G relevance sayıları Phase F S6–S7 tablolarıyla eşleşti; bunların within-corpus coverage olduğu açık tutuldu.

Regex tabanlı headline-count regression seti **26/26 PASS** verdi.

## Citation, yapı ve tekrar QA

- Citation-key use: 182.
- Unique citation key: 103.
- Undefined citation key: 0.
- Label: 14; duplicate label: 0.
- Ref/eqref/autoref: 22; unresolved reference: 0.
- Section commands: 9; subsection commands: 29; subsubsection commands: 18.
- On section dosyasının tümünde aktif metin brace sayıları dengeli.
- Cross-file paragraph similarity: 185 prose block test edildi; Jaccard >= 0.30 hit: 0.
- Stale-claim taraması: `Three integration patterns`, `integration ladder`, `causal sequence`, `causal mechanisms`, `one causal chain`, `Tighter coupling`, `sharing cable is weaker`, `Most rely`, `widely under`, `76 COMST`, `openly reusable` ve belirsiz `indicate prevalence` ifadeleri bulunmadı.
- Conflict marker: 0.
- Manuscript citation key'lerinin tamamı mevcut iki bibliography dosyasında tanımlı. Primary-study örneklerinin identity ve claim fit'i Phase D Study Master ile ilgili evidence/metric/tradeoff kayıtlarına karşı kontrol edildi.

Mohsan et al. için DOI `10.1016/j.osn.2026.100854` metadata'sı 13 Ağustos 2026'da ayrıca kontrol edildi. Crossref ve Elsevier core metadata yalnız September 2026 cover date sağladı; ayrı bir official first-online field sağlanmadı. Bu nedenle Table I notundaki “issue date is not used to establish precedence” sınırı korundu.

## Kapsam dışı veya açık kalan işler

- PRISMA Item 17 için 206/206 included-study citation completeness bu görevin konusu değildir; ayrı Item 17 hattı tarafından yürütülmektedir.
- Bu görev, locked extraction ve synthesis artefaktlarının manuscript'e doğru aktarımını denetledi; 206 PDF'nin tamamını sıfırdan yeniden çıkarmadı.
- Bibliography, supplements, visual contract, durable project logs ve memory bank değiştirilmedi.
- Figure/table taslakları ve supplement artefaktları materialize edilmedi.
- Kullanıcı talimatı doğrultusunda LaTeX derlemesi yapılmadı.
