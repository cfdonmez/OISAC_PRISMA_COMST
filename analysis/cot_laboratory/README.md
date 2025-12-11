# 🧪 O-ISAC Extraction Laboratory (CoT Architecture)

This directory contains the modular **Chain-of-Thought (CoT)** extraction system designed for the O-ISAC Systematic Review. It replaces monolithic scripts with a **"Legos & Recipes"** architecture to ensure maintainability and experiment tracking.

---

## 🔄 Master Workflow

```mermaid
flowchart TB
    subgraph User["👤 User"]
        U1[Select Recipe]
        U2[Provide Paper Content]
    end
    
    subgraph Assembler["🏭 core/assembler.py"]
        A1[Load Recipe YAML] --> A2[Read Module Files]
        A2 --> A3[Build System Prompt]
        A3 --> A4[Call Groq API]
        A4 --> A5[Parse JSON Response]
    end
    
    subgraph Logger["📝 core/logger.py"]
        L1[Save PROMPT.md] --> L2[Save RESULT.json]
    end
    
    subgraph Modules["📦 modules/"]
        M1[reasoning/*.md] --> A2
        M2[formatting/*.yaml] --> A2
    end
    
    subgraph Recipes["📋 recipes/"]
        R1[experiment_v1.yaml] --> A1
    end
    
    U1 --> R1
    U2 --> A4
    A5 --> L1
```

---

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
│   ├── batch_runner.py      # Batch processing for multiple papers
│   └── logger.py            # Logs every run for PRISMA traceability
│
├── logs/                    # [MEMORY] Execution evidence logs
└── README.md                # This file
```

---

## 🚀 How It Works

### Execution Flow

```mermaid
sequenceDiagram
    participant User
    participant Assembler
    participant Modules
    participant Groq API
    participant Logger

    User->>Assembler: run_extraction(recipe, content)
    Assembler->>Modules: Load reasoning modules
    Modules-->>Assembler: 00_role.md, 01_concept.md...
    Assembler->>Modules: Load formatting schema
    Modules-->>Assembler: schema_v2.yaml
    Assembler->>Assembler: Build System Prompt
    Assembler->>Groq API: Send prompt + content
    Groq API-->>Assembler: JSON Response
    Assembler->>Logger: log_run(prompt, result)
    Logger-->>User: 20251211_093015_O_ISAC_029_...
```

1.  **Pick a Recipe:** You decide what you want to extract (e.g., "Just fast tuning" or "Deep benchmark analysis").
2.  **Assembler Builds Prompt:** The Python engine reads the recipe, fetches the requested text modules (Legos) from `modules/`, and stitches them into a single System Prompt.
3.  **Execution & Logging:** The engine calls the LLM and records the exact combination used in `logs/` to ensure reproducibility.

---

## 🧠 The Logic Cascade (CoT Mechanism)

How do the "Legos" talk to each other? The system follows a **Chain-of-Thought** flow before outputting any JSON:

```mermaid
flowchart LR
    subgraph Phase1["Phase 1"]
        P1[🎭 Role Definition<br/>Mod 00]
    end
    
    subgraph Phase2["Phase 2"]
        P2[🔧 Concept Tuning<br/>Mod 01]
    end
    
    subgraph Phase3["Phase 3"]
        P3[📊 Reality Check<br/>Mod 02]
    end
    
    subgraph Phase4["Phase 4"]
        P4[🎯 Strategic Critique<br/>Mod 03]
    end
    
    subgraph Phase5["Phase 5"]
        P5[📋 Schema Filling<br/>Formatting]
    end
    
    P1 --> P2 --> P3 --> P4 --> P5
```

| Phase | Module | Action | Purpose |
|-------|--------|--------|---------|
| 1 | [`00_role_definition.md`](modules/reasoning/00_role_definition.md) | Set persona as "Senior Research Architect" | Establishes domain expertise tone |
| 2 | [`01_concept_tuning.md`](modules/reasoning/01_concept_tuning.md) | Identify ISAC Mechanism (TDM/FDM/Joint) | Prevents wrong categorization |
| 3 | [`02_benchmark_compare.md`](modules/reasoning/02_benchmark_compare.md) | Cross-check metrics vs hardware limits | Hallucination filter |
| 4 | [`03_critical_analysis.md`](modules/reasoning/03_critical_analysis.md) | Find "Solved" vs "Open Challenges" | Quality text for survey |
| 5 | [`schema_v2.yaml`](modules/formatting/schema_v2.yaml) | Fill 113-field JSON | Structured output |

---

## 📋 Log File Format

Logs are saved with full timestamp for traceability:

```
YYYYMMDD_HHMMSS_<paper_id>_<model>_<type>.ext
│        │       │          │       │
│        │       │          │       └─ PROMPT.md or RESULT.json
│        │       │          └─ LLM model name
│        │       └─ Paper identifier
│        └─ Time: Hour Minute Second
└─ Date: Year Month Day
```

**Example:** `20251211_093015_O_ISAC_029_llama-3.3-70b-versatile_RESULT.json`
- Date: 2025-12-11
- Time: 09:30:15
- Paper: O_ISAC_029
- Model: llama-3.3-70b-versatile
- Type: RESULT (extraction output)

---

## 🛠️ How to Extend

*   **To change the Logic:** Don't touch Python code. Edit/Add a markdown file in `modules/reasoning/`.
*   **To change the Output Format:** Edit `modules/formatting/schema_v2.yaml`.
*   **To run a new Experiment:** Create a new YAML file in `recipes/`.

---

## 🔗 Related Documentation

- [Notebooks README](../notebooks/README.md) - Pipeline notebook documentation
- [Recipe Example](recipes/experiment_v1_full_analysis.yaml) - Full analysis recipe

---
**Maintained by:** Antigravity & User  
**Status:** Active Development  
**Last Updated:** 2025-12-11
