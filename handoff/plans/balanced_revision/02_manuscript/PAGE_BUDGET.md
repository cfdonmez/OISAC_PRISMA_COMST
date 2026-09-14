# Sayfa Bütçesi — Dengeli Revizyon

Baseline: 27 çift sütun sayfa.  
Hard cap: 30 sayfa.  
Operasyonel hedef: 29--30 sayfa.

| Taşıyıcı | Brüt değişim hedefi |
|---|---:|
| Section III verification yöntemi | +0.2--0.3 |
| Section V verified cards / comparison carrier | +1.0--1.3 |
| Section VI decision/validation bağlantısı | +0.4--0.6 |
| Section VIII quantified roadmap | +0.7--0.9 |
| Abstract, Introduction, Conclusion | +0.2--0.4 |
| Float/layout buffer | +0.4--0.6 |
| Brüt artış | +2.9--4.1 |
| Tekrar eden inventory/taxonomy prose azaltımı | -0.7--1.2 |
| Beklenen final | 29.0--30.0 |

## Kapılar

- Section V ilk entegre build sonrasında PDF `<=29.5` olmalıdır.
- Section VIII sonrasında ilk tam build `<=31` olabilir; 31'i aşarsa yeni içerik
  durur ve carrier allocation yeniden yapılır.
- Release build `<=30` olmalıdır.
- References ve author biographies varsa sayfa sayımına dahildir.
- `\footnotesize` altına inilmez; figure/table text final ölçekte en az 8 pt
  hedeflenir.
- Negatif spacing ve margin hilesi yasaktır.

Sayfa geri kazanımı için önce şunlar incelenir:

1. prose içinde tekrar edilen float envanteri;
2. aynı caveat'ın birden fazla section'da açılması;
3. taxonomy sayımı ile decision lesson'ın aynı paragrafta yinelenmesi;
4. ayrıntılı yöntem bilgisinin supplement pointer'ıyla taşınabilmesi.

