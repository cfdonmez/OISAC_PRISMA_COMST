# WBS, Takvim ve RACI — Tam Revizyon

## Work packages

| WP | İş | Bağımlılık | Kişi-saat | Bitiş ölçütü |
|---|---|---|---:|---|
| WP0 | Baseline source/hash/build freeze | — | 3--4 | G0 PASS |
| WP1 | Phase G amendment, codebook, acceptance tests | WP0 | 5--6 | G1 PASS |
| WP2 | 12-row pilot packet ve double review | WP1 | 6--8 | G2 PASS |
| WP3 | 16 report packet ve PDF manifest | WP1 | 4--5 | G3 PASS |
| WP4 | 118-row V1/V2 independent verification | WP2+WP3 | 36--44 toplam | G4 PASS |
| WP5 | Discrepancy adjudication ve 118 lock | WP4 | 7--9 | G5 PASS |
| WP6 | Comparison groups, non-pooling, anchor selection | WP5 | 9--11 | G6--G7 PASS |
| WP7 | Abstract/I/III/IV--IX scientific rewrite | WP6 | 13--16 | G8 PASS |
| WP8 | Supplement ST-G01--G09 ve provenance | WP5+WP6 | 6--8 | G9 PASS |
| WP9 | Compression, build, citation, render, reader QA | WP7+WP8 | 7--9 | G10 technical PASS |
| WP10 | Author adjudication, RC1, final release | WP9 | 3--4 | G10 author PASS |
|  | **Toplam** |  | **99--124** |  |

Planlama bandı 99--124 kişi-saat olarak kullanılacaktır; pilot veya discrepancy
yükü yüksekse üst sınır yeniden tahmin edilir ve scope sessizce genişletilmez.

Kritik zincir:

`WP0 -> WP1 -> (WP2 || WP3) -> WP4 -> WP5 -> WP6 -> (WP7 || WP8) -> WP9 -> WP10`

## Takvim

| Hafta | Ana çıktı |
|---|---|
| 0 | Baseline freeze + amendment/codebook lock |
| 1 | 12-row pilot, protocol correction gerekirse repeat, 16 report packets |
| 2 | V1/V2 full verification |
| 3 | Verification completion, adjudication, G3 lock, comparison groups |
| 4 | IV--VIII rewrite, supplement, compression/build/render/reader QA, RC1 |

Yazarların veya V1/V2'nin ardışık çalışması gerekirse takvim uzar; bilimsel
gate'ler sıkıştırılmaz.

## Roller ve RACI

- `CA`: lead/corresponding author
- `SA`: senior scientific author ve adjudicator
- `RM`: review methodologist/data steward
- `V1`, `V2`: bağımsız insan doğrulayıcılar
- `MW`: manuscript/section owner
- `SQ`: independent scientific/build QA
- `IR`: independent readers
- `ALL`: bütün yazarlar

| WP | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| WP0 | RM, SQ | CA | SA | ALL |
| WP1 | RM | SA | V1, V2, SQ | ALL |
| WP2 | V1, V2, RM | SA | CA | ALL |
| WP3 | RM | SA | V1, V2 | CA |
| WP4 | V1, V2 | SA | RM | CA |
| WP5 | SA, RM | CA | V1, V2 | ALL |
| WP6 | RM, CA | SA | SQ, section owners | ALL |
| WP7 | MW, section owners | CA | SA, RM | ALL |
| WP8 | RM, SQ | SA | MW | ALL |
| WP9 | SQ, MW, IR | CA | RM, SA | ALL |
| WP10 | SQ | CA | SA, ALL | ALL |

Her WP için tek accountable rol korunur.
