# Amendment-001 — Conditional Comparison Reanalysis

Status: `LOCKED_RETROSPECTIVE_SEQUENCE_DEVIATION_RECORDED`

Proposed date: `2026-09-01`

Applies to: O-ISAC COMST full-revision option only

## Rationale

Frozen manuscript, teknoloji taksonomisi ve sınıflandırma bakımından güçlü bir
kanıt haritası sunarken okuyucunun “hangi yöntem, hangi koşulda, hangi
baseline'a karşı, ne düzeyde ve hangi transfer sınırıyla çalıştı?” sorusuna
doğrudan yanıt veren karşılaştırma katmanı sınırlıdır. Bu amendment, mevcut
kanıt korpusunu yeniden taramadan, önceden materialize edilmiş koşullu
karşılaştırma adaylarını insanla doğrulayıp koşul-korumalı bir teknik senteze
dönüştürmeyi önerir.

## Amendment sorusu

Kilitli Phase A--F korpusu içindeki koşullu karşılaştırma kayıtlarından hangileri
kaynak raporda value/unit, operating condition, baseline, measurement plane,
validation context ve transfer sınırı birlikte doğrulanarak ana metinde bounded
comparison anchor olarak kullanılabilir?

## Değişmeyen kapsam

Bu amendment şunları değiştirmez:

- search window, database/source set veya search strings;
- eligibility ve exclusion kararları;
- 227 eligible report / 206 included study korpusu;
- report-to-study/companion mapping;
- Phase C PRISMA sayımları;
- kanonik Phase D satırları;
- Phase E TQAF ve Phase F S1--S7 otoriteleri;
- retrospective registration açıklaması.

Yeni literatür araması veya outcome-temelli çalışma seçimi yapılmaz.

## Önerilen Phase G kapsamı

- Source universe: ST-19 içindeki 4,779 primary metric kayıt.
- Verification candidate set: 118 koşullu karşılaştırma satırı.
- Study/report kapsamı: 15 çalışma ve 16 rapor.
- Analysis unit: `study + condition set + comparison group`.
- Default synthesis rule: non-pooling; pooling ancak ayrıca tanımlanmış
  homojenlik ve bağımsızlık koşulları geçerse değerlendirilir.

`118`, 118 bağımsız deney veya 118 bağımsız çalışma anlamına gelmez. Frozen
manuscript'teki legacy `92` unresolved-conditional sayımı da Phase G aday
kümesiyle eş anlamlı değildir. Bu iki sayı, doğrulama tamamlanmadan manuscript
iddiasında birbirinin yerine kullanılamaz. Nihai retained/corrected/rejected
dağılımı yalnız adjudication lock sonrasında raporlanır.

## Doğrulama modeli

1. Farklı modality ve metric sınıflarından 12 satırlık pilot hazırlanır.
2. Reviewer 1 ve Reviewer 2 farklı insanlardır; kararları birbirine kapalıdır.
3. Her reviewer kaynak PDF'yi açarak en az şu alanları bağımsız kaydeder:
   report identity ve SHA-256, source locator, metric family, operator,
   `value_numeric`/low/high, reported unit, uncertainty type/value, operating
   condition, geometry/scenario, measurement plane, comparator/baseline,
   comparison direction/role ve validation context.
4. Eksik bilgi `NR`, belirsiz bilgi `UNC` olarak korunur; tahmin yapılmaz.
5. Bütün farklılıklar ayrı adjudicator tarafından gerekçeli kapatılır.

## Overlay-only veri yönetişimi

Kanonik Phase D ve ST-19 satırları overwrite edilmez. Phase G çıktısı her source
row için aşağıdaki kararlardan birini taşır:

- `verified_as_reported`;
- `corrected_in_overlay`;
- `rejected_after_human_verification`;
- `supplement_only`.

Her düzeltme eski değer, yeni değer, source locator, iki reviewer kararı,
adjudication gerekçesi ve ilgili hashes ile izlenir. Companion report ayrı bir
çalışma olarak sayılmaz.

## Manuscript kullanım kapısı

G5 adjudication lock ve G7 carrier approval öncesinde:

- yeni Phase G sayısal iddiası yazılamaz;
- aday kayıt “verified” olarak etiketlenemez;
- Fig. 6 veya Table V'e yeni operating-point değeri eklenemez;
- Phase G tamamlanmış bir yöntem gibi Methods bölümüne yazılamaz.

G7 sonrasında her ana-metin sayısı source-to-claim crosswalk, comparison-group
kararı ve transfer sınırı taşımak zorundadır. Uyuşmayan platformlar bir
leaderboard içinde sıralanamaz.

## Beklenen çıktılar

- ayrı Reviewer 1 ve Reviewer 2 kayıtları;
- 16-report identity/path/hash manifesti;
- adjudication log ve immutable 118-row lock;
- comparison-group ve non-pooling katalogları;
- main-text evidence crosswalk;
- Phase G errata overlay;
- doğrulanmış ana-metin taşıyıcıları ve tam supplement atlası.

## Lock koşulları

Amendment ancak aşağıdaki kararların tamamı yazılı kaydedildiğinde `LOCKED`
olabilir:

- [x] Bütün insan katılımcılar kapsamı onayladı.
- [x] 118/15/16 aday sınırı onaylandı.
- [x] Reviewer 1 ve Reviewer 2 olarak iki farklı insan atandı.
- [x] Uyuşmazlık hâlinde görev alacak üçüncü insan kontrol rolü belirlendi.
- [x] Reviewer codebook ve 12-row pilot ölçütleri onaylandı.
- [x] Overlay-only ve varsayılan non-pooling ilkeleri onaylandı.
- [x] Numeric manuscript claim gate onaylandı.
- [x] Balanced branch/worktree merge veya carryover yasağı onaylandı.

Author approval record: `2026-09-01__TWO_INDEPENDENT_ANONYMOUS_HUMAN_REVIEWERS_AND_ONE_ANONYMOUS_HUMAN_AUTHOR_CONTROLLER_CONFIRMED`

G1 decision: `PASS_RETROSPECTIVE_SEQUENCE_DEVIATION_RECORDED`

## Uygulama kronolojisi

İki bağımsız insan inceleyici 118 kaydı analog olarak inceleyip kaynak
kimliği, locator, değer, birim, koşul ve comparator rolü bakımından onayladı.
Üçüncü insan katılımcı kapsamı ve dijital kayıt işlemini 2026-09-01 tarihinde
onayladı. Analog inceleme resmî dijital G1 ve pilot kaydından önce tamamlandığı
için tarih veya sıra geriye dönük değiştirilmedi; bu durum açık protokol
sapması olarak kaydedildi.

İki inceleyici bütün kayıtlar üzerinde uzlaştı. Uyuşmazlık sayısı sıfır olduğu
için ayrı bir adjudication kararı gerekmedi. Kaynak doğrulama onayı, G6
karşılaştırma rolü ve G7 ana-metin kullanımı kararlarından ayrıdır.
