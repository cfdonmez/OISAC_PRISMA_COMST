from pathlib import Path
import hashlib
import json
import re
import shutil

OUT = Path(__file__).parent
ROOT = Path('C:/OISAC/worktrees/comst-v3-20260906')
SECTION = ROOT / 'manuscript/sections/03_REVIEW_METHOD_AND_EVIDENCE_BASE.tex'
records = json.loads((OUT / 'scan.json').read_text(encoding='utf-8'))
sources = {r['id']: Path(r['path']) for r in records}
sources.update({k: Path(f'C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06/{k}/reading_text.md') for k in ['P01', 'P02']})
qa = json.loads((OUT / 'qa.json').read_text(encoding='utf-8'))


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


assert digest(SECTION) == qa['section3_sha256'], 'Section III changed; review current source first'
assert all(digest(sources[r['id']]) == r['sha256'] for r in records)
before = {p: digest(p) for p in (ROOT / 'manuscript/sections').glob('*.tex')}
before.update({sources[k]: digest(sources[k]) for k in ['P01', 'P02']})


def link(key, start, end=None, label=None):
    p = SECTION if key == 'ours' else sources[key]
    n = len(p.read_text(encoding='utf-8-sig').splitlines())
    assert 1 <= start <= (end or start) <= n
    label = label or (f'L{start}–{end}' if end else f'L{start}')
    return f'[{label}]({p.as_posix()}:{start})'


def art(key, name, label):
    p = sources[key].parent / name
    assert p.is_file()
    return f'[{label}]({p.as_posix()})'


def table(headers, rows):
    assert all(len(r) == len(headers) for r in rows)
    assert all('|' not in cell and '\n' not in cell for r in rows for cell in r)
    return '\n'.join(['| ' + ' | '.join(headers) + ' |', '|' + '---|' * len(headers)] + ['| ' + ' | '.join(r) + ' |' for r in rows])


method_rows = [
    ['COMST_010 — yaklaşık uç yapay zekâ; II-G',
     'Literatürdeki ihtiyaç → araştırma sorusu/amaç → arama → kapsam ölçütleri → katkıya göre sınıflandırma → karşılaştırma. ' + link('COMST_010', 280, 300),
     'Fig. 5, beş adımı aynı akışta gösteriyor; ' + art('COMST_010', '_page_7_Figure_10.jpeg', 'görsel') + ' · ' + link('COMST_010', 288, label='başlık'),
     'Okura yayın listesinin hangi işlemlerden geçerek karşılaştırmaya dönüştüğünü gösteriyor.',
     'III-A/B/C geçişlerini aynı neden–sonuç bağıyla açıklaştırabiliriz. Bizdeki Fig. 5 seçim ve rapor–çalışma uzlaştırmasını gösteriyor; bütün yöntem için ikinci bir akış şekli gerekmiyor. Kaynağın arama araçları veya işlemleri bize yapılmış işlem olarak aktarılamaz.'],
    ['COMST_038 — siber fiziksel sistemlerde adversarial ML; I-B/I-C',
     'Arama kaynakları ve strateji → iki aşamalı filtre → konu kapsamı ve sınırları. ' + link('COMST_038', 85, 93),
     'İlgili yöntemi taşıyan unsur kısa metin. Fig. 1, AML saldırı yüzeyini anlatıyor; seçim akışı değil. ' + link('COMST_038', 29, label='Fig. 1 başlığı'),
     'Kapsam sınırlarını ayrı bir paragrafta görünür kılıyor; yöntem anlatısı için mutlaka yeni şekil gerekmiyor.',
     'III-A’da uygunluk ve kapsam sınırları korunmalı. Sorgu başına ilk beş sonuç sayfası bu makaleye ait bir sınırlılık; bize önerilen seçim kuralı değil. PRISMA adı geçmesi, ayrıca akış şekli bulunduğunun kanıtı değil.'],
    ['COMST_050 — Industry 5.0; I-C/I-E1',
     'Sorular → arama/seçim → atıf izleme → yinelemeli tematik düzenleme → bölüm kategorileri. ' + link('COMST_050', 162, 195) + ' · ' + link('COMST_050', 223, 229),
     'Fig. 3, konuları bölüm ve alt bölüm numaralarıyla eşliyor; ' + art('COMST_050', '_page_8_Figure_2.jpeg', 'görsel') + '. Tables III–V önceki derlemelerle kapsam/katkı karşılaştırmasıdır.',
     'Kategori ağacı hem kapsamı gösteriyor hem okuyucuyu teknik bölümlere yönlendiriyor. Önceki derleme tabloları ise konumlandırma yapıyor.',
     'III-C sonunda tematik grupların IV–VI’daki görevleri daha somut bağlanabilir. Bu bağ mevcut Table III’ün “Use” sütunu ve son paragrafta kurulabilir. Yayın yeri itibarını kullanan değerlendirmesi TQAF’a eşdeğer değil.'],
    ['COMST_060 — RIS ile radyo konumlama; I-B',
     'Araştırma soruları → Boolean sorgu/IEEE kaynağı → geriye doğru atıf izleme → uygunluk ve sürüm tercihi. ' + link('COMST_060', 75, 95),
     'Table II, önceki derlemelerin araştırma sorularını ne ölçüde ele aldığını gösteriyor. ' + link('COMST_060', 62, label='Table II başlığı') + '. I-B’de ayrı bir seçim şekli doğrulanmadı.',
     'Sorular, hem literatürdeki boşluğu hem aramanın yönünü açıklıyor; tablo dahil edilen çalışmaların kalite matrisi değil.',
     'III-A açılışında seçilen kapsamın teknik sorularımızla ilişkisi kısa tutulabilir. Yayımlanmış sürümü ön baskıya tercih etme, bizdeki çoklu rapor–bağımsız çalışma uzlaştırmasının tamamını karşılamaz.'],
]

comparison_rows = [
    ['COMST_023 — güven modelleri; III ve V-A',
     'Ortak ölçüt ihtiyacı → ölçütlerin tanımı → tekil kaynaklarda gerekçeli uygulama → ortak karşılaştırma matrisi. ' + link('COMST_023', 151, 169) + ' · ' + link('COMST_023', 304, 331),
     'Table VI: kaynak, model/uygulama/teknik, ölçüt sonuçları ve sınırlılıklar. ' + link('COMST_023', 323, 331, 'sütunlar ve örnek satırlar'),
     'Ölçütlerin yalnız ilan edilmediğini, gerçek kaynaklara uygulandığını görünür kılıyor.',
     'TQAF tanımı ile toplu Fig. 6 arasında mevcut doğrulanmış bir kaydın kısa uygulama örneği yararlı olabilir. Teknik model özelliği ile araştırma desteğini ayırmalıyız; ölçütleri veya puanları bu makaleden kopyalamamalıyız.'],
    ['COMST_026 — OWC-IoWT; IV-C1',
     'Deneysel bağlam → düzenek ve koşullarıyla sonuçlar → eşit olmayan deneylerin kıyas sınırı → sınırlı teknik çıkarım. ' + link('COMST_026', 560, 566),
     'Table V: ortam, dalga boyu, topoloji, Tx/Rx, hız, BER, mesafe ve modülasyon aynı satırda. ' + link('COMST_026', 530, 552),
     'Bir performans sayısının koşullarından ayrılarak üstünlük sırasına çevrilemeyeceğini somutlaştırıyor.',
     'III-B’de kaydedilen koşulların III-C’de yorumu nasıl sınırladığı aynı gerçek kayıt üzerinde açıklanabilir. Tablo kapsamlı veya normalize edilmiş bir deney karşılaştırması değil; adil kıyas yapılamayacağını açıkça belirtiyor.'],
    ['COMST_012 — CAN tersine mühendisliği; VI-B',
     'Heterojen deney sorunu → mevcut veri/kod ve doğruluk referansı eksikleri → gerekli koşul alanları → sonuçları birleştirme sınırı. ' + link('COMST_012', 1047, 1072),
     'Ayrı şekil/tablo yerine araç modeli/yılı, kayıt donanımı/yazılımı, sürüş/çevre koşulları ve doğruluk referansı için maddeli liste. ' + link('COMST_012', 1059, 1066),
     'Soyut “karşılaştırılabilirlik” sorununu hangi bilginin gerekli olduğu sorusuna çeviriyor.',
     'Koşul bilgisinin varlığı/yokluğu ile izin verilen yorum arasındaki bağı açıklayabiliriz. Liste, önerilen değerlendirme verisinin özellikleridir; yazarların uyguladığı veri çıkarım formu gibi sunulmamalı. Önceki Fig. 23 bu pasajın kanıt taşıyıcısı değil.'],
    ['COMST_014 — VLP algoritmaları; III-D',
     'Ortak teknik özellikler → donanım ihtiyacı ve avantaj/zayıflıklar → uygulanabilirlik dersleri. ' + link('COMST_014', 392, 396),
     'Table II, LED sayısı, yardımcı donanım ve avantaj/zayıflıkları karşılaştırıyor. ' + link('COMST_014', 353, label='Table II başlığı') + '. Figs. 10–12, III-C’de yazarların sayısal algoritma karşılaştırmasına ait.',
     'Tablodan sonra hangi teknik tercihin hangi sonucu doğurduğunu yorumluyor; tabloyu tek başına bırakmıyor.',
     'Bizde Table III’ün sayımlarından sonra birimlerin sentezde ne işe yaradığını bağlamak yararlı. Teknik alanın yeni deneysel eğrilerini Section III’e taşımak veya bu tabloyu kalite ölçeği saymak uygun değil.'],
    ['COMST_075 — V2X; IV-C',
     'Karşılaştırmalı yayınların haritası → değerlendirme yöntemi/metrik → yoğunluk, uzaklık ve fiziksel katmana bağlı sonuçlar → koşullu özet. ' + link('COMST_075', 787, 803),
     'Table XVI, kaynak/yıl/değerlendirme yöntemi/metrikleri listeliyor; koşula bağlı yorum takip eden metinde kuruluyor. ' + link('COMST_075', 760, 781),
     'Hangi sonuçların hangi değerlendirme yaklaşımından geldiğini gösteriyor. Bütün koşulların tablo sütunlarında bulunduğu varsayılmamalı.',
     'III-B kayıtları ve III-C sentez kuralları birlikte tanıtılmalı. Ayrıntılı teknik üstünlük tartışması sonraki sentez bölümlerine ait; farklı koşullardan evrensel kazanan çıkarılamaz.'],
]

framework_rows = [
    ['COMST_003 — radyo kaynak yönetimi; IV',
     'Karşılaştırma boyutları → alt kategoriler → kaynakların kategorilere yerleştirilmesi. ' + link('COMST_003', 200, 202),
     'Fig. 9, yaklaşım/metrik/model/karmaşıklık/kontrol dallarını ve kaynak numaralarını gösteriyor. ' + art('COMST_003', '_page_7_Figure_4.jpeg', 'görsel') + ' · ' + link('COMST_003', 225, label='başlık'),
     'Kategorilerin adını vermenin ötesinde, literatürün hangi eksenlerle düzenlendiğini gösteriyor.',
     'III-B’de hangi alanın kaydedildiği, III-C’de neye göre gruplandığı bağlanabilir. Teknik taksonominin kendisini III’e taşımak Section II/IV ile tekrar yaratabilir. Görsel bir veri çıkarım denetimi veya kalite puanlaması değil.'],
    ['COMST_025 — anonimlik ağlarında güvenlik; II-F',
     'Varlıklar ve ilişkiler → kapsam/sorular → yukarıdan aşağıya ontoloji ve aşağıdan yukarıya mekanizma okuması. ' + link('COMST_025', 334, 340),
     'Fig. 1, saldırı/zafiyet/savunma gibi öğeleri anlam taşıyan ilişkilerle bağlıyor. ' + art('COMST_025', '_page_4_Figure_2.jpeg', 'görsel') + ' · ' + link('COMST_025', 114, label='başlık'),
     'Sentezin yalnız konu kümeleri değil, öğeler arasındaki ilişkiler üzerinden de kurulabileceğini gösteriyor. Şekil yöntem alt bölümünden önce yer alıyor.',
     'III-B’deki ilişki kayıtlarının faktör–koşul–sonuç bağını koruduğunu, III-C’de bu kayıtlarla nasıl koşullu mekanizma yorumu yapıldığını açıklayabiliriz. Yeni büyük ontoloji şekli zorunlu değil; nedensellik kanıtı veya kalite ölçeği aktarmıyoruz.'],
    ['P01 — ISAC evrimi; I-B/I-C ve II-D',
     'Önceki derlemelerde kapsam farkı → beş evrim ekseni → bölüm düzeni → dersler. ' + link('P01', 129, 214) + ' · ' + link('P01', 225, 233) + ' · ' + link('P01', 600, 625),
     'Table I, önceki derlemelerin odak ve uygulama kapsamını karşılaştırıyor. ' + link('P01', 222, 223) + '. Organizasyon paragrafı Fig. 1’e yönlendiriyor.',
     'Okur, seçilen anlatı eksenlerinin kapsam boşluğuyla bağını izleyebiliyor; lessons learned bu çerçevenin teknik çıktısı.',
     'III’te yöntem adımlarını sonraki teknik çıktılarla bağlamak için anlatı örneği. Önceki derleme karşılaştırmasını III’e taşımayalım; seçim/çıkarım/değerlendirme protokolü yerine kullanmayalım. P01’in Section III’ü ağ mimarisidir.'],
    ['P02 — optik ISAC; 3.5 ve 7',
     'Deneysel çalışmalar → yöntem/sonuç/düzenek karşılaştırması; ileride uygulama eksikleri ve gelecek yönleri. ' + link('P02', 979, 1004) + ' · ' + link('P02', 2596, 2607),
     'Table 5, modülasyon/algoritma/hız/doğruluk/Tx–Rx/test alanını; Table 9, yöntem/algılama nesnesi/fayda/gelecek yönlerini topluyor. ' + link('P02', 1038, 1054, 'Table 5') + ' · ' + link('P02', 2823, 2834, 'Table 9'),
     'Table 5 koşullu deney kaydına, Table 9 ise teknik sentez çıktısına örnek. Bunlar birbirini doğrudan izleyen tek yöntem alt bölümünde değil.',
     'III-B’de çıkarılan alanların ne işe yaradığını Table 5’in mantığıyla açıklayabiliriz. Büyük çalışma karşılaştırmaları ve gelecek yönleri sonraki teknik bölümlerde kalmalı. Bu tablolar, uygulanmış çıkarım veya kalite değerlendirme protokolünü tek başına kanıtlamıyor.'],
]

ours_rows = [
    ['Açılış ve üçlü yapı', link('ours', 5, 10, 'Mevcut açılış'),
     'Section II ile ilişki ve seçme → çıkarma → değerlendirme sırası zaten açıklanıyor.',
     'Üç alt bölümü koru. Geçişleri “hangi çalışmalar?”, “her çalışmadan hangi koşullu kayıt?”, “bu kayıtla hangi yorum?” sorularına bağla; yeni bir genel giriş ekleme.',
     'COMST_010 Fig. 5; COMST_060 I-B. **Metin düzeni**, yeni veri gerektirmez.'],
    ['III-A ve Fig. 5', link('ours', 15, 63, 'Arama, seçim, akış ve süreç sınırları'),
     'Seçim koşulları ve rapor–çalışma uzlaştırması var. Fig. 5, 227 uygun raporun 206 çalışmayla ilişkisini görünür kılıyor.',
     'Fig. 5’i koru; devamında bu çalışmaların birden çok kodlama kaydı üretebildiğini III-B’ye bağla. Uygunluk ile aynı koşullarda ortak iletişim–algılama karşılaştırmasını ayrı tut. Gerçek insan/AI iş akışı ve geriye dönük kayıt açıklaması korunmalı.',
     'COMST_010/038/060. **Kısa geçiş**; ikinci seçim akışı veya yeni sayım gerekmiyor.'],
    ['III-B: koşullu kayıt', link('ours', 68, 81, 'Çıkarılan alanlar ve ilişkiler'),
     'Kaynak konumu, ölçü/birim/ölçüm noktası, düzenek/koşul/baz çizgi/doğrulama alanları ve ilişki kayıtları tanımlı.',
     'Bu alanların neden birlikte tutulduğunu açıklaştır. Aynı gerçek örnek, hem sonuç koşullarını hem ortak iletişim–algılama noktasının kurulup kurulamadığını gösterebilir; kayıtta bulunmayan bağlantı tamamlanmamalı.',
     'COMST_026 Table V; P02 Table 5; COMST_012 VI-B. **Metin + mevcut doğrulanmış kayıt seçimi**.'],
    ['Table III: analiz birimleri', link('ours', 83, 144, 'Tablo, sayımlar ve açıklamalar'),
     '206 çalışma, 8.203 birincil kodlama kaydı, 4.779 metrik kaydı, 402 ilişki ve 115 sentez grubunun anlamını/kullanımını ayırıyor; kategoriler yeni bağımsız çalışma sayıları değil.',
     'Sayım tablosunu koru. “Meaning/Use” açıklamalarını okurun birim → sonraki kullanım bağını izleyeceği şekilde güçlendir. Büyük bir deney karşılaştırma tablosuna dönüştürme; örneği gerekirse bitişik kısa paragrafta göster.',
     'COMST_003 Fig. 9; COMST_050 Fig. 3. **Mevcut tablo/metin açıklığı**; yeni sayım yok.'],
    ['III-C: TQAF tanımı ve uygulanması', link('ours', 149, 163, 'Boyutlar ve işlevleri'),
     'Sekiz boyut, 0–3 değerlendirme, ayrı genel katkı ve yorum/doğrulama/yeniden kullanım işlevleri var. Bağımsız doğrulanmış veya klasik yanlılık ölçeği olduğu iddia edilmiyor.',
     'Tanımın ardından bir boyutun gerçek kaynak bilgisinden nasıl değerlendirildiğini göster. Teknik desteği, karşılaştırılabilirliği ve sentezde kullanılabilirliği ayrı gerekçelendir; toplam puanı otomatik dahil etme, havuzlama veya üstünlük kuralına dönüştürme.',
     'COMST_023 III + Table VI. **Mevcut değerlendirme kaydı ve kuralı doğrulanmalı**; yeni puan üretme.'],
    ['Fig. 6: toplu değerlendirme profili', link('ours', 165, 175, 'Şekil ve açıklaması'),
     '206 çalışmanın boyutlar üzrə destek dağılımını toplu gösteriyor; tek bir çalışmanın karar gerekçesini gösterme amacı yok.',
     'Şekli koru. Önce ölçütlerin işlevini ve seçilirse tekil uygulama örneğini, sonra toplu profili sun. 0–3 kayıtlarının üç destek grubuna nasıl geçtiğine dair açıklama gerekirse mevcut kuraldan doğrulanmalı.',
     'COMST_023 ölçüt → uygulama düzeni. **Metin ve mevcut kural kontrolü**; şekli yeniden üretmek bu aşamada gerekmiyor.'],
    ['III-C: koşullu sentez ve bölüm geçişi', link('ours', 177, 194, 'Sentez ve IV–VI bağlantısı'),
     'Yedi alan, tema/ilişki grupları, yapılandırılmış anlatısal sentez ve havuzlanmış etki modeli kullanılmaması açıklanıyor. IV–VI geçişi zaten mevcut.',
     'Çıkarılan koşul → değerlendirme gerekçesi → izin verilen yorum bağını somutlaştır. Tema grubu ile faktör–sonuç ilişkisinin görevini ayır. IV’te fiziksel mekanizma/kaynak, V’te performans ilişkisi, VI’da doğrulama için hangi kayıtların işe yaradığına kısa işlev bağı kur.',
     'COMST_025 Fig. 1; COMST_026/075 koşullu yorum; COMST_050 bölüm haritası. **Metin düzeni**, teknik sonuçları III’te yineleme gerekmiyor.'],
]

example_rows = [
    ['Kaynak ve analiz birimi', 'Mevcut çalışma/rapor kimliği, sayfa/şekil/tablo konumu ve ilgili kayıt türü.', 'Kaynak bilgisinin hangi bağımsız çalışmaya bağlandığı.'],
    ['Sonuç ve koşullar', 'Kaynakta bildirilen ölçü, birim, ölçüm noktası, düzenek ve ilgili koşullar; kayıtta gerçekten bulunuyorsa iletişim–algılama eşleşmesi.', 'Sayının hangi şartlar altında anlam taşıdığı; aynı ayarda ölçülmeyen çıktılar ortak nokta gibi birleştirilmez.'],
    ['Teknik değerlendirme', 'Mevcut TQAF boyutu, kayıtlı karar ve o kararı destekleyen kaynak bilgisi; kullanılan mevcut kural.', 'Puanın hangi gözleme dayandığı. Eksik bilgiye ait durum adları yalnız mevcut kodlama destekliyorsa kullanılır.'],
    ['Karşılaştırma ve sentez', 'Mevcut karşılaştırılabilirlik/sentez kuralı, kayıtla gerçekten desteklenen kullanım ve açık kalan koşul.', 'Teknik kalite ile karşılaştırılabilirlik ayrı gerekçelendirilir. Betimleme, koşullu ilişki veya daha güçlü kıyasın hangisinin desteklendiği kayıtla belirlenir.'],
]

priority_rows = [
    ['1 — Önce', 'III-A/B/C geçişlerini ve mevcut Table III/ Fig. 6 çevresindeki neden–sonuç bağını düzenlemek.', 'Mevcut üçlü yapı ve öğeler yeterli temel sunuyor; okuma akışını doğrudan iyileştirir.', 'Mevcut TeX ve bu kaynak eşleştirmesi; yeni veri/şekil yok.'],
    ['2 — Somut örnek', 'Tek bir doğrulanmış çalışma kaydını III-B/C arasında kısa örnek olarak kullanmak.', 'Alan tanımı, uygulanan karar ve izin verilen yorum arasındaki bağı görünür kılar.', 'İlgili kaynak + çıkarım kaydı + mevcut değerlendirme/sentez kuralı birlikte doğrulanmalı. Bu turda örnek seçilmedi.'],
    ['3 — Gerekiyorsa görsel', 'Örnek paragrafla anlaşılmıyorsa küçük bir tablo kullanmak; süreç şekli ancak hâlâ gerçek bir açıklama boşluğu kalırsa düşünülmeli.', 'Fig. 5, Table III ve Fig. 6 zaten farklı görevleri yerine getiriyor; önce örneğin işlevi netleşmeli.', 'Yeni şekil veya tablo üretilmedi. Kaynaklardaki görseller biçim ve anlatı örneği; doğrudan kopyalanacak varlıklar değil.'],
]

headers = ['Kaynak / ilgili yer', 'Anlatının ilerleyişi', 'Şekil, tablo veya diğer destek', 'Anlatıda yaptığı iş', 'Bizim Section III’e öneri ve aktarım sınırı']
addition = '''## Section III’ün kurgusu için bu taramadan çıkan öneri

**Üç alt bölümlü yapı korunabilir. En somut geliştirme fırsatı, kaynaktan çıkarılan bilgiyi değerlendirme gerekçesine ve izin verilen senteze bağlayan kısa bir uygulama örneğidir.** Mevcut açılış bu sırayı zaten kuruyor; yeni öneri, sıranın tek bir gerçek kayıt üzerinde nasıl işlediğini okura göstermek. Fig. 5 seçim/uzlaştırmayı, Table III analiz birimlerini, Fig. 6 toplu değerlendirme profilini taşıyor. Bunlar birbirinin yerine geçmiyor.

Bu sürüm, önceki eşleştirmeyi **11 COMST çalışması + P01/P02** için anlatı ve destekleyici öğe düzeyinde derinleştirir. Aşağıdaki ilk üç tabloda kaynakta gözlenen düzen, son sütunda ise **bizim yorumumuz olan aktarım önerisi** yer alır. Bir derlemenin bu anlatım biçimini kullanması, bizim yöntemin geçerliliğini kanıtlamaz veya dergi için zorunlu biçim oluşturmaz. Bölüm ve öğe numaraları ilgili kaynak makaleye aittir; “bizde” denilenler mevcut taslağı gösterir.

### 1. Kaynak seçimini ve bölüm düzenini anlatan örnekler

''' + table(headers, method_rows) + '''

### 2. Çıkarılan bilgiden gerekçeli karşılaştırmaya geçen örnekler

''' + table(headers, comparison_rows) + '''

### 3. Sınıflandırmayı ve ilişkileri teknik anlatıya bağlayan örnekler

''' + table(headers, framework_rows) + '''

**Okuma ayrımı:** COMST_003 Fig. 9, COMST_010 Fig. 5, COMST_025 Fig. 1 ve COMST_050 Fig. 3’ün yerel görselleri doğrudan incelendi. Diğer şekillere ilişkin sınırlı tespitler başlık ve çevre metne; tablo tespitleri mevcut Markdown sütunlarına, satırlarına ve açıklayıcı paragraflara dayanıyor. Bu, tüm PDF sayfalarının görsel denetimi değildir. Anlatı okları düşüncenin nasıl ilerlediğini özetler; şeklin her zaman bu metnin hemen ardından geldiğini ifade etmez.

### 4. Bizim mevcut Section III’te ne korunmalı, ne geliştirilmeli?

''' + table(['Mevcut parça', 'Taslak konumu', 'Şu anda yaptığı iş', 'Somut geliştirme önerisi', 'Kaynak dayanağı / gereken iş'], ours_rows) + '''

### 5. Tek gerçek örnek nasıl kurulabilir?

Aşağıdaki, **doldurulmuş bir araştırma kaydı değil, önerilen örneğin içerik şemasıdır**. Önce mevcut doğrulanmış kayıtlardan kaynak ve değerlendirme bağlantısı izlenebilen bir örnek seçilmelidir. Aynı örneğin kısa bir kısmı III-B’de, karar ve yorum kısmı III-C’de kullanılabilir; sayfa düzeni uygunsa tek küçük tablo da yeterlidir. Tek örnek bütün derleme sürecini doğrulamaz; sürecin nasıl uygulandığını gösterir.

''' + table(['Örneğin parçası', 'Mevcut kayıttan gösterilecek bilgi', 'Okurun anlayacağı bağ / sınır'], example_rows) + '''

Örneğin en önemli ayrımı şudur: bir çalışmanın kapsama uygunluğu, sonucunun teknik desteği ve başka sonuçlarla karşılaştırılabilirliği farklı kararlardır. TQAF puanından tek başına “havuzlanabilir” veya “üstündür” sonucu üretilmemelidir. “Bildirilmemiş / değerlendirilememiş / yetersiz” gibi durumlar da mevcut kurallarda tanımlı değilse sanki kullanılmış kategorilermiş gibi eklenmemelidir.

### 6. Uygulama önceliği

''' + table(['Sıra', 'Önerilen değişiklik', 'Neden önce bu?', 'Gereken dayanak / mevcut durum'], priority_rows) + '''

Bu turda **yalnız bu Markdown incelemesi güncellendi**. TeX metni, kaynak veriler, puanlar, şekiller ve tablolar değiştirilmedi. Aşağıdaki A–G tabloları, önerilerin dayandığı önceki bölüm eşleştirmesini ve 77 kaydın tarama durumunu korur.

---

'''

target = OUT / 'map.md'
backup = OUT / 'map_v2.md'
assert not backup.exists(), 'Keep the previous report; do not overwrite a prior backup'
old = target.read_text(encoding='utf-8')
assert old.startswith('# Section III için bölüm eşleştirme tablosu')
new = old.replace('# Section III için bölüm eşleştirme tablosu', '# Section III: kaynak eşleştirmesi ve kurgu önerileri', 1)
new = new.replace('## Kapsam ve okuma düzeyi', addition + '## Kapsam ve okuma düzeyi', 1)
new = new.replace('P01/P02’nin önceki hedefli okuma sonuçları korundu; bu turda yeniden tam okuma yapılmadı.', 'P01/P02’nin önceki hedefli okuma sonuçları korundu; üçüncü geçişte ilgili anlatı ve tablo başlıkları yeniden kontrol edildi, tam okuma yapılmadı.')
new = new.replace('İlk rapor `build.py`, bu güncelleme `refine.py` ile üretildi. Önceki rapor `map_v1.md` olarak korundu.', 'İlk rapor `build.py`, ikinci sürüm `refine.py`, anlatı/şekil/tablo incelemesini ekleyen üçüncü sürüm `narrative.py` ile üretildi. Önceki raporlar `map_v1.md` ve `map_v2.md` olarak korundu.')
new = new.replace('Bu belge karşılaştırma ve kaynak bulma tablosudur.', 'Üçüncü geçişte COMST_012/023/026 anlatı ve tablo işlevleri ayrı bir AI okumasıyla kontrol edildi; öneride teknik değerlendirme ile karşılaştırılabilirlik ayrımı ayrıca sorgulandı. Bu kontrol de insan bilimsel değerlendirmesi yerine geçmez.\n\nBu belge kaynak eşleştirmesi ve kurgu geliştirme önerisidir.')
new = new.replace('boyutlar üzrə', 'boyutlar üzerinden')

# Validate every local Markdown link, including one-based source locations.
links = re.findall(r'\]\((C:/[^)]+)\)', new)
for dest in links:
    m = re.fullmatch(r'(.+?):(\d+)', dest)
    path = Path(m.group(1) if m else dest)
    assert path.is_file(), dest
    if m:
        assert 1 <= int(m.group(2)) <= len(path.read_text(encoding='utf-8-sig').splitlines()), dest
table_width = None
table_count = 0
for line in new.splitlines():
    if line.startswith('|'):
        width = len(line.split('|')) - 2
        if table_width is None:
            table_width = width
            table_count += 1
        assert width == table_width, line
    else:
        table_width = None
inventory = new[new.index('## G.'):new.index('## Kontrol kaydı')]
ids = re.findall(r'^\| \[(COMST_\d+)\]', inventory, re.M)
assert len(ids) == len(set(ids)) == 77
assert len(method_rows) + len(comparison_rows) + len(framework_rows) == 13
assert all(digest(p) == h for p, h in before.items())
assert all(digest(sources[r['id']]) == r['sha256'] for r in records)
shutil.copy2(target, backup)
target.write_text(new, encoding='utf-8')
qa.update(revision=3, narrative_source_rows=13, narrative_comst_articles=11,
          narrative_external_articles=2, directly_inspected_source_figures=4,
          manuscript_component_rows=len(ours_rows), implementation_priority_rows=len(priority_rows),
          example_status='Schema only; no study record selected or invented',
          markdown_links_verified=len(links), markdown_tables_checked=table_count,
          manuscript_section_files_unchanged=len([p for p in before if p.suffix == '.tex']),
          section3_unchanged=digest(SECTION) == qa['section3_sha256'],
          source_hashes_unchanged=True, output_sha256=digest(target),
          method='Revision 2 corpus screening preserved; targeted narrative and artifact analysis of 11 COMST papers plus P01/P02, four local figures visually inspected; no full PDF reread or manuscript edits')
(OUT / 'qa.json').write_text(json.dumps(qa, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: qa[k] for k in ['revision', 'narrative_source_rows', 'markdown_links_verified', 'markdown_tables_checked', 'manuscript_section_files_unchanged', 'section3_unchanged', 'source_hashes_unchanged', 'output_sha256']}, ensure_ascii=False))
