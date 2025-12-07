# System Patterns

## Technical Architecture
*   **Scripts:** Use **Python** for data analysis and visualization. Use **PowerShell** for file system operations.
*   **Data Formats:**
    *   Input Data: `.csv` (e.g., screening results).
    *   Config/Schema: `.yaml` (for extraction forms).
    *   Reports: `.md` (Markdown).
*   **Paths:**
    *   Use absolute paths when possible in tool calls, but relative paths in repository documentation.

## Process Rules
1.  **Read-Only Inputs:** Do not modify the source screening CSVs. Always read them and generate *new* outputs.
2.  **Artifact First:** Generate analysis as an "Artifact" first (in `.gemini` brain), then commit to the repo (`analysis/` folder) upon approval.
3.  **Protocol-Driven:** Every decision (e.g., "Should I include this?") must track back to a section in `prisma_protocol.md`.
4.  **Git Disciplince:** Commit changes after completing a logical "Phase" or significant "Task chunk".
5.  **Identifier Standards:**
    *   **Track_ID:** Unique identifier for included studies (Format: `O_ISAC_XXX`, e.g., `O_ISAC_001`). This ID must be the **first column** in all data CSVs (`included_studies_list.csv`, `extraction_dataset.csv`) to maintain relational integrity.
    *   **PDF Naming:** `[Track_ID]_[FirstAuthor]_[Year].pdf` (e.g., `O_ISAC_001_Rosmaninho_2025.pdf`). Store in `data/retrieved_docs`.

## Decision Log
*   **Exclusion Logic:** "No optical carrier" is the primary exclusion reason for RF-ISAC papers.
*   **Taxonomy:** we differentiate primarily by **Medium** (Fiber vs Wireless) as per Protocol Section 8.
