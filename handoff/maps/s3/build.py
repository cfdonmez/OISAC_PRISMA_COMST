from pathlib import Path
import json, re, hashlib

OUT = Path(__file__).parent
ROOT = Path(r'C:\GH\OISAC_PRISMA_COMST\data\corp_std')
PAPERS = Path(r'C:\OISAC\outputs\IKI_CALISMA_OKUMA_2026-09-06')
SECTION = Path(r'C:\OISAC\worktrees\comst-v3-20260906\manuscript\sections\03_REVIEW_METHOD_AND_EVIDENCE_BASE.tex')
records = json.loads((OUT / 'scan.json').read_text(encoding='utf-8'))
by_id = {r['id']: r for r in records}

# Article, actual section, local source line spans, functional mapping, paraphrase, limitation.
direct = [
('COMST_010', 'II-G. Motivation and Methodology for Choosing Literature; Fig. 5', [(280,300)], 'III-A; III-C sentez yöntemi',
 'Araştırma sorusu ve amaç → arama stratejisi → ilişkili yayınları izleme → dahil etme/dışlama → katkıya göre kategorileştirme. Kitchenham–Charters yaklaşımına dayandığını açıklıyor.',
 'Sınıflandırma; teknik kalite puanı değildir. “Quantitative approach” ifadesinin ayrıntısı verilmediği için nicel havuzlama anlamı çıkarılamaz.'),
('COMST_023', 'V. Trust Models in Heterogeneous Networks — açılış paragrafı', [(300,302)], 'III-A doğrudan; III-C sınıflandırma kısmen',
 '2016–2020 yayın penceresini, Web of Science/Google Scholar/IEEE Xplore/ACM kaynaklarını ve anahtar sözcükleri veriyor. Çalışmaları taksonomi ve ağ türü üzerinden değerlendiriyor.',
 'Bu pasajda ayrıntılı eleme akışı, çıkarım şeması veya çalışma kalitesi protokolü yok. Bizim III’e benzeyen bölüm burada V numarasını taşıyor.'),
('COMST_025', 'II-F. Survey Methodology', [(334,340)], 'III-A; III-C sentez yöntemi',
 'Freehaven arşivindeki 2010’dan başlayan güvenlik yayınlarından kapsam oluşturuyor. Sansür saldırılarını kapsam dışında tutuyor. Yukarıdan aşağıya ontoloji ve aşağıdan yukarıya zafiyet analiziyle kaynakları ilişkilendiriyor.',
 '2010 başlangıç yılıdır. Zafiyet analizi, makalelerin yöntem kalitesini puanlama değildir. Ontoloji ve mekanizma üzerinden sentez için örnektir.'),
('COMST_038', 'I-B. Survey Methodology; I-C. Survey Scope', [(85,93)], 'III-A doğrudan',
 'PRISMA temelli seçim, Google Scholar/Semantic Scholar, anahtar sözcük birleşimleri, iki aşamalı filtreleme ve kapsam dışı konuları açıklıyor. Her sorgunun ilk beş sonuç sayfasını inceliyor; ana odak 2018–Mart 2023.',
 'İlk beş sayfa sınırı korunmalı. 2018–Mart 2023 mutlak dahil etme kuralı olarak genişletilmemeli. III-B çıkarım birimleri ve III-C teknik kalite puanlaması bu pasajda yok.'),
('COMST_050', 'I-C. Research Methodology; I-E1. Literature Categorization', [(162,179),(187,195),(223,229)], 'III-A; III-C sınıflandırma/sentez; kalite ölçütü kısmi',
 'Araştırma soruları, IEEE Xplore/ACM/Google Scholar araması, seçim ölçütleri, atıf zinciri ve temaya göre yinelemeli sentez veriliyor. 115 yayının alan ve kategori üzerinden nasıl düzenlendiği açıklanıyor.',
 '“Quality assessment” burada yayın yerinin itibarıyla ilişkilendiriliyor; bizim teknik çalışma değerlendirmemize eşdeğer değil. 115 sayısı bağımsız çalışma değil “papers”. Ölçütlerden herhangi birini karşılama kuralı var.'),
('COMST_060', 'I-B. Review Method', [(85,95)], 'III-A doğrudan; sürüm ayıklama açısından kısmi yakınlık',
 'Araştırma sorusundan Boolean sorgu türetiyor; IEEE Xplore ve geriye doğru kaynak izleme kullanıyor. Konu uygunluğunu ve aynı çalışmanın yayımlanmış sürümünü ön baskıya tercih etme kuralını açıklıyor.',
 'Sürüm ayıklama, bizim tüm raporları bağımsız çalışmalara uzlaştırmamızın tam karşılığı değildir. Ayrıntılı çıkarım birimi veya TQAF benzeri çerçeve bu pasajda doğrulanmadı.'),
]

limited = [
('COMST_006', 'VII-A. Features of Quantum Machine Learning — Table XIV öncesi', [(841,843)], 'III-A’ya sınırlı seçim açıklaması',
 'Her kategoride daha fazla yaklaşım bulunduğunu ve ilginç buldukları birkaçını seçtiklerini açıkça söylüyor.',
 'Seçimin öznel sınırını bildiriyor; tekrarlanabilir arama ve uygunluk protokolü vermiyor.'),
('COMST_024', 'I-B. Article Scope and Contributions', [(51,55),(81,85)], 'III-A kapsam; III-C sınıflandırma açısından kısmi',
 'Mobil cihazların yerleşik sensörleriyle insan etkinliği tanımayı kapsam olarak belirliyor. Etkinlik, veri, ön işleme, tanıma ve değerlendirme boyutlarına göre anlatım kuruyor.',
 'Başlığındaki “Systematic Review” ifadesi tek başına açık yöntem protokolü kanıtı değil. Değerlendirme standartları esasen birincil tanıma sistemlerinin değerlendirilmesine ilişkin.'),
]

external = [
('P01','I-B. Related Survey Papers; Table I',[(129,182),(222,223)],'III-A’ya yalnız bağlam',
 'Önceki derlemeleri konu ve uygulama eksenleriyle karşılaştırarak kendi kapsamını gerekçelendiriyor.',
 'Kaynakların nasıl arandığını, seçildiğini veya elendiğini açıklayan yöntem yerine geçmez.'),
('P01','I-C. Contributions',[(183,214)],'III-A kapsam; III-C sentez eksenleri kısmen',
 'Spektrum, ağ mimarisi, algılama kipleri, güvenlik ve standardizasyonu ortak evrim çerçevesinde topluyor.',
 'Bu eksenler sentez düzenidir; çalışma uygunluğu veya kalite puanlama kuralları değildir.'),
('P01','II-D. Lessons Learned',[(600,625)],'III-C’ye kısmi — sentez çıktısı',
 'RF–optik bütünleşmesi üzerine ortak tasarım, uyarlama, eşzamanlama ve kalibrasyon gereksinimleri çıkarıyor.',
 'Anlatısal sentezin nasıl göründüğüne örnektir; sentez yöntemi ya da çalışma kalitesi değerlendirme protokolü değildir.'),
('P02','1.2. Existing works; 1.3. Salient contributions',[(238,253),(318,327),(365,384)],'III-A kapsam kısmen',
 'Önceki çalışmaların kapsamını ve kendi O-ISAC kategori, deney ve tasarım odağını tanımlıyor.',
 'Açık veri tabanı, sorgu, dahil etme/dışlama veya eleme protokolü olarak alınmamalı.'),
('P02','3.5. Existing experimental works on O-ISAC; Table 5',[(979,1004),(1038,1054)],'III-B’ye kısmi — çıkarım çıktısı',
 'Deneyleri kaynak/yıl, modülasyon, konumlama algoritması, veri hızı, doğruluk, verici/alıcı ve test alanıyla karşılaştırıyor.',
 'Koşullarıyla sonuç kaydına en yakın örnek. Ancak çıkarım prosedürü, analiz birimi veya veri doğrulama kuralı açıklamıyor.'),
('P02','7. Open research issues and future aspects — Real-time practice; Table 9',[(2596,2607),(2823,2834)],'III-C’ye kısmi — sentez çıktısı',
 'Uygulama ve saha deneyi eksiklerini tartışıyor; sistemlerin yöntem, algılama nesnesi, fayda ve gelecek yönlerini karşılaştırıyor.',
 'Uygulama eksikliği yorumu, yapılandırılmış çalışma kalitesi veya yanlılık değerlendirmesiyle eşdeğer değil.'),
]

def source_path(key):
    return Path(by_id[key]['path']) if key.startswith('COMST_') else PAPERS / key / 'reading_text.md'

def links(key, spans):
    p=source_path(key)
    lines=p.read_text(encoding='utf-8-sig').splitlines()
    for a,b in spans:
        assert 1 <= a <= b <= len(lines), (key,a,b,len(lines))
        assert any(s.strip() for s in lines[a-1:b])
    return ' · '.join(f'[L{a}–{b}]({p.as_posix()}:{a})' for a,b in spans)

def table(rows):
    text=['| Çalışma | Gerçek bölüm / parça | Bizdeki karşılık | Pasajın yaptığı iş | Eşleşmenin sınırı | Kaynak satırları |',
          '|---|---|---|---|---|---|']
    for key,section,spans,mapping,summary,limit in rows:
        vals=[key,section,mapping,summary,limit,links(key,spans)]
        assert all('|' not in v for v in vals)
        text.append('| '+' | '.join(vals)+' |')
    return '\n'.join(text)

body='''# Section III için bölüm eşleştirme tablosu

Tarih: 12 Eylül 2026. Amaç, başka makalelerde **bizim Section III’ün yaptığı işi üstlenen parçaları** bulmak. Bölüm numaralarının aynı olması aranmıyor. Örneğin COMST_023’te karşılık Section V’in açılışında.

## Kapsam ve okuma düzeyi

Yerel COMST arşivindeki **77 Markdown metninin tamamı** başlıklar ve derleme yöntemine ilişkin ifadelerle tarandı. Eski notlardaki 76 sayısı yerine bu çalışmada mevcut dosya sayısı kullanıldı. P01 ve P02 ayrıca tarandı; bu iki başlık 77 COMST kaydında yinelenmiyor. Aday yöntem pasajları bağlamlarıyla okundu. PDF’ler yeniden açılmadı, bütün makaleler baştan sona yeniden okunmadı.

**Altı COMST çalışmasında doğrudan yöntem eşleşmesi doğrulandı.** İki ek COMST örneği yalnız seçim/kapsam açıklaması bakımından yakın. P01/P02’deki yakınlık kapsam, karşılaştırma tabloları ve sentez çıktısı düzeyinde. “Saptanmadı” kaydı, hedefli taramada doğrulanmış bir yöntem pasajı bulunmadığını belirtir; makalenin hiçbir yerinde böyle bir açıklama bulunmadığına dair kesin hüküm değildir.

## Bizim Section III’te aranan işlevler

| Parçamız | Aranan işlev | Salt teknik konu olarak benzer sayılmayanlar |
|---|---|---|
| III-A — Search, Eligibility, and Study Reconciliation | Kaynak/sorgu, zaman penceresi, uygunluk, eleme, yinelenen sürümler ve rapor–çalışma ilişkisi | Önceki derlemeleri tanıtmak veya makale organizasyonu vermek tek başına seçim yöntemi değildir |
| III-B — Extraction and Units of Analysis | Kaynak bağlantılı çıkarım, analiz birimi, ölçü/birim/koşul kayıtları | Birincil sistemde veri toplama, özellik çıkarma veya makine öğrenmesi veri kümesi hazırlama |
| III-C — Technical Appraisal and Synthesis | Çalışmaların teknik desteğini değerlendirme ve sonuçları sınıflandırıp koşullarıyla sentezleme | Sinyal kalitesi, saldırı başarısı veya model doğruluğunu değerlendirmek tek başına derleme kalitesi değerlendirmesi değildir |

## A. Doğrudan yöntem eşleşmeleri

'''+table(direct)+'''

## B. COMST içinde sınırlı benzerlikler

Bu iki kayıt doğrudan yöntem sayısına dahil edilmedi.

'''+table(limited)+'''

## C. Paylaşılan iki çalışmadaki karşılıklar

- **P01:** Integrated Sensing and Communications Over the Years: An Evolution Perspective.
- **P02:** Optical integrated sensing and communication: Fundamentals, applications, challenges and future aspects.

'''+table(external)+'''

P01’in I-C içindeki organizasyon paragrafı (L225–233), P02’nin “2. Categories of O-ISAC” (L388–392) ve “5.2. Performance metrics” (L1230–1238, L1268–1284) parçaları da ayrıştırıldı. Bunlar teknik kapsam/organizasyon ve sistem performansına ilişkindir; derleme yöntemi diye sınıflandırılmadı. P01’in kendi Section III’ü ağ mimarisini anlatır; bizim Section III ile numarası dışında doğrudan yöntem eşleşmesi yoktur.

İki çalışmada bu hedefli incelemeyle açık sorgu/veri tabanı protokolü, eleme akışı, rapor–çalışma uzlaştırması veya yapılandırılmış teknik kalite değerlendirme süreci doğrulanmadı.

## D. Bizim alt bölümlerimize göre okuma sırası

| Bakılacak iş | En yakın yerler | Dikkat edilecek sınır |
|---|---|---|
| III-A’yı nasıl anlatabiliriz? | COMST_060 I-B; COMST_038 I-B/I-C; COMST_010 II-G | Yöntemin somut kaynak, sorgu ve kapsam kararlarıyla anlatılması. Başka çalışmanın eksik raporlaması bizim gereksinimlerimizi kaldırmaz |
| III-B’de koşullarıyla sonuç kaydı nasıl görünür? | P02 3.5 / Table 5 | Bu bir çıkarım çıktısı örneği; bizim çıkarım şeması ve analiz birimleri için tam yöntem karşılığı doğrulanmadı |
| III-C’de sentez yaklaşımı nasıl açıklanır? | COMST_025 II-F; COMST_010 II-G; COMST_050 I-C/I-E1 | Sentez yaklaşımını, teknik kalite değerlendirmesini ve sentez çıktısını ayrı okumak gerekir |
| III-C’de teknik kalite çerçevesine karşılık var mı? | COMST_050 I-C yalnız kısmi yakınlık | Yayın yeri itibarı, TQAF boyutlarıyla eşdeğer değil. Doğrulanan pasajlarda tam eşdeğer bulunmadı |

## E. Tüm COMST metinlerinin tarama durumu

**D:** Yukarıdaki A tablosunda kaynak pasajıyla doğrulanan doğrudan yöntem eşleşmesi. **K:** B tablosundaki sınırlı seçim/kapsam benzerliği. **T:** Başlık ve yöntem ifadesi tarandı; doğrudan yöntem pasajı doğrulanmadı. T, tam okuma sonrası verilmiş bir “yok” hükmü değildir. Genel teknik taksonomi ve lessons-learned bölümlerinin tümü ayrıca çıkarılmadı.

| ID ve kaynak | Makale başlığı | Durum | Doğrulanan yakın yer |
|---|---|---|---|
'''
positive={r[0]:('D',r[1]) for r in direct}
positive.update({r[0]:('K',r[1]) for r in limited})
for r in records:
    code,where=positive.get(r['id'],('T','Doğrudan yöntem pasajı doğrulanmadı'))
    title=r['title'].replace('|','/').replace('\n',' ')
    body+=f"| [{r['id']}]({Path(r['path']).as_posix()}) | {title} | {code} | {where} |\n"
body+='''
## Kontrol kaydı

Eşleştirme, `C:/GH/OISAC_PRISMA_COMST/data/corp_std` arşivinde yapıldı. Aynı 77 kaynak, kurtarma arşivindeki kopyalarıyla SHA-256 üzerinden aynı bulundu. Arama ifadeleri ve satır adayları `scan.json` dosyasında, tablo üretimi `build.py` dosyasında tutuldu. Makale TeX dosyaları değiştirilmedi.

Altı doğrudan eşleşmenin bölüm numaraları ve yorum sınırları ikinci bir AI okumasıyla kontrol edildi. P01/P02 adayları ayrı bir AI okumasıyla incelendi. Bu, bağımsız insan değerlendirmesi değildir.

Bu belge karşılaştırma ve kaynak bulma tablosudur. Section III’e yeni içerik eklemez; bütün korpusun her paragrafını eksiksiz yorumladığımızı veya bizim yöntemimizin diğerlerinden üstün olduğunu ileri sürmez.
'''

target=OUT/'map.md'
assert not target.exists(), 'Preserve existing report'
target.write_text(body,encoding='utf-8')
qa={'date':'2026-09-12','corpus_files':len(records),'external_papers':2,'direct_method_articles':len(direct),'limited_corpus_articles':len(limited),'screen_only_corpus_articles':len(records)-len(positive),'external_passage_rows':len(external),'section3_sha256':hashlib.sha256(SECTION.read_bytes()).hexdigest(),'source_links_checked':True,'method':'All 77 local texts searched; candidate passages read, not full-paper exhaustive reading','output_sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
(OUT/'qa.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(qa,ensure_ascii=False,indent=2))
