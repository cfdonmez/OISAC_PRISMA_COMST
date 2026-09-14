# O-ISAC COMST Tam Revizyon Çalışma Şartı

Durum: `RC1_TECHNICAL_QA_PASS__G8_G9_HUMAN_APPROVALS_PENDING__G10_READER_AND_ALL_AUTHOR_SIGNOFF_PENDING`

Tarih: `2026-09-01`

Çalışma ağacı: `C:\OISAC\worktrees\comst-full-20260901`

Baseline commit: `13e3727241cb1d7726abb3ddb1833505c73c157f`

## 1. Amaç

Bu çalışma ağacı, frozen 27 sayfalık O-ISAC COMST adayını okuyucu değeri,
koşula bağlı teknik karşılaştırmalar, lessons learned ve somut deney roadmap'i
açısından tam revize etmek için ayrılmıştır. Revizyon yeni bir sistematik
tarama değildir; kilitli Phase A--F korpusu üzerinde ayrı bir Phase G
doğrulama, analiz ve raporlama katmanı kurar.

G0 girdi dondurma ve yeniden üretilebilir baseline doğrulamasıdır. G1--G5 insan
kaynak doğrulamasını; G6 koşul-korumalı yöntem/non-pooling kararını; G7 ise
sekiz kart/18 anchor taşıyıcı setini kilitlemiştir. G8 manuscript revizyonu ve
G9 paket uygulaması bu onaylı sınırlar içinde tamamlanmış ve RC1 teknik QA'dan
geçmiştir; bilimsel içerik ve veri sorumlusu insan onayları beklenmektedir.

## 2. Yetkili baseline ve izolasyon

- Frozen source paketi:
  `C:\OISAC\prisma2020Review\systematic_review_workflow\07_raporlama\outputs\comst_prose_revision_2026-08-08\manuscript\comst_206_v2_9section\deliverables\OISAC_COMST_OVERLEAF_CORE_2026-08-25.zip`.
- Canonical 27 sayfalık PDF:
  `C:\OISAC\prisma2020Review\systematic_review_workflow\07_raporlama\outputs\comst_prose_revision_2026-08-08\manuscript\comst_206_v2_9section\main.pdf`.
- Tam revizyon ağacı frozen source paketinden bağımsız fiziksel kopya olarak
  kurulmuştur; baseline commit tek ebeveynsiz root commit'tir.
- Canonical manuscript, publisher PDF'leri ve Phase A--F artefact'ları bu
  ağaçta overwrite edilmez.
- Symlink, junction ve hardlink kullanılmaz. Kaynak dosyalar yalnız path ve
  SHA-256 pointer'larıyla izlenir.
- `comst-balanced-20260901` veya başka bir balanced branch/worktree'den merge,
  cherry-pick, toplu kopyalama ya da otomatik carryover yasaktır. Daha sonra
  taşınması önerilen her değişiklik ayrıca bilimsel ve satır-bazlı onay ister.

## 3. Korunan bilimsel sınırlar

Şunlar Phase G tarafından yeniden açılmaz:

- 1 January 2020--22 June 2026 search window;
- search kaynakları ve yürütülmüş sorgular;
- Phase A eligibility kararları;
- Phase B report-to-study mapping;
- Phase C PRISMA sayımları;
- 227 eligible report ve 206 included study ayrımı;
- Phase D kanonik workbook ve ham evidence/metric/trade-off kayıtları;
- Phase E TQAF sınıflandırması;
- Phase F S1--S7 sentez otoriteleri;
- retrospective registration niteliği.

Yeni arama, inclusion/exclusion değişikliği, yeni çalışma ekleme, graph
digitization, eksik değer tahmini veya kanıtsız unit normalization bu revizyonun
dışındadır.

## 4. Phase G yetki sınırı

Phase G ancak Amendment-001 bütün yazarlarca kilitlendikten sonra aşağıdakileri
yapabilir:

1. ST-19 içindeki 118 koşullu karşılaştırma adayını 15 çalışma ve 16 kaynak
   rapor bağlamında çift bağımsız insan doğrulamasına açmak.
2. Her aday için source locator, value/unit, condition, baseline, comparison
   role, uncertainty, measurement plane ve report hash alanlarını doğrulamak.
3. Farklı insan reviewer kararlarını maskeli yürütmek ve bütün farkları ayrı
   adjudication ile kapatmak.
4. Kanonik Phase D satırını değiştirmeden düzeltme veya red kararını Phase G
   overlay'inde tutmak.
5. Uyumlu kayıtları `study + condition set + comparison group` analiz biriminde
   toplamak; uyumsuz kayıtları gerekçeli non-pooling ile ayırmak.
6. Yalnız G5 adjudication ve G7 carrier approval sonrasında manuscript'e yeni
   sayısal iddia taşımak.

## 5. Kapılar ve mevcut yetki

| Gate | Mevcut durum | Yetki sonucu |
|---|---|---|
| G0 -- Input freeze | `PASS` | Governance ve baseline kayıtları dondurulabilir. |
| G1 -- Amendment lock | `PASS_RETROSPECTIVE_SEQUENCE_DEVIATION_RECORDED` | 118/15/16 kapsamı, iki bağımsız insan incelemesi, overlay-only ve non-pooling ilkeleri kilitlidir. |
| G2 -- Pilot | `PASS_100_PERCENT_RETROSPECTIVE_CHECK` | 12 kayıtlık kritik alan kontrolü tamamdır. |
| G3 -- Report packets | `PASS` | 16/16 kaynak raporun kimlik, yol ve SHA-256 kayıtları doğrulanmıştır. |
| G4 -- Double verification | `PASS_236_HUMAN_REVIEWS_RECORDED` | 118 x 2 insan incelemesi dijital kayda alınmıştır. |
| G5 -- Adjudication lock | `PASS_ZERO_DISCREPANCIES_NO_ADJUDICATION_REQUIRED` | 118/118 uzlaşı; düzeltme, ret ve adjudication gereği yoktur. |
| G6 -- Analysis lock | `PASS_HUMAN_METHODS_LOCKED` | 76 grup, 0 çok-çalışmalı grup ve kaynak-içi karşılaştırma + açık non-pooling yöntemi onaylandı. |
| G7 -- Carrier approval | `PASS_8_CARDS_18_ANCHORS_APPROVED` | 8 kart/18 anchor, 7 contextual ve 93 supplement-only kullanımı onaylandı. |
| G8 -- Scientific content | `RC1_TECHNICAL_QA_PASS__HUMAN_SCIENTIFIC_APPROVAL_PENDING` | Revize bilimsel içerik, Table V ve Figure 6 teknik QA'dan geçmiştir; yetkili insan bilimsel onayı beklenmektedir. |
| G9 -- Supplement | `RC1_TECHNICAL_QA_PASS__HUMAN_DATA_STEWARD_APPROVAL_PENDING` | ST-G01--ST-G09, veri sözlüğü, provenance ve RC1 release manifesti teknik QA'dan geçmiştir; insan veri sorumlusu onayı beklenmektedir. |
| G10 -- COMST release | `RC1_TECHNICAL_QA_PASS__TWO_INDEPENDENT_READERS_AND_ALL_AUTHOR_SIGNOFF_PENDING` | RC1 build/render/citation kontrolleri geçmiştir; iki bağımsız nihai-manuscript okuyucusu ve bütün yazarların açık imzası beklenmektedir. Bu durum release PASS değildir. |

Analog kaynak incelemesi resmî dijital G1/pilot kilidinden önce yapılmıştır.
Bu sıra yeniden tarihlenmemiş; `governance/G1_AMENDMENT_LOCK_2026-09-01.md`
içinde geriye dönük usul onayı ve açık protokol sapması olarak kaydedilmiştir.

## 6. Sürüm ve kanıt zinciri

Her bilimsel sürüm aşağıdakileri birlikte taşır:

- source commit veya immutable source hash;
- evidence-input SHA-256 manifesti;
- claim/crosswalk değişiklik kaydı;
- build log özeti;
- PDF SHA-256 ve sayfa sayısı;
- render QA;
- ilgili gate kararı ve insan onayı.

Eski bir QA PASS, input veya source hash değiştiğinde geçersizdir. İki bağımsız
nihai-manuscript okuyucu değerlendirmesi ve bütün-yazar imzasıyla G10 ayrıca
kapatılana kadar hiçbir çıktı submission-ready olarak adlandırılamaz.

## 7. Mevcut karar

`qa/G0_INPUT_FREEZE_QA_2026-09-01.md` ile G0; Phase G insan kilidi
artefact'larıyla G1--G5 PASS kaydedilmiştir. İnsanlar 118 kaydın kaynak
kimliği, locator, değer, birim, koşul ve comparator rolünü onaylamıştır. Bu
onay, bir kaydı otomatik olarak çalışmalar arası karşılaştırılabilir veya ana
metne uygun yapmaz. G6 için 76 grup/0 çok-çalışmalı grup ve non-pooling yöntemi;
G7 için 18 anchor/8 kart 2026-09-01 tarihinde anonim insan-yazar rolüyle
onaylanmıştır. Baseline korunarak ayrı revizyon source'u üzerinde G8/G9
uygulaması ve RC1 teknik QA tamamlanmıştır. G8 bilimsel insan onayı, G9 insan
veri sorumlusu onayı ve G10 için iki bağımsız nihai-manuscript okuyucusu ile
bütün-yazar imzası beklenmektedir; RC1 henüz nihai release değildir.
