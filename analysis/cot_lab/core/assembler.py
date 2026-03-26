from .logger import CoTLogger
import yaml
import os
import json
import re  # Added for Regex
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
        system_prompt_parts.append("\nCRITICAL INSTRUCTION: You must output your analysis as a valid JSON object matching the provided schema. Do not add any markdown formatting or chatter.\n")
        system_prompt_parts.append("IMPORTANT: You must START your JSON with 'step_0_visual_inspection' and explicitly describe the visual evidence.\n")
            
        return "".join(system_prompt_parts)

    def _repair_json(self, json_str: str) -> str:
        """Fixes common JSON syntax errors like unbalanced brackets."""
        stack = []
        fixed = []
        in_string = False
        escape = False
        
        for char in json_str:
            if in_string:
                if char == '\\' and not escape:
                    escape = True
                elif char == '"' and not escape:
                    in_string = False
                else:
                    escape = False
                fixed.append(char)
            else:
                if char == '"':
                    in_string = True
                    fixed.append(char)
                elif char in '{[':
                    stack.append(char)
                    fixed.append(char)
                elif char in '}]':
                    if not stack:
                        continue # Ignore extra closing brackets
                    last = stack.pop()
                    expected = '}' if last == '{' else ']'
                    if char != expected:
                        fixed.append(expected) # Correct mismatch
                    else:
                        fixed.append(char)
                else:
                    fixed.append(char)
                    
        # Close remaining open structures
        while stack:
            last = stack.pop()
            fixed.append('}' if last == '{' else ']')
            
        return "".join(fixed)

    def _clean_json(self, raw_text: str) -> str:
        """Attempts to extract valid JSON from markdown-wrapped text."""
        import re
        
        # 1. Extract content from Markdown wrappers
        cleaned = raw_text.strip()
        if "```" in cleaned:
             pattern = r"```(?:json)?\s*(\{.*?\})\s*```"
             match = re.search(pattern, cleaned, re.DOTALL)
             if match:
                 cleaned = match.group(1)
             else:
                 # Fallback: Find outer braces
                 start = cleaned.find("{")
                 end = cleaned.rfind("}")
                 if start != -1 and end != -1:
                     cleaned = cleaned[start:end+1]
        else:
             start = cleaned.find("{")
             end = cleaned.rfind("}")
             if start != -1 and end != -1:
                 cleaned = cleaned[start:end+1]

        # 2. Fix Trailing Commas
        cleaned = re.sub(r",\s*([\]}])", r"\1", cleaned)
        
        # 3. Structural Repair (Unbalanced/Mismatched Brackets)
        cleaned = self._repair_json(cleaned)
        
        return cleaned

    def run_extraction(self, recipe_path: str, paper_text: str, paper_id: str = "Unknown", visual_content: str = None, image_data: list = None) -> Dict[str, Any]:
        """
        Executes the full extraction process AND logs it.
        Now supports 'visual_content' (text descriptions) and 'image_data' (base64 encoded images).
        """
        # 1. Load Recipe
        print(f"[INFO] Loading Recipe: {recipe_path}...")
        recipe = self.load_recipe(recipe_path)
        target_model = recipe.get("metadata", {}).get("target_model", "llama-3.3-70b-versatile")
        
        # Override model if images are provided
        if image_data and len(image_data) > 0:
            target_model = "meta-llama/llama-4-scout-17b-16e-instruct"
            print(f"[INFO] 🖼️ Images detected! Switching model to: {target_model}")
            
        params = recipe.get("parameters", {})
        experiment_name = recipe.get("metadata", {}).get("target_model", "experiment")

        # 2. Build Prompt
        print("[INFO] Assembling System Prompt from Modules...")
        system_prompt = self.build_system_prompt(recipe)

        # 3. Prepare User Content
        messages = []
        # Case A: Standard Text (or Text + Visual Descriptions)
        if not image_data:
            final_user_content = "Analyze the following paper content:\n\n"
            if visual_content and visual_content.strip():
                final_user_content += f"=== VISUAL ANALYSIS DATA (Charts/Figures) ===\n{visual_content}\n\n"
            final_user_content += f"=== FULL PAPER TEXT ===\n{paper_text}"
            
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": final_user_content}
            ]
            
        # Case B: Multimodal (Text + Direct Images)
        else:
            final_user_content = []
            
            # Add images first (Context)
            for b64_img in image_data:
                final_user_content.append({
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{b64_img}"
                    }
                })
            
            # Add text
            text_payload = "Analyze the provided paper images and the following text:\n\n"
            text_payload += f"=== FULL PAPER TEXT ===\n{paper_text}\n\n"
            text_payload += "!!! CONSTRAINT: The first item in 'reasoning_trace' MUST be 'step_0_visual_inspection'. Do NOT skip it. !!!"
            
            final_user_content.append({"type": "text", "text": text_payload})
            
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": final_user_content}
            ]

        # 4. Call API
        print(f"[INFO] Calling Groq API (Model: {target_model})...")
        result_bundle = {}
        try:
            # Note: Vision models may not strictly support json_mode, so we handle it manually
            use_json_mode = params.get("json_mode") and not image_data
            
            completion = self.client.chat.completions.create(
                messages=messages,
                model=target_model,
                temperature=params.get("temperature", 0.1),
                max_tokens=params.get("max_tokens", 6000),
                response_format={"type": "json_object"} if use_json_mode else None
            )
            
            # 4. Process Response
            raw_response = completion.choices[0].message.content
            print(f"\n[DEBUG] RAW RESPONSE LEN: {len(raw_response)}")
            print(f"[DEBUG] RAW RESPONSE START: {raw_response[:200]}...")
            
            # Clean JSON if we didn't use strict mode
            if not use_json_mode:
                cleaned_response = self._clean_json(raw_response)
                print(f"[DEBUG] CLEANED RESPONSE START: {cleaned_response[:200]}...")
                try:
                    parsed_json = json.loads(cleaned_response)
                except json.JSONDecodeError:
                    print(f"[ERROR] JSON PARSE FAILED. FULL RAW CONTENT:\n{raw_response}")
                    raise
            else:
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
