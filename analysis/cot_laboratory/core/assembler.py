from .logger import CoTLogger
import yaml
import os
import json
from groq import Groq
from typing import Dict, Any, Optional

class CoTAssembler:
    """
    The Engine of the CoT Laboratory.
    Responsibilities:
    1. Read the Recipe (YAML)
    2. Fetch the Ingredients (Modules/Prompts)
    3. Mix them (Build System Prompt)
    4. Cook (Call LLM API)
    5. Record (Log via Logger)
    """
    
    def __init__(self, project_root: str):
        self.project_root = project_root
        self.logger = CoTLogger(project_root)
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set!")
        self.client = Groq(api_key=self.api_key)

    def load_recipe(self, recipe_path: str) -> Dict[str, Any]:
        """Loads the YAML configuration file."""
        full_path = os.path.join(self.project_root, recipe_path)
        with open(full_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def _read_module(self, relative_path: str) -> str:
        lab_root = os.path.join(self.project_root, "analysis", "cot_laboratory")
        full_path = os.path.join(lab_root, relative_path)
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"[ERROR: Module not found at {relative_path}]"

    def build_system_prompt(self, recipe: Dict[str, Any]) -> str:
        system_prompt_parts = []
        system_prompt_parts.append("<!-- O-ISAC CHAIN-OF-THOUGHT SYSTEM PROMPT -->\n")
        for step in recipe.get("steps", []):
            module_name = step.get("name", "Unknown Module")
            module_path = step.get("path")
            content = self._read_module(module_path)
            system_prompt_parts.append(f"\n# === MODULE: {module_name} ===\n")
            system_prompt_parts.append(content)
            system_prompt_parts.append("\n# =============================\n")
        
        # CRITICAL: Groq API requires the word 'json' in the prompt to use JSON mode
        system_prompt_parts.append("\nCRITICAL INSTRUCTION: You must output your analysis as a valid JSON object matching the provided schema.\n")
            
        return "".join(system_prompt_parts)

    def run_extraction(self, recipe_path: str, paper_text: str, paper_id: str = "Unknown", visual_content: str = None) -> Dict[str, Any]:
        """
        Executes the full extraction process AND logs it.
        Now supports 'visual_content' (text descriptions of charts/tables).
        """
        # 1. Load Recipe
        print(f"[INFO] Loading Recipe: {recipe_path}...")
        recipe = self.load_recipe(recipe_path)
        target_model = recipe.get("metadata", {}).get("target_model", "llama-3.3-70b-versatile")
        params = recipe.get("parameters", {})
        experiment_name = recipe.get("metadata", {}).get("target_model", "experiment")

        # 2. Build Prompt
        print("[INFO] Assembling System Prompt from Modules...")
        system_prompt = self.build_system_prompt(recipe)

        # 3. Prepare User Content (Text + Visuals)
        final_user_content = "Analyze the following paper content:\n\n"
        if visual_content and visual_content.strip():
            final_user_content += f"=== VISUAL ANALYSIS DATA (Charts/Figures) ===\n{visual_content}\n\n"
        
        final_user_content += f"=== FULL PAPER TEXT ===\n{paper_text}"

        # 4. Call API
        print(f"[INFO] Calling Groq API (Model: {target_model})...")
        result_bundle = {}
        try:
            completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": final_user_content}
                ],
                model=target_model,
                temperature=params.get("temperature", 0.1),
                max_tokens=params.get("max_tokens", 6000),
                response_format={"type": "json_object"} if params.get("json_mode") else None
            )
            
            # 4. Process Response
            raw_response = completion.choices[0].message.content
            parsed_json = json.loads(raw_response)
            
            result_bundle = {
                "status": "success",
                "model_used": target_model,
                "parsed_output": parsed_json,
                "raw_response": raw_response
            }

        except Exception as e:
            result_bundle = {
                "status": "error",
                "error_message": str(e)
            }
        
        # 5. Log Everything (The Black Box)
        print("[INFO] Logging Run Evidence...")
        run_id = self.logger.log_run(experiment_name, paper_id, system_prompt, result_bundle)
        print(f"[OK] Run Logged: {run_id}")
        
        return result_bundle
