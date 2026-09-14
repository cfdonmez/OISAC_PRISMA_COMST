# Devir paketi rehberi

Önce [state.md](state.md), ardından
[güncel yazım kararları](../governance/V3_ACTIVE_WRITING_RULES.md) okunur.
Aşağıdaki ayrıntılar yalnız ilgili görev için açılmalıdır.

| İhtiyaç | Konum |
|---|---|
| Güncel makale / okuma kopyası | [manuscript](../manuscript/), [review.pdf](../output/pdf/review.pdf) |
| V3 reçeteleri, figür promptları, uygulama geçmişi | [governance](../governance/) |
| Yöntemlerin yeni yerleşimi ve açık OSF işi | [review.md](../governance/review.md), [plan.md](maps/s3/plan.md) |
| Bilimsel supplement ve kaynak taşıyıcıları | [methods.md](../supplement/methods.md), [index.md](../supplement/index.md), [v10](../supplement/v10/) |
| Section III benzerlik/kanıt/anlatı haritası ve öneriler | [maps/s3](maps/s3/) — `map.md`, `plan.md`, `s3a.md`; önceki haritalar da saklı |
| Section II anlatı ve COMST karşılaştırması | [maps/s2](maps/s2/) |
| Kullanıcının P01/P02 çalışmaları için okuma notları | [maps/p01-p02](maps/p01-p02/) |
| Önceki survey ve TeX karşılaştırmaları | [maps/surveys](maps/surveys/) |
| COMST house style / claim-language reçetesi | [style](style/) |
| Genel PRISMA know-how | [prisma/workflow/08_bilgi_notlari](prisma/workflow/08_bilgi_notlari/) |
| Asıl proje Codex memory bank | [codex_memory_bank.md](prisma/workflow/09_kayitlar/codex_memory_bank.md) |
| Karar ve ilerleme kayıtları | [decision_log.md](prisma/workflow/09_kayitlar/decision_log.md), [progress_tracker.md](prisma/workflow/09_kayitlar/progress_tracker.md) |
| Önceki proje bağlamı | [context.md](prisma/context.md), [start.md](prisma/start.md) |
| Codex'in ilgili yerel hafıza kayıtları | [history/memory.md](history/memory.md), `history/r01.md`–`r07.md`; [eşleme](history/index.json) |
| Tam makale ilişki mimarisi ve revizyon senaryoları | [plans](plans/) — tarihsel adaylar, kendi onay durumlarıyla |
| RC1 / G6–G7 kanıt kilidi geçmişi | [rc1](rc1/) — V3 onayı sayılmaz |
| Özgün konum, byte boyutu ve SHA-256 | [files.json](files.json) |
| Yeni bilgisayarda bütünlük kontrolü | [verify.py](verify.py) |

## Tarih ve otorite

`history`, `prisma`, `plans`, `style` ve `rc1` altında kaynaklar tarihsel
halleriyle korunur. Eski Section III/V/IX numaraları, erken corpus sayıları,
prospektif planlar, GRADE taslakları veya figür üretim yasakları güncel kararı
otomatik olarak değiştirmez. Eski mimari adayının adı bir onay değildir.
14 Eylül yöntem yerleşimi ve en son yazar talimatı esas alınır.

V10 kaynakları frozen snapshot'tır. PRISMA know-how, gerçek uygulanmış süreç
kaydıyla birlikte okunur. Eski raporlama uyum matrisi tamamlanmış güncel PRISMA
checklist yerine geçmez. COMST031 ile ilgili tarihsel metadata sorunu açıktır.

## Taşınabilirlik ve kapsam

`files.json`, eski mutlak dosya konumunu yeni repo konumuna eşler. Özgün
hafıza/analiz kayıtlarının içindeki `C:/...` ve `C:\...` yolları tarihsel kaynak
adresleridir; diğer bilgisayarda mevcut oldukları varsayılmaz. Güncel başlangıç
ve supplement bağlantıları göreli yollardır. Eski bir kaynaktaki dosyayı ararken
önce bu manifestte arayın.

Proje kaynakları, yazdığımız notlar, reçeteler, hafıza özetleri, geçmiş yerel
revizyonlar ve QA çıktıları taşınır. Global Codex kimlik bilgileri, hesap/eklenti
ayarları, tarayıcı profilleri, başka projelerin özel hafızası ve ham sohbet
veritabanları bu bilimsel devir paketine dahil değildir. Yeni cihazda kendi
Codex hesabınıza giriş yapın; `.codex` klasörünü bu repodan kurmayın.

P01/P02 ve COMST için authored analizler, bibliyografya, kaynak envanterleri ve
sayfa/bölüm eşlemeleri bulunur. Yayıncı PDF'leri ve tam metin kopyaları yeni
pakete eklenmemiştir. İleride bir özgün iddiayı yeniden denetlemek gerekirse
envanterdeki DOI/kaynak ve sayfa bilgileriyle asıl yayına erişilmelidir.
Eski COMST corpus'u repo `main` geçmişindeki `data/corp_std` alanıyla ilişkilidir;
V3 dalına otomatik birleştirilmez. Kanıtı bulmadan yeniden doğrulanmış demeyin.

## Betikler ve eski QA

Normal makale derlemesi hazır figürleri kullanır. `qa/review/selection.py`
(governance altında) yeniden üretim için ReportLab, pypdf ve Windows Arial
font yollarını kullanır; başka işletim sisteminde font yolları uyarlanmalıdır.
Eski analiz betikleri de yerel kaynak yolları içerebilir; otomatik çalıştırılmaz.

`governance/qa/review/check.py` yalnız kontrol etmez: PDF, fark ve `result.json`
yazar. Yeniden çalıştırılması sonradan eklenen görsel inceleme kanıtlarını
silebilir. Yeni doğrulamayı ayrı sonuç dosyasına yazın; kayıtlı QA'yı koruyun.
`output/pdf` içindeki eski sürümler ve `governance` yedekleri tarihsel kanıttır;
güncel okuma kopyası yalnız `review.pdf` olarak belirtilmiştir.
