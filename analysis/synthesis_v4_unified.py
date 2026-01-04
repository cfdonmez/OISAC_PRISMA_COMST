import os
import json
import pandas as pd
from glob import glob

def safe_get(data, path, default="NR"):
    """Safely extracts nested data from a dictionary."""
    try:
        curr = data
        for p in path.replace('[', '.').replace(']', '').split('.'):
            if p.isdigit():
                curr = curr[int(p)]
            else:
                curr = curr.get(p, default)
            if curr == default: return default
        return curr
    except:
        return default

def synthesize_v4_results(results_dir, output_csv):
    files = glob(os.path.join(results_dir, "*.json"))
    print(f"🔍 Found {len(files)} result files. Processing...")
    
    rows = []
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except:
                continue
        
        paper_id = os.path.basename(file_path).split('_v4')[0]
        
        # Extract Key Metrics for Trend Analysis
        title = safe_get(data, "study_level.bibliographic.title")
        scenario = safe_get(data, "study_level.classification.oisac_medium_class")
        
        # Scenario 0 Metrics (Primary)
        # Note: 'scenario_level' is a list
        scenario_data = safe_get(data, "scenario_level.0", default={})
        
        # Comm Metrics
        bitrate_gbps = safe_get(scenario_data, "comm_metrics.data_rate_gbps")
        
        # Sensing Metrics
        resolution_m = safe_get(scenario_data, "sensing_metrics.range_resolution_m")
        if resolution_m == "NR":
             resolution_m = safe_get(scenario_data, "sensing_metrics.spatial_resolution_m")
        
        # Distance
        distance_m = safe_get(scenario_data, "channel_wireless.link_distance_m")
        if distance_m == "NR" or distance_m == 0:
             distance_m = safe_get(scenario_data, "channel_fiber.fibre_length_km") 
             if distance_m != "NR": distance_m = float(distance_m) * 1000 # Convert km to m
        
        # Hardware
        freq_band = safe_get(scenario_data, "transmitter.wavelength_nm") # Proxy for band
        
        rows.append({
            "Paper_ID": paper_id,
            "Title": title,
            "Scenario": scenario,
            "Bitrate_Gbps": bitrate_gbps,
            "Resolution_m": resolution_m,
            "Distance_m": distance_m,
            "Wavelength_nm": freq_band
        })
    
    df = pd.DataFrame(rows)
    df.to_csv(output_csv, index=False, encoding='utf-8-sig')
    print(f"✅ Synthesis complete! Saved to {output_csv}")
    return df

if __name__ == "__main__":
    PROJECT_ROOT = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST"
    RESULTS_DIR = os.path.join(PROJECT_ROOT, "data", "extraction_results_v4")
    OUTPUT_FILE = os.path.join(PROJECT_ROOT, "data", "extraction_v4_unified.csv")
    
    synthesize_v4_results(RESULTS_DIR, OUTPUT_FILE)
