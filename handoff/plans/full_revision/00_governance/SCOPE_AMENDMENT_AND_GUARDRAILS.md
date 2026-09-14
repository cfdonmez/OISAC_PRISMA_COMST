# Phase G Kapsam Amendment'i ve Koruma Kuralları — Tam Revizyon

Durum: `PROPOSED_AMENDMENT_NOT_LOCKED`

## Amendment amacı

Bu amendment'in tek amacı, mevcut 4,779 primary metric kaydı içindeki 118
koşullu karşılaştırma adayını insanla yeniden doğrulamak ve okuyucuya dönük
teknik senteze dönüştürmektir.

Amendment şunları değiştirmez:

- 1 January 2020--22 June 2026 search window;
- 206 included study ve 227 eligible report;
- Phase A eligibility, Phase B mapping, Phase C PRISMA;
- Phase D kanonik workbook;
- Phase E TQAF ve Phase F S1--S7 synthesis;
- review'un retrospective registration niteliği.

## Phase G veri modeli

Kanonik Phase D satırı overwrite edilmez. Her Phase G satırı en az şu katmanları
taşır:

- `source_metric_record_id`;
- source study/report/PDF hash ve locator;
- Reviewer 1 ve Reviewer 2 bağımsız kararları;
- adjudicated value/condition/baseline/comparison role;
- `verified_as_reported`, `corrected_in_overlay`,
  `rejected_after_human_verification` veya `supplement_only` durumu;
- comparison group veya gerekçeli non-pooling code;
- main-text/supplement kullanım kararı.

Ana analiz birimi metric row sayısı değil,
`study + condition set + comparison group` olur. `118` hiçbir yerde 118 bağımsız
deney veya 118 bağımsız çalışma olarak sunulmaz.

## İzolasyon

1. 27 sayfalık kaynak ZIP/PDF hash ile doğrulanır.
2. Tam revizyon için ayrı fiziksel yazılabilir kopya oluşturulur.
3. Active manuscript ve Phase A--F salt okunur kalır.
4. Symlink, junction veya hardlink kullanılmaz.
5. Publisher PDF'ler çalışma/release repository'sine alınmaz; yalnız güvenli
   yerel path, bibliyografik identity ve SHA-256 manifesti tutulur.
6. Mevcut dizin Git repository olmadığından, Git branch/worktree ancak ayrı G0
   doğrulaması sonrasında kurulabilir.

## Yasaklar

- Yeni literatür taraması veya geriye dönük outcome seçimi.
- Eksik value/unit/uncertainty/condition tahmini.
- Protocol dışı graph digitization.
- Formül ve lineage olmadan unit normalization.
- Companion report'u ayrı çalışma sayma.
- Incompatible platform leaderboard.
- İnsan doğrulaması tamamlanmadan yeni sayısal manuscript claim'i.
- Eski QA PASS'i yeni source üzerinde geçerli sayma.

## Sürüm zinciri

- `G0-protocol`
- `G1-pilot-locked`
- `G2-double-verified`
- `G3-adjudicated-118-lock`
- `v3.0.0-draft.1`
- `v3.0.0-RC1`
- `v3.0.0-submission`

Her sürüm source hash, evidence-input hash, build log ve PDF hash taşır.

