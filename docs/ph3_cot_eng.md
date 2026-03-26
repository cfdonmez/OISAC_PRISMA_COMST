# 🧠 Phase 3: Akıl Yürütme Motoru (CoT Engine) Detayları

> **"Bilgiyi Hikmet'e (Sentez) Çevirmek"**

Burası fabrikanın son ve en karmaşık hattıdır. Phase 1'den gelen **karışık metin** ve Phase 2'den gelen **görsel notlar** burada birleşir ve anlamlı bir bütüne dönüşür.

---

## 🎯 Amaç
Sadece *"Şu rakamı bul"* demek yetmez. Bilimsel bir analiz için modelin **neden** o rakamı seçtiğini, **nasıl** bir karar verdiğini bilmemiz gerekir.
*   Bu rakam simülasyon mu deney mi?
*   Bu sistemin darboğazı ne?
*   Yazarlar neyi iddia ediyor, aslında ne yapmışlar?

---

## ⚙️ Motor: `CoTAssembler` (Chain-of-Thought)

Bu motor, projemize özel yazılmış bir Python sınıfıdır (`analysis/cot_lab/core/assembler.py`).

### Çalışma Prensibi: "Tarif" (Recipe) Sistemi
Sisteme tek bir uzun prompt yazmak yerine, modüler bir **Tarif Dosyası (.yaml)** veririz.

**Dosya:** `analysis/cot_lab/recipes/experiment_v1_full_analysis.yaml`

Bu tarif şunları söyler:
1.  **Adım 1:** Önce `role_definition.md` modülünü oku. (Sen kimsin?)
2.  **Adım 2:** Sonra `concept_tuning.md` modülünü oku. (O-ISAC sistemi nedir?)
3.  **Adım 3:** `schema_v2.yaml` şablonuna bak. (Hangi kutucukları dolduracaksın?)

Bu modüler yapı sayesinde, sistemi güncellemek için kod yazmaya gerek kalmaz; sadece küçük text dosyalarını (`.md`) değiştiririz.

---

## 🏗️ Süreç Akışı (Reasoning Trace)

Modelden direkt JSON istersek halüsinasyon görebilir. O yüzden onu **"Sesli Düşünmeye"** zorlarız. JSON çıktısının başında zorunlu bir `reasoning_trace` (akıl yürütme izi) alanı vardır.

Model şu sırayla düşünmek **ZORUNDADIR**:

1.  **`step_0_visual_inspection`:** *"Görsel analiz metnini okudum. Şekil 3'te bir deney düzeneği görüyorum.."* (Kanıt sunar).
2.  **`step_1_concept_analysis`:** *"Bu makale FSO tabanlı bir sistem öneriyor, RF kullanılmamış."*
3.  **`step_2_benchmark_verification`:** *"Buldukları 100 Gbps hız, 1550nm dalgaboyunda fiziksel olarak mümkün."*
4.  **`step_3_strategic_critique`:** *"Ancak sisli havada ne olacağını test etmemişler."*

Model ancak bu adımları bitirdikten sonra asıl veri tablosunu (JSON) doldurur.

---

## 🛡️ Hata Koruması (Safety Nets)

1.  **JSON Onarımı:** LLM bazen parantez hatası yapar (`}}` yerine `}`). `_repair_json` fonksiyonumuz bunu otomatik düzeltir.
2.  **Schema Doğrulama:** Çıkan verinin bizim istediğimiz formatta olup olmadığı kontrol edilir.

---

## 📂 Çıktı: `extraction_v4_unified.json`

Bu dosya, makalenin dijital ikizidir.

*   `Study_Level`: Makalenin künyesi, temel iddiası.
*   `Experiments[]`: Yapılan her deneyin ayrı ayrı parametreleri (Verici gücü, Alıcı tipi, Hatalar).
*   `Quality_Assessment`: Çalışmanın güvenilirlik puanı.

[🔙 Ana Kılavuza Dön](v4_pipe_expl.md)
