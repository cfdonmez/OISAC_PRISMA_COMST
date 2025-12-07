# =============================================================================
# O-ISAC PRISMA Extraction Pipeline v2.0
# =============================================================================
# Enhanced extraction aligned with PRISMA Protocol Section 9
# Designed for Google Colab with Groq API (Llama-3.3-70b)
# Last Updated: 2025-12-07
# =============================================================================

import asyncio
import os
import glob
import json
import pandas as pd
from datetime import datetime

# For Colab
try:
    from google.colab import userdata
    IN_COLAB = True
except ImportError:
    IN_COLAB = False
    from dotenv import load_dotenv
    load_dotenv()

from openai import AsyncOpenAI

# =============================================================================
# 1. CONFIGURATION
# =============================================================================
PROJECT_PATH = "/content/drive/MyDrive/AKU_WorkSpace/survey_fdgit/OISAC_PRISMA_COMST"
INTERMEDIATE_DIR = os.path.join(PROJECT_PATH, "data/processed_markdowns")
FINAL_DIR = os.path.join(PROJECT_PATH, "data/extraction_results_v2")
os.makedirs(FINAL_DIR, exist_ok=True)

# API Connection
try:
    if IN_COLAB:
        api_key = userdata.get('GROQ_API_KEY')
    else:
        api_key = os.getenv('GROQ_API_KEY')
    
    if not api_key:
        raise ValueError("GROQ_API_KEY not found!")
    
    client = AsyncOpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")
    print("✅ Groq (Llama-3.3-70b) Connected. PRISMA Protocol v2.0 Active.")
except Exception as e:
    print(f"❌ ERROR: {e}")
    client = None

# =============================================================================
# 2. SYSTEM PROMPT - PRISMA Protocol Section 9 Aligned
# =============================================================================
SYSTEM_PROMPT = """
You are a Senior Technical Editor for IEEE COMST and an advanced extraction engine for a PRISMA-2020-compliant systematic review on "Optical Integrated Sensing and Communication (O-ISAC)".

Your task is to extract STRUCTURED DATA from academic papers into a precise JSON format. You must be thorough and extract ALL reported metrics.

================================================================================
CRITICAL RULES
================================================================================
1. ONLY extract explicitly stated values. Use "NR" (Not Reported) for missing data.
2. Use "NA" (Not Applicable) when a field doesn't apply to this paper type.
3. Create MULTIPLE experiment entries if the paper reports different scenarios.
4. Include EVIDENCE snippets (exact quotes) for all numerical values.
5. Pay attention to UNITS - convert to standard units specified in the schema.
6. The "isac_waveform_relationship" field is CRITICAL - determine how S&C waveforms relate.

================================================================================
OUTPUT JSON STRUCTURE
================================================================================
{
  "Paper_ID": "O_ISAC_XXX",
  
  "Study_Level": {
    "title": "string",
    "year": integer,
    "venue": "string",
    "document_type": "journal" | "conference" | "letter" | "review",
    
    "oisac_medium_class": "cabled_fibre" | "wireless_fso" | "wireless_vlc" | "wireless_lidar_like" | "wireless_retroreflective" | "hybrid",
    "carrier_band": "visible" | "NIR" | "C-band" | "L-band" | "other" | "NR",
    "operational_environment": "indoor" | "outdoor" | "lab" | "field_trial" | "mixed" | "NR",
    "link_topology": "monostatic" | "bistatic" | "multistatic" | "distributed_fibre" | "point_to_point" | "NR",
    
    "application_domain": ["vehicular", "indoor_positioning", "fibre_network_monitoring", ...],
    "evidence_type": ["simulation", "experimental", "analytical", "hybrid"],
    
    "ris_present": boolean,
    "opa_present": boolean,
    "ml_used": boolean,
    
    "key_contribution": "1-2 sentence summary",
    "gap_addressed": "1 sentence"
  },
  
  "Experiments": [
    {
      "Experiment_ID": "E1",
      "Scenario_Label": "Descriptive label (e.g., 'FSO link, 1km, Gamma-Gamma turbulence')",
      
      "Transmitter": {
        "tx_source_type": "laser" | "led" | "vcsel" | "frequency_comb" | "other",
        "tx_modulation_type": "im_dd" | "coherent" | "mixed" | "NR",
        "wavelength_nm": float or null,
        "tx_power_dbm": float or null,
        "optical_bandwidth_ghz": float or null
      },
      
      "Receiver": {
        "rx_detection_type": "direct" | "coherent" | "self_coherent" | "imaging" | "spad",
        "rx_detector": "pin_pd" | "apd_pd" | "balanced_pd" | "camera" | "NR"
      },
      
      "Integration": {
        "hardware_sharing_mode": "shared_frontend" | "partially_shared" | "separate_frontends" | "NR",
        "duplexing_mode": "full_duplex" | "half_duplex" | "tdm" | "fdm" | "wdm" | "NR"
      },
      
      "Waveform": {
        "comm_waveform_family": "ook" | "pam" | "ofdm" | "dmt" | "qam" | "psk" | "chirp_fmcw" | "other",
        "comm_modulation_order": integer or null,
        "comm_symbol_rate_gbaud": float or null,
        "sensing_waveform_family": "pulse_tof" | "fmcw_chirp" | "lfm_chirp" | "ofdm_sensing" | "backscatter_probe" | "same_as_comm" | "other",
        "isac_waveform_relationship": "single_dual_function" | "comm_embedded_in_sensing" | "sensing_embedded_in_comm" | "multiplexed_separate" | "superimposed" | "NR",
        "resource_partition": "string describing split (e.g., 'α=0.7 power to comm') or null"
      },
      
      "Channel_Fiber": {
        "fibre_length_km": float or null,
        "fibre_type": "smf" | "mmf" | "fmf" | "mcf" | null,
        "attenuation_db_per_km": float or null,
        "backscatter_sensing_type": "rayleigh_phi_otdr" | "das" | "brillouin" | "raman" | null
      },
      
      "Channel_Wireless": {
        "link_distance_m": float or null,
        "turbulence_model": "lognormal" | "gamma_gamma" | "malaga" | "none" | null,
        "turbulence_Cn2": float or null,
        "pointing_error_model": "zero" | "gaussian_jitter" | "beckmann" | null,
        "weather_visibility_m": float or null
      },
      
      "Comm_Metrics": {
        "data_rate_gbps": float or null,
        "spectral_efficiency_bps_hz": float or null,
        "ber": float or null,
        "snr_db": float or null,
        "outage_probability": float or null,
        "latency_ms": float or null
      },
      
      "Sensing_Metrics": {
        "sensing_task_type": ["ranging", "velocity", "localization_2d", "vibration", "target_detection", ...],
        "sensing_range_m": float or null,
        "range_resolution_m": float or null,
        "range_accuracy_m": float or null,
        "velocity_resolution_mps": float or null,
        "localization_error_m": float or null,
        "pd_detection_prob": float or null,
        "pfa_false_alarm": float or null,
        "crb_crlb_value": float or null,
        "crb_parameter": "range" | "angle" | "delay" | "position" | null
      },
      
      "Tradeoff": {
        "coupling_mode": "resource_division" | "joint_waveform" | "joint_receiver_processing" | "shared_hardware_only" | "NR",
        "tradeoff_type": ["rate_vs_rmse", "rate_vs_range_resolution", "power_split", "time_split", ...] or [],
        "tradeoff_representation": "single_point" | "curve" | "pareto_front" | "table" | "not_explicit",
        "tradeoff_control_parameter": "string (e.g., 'α', 'power_ratio')" or null,
        "tradeoff_control_range": "string (e.g., '[0.1, 0.9]')" or null
      },
      
      "OPA_Details": {
        "opa_num_emitters": integer or null,
        "opa_steering_range_deg": float or null
      },
      
      "Evidence": [
        {"field": "data_rate_gbps", "snippet": "exact quote from paper", "source": "TEXT" | "TABLE" | "FIGURE"},
        {"field": "range_resolution_m", "snippet": "exact quote", "source": "TEXT"},
        {"field": "isac_waveform_relationship", "snippet": "quote explaining waveform design", "source": "TEXT"}
      ],
      
      "Source_Pointer": "e.g., 'Section IV, Table II, Fig. 5'"
    }
  ],
  
  "Quality_Flags": {
    "both_sc_metrics_reported": boolean,
    "tradeoff_explicitly_analyzed": boolean,
    "uncertainty_reported": boolean,
    "baseline_comparison_present": boolean
  }
}

================================================================================
IMPORTANT NOTES
================================================================================
- For wavelength: Convert to nm (e.g., 1.55 μm → 1550 nm)
- For data rate: Convert to Gbps (e.g., 100 Mbps → 0.1 Gbps, 1 Tbps → 1000 Gbps)
- For distance: Convert to meters for wireless, km for fiber
- The "isac_waveform_relationship" is CRITICAL for taxonomy - always try to determine it
- If paper does NOT report BOTH comm AND sensing metrics, flag it in Quality_Flags
"""

# =============================================================================
# 3. EXTRACTION WORKER
# =============================================================================
async def extract_paper_v2(folder_path, semaphore):
    """Extract data from a single paper using enhanced schema."""
    async with semaphore:
        paper_id = os.path.basename(folder_path)
        
        # Find markdown file
        md_files = glob.glob(os.path.join(folder_path, "**", "*.md"), recursive=True)
        vis_file = os.path.join(folder_path, "visual_analysis.txt")
        
        if not md_files:
            print(f"   ⚠️ No markdown found: {paper_id}")
            return None

        try:
            # Read content
            with open(md_files[0], "r", encoding="utf-8") as f:
                text = f.read()
            
            visuals = ""
            if os.path.exists(vis_file):
                with open(vis_file, "r", encoding="utf-8") as f:
                    visuals = f.read()
            
            # Construct prompt
            user_content = f"""
=== PAPER ID: {paper_id} ===

=== VISUAL DATA (Charts/Figures) ===
{visuals if visuals else "No visual data extracted."}

=== FULL PAPER TEXT ===
{text[:90000]}
"""
            
            print(f"   🔬 Extracting: {paper_id}...")
            
            response = await client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_content}
                ],
                response_format={"type": "json_object"},
                temperature=0.05,  # Lower for more deterministic extraction
                max_tokens=8000
            )
            
            result = json.loads(response.choices[0].message.content)
            result["Paper_ID"] = paper_id
            result["extraction_timestamp"] = datetime.now().isoformat()
            result["schema_version"] = "2.0"
            
            print(f"   ✅ Done: {paper_id} - {len(result.get('Experiments', []))} experiments")
            return result

        except Exception as e:
            print(f"   ❌ Error ({paper_id}): {e}")
            return {"Paper_ID": paper_id, "error": str(e)}


# =============================================================================
# 4. DATA FLATTENING UTILITIES
# =============================================================================
def flatten_study_level(data):
    """Flatten study-level data for CSV export."""
    rows = []
    for paper in data:
        if "error" in paper:
            continue
            
        sl = paper.get("Study_Level", {})
        qf = paper.get("Quality_Flags", {})
        
        rows.append({
            "Paper_ID": paper.get("Paper_ID"),
            "Title": sl.get("title"),
            "Year": sl.get("year"),
            "Venue": sl.get("venue"),
            "Document_Type": sl.get("document_type"),
            "Medium_Class": sl.get("oisac_medium_class"),
            "Carrier_Band": sl.get("carrier_band"),
            "Environment": sl.get("operational_environment"),
            "Topology": sl.get("link_topology"),
            "Application_Domains": "|".join(sl.get("application_domain", [])),
            "Evidence_Type": "|".join(sl.get("evidence_type", [])),
            "RIS_Present": sl.get("ris_present"),
            "OPA_Present": sl.get("opa_present"),
            "ML_Used": sl.get("ml_used"),
            "Key_Contribution": sl.get("key_contribution"),
            "Gap_Addressed": sl.get("gap_addressed"),
            "Both_SC_Metrics": qf.get("both_sc_metrics_reported"),
            "Tradeoff_Analyzed": qf.get("tradeoff_explicitly_analyzed"),
            "Uncertainty_Reported": qf.get("uncertainty_reported"),
            "Baseline_Present": qf.get("baseline_comparison_present")
        })
    return pd.DataFrame(rows)


def flatten_experiments(data):
    """Flatten experiment-level data for comprehensive CSV export."""
    rows = []
    for paper in data:
        if "error" in paper:
            continue
            
        paper_id = paper.get("Paper_ID")
        
        for exp in paper.get("Experiments", []):
            tx = exp.get("Transmitter", {})
            rx = exp.get("Receiver", {})
            intg = exp.get("Integration", {})
            wf = exp.get("Waveform", {})
            cf = exp.get("Channel_Fiber", {})
            cw = exp.get("Channel_Wireless", {})
            cm = exp.get("Comm_Metrics", {})
            sm = exp.get("Sensing_Metrics", {})
            tf = exp.get("Tradeoff", {})
            opa = exp.get("OPA_Details", {})
            
            rows.append({
                # Identification
                "Paper_ID": paper_id,
                "Exp_ID": exp.get("Experiment_ID"),
                "Scenario": exp.get("Scenario_Label"),
                "Source": exp.get("Source_Pointer"),
                
                # Transmitter
                "TX_Source": tx.get("tx_source_type"),
                "TX_Mod_Type": tx.get("tx_modulation_type"),
                "Wavelength_nm": tx.get("wavelength_nm"),
                "TX_Power_dBm": tx.get("tx_power_dbm"),
                "Optical_BW_GHz": tx.get("optical_bandwidth_ghz"),
                
                # Receiver
                "RX_Detection": rx.get("rx_detection_type"),
                "RX_Detector": rx.get("rx_detector"),
                
                # Integration
                "HW_Sharing": intg.get("hardware_sharing_mode"),
                "Duplexing": intg.get("duplexing_mode"),
                
                # Waveform - CRITICAL
                "Comm_Waveform": wf.get("comm_waveform_family"),
                "Mod_Order": wf.get("comm_modulation_order"),
                "Symbol_Rate_GBaud": wf.get("comm_symbol_rate_gbaud"),
                "Sensing_Waveform": wf.get("sensing_waveform_family"),
                "ISAC_Relationship": wf.get("isac_waveform_relationship"),  # ⭐ KEY
                "Resource_Partition": wf.get("resource_partition"),
                
                # Channel - Fiber
                "Fibre_Length_km": cf.get("fibre_length_km"),
                "Fibre_Type": cf.get("fibre_type"),
                "Attenuation_dB_km": cf.get("attenuation_db_per_km"),
                "Backscatter_Type": cf.get("backscatter_sensing_type"),
                
                # Channel - Wireless
                "Link_Distance_m": cw.get("link_distance_m"),
                "Turbulence_Model": cw.get("turbulence_model"),
                "Cn2": cw.get("turbulence_Cn2"),
                "Pointing_Error": cw.get("pointing_error_model"),
                "Visibility_m": cw.get("weather_visibility_m"),
                
                # Communication Metrics
                "Data_Rate_Gbps": cm.get("data_rate_gbps"),
                "Spectral_Eff_bps_Hz": cm.get("spectral_efficiency_bps_hz"),
                "BER": cm.get("ber"),
                "SNR_dB": cm.get("snr_db"),
                "Outage_Prob": cm.get("outage_probability"),
                "Latency_ms": cm.get("latency_ms"),
                
                # Sensing Metrics
                "Sensing_Tasks": "|".join(sm.get("sensing_task_type", [])),
                "Sensing_Range_m": sm.get("sensing_range_m"),
                "Range_Resolution_m": sm.get("range_resolution_m"),
                "Range_Accuracy_m": sm.get("range_accuracy_m"),
                "Velocity_Resolution_mps": sm.get("velocity_resolution_mps"),
                "Localization_Error_m": sm.get("localization_error_m"),
                "Pd_Detection": sm.get("pd_detection_prob"),
                "Pfa_FalseAlarm": sm.get("pfa_false_alarm"),
                "CRB_Value": sm.get("crb_crlb_value"),
                "CRB_Param": sm.get("crb_parameter"),
                
                # Tradeoff - CRITICAL
                "Coupling_Mode": tf.get("coupling_mode"),
                "Tradeoff_Type": "|".join(tf.get("tradeoff_type", [])),
                "Tradeoff_Repr": tf.get("tradeoff_representation"),
                "Tradeoff_Param": tf.get("tradeoff_control_parameter"),
                "Tradeoff_Range": tf.get("tradeoff_control_range"),
                
                # OPA
                "OPA_Emitters": opa.get("opa_num_emitters"),
                "OPA_Steering_deg": opa.get("opa_steering_range_deg")
            })
    
    return pd.DataFrame(rows)


# =============================================================================
# 5. MAIN PIPELINE
# =============================================================================
async def run_extraction_pipeline_v2(limit=None):
    """Run the full extraction pipeline."""
    if not client:
        print("❌ No API client available.")
        return
    
    print("\n" + "="*70)
    print("🚀 O-ISAC PRISMA EXTRACTION PIPELINE v2.0")
    print("="*70)
    
    # Find all paper folders
    folders = sorted([f for f in glob.glob(os.path.join(INTERMEDIATE_DIR, "*")) if os.path.isdir(f)])
    
    if limit:
        folders = folders[:limit]
    
    print(f"📄 Papers to process: {len(folders)}")
    
    # Rate limit (Groq Free: 2 concurrent, adjust for paid)
    semaphore = asyncio.Semaphore(2)
    
    # Run extraction
    tasks = [extract_paper_v2(f, semaphore) for f in folders]
    results = await asyncio.gather(*tasks)
    
    # Filter valid results
    valid_data = [r for r in results if r is not None]
    error_data = [r for r in valid_data if "error" in r]
    success_data = [r for r in valid_data if "error" not in r]
    
    print(f"\n✅ Successful: {len(success_data)}")
    print(f"❌ Errors: {len(error_data)}")
    
    if success_data:
        # Save JSON
        json_path = os.path.join(FINAL_DIR, "extraction_v2_full.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(success_data, f, indent=2, ensure_ascii=False)
        
        # Flatten and save CSVs
        df_study = flatten_study_level(success_data)
        df_exp = flatten_experiments(success_data)
        
        study_path = os.path.join(FINAL_DIR, "study_level_v2.csv")
        exp_path = os.path.join(FINAL_DIR, "experiment_level_v2.csv")
        
        df_study.to_csv(study_path, index=False)
        df_exp.to_csv(exp_path, index=False)
        
        print("\n" + "="*70)
        print("📁 OUTPUT FILES")
        print("="*70)
        print(f"📋 Full JSON: {json_path}")
        print(f"📊 Study-Level CSV: {study_path}")
        print(f"🔬 Experiment-Level CSV: {exp_path}")
        
        # Quick stats
        print("\n" + "="*70)
        print("📈 QUICK STATISTICS")
        print("="*70)
        print(f"Total Experiments: {len(df_exp)}")
        print(f"\nMedium Distribution:")
        print(df_study["Medium_Class"].value_counts().to_string())
        print(f"\nISAC Waveform Relationship:")
        print(df_exp["ISAC_Relationship"].value_counts().to_string())
        print(f"\nCoupling Mode:")
        print(df_exp["Coupling_Mode"].value_counts().to_string())
        
        # Sample output
        print("\n" + "="*70)
        print("🔍 SAMPLE EXPERIMENT DATA")
        print("="*70)
        print(df_exp[["Paper_ID", "Scenario", "ISAC_Relationship", "Data_Rate_Gbps", "Range_Resolution_m", "Coupling_Mode"]].head(5).to_string())
    
    return success_data


# =============================================================================
# 6. ENTRY POINT
# =============================================================================
if __name__ == "__main__":
    # For Colab, use: await run_extraction_pipeline_v2()
    # For local Python: asyncio.run(run_extraction_pipeline_v2())
    pass

# In Colab, run:
# await run_extraction_pipeline_v2(limit=5)  # Test with 5 papers first
# await run_extraction_pipeline_v2()  # Full run
