import os
import json
import time
from datetime import datetime
from typing import Dict, Any

class CoTLogger:
    """
    The Black Box Record Keeper.
    Ensures every experiment is traceable (PRISMA Requirement).
    """

    def __init__(self, project_root: str):
        self.log_dir = os.path.join(project_root, "analysis", "cot_laboratory", "logs")
        os.makedirs(self.log_dir, exist_ok=True)

    def log_run(self, 
                experiment_name: str, 
                paper_id: str, 
                system_prompt: str, 
                result_bundle: Dict[str, Any]):
        """
        Saves two files for every run:
        1. The PROMPT (Reviewer Evidence): What exactly did we ask?
        2. The RESULT (Data Evidence): What exactly did it answer?
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        run_id = f"{timestamp}_{paper_id}_{experiment_name}"
        
        # 1. Save System Prompt (Markdown)
        # This allows us to prove exactly what instructions were used at that moment.
        prompt_file = os.path.join(self.log_dir, f"{run_id}_PROMPT.md")
        with open(prompt_file, 'w', encoding='utf-8') as f:
            f.write(system_prompt)
            # Append User Prompt context if needed, usually passed in logic
            
        # 2. Save Full Result (JSON)
        # Includes metadata + raw response + parsed output
        result_file = os.path.join(self.log_dir, f"{run_id}_RESULT.json")
        
        # Enrich bundle with timestamp
        log_data = {
            "run_id": run_id,
            "timestamp": timestamp,
            "paper_id": paper_id,
            "experiment": experiment_name,
            **result_bundle # Unpack the assembler result
        }
        
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=2, ensure_ascii=False)
            
        return run_id
