# 📂 PDF Storage (Retrieved Documents)

This folder is the **"Input Hopper"** for the Analysis Engine.

## ⚠️ Critical Rules

1.  **Naming Convention:**
    *   Files MUST be named `O_ISAC_[ID].pdf`.
    *   Example: `O_ISAC_001.pdf`, `O_ISAC_042.pdf`.
    *   *Do NOT use original filenames like "ieee_explore_1234.pdf".*

2.  **Processing Trigger:**
    *   Any **NEW** PDF added here will be automatically detected by the `extraction_pipeline_v3.py`.
    *   If you update a PDF (replace it), it will be re-processed in the next batch.

3.  **Folder Structure:**
    *   Keep it flat. Do not create subfolders here unless archiving old files.
    *   The pipeline reads `.pdf` files directly from this root.
