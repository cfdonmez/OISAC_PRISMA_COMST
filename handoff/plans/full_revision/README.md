# Tam Revizyon Çalışma Ağacı

Durum: `PLAN_READY_EXECUTION_NOT_STARTED`

Bu seçenek, hoca yorumunu yalnız birkaç örnek ekleyerek değil, koşullu teknik
karşılaştırmaya aday 118 kaydın tamamını kaynak PDF düzeyinde yeniden
doğrulayarak ele alır. Sonuç, yeni bir corpus taraması değil, kilitli Phase A--F
üzerinde versioned bir `Phase G conditional-comparison overlay` olur.

## Somut teslim vaadi

- 118/118 kayıt için iki bağımsız insan doğrulaması;
- 15 çalışma / 16 rapor study-report crosswalk'ı;
- bütün uyuşmazlıkların kıdemli üçüncü kişiyle adjudication'ı;
- verified, corrected, rejected ve non-poolable kayıtları koruyan Phase G
  provenance/errata katmanı;
- condition-complete comparison-group kataloğu;
- ana metinde 12--20 temsilî teknik anchor ve supplementte 118 kayıtlık tam atlas;
- Sections IV--VIII'in taxonomy -> conditional comparison -> lessons learned ->
  research action zinciriyle yeniden yazılması;
- her roadmap önceliği için hipotez, benchmark, baseline, stress sweep, success
  measure ve artifact/dependency;
- yeni bütün sayısal iddialar için TeX-to-source traceability crosswalk.

## Kapsam

- 4,779 primary metric kayıt içindeki 118
  `cross_study_quantitative_comparison_allowed=yes_with_conditions` satırı.
- 106 dolu numeric value, 15 study cluster, 16 source report.
- 118 satırın tamamı çift insan doğrulamasına girer; “başarısız” kayıt silinmez,
  overlay'de gerekçeli `rejected_after_human_verification` olur.
- Yeni arama, yeni inclusion/exclusion, yeni PRISMA sayımı ve Phase A--F
  overwrite yapılmaz.
- Meta-analiz yalnız bağımsız çalışma, ortak outcome tanımı, uncertainty ve
  alignment gerçekten yeterliyse ayrı yöntem onayıyla düşünülebilir. Varsayılan
  ürün pooled effect değil, bounded comparison ve gerekçeli non-pooling'dir.

## İş akışı

`G0 baseline -> amendment/protocol -> 12-row pilot -> 16 report packet ->
Reviewer 1 ve 2 -> adjudication -> VERIFIED_118_LOCK -> comparison groups ->
Sections IV--VIII + front/back matter -> supplement -> 30-page/build/render QA ->
independent reader/scientific audit -> author release`

## Bu ağacın dosyaları

- `00_governance/`: Phase G amendment, koruma kuralları ve kapılar.
- `01_verification/`: pilot, çift review, adjudication ve 118-row register.
- `02_analysis/`: comparison groups, non-pooling, main-text selection ve trace.
- `03_manuscript/`: bölüm yeniden yazım haritası ve sayfa bütçesi.
- `04_qa/`: scientific, reader-value, build ve release acceptance.
- `05_management/`: WBS, takvim, RACI ve riskler.
- `06_outputs/`: versioned supplement ve release sözleşmesi.

Tahmini emek 99--124 kişi-saat; iki reviewer paralel ve roller hazırsa 3--4
takvim haftasıdır. Bu tahmin kaynak rapor erişiminin hazır olduğunu varsayar.
