# VII-F Preflight Patch Note

1. Replaced the weak axis-list scope framing with a hardened, data-derived VII-F scope block in `VII-F_PREFLIGHT_PATCH.md`.
2. Retained the existing VII-F scope label wording (`cross-domain Section VII application view`) and did not introduce a new label.
3. Added explicit numeric scope evidence using VII-F summary artifacts: `204/221`, `104/221`, `81/221`, and `n_unique_micro_domains=48`.
4. Added precise artifact locators for scope evidence (`section7F_summary.json`, `s7f_macro_med_cov.csv`, `s7f_micro_dom_cnts.csv`, `section7F_transfer_map.csv`).
5. Hardened scenario `evidence_source` fields by binding row locators to cite keys explicitly, e.g., `:39(O_ISAC_038)`.
6. Re-validated all scenario cite keys against `data/references.bib`; no missing keys found.
7. Performed citekey-locator consistency audit across all four scenarios; no mismatches remained.
8. Verified markdown paths via fallback inventory (`file_index.csv` had `0/8` hits; `II_markdown_inventory.csv` had `8/8` hits).
9. Checked duplicate-folder paths (`O_ISAC_143`, `O_ISAC_108`) and retained them because they exist on disk.
10. Shortlist scenarios and scope-fit notes were preserved; only scope hardening and audit-tight consistency updates were applied.

