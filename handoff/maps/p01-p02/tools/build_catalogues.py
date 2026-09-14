"""Build local catalogues from the completed PDF reading; no network calls."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
def save(relative, content):
    (ROOT / relative).write_text(json.dumps(content, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

bibliography = [
    dict(paper_id='P01', original_filename='1.pdf', title='Integrated Sensing and Communications Over the Years: An Evolution Perspective',
         authors=['Di Zhang','Yuanhao Cui','Xiaowen Cao','Nanchi Su','Yi Gong','Fan Liu','Weijie Yuan','Xiaojun Jing','J. Andrew Zhang','Jie Xu','Christos Masouros','Dusit Niyato','Marco Di Renzo'],
         journal='IEEE Communications Surveys & Tutorials', volume='28', year=2026, pages='5014-5048', doi='10.1109/COMST.2026.3655674',
         received='2025-09-14', revised='2025-12-11', accepted='2026-01-10', first_published='2026-01-19', current_version='2026-03-06',
         pdf_pages=35, numbered_references=248, numbered_tables=7, numbered_figures=14, issue=None),
    dict(paper_id='P02', original_filename='2.pdf', title='Optical integrated sensing and communication: Fundamentals, applications, challenges and future aspects',
         authors=['S.A.H. Mohsan','Siyu Bai','Haoyu Huang','Yi Hao','Shichen Zheng','Qian Li','H.Y. Fu'],
         journal='Optical Switching and Networking', volume='61', year=2026, article_number='100854', doi='10.1016/j.osn.2026.100854',
         received='2025-12-23', revised='2026-02-03', accepted='2026-02-04', first_published='2026-02-06',
         pdf_pages=37, numbered_references=174, numbered_tables=10, numbered_figures=25, issue=None)
]
for row in bibliography:
    row['source'] = 'User-supplied PDF, first page and visible page/reference/caption numbering; no external bibliographic lookup.'
    row['sha256'] = json.loads((ROOT / row['paper_id'] / 'metadata.json').read_text(encoding='utf-8'))['sha256']
save('bibliography.json', bibliography)
(ROOT / 'references.bib').write_text('''@article{Zhang2026ISACEvolution,
  author = {Zhang, Di and Cui, Yuanhao and Cao, Xiaowen and Su, Nanchi and Gong, Yi and Liu, Fan and Yuan, Weijie and Jing, Xiaojun and Zhang, J. Andrew and Xu, Jie and Masouros, Christos and Niyato, Dusit and Di Renzo, Marco},
  title = {Integrated Sensing and Communications Over the Years: An Evolution Perspective},
  journal = {IEEE Communications Surveys \\& Tutorials},
  year = {2026}, volume = {28}, pages = {5014--5048},
  doi = {10.1109/COMST.2026.3655674}
}

@article{Mohsan2026OpticalISAC,
  author = {Mohsan, S. A. H. and Bai, Siyu and Huang, Haoyu and Hao, Yi and Zheng, Shichen and Li, Qian and Fu, H. Y.},
  title = {Optical integrated sensing and communication: Fundamentals, applications, challenges and future aspects},
  journal = {Optical Switching and Networking},
  year = {2026}, volume = {61}, pages = {100854},
  doi = {10.1016/j.osn.2026.100854}
}
''', encoding='utf-8')

table_pages = {'P01': [3,5,7,9,11,22,23], 'P02': [2,3,4,6,12,17,17,31,32,33]}
table_topics = {
 'P01': ['Önceki survey kapsamları','Anten teknolojileri ve yeniden yapılandırılabilir yüzeyler','Optik ISAC türleri','Ortogonal kaynak tahsisli dalga biçimleri','Algılama ve iletişim merkezli amaç/kısıtlar','ISAC için derin öğrenme yöntemleri','ISAC veri kümeleri'],
 'P02': ['RF ve optik ISAC sayısal özellikleri','RF ve optik ISAC nitel özellikleri','Önceki derlemeler ve Our Work','O-ISAC türleri','Optik haberleşme ve konumlandırma deneyleri','MWP sistemlerinin nitel karşılaştırması','MWP kaynak çoğullama deneyleri','O-ISAC için makine öğrenmesi rolleri','Yöntem, algılama nesnesi, yarar ve gelecek yönler','Kısaltmalar']}
figure_pages = {'P01': [4,6,10,14,15,16,18,19,21,21,25,26,27,28], 'P02': [5,5,7,7,8,9,9,10,12,13,13,14,15,16,17,19,20,22,23,24,25,26,27,27,28]}
figure_topics = {
 'P01': ['Makale yapısı','VLC-FSO-photonic sensing','Ortogonal kaynak tahsisi','Tek hücre topolojileri','Çok hücre topolojileri','Uzay-hava-yer ağı','Edge perception mimarisi','AI ve ISAC etkileşimi','RIS beamforming sinir ağı [169]','Penetrative AI [185]','Güvenlik ve algılama mahremiyeti','3GPP zaman çizelgesi','Multi-RTT mesajlaşması','Döner kanatlı UAV senaryosu [244]'],
 'P02': ['Makale yapısı','VLC-FSO-photonic sensing','MoF deney düzeneği ve sonuçları [43]','Dağıtık fiber algılama teknikleri','Geri saçılma spektrumları','Fiber algılama sinyal yolu','DOFS ve haberleşme paylaşımı [52]','Ortak fiber/dalga biçimi ISAC [10]','Genel FSO ağırlıklı ISAC mimarisi','PPM, LFM-CPM, OFDM dalga biçimleri','Donanım, hibrit tasarım ve öğrenme','Performans ölçütleri','PSS-PPM ve LFM-CPM','Fotonik çoklu hüzme oluşturma','TDM, FDM, HRDM ve SDM','ML ile dinleme tespiti [107]','Çok parametreli fiber algılama [109]','Kuantum-transformer/mmWave beam prediction [123]','UAV optik haberleşme ve algılama [14]','ROS robotik deneyleri [139]','SiN tabanlı algılama ve haberleşme [152]','MIR gaz algılama ve haberleşme [156]','Akıllı yapıda fiber algılama','Fiber ve optik kablosuz köprü/demiryolu izleme','Araçta aydınlatma-algılama-haberleşme']}
for paper in ['P01','P02']:
    items=[]
    for kind, pages, topics in [('table',table_pages[paper],table_topics[paper]),('figure',figure_pages[paper],figure_topics[paper])]:
        for number,(page,topic) in enumerate(zip(pages,topics),1):
            items.append(dict(kind=kind,number=number,pdf_pages=([33,34] if paper=='P02' and kind=='table' and number==10 else [page]),topic_tr=topic,
                              source_render=f'rendered_pages/page-{page:02}.png'))
    save(f'{paper}/table_figure_inventory.json',dict(paper_id=paper, label_note='Türkçe konu etiketleri okuma özeti; birebir İngilizce başlık transkripsiyonu değildir.',items=items))

dataset_rows = [
 ('SDP',206,['CSI','Kinect data'],[1,1,1,1,1],'Time >400 hours','IEEE ISAC-ETI','https://www.SDP8.org'),
 ('ImgFi',176,['CSI images'],[0,0,0,1,0],'Size >10,000','Nanjing Forestry University',None),
 ('WiMANS',207,['CSI','RGB video'],[0,0,0,1,0],'Time >9.4 hours','Imperial College London',None),
 ('Radar Signatures of Human Activities',208,['Radar'],[0,0,0,1,0],'-','University of Glasgow','https://researchdata.gla.ac.uk/id/eprint/848'),
 ('EyeFi',209,['CSI','RGB video'],[0,0,1,1,0],'-','University of North Carolina',None),
 ('OPERAnet',210,['CSI','Kinect data'],[0,0,0,1,0],'Size >8 hours','Bocus et al.',None),
 ('MmWave Gesture Dataset',211,['mmWave','Camera','Depth maps'],[0,0,0,1,0],'Size >54,620; Time >1357 minutes','Beijing University of Post and Telecommunications',None),
 ('DeepSense 6G',212,['RGB','LiDAR','GPS','Radar','mmWave'],[0,1,1,0,0],'Size >1 million data points','Arizona State University',None),
 ('WALDO',213,['mmWave received signals','Channel data'],[0,1,0,0,0],'-','National Institute of Standards and Technology','https://github.com/usnistgov/PS-002-WALDO'),
 ('M³SC datasets',27,['LiDAR','RGB','Depth maps','mmWave'],[0,1,1,0,0],'Size >1500 scenarios','School of Electronics, Peking University',None)
]
tasks=['Detection','Positioning','Tracking','Recognition','Imaging']
datasets=[]
for name,ref,types,flags,volume,provider,url in dataset_rows:
    datasets.append(dict(name=name,cited_reference=ref,pdf_page=23,table='VII',data_types=types,
                         application_marks_as_printed={task:('✓' if flag else '×') for task,flag in zip(tasks,flags)},
                         data_volume_as_printed=volume,provider_as_printed=provider,url_as_printed=url,url_visited=False,downloaded=False))
save('P01/DATASET_CATALOGUE.json',dict(paper_id='P01',source='Table VII, PDF p.23, checked against rendered table',
    kind='secondary_dataset_catalogue_not_raw_data',datasets=datasets,
    notes=['Tablo raster biçiminde; otomatik metin dosyası tablo hücrelerini içermiyor. Bu kayıt görsel tabloya dayanır.',
           'Tablodaki > işaretleri aynen korunmuştur. OPERAnet için kaynağın Size >8 hours ifadesi düzeltilmemiştir.',
           'WiMANS tabloda Recognition ile işaretli; s.23 metni tracking ve pose estimation görevlerinden de söz eder. Tablo aynen korunur.',
           'URL yalnız PDF kaynakçasında açıkça bulunduğu üç kayıt için girilmiştir (kaynakça s.34-35); diğer URL alanları bilinmeyen olarak null bırakılmıştır.',
           'Katalog optik kablosuz ISAC veri setleri ile sınırlı değildir. Dış veri dosyası indirilmedi, erişim ve lisans doğrulanmadı.']))

claims = [
 ('P01',5,64,'photonics-assisted RF W-band',['48.04 Gbps','1.02 cm','16 GHz bandwidth'],'Aynı derleme cümlesinde; RF taşıyıcı, optik hava kanalı değil.'),
 ('P01',5,65,'sub-THz RF',['around 275 GHz','30 GHz effective bandwidth','sub-centimeter resolution'],'Santimetre altı ifade sayısal bir hata değerine çevrilmedi.'),
 ('P01',6,69,'optical wireless localization',['1.2 m × 1.2 m × 2.16 m','centimeter-level localization'],'Bu paragraf sayısal hata istatistiği ve veri hızı vermiyor.'),
 ('P01',6,74,'photonics-assisted RF W-band',['47.54 Gbps'],'Cümlede sayısal radar hatası yok.'),
 ('P01',6,75,'photonics-assisted 28 GHz RF',['better than 20 mm ranging accuracy','decimeter-level resolution','28 GHz'],'İlk algılama sonucu tek kullanıcı, ikincisi çift kullanıcı koşulu.'),
 ('P02',4,36,'photonics-assisted RF W-band',['96.5 GHz','10 km fiber','1 m free-space','5.98-41.48 Gbps','1.53-6.94 cm'],'Aralık uçları eşzamanlı performans çifti sayılmadı.'),
 ('P02',6,37,'photonics-assisted RF D-band',['10 m','251.03 Gbps real-time','2.5 cm offline radial resolution'],'Haberleşme gerçek zamanlı; algılama çevrimdışı olarak raporlanıyor.'),
 ('P02',6,33,'photonics-assisted RF W-band',['97.5 GHz','10 km fiber','1 m','15-60 Gbps','1.76-3.15 cm'],'Farklı kaynak Tablo7 [92] ile karıştırılmamalı.'),
 ('P02',6,38,'photonics-assisted RF W-band',['47.07 Gbps','10 m','1.02 cm'],'Offline DSP; P01 48.04 sayısı farklı atıf/rapora bağlı olabilir, sessiz eşitleme yapılmadı.'),
 ('P02',6,43,'mmWave-over-fiber',['28 GHz','5.41 km SMF','2 m wireless','23 Gbps','±15 mm','30 cm'],'±15 mm tek hedef doğruluğu; 30 cm çift hedef çözünürlüğü.'),
 ('P02',8,52,'fiber WDM coexistence',['36.8 Tbps'],'Saha uygulaması anlatımı; üç ayrılmış 50-GHz kanal s.9.'),
 ('P02',10,59,'fiber joint-frame waveform',['60 GBaud','16-QAM','0.5 m spatial resolution'],'GBaud bit hızı olarak dönüştürülmedi.'),
 ('P02',11,10,'fiber LFM-carrier PAM4',['56 Gbit/s','24.5 km','42 kHz effective sampling','4 m spatial resolution','7 dB optimal launch power difference','~1.3 dB gain at 7% FEC','~1.25 dB sensing penalty'],'Kazanç/kayıplar farklı ölçüt ve karşılaştırmalara ait; 1.25 dB ölçütü derlemede belirsiz.'),
 ('P02',11,29,'infrared optical wireless localization',['12 Mbps pre-FEC','BER <3.8 × 10^-3','error <5.9 cm in 90% of experiments'],'Tablo5 s.12 persentili göstermiyor; metin koşulu saklandı.'),
 ('P02',18,107,'fiber channel-monitoring ML',['92.76% localization accuracy','100% eavesdropping detection','1 normal +20 eavesdropping cases','0-90 km','5% and 10% splitting ratios'],'Belirtilen deney sınıflandırması; genel güvenlik garantisi değil.'),
 ('P02',21,117,'fiber quantum communication and sensing',['~0.7 Mbps per user secret key rate','10 km','8 users network capacity','0.20 m spatial resolution','1-2 kHz vibration response bandwidth'],'Secret key rate klasik haberleşme veri hızından ayrı.'),
 ('P02',21,123,'multimodal mmWave beam prediction with quantum learning',['0.8832 positioning-based','0.9124 multimodal-based'],'Distance-aided accuracy; optik taşıyıcılı haberleşme veya QKD deneyi değil.'),
 ('P02',26,156,'mid-infrared gas sensing and communication',['10% H2S','BER below FEC limit'],'Laboratuvar demonstrasyonu; sınırsız menzil veya saha güvenlik doğrulaması değil.')
]
for paper in ['P01','P02']:
    records=[]
    for i,(pid,page,ref,platform,values,caveat) in enumerate([x for x in claims if x[0]==paper],1):
        records.append(dict(id=f'{paper}-C{i:02}',pdf_page=page,cited_reference=ref,platform=platform,
                            values_as_reported=values,interpretation_caveat_tr=caveat,primary_source_verified=False))
    save(f'{paper}/structured_evidence.json',dict(paper_id=paper,scope='Selected quantitative statements; not exhaustive extraction of every number in the PDF.',
        kind='secondary_review_reported',source_sha256=next(b['sha256'] for b in bibliography if b['paper_id']==paper),records=records))

crosswalk = [
 (67,27,'Wen et al., architectures, potentials and challenges','same publication'),
 (68,6,'Zhang et al., light-emitting diode ISAC','related conference/journal versions; P01 cites ICC Workshops 2024, P02 IoT Journal 2025; do not equate reports'),
 (69,29,'Shi et al., experimental optical wireless sensing and communication','same publication'),
 (70,30,'Khorasgani et al., fundamental performance limits','same arXiv identifier 2408.11792'),
 (71,81,'Wen et al., EADO-OFDM','same publication; P01 prose calls it DCO-OFDM'),
 (72,32,'Bohata et al., 39 GHz RoFSO','same publication'),
 (73,33,'Dong et al., multiple-target W-band fiber-wireless','same publication'),
 (74,34,'Yan et al., W-band OFDM and two-stage recovery','same publication'),
 (75,35,'Lei et al., DC-offset QPSK LFMCW','same publication'),
 (76,77,'Wen et al., FSO LFM and CPM','same publication'),
 (78,93,'Huang et al., hybrid SAGO FSO/VLC network','same publication'),
 (79,10,'He et al., integrated sensing and communication in optical fibre','same publication'),
 (80,1,'Wen et al., DCO-OFDM metrics and allocation','same publication')
]
save('shared_reference_crosswalk.json',dict(scope='Selected optical references only; PDF bibliography identity comparison, not primary-source validation.',
    records=[dict(p01_reference=a,p02_reference=b,identity=c,relation=d) for a,b,c,d in crosswalk]))
print('Built bibliography, BibTeX, 56 figure/table inventory items, 10 dataset rows, 18 selected claims and 13 reference mappings.')
