# V3-S1 Scientific Core Lock

| Alan | Değer |
|---|---|
| `lock_id` | `V3-S1` |
| `status` | `DRAFT_FOR_AUTHOR_REVIEW` |
| `opened_at` | `2026-09-04` |
| `payload_version` | `V3-S1-PAYLOAD-1.1` |
| `payload_sha256` | `c80876e2958774ee7957eeaf3b11d406efceb5f530bebc8ecc01a46f2c50ad09` |
| `scope` | Yalnızca merkezî soru, J tanımı ve jointness temel kararı |

Bu kayıt, V3 tam-makale ilişkilendirme haritasındaki ilk karar kapısını açar.
Bir manuscript uygulaması veya bölüm mimarisi onayı değildir. Bu dosya
`LOCKED` durumuna yalnızca bütün kabul testleri geçtikten ve üç yazar aynı
payload hash'i için `APPROVE` verdikten sonra geçirilebilir.

## Kanonik payload

Hash, aşağıdaki işaretçiler arasındaki metnin işaretçiler hariç UTF-8
baytlarından üretilir. Satır sonları LF olarak normalize edilir ve payload'ın
başındaki ve sonundaki tek satır sonu hash girdisine alınmaz.

<!-- V3-S1-PAYLOAD-START -->
### Canonical central research question

> Across heterogeneous optical integrated sensing and communication (O-ISAC)
> platforms, what combination of physical paths, coupling mechanisms or
> locations, and shared design factors links communication and sensing
> performance, and under what measurement and evidence conditions can the
> resulting relations be compared, transferred across designs, and converted
> into testable experimental decisions?

### Canonical scientific object

\[
J_r=\langle P_r,G_r,X_r,C_r,S_r,M_r,E_r\rangle
\]

- **P — Physical system and target-reaching path:** System boundary, the role
  of optics, the target-reaching signal path, and any optical–RF conversion
  boundary.
- **G — Coupling mechanism/location:** What communication and sensing share and
  where that coupling occurs in the system.
- **X — Shared/varied factor:** The common or varied design variable,
  constraint, or impairment that links the two functions.
- **C — Communication outcomes:** Rate, BER, SNR, latency, reliability,
  coverage, and other communication outcomes.
- **S — Sensing outcomes:** Resolution, accuracy/error, range, sensitivity,
  detection/localization, and other sensing outcomes.
- **M — Measurement contract:** Outcome definitions, measurement planes,
  units, accounting states, operating points, baselines, ground truth, and
  condition-set alignment.
- **E — Evidence envelope:** Source provenance, validation setting,
  configuration/timing trace, source locator, and permitted inference boundary.

The operational refinements are

\[
M_r=\langle M_C,M_S,A_M\rangle,\qquad
E_r=\langle E_C,E_S,T_r,B_r\rangle.
\]

Here, \(A_M\) records whether C and S were produced under the same or an
alignable operating condition, \(T_r\) records the configuration/timing trace,
and \(B_r\) records the permitted inference boundary.

### Canonical jointness decision

The presence of a communication metric and a sensing metric in the same paper
does not by itself establish a joint-performance link. The minimum evidential
link requires a source-traceable shared or varied factor **X** that connects the
two outcomes, with sufficient **M/E** information to establish the relation in
its native context. A complete and transferable **J** record additionally
requires resolved **P/G** context and an **M/E** contract adequate for the
proposed comparison or transfer. The transferable scientific unit is therefore
not the highest reported value, but the X–C–S relation whose physical context,
measurement conditions, and evidence boundary remain intact.
<!-- V3-S1-PAYLOAD-END -->

## Türkçe çalışma anlamı

Merkezî soru şunu sorar: Heterojen O-ISAC platformlarında hangi fiziksel yol,
coupling mekanizması veya konumu ve ortak tasarım etkeni bileşimi iletişim ile
algılama performansını birbirine bağlamaktadır; oluşan ilişkiler hangi ölçüm ve
kanıt koşullarında karşılaştırılabilir, başka tasarımlara aktarılabilir ve
sınanabilir deney kararlarına dönüştürülebilir?

Bu paragraf kanonik sorunun çalışma içi açıklamasıdır; ikinci veya rakip bir
araştırma sorusu değildir.

## Soru ile J arasındaki izlenebilirlik

| Soru öğesi | J karşılığı | Sağladığı karar |
|---|---|---|
| Physical paths | P | Sistem ve dönüşüm sınırını belirler. |
| Coupling mechanisms or locations | G | İki fonksiyonun neyi ve sistemin neresinde paylaştığını belirler. |
| Shared design factors | X | İki outcome'u bağlayan değişken, kısıt veya impairment'ı belirler. |
| Communication and sensing performance | C, S | İlişkinin iki outcome tarafını tanımlar. |
| Measurement conditions | M | Değerlerin aynı veya eşlenebilir operating point altında olup olmadığını sınar. |
| Evidence conditions and transfer | E | İddianın kapsamını, validation izini ve aktarım sınırını belirler. |
| Testable experimental decisions | Bütün J | Bulguyu kontrollü deney, başarı ölçütü ve artifact kararına dönüştürür. |

## Claim-language bağı

Bu bilimsel çekirdek, [O-ISAC Author-Governed Claim-Language
Recipe](../../../outputs/comst_prose_revision_2026-08-08/style_profile/OISAC_AUTHOR_GOVERNED_CLAIM_LANGUAGE_RECIPE_2026-09-04.md)
ile uygulanır. İç durum kodları evidence/audit katmanında korunur; okuyucuya
mekanik biçimde aktarılmaz. Ana metin en güçlü desteklenen ilişkiyi öne çıkarır.
İddiayı değiştiren eksiklik ve maddi karşı kanıt ise gizlenmez ve ilgili
iddianın yanında bilimsel sınır olarak gösterilir.

## Bu kilidin onayladığı ve onaylamadığı işler

Bu kapı yalnızca merkezî soruyu, J öğelerinin anlamını ve operational jointness
kuralını onaylayabilir.

Bu kapı aşağıdakileri **onaylamaz**:

- section/subsection mimarisi ve bölüm devirleri;
- figure/table carrier tasarımı;
- P, X, M veya E backfill kapsamı;
- controlled X-family sınıflandırması;
- karşılaştırma sonucu, pooling veya promotion kararı;
- herhangi bir yeni nicel corpus iddiası;
- manuscript `.tex` metni veya yeni sürüm ağacı.

Frozen 206 çalışma / 227 report tabanı ile Phase G overlay ayrımı bu kapıda
değiştirilemez. Doğrulanmış 118 metric record, 118 joint relation veya 118
cross-study comparison olarak adlandırılamaz. Mevcut comparison-group
dağılımının yorumlanması sonraki Comparison Lock'a aittir.

## Kabul testleri

| Test | Durum | Kanıt / kalan işlem |
|---|---|---|
| `S1-01 Canonical question` | `PASS` | Harita ve bu kayıtta tek İngilizce kanonik soru sözcüğü sözcüğüne aynıdır; Türkçe metin yalnız çalışma anlamıdır. |
| `S1-02 J completeness` | `PASS` | P, G, X, C, S, M ve E birer kez tanımlıdır; M ve E alt bileşenleri verilmiştir. |
| `S1-03 Semantic boundaries` | `PASS` | G coupling mechanism/location, X bağlayıcı factor, M measurement contract ve E inference boundary olarak ayrılmıştır. |
| `S1-04 Question-to-J coverage` | `PASS` | Yukarıdaki izlenebilirlik tablosu sorunun bütün öğelerini J'ye bağlar. |
| `S1-05 Operational jointness` | `PASS` | Aynı makalede C+S bulunması FAIL; native bağ için X+izlenebilir M/E gerekir. Tam ve aktarılabilir J ayrıca çözümlenmiş P/G ile amaçlanan çıkarıma yeterli M/E gerektirir. |
| `S1-06 Claim and denominator guard` | `PASS` | 118 kayıt ilişki veya cross-study comparison olarak yeniden etiketlenmez; bu kilit pooling/leaderboard iddiası üretmez. |
| `S1-07 Author/hash lock` | `PENDING` | Üç yazarın aynı payload hash'i için açık kararı bekleniyor. |
| `S1-08 State and scope consistency` | `PENDING` | `LOCKED/PASS` eşlemesi yalnız S1-07 tamamlandıktan sonra yapılabilir; ayrı V3 QA kaydı ile `.tex`, corpus ve evidence değişmezliği yeniden doğrulanacak. |

## Yazar kararları

Her yazar yalnız `APPROVE`, `REVISE` veya `REJECT` seçer. `APPROVE`, tabloda
gösterilen payload version ve SHA-256 için verilir.

| Yazar | Karar | Tarih | Payload version | Payload SHA-256 | Not |
|---|---|---|---|---|---|
| Fatih Dönmez | `PENDING` | — | `V3-S1-PAYLOAD-1.1` | `c80876e2958774ee7957eeaf3b11d406efceb5f530bebc8ecc01a46f2c50ad09` | — |
| Ahmet Altuncu | `PENDING` | — | `V3-S1-PAYLOAD-1.1` | `c80876e2958774ee7957eeaf3b11d406efceb5f530bebc8ecc01a46f2c50ad09` | — |
| Mustafa Namdar | `PENDING` | — | `V3-S1-PAYLOAD-1.1` | `c80876e2958774ee7957eeaf3b11d406efceb5f530bebc8ecc01a46f2c50ad09` | — |

## Yeniden açma kuralı

Kanonik payload'da tek karakterlik değişiklik dahi yeni `payload_version` ve
SHA-256 gerektirir; önceki yazar onayları yeni payload'a taşınmaz. Kilitli bir
payload değiştirilirse durum `REOPENED` olur. Yeni payload bütün yazarlarca
onaylanmadan Architecture Lock başlatılamaz.

## Sonraki adım

Bu dosya teknik inceleme ve yazar kararlarıyla tamamlandığında V3-S1 `LOCKED`
olur. Yalnız bundan sonra ikinci kapı olan Architecture Lock, mevcut V3 aday
haritasındaki section/subsection çıktıları ve handoff'lar üzerinden ele alınır.
