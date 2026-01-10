# Body Section Templates (Synthesis Strategies)

Bu belge, O-ISAC survey makalesinin gövde bölümlerinde (Section IV, V, VI) kullanılacak sentez yaklaşımlarını ve şablonlarını içerir.

## 🎯 "Non-List" Yazım Politikası
**Asla Yapma:** "Makale [1] şunu yaptı. Makale [2] bunu yaptı." (Annotated Bibliography tarzı).
**Her Zaman Yap Kelimeler:** Makaleleri problem, metodoloji veya sonuç ekseninde gruplayın.

---

## 🏗️ Template 1: Challenge-Based Synthesis
Teknik bir zorluğun nasıl aşıldığını anlatırken kullanılır (Örn: Non-linearity in fibers).

> "Managing **[Challenge Name]** is critical for joint sensing and communication in [System Type]. Early attempts primarily focused on [Category 1: e.g., Digital Compensation], where [Ref A, B] utilized [Technique]. However, these approaches often suffer from [Limitation]. To address this, a more recent trend involves [Category 2: e.g., All-optical Processing], as demonstrated by [Ref C], achieving [Result]. Table [X] provides a comprehensive comparison of these strategies based on complexity and accuracy."

---

## 🏗️ Template 2: Technology/Architecture Synthesis
Farklı mimarilerin karşılaştırılmasında kullanılır (Örn: VLC vs FSO ISAC).

> "The architectural landscape of [Domain] O-ISAC is bifurcated into [Type 1] and [Type 2]. While [Type 1] architectures ([Ref 1, 2]) excel in [Metric A], they are inherently limited by [Metric B]. In contrast, [Type 2] designs ([Ref 3-5]) leverage [Key Component] to bridge this gap. Fig. [Y] illustrates the unified system model that encompasses both paradigms, highlighting the common hardware enablers such as [Component]."

---

## 📊 Visual Standards for Body Sections

Her ana bölüm (Fiber, Wireless, FSO) şu iki görsel elementi içermelidir:

1.  **Unified System Model (Diyagram):** İncelenen tüm makalelerin ortak paydasını gösteren bir blok diyagram.
2.  **Summary Table (Karşılaştırma Tablosu):**
    *   **Sütunlar:** Reference, Integration Level, Key Sensing Metric, Key Comm Metric, Implementation (Sim/Exp).
    *   **Satırlar:** Tek tek makaleler değil, benzer makale grupları için "cluster" satırları kullanılabilir.

---

## 🔑 Engineer's Perspective (Trade-off Analysis)
Her büyük teknoloji başlığının sonunda şu kalıp ile bir analiz yapılmalıdır:

> "From an engineering perspective, the trade-off between [Metric 1] and [Metric 2] remains the primary optimization constraint. As visualized in the **Pareto Frontier (Fig. Z)**, increasing sensing resolution by [X]% typically incurs a [Y]% loss in spectral efficiency when using [Scheme Name]."
