# 📡 O-ISAC Systematic Review (PRISMA 2020)

> **"Optical Integrated Sensing and Communication: A Unified Survey"**

Hoş geldiniz! 👋 Bu repo, **IEEE Communications Surveys & Tutorials (COMST)** dergisi için hazırlanan akademik bir sistematik derleme (survey) projesinin **tüm mutfağını** barındırır.

Burada, literatürdeki binlerce makalenin nasıl tarandığını, nasıl elendiğini ve yapay zeka destekli araçlarla nasıl analiz edildiğini **şeffaf bir şekilde** görebilirsiniz.

---

## 📖 Bu Proje Nedir? (Hikaye)

Biz, **"Fiber optik kablolar ve kablosuz optik sistemler (FSO, VLC) hem haberleşme yapıp hem de ortamı algılayabilir mi?"** sorusunun cevabını arıyoruz. Buna **O-ISAC** (Optical Integrated Sensing and Communication) denir.

Bu repo, bu soruyu cevaplamak için yapılan **bilimsel yolculuğun** dijital kanıtıdır.

---

## 🚦 Proje Durum Paneli (Dashboard)

Şu anda projenin hangi aşamasında olduğumuzu buradan takip edebilirsiniz:

| Aşama | Ne Yapıyoruz? | Durum |
|:---|:---|:---:|
| **1. Planlama** | Kuralları ve protokolü belirledik. ([Protokolü İncele](protocol/prisma_protocol.md)) | ✅ Tamamlandı |
| **2. Arama** | 1200+ makaleyi veritabanlarından bulduk. | ✅ Tamamlandı |
| **3. Eleme** | Başlık ve özet okuyarak ilgisizleri ayıkladık (223+ dahil edildi). | ✅ Tamamlandı |
| **4. PDF Toplama** | Dahil edilen 223+ makalenin tam metinlerini topladık. | ✅ Tamamlandı |
| **5. Veri Madenciliği** | **Pipeline V4 (Vision + CoT)** ile derin analiz yapıyoruz. | 🟢 Devam Ediyor (200+ İşlendi) |
| **6. Benchmark** | V4 vs Legacy sonuçlarını kıyaslıyoruz. | 🟢 Devam Ediyor ([Benchmark Lab](analysis/notebooks/06_Extraction_Benchmark_Lab.ipynb)) |
| **7. Yazım** | Sonuçları COMST taslağına dönüştürüyoruz. | 🟡 Hazırlanıyor |

> **Canlı Süreç:** Bu proje "Onion" (Soğan) mimarisiyle katman katman derinleşir. ([Detaylı Takip Dosyası](data/extraction_tracker.md))

---

## 🛠️ Nasıl Çalışıyoruz? (Teknik Mutfak)

Bu projeyi yönetmek için **Pipeline V4** mimarisini kullanıyoruz:

### 1. Katmanlı Veri İşleme (Onion Structure)
Proje, veriyi merkezden dışa doğru 5 aşamada işler:
1.  **Öz:** Marker V1.0 ile PDF'ten Markdown'a dijitalleştirme.
2.  **Legacy:** Temel meta-veri çıkarımı (O_ISAC_001-066).
3.  **V4 (Vision+CoT):** Llama-3.3-70b ve Vision modelleriyle karmaşık tablo/grafik analizi.
4.  **Benchmark:** Doğruluk kalibrasyonu ve kıyaslama.
5.  **Sentez:** PRISMA uyumlu sistematik raporlama.

### 2. İş Akışımız (Workflow)
```mermaid
graph LR
    A[📄 PDF] --> B(📝 Markdown)
    B --> C{🖼️ Vision Analysis}
    C --> D[🧠 Chain of Thought Extraction]
    D --> E[📊 Structured JSON]
    E --> F[🧪 Benchmark Lab]
```

---

## 📂 Dosyalar Nerede? (Harita)

*   `data/`: **Hazine.** JSON verileri ve [`extraction_tracker.md`](data/extraction_tracker.md).
*   `analysis/notebooks/`: **Laboratuvar.** `CoT_Master_Pipeline.ipynb` ve `06_Extraction_Benchmark_Lab.ipynb`.
*   `protocol/`: **Anayasa.** PRISMA protokolü.

---

## 🤖 İzlenebilirlik ve Şeffaflık

Bir bilimsel çalışmanın en önemli özelliği **tekrarlanabilir** olmasıdır.
*   Her eleme kararı bir CSV dosyasına işlenir.
*   Yapay zekanın her analizi bir "Log" dosyası olarak saklanır.
*   Tüm kıyaslama süreçleri notebook'lar üzerinden şeffafça izlenebilir.

---

**Son Güncelleme:** 2 Ocak 2026
*Bu proje, Açık Bilim (Open Science) ilkelerine adanmıştır.*
