# Project Brief: O-ISAC Systematic Review

## Core Objective
Conduct a **Systematic Review** of **Optical Integrated Sensing and Communication (O-ISAC)** systems, strictly adhering to the **PRISMA 2020** guidelines and the specific protocol defined in `protocol/prisma_protocol.md`.

## Scope
The review covers physical-layer implementations of O-ISAC in two primary domains:
1.  **Cabled O-ISAC (Fiber-based):** Joint sensing (e.g., vibration, temp) and comms on optical fiber.
2.  **Wireless O-ISAC:** Free-Space Optical (FSO), Visible Light Communication (VLC), and LiDAR-based systems.

## Critical Constraints
*   **Protocol Adherence:** All steps (screening, extraction, synthesis) must follow the protocol.
*   **Data Integrity:** The source data (`IEEE_511_OISAC_Results_Screened.csv`) is part of the record and must be treated as the "Phase 1" truth.
*   **Reproducibility:** All analysis methodology (scripts, schemas) must be version-controlled.

## Key Deliverables
1.  **Screening Reports:** Statistical summaries of study selection (Phase 1 Complete).
2.  **Extraction Schema:** A unified YAML/JSON structure for collecting technical parameters.
3.  **Physical-Layer Taxonomy:** A unified framework categorizing systems by medium, waveform, and integration strategy.
