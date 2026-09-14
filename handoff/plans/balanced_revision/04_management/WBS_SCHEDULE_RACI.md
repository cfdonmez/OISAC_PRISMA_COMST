# WBS, Takvim ve RACI — Dengeli Revizyon

## Work packages

| WP | İş | Bağımlılık | Tahmini kişi-saat | Bitiş ölçütü |
|---|---|---|---:|---|
| WP0 | Exact source import, hash, 27-page baseline build | — | 2--3 | G0 PASS |
| WP1 | Selection protocol ve candidate freeze | WP0 | 3--4 | G1 PASS |
| WP2 | Seçilen raporların PDF/hash manifesti ve reviewer packets | WP1 | 3--4 | G2 PASS |
| WP3A/B | İki bağımsız insan doğrulaması | WP2 | 12--14 toplam | İki form tamam |
| WP4 | Uyuşmazlık adjudication ve evidence lock | WP3A+B | 3--4 | G3--G4 PASS |
| WP5 | Cards, decision matrix ve research agenda | WP4 | 5--6 | Traceable carriers hazır |
| WP6 | Abstract, I, III, IV--IX revizyonu | WP5 | 9--10 | G5 PASS |
| WP7 | Build, page recovery, citation ve render QA | WP6 | 5 | G6--G7 PASS |
| WP8 | Author reread, release manifest ve package | WP7 | 2 | G8 PASS |
|  | **Toplam** |  | **44--52** |  |

Kritik zincir:

`WP0 -> WP1 -> WP2 -> (WP3A || WP3B) -> WP4 -> WP5 -> WP6 -> WP7 -> WP8`

## Takvim

| Gün | Ana iş |
|---|---|
| 0 | WP0 baseline freeze |
| 1 | WP1 selection lock + WP2 packets |
| 2 | Reviewer A/B ilk yarı |
| 3 | Reviewer A/B tamamlama + adjudication |
| 4 | Cards, matrix, Section V ve VIII |
| 5 | I, III, IV, VI, VII, IX + entegre build |
| 6 | Teknik reread, page recovery, citation/render QA |
| 7--10 | Yazar geri bildirimi, son düzeltme ve release gate |

## Roller

- `CA`: corresponding/lead author
- `EL`: evidence lead
- `RA`, `RB`: birbirinden bağımsız insan doğrulayıcılar
- `ADJ`: senior scientific adjudicator
- `MW`: manuscript writer/section owner
- `QA`: build, citation ve render QA lead
- `IR`: independent reader
- `ALL`: bütün yazarlar

| WP | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| WP0 | QA | CA | EL | ALL |
| WP1 | EL | ADJ | RA, RB, CA | ALL |
| WP2 | EL | ADJ | RA, RB | CA |
| WP3 | RA, RB | ADJ | EL | CA |
| WP4 | ADJ | CA | RA, RB, EL | ALL |
| WP5 | EL, MW | ADJ | RA, RB | CA |
| WP6 | MW | CA | EL, ADJ, section owners | ALL |
| WP7 | QA, MW | CA | EL, IR | ALL |
| WP8 | QA | CA | ADJ, ALL | ALL |

RA ve RB aynı kişi olamaz; ilk geçişte birbirlerinin kararlarını göremez.
