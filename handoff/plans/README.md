# O-ISAC COMST Revizyon Senaryoları

Tarih: 2026-09-01  
Durum: `PLAN_ONLY_NOT_EXECUTED`

Bu klasör, hoca yorumunu iki farklı kapsamla ele almak için hazırlanmış iki
bağımsız çalışma ağacını içerir:

1. `balanced_revision/`: hızlı gönderim hedefini koruyan, seçilmiş ve çift
   insan doğrulamalı teknik kanıta dayanan dengeli revizyon.
2. `full_revision/`: koşullu karşılaştırmaya açık 118 kaydın tamamını yeniden
   doğrulayan ve Section IV--VIII'i kapsamlı biçimde yeniden kuran tam revizyon.

İki ağaç birbirinden bağımsızdır. Bir seçenekte üretilen taslak, doğrulama
formu, tablo, şekil veya QA çıktısı diğer seçeneğin girdisi sayılmaz. Ortak
olabilecek olgusal bir düzeltme dahi önce kaynakla doğrulanır, sonra iki ağaca
ayrı değişiklik kaydıyla uygulanır.

## Korunan başlangıç otoritesi

- Aktif manuscript:
  `systematic_review_workflow/07_raporlama/outputs/comst_prose_revision_2026-08-08/manuscript/comst_206_v2_9section/`
- Referans PDF: 27 sayfa; SHA-256
  `6A195C6856E5BD784DEF0A5149B1DF025771E5E50D7B2C02A7D229108B450DC2`.
- Donmuş Overleaf kaynak paketi: SHA-256
  `FD69AD68C68B6408FF1B0CE5E584156F6B773FA78F199ADEDF0C9440B648AC88`.
- Sayısal kanıt evreni: 4,779 satırlı `ST-19_PRIMARY_METRIC_RESULTS_4779.csv`.
- Koşullu karşılaştırma bayrağı taşıyan evren: 118 satır, 15 çalışma kümesi,
  16 kaynak rapor; bunların 106'sında `value_numeric` doludur.
- Bu 118 satırın tamamında `independent_human_status=not_documented` olduğu
  için ana metne alınacak her sayı yeniden insan doğrulamasından geçecektir.

## Bu hazırlıkta yapılmayanlar

- Aktif manuscript veya kilitli Phase A--F dosyaları değiştirilmedi.
- Gerçek bir Git branch/worktree oluşturulmadı. Mevcut `C:\OISAC` ve
  `prisma2020Review` dizinleri şu anda Git çalışma ağacı olarak doğrulanmıyor.
- Kaynak PDF'ler kopyalanmadı.
- 118 kayıt üzerinde yeni bilimsel karar verilmedi.
- LaTeX revizyonu, derleme veya submission yapılmadı.

Gerçek uygulama başladığında ilk adım, hocalara gönderilen 27 sayfalık kaynak
paketin hash ile dondurulması ve iki yazılabilir kopyanın aynı doğrulanmış
baseline'dan üretilmesidir. Recovery klasörlerinden biri doğrulama yapılmadan
başlangıç noktası seçilmeyecektir.

## Klasörler

- [Senaryo karşılaştırması](SCENARIO_COMPARISON.md)
- [Dengeli revizyon planı](balanced_revision/README.md)
- [Tam revizyon planı](full_revision/README.md)
- [Plan QA raporu](PLAN_QA_REPORT.md)

## COMST tasarım dayanağı

Planlar, yerel 76-COMST korpusunu yalnız style/architecture benchmark olarak
kullanır. Ayrıca güncel resmi COMST author/reviewer rehberindeki üç hard yönü
uygular: yeni manuscript `<=30` çift sütun sayfa olmalı; reader usefulness
reviewer'ın en önemli değerlendirme konusudur; reviewer formu lessons learned
ve okuyucunun kendi çalışmasında hatalardan kaçınmasına yardım eden içeriği
açıkça sorgular. Resmi kaynak:
<https://www.comsoc.org/publications/journals/ieee-comst/policies-guidelines>.

İki plan da şu ortak soruyu yanıtlamayı hedefler:

> O-ISAC alanına yeni giren bir araştırmacı bu survey'den hangi yöntemin hangi
> koşulda anlamlı olduğunu, hangi sonucun neye karşı elde edildiğini, hangi
> sınırın sonucu taşımasını engellediğini ve sıradaki deneyi nasıl kuracağını
> öğrenebiliyor mu?

