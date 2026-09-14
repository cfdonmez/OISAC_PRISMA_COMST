# QA ve Kabul Planı — Dengeli Revizyon

## Bilimsel kanıt QA

- Seçilen kayıt sayısı 30--40; hedef 34--36.
- Her kayıt için Reviewer A ve B tamamlanmış.
- Uyuşmazlıkların %100'ü adjudicated; unresolved = 0.
- Source PDF SHA-256 ve locator mevcut.
- Value/operator/range/unit kaynakla tam eşleşiyor.
- Study/report lineage çözülmüş; companion report çift sayılmıyor.
- Yeni ana metin sayısal iddialarının %100'ü traceability crosswalk'ta.
- Uyumsuz platformlar arasında doğrudan sıralama yok.

## Lessons-learned QA

Sections IV--VII'nin her biri aşağıdaki dört alanı en az bir kez taşır:

1. observed/learned pattern;
2. validity condition;
3. limit or tradeoff;
4. design/research implication.

Bu alanlar başlık eklemekle değil, bölümün bilimsel akışı içinde görünür olur.

## Roadmap QA

Beş önceliğin her biri şu alanları doldurur:

`gap, insufficiency, hypothesis, experiment, baseline/control, stress sweep,
success measure, artifact/dependency`.

Genel “AI kullanılabilir”, “benchmark gerekir” veya “daha fazla çalışma
yapılmalı” cümlesi tek başına PASS sayılmaz.

## Reader-value QA

Manuscript'i yazmayan en az bir teknik okuyucu beş soruluk testi uygular. Ana
metin başarı eşiği 4/5; yeni sayısal iddianın supplement trace başarısı %100'dür.

## Build ve görsel QA

- Clean LaTeX build exit 0.
- Undefined citation/reference, fatal error, overfull box veya broken float yok.
- PDF <=30 çift sütun sayfa.
- Tüm sayfalar render edilir ve clipping, overlap, unreadable label, broken
  table ve caption separation açısından incelenir.
- Figürler renk olmadan da ayrıştırılabilir.
- Cross-references, table/figure numbering ve bibliography yeniden denetlenir.

## Stale QA kuralı

Kaynak `.tex`, table, figure veya bibliography değiştiğinde eski PASS o dosya
için geçerli sayılmaz. Release QA yeni source hash ve yeni PDF hash ile bağlanır.

