from pathlib import Path
import json, re, shutil, hashlib

OUT=Path(__file__).parent
target=OUT/'map.md'
backup=OUT/'map_v1.md'
assert not backup.exists(), 'Preserve the first version'
shutil.copy2(target,backup)
text=backup.read_text(encoding='utf-8')
records=json.loads((OUT/'scan.json').read_text(encoding='utf-8'))
by_id={r['id']:r for r in records}

# Functional matches are not equivalent to explicit review protocols.
embedded=[
('COMST_003','IV. RRM Taxonomy',[(200,202)],'III-B için alan çerçevesi; III-C için sınıflandırma',
 'Literatürü beş açıdan düzenliyor: yaklaşım, metrik, model, karmaşıklık ve kontrol. Çalışmalara hangi sorularla bakılacağını görünür kılıyor.',
 'Bu pasaj bir karşılaştırma/sınıflandırma çerçevesini tanımlıyor. Tek başına uygulanmış veri çıkarım prosedürü veya teknik kalite puanı göstermiyor.'),
('COMST_012','VI. Future Work → B. Performance Evaluation of CAN Reverse Engineering',[(1047,1072)],'III-C karşılaştırılabilirlik; III-B için önerilen koşul alanları',
 'Farklı donanım, test düzeni ve değerlendirme ölçütlerinin adil kıyası engellediğini açıklıyor. Açık kod/veri, doğruluk referansı, araç modeli/yılı, kayıt araçları ve sürüş koşulları gibi bilgileri gerekli görüyor.',
 'Bunlar önerilen ortak değerlendirme verisinin özellikleri. Derlemede bu alanların sistematik çıkarıldığı iddia edilemez. Karşılaştırma sınırlarını açıklamak açısından güçlü örnek.'),
('COMST_014','III-D. Summary and Lessons Learned — Table II açıklaması',[(392,396)],'III-B karşılaştırma alanları; III-C teknik sentez',
 'VLP algoritmalarını gereken LED sayısı, yardımcı donanım, avantaj ve zayıflıklar üzerinden karşılaştırıyor. Donanım ihtiyacı ile uygulanabilirlik yorumunu birbirine bağlıyor.',
 'Algoritma/teknik özellik karşılaştırmasıdır; makalenin yöntem kalitesini puanlama değildir. III-C’deki yeni sayısal algoritma deneyinden ayrı okunmalı.'),
('COMST_023','III. Evaluation Criteria on Trust Models; V-A. Decision Models in HetNets; Table VI',[(151,169),(300,317),(323,331)],'III-B ve III-C için güçlü, uygulanan karşılaştırma örneği',
 'Önce ortak değerlendirme ölçütlerini tanımlıyor, sonra kaynaklardaki modelleri bunlarla değerlendiriyor. Tablo VI kaynak, ağ türü, uygulama, teknik, ölçütler ve sınırlılıkları bir araya getiriyor. Bahsedilmemiş bilgi ile desteklenmeyen özellik ayrımı yapılabiliyor.',
 'Teknik modelin niteliğini değerlendirmek, araştırma raporunun yanlılık riskini değerlendirmekle aynı değildir. Bu makale ayrıca A tablosunda arama yöntemi örneğidir; iki ayrı makale gibi sayılmamalı.'),
('COMST_026','IV-C. Testbeds, Prototypes, and COTS Products → 1) Laboratory Testbeds; Table V',[(530,552),(560,566)],'III-B sonuç/koşul kaydı; III-C karşılaştırma sınırı',
 'Test düzeneklerini ortam, donanım, hız, BER, kanal uzunluğu ve modülasyon gibi alanlarla birlikte sunuyor. Test düzenekleri aynı olmadığından adil bir doğrudan karşılaştırma yapılamayacağını açıkça söylüyor; ardından sınırlı genel çıkarımlar yapıyor.',
 'Koşulları görünür kılmak, sonuçları normalleştirmek veya eşit koşullarda sıralamak değildir. Sentezin hangi sınırla yapılabileceğini anlatan güçlü bir örnek.'),
('COMST_075','IV. Addressing the DSRC vs. C-V2X Debate → C. Comparative Evaluations; Table XVI',[(760,781),(787,803)],'III-B kaynak/yöntem/metrik kaydı; III-C koşullara bağlı sentez',
 'Karşılaştırmalı yayınları kaynak, yıl, değerlendirme yöntemi ve metrik alanlarıyla özetliyor. Sonuçları fiziksel katman, cihaz yoğunluğu, uzaklık, gecikme ve güvenilirlik koşullarıyla yorumluyor.',
 'Bu bir karşılaştırma kaydı ve sentez çıktısıdır. Açık arama protokolü veya birleştirilmiş etki modeli değildir; başka koşullardaki sonuçlardan evrensel üstünlük çıkarılmamalı.'),
]
adjacent=[
('COMST_032','VI. Simulation and Channel Model → A. Evaluation Methodology',[(574,594)],'III-B/C’ye komşu — ortak teknik değerlendirme koşulları',
 'Teknik önerilerin oda/nesne, anten, trafik ve donanım koşullarıyla değerlendirilmesini; doğruluk referansı, RMSE ve SNR’ye bağlı sonuç sunumunu anlatıyor.',
 'IEEE 802.11bf teknik önerilerinin değerlendirme protokolü aktarılıyor. Yazarların literatürü nasıl seçtiği, çıkardığı veya değerlendirdiği sürecin karşılığı değil.'),
('COMST_074','IV. Evaluation of CSI Processing Techniques; IV-A. Experiment Descriptions',[(486,500)],'III-B/C’ye komşu — yazarların kendi karşılaştırmalı deneyleri',
 'Derlemede belirlenen CSI işleme tekniklerini üç deney ölçeğinde yeni deneylerle değerlendiriyor; görevler ve deney koşulları açıklanıyor.',
 'Başlıktaki “Evaluation” yanıltmamalı. Bu, derleme çalışmalarının kanıt kalitesi incelemesi değil; makalenin kendi deneysel değerlendirmesi.'),
]
def table(rows):
    out=['| Çalışma | Gerçek bölüm / parça | Bizdeki karşılık | Pasajın yaptığı iş | Eşleşmenin sınırı | Kaynak satırları |','|---|---|---|---|---|---|']
    for key,section,spans,mapping,summary,limit in rows:
        p=Path(by_id[key]['path']);lines=p.read_text(encoding='utf-8-sig').splitlines()
        assert all(1<=a<=b<=len(lines) for a,b in spans)
        links=' · '.join(f'[L{a}–{b}]({p.as_posix()}:{a})' for a,b in spans)
        out.append('| '+' | '.join([key,section,mapping,summary,limit,links])+' |')
    return '\n'.join(out)

old='**Altı COMST çalışmasında doğrudan yöntem eşleşmesi doğrulandı.** İki ek COMST örneği yalnız seçim/kapsam açıklaması bakımından yakın. P01/P02’deki yakınlık kapsam, karşılaştırma tabloları ve sentez çıktısı düzeyinde. “Saptanmadı” kaydı, hedefli taramada doğrulanmış bir yöntem pasajı bulunmadığını belirtir; makalenin hiçbir yerinde böyle bir açıklama bulunmadığına dair kesin hüküm değildir.'
new='''**İkinci tarama düzeltmesi:** İlk geçiş açık derleme protokollerine ağırlık verdiği için III-B/III-C’deki gömülü işlevleri dar temsil ediyordu. İkinci geçişte 77 metin yeniden; karşılaştırma alanları, değerlendirme ölçütlerinin uygulanması, deney koşulları, karşılaştırılabilirlik ve sentez kararları açısından aday belirlemeye tabi tutuldu. Adayların hepsi baştan sona okunmadı; aşağıda eklenen sekiz parçanın ilgili bağlamları incelendi.

Altı açık derleme yöntemi kaydı korundu. **Altı gömülü karşılaştırma/sentez eşleşmesi** ve bunlarla karıştırılmaması gereken **iki komşu değerlendirme örneği** eklendi. COMST_023 hem açık yöntem hem gömülü değerlendirme içerir. Böylece 11 farklı COMST çalışmasında açık yöntem veya doğrulanmış gömülü karşılaştırma/sentez işlevi gösteriliyor. Bu sayı sistematik derleme protokolü olan makale sayısı değildir. İki sınırlı kapsam/seçim kaydı ayrıca korunuyor.

P01/P02’nin önceki hedefli okuma sonuçları korundu; bu turda yeniden tam okuma yapılmadı. “Saptanmadı” kaydı, yöntem bulunmadığının kesin hükmü değildir. COMST’te bu içeriğin mutlaka ayrı bir yöntem bölümü olması gerektiği varsayılmadı; eşleşmeler bulunan pasajlara dayanıyor.'''
assert old in text
text=text.replace(old,new)
text=text.replace('## A. Doğrudan yöntem eşleşmeleri','## A. Açık derleme yöntemi eşleşmeleri')
addition='''## B. İkinci taramada bulunan gömülü işlevsel karşılıklar

Buradaki parçalar başka bölümlere dağılmış olsa da bizim III-B/III-C’de açıkladığımız karşılaştırma alanları ve sentez sınırlarını somutlaştırıyor. “Gömülü eşleşme”, derleme protokolünün tamamına eşdeğerlik anlamına gelmez.

'''+table(embedded)+'''

## C. Benzer görünüp farklı işi yapan değerlendirme bölümleri

Bu iki kayıt, “Evaluation Methodology” gibi başlıkları neden doğrudan derleme yöntemi saymadığımızı gösteriyor.

'''+table(adjacent)+'\n\n'
text=text.replace('## B. COMST içinde sınırlı benzerlikler',addition+'## D. COMST içinde sınırlı benzerlikler')
text=text.replace('## C. Paylaşılan iki çalışmadaki karşılıklar','## E. Paylaşılan iki çalışmadaki karşılıklar')
start=text.index('## D. Bizim alt bölümlerimize göre okuma sırası')
end=text.index('## E. Tüm COMST metinlerinin tarama durumu')
replacement='''## F. Bizim alt bölümlerimize göre en yararlı okuma sırası

| Bakılacak iş | En yakın yerler | Ne için yararlı? |
|---|---|---|
| III-A — kaynak seçimi | COMST_060 I-B; COMST_038 I-B/I-C; COMST_010 II-G | Sorgu, kaynak, kapsam ve seçim kararlarının açıklanması |
| III-B — karşılaştırma alanlarının düzenlenmesi | COMST_023 III + V-A/Table VI; COMST_026 IV-C1/Table V; P02 3.5/Table 5 | Kaynak, özellik, ölçü ve koşulların karşılaştırma kayıtlarına dönüşmesi. Çıkarım formu/prosedürüyle eşdeğerlik ileri sürülmez |
| III-C — ortak ölçütlerin uygulanması | COMST_023 III + V-A | Önce ölçütü tanımlama, sonra çalışmalara uygulama. Teknik model değerlendirmesi ile araştırma kalitesi ayrımı korunur |
| III-C — karşılaştırılabilirliğin sınırı | COMST_012 VI-B; COMST_026 IV-C1 | Farklı test düzeneklerinden gelen sonuçların hangi koşullarda yorumlanabileceği |
| III-C — sentez çerçevesi | COMST_025 II-F; COMST_003 IV; COMST_050 I-C/I-E1 | Ontoloji, analiz boyutları ve tematik gruplarla sentezin düzenlenmesi |
| TQAF’ın tam karşılığı var mı? | COMST_023 teknik ölçüt uygulaması ve COMST_050 yayın yeri ölçütü yalnız kısmi yakınlık | Bunların hiçbiri bizim sekiz boyutlu TQAF’ın aynı veya doğrulanmış eşdeğeri olarak gösterilmiyor |

'''
text=text[:start]+replacement+text[end:]
start=text.index('## E. Tüm COMST metinlerinin tarama durumu')
end=text.index('## Kontrol kaydı',start)
inventory='''## G. Tüm COMST metinlerinin tarama durumu

**D:** Açık derleme yöntemi doğrulandı. **G:** Gömülü karşılaştırma/sentez işlevi doğrulandı. **K:** Sınırlı seçim/kapsam açıklaması. **Y:** Komşu teknik değerlendirme, derleme yöntemiyle karıştırılmamalı. **T:** İki taramada aday belirleme yapıldı; bu raporda doğrulanmış işlevsel pasajı henüz gösterilmiyor. T, içerik yokluğu değildir. Genel taksonomi/organizasyon/lessons-learned adaylarının tamamı ayrıntılı doğrulanmadı.

| ID ve kaynak | Makale başlığı | Durum | Doğrulanan yakın yer |
|---|---|---|---|
'''
old_rows={m.group(1):(m.group(2),m.group(3)) for m in re.finditer(r'^\| \[(COMST_\d+)\]\([^\n]+?\) \| [^\n]+? \| ([DKT]) \| ([^\n]+?) \|$',text,re.M)}
g={r[0]:r[1] for r in embedded};y={r[0]:r[1] for r in adjacent}
statuses={}
for r in records:
    key=r['id'];code,where=old_rows.get(key,('T','Bu raporda ayrıntılı eşleşme henüz doğrulanmadı'))
    if key in g:
        code='D+G' if code=='D' else 'G'
        where=(where+'; '+g[key]) if code=='D+G' else g[key]
    elif key in y:code,where='Y',y[key]
    elif code=='T':where='Aday taraması yapıldı; ayrıntılı eşleşme henüz doğrulanmadı'
    statuses[key]=code
    title=r['title'].replace('|','/')
    inventory+=f"| [{key}]({Path(r['path']).as_posix()}) | {title} | {code} | {where} |\n"
text=text[:start]+inventory+'\n'+text[end:]
text=text.replace('Arama ifadeleri ve satır adayları `scan.json` dosyasında, tablo üretimi `build.py` dosyasında tutuldu.', 'İlk tarama adayları `scan.json`, ikinci geçişin işlevsel ifade adayları `scan2.json` dosyasında tutuldu. İlk rapor `build.py`, bu güncelleme `refine.py` ile üretildi. Önceki rapor `map_v1.md` olarak korundu.')
text=text.replace('Altı doğrudan eşleşmenin bölüm numaraları ve yorum sınırları ikinci bir AI okumasıyla kontrol edildi.', 'Altı açık yöntem eşleşmesinin bölüm numaraları ve sınırları ikinci bir AI okumasıyla kontrol edildi. İkinci geçişte COMST_012/023/032 pasajları ayrı bir AI okumasıyla doğrulandı; yeni sınıflandırmaların kavramsal sınırları da çapraz kontrol edildi.')
assert len(old_rows)==77
target.write_text(text,encoding='utf-8')
qa=json.loads((OUT/'qa.json').read_text(encoding='utf-8'))
qa.update(revision=2,embedded_passage_rows=len(embedded),adjacent_rows=len(adjacent),unique_protocol_or_embedded_articles=sum('D' in c or 'G' in c for c in statuses.values()),screen_only_corpus_articles=sum(c=='T' for c in statuses.values()),method='All 77 texts re-screened for comparison fields, criteria application and synthesis constraints; eight additional passages contextualized, not exhaustive full reading',output_sha256=hashlib.sha256(target.read_bytes()).hexdigest())
(OUT/'qa.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'embedded_rows':6,'adjacent_rows':2,'unique_protocol_or_embedded_articles':qa['unique_protocol_or_embedded_articles'],'statuses':{c:list(statuses.values()).count(c) for c in sorted(set(statuses.values()))}},ensure_ascii=False))
