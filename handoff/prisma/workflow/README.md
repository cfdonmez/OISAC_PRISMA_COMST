# O-ISAC PRISMA Calisma Kiti

Bu klasor, Optical Integrated Sensing and Communication (O-ISAC) for 6G konulu PRISMA-grounded narrative systematic review with a scoping-style PCC component calismasini adim adim yurutmek icin kullanilir. Amac tek seferde manuscript yazmak degil; once kapsam, PCC framework, search kararleri, secim gerekceleri, veri cekme, kalite degerlendirmesi, sentez ve raporlama adimlarini izlenebilir bicimde ilerletmektir.

Calisma aciklamalari, workflow yonlendirmeleri, karar notlari ve ara notlar Turkce yazilir. Manuscript-ready title, abstract, research question, section draft, table caption ve akademik metin taslaklari English hazirlanir.

## Kaynak Baglam

Bu klasordeki tum calisma `../PROJECT_CONTEXT_OISAC_PRISMA.md` dosyasindaki kararlara gore yurutulur. Yeni metodolojik kararlar alindiginda once proje baglami guncellenmeli, sonra ilgili workflow dosyalarina islenmelidir.

Ana metodolojik kararlar:

- Calisma konusu: Optical Integrated Sensing and Communication (O-ISAC) for 6G.
- Manuscript-ready title: Optical Integrated Sensing and Communication for 6G: A PRISMA-Grounded Systematic Review and Metric-Governed Cross-Modality Survey.
- Review tipi: PRISMA-grounded narrative systematic review with a scoping-style PCC component.
- Framework: PCC - Population / Concept / Context; PICO kullanilmayacak.
- Search window: January 1, 2020 - June 30, 2026.
- Search freeze date: planned search freeze date: June 30, 2026.
- Core primary databases: Scopus, IEEE Xplore.
- Selected supplementary sources: ScienceDirect, SpringerLink, Wiley Online Library, Taylor & Francis Online.
- Language: English only.
- Meta-analysis planlanmamistir.
- Kapsam: fiber, FSO, VLC/LiFi, photonic-THz ve hybrid optical systems.
- Ana katki: taxonomy, metric-governed comparison, rate-sensing tradeoff synthesis, validation maturity, benchmark readiness ve research roadmap.
- O-ISAC operational definition: optical or photonic systems in which sensing and communication functions are jointly considered, integrated, co-designed, co-optimized, or evaluated within the same architecture, optical link, waveform/resource framework, hardware platform, channel model, or application scenario.
- Primary technical evidence corpus: peer-reviewed journal articles, early-access journal articles, and full-length conference/proceedings papers.
- Contextual corpus: review/survey papers and pre-2020 foundational studies; contextual records primary technical evidence sayilmaz.
- 6G relevance strict keyword-only inclusion criterion degildir; direct / inferred / weak / not applicable olarak kodlanir.
- Screening decision categories: include_primary, include_contextual, exclude, unclear_full_text_needed, duplicate, date_uncertain.

## PRISMA Kaynaklari

- BMJ PRISMA 2020 Explanation and Elaboration: https://doi.org/10.1136/bmj.n160
- PRISMA 2020 statement: https://www.prisma-statement.org/prisma-2020-statement
- PRISMA 2020 checklist: https://www.prisma-statement.org/prisma-2020-checklist
- PRISMA 2020 flow diagram: https://www.prisma-statement.org/prisma-2020-flow-diagram

Mevcut ana dosyalar:

- `../PRISMA_2020_expanded_checklist.pdf`: PRISMA 2020 genisletilmis checklist.
- `../PRISMA_2020_kontrol_listesi_TR.md`: Turkce takip listesi.
- `../PRISMA_2020_flow_diagram_new_SRs_v2.docx`: PRISMA akis diyagrami sablonu.

Bu PDF, Word ve checklist dosyalarina dokunulmaz.

## Klasor Haritasi

1. `00_baslangic`: konu, PCC framework, kapsam, research question ve ilk kararlar.
2. `01_protokol`: protokol sablonu ve protokol kalite kontrolu.
3. `02_arama`: veri tabani arama plani, sorgu kaydi ve arama gunlugu.
4. `03_secim`: baslik/ozet tarama, tam metin secim ve dislama kayitlari.
5. `04_veri_cekme`: dahil edilen calismalardan veri cikarma formlari.
6. `05_kalite_kanit`: TQAF-style technical quality assessment ve kanit gucu nitelendirmesi.
7. `06_sentez`: structured narrative synthesis, taxonomy mapping, metric-governed comparison ve roadmap sentezi.
8. `07_raporlama`: PRISMA uyumlu manuscript iskeleti ve teslim kontrolu.
9. `08_bilgi_notlari`: surec boyunca basvurulacak kisa know-how notlari.
10. `09_kayitlar`: karar gunlugu, ilerleme takip tablosu ve Codex'e sorulacak sorular.

## Beraber Nasil Calisacagiz?

Her turda bir dosya veya bir is adimi uzerinde ilerlenir:

1. `00_baslangic/01_konu_ve_soru_formu.md` dosyasi O-ISAC PCC ve research questions icin temel formdur.
2. `00_baslangic/02_kapsam_ve_hizli_kalite_kontrol.md` dosyasi kapsam, arama uygulanabilirligi ve kalite yaklasimi icin hizli kontrol saglar.
3. Protokol, `01_protokol/01_protokol_sablonu.md` dosyasinda PRISMA-grounded narrative systematic review olarak yazilir.
4. Arama stratejisi `02_arama/01_arama_plani.md`, `02_arama/database_source_pool.md` ve `02_arama/search_log.csv` ile kurulur.
5. Kayitlar ve secim gerekceleri `03_secim` dosyalarinda izlenir.
6. Dahil edilen calismalardan veri `04_veri_cekme/data_extraction.csv` ile cekilir.
7. Kalite ve kanit gucu `05_kalite_kanit` altinda TQAF-style yaklasimla nitelendirilir.
8. Bulgular `06_sentez` ve `07_raporlama` ile English manuscript-ready metne donusturulur.

## Ilk Yapilacak Is

Baslangic icin `00_baslangic/01_konu_ve_soru_formu.md` ve `00_baslangic/02_kapsam_ve_hizli_kalite_kontrol.md` dosyalarindaki kararlar korunur. Arama fiilen yurutulene kadar tarih ifadesi `planned search freeze date: June 30, 2026` olarak kalmalidir; `final search date` ifadesi kullanilmamalidir.
