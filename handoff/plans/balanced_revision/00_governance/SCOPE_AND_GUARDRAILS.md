# Kapsam ve Koruma Kuralları — Dengeli Revizyon

Durum: `PROPOSED_LOCK`

## Korunan otoriteler

- Active 27-page manuscript ve donmuş Overleaf kaynak paketi salt okunurdur.
- Phase A--F eligibility, report-to-study mapping, PRISMA, extraction, TQAF ve
  synthesis dosyaları değiştirilmez.
- 206 çalışma, 227 eligible report, 4,779 primary metric record ve 402
  substantive tradeoff ilişkisi yeniden hesaplanmaz.
- 76 COMST makale korpusu yalnız yazım/organizasyon benchmark'ıdır; O-ISAC
  bilimsel kanıt otoritesi değildir.

## Uygulama izolasyonu

1. G0'da gönderilen 27 sayfalık kaynak paket hash ile doğrulanır.
2. Dengeli seçenek için ayrı fiziksel yazılabilir kopya oluşturulur.
3. Kanonik manuscript ile junction, symlink veya hardlink kurulmaz.
4. Kaynak PDF'ler Git'e ya da teslim paketine eklenmez; güvenli yerel yol ve
   SHA-256 manifesti tutulur.
5. Mevcut dizin Git repository olmadığı için, branch/worktree iddiası yalnız
   doğrulanmış yeni baseline repository kurulursa kullanılabilir.

## Bilimsel sınırlar

- Analiz birimi `study + condition set + comparison group` olur; metric row
  sayısı bağımsız deney sayısı gibi sunulmaz.
- Uyumsuz modality, metrik tanımı, unit, measurement plane, validation type,
  scenario veya baseline taşıyan sonuçlar aynı leaderboard'a girmez.
- Birim dönüşümü yalnız önceden tanımlı formül, girdi lineage'ı ve insan onayı
  varsa yapılabilir.
- Grafikten sayısallaştırma bu revizyonda varsayılan olarak yasaktır.
- Eksik değer tahmin edilmez; `NR`, `UNC` veya `not_eligible_for_card` olarak
  kaydedilir.
- Sadece olumlu rekorlar seçilemez. En az iki degradation/constraint/tradeoff
  sonucu hedeflenir.
- Seçim protokolü sonuçlar görülerek geriye dönük gevşetilemez.

## Düzeltme politikası

Kaynak yeniden okuması kanonik Phase D satırında hata bulursa eski dosya
üzerine yazılmaz. `proposed_correction`, eski değer, yeni değer, gerekçe,
kaynak lokatörü ve onaylayan roller ayrı overlay kaydında tutulur. Kanonik
değişiklik ancak ekip ayrıca onaylarsa bağımsız bilimsel amendment olarak ele
alınır.

## Editoryal sınırlar

- Yeni gönderim hedefi `<=30` çift sütun sayfadır; operasyonel hedef 29--30'dur.
- Font küçültme, negatif `vspace` veya okunaksız tabloyla sayfa kazanılmaz.
- Mevcut Table V, Figure 6 ve Table VIII mümkün olduğunca yeniden
  işlevlendirilir; gereksiz yeni float eklenmez.
- Prose tabloyu satır satır tekrar etmez.

