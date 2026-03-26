# =============================================================================
# O-ISAC EXTRACTION PIPELINE v3.0 - Optimized for Colab
# =============================================================================
# Features:
# - Resume/checkpoint support (only process new PDFs)
# - Batched visual analysis for GPU efficiency
# - v2.0 PRISMA schema aligned
# - Async LLM with rate limiting
# - Smart memory management
# Last Updated: 2025-12-08
# =============================================================================

import os
import gc
import glob
import json
import hashlib
import asyncio
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict

try:
    import pandas as pd
except ImportError:
    pd = None
    print("Starting... Pandas not found. CSV/Excel export disabled.")
try:
    from PIL import Image
except ImportError:
    Image = None
    print("Starting... PIL not found. Image processing disabled.")
try:
    import torch
    from transformers import AutoProcessor, AutoModelForCausalLM
except ImportError:
    torch = None
    AutoProcessor = None
    AutoModelForCausalLM = None
    print("Starting... Torch/Transformers not found. heavy local models will be disabled.")
import warnings
warnings.filterwarnings("ignore")

# =============================================================================
# CONFIGURATION
# =============================================================================
class Config:
    # 🌍 Environment & Path Detection
    if os.path.exists("/content/drive"):
        # Google Colab
        PROJECT_PATH = "/content/drive/MyDrive/AKU_WorkSpace/survey_fdgit/OISAC_PRISMA_COMST"
        print("Environment: Google Colab")
    else:
        # Local Windows (assuming we are running from project root or analysis folder)
        # Try to find the root dynamically
        current_path = Path(os.getcwd())
        if (current_path / "prisma_proto.md").exists():
            PROJECT_PATH = str(current_path)
        elif (current_path.parent / "prisma_proto.md").exists(): # analysis/
            PROJECT_PATH = str(current_path.parent)
        elif (current_path.parent.parent / "prisma_proto.md").exists(): # analysis/nb
            PROJECT_PATH = str(current_path.parent.parent)
        else:
            # Fallback to hardcoded local if detection fails
            PROJECT_PATH = r"G:\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST"
        print(f"Environment: Local Windows ({PROJECT_PATH})")

    PDF_DIR = os.path.join(PROJECT_PATH, "data/ret_docs")
    MARKDOWN_DIR = os.path.join(PROJECT_PATH, "data/proc_markdowns")
    OUTPUT_DIR = os.path.join(PROJECT_PATH, "data/ext_res_v3")
    CHECKPOINT_FILE = os.path.join(OUTPUT_DIR, "checkpoint.json")
    
    # Processing
    VISUAL_BATCH_SIZE = 4  # Images per batch for GPU
    LLM_CONCURRENCY = 2    # Parallel LLM calls (Groq free tier)
    MAX_CONTEXT_CHARS = 85000  # LLM context limit
    
    # Models
    LLM_MODEL = "llama-3.3-70b-versatile"
    LLM_TEMPERATURE = 0.05
    
    @classmethod
    def init_dirs(cls):
        os.makedirs(cls.MARKDOWN_DIR, exist_ok=True)
        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)

# =============================================================================
# CHECKPOINT MANAGER - Resume support
# =============================================================================
class CheckpointManager:
    def __init__(self, checkpoint_path: str):
        self.path = checkpoint_path
        self.data = self._load()
    
    def _load(self) -> dict:
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                return json.load(f)
        return {"processed": {}, "errors": [], "last_run": None}
    
    def save(self):
        self.data["last_run"] = datetime.now().isoformat()
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def get_pdf_hash(self, pdf_path: str) -> str:
        """Get MD5 hash of PDF file for change detection."""
        with open(pdf_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    
    def needs_processing(self, paper_id: str, pdf_path: str) -> bool:
        """Check if PDF needs processing (new or changed)."""
        current_hash = self.get_pdf_hash(pdf_path)
        if paper_id not in self.data["processed"]:
            return True
        return self.data["processed"][paper_id].get("pdf_hash") != current_hash
    
    def mark_complete(self, paper_id: str, pdf_hash: str, phase: str):
        if paper_id not in self.data["processed"]:
            self.data["processed"][paper_id] = {}
        self.data["processed"][paper_id][f"{phase}_done"] = True
        self.data["processed"][paper_id]["pdf_hash"] = pdf_hash
        self.data["processed"][paper_id]["timestamp"] = datetime.now().isoformat()
        self.save()
    
    def add_error(self, paper_id: str, phase: str, error: str):
        self.data["errors"].append({
            "paper_id": paper_id, "phase": phase, 
            "error": error, "time": datetime.now().isoformat()
        })
        self.save()

# =============================================================================
# PHASE 1: PDF TO MARKDOWN (Marker)
# =============================================================================
def phase1_marker_conversion(checkpoint: CheckpointManager, force_all: bool = False):
    """Convert PDFs to Markdown using Marker library."""
    print("\n" + "="*60)
    print("📄 PHASE 1: PDF → MARKDOWN (Marker)")
    print("="*60)
    
    pdf_files = sorted(glob.glob(os.path.join(Config.PDF_DIR, "*.pdf")))
    print(f"Found {len(pdf_files)} PDFs")
    
    to_process = []
    for pdf_path in pdf_files:
        paper_id = Path(pdf_path).stem
        if force_all or checkpoint.needs_processing(paper_id, pdf_path):
            to_process.append((paper_id, pdf_path))
        else:
            print(f"   ⏩ {paper_id} - already processed, skipping")
    
    print(f"\n📋 PDFs to convert: {len(to_process)}")
    
    for i, (paper_id, pdf_path) in enumerate(to_process):
        print(f"\n[{i+1}/{len(to_process)}] 🔨 Processing: {paper_id}")
        output_folder = os.path.join(Config.MARKDOWN_DIR, paper_id)
        
        try:
            # Force CUDA device for marker
            env = os.environ.copy()
            env["TORCH_DEVICE"] = "cuda" if torch.cuda.is_available() else "cpu"
            
            cmd = [
                "marker_single", pdf_path,
                "--output_dir", output_folder,
                "--paginate_output"
            ]
            result = subprocess.run(cmd, env=env, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                pdf_hash = checkpoint.get_pdf_hash(pdf_path)
                checkpoint.mark_complete(paper_id, pdf_hash, "marker")
                print(f"   ✅ Done")
            else:
                raise Exception(result.stderr[:500])
                
        except Exception as e:
            print(f"   ❌ Error: {str(e)[:100]}")
            checkpoint.add_error(paper_id, "marker", str(e))
    
    print("\n✅ Phase 1 Complete")

# =============================================================================
# PHASE 2: VISUAL ANALYSIS (BLIP + DePlot) - Batched
# =============================================================================
# =============================================================================
# PHASE 2: VISUAL ANALYSIS (BLIP + DePlot) - Batched
# =============================================================================
def analyze_with_backup_model(images, prompt_list):
    """
    Backup analysis using Nvidia Nemotron (via OpenRouter/OpenAI-compatible API)
    when Gemini hits rate limits.
    """
    try:
        from openai import OpenAI
        from google.colab import userdata
        import base64
        import io
        
        # Get Backup Key
        # User specified the key name is the model name
        key_names = ['nvidia/nemotron-nano-12b-v2-vl:free', 'OPENROUTER_API_KEY', 'NVIDIA_API_KEY']
        api_key = None
        
        for name in key_names:
            try:
                api_key = userdata.get(name)
                if api_key:
                    break
            except:
                pass
            
            if not api_key:
                api_key = os.getenv(name)
                if api_key:
                    break
            
        if not api_key:
            print(f"     ⚠️ Backup API Key (tried: {key_names}) not found. Cannot switch to backup.")
            return None

        # Init Client
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
            timeout=30.0, # Add timeout to prevent hanging
            max_retries=1 
        )
        
        print("     🔄 Switching to Backup Model: nvidia/nemotron-nano-12b-v2-vl:free")
        
        # Prepare content for OpenAI Vision format
        content_parts = []
        
        # Add text prompt
        text_prompt = (
            "You are an expert scientific image analyst. Analyze these images for a systematic review.\n"
            "For EACH image, provide a structured analysis following this EXACT format:\n\n"
            "Image [FILENAME]:\n"
            "- Type: (Chart / Diagram / Setup / Other)\n"
            "- Description: (Brief explanation of visual content)\n"
            "- KEY DATA: (If chart, extract numerical values/trends. If diagram, explain relationships.)\n"
            "--------------------------------------------------\n"
        )
        content_parts.append({"type": "text", "text": text_prompt})
        
        # Add images
        for img_path in images:
            try:
                # Open and resize if needed (though API might handle it, safer to keep manageable)
                img = Image.open(img_path)
                
                # OPTIMIZATION: Resize large images to max 1024px to prevent timeouts/context overflow
                max_dim = 1024
                if img.width > max_dim or img.height > max_dim:
                    img.thumbnail((max_dim, max_dim))
                
                # Convert to RGB if needed
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                    
                # Encode to base64
                buffered = io.BytesIO()
                img.save(buffered, format="JPEG", quality=85) # Compress slightly
                img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
                
                content_parts.append({
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{img_str}"
                    }
                })
                # Add specific instruction per image as text is tricky in batched vision, 
                # but we added global instruction. Let's add filename as context if possible for the model to map
                content_parts.append({
                    "type": "text", 
                    "text": f"\n[Context] Above is Image: {os.path.basename(img_path)}"
                })
                
            except Exception as e:
                print(f"     ⚠️ Error preparing image for backup: {e}")
                continue

        response = client.chat.completions.create(
            model="nvidia/nemotron-nano-12b-v2-vl:free",
            messages=[
                {
                    "role": "user",
                    "content": content_parts
                }
            ]
        )
        
        content = response.choices[0].message.content
        if content:
             print(f"     📝 Nvidia Output Preview: {content[:100].replace(chr(10), ' ')}...")
        return content

    except Exception as e:
        print(f"     ❌ Backup Model Check Failed: {e}")
        return None

# =============================================================================
# LOCAL VISION MODEL (Florence-2)
# =============================================================================
class LocalVisionModel:
    def __init__(self, model_id="microsoft/Florence-2-large"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_id = model_id
        self.model = None
        self.processor = None
        
        if self.device == "cuda":
            print(f"     🚀 Loading Local Vision Model ({model_id}) on {self.device}...")
            try:
                self.model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True).to(self.device).eval()
                self.processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
                print("     ✅ Local Model Loaded Successfully!")
            except Exception as e:
                print(f"     ❌ Failed to load local model: {e}")
                self.model = None
        else:
            print("     ⚠️ No GPU found. Skipping Local Vision Model load.")

    def analyze_image(self, image_path: str) -> str:
        if not self.model:
            return None
            
        try:
            image = Image.open(image_path)
            if image.mode != "RGB":
                image = image.convert("RGB")
                
            task_prompt = "<MORE_DETAILED_CAPTION>"
            inputs = self.processor(text=task_prompt, images=image, return_tensors="pt").to(self.device, torch.float16)

            generated_ids = self.model.generate(
                input_ids=inputs["input_ids"],
                pixel_values=inputs["pixel_values"],
                max_new_tokens=1024,
                early_stopping=False,
                do_sample=False,
                num_beams=3,
            )
            generated_text = self.processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
            parsed_answer = self.processor.post_process_generation(
                generated_text, 
                task=task_prompt, 
                image_size=(image.width, image.height)
            )
            
            description = parsed_answer.get(task_prompt, "")
            
            # Identify type based on description keywords
            img_type = "Chart/Diagram" # Default
            lower_desc = description.lower()
            if "chart" in lower_desc or "graph" in lower_desc or "plot" in lower_desc:
                img_type = "Chart"
            elif "diagram" in lower_desc or "setup" in lower_desc or "schematic" in lower_desc:
                img_type = "Diagram"
                
            return (
                f"Image {os.path.basename(image_path)}:\n"
                f"- Type: {img_type} (Detected by Local Model)\n"
                f"- Description: {description}\n"
                f"--------------------------------------------------"
            )

        except Exception as e:
            print(f"     ⚠️ Local Analysis Error: {e}")
            return None

def phase2_visual_analysis(checkpoint: CheckpointManager):
    """Analyze images using Local GPU (Florence-2) with Gemini/Backup Fallback."""
    print("\n" + "="*60)
    print("👁️ PHASE 2: VISUAL ANALYSIS (Local GPU + Gemini Fallback) - Deep Traversal Mode")
    print("="*60)
    
    # Init Local Model
    local_model = LocalVisionModel()
    
    # Imports
    try:
        import google.generativeai as genai
        from google.colab import userdata
    except ImportError:
        import google.generativeai as genai
        userdata = None # Fallback for local

    # --- API KEY MANAGEMENT ---
    def get_key(name):
        k = None
        if userdata:
            try:
                k = userdata.get(name)
            except:
                pass
        if not k:
            k = os.getenv(name)
        return k

    primary_key = get_key('GOOGLE_API_KEY')
    secondary_key = get_key('gapi2')
    
    # State tracking for active key
    # 0: Primary (GOOGLE_API_KEY)
    # 1: Secondary (gapi2)
    # 2: Backup (Nvidia) - this is handled by fallback function, not genai
    current_key_state = 0 
    
    if primary_key:
        print("   🔑 Using Primary Key: GOOGLE_API_KEY")
        genai.configure(api_key=primary_key)
    elif secondary_key:
        print("   🔑 Primary Key not found. Switching to Secondary: gapi2")
        genai.configure(api_key=secondary_key)
        current_key_state = 1
    else:
        print("   ⚠️ No Gemini Keys found (GOOGLE_API_KEY or gapi2). Will rely entirely on Backup Model.")
        current_key_state = 2 # Start directly with backup

    # Model definition
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # Config
    BATCH_SIZE = 5 
    RATE_LIMIT_DELAY = 15.0 

    # Find papers
    paper_folders_root = sorted(glob.glob(os.path.join(Config.MARKDOWN_DIR, "*")))
    # Filter to only directories
    paper_folders_root = [f for f in paper_folders_root if os.path.isdir(f)]
    
    print(f"Papers found for discovery: {len(paper_folders_root)}")
    
    import time
    
    for i, folder_path in enumerate(paper_folders_root):
        paper_id = os.path.basename(folder_path)
        
        # --- PATH NORMALIZATION (Nested Check) ---
        # Rule: Check if [Root]/[Paper_ID]/[Paper_ID]/ exists.
        nested_folder = os.path.join(folder_path, paper_id)
        if os.path.isdir(nested_folder):
            working_dir = nested_folder
            print(f"   📂 Nested Structure detected for {paper_id}. Working Dir: .../{paper_id}/{paper_id}/")
        else:
            working_dir = folder_path
            
        # --- CHECKPOINT VERIFICATION ---
        output_file = os.path.join(working_dir, "visual_analysis.txt")
        if os.path.exists(output_file):
             # Check if it has valid content (not empty or just "No valid images found" if we want to re-try, but strict rule says skip)
             # User rule: "IF Found: Skip this paper entirely"
             print(f"   ⏩ {paper_id} - visually analyzed (checkpoint found), skipping")
             continue
        
        print(f"[{i+1}/{len(paper_folders_root)}] 👁️ Analyzing: {paper_id}")
        
        # --- IMAGE COLLECTION (Recursive) ---
        # "Scan Working Directory and ALL subdirectories recursively."
        images = []
        for root, dirs, files in os.walk(working_dir):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    images.append(os.path.join(root, file))
        
        images = sorted(images) # Sort for consistency
        
        # --- FILTERING (Quality Control) ---
        valid_images = []
        for img_path in images:
            try:
                img = Image.open(img_path)
                # Rule: Discard if Width < 150px OR Height < 150px
                if img.width >= 150 and img.height >= 150:
                    valid_images.append(img_path)
                else:
                    # Optional: print skipped images? Nah, too verbose.
                    pass
            except:
                continue
                
        if not valid_images:
            print(f"     ⚠️ No valid images found after filtering (Total raw: {len(images)})")
            with open(output_file, 'w') as f:
                f.write("No valid images found.")
            continue
            
        # --- BATCHING ---
        batches = [valid_images[j:j + BATCH_SIZE] for j in range(0, len(valid_images), BATCH_SIZE)]
        results = []
        print(f"     Found {len(valid_images)} images -> {len(batches)} batches")
        
        # Process Batches
        for batch_idx, batch_paths in enumerate(batches):
            
            # Prepare Inputs (Common to Gemini)
            inputs = ["Analyze these scientific images for a systematic review. For EACH image, strictly follow this format:\nImage [FILENAME]: [Your Analysis]\n"]
            try:
                batch_imgs_objs = []
                for p in batch_paths:
                    img = Image.open(p)
                    name = os.path.basename(p)
                    inputs.append(f"Image [{name}]: Identify if Chart/Diagram/Setup. If Chart, extract data. If Diagram, explain.")
                    inputs.append(img)
                    batch_imgs_objs.append(img)
            except Exception as e:
                print(f"     ⚠️ Error loading images for batch: {e}")
                continue

            # Retry Loop for Strategies
            batch_success = False
            
            # Create a loop that allows trying strategies in order for THIS batch
            # We start with the globally active current_key_state
            
            # Strategies to try for this batch
            # Strategy -1: Local Model (Priority if available)
            # Strategy 0: Primary Gemini
            # Strategy 1: Secondary Gemini
            # Strategy 2: Backup Model (Nvidia)
            
            temp_strategies = []
            if local_model.model:
                temp_strategies.append(-1)
            
            if current_key_state == 0:
                temp_strategies.extend([0, 1, 2])
            elif current_key_state == 1:
                temp_strategies.extend([1, 2])
            else:
                temp_strategies.append(2)
                
            for strategy_idx in temp_strategies:
                if batch_success: break
                
                try:
                    # Strategy -1: Local GPU Model
                    if strategy_idx == -1:
                        local_results = []
                        for p in batch_paths:
                            analysis = local_model.analyze_image(p)
                            if analysis:
                                local_results.append(analysis)
                            else:
                                raise Exception("Local Analysis Failed")
                        
                        results.append("\n".join(local_results))
                        batch_success = True
                        print(f"     ✅ Batch {batch_idx+1}/{len(batches)} processed (Local GPU Model)")
                        
                    # Strategy 0: Primary Gemini
                    elif strategy_idx == 0:
                        # Ensure Primary Key is set
                        response = model.generate_content(inputs)
                        results.append(response.text.strip())
                        batch_success = True
                        print(f"     ✅ Batch {batch_idx+1}/{len(batches)} processed (Primary Gemini)")
                        time.sleep(RATE_LIMIT_DELAY)

                    # Strategy 1: Secondary Gemini
                    elif strategy_idx == 1:
                        if not secondary_key:
                            print("     ℹ️ No secondary key (gapi2) available to switch to.")
                            continue # Skip to next strategy (Backup)

                        # Switch Global State if we were at 0
                        if current_key_state == 0:
                            print("     ⏳ Primary Key Rate Limit! Switching to Secondary Key (gapi2)...")
                            genai.configure(api_key=secondary_key)
                            current_key_state = 1 # Permanently switch for future lines
                        
                        # Try request
                        response = model.generate_content(inputs)
                        results.append(response.text.strip())
                        batch_success = True
                        print(f"     ✅ Batch {batch_idx+1}/{len(batches)} processed (Secondary Gemini)")
                        print(f"     💤 Cooling down for {RATE_LIMIT_DELAY}s...")
                        time.sleep(RATE_LIMIT_DELAY)

                    # Strategy 2: Backup Model (Nvidia)
                    elif strategy_idx == 2:
                        print("     ⏳ Gemini Rate Limit! Switching to Backup (Nvidia)...")
                        
                        # If we are here because Gemini failed, and we have a secondary key,
                        # it means even the secondary key failed (or we are skipping it).
                        # Let's make this fallback STICKY if we were using Gemini before.
                        if current_key_state < 2:
                             print("     ⚠️ Gemini API Limit Reached consistently. Switching to Backup Mode PERMANENTLY for this run.")
                             current_key_state = 2

                        backup_res = analyze_with_backup_model(batch_paths, inputs)
                        if backup_res:
                            results.append(backup_res)
                            batch_success = True
                            print(f"     ✅ Batch {batch_idx+1}/{len(batches)} processed (Backup Model)")
                            
                            # Shorter delay for backup model
                            BACKUP_DELAY = 5.0
                            print(f"     💤 Cooling down for {BACKUP_DELAY}s...")
                            time.sleep(BACKUP_DELAY)
                        else:
                            print("     ❌ Backup Model also failed.")
                
                except Exception as e:
                    err_str = str(e)
                    if "429" in err_str:
                        # Rate limit hit - loop will naturally try next strategy defined in temp_strategies
                        continue 
                    else:
                        print(f"     ❌ Error in batch (Strategy {strategy_idx}): {err_str}")
                        # If Backup failed with non-429, we might want to continue or break? 
                        # Continue to retry logic just in case
                        continue

            if not batch_success:
                 print("     ❌ All strategies failed for this batch. Waiting 60s and skipping...")
                 time.sleep(60)

        # Save results
        with open(output_file, 'w', encoding='utf-8') as f:
            final_output = "\n\n=== NEW BATCH ANALYSIS ===\n\n".join(results) if results else "Analysis failed."
            f.write(final_output)
        
        print(f"   ✅ Processed. Saved to visual_analysis.txt")
    
    print("\n✅ Phase 2 Complete")

# =============================================================================
# PHASE 3: LLM EXTRACTION (Groq API)
# =============================================================================
# =============================================================================
# PHASE 3: LLM EXTRACTION (Groq API)
# =============================================================================
SYSTEM_PROMPT = """You are a Senior Technical Editor and Optical Systems Engineer specializing in O-ISAC (Optical Integrated Sensing and Communication). Your task is to perform a Deep Extraction & Verification of a scientific paper.

Inputs:
1. Full Text: Markdown content of the paper.
2. Visual Context: Descriptions of charts/diagrams.

Execution Protocol (Must Follow Step-by-Step):

STEP 1: VISUAL INSPECTION (Grounding)
- Review the "Visual Context" provided.
- Verify what the diagrams prove. Does the "System Setup" diagram show a Fiber link or FSO? Does the "BER Graph" show performance below the threshold?
- Output: Briefly state the physical reality grounded in the images.

STEP 2: CONCEPT ANALYSIS (Classification)
- Classify the fundamental architecture.
- Decision Tree:
  - Is it Fiber, Wireless (FSO/VLC), or Hybrid?
  - Is the Sensing Active (Radar/Lidar) or Passive (DAS)?
  - Is the Integration method Spectral (OFDM), Time (TDM), or Hardware sharing?

STEP 3: BENCHMARK VERIFICATION (Sanity Check)
- Extract key metrics (Data Rate, Sensing Range, Resolution).
- Constraint Check: Do these numbers make physical sense? (e.g., A resolution of 1mm over 100km fiber is suspicious—flag it or verify it against the Abstract).
- Logic: Compare "Claims" in the Abstract vs. "Evidence" in the Results/Table section.

STEP 4: STRATEGIC CRITIQUE (Gap Analysis)
- Identify what is MISSING or WEAK.
- Focus: Did they simulate or experiment? Did they compare with baselines? Is the code available?

STEP 5: JSON SYNTHESIS (Final Output)
Populate the Target Schema with the extracted, verified data.
- Rule 1: JSON must be strictly valid.
- Rule 2: Use "NR" for missing data, do not hallucinate.
- Rule 3: Keep the reasoning steps internal (or in a separate trace field if prompted, but here produce CLEAN JSON).

Target Schema:
{
  "Paper_ID": "O_ISAC_XXX",
  "Study_Level": {
    "title": "string",
    "authors": "string",
    "year": int,
    "venue": "string",
    "doi": "string or NR",
    "document_type": "journal|conference|letter|review",
    "oisac_medium_class": "cabled_fibre|wireless_fso|wireless_vlc|wireless_lidar_like|wireless_retroreflective|hybrid",
    "carrier_band": "visible|NIR|SWIR|C-band|L-band|O-band|other|NR",
    "operational_environment": "indoor|outdoor|lab|field_trial|mixed|NR",
    "link_topology": "monostatic|bistatic|multistatic|distributed_fibre|point_to_point|NR",
    "mobility_context": "static|quasi_static|mobile|not_specified",
    "application_domain": ["vehicular", "industrial_manufacturing", "indoor_positioning", "environmental_monitoring", "critical_infrastructure", "fibre_network_monitoring", "robotics_autonomy", "aerospace_space", "uav_aerial", "maritime_underwater", "security_surveillance", "6g_networks", "other"],
    "scenario_description": "free-text description of use case",
    "evidence_type": ["analytical", "simulation", "experimental", "hybrid"],
    "validation_baselines_present": bool,
    "reproducibility_artifacts": "code_available|data_available|parameters_sufficient|insufficient|NR",
    "ris_present": bool,
    "opa_present": bool,
    "machine_learning_used": bool,
    "key_contribution": "summary",
    "gap_addressed": "summary",
    "performance_enablers": ["photonic_dechirping", "electronic_dechirping", "matched_filtering", "fft_based_processing", "compressed_sensing", "coherent_homodyne", "coherent_heterodyne", "direct_detection", "self_coherent", "balanced_detection", "tfln_modulator", "high_bandwidth_modulator", "frequency_comb", "photonic_adc", "integrated_photonics", "joint_waveform_design", "superimposed_waveform", "orthogonal_waveform", "dual_function_waveform", "frequency_jitter_mitigation", "false_target_suppression", "phase_noise_compensation", "nonlinearity_compensation", "wavelength_reuse", "shared_fiber_bidirectional", "distributed_architecture", "monostatic_full_duplex", "other"],
    "novel_component": "string",
    "novel_component_specs": "string"
  },
  "Experiments": [
    {
      "experiment_id": "E1",
      "scenario_label": "string",
      "Transmitter": {
        "tx_source_type": "laser|led|vcsel|frequency_comb|sld|other",
        "tx_modulation_type": "im_dd|coherent|mixed|not_specified",
        "tx_external_modulator": "mzm|eam|iq_modulator|none|other|NR",
        "wavelength_nm": float,
        "optical_bandwidth_ghz": float,
        "tx_power_dbm": float,
        "aperture_diameter_m": float,
        "beam_divergence_mrad": float
      },
      "Receiver": {
        "rx_detection_type": "direct|coherent|self_coherent|imaging|spad|other",
        "rx_detector": "pin_pd|apd_pd|balanced_pd|camera_cmos|camera_ccd|spad_array|other|NR",
        "rx_aperture_diameter_m": float,
        "rx_photonic_processing": "none|photonic_dechirping|photonic_downconversion|photonic_mixing|envelope_detection|other|NR",
        "rx_modulator_type": "none|tfln_mzm|ln_mzm|iq_modulator|phase_modulator|eam|other|NR",
        "rx_modulator_bandwidth_ghz": float,
        "rx_modulator_operating_point": "mitp|matp|qbp|other|not_specified|NR",
        "false_target_mitigation": "none|mitp_bias|balanced_detection|signal_processing|waveform_design|other|NR"
      },
      "Integration": {
        "hardware_sharing_mode": "shared_frontend|partially_shared|separate_frontends|not_specified",
        "duplexing_mode": "full_duplex|half_duplex|tdm|fdm|wdm|cdm|sdm|other|NR"
      },
      "Waveform": {
        "comm_waveform_family": "ook|pam|pam4|ofdm|dmt|ppm|qam|psk|dpsk|chirp_fmcw|pulse_train|cap|other",
        "comm_modulation_order": int,
        "comm_symbol_rate_gbaud": float,
        "comm_fec_type": "string or NR",
        "sensing_waveform_family": "pulse_tof|fmcw_chirp|lfm_chirp|ofdm_sensing|backscatter_probe|phase_coded|reflectometry|same_as_comm|other",
        "isac_waveform_relationship": "single_dual_function|comm_embedded_in_sensing|sensing_embedded_in_comm|multiplexed_separate|superimposed|not_specified",
        "resource_partition": "string or NR"
      },
      "Channel_Fiber": {
        "fibre_length_km": float,
        "fibre_type": "smf|mmf|fmf|mcf|dcf|other|NR",
        "attenuation_db_per_km": float,
        "dispersion_ps_per_nm_km": float,
        "nonlinearity_model": "gn_model|nlse|kerr_only|ignored|other|NR",
        "backscatter_sensing_type": "rayleigh_phi_otdr|das|brillouin_botda|brillouin_botdr|raman|fbg|other|NR"
      },
      "Channel_Wireless": {
        "link_distance_m": float,
        "path_loss_model": "string or NR",
        "turbulence_model": "lognormal|gamma_gamma|malaga|negative_exponential|rice_nakagami|none|other|NR",
        "turbulence_Cn2": float,
        "scintillation_index": float,
        "pointing_error_model": "zero|gaussian_jitter|beckmann|rayleigh|other|NR",
        "weather_visibility_m": float,
        "ambient_light_model": "string or NR"
      },
      "Comm_Metrics": {
        "data_rate_gbps": float,
        "spectral_efficiency_bps_hz": float,
        "ber": float,
        "ber_target": float,
        "snr_db": float,
        "osnr_db": float,
        "outage_probability": float,
        "latency_ms": float,
        "capacity_bps_hz": float
      },
      "Sensing_Metrics": {
        "sensing_task_type": ["ranging", "localization_2d", "localization_3d", "velocity", "imaging", "vibration", "displacement", "strain", "temperature", "target_detection", "obstacle_detection", "turbulence_estimation", "channel_sensing", "other"],
        "sensing_range_m": float,
        "range_resolution_m": float,
        "range_accuracy_m": float,
        "angular_resolution_deg": float,
        "velocity_resolution_mps": float,
        "velocity_accuracy_mps": float,
        "localization_error_m": float,
        "spatial_resolution_m": float,
        "sensing_bandwidth_hz": float,
        "pd_probability_detection": float,
        "pfa_probability_false_alarm": float,
        "crb_crlb_value": float,
        "crb_parameter": "range|angle|delay|doppler|position|velocity|other|NR"
      },
      "Tradeoff": {
        "coupling_mode": "resource_division|joint_waveform|joint_receiver_processing|shared_hardware_only|other|NR",
        "tradeoff_type": ["rate_vs_rmse", "rate_vs_range_resolution", "rate_vs_sensing_range", "ber_vs_detection_prob", "throughput_vs_localization", "power_split", "time_split", "bandwidth_split", "pareto_multi_objective", "other"],
        "tradeoff_representation": "single_point|curve|pareto_front|table|not_explicit",
        "tradeoff_control_parameter": "string or NR",
        "tradeoff_control_range": "string or NR"
      },
      "Enabling_Tech": {
        "opa_num_emitters": int,
        "opa_steering_range_deg": float,
        "opa_beamwidth_deg": float,
        "ris_num_elements": int,
        "ris_type": "reflective|transmissive|hybrid|slm|other|NR",
        "ris_phase_bits": int
      },
      "Provenance": {
        "source_pointer": "string",
        "value_origin": "reported_text|reported_table|digitised_figure|computed|inferred",
        "confidence_reporting": "ci_reported|std_reported|none_reported",
        "num_trials": int
      }
    }
  ],
  "Quality_Assessment": {
    "tqaf_modelling_fidelity": "0|1|2",
    "tqaf_validation_strength": "0|1|2",
    "tqaf_experimental_validity": "0|1|2",
    "tqaf_metric_completeness": "0|1|2",
    "tqaf_reproducibility": "0|1|2",
    "both_sc_metrics_reported": bool,
    "tradeoff_explicitly_analyzed": bool,
    "uncertainty_reported": bool,
    "baseline_comparison_present": bool,
    "tqaf_notes": "string"
  }
}

CRITICAL: Return ONLY valid JSON.
"""

async def extract_single_paper(client, paper_id: str, folder: str, semaphore) -> Optional[dict]:
    """Extract data from single paper using LLM with CoT + Visual Context."""
    async with semaphore:
        print(f"   📐 Extracting: {paper_id}")
        
        # 1. READ MARKDOWN
        try:
            # Handle nested folder logic if it exists
            nested_folder = os.path.join(folder, paper_id)
            if os.path.isdir(nested_folder):
                working_dir = nested_folder
            else:
                working_dir = folder
                
            md_path = os.path.join(working_dir, f"{paper_id}.md")
            if not os.path.exists(md_path):
                 # Fallback to recursively finding ANY md file
                 md_files = glob.glob(os.path.join(working_dir, "*.md"))
                 if md_files:
                     md_path = md_files[0]
                 else:
                     print(f"   ❌ Markdown not found for {paper_id}")
                     return None
            
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # 2. READ VISUAL CONTEXT
            viz_path = os.path.join(working_dir, "visual_analysis.txt")
            visual_context = "No visual analysis available."
            if os.path.exists(viz_path):
                with open(viz_path, 'r', encoding='utf-8') as f:
                    visual_context = f.read()
            
        except Exception as e:
            print(f"   ❌ Error reading files for {paper_id}: {e}")
            return None

        # 3. PREPARE PROMPT
        prompt = (
            f"Paper ID: {paper_id}\n\n"
            f"=== VISUAL CONTEXT ===\n{visual_context}\n\n"
            f"=== FULL TEXT ===\n{content[:Config.MAX_CONTEXT_CHARS]}" # Truncate if needed
        )
        
        # 4. CALL LLM
        try:
            # Using Groq (OpenAI-compatible)
            chat_completion = await client.chat.completions.create(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                model=Config.LLM_MODEL,
                temperature=Config.LLM_TEMPERATURE,
                stream=False
            )
            
            response_text = chat_completion.choices[0].message.content
            
            # 5. PARSE JSON
            # Find JSON block
            import re
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
                data = json.loads(json_str)
                data["Paper_ID"] = paper_id # Ensure ID matches
                return data
            else:
                print(f"   ⚠️ No JSON found in response for {paper_id}")
                return None
                
        except Exception as e:
            print(f"   ❌ LLM Error for {paper_id}: {e}")
            return None

        # Read markdown
        md_files = glob.glob(os.path.join(folder, "**", "*.md"), recursive=True)
        if not md_files:
            return {"Paper_ID": paper_id, "error": "No markdown found"}
        
        with open(md_files[0], 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Read visual analysis
        vis_file = os.path.join(folder, "visual_analysis.txt")
        visuals = ""
        if os.path.exists(vis_file):
            with open(vis_file, 'r', encoding='utf-8') as f:
                visuals = f.read()
        
        user_content = f"""=== PAPER: {paper_id} ===

=== VISUAL DATA ===
{visuals[:5000] if visuals else "None"}

=== PAPER TEXT ===
{text[:Config.MAX_CONTEXT_CHARS]}"""

        try:
            response = await client.chat.completions.create(
                model=Config.LLM_MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_content}
                ],
                response_format={"type": "json_object"},
                temperature=Config.LLM_TEMPERATURE,
                max_tokens=16000
            )
            
            result = json.loads(response.choices[0].message.content)
            result["Paper_ID"] = paper_id
            result["extraction_timestamp"] = datetime.now().isoformat()
            result["schema_version"] = "3.0"
            return result
            
        except Exception as e:
            return {"Paper_ID": paper_id, "error": str(e)}

async def phase3_llm_extraction(checkpoint: CheckpointManager, limit: int = None):
    """Run LLM extraction on all papers."""
    print("\n" + "="*60)
    print("🧠 PHASE 3: LLM EXTRACTION (Groq)")
    print("="*60)
    
    try:
        from google.colab import userdata
        api_key = userdata.get('GROQ_API_KEY')
    except:
        api_key = os.getenv('GROQ_API_KEY')
    
    if not api_key:
        print("❌ GROQ_API_KEY not found!")
        return []
    
    from openai import AsyncOpenAI
    client = AsyncOpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")
    
    # Find papers to process
    folders = sorted(glob.glob(os.path.join(Config.MARKDOWN_DIR, "*")))
    if limit:
        folders = folders[:limit]
    
    print(f"Papers to extract: {len(folders)}")
    
    semaphore = asyncio.Semaphore(Config.LLM_CONCURRENCY)
    
    tasks = []
    for folder in folders:
        paper_id = os.path.basename(folder)
        tasks.append(extract_single_paper(client, paper_id, folder, semaphore))
    
    results = await asyncio.gather(*tasks)
    
    # Filter and save
    success = [r for r in results if r and "error" not in r]
    errors = [r for r in results if r and "error" in r]
    
    print(f"\n✅ Success: {len(success)}")
    print(f"❌ Errors: {len(errors)}")
    
    if success:
        # Save JSON
        json_path = os.path.join(Config.OUTPUT_DIR, "extraction_v3.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(success, f, indent=2)
        print(f"\n📁 Saved: {json_path}")
        
        # Flatten to CSV with enhanced columns
        rows = []
        for paper in success:
            sl = paper.get("Study_Level", {})
            qa = paper.get("Quality_Assessment", {})
            for exp in paper.get("Experiments", []):
                tx = exp.get("Transmitter", {})
                rx = exp.get("Receiver", {})
                wf = exp.get("Waveform", {})
                ch_w = exp.get("Channel_Wireless", {})
                ch_f = exp.get("Channel_Fiber", {})
                cm = exp.get("Comm_Metrics", {})
                sm = exp.get("Sensing_Metrics", {})
                tr = exp.get("Tradeoff", {})
                pr = exp.get("Provenance", {})
                
                rows.append({
                    # Study Level
                    "Paper_ID": paper.get("Paper_ID"),
                    "Title": sl.get("title"),
                    "Year": sl.get("year"),
                    "Venue": sl.get("venue"),
                    "Medium_Class": sl.get("oisac_medium_class"),
                    "Carrier_Band": sl.get("carrier_band"),
                    "Environment": sl.get("operational_environment"),
                    "Topology": sl.get("link_topology"),
                    "Evidence_Type": ", ".join(sl.get("evidence_type", [])) if isinstance(sl.get("evidence_type"), list) else sl.get("evidence_type"),
                    "RIS": sl.get("ris_present"),
                    "OPA": sl.get("opa_present"),
                    "ML_Used": sl.get("machine_learning_used"),
                    
                    # Experiment
                    "Exp_ID": exp.get("experiment_id"),
                    "Scenario": exp.get("scenario_label"),
                    
                    # Transmitter
                    "TX_Type": tx.get("tx_source_type"),
                    "TX_Mod_Type": tx.get("tx_modulation_type"),
                    "Wavelength_nm": tx.get("wavelength_nm"),
                    "TX_Power_dBm": tx.get("tx_power_dbm"),
                    
                    # Receiver
                    "RX_Detection": rx.get("rx_detection_type"),
                    "RX_Detector": rx.get("rx_detector"),
                    
                    # Waveform (CRITICAL)
                    "Comm_Waveform": wf.get("comm_waveform_family"),
                    "Sensing_Waveform": wf.get("sensing_waveform_family"),
                    "ISAC_Relationship": wf.get("isac_waveform_relationship"),
                    
                    # Channel
                    "Link_Distance_m": ch_w.get("link_distance_m"),
                    "Turbulence_Model": ch_w.get("turbulence_model"),
                    "Fiber_Length_km": ch_f.get("fibre_length_km"),
                    "Fiber_Type": ch_f.get("fibre_type"),
                    "Backscatter_Type": ch_f.get("backscatter_sensing_type"),
                    
                    # Comm Metrics
                    "Data_Rate_Gbps": cm.get("data_rate_gbps"),
                    "Spectral_Eff": cm.get("spectral_efficiency_bps_hz"),
                    "BER": cm.get("ber"),
                    "SNR_dB": cm.get("snr_db"),
                    
                    # Sensing Metrics
                    "Sensing_Task": ", ".join(sm.get("sensing_task_type", [])) if isinstance(sm.get("sensing_task_type"), list) else sm.get("sensing_task_type"),
                    "Range_Resolution_m": sm.get("range_resolution_m"),
                    "Range_Accuracy_m": sm.get("range_accuracy_m"),
                    "Sensing_Range_m": sm.get("sensing_range_m"),
                    "Velocity_Resolution_mps": sm.get("velocity_resolution_mps"),
                    "Localization_Error_m": sm.get("localization_error_m"),
                    
                    # Tradeoff
                    "Coupling_Mode": tr.get("coupling_mode"),
                    "Tradeoff_Type": ", ".join(tr.get("tradeoff_type", [])) if isinstance(tr.get("tradeoff_type"), list) else tr.get("tradeoff_type"),
                    "Tradeoff_Repr": tr.get("tradeoff_representation"),
                    
                    # Quality
                    "TQAF_Total": sum([int(qa.get(k, 0)) for k in ["tqaf_modelling_fidelity", "tqaf_validation_strength", "tqaf_metric_completeness", "tqaf_reproducibility"] if isinstance(qa.get(k), (int, str)) and str(qa.get(k)).isdigit()]),
                    "Both_SC_Metrics": qa.get("both_sc_metrics_reported"),
                    "Tradeoff_Analyzed": qa.get("tradeoff_explicitly_analyzed"),
                    
                    # Provenance
                    "Source": pr.get("source_pointer")
                })
        
        df = pd.DataFrame(rows)
        csv_path = os.path.join(Config.OUTPUT_DIR, "extraction_v3.csv")
        df.to_csv(csv_path, index=False)
        print(f"📊 Saved: {csv_path}")
        print(f"\n{df.head(10)}")
    
    return success

# =============================================================================
# MAIN RUNNER
# =============================================================================
def run_full_pipeline(skip_phase1=False, skip_phase2=False, limit=None, force_all=False):
    """Run the complete extraction pipeline."""
    print("\n" + "="*70)
    print("🚀 O-ISAC EXTRACTION PIPELINE v3.0")
    print("="*70)
    print(f"📅 Started: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    Config.init_dirs()
    checkpoint = CheckpointManager(Config.CHECKPOINT_FILE)
    
    if not skip_phase1:
        phase1_marker_conversion(checkpoint, force_all=force_all)
    
    if not skip_phase2:
        phase2_visual_analysis(checkpoint)
    
    # Phase 3 needs async
    import nest_asyncio
    nest_asyncio.apply()
    
    results = asyncio.get_event_loop().run_until_complete(
        phase3_llm_extraction(checkpoint, limit=limit)
    )
    
    print("\n" + "="*70)
    print(f"🎉 PIPELINE COMPLETE - {len(results)} papers extracted")
    print("="*70)
    
    return results
