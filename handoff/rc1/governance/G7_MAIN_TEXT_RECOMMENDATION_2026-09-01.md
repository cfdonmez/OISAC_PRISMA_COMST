# Phase G Human Decision Packet — G6 Method and G7 Main-Text Carriers

Status: `G6_METHODS_LOCKED__G7_CARRIERS_APPROVED`

Date: `2026-09-01`

## Karar özeti

İnsan kaynak doğrulaması tamamlandı: 118 kayıt, 15 çalışma, 16 rapor,
118/118 iki-reviewer uzlaşısı ve sıfır uyuşmazlık. Aşağıdaki iki karar
2026-09-01 tarihinde kilitlenmiştir:

1. **G6 yöntem kararı:** 76 kanonik grubun hiçbirinin birden fazla bağımsız
   çalışma içermediğini ve bu nedenle sentezin kaynak-içi koşullu karşılaştırma
   + açık non-pooling olarak yürütülmesini onaylamak.
2. **G7 taşıyıcı kararı:** 18 kanıt satırını sekiz çok-metrikli ana-metin kartı
   olarak kullanmak; 7 satırı bağlamsal, 93 satırı supplement-only tutmak.

## G6 için net yöntem önerisi

- Analiz birimi: `study + condition set + comparison group`.
- 76 grup: 53 condition-bound singleton, 23 kaynak-içi çok-satırlı grup.
- Bağımsız çok-çalışmalı grup: 0.
- Pooled effect, unit normalization veya leaderboard: yapılmamalı.
- İzin verilen anlatım: aynı çalışma içindeki operating point, before/after,
  interval/sweep ve maliyet--kazanım ilişkileri.
- Çalışmalar arası ifade: yalnız neden pooling yapılamadığını ve hangi ortak
  deney sözleşmesinin gerektiğini açıklamalı.

## G7 için önerilen sekiz kart ve 18 anchor

1. **K1 — Fiber data-rate--resolution**
   - `MET-STCENDOGENOUS-G2-002`
   - `MET-STCENDOGENOUS-G2-011`
2. **K2 — LPN compensation before--after**
   - `MET-SCR00008-009`
   - `MET-SCR00008-010`
3. **K3 — Probe interval--resolution**
   - `MET-SCR00038-G2-004`
   - `MET-SCR00038-G2-005`
   - `MET-SCR00038-G2-006`
   - `MET-SCR00038-G2-007`
4. **K4 — Distance--error envelope**
   - `MET-SCR00056-G2-006`
   - `MET-SCR00056-G2-007`
5. **K5 — Photonic mmWave rate--ranging**
   - `MET-SCR00036-G2-005`
   - `MET-SCR00036-G2-002`
6. **K6 — VLC laboratory--application boundary**
   - `MET-SCR00196-009`
   - `MET-SCR00196-019`
7. **K7 — FSO gain--processing cost**
   - `MET-R01-SCR00233-003`
   - `MET-R01-SCR00233-019`
8. **K8 — Photonic-THz bandwidth--efficiency**
   - `P03-M040`
   - `P03-M041`

Bu yapı 18 ayrı çalışma iddiası değil, sekiz koşul-korumalı çok-metrikli
karttır. K3 dört operating point içerir; diğer kartlar ikişer kanıt satırı
içerir.

## Bağlamsal ve supplement dağılımı

Bağlamsal yedi kayıt:

- `MET-SCR00057-G2-001`
- `MET-SCR00941-001`
- `MET-SCR00941-002`
- `MET-SCR00941-004`
- `MET-SCR00941-005`
- `MET-SCR00941-007`
- `MET-SCR00941-010`

Kalan 93 kayıt `supplement_only` önerisidir. Ret önerisi yoktur. Bütün 118
kayıt ST-G01 atlasında korunur.

## Kanıt sınırları

- Validation: 98 laboratory, 9 simulation, 7 analytical, 2 mixed,
  2 prototype/testbed, 0 field.
- Metric domain: 70 sensing, 39 communication, 9 joint, 0 implementation.
- Bu nedenle field readiness ve implementation cost kanıtlanmış sonuç olarak
  sunulamaz; açık deney boşluğu olarak yazılmalıdır.
- Satır yoğunluğu kanıt gücü veya çalışma bağımsızlığı gibi yorumlanmamalıdır.

## G7 onayından sonra uygulanacak manuscript revizyonu

- Abstract ve Section I: okuyucu çıktısı, koşula bağlı yöntem seçimi, teknik
  sınırlar ve somut deney motivasyonu.
- Section II: karşılaştırma sözleşmesi; `within-study`, `non-poolable` ve
  transfer boundary ayrımı.
- Section III: 118/15/16 kapsamı, iki bağımsız insan incelemesi, sıfır
  uyuşmazlık, overlay-only ve varsayılan non-pooling.
- Section IV: modality başına temsilî operating point ve taşıma sınırı.
- Section V/Table V: sekiz kart ve 18 anchor; ortak leaderboard olmadan.
- Figure 6: kaynak-içi LPN, probe-interval ve distance--error mekanizma
  panelleri; native unit korunur.
- Section VI: validation dağılımı, özellikle 98 laboratory ve 0 field sonucu.
- Section VII/Table VII: application requirement -> verified evidence ->
  validation -> eksik test zinciri.
- Section VIII/Table VIII: ortak benchmark, disturbance sweep,
  laboratory-to-field transfer, implementation/reconstructability ve
  interoperability/failure testleri için beş deney reçetesi.
- Conclusion: yöntem dersi, kıyas sınırı ve sıradaki deneyler.

Hedef final uzunluk 29--30 sayfadır; hard cap 30 sayfadır. Manuscript
uygulaması G6/G7 onayından sonra başlatılmış; dondurulmuş baseline PDF
değiştirilmemiştir.

## İnsan-yazar kararı

- [x] G6 yöntemi: `APPROVE_WITHIN_STUDY_PLUS_NONPOOLING`
- [x] G7 taşıyıcıları: `APPROVE_8_CARDS_18_ANCHORS_7_CONTEXT_93_SUPPLEMENT`
- [x] Kanıt boşlukları: `ACCEPT_0_FIELD_0_IMPLEMENTATION_AS_EXPLICIT_GAPS`

Approval record:
`2026-09-01__ANONYMOUS_HUMAN_AUTHOR_CONTROLLER__APPROVED`

Karar sahibi adı yerine anonim insan-yazar rolü ve karar tarihi kaydedilmiştir.
G8 manuscript uygulaması bu karar sonrasında başlatılmıştır.
