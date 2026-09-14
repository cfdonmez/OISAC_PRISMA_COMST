# İki yayımlanmış derleme ile önceki ve güncel O-ISAC çalışmamızın karşılaştırması

**Tarih:** 6 Eylül 2026. **İşlem:** Karşılaştırmalı okuma; manuscript düzenlenmedi.

## Esas alınan sürümler

- **Bizim çalışma:** *Optical Integrated Sensing and Communication for 6G Through a Systematic Review of Architectures, Metrics, and Tradeoffs Across Optical Platforms*. `comst-v3-20260906` çalışma ağacındaki 27 sayfalık PDF ve onu oluşturan TeX dosyaları. V2 tabanına II. bölümün ilk yeniden yazımı uygulanmış yazar inceleme taslağıdır. Ayrı `comst-full-20260901` RC1 sürümüyle karıştırılmadı.
- **Önceki çalışmamız — Eski 220:** *Optical Integrated Sensing and Communication: A Systematic Review of Fiber, Free-Space, VLC/LiFi, and Photonic-THz Platforms*. Bulunan depo `C:/GH/OISAC_PRISMA_COMST`; esas alınan kaynak `manuscript/finalShortened/bare_jrnl_new_sample4.tex`. Bu TeX dosyasının son commit tarihi 15 Nisan 2026. `current_bundle` ve `finalManuscript` daha erken çalışma katmanlarıdır; sürümler birleştirilmedi.
- **P01:** Zhang vd., *Integrated Sensing and Communications Over the Years: An Evolution Perspective*, IEEE Communications Surveys & Tutorials, 2026; 35 sayfa; DOI 10.1109/COMST.2026.3655674.
- **P02:** Mohsan vd., *Optical integrated sensing and communication: Fundamentals, applications, challenges and future aspects*, Optical Switching and Networking, 2026; 37 sayfa; DOI 10.1016/j.osn.2026.100854.

Dosya kimlikleri ve SHA-256 değerleri [COMPARISON_SNAPSHOT.json](COMPARISON_SNAPSHOT.json) içinde. Bizim bütün bölümler okundu; seçili karşılaştırma, yöntem, veri ve yol haritası sayfaları PDF üzerinden görüldü. P01/P02'nin önceki tam okumaları ve sayfa kayıtları kullanıldı. V3'teki 4,779 satırlık metrik girdisi ayrıca yeniden hesaplandı. Bu çalışma, birincil 206 çalışmanın veya bütün eklerin yeniden doğrulanması değildir. Dış web kullanılmadı.

**Dördüncü eser eklenirken uygulanan sınır:** Kullanıcının isteğiyle bu ek incelemede PDF kullanılmadı. Eski 220'nin özeti ve I–IX bölümleri TeX üzerinden okundu; V3'ün ilgili TeX kaynakları ve önceki P01/P02 okuma notları kullanıldı. Yukarıdaki PDF incelemesi ilk üç eserlik karşılaştırmaya aittir. Kullanıcının yazdığı `C:/GH/OISAC/_PRISMA/_COMST` yolu mevcut değildi; aynı üst klasörde bulunan `C:/GH/OISAC_PRISMA_COMST` deposu kullanıldı. [TeX kaynak kaydı](ONCEKI_SURVEY_TEX_SNAPSHOT.json).

## Ana değerlendirme

**Bizim survey'in en savunulabilir farkı, bir sonucun hangi fiziksel ve ölçümsel koşullarda hangi bilimsel iddiayı destekleyebileceğini sistematik olarak belirlemesidir.** Bu fark iki makalede aynı ayrıntı ve uygulama yapısıyla raporlanmıyor. Ancak mevcut V3, bu katkıyı tarif etme konusunda, onun sağladığı somut mühendislik sonuçlarını gösterme konusunda olduğundan daha ileride.

P01 güçlü bir genel ISAC evrim anlatısı kuruyor. P02 optik alanı deney düzenekleri, dalga biçimleri ve uygulamalarla daha görünür öğretiyor. Bizim metin, kanıtların anlamını ve karşılaştırma sınırlarını daha dikkatli ele alıyor; buna karşılık bazı teknik sonuçları sayısal çalışma noktaları, fiziksel mekanizma çizimleri ve tamamlanmış karşılaştırma örnekleriyle yeterince somutlaştırmıyor. Bu değerlendirme bütün boyutlarda tek bir yayını üstün ilan etmez; her yayının okuyucuya sunduğu farklı işi ayırır.

**Eski 220 eklendiğinde değerlendirme değişiyor:** Sistematik derleme, platformlar arası kapsam, OSNR/SNR ayrımı ve çözünürlük/doğruluk disiplini önceki çalışmamızda da var. Bunlar V3'ün önceki sürümümüze göre yeni katkıları diye sunulamaz. Eski metin fiziksel modelleri ve tasarım denklemlerini daha geniş anlatıyor; V3'ün yeni II. bölümü ise ortak mimari ile gerçekten bağlantılı iki performans sonucunu daha açık ayırıyor. Dolayısıyla revizyon için yararlı yön, eski metnin fiziksel açıklamalarını kaynak ve koşullarıyla yeniden değerlendirerek V3'ün ilişki temelli kanıt çerçevesine bağlamaktır.

## Karşılaştırma matrisi

| Boyut | P01 — Zhang vd. | P02 — Mohsan vd. | Önceki çalışmamız — Eski 220 | Güncel çalışmamız — V3 |
|---|---|---|---|---|
| Merkezî soru | ISAC farklı teknolojik/ağsal eksenlerde nasıl evriliyor? | O-ISAC nasıl çalışıyor, nerelerde uygulanıyor, hangi sorunları var? | Optik platformlar ortak fiziksel temeller, taksonomi ve metrik kurallarıyla nasıl birleştirilebilir? | Hangi ortak tasarım etkeni iki performans sonucunu bağlıyor ve ilişki hangi koşullarda kullanılabilir? |
| Optik kapsam | Geniş RF/ISAC çerçevesinde optik alt bölüm | VLC, FSO, fiber, fotonik sistemler, hibritler | Fiber, FSO, VLC/LiFi, fotonik-THz ve hibritler; enabler ve uygulama bölümleri geniş | Benzer genişlik; fiziksel platform aileleri ve ortak tasarım mekanizmaları üzerinden düzenleniyor |
| Literatür seçimi | Önceki tam okumada yeniden üretilebilir arama/eleme yöntemi raporlanmadığı görüldü | Aynı raporlama sınırı | PRISMA/PRISMA-S, üç veritabanı, 30 Kasım 2025 arama dondurması, 220 çalışma; ilk eleme aşamaları kısmen yeniden kurulmuş | Altı kaynak, 1 Ocak 2020–22 Haziran 2026 dönemi, 227 rapor/206 çalışma; rapor-çalışma ayrımı açık |
| Sentez birimi | Tema, mimari, yöntem, örnek yayın | Teknoloji, deney, uygulama ve sorun | Çalışma düzeyinde dört eksen: ortam, entegrasyon, algılama/alıcı, görev; metrik uygunluk kuralları | Çalışma/rapor/iddia ve koşul düzeyi; yeni II. bölümde P/G/X/C/S/M/E ortak performans ilişkisi |
| Fiziksel sınıflandırma | VLC/FSO/photonic sensing aynı üst düzeyde | Benzer üçlü ve ayrı fiber anlatısı | Fotonik-THz'nin RF yayılımı açıkça anlatılıyor; ancak çok sayıda örnek geniş hibrit sınıfında toplanıyor | Hedefe ulaşan fiziksel yol, optiğin üretim/taşıma rolü ve paylaşım mekanizması daha açık ayrılıyor |
| Metrik disiplini | Çeşitli sayılar ve öğretici modeller | Sayısal deney tabloları; hata tanımları her satırda ortak değil | OSNR/SNR, çözünürlük/doğruluk/CRLB ayrımı zaten güçlü; hız–çözünürlük ve CRQ karşılaştırmaları ek koşul denetimi gerektiriyor | Net/brüt, ölçüm düzlemi, sonuç çifti ve eşzamanlılık daha açık; 118 koşullu kaydın çalışmalar arası kıyas diliyle sunulması halen sorunlu |
| Öğretici teknik görünürlük | Dalga biçimi denklemleri ve ağ mimarileri | Deney düzenekleri, waveform ve optik/fiber mekanizmaları | Kanal ve alıcı modelleri, menzil/CRLB ilişkileri, optimizasyon ve sayısal özetler daha görünür; tam çözülmüş gerçek örnek eksik | Bazı güçlü mekanizma açıklamaları var; yeni çerçevenin tam gerçek örneği ve sayısal tasarım dersi daha az görünür |
| Doğrulama ve yeniden üretim | Veri kümesi kataloğu ve genel değerlendirme | Deney örnekleri ve gelecek gereksinimleri | TQAF, doğrulama anlatısı, asgari raporlama ve benchmark kuralları var | Ayrı bölümde çalışma bazında saha kanıtı, veri/kod erişimi, yeniden kurulabilirlik ve benchmark hazırlığı değerlendiriliyor |
| Gelecek yönler | Evrim eksenlerinden araştırma soruları | Geniş uygulama/teknoloji sorunları | Beş sorun alanı; standart, donanım, kanal, güvenlik, kurulum ve bağımlılıklarla sıralanmış gündem | Beş öncelik, bulgu–eylem–başarı ölçütü ilişkisi; somut teknik çıkarımla bağ güçlendirilebilir |
| Katkının girişte görünürlüğü | Kendi derlemesini karşılaştırma tablosuna koyuyor | Kendi derlemesini karşılaştırma tablosuna koyuyor | “This Review” satırı var; bütün eksenlerde güçlü işaretlenmesi ve önceki yayın listesi yeniden denetlenmeli | P01/P02 zaten tabloda; kendi çalışmamızın satırı eksik, P02'nin teknik kapsamı dar temsil ediliyor |
| Mevcut anlatının ana riski | Optik sınırlar ve bazı atıf/tarih uyuşmazlıkları | Heterojen örnekler ve bazı geniş genellemeler | Genel model/sayısal özetin deneysel üstünlük gibi okunması; geniş hibrit sınıfı ve tekrarlanan karşılaştırma uyarıları | Kanıt yönetimi anlatısının teknik sonuçları gölgelemesi; yeni çerçeve ile eski sonuç dilinin tutarsızlığı |

Eski 220 sütununun TeX satırlarına dayalı gerekçeleri, sürüm sınırları ve V3'e taşınabilecek unsurlar [önceki sürüm karşılaştırma notunda](ONCEKI_SURVEY_ILE_V3_NOTLARI.md) verilmiştir. Aşağıdaki ilk karşılaştırmanın ayrıntıları esas olarak V3 ile P01/P02 arasındaki farkları açıklar; eski sürümümüze göre yenilik iddiası olarak okunmamalıdır.

## Bizim güçlü taraflarımız

### 1. Sistematik derleme yapısı gerçek bir ayrım

Bizim yöntem altı kaynağı, 1 Ocak 2020-22 Haziran 2026 zaman aralığını, uygun raporları ve çalışma eşlemesini açıklıyor: **227 uygun rapor, 206 benzersiz çalışma**. İddialar tanım, birim, ölçüm düzlemi, koşul, doğrulama ortamı ve kaynak konumuyla bağlanıyor. P01/P02'de bu ayrıntıda yeniden üretilebilir bir arama-eleme ve iddia kaydı yapısı raporlanmıyor.

Bu üstünlük doğru sınırlandırılmalı: PRISMA'ya atıf yapmak veya kayıt sayısını artırmak tek başına bilimsel doğruluğu garanti etmez. Bizim sınırlamalarımızda geriye dönük kayıt, tek araştırmacı gözetimi, seçili bağımsız kontroller ve 272/330 tam metin erişimi zaten açıklanıyor. TQAF bu review için geliştirilmiş bir değerlendirmedir; harici olarak geçerlenmiş evrensel kalite ölçeği diye sunulmamalı.

**Kaynak:** Yöntem s.4-7; [03_REVIEW_METHOD_AND_EVIDENCE_BASE.tex](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/03_REVIEW_METHOD_AND_EVIDENCE_BASE.tex:50); sınırlamalar [08_DISCUSSION_ROADMAP_AND_LIMITATIONS.tex](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/08_DISCUSSION_ROADMAP_AND_LIMITATIONS.tex:125).

**Sayım uyarısı:** Bizdeki 206 çalışma, P01'in 248 ve P02'nin 174 kaynakça kaydıyla büyüklük sıralamasına sokulamaz. Ayrıca P02, örneğin Tablo 5'te 2017/2018 çalışmalarını içerirken bizim birincil sentez dönemimiz 2020'de başlıyor. Daha fazla veya daha az kaynak otomatik kapsam/kalite hükmü vermez.

### 2. Optiğin sistemdeki rolü daha temiz tanımlanıyor

Bizde fiberin algılama ortamı olması, yalnız taşıma yapması, fotonik devrenin RF taşıyıcısı üretmesi ve optik ışının doğrudan hedefe ulaşması ayrılıyor. Bu ayrım, fotonik destekli W-band veri hızını FSO hava-kanalı sonucu gibi sunma riskini azaltıyor. P01 ve P02'nin geniş photonic sensing başlığı bu fiziksel eksenleri daha fazla bir araya getiriyor.

Bu, yalnız isimlendirme düzeltmesi değil; hangi yayılım modeli, güç düzlemi, hedef etkileşimi ve alıcı sınırının geçerli olduğunu belirleyen mühendislik farkı.

**Kaynak:** Bizim II. bölüm [02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex:36), IV. bölüm; P01 s.5-8, P02 s.3-6.

### 3. Ortak mimari ile ortak performans kanıtı ayrılıyor

Yeni II. bölümde aynı makalede haberleşme ve algılama sonucu bulunması yeterli kabul edilmiyor. Ortak/değiştirilen etkenin iki sonuca bağlanması ve koşulların izlenebilmesi gerekiyor. `J = <P,G,X,C,S,M,E>` bu ilişkinin kayıt yapısıdır.

Bu yaklaşım bazı eski teknik paragraflarda da uygulanmış: IV. bölümde exposure time üzerinden ortak tasarım, analitik/sayısal sonuç ve ayrı laboratuvar konfigürasyonları ayrılıyor. VI. bölümde de bir çalışmanın iki fonksiyon için saha sonucu vermesi ile iki fonksiyonun aynı zamanda, aynı düzende çalışması aynı iddia sayılmıyor.

**Kaynak:** [04_OPTICAL_PLATFORMS_AND_INTEGRATION_ARCHITECTURES.tex:320](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/04_OPTICAL_PLATFORMS_AND_INTEGRATION_ARCHITECTURES.tex:320); [06_VALIDATION_REPRODUCIBILITY_AND_BENCHMARK_READINESS.tex:71](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/06_VALIDATION_REPRODUCIBILITY_AND_BENCHMARK_READINESS.tex:71).

### 4. Yeniden üretilebilirlik incelemesi somut araştırma çıktısı sağlıyor

V3, 206 çalışma içinde 13 açık veri kaydı; 197 kapalı veya erişim durumu belirtilmeyen kod/model kaydı; kendi ölçütleri altında üç güçlü reproducibility ve sıfır güçlü benchmark readiness sonucu bildiriyor. Bunlar P01'in veri kümesi kataloğundan ve P02'nin genel gelecek önerilerinden farklı bir alan değerlendirmesi.

Burada sıfır güçlü benchmark, alanın hiçbir yararlı benchmark'ı olmadığı anlamına gelmez. Sonuç review'ün bileşik koşullarına bağlıdır. Kapalı ve belirtilmemiş erişimin aynı grupta olduğu da korunmalı. Bu sayılar bu karşılaştırmada ana kaynak verilerinden yeniden doğrulanmadı; mevcut V3 sonuçları olarak değerlendirildi.

**Kaynak:** V3 s.15-17; [06_VALIDATION_REPRODUCIBILITY_AND_BENCHMARK_READINESS.tex:126](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/06_VALIDATION_REPRODUCIBILITY_AND_BENCHMARK_READINESS.tex:126).

## Bizim geliştirmemiz gereken noktalar

### 1. En önemli mevcut tutarsızlık: 118 kayıt ve çalışmalar arası kıyaslama

V3 Tablo V, **118 metrik kaydını “Bounded relation / Conditional comparison across studies”** olarak sunuyor. Yeni II. bölüm ise çalışmalar arası sayısal kıyas için en az iki bağımsız çalışmadan gelen, fiziksel bağlamı ve ölçüm koşulları hizalanmış ilişkiler istiyor.

V3'ün doğrudan kullandığı `ST-19_PRIMARY_METRIC_RESULTS_4779.csv` üzerinde hesapladığım sonuç:

| Kontrol | Sonuç |
|---|---:|
| Toplam metrik kaydı | 4,779 |
| `yes_with_conditions` etiketli kayıt | 118 |
| Bu kayıtların ait olduğu benzersiz çalışma | 15 |
| Bu kayıtların boş olmayan karşılaştırma grubu | 76 |
| Birden fazla çalışmayı içeren grup | **0** |

**Yorum:** Koşullu kullanıma işaretlenen metrik kayıtları, bu girdide kurulmuş bağımsız çalışmalar arası karşılaştırmalara dönüşmüyor. Tablo dili ile veri grubunun fiilen gösterdiği şey aynı değil. Bu 118 kaydın değersiz/yanlış olduğu sonucu çıkmaz; “koşullu aday kayıt”, “çalışma içi ilişki” ve “gerçekleştirilmiş çalışmalar arası kıyas” ayrı tutulmalı.

Aynı CSV'nin bu 118 satırındaki `independent_human_status` alanı `not_documented`. Bu, başka bir sürümde insan doğrulaması yapılmadığı iddiası değildir; önceki RC1 durumunu mevcut V3 girdisine kendiliğinden taşıyamayacağımızı gösterir. Bu incelemede insan onayı verilmedi veya değiştirilmedi.

**Kaynak:** V3 PDF s.10; [05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex:63](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex:63), aynı dosya sonda satır 552; yeni koşul [02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex:217](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex:217). Hesap girdisi ve ayrıntı [COMPARISON_SNAPSHOT.json](COMPARISON_SNAPSHOT.json) içinde.

### 2. Çerçeveyi bir gerçek örnek üzerinde baştan sona göstermiyoruz

Yeni II. bölüm iyi bir karar sistemi tarif ediyor. Ancak okuyucuya bir gerçek çalışmanın P/G/X/C/S/M/E alanlarını, kaynak konumlarını ve çıkan iddia sınıfını birlikte gösteren tamamlanmış örnek sunulmuyor. IV-VI'da bazı iyi uygulamalar var; çerçevenin bütün karar zinciri görünür değil.

Bu nedenle matematiksel tuple'ı doğrudan yeni fiziksel teori gibi sunmak uygun olmaz. Katkısı, kanıtın nasıl yapılandırılıp değerlendirileceğidir. Fiziksel teori veya tasarım sonucu bakımından getirisi, uygulandığı örneğin neyi değiştirdiğiyle gösterilmeli.

### 3. P02, bazı mekanizmaları daha somut öğretiyor

P02 s.10-11 ortak fiber/dalga biçimi örneğini LFM, SBS, SPM ve dispersiyon etkileşimi üzerinden açıklıyor. 56 Gbit/s, 24.5 km, 4 m, 42 kHz gibi bir düzenin ölçeğini; 7 dB optimum launch-power farkı ve yaklaşık 1.3 dB performans kazancını farklı karşılaştırmalar olarak veriyor. S.12 ve 17'de deney tabloları, diğer sayfalarda deney ve alıcı çizimleri bulunuyor.

Bizim V. bölüm güç oranı arttığında sensing SNR ve BER'in birlikte değiştiğini söylüyor; ancak çoğu örnekte hangi güç aralığı, ne kadar değişim, hangi eşik veya hangi eğri olduğunu ana metinde göstermiyor. Sayılar ağırlıkla çalışma/kayıt dağılımlarına ait. Bu, karşılaştırma disiplininin teknik sezgi üretme işlevini kısmen saklıyor.

P02'nin bütün rakamlarını örnek almak veya uyumsuz performansları sıralamak gerekmiyor. Az sayıda, koşulları korunmuş çalışma içi deney örneği bizim yaklaşımımızın farkını daha iyi gösterebilir.

**Kaynak:** [05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex:313](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex:313), P02 s.10-12 ve Fig.8. P01 de s.11-13'te FMCW/OFDM/OTFS ve amaç fonksiyonlarını açıklayarak farklı bir öğretici avantaj sunuyor. Fazla denklem tek başına kalite değildir; burada mesele savı taşıyan fiziksel açıklamanın görünürlüğüdür.

### 4. Şekillerimiz kanıt yapısını gösteriyor; fiziksel sonuçları daha az gösteriyor

V3'te sekiz şeklin ana işleri ilişki/karar şeması, PRISMA, appraisal, paylaşım kategorileri, tradeoff kayıt dağılımları, validation ve teknoloji-uygulama ilişkisi. Özellikle Fig.6 hangi mekanizmadan kaç kayıt bulunduğunu ve koşula bağlılık oranını gösteriyor; bir tasarım değişkeninin C ve S üzerindeki nicel etkisini göstermiyor.

P01'in ağ/dalga biçimi çizimleri ve P02'nin optik düzenek, sinyal ve sonuç panelleri okuyucuya sistemi görerek anlama olanağı veriyor. Bizim Fig.1-2'nin geçici çizim olduğu V3 README'sinde zaten belirtilmiş. Revizyonda sayılarını artırmaktan ziyade bazı görsellerin fiziksel mekanizma veya doğrulanmış çalışma içi ilişki öğretmesi daha yararlı olur.

### 5. Önceki çalışmalarla farkımız girişte yeterince dengeli ve görünür değil

**İki makale de zaten kaynakçamızda ve Tablo I'de var.** Sorun eksik atıf değil. P02'nin fiziksel kapsamı doğru yazılmış; fakat yalnız “Applications and challenges across platforms” ailesine konması, fiber/DOFS, waveform, donanım ve deney tablolarını olduğundan az temsil ediyor.

Tablo I'de ayrıca “This survey” satırı yok. P01 Tablo I ve P02 Tablo 3 bu öz karşılaştırmayı açıkça yapıyor. Bizde katkılar tablo dışında veriliyor; okuyucunun önceki kapsam ile bizim getirdiğimiz yeni işi kendisinin birleştirmesi gerekiyor.

Fark, önceki derlemelerin teknik içeriğini daraltarak kurulamaz. Adil tanımlama sonrasında çalışma-rapor-iddia bağlantısı, ölçüm düzlemi/koşul hizalama, ilişki düzeyindeki karar ve veri temelli doğrulama değerlendirmesi öne çıkarılabilir.

**Kaynak:** V3 s.1-2; [01_INTRODUCTION.tex:117](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/01_INTRODUCTION.tex:117); P01 s.3, P02 s.4.

### 6. Bazı sonuçlar mühendislik dersinden çok raporlama gereğine dönüyor

Metinde güçlü sentez örnekleri de var: sequence shaping ile girişimin oluşumunu azaltma, DC offset ile enerjiyi yeniden dağıtma karşılaştırması aynı sonuç çiftinin neden farklı davranabileceğini açıklıyor. Geniş linewidth lazer ile DSP yükünün değişimi de yararlı bir mühendislik dersi.

Ancak bu düzey bütün teknik paragraflara yayılmıyor. Uzun kaynak grupları çoğu zaman “koşullar korunmalıdır” sonucuna dönüyor. Sonuç ve yol haritası da ölçüm, izlenebilirlik ve artifact temasına ağırlık veriyor. Okuyucu, daha dikkatli değerlendirme yapmayı öğrenirken hangi tasarım kararının hangi durumda yararlı olduğu konusunda daha az somut sonuçla ayrılabilir.

**Kaynak:** İyi sentez [05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex:370](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/05_PERFORMANCE_METRICS_AND_JOINT_DESIGN_TRADEOFFS.tex:370) ve satır 509; geliştirme alanları aynı dosya satır 243-302 ve [09_CONCLUSION.tex:12](C:/OISAC/worktrees/comst-v3-20260906/manuscript/sections/09_CONCLUSION.tex:12).

İki küçük teknik anlatım noktası da gözden geçirilmeli: zero-padding/transform length ile fiziksel resolution aynı cümlede ayrışmadan geçiyor (V, satır 485); pilot sembol sapmasının hangi çevresel/hedef değişkeni temsil ettiği yeterince açıklanmıyor (V, satır 167). Bunlar birincil çalışmanın hatalı olduğu hükmü değil, kendi metnimizdeki tanım/yorum açıklığı sorunlarıdır.

## Revizyon açısından karşılaştırmanın işaret ettiği yön

Bu dört metne göre en uygun yön, sistematik kanıt yaklaşımını koruyup onun sağladığı **somut teknik anlayışı** daha görünür hale getirmektir. Önceki çalışmamızın fiziksel temelleri bu amaçla yeniden değerlendirilebilir; eski hız–çözünürlük/CRQ özetleri ile yeni 118 kayıt doğrudan birleştirilemez. Bunun için tartışılacak ilk üç iş şunlar olabilir:

1. Yeni II. bölümün tanımlarıyla sonuç bölümündeki kayıt/ilişki/karşılaştırma dilini uzlaştırmak; özellikle 118 sayısının kullanımını düzeltmek.
2. Az sayıda gerçek çalışmada tam ilişki kaydını, fiziksel mekanizmayı, kaynakta bildirilen C/S sonuçlarını ve çıkan tasarım dersini bir arada göstermek.
3. Girişte P01/P02'yi adil temsil edip, çalışmamızın hangi yeni soruyu hangi somut çıktı ile cevapladığını doğrudan karşılaştırmak.

Yeni platform, bölüm veya iddia eklenmesine bu raporla karar verilmedi. Kullanıcıyla sonraki adım belirlenmeden manuscript değişmedi.

## Kaynak dosyalar

- [Önceki çalışmamızın incelenen TeX kaynağı](C:/GH/OISAC_PRISMA_COMST/manuscript/finalShortened/bare_jrnl_new_sample4.tex)
- [Bizim güncel V3 PDF](C:/OISAC/worktrees/comst-v3-20260906/output/pdf/OISAC_COMST_V3_WORKING_DRAFT_2026-09-06.pdf)
- [P01 PDF](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P01/1.pdf) ve [ayrıntılı notları](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P01/OKUMA_NOTLARI.md)
- [P02 PDF](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P02/2.pdf) ve [ayrıntılı notları](C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/P02/OKUMA_NOTLARI.md)
- [V3 sürüm açıklaması](C:/OISAC/worktrees/comst-v3-20260906/README_V3_WORKING_DRAFT.md)
- [V3 metrik girdisi](C:/OISAC/worktrees/comst-v3-20260906/evidence/inputs/ST-19_PRIMARY_METRIC_RESULTS_4779.csv)
