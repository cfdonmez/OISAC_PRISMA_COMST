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
    # 🌍 Environment & Path Detection
    if os.path.exists("/content/drive"):
        # Google Colab
        PROJECT_PATH = "/content/drive/MyDrive/AKU_WorkSpace/survey_fdgit/OISAC_PRISMA_COMST"
        print("🌍 Environment: Google Colab")
    else:
        # Local Windows (assuming we are running from project root or analysis folder)
        # Try to find the root dynamically
        current_path = Path(os.getcwd())
        if (current_path / "prisma_protocol.md").exists():
            PROJECT_PATH = str(current_path)
        elif (current_path.parent / "prisma_protocol.md").exists(): # analysis/
            PROJECT_PATH = str(current_path.parent)
        elif (current_path.parent.parent / "prisma_protocol.md").exists(): # analysis/notebooks
            PROJECT_PATH = str(current_path.parent.parent)
        else:
            # Fallback to hardcoded local if detection fails
            PROJECT_PATH = r"G:\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST"
        print(f"🌍 Environment: Local Windows ({PROJECT_PATH})")

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
    
    # Find papers with processed markdowns
    paper_folders = sorted(glob.glob(os.path.join(Config.MARKDOWN_DIR, "*")))
    print(f"Papers to analyze: {len(paper_folders)}")
    
    for i, folder in enumerate(paper_folders):
        paper_id = os.path.basename(folder)
        
        # Look for inner folder (marker creates nested folders)
        inner_folder = os.path.join(folder, paper_id)
        if os.path.exists(inner_folder):
            folder = inner_folder
        
        output_file = os.path.join(folder, "visual_analysis.txt")
        
        # Skip if already done
        if os.path.exists(output_file):
            print(f"   ⏩ {paper_id} - already analyzed, skipping")
            continue
        
        print(f"[{i+1}/{len(paper_folders)}] 👁️ Analyzing: {paper_id}")
        
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
SYSTEM_PROMPT = """You are a Senior Technical Editor for IEEE COMST extracting structured data from Optical Integrated Sensing and Communication (O-ISAC) papers for a PRISMA-2020 systematic review.

================================================================================
CRITICAL EXTRACTION RULES
================================================================================
1. Use "NR" (Not Reported) for missing values, "NA" (Not Applicable) for inapplicable fields
2. Create MULTIPLE Experiment entries if the paper reports different scenarios/configurations
3. Extract EXACT numerical values with units - convert to standard: wavelength→nm, distance→m (wireless)/km (fiber), rate→Gbps
4. Include evidence snippets with source pointers (e.g., "Table II", "Fig. 5", "Section IV-B")
5. The "isac_waveform_relationship" field is MOST CRITICAL for taxonomy - always determine it

================================================================================
OUTPUT JSON SCHEMA (Full v2.1 - Updated 2025-12-08)
================================================================================
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
    
    "key_contribution": "1-2 sentence summary of the paper's main technical contribution",
    "gap_addressed": "What gap/limitation does this work address?",
    "performance_enablers": ["photonic_dechirping", "electronic_dechirping", "matched_filtering", "fft_based_processing", "compressed_sensing", "coherent_homodyne", "coherent_heterodyne", "direct_detection", "self_coherent", "balanced_detection", "tfln_modulator", "high_bandwidth_modulator", "frequency_comb", "photonic_adc", "integrated_photonics", "joint_waveform_design", "superimposed_waveform", "orthogonal_waveform", "dual_function_waveform", "frequency_jitter_mitigation", "false_target_suppression", "phase_noise_compensation", "nonlinearity_compensation", "wavelength_reuse", "shared_fiber_bidirectional", "distributed_architecture", "monostatic_full_duplex", "other"],
    "novel_component": "Specific novel hardware/component if applicable (e.g., 'TFLN-MZM with 110 GHz bandwidth')",
    "novel_component_specs": "Key specifications of the novel component"
  },
  
  "Experiments": [
    {
      "experiment_id": "E1",
      "scenario_label": "Human-readable label (e.g., 'Outdoor FSO, 500m, Gamma-Gamma turbulence')",
      
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
        "resource_partition": "string describing split (e.g., 'α=0.7 power to comm') or NR"
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
        "tradeoff_control_parameter": "string (e.g., 'α', 'power_ratio') or NR",
        "tradeoff_control_range": "string (e.g., '[0.1, 0.9]') or NR"
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
        "source_pointer": "e.g., 'Table II, Section IV-B, Fig. 5'",
        "value_origin": "reported_text|reported_table|digitised_figure|computed|inferred",
        "confidence_reporting": "ci_reported|std_reported|none_reported",
        "num_trials": int
      }
    }
  ],
  
  "Quality_Assessment": {
    "tqaf_modelling_fidelity": "0|1|2 (0=low, 1=moderate, 2=high)",
    "tqaf_validation_strength": "0|1|2",
    "tqaf_experimental_validity": "0|1|2",
    "tqaf_metric_completeness": "0|1|2 (both S&C metrics reported?)",
    "tqaf_reproducibility": "0|1|2",
    "both_sc_metrics_reported": bool,
    "tradeoff_explicitly_analyzed": bool,
    "uncertainty_reported": bool,
    "baseline_comparison_present": bool,
    "tqaf_notes": "string"
  }
}

================================================================================
UNIT CONVERSION RULES
================================================================================
- Wavelength: always in nm (1.55 μm → 1550 nm)
- Data rate: always in Gbps (100 Mbps → 0.1 Gbps, 1 Tbps → 1000 Gbps)
- Distance: meters for wireless, km for fiber
- Power: dBm or dB as reported
- BER: scientific notation (e.g., 1e-9)

================================================================================
IMPORTANT NOTES
================================================================================
- For fiber-based O-ISAC: focus on Channel_Fiber, backscatter_sensing_type
- For wireless O-ISAC (FSO/VLC): focus on Channel_Wireless, turbulence_model
- The isac_waveform_relationship is CRITICAL for the taxonomy
- If paper does NOT report BOTH comm AND sensing metrics, set both_sc_metrics_reported=false
- Extract ALL experiments/scenarios reported in the paper as separate entries
"""

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
