# 📓 Analysis Notebooks

This folder contains the Jupyter Notebooks and Scripts for the O-ISAC Systematic Review.

## 🚀 The PRIMARY Tool
**`OISAC_Extraction_Pipeline_v3.ipynb`**
*   **Use This For:** Everything.
*   **Function:** It is the "Master Controller". It imports the extraction script and runs the full pipeline (PDF -> Image -> Vision -> JSON).
*   **Platform:** Google Colab (Requires GPU).

## 🧩 Supporting Scripts
*   **`extraction_pipeline_v3.py`**: The "Engine Room". Contains the python logic (Classes, API calls) used by the notebook.
*   **`CoT_Vision_Factory_Runner.ipynb`**: *Legacy/Component.* Focused only on the vision part. Use the Master Notebook instead.
*   **`prep_batch_data.py`**: A local utility to check file readiness.

## 📊 Analysis & Reporting
*   **`PRISMA_Flowchart_Generator.ipynb`**: Generates the PRISMA flow diagram from the metrics.
*   **`04_figures_tables.ipynb`**: Creates the charts for the final paper.
