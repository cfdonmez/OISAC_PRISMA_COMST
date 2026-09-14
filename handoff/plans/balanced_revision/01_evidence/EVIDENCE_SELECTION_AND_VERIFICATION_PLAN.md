# Kanıt Seçimi ve Çift Doğrulama Planı — Dengeli Revizyon

## 1. Evren

Kaynak `ST-19_PRIMARY_METRIC_RESULTS_4779.csv` içindeki
`cross_study_quantitative_comparison_allowed=yes_with_conditions` satırlarıdır:

- 118 kayıt;
- 15 study cluster;
- 16 source report;
- 106 dolu `value_numeric`;
- 118/118 `independent_human_status=not_documented`.

Bu bayrak tek başına ana metin izni değildir; yalnız aday evrenini tanımlar.

## 2. Hard inclusion

Bir kayıt ancak aşağıdaki alanlar kaynak PDF ile doğrulanabiliyorsa seçilebilir:

- eligible primary quantitative claim;
- sayı, sınır veya aralık;
- study/report lineage;
- PDF page ve section/table/figure/equation locator;
- metric adı ve unit;
- measurement plane;
- validation type ve scenario/condition set;
- baseline/comparator veya açık `within-study operating point` rolü;
- conflict-free final claim status.

## 3. Önceden tanımlı seçim sırası

### 3.1 Zorunlu çekirdek adaylar

İlk 11 aday şu ID'lerdir; bunlar henüz insan doğrulanmış değildir:

- Fiber communication data rate:
  `MET-SCR00052-G2-009`, `MET-STCENDOGENOUS-G2-001`,
  `MET-STCENDOGENOUS-G2-002`.
- Fiber sensing spatial resolution:
  `MET-SCR00038-G2-004`--`007`, `MET-SCR00057-G2-005`,
  `MET-STCENDOGENOUS-G2-011`.
- Photonics-assisted THz communication data rate:
  `MET-SCR00036-G2-005`, `MET-SCR00086-G2-001`.

Kaynak doğrulaması başarısız olan çekirdek aday zorla tutulmaz.

### 3.2 Ek 23--25 sonuç

- Fiber, photonics-assisted THz, VLC/LiFi ve FSO için kanıt varsa en az birer
  decision cell sağlanır.
- Communication, sensing ve joint/implementation işlevleri temsil edilir.
- Rapor başına en fazla dört ek kayıt alınır.
- Explicit baseline ve condition set taşıyan kayda öncelik verilir.
- En az iki constraint/degradation/tradeoff örneği hedeflenir.
- Yeni okuyucu kararı üretmeyen yinelenen sayı eklenmez.
- Pending-human veya eksik-locator kayıt çözümlenmeden seçilmez.

### 3.3 Stop rule

30 kayıt elde edildikten sonra yalnız yeni modality, işlev, validation tier veya
karar ekseni sağlayan kayıt eklenir. 40 kayıtta koşulsuz durulur. Hedef 34--36'dır.

## 4. Karşılaştırma sözleşmesi

Cross-study kart için aşağıdaki tuple tam eşleşmelidir:

`modality + metric domain/family + exact reported unit + measurement plane +
validation type + condition/scenario + baseline role`

Tam eşleşmeyen değerler sıralanmaz. Bunlar ayrı `reported operating point`
kartlarında, kendi koşulları içinde gösterilebilir. Bir kart üstünlük iddiası
değil, yöntem seçimi için sınırlandırılmış kanıt sunar.

## 5. İki insan doğrulaması

Reviewer A ve Reviewer B birbirlerinin formunu görmeden PDF'yi açar. AI yalnız
ön doldurma ve consistency QA yapabilir; insan reviewer sayılamaz.

Her reviewer şunları kaydeder:

- metric/study/report kimliği ve PDF SHA-256;
- page/section/table/figure/equation locator;
- reported metric adı, operator, value/range/uncertainty ve unit;
- measurement plane, validation type ve scenario;
- baseline, directionality ve comparison role;
- `include_card`, `supplement_only`, `context_only` veya `reject_after_review`;
- karar gerekçesi, reviewer ID ve timestamp.

Reviewer farkları adjudicator tarafından kaynak açıkken çözülür. Çözümsüz kayıt
ana metne veya kilitli evidence paketine giremez.

## 6. Ürünler

- `LOCKED_RESULTS_30_40.csv`
- `EXCLUDED_CANDIDATES_WITH_REASONS.csv`
- `CONDITION_MATCHED_COMPARISON_CARDS.csv/.tex`
- `OPERATING_POINT_CARDS.csv/.tex`
- `METHOD_DECISION_MATRIX.csv/.tex`
- `TRACEABILITY_CROSSWALK.csv`
- `ST-BALANCED_NUMERIC_EVIDENCE_30_40.csv`

