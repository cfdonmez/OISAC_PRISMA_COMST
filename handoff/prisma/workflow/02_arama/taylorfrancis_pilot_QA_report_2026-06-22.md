# Taylor & Francis Online Pilot QA Report – 2026‑06‑22

**PASS**
- All three Taylor & Francis raw CSV exports are represented.
- Audit package is available.
- Pilot status is documented.
- Taylor & Francis pilot rows are now synchronized across search_log.csv, progress_tracker.md and decision_log.md.
- PRISMA flow counts remain TBD.
- No included studies were created.

**WARNING**
- Taylor & Francis pilot results are low‑yield and noisy.
- TF‑PILOT‑P2C includes many records outside the intended 2020‑2026 window, suggesting date‑filter/export mismatch.
- Some records have anomalous or unreliable year metadata.
- Most records are false positives, unrelated legacy records, technical news, non‑O‑ISAC material, or generic communication/sensing records.
- TF‑PILOT‑P2A/P2B/P2C should not be retained as strong final candidate searches.
- Taylor & Francis may remain only as optional tight exact‑phrase supplementary source.

**FAIL**
- None (unless required files are missing, which they are not).
