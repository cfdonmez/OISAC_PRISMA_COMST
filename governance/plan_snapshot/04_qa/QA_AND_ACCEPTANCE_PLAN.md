# QA ve Kabul Planı — Tam Revizyon

## Verification completeness

- 118/118 V1 + 118/118 V2.
- 16/16 report identity/path/hash verified.
- 0 unresolved discrepancy.
- 0 retained numeric claim without source locator.
- 0 unresolved companion-report duplication.
- Corrected/rejected/non-poolable rows overlay'de gerekçeli.

## Analysis integrity

- Analysis unit study + condition + group olarak uygulanmış.
- Comparison group contract bütün alanlarda tam.
- Incompatible values rank edilmemiş.
- Non-pooling decision her dışlanan group için kayıtlı.
- Meta-analysis yalnız ayrıca onaylı minimum assumptions geçerse yapılmış;
  varsayılan PASS için meta-analysis gerekmiyor.
- Main-text anchor selection, önceden yazılmış coverage testini geçmiş.

## Manuscript reader value

- Sections IV--VII'nin her biri learned pattern, validity condition, limit ve
  design decision taşıyor.
- Her yeni sayı source crosswalk'ta.
- Section V yöntem + koşul + baseline + result + validation + limit sorularını
  yanıtlıyor.
- Beş roadmap priority'nin sekiz alanı tam.
- Conclusion yeni kanıt eklemeden bilimsel kararları özetliyor.

## Independent reader test

Manuscript'i yazmayan en az iki teknik okuyucu şu soruları yanıtlar:

1. Hangi yaklaşım hangi koşulda ne başardı?
2. Neye karşı kıyaslandı?
3. Hangi sınıra taşınamaz?
4. Hangi benchmark kurulmalı?
5. Başarı ölçütü nedir?

Ana metin ortalama eşiği >=80%; supplement source trace başarısı %100'dür.

## Build/release QA

- Clean build exit 0.
- Undefined citation/reference, LaTeX fatal, overfull box, broken float yok.
- PDF <=30 sayfa.
- Bütün sayfalar render edilmiş; clipping/overlap/unreadable label yok.
- Table/figure cross-reference ve bibliography kontrolü PASS.
- 206-study/227-report protected counts unchanged.
- Final source, supplement, PDF ve manifests SHA-256 ile dondurulmuş.
- Bütün yazarlar release'i açıkça onaylamış.

## Stale QA

Her QA report input source hash ve commit/baseline ID taşır. İlgili source
değiştiğinde eski PASS geçersizdir ve gate yeniden çalıştırılır.

