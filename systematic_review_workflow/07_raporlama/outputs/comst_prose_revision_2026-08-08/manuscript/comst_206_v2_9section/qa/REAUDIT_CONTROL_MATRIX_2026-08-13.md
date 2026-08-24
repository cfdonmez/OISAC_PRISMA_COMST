# O-ISAC Survey Tam Yeniden Denetim Kontrol Matrisi

Tarih: 2026-08-13  
Durum: `IN_PROGRESS`  
Amaç: Önceki `PASS` etiketlerinin yalnızca ölçtükleri dar kontroller için geçerli
olduğunu kabul ederek, dokuz bölümlü yeni survey adayını bilimsel kapsam,
PRISMA 2020 raporlaması, bibliyografik tamlık, iddia desteği ve yayın üretimi
açısından yeniden denetlemek.

## Otorite ayrımı

- Kilitli Phase C--F artefaktları bilimsel kapsam, payda, sınıflandırma ve
  provenance için tek otoritedir.
- Yayımlanmamış 220/221 çalışmalık eski manuscript yalnız tarihsel kayıttır;
  yeni survey için veri veya bilimsel karar otoritesi değildir.
- Yerel 76 IEEE Communications Surveys & Tutorials makalesi yalnız anlatı
  dili, bölüm mimarisi, tablo/şekil işlevi ve yayın sunumu için karşılaştırma
  kümesidir. Bu makaleler O-ISAC kapsamını, dahil edilecek kaynakları veya
  PRISMA yükümlülüklerini belirlemez.
- Önceki QA dosyalarındaki `PASS`, aşağıdaki tüm kapıların geçtiği anlamına
  gelmez. Yeni bütünleşik kapı tamamlanmadan aday `submission-ready` olarak
  adlandırılamaz.

## Zorunlu kapılar

| Kapı | Soru | Başarısızlık ölçütü | Düzeltme çıktısı |
| --- | --- | --- | --- |
| K1 Kanonik evren | 227 uygun rapor doğru biçimde 206 benzersiz çalışmaya mı bağlanıyor? | Raporun çalışma gibi sayılması, 232 public lineage satırının filtresiz kullanılması veya 221 predecessor ile attrition kurulması | 206 çalışma ve filtrelenmiş 227 rapor için ayrı journal carrier ve join QA |
| K2 PRISMA 2020 | 42 madde, alt öğeleriyle birlikte manuscript ve gerçek artefaktlarda karşılanıyor mu? | Açık/kısmi bir maddeye `PASS` verilmesi veya planlanan artefaktın mevcutmuş gibi sunulması | 42 satırlı güncel durum matrisi, eksiklerin metin/artefakt düzeltmesi |
| K3 Item 17 | Dahil edilen 206 çalışmanın her biri gerçek bir bibliyografik atıf ve özellik kaydıyla görünür mü? | Birincil çalışma anahtarının bibliyografyada görünmemesi, yalnız `\nocite{*}` kullanılması veya study-characteristics bağlantısının kurulmaması | Materyalize ST-01, 206/206 citation-key gate, 206-key reference inclusion |
| K4 Report lineage | Companion raporlar kaybolmadan, bağımsız çalışma gibi çift sayılmadan gösteriliyor mu? | 227 raporun 206 çalışma olarak uzlaştırılamaması ya da companion rapor kimliklerinin kaybolması | 227 satırlı filtrelenmiş lineage supplement ve 21 rapor azalımının doğrulanması |
| K5 İddia desteği | Her teknik, nicel, nedensel, karşılaştırmalı ve yenilik iddiası uygun kanıtla bağlı mı? | Yanlış DOI/başlık, modality-mismatch, koşulsuz üstünlük, kanıtsız evrensel/ilk iddiası veya payda kayması | Cümle düzeyi claim audit; güvenli metin ve atıf düzeltmeleri |
| K6 Payda güvenlik duvarı | Search record, report, study, claim, metric, tradeoff, TQAF row ve evidence body ayrılıyor mu? | Birimlerin sessizce birbirinin yerine kullanılması | Otomatik payda kontrolleri ve her karma kullanım için açık mapping |
| K7 Individual results | Her çalışmanın sonuçları ve appraisal bilgisi reader-facing supplementte izlenebilir mi? | 4,861/4,779 metric, 404/402 tradeoff, 206 TQAF veya 115 body artefaktına final pointer olmaması | Sanitized journal carriers, final labels ve manuscript pointers |
| K8 Yöntem doğruluğu | Fiilen yapılan reviewer/AI, retrieval, registration ve synthesis süreci olduğu gibi mi yazılıyor? | Prospective-registration, independent duplicate review, tam retrieval exhaustion, formal bias/sensitivity veya author-contact gibi yapılmayan işlem iddiası | Methods ve limitations düzeltmesi; 24c deviation uzlaştırması |
| K9 Survey bütünlüğü | Metin bir audit raporu değil, teknik bir O-ISAC survey olarak mekanizma, koşul, kanıt ve tasarım çıkarımı üretiyor mu? | PRISMA'nın bilimsel hikâyeyi bastırması, çalışma katalogu, tekrar veya sonuçsuz sınıflandırma | Survey-first bölüm akışı ve tematik sentez; PRISMA ayrıntısı yöntem/supplementte |
| K10 COMST sunumu | Dil, bölüm akışı, tablo ve şekil işlevleri hedef derginin survey pratiğiyle uyumlu mu? | COMST örneklerinin bilimsel kapsam otoritesi yapılması, gereksiz bölüm parçalanması veya görsel/metin tekrarı | 9 bölümlü yapı; işlevsel visual carrier sözleşmesi; prose-only style comparison |
| K11 Bibliyografik kalite | DOI, başlık, yazar, venue ve yıl eşleşmeleri doğrulanmış mı? | Duplicate DOI, unresolved key, placeholder author veya yanlış eser kimliği | 206 primary + kullanılan contextual/method kaynaklarının metadata QA'sı |
| K12 Release sınırı | Lisans, hak sahibi, DOI/repository ve public package durumu dürüst mü? | Draft staging'in released sayılması, publisher PDF'lerinin dağıtılması veya tamamlanmamış lisansın kesin gösterilmesi | Açık blocker listesi; yalnız sanitized artefaktlar; author decision gereken maddeler |
| K13 Üretim durumu | Planlanan ve materyalize edilen görseller, tablolar ve supplementler ayrılıyor mu? | Blueprint'in gerçek Figure/Table/Supplement diye referanslanması | Stable ID, status, existence, checksum ve manuscript-reference gate |
| K14 QA kapsamı | Her `PASS` etiketi tam olarak neyi ölçtüğünü ve neyi ölçmediğini söylüyor mu? | Dar regex/count kontrolünün bilimsel doğruluk veya submission readiness olarak yorumlanması | Katmanlı sonuç: science, reporting, bibliography, production ve release için ayrı durum |

## Yeni sonuç sözlüğü

- `PASS`: Yalnız adı verilen kapının bütün zorunlu kontrolleri geçti.
- `PASS_WITH_DOCUMENTED_LIMITATION`: Kontrol tamamlandı; sınır manuscriptte açıkça
  raporlandı ve sonuç o sınırı aşmıyor.
- `READY_FOR_AUTHOR_REVIEW`: Bilimsel/metinsel paket insan okumasına hazır;
  production veya release işleri kalabilir.
- `OPEN`: Düzeltilebilir iş henüz yapılmadı.
- `AUTHOR_DECISION_REQUIRED`: Hak sahibi, lisans, CRediT veya opsiyonel ORCID
  gibi kanıttan otomatik çıkarılamayan karar gerekir.
- `BLOCKING`: Yanlış iddia, eksik zorunlu artefakt veya çözülmemiş veri
  bütünlüğü sorunu vardır.
- `NOT_SUBMISSION_READY`: Görsel, supplement, front matter, repository veya
  rendered-layout kapılarından en az biri açıktır.

## Önceki QA'nın bilinen kapsam sınırları

1. `FINAL_MANUSCRIPT_INTEGRITY_QA` dosya yapısı, etiket, brace ve citation-key
   çözümünü ölçtü; 206 çalışmanın tamamının atıflanmasını veya cümlelerin doğru
   çalışmayı cite etmesini ölçmedi.
2. `FINAL_EVIDENCE_ASSERTION_QA` seçilmiş 14 sayı/ifade ailesini ölçtü; PRISMA
   42-item compliance, full citation coverage, study-characteristics ve tüm
   sentence-level claim support kapsam dışındaydı.
3. `FINAL_SURVEY_ARCHITECTURE_QA` dokuz bölümlü yapının varlığını ve bazı stil
   ölçülerini doğruladı; bilimsel kapsam tamlığını veya individual-study
   reporting'i doğrulamadı.
4. `FINAL_VISUAL_CONTRACT_QA` 16 blueprint carrier'ın sözleşmesini doğruladı;
   yalnız Table I materyalizeydi. Kalan blueprintler gerçek şekil/tablo
   değildir.
5. Public-release QA sanitized row counts ve leakage kontrollerini doğruladı;
   draft staging için creator, rights, license, DOI ve final deposit kapıları
   hâlâ açıktır.

## Tamamlanma koşulu

Yeniden denetim ancak K1--K14 için güncel kanıt, düzeltme ve durum üretildiğinde
tamamlanır. Bilimsel metin ve bibliyografik kapılar geçse bile gerçek görseller,
final supplement packaging, front matter, lisans/repository ve rendered-layout
kontrolleri tamamlanmadan sonuç `NOT_SUBMISSION_READY` kalır.
