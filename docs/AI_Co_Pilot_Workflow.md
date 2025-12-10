# AI Co-Pilot Workflow: O-ISAC Systematic Review

This guide outlines how to collaborate with an AI assistant to conduct a **PRISMA 2020 Systematic Review**. It is designed for researchers who want to leverage "Agentic AI" (like the one creating this file) to automate the heavy lifting of data management, reporting, and consistency checking.

## 1. The Core Concept: "The Memory Bank"

The most critical component of this workflow is the **Memory Bank**. AIs have limited memory of past conversations. The `memory-bank/` folder in this repository serves as the **External Long-Term Memory**.

*   **Rule #1:** When starting a new session, always ask the AI: *"Please read the `memory-bank/` folder to understand the project context."*
*   **Rule #2:** After completing a major task (e.g., finishing screening), tell the AI: *"Please update `memory-bank/activeContext.md` to reflect our new status."*

## 2. Phase-by-Phase Workflow

### Phase 0: Setup & Protocol
*   **Your Job:** Write the `protocol/prisma_protocol.md`. This is the "Constitution".
*   **AI's Job:** Read it and strictly enforce it.
*   **Action:** Ask the AI, *"Read the protocol and tell me if my rules for exclusion are clear."*

### Phase 1: Screening (Title/Abstract)
*   **Input:** A CSV file from Scopus/IEEE Xplore (e.g., `IEEE_511_OISAC_Results_Screened.csv`).
*   **AI's Job:**
    1.  **Analyze**: Calculate Inclusion/Exclusion rates.
    2.  **Verify**: Check if "Reasons" match the Protocol (e.g., "Exclude RF-only").
    3.  **Report**: Generate a Markdown report (e.g., `Phase1_Screening_Report.md`).
    4.  **Filter**: Create a clean list of studies for the next phase.

### Phase 2: Full-Text Eligibility & Extraction (Current Phase)
*   **Input:** PDF files or full-text text.
*   **AI's Job:**
    1.  **Schema Creation**: Convert Protocol Section 9 into a YAML/JSON form (e.g., `oisac_extraction_schema.yaml`).
    2.  **Extraction**: "Read this PDF and extract the `data_rate` and `sensing_range` according to the schema."
    3.  **Validation**: Flag missing data (`NR`) or inconsistent units.

### Phase 3: Synthesis & Reporting
*   **Input:** The final Extracted Data (CSV/JSON).
*   **AI's Job:**
    1.  **Visualize**: Write Python scripts to plot "Rate vs. Range" trade-offs.
    2.  **Taxonomy**: Help build the "Sunburst Chart" described in the Protocol.
    3.  **Drafting**: Write sections of the final paper based on the data.

## 3. Best Practices for Prompts

| Goal | Recommended Prompt Pattern |
| :--- | :--- |
| **Start Session** | "Read `memory-bank/projectbrief.md` and `activeContext.md`. What is our current task?" |
| **Analyze Data** | "Write a Python script to analyze `[filename.csv]`. Don't guess—calculate the stats." |
| **Save Work** | "Commit these changes to GitHub with a descriptive message." |
| **Check Rules** | "Does this decision align with Section 4.2 of `prisma_protocol.md`?" |

## 4. Directory Structure Role

*   `protocol/`: The fixed rules.
*   `analysis/`: Where the AI puts its work (reports, scripts, cleaned lists).
*   `memory-bank/`: The AI's brain state. **Do not delete this.**

---
*Created by your AI Assistant, December 2025*
