# 🧪 O-ISAC Extraction Laboratory (CoT Architecture)

This directory contains the modular **Chain-of-Thought (CoT)** extraction system designed for the O-ISAC Systematic Review. It replaces monolithic scripts with a **"Legos & Recipes"** architecture to ensure maintainability and experiment tracking.

## 📂 Directory Structure

```text
analysis/cot_laboratory/
├── modules/                 # [LEGOS] Indivisible logic blocks (Prompts)
│   ├── reasoning/           # Thinking logic (e.g., "compare numbers", "find gaps")
│   └── formatting/          # Output schemas (e.g., JSON structure)
│
├── recipes/                 # [RECIPES] Configurations defining an experiment
│   └── experiment_v1.yaml   # "Combine Module A + B + Schema C"
│
├── core/                    # [ENGINE] Python code (No hardcoded prompts here!)
│   ├── assembler.py         # Builds the full prompt from a Recipe
│   └── logger.py            # Logs every run for PRISMA traceability
│
├── logs/                    # [MEMORY] Daily execution logs
└── README.md                # This file
```

## 🚀 How It Works

1.  **Pick a Recipe:** You decide what you want to extract (e.g., "Just fast tuning" or "Deep benchmark analysis").
2.  **Assembler Builds Prompt:** The Python engine reads the recipe, fetches the requested text modules (Legos) from `modules/`, and stitches them into a single System Prompt.
3.  **Execution & Logging:** The engine calls the LLM and records the exact combination used in `logs/` to ensure reproducibility.

## 🧠 The Logic Cascade (CoT Mechanism)

How do the "Legos" talk to each other? The system follows a **Chain-of-Thought** flow before outputting any JSON:

1.  **Phase 1: Role Definition (Mod 00):** 
    *   *Input:* "Act as a Senior Research Architect."
    *   *Output:* Sets the sophisticated tone and domain knowledge base.
2.  **Phase 2: Concept Tuning (Mod 01):**
    *   *Action:* Identifies the specific ISAC Mechanism (e.g., TDM, FDM, Joint Waveform).
    *   *Why:* Prevents analyzing a "TDM system" as if it were a "Joint Waveform" one.
3.  **Phase 3: Reality Check (Mod 02):**
    *   *Action:* Cross-checks reported metrics (Speed) against Hardware limits (Bandwidth).
    *   *Why:* Hallucination filter. If numbers don't match physics, it flags them.
4.  **Phase 4: Strategic Critique (Mod 03):**
    *   *Action:* Identifies "Solved Problems" vs "Open Challenges" based on the previous findings.
    *   *Why:* Creates high-quality text for the Survey's "Future Directions" section.
5.  **Phase 5: Schema Filling (Formatting):**
    *   *Action:* ONLY after these 4 thinking steps, the model fills the 113-field JSON.
    *   *Result:* High-precision, verified data extraction.

## 🛠️ How to Extend

*   **To change the Logic:** Don't touch Python code. Edit/Add a markdown file in `modules/reasoning/`.
*   **To change the Output Format:** Edit `modules/formatting/schema.yaml`.
*   **To run a new Experiment:** Create a new YAML file in `recipes/`.

---
**Maintained by:** Antigravity & User
**Status:** In Development
