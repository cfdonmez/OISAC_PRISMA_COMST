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

import torch
import pandas as pd
from PIL import Image

# =============================================================================
# CONFIGURATION
# =============================================================================
class Config:
    # Paths (Google Drive)
    PROJECT_PATH = "/content/drive/MyDrive/AKU_WorkSpace/survey_fdgit/OISAC_PRISMA_COMST"
    PDF_DIR = os.path.join(PROJECT_PATH, "data/retrieved_docs")
    MARKDOWN_DIR = os.path.join(PROJECT_PATH, "data/processed_markdowns")
    OUTPUT_DIR = os.path.join(PROJECT_PATH, "data/extraction_results_v3")
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
            cmd = [
                "marker_single", pdf_path,
                "--output_dir", output_folder,
                "--paginate_output"
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
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
def phase2_visual_analysis(checkpoint: CheckpointManager):
    """Analyze images with BLIP and DePlot models."""
    print("\n" + "="*60)
    print("👁️ PHASE 2: VISUAL ANALYSIS (BLIP + DePlot)")
    print("="*60)
    
    from transformers import (
        BlipProcessor, BlipForConditionalGeneration,
        Pix2StructProcessor, Pix2StructForConditionalGeneration
    )
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device.upper()}")
    
    # Load models
    print("Loading BLIP model...")
    blip_proc = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    blip_model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-large"
    ).to(device).eval()
    
    print("Loading DePlot model...")
    deplot_proc = Pix2StructProcessor.from_pretrained("google/deplot")
    deplot_model = Pix2StructForConditionalGeneration.from_pretrained(
        "google/deplot"
    ).to(device).eval()
    
    # Process each paper folder
    folders = sorted(glob.glob(os.path.join(Config.MARKDOWN_DIR, "*")))
    
    for folder in folders:
        paper_id = os.path.basename(folder)
        output_file = os.path.join(folder, "visual_analysis.txt")
        
        # Skip if already done
        if os.path.exists(output_file):
            continue
        
        print(f"\n🖼️ Analyzing: {paper_id}")
        
        # Find images
        images = []
        for ext in ['*.png', '*.jpg', '*.jpeg']:
            images.extend(glob.glob(os.path.join(folder, "**", ext), recursive=True))
        
        if not images:
            with open(output_file, 'w') as f:
                f.write("No images found.")
            continue
        
        results = []
        for img_path in sorted(images):
            try:
                img = Image.open(img_path).convert("RGB")
                if img.width < 100 or img.height < 100:
                    continue
                
                img_name = os.path.basename(img_path)
                
                # Check if chart
                with torch.no_grad():
                    inputs = blip_proc(img, "Is this a chart?", return_tensors="pt").to(device)
                    out = blip_model.generate(**inputs, max_new_tokens=10)
                    is_chart = "yes" in blip_proc.decode(out[0], skip_special_tokens=True).lower()
                
                if is_chart:
                    # DePlot for charts
                    with torch.no_grad():
                        d_in = deplot_proc(images=img, text="Generate data table:", return_tensors="pt").to(device)
                        d_out = deplot_model.generate(**d_in, max_new_tokens=400)
                        data = deplot_proc.decode(d_out[0], skip_special_tokens=True)
                    results.append(f"📊 [CHART - {img_name}]:\n{data}")
                else:
                    # BLIP for other images
                    with torch.no_grad():
                        b_in = blip_proc(img, return_tensors="pt").to(device)
                        b_out = blip_model.generate(**b_in, max_new_tokens=40)
                        desc = blip_proc.decode(b_out[0], skip_special_tokens=True)
                    results.append(f"📷 [IMAGE - {img_name}]: {desc}")
                    
            except Exception as e:
                continue
        
        # Save results
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("\n\n".join(results) if results else "No processable images.")
        
        print(f"   ✅ {len(results)} images analyzed")
    
    # Cleanup GPU
    del blip_model, deplot_model
    torch.cuda.empty_cache()
    gc.collect()
    
    print("\n✅ Phase 2 Complete")

# =============================================================================
# PHASE 3: LLM EXTRACTION (Groq API)
# =============================================================================
SYSTEM_PROMPT = """You are an IEEE COMST technical reviewer extracting structured data from O-ISAC papers.

CRITICAL RULES:
1. Use "NR" for Not Reported, "NA" for Not Applicable
2. Create MULTIPLE experiments if paper has different scenarios
3. Include evidence snippets for key values
4. Convert units: wavelength→nm, distance→m (wireless)/km (fiber), rate→Gbps

OUTPUT JSON:
{
  "Paper_ID": "O_ISAC_XXX",
  "Study_Level": {
    "title": "string",
    "year": int,
    "venue": "string",
    "document_type": "journal|conference|letter",
    "oisac_medium_class": "cabled_fibre|wireless_fso|wireless_vlc|wireless_lidar_like|hybrid",
    "carrier_band": "visible|NIR|C-band|L-band|other|NR",
    "application_domain": ["list"],
    "evidence_type": ["simulation|experimental|analytical"],
    "ris_present": bool,
    "opa_present": bool,
    "ml_used": bool,
    "key_contribution": "1-2 sentences",
    "gap_addressed": "1 sentence"
  },
  "Experiments": [{
    "Experiment_ID": "E1",
    "Scenario_Label": "descriptive",
    "Transmitter": {"tx_source_type": "laser|led|vcsel", "wavelength_nm": float, "tx_power_dbm": float},
    "Receiver": {"rx_detection_type": "direct|coherent", "rx_detector": "pin_pd|apd_pd|balanced_pd"},
    "Waveform": {
      "comm_waveform_family": "ook|ofdm|qam|pam|chirp_fmcw",
      "sensing_waveform_family": "fmcw_chirp|pulse_tof|same_as_comm",
      "isac_waveform_relationship": "single_dual_function|multiplexed_separate|sensing_embedded_in_comm"
    },
    "Channel": {"link_distance_m": float, "fibre_length_km": float},
    "Comm_Metrics": {"data_rate_gbps": float, "ber": float, "snr_db": float},
    "Sensing_Metrics": {
      "sensing_task_type": ["ranging|velocity|localization_2d"],
      "range_resolution_m": float,
      "sensing_range_m": float
    },
    "Tradeoff": {"coupling_mode": "joint_waveform|resource_division", "tradeoff_type": ["list"]},
    "Source_Pointer": "Section X, Table Y"
  }],
  "Quality_Flags": {"both_sc_metrics_reported": bool, "tradeoff_analyzed": bool}
}"""

async def extract_single_paper(client, paper_id: str, folder: str, semaphore) -> Optional[dict]:
    """Extract data from single paper using LLM."""
    async with semaphore:
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
                max_tokens=6000
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
        
        # Flatten to CSV
        rows = []
        for paper in success:
            sl = paper.get("Study_Level", {})
            for exp in paper.get("Experiments", []):
                rows.append({
                    "Paper_ID": paper.get("Paper_ID"),
                    "Title": sl.get("title"),
                    "Year": sl.get("year"),
                    "Medium": sl.get("oisac_medium_class"),
                    "Exp_ID": exp.get("Experiment_ID"),
                    "Scenario": exp.get("Scenario_Label"),
                    "Data_Rate_Gbps": exp.get("Comm_Metrics", {}).get("data_rate_gbps"),
                    "Range_Resolution_m": exp.get("Sensing_Metrics", {}).get("range_resolution_m"),
                    "ISAC_Relationship": exp.get("Waveform", {}).get("isac_waveform_relationship"),
                    "Coupling_Mode": exp.get("Tradeoff", {}).get("coupling_mode")
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
