# 118 Kayıt için Çift İnsan Doğrulama Protokolü

Durum: `DRAFT_FOR_LOCK`

## 1. Reviewer modeli

- `V1` ve `V2` iki farklı insandır.
- İlk değerlendirmede birbirlerinin sonuçlarını görmezler.
- AI, kaynak lokatörü bulabilir ve formu ön doldurabilir; V1/V2 sayılamaz.
- `SA` kıdemli insan adjudicator'dır ve bütün uyuşmazlıkları kaynak açıkken çözer.

## 2. Pilot

Tam review öncesinde 12 kayıt seçilir:

- en az dört modality;
- communication, sensing ve joint/implementation;
- scalar, range/bound ve uncertainty içeren kayıtlar;
- table/figure/equation locator çeşitliliği;
- single-report ve companion-report family örnekleri.

Kritik alanlar `value/operator/range/unit/source locator` için exact agreement
>=90% olmalıdır. Altında kalırsa codebook/protokol düzeltilir ve aynı pilot baştan
tekrarlanır. Her pilot uyuşmazlığı tam review öncesi çözülür.

## 3. Her kayıt için zorunlu alanlar

- metric, study cluster ve source report ID;
- DOI/title/report identity ve companion ilişkisi;
- source PDF SHA-256;
- page, section, table, figure, equation locator;
- reported metric adı ve kaynak tanımı;
- operator, value, low/high, uncertainty ve unit;
- measurement plane ve reference point;
- communication/sensing task ve objective;
- scenario, geometry, condition set;
- baseline/comparator;
- validation type;
- value origin: `reported`, `source_calculated`, `digitized`;
- comparison group ve cross-study decision rationale;
- `main_text`, `supplement_only`, `context_only`, `reject_after_review` kararı.

## 4. Karar kuralları

- Sayı ve unit kaynakla tam eşleşir.
- Protocol dışı digitized value kullanılmaz.
- Unit conversion yalnız formül, input IDs ve iki insan onayıyla yapılır.
- Companion report bağımsız çalışma sayılmaz.
- Blank tahmin edilmez; `NR/UNC` kullanılır.
- Bir kayıt insan verification'da başarısızsa kanonik kayıttan silinmez; overlay
  statüsü ve gerekçesi korunur.
- 118 kayıt tek bir pooled performance universe oluşturmaz.

## 5. Adjudication

V1/V2 kilitli formlar karşılaştırılır. Her farklı alan için discrepancy kaydı
açılır. SA, original PDF/publisher source üzerinden final kararı ve gerekçeyi
yazar. Çözümsüz satır `VERIFIED_118_LOCK` içine giremez.

Kategorik alanlarda percent agreement ve anlamlı olduğunda Cohen's kappa
raporlanabilir; ancak istatistik bütün uyuşmazlıkların kaynak düzeyinde çözülmesi
zorunluluğunun yerine geçmez.

## 6. Lock ölçütü

- 118/118 V1 tamam;
- 118/118 V2 tamam;
- 16/16 source report açılmış ve hash doğrulanmış;
- 0 missing source locator for retained numeric claim;
- 0 unresolved discrepancy;
- 0 unresolved study/report duplication;
- corrected/rejected/non-poolable bütün kayıtlar gerekçeli;
- lock JSON/CSV input hash ve karar tarihi taşıyor.

