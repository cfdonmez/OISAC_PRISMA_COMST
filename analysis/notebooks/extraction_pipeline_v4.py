# =============================================================================
# O-ISAC INTEGRATED EXTRACTION PIPELINE v4.0 (The Factory)
# =============================================================================
# OPTIMIZATION: Unifies Structural Extraction + Reasoning (CoT)
# 
# Features:
# - Phase 1: PDF -> Markdown (Marker)
# - Phase 2: Visual Analysis (Gemini 2.5 Flash)
# - Phase 3: Reasoning + Extraction (CoTAssembler + Llama 3.3)
# - "Living" Workflow aware (Batch processing)
# =============================================================================

import os
import glob
import json
import asyncio
import pandas as pd
from datetime import datetime
from pathlib import Path

# Import existing V3 logic for Phase 1 & 2 (Reuse what works)
import extraction_pipeline_v3 as v3
from extraction_pipeline_v3 import Config, CheckpointManager

# Import The Engine
import sys
# Ensure analysis/cot_laboratory is in path
sys.path.append(os.path.join(Config.PROJECT_PATH, "analysis/cot_laboratory"))
from core.assembler import CoTAssembler

# =============================================================================
# CONFIGURATION EXTENSIONS
# =============================================================================
class ConfigV4(Config):
    OUTPUT_DIR = os.path.join(Config.PROJECT_PATH, "data/extraction_results_v4")
    RECIPE_PATH = "analysis/cot_laboratory/recipes/experiment_v1_full_analysis.yaml"
    
    @classmethod
    def init_dirs(cls):
        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)
        # Also ensure v3 dirs exist for compatibility
        Config.init_dirs() 

# =============================================================================
# PHASE 3: INTEGRATED REASONING EXTRACTION
# =============================================================================
def phase3_integrated_extraction(checkpoint: CheckpointManager, limit: int = None):
    """
    Replaces v3's LLM extraction with CoTAssembler.
    """
    print("\n" + "="*60)
    print("🧠 PHASE 3: INTEGRATED REASONING EXTRACTION (CoTAssembler)")
    print("="*60)
    
    # Initialize Engine
    try:
        assembler = CoTAssembler(Config.PROJECT_PATH)
    except Exception as e:
        print(f"❌ Failed to initialize CoTAssembler: {e}")
        return []

    # Find papers to process
    folders = sorted(glob.glob(os.path.join(Config.MARKDOWN_DIR, "*")))
    if limit:
        folders = folders[:limit]
    
    print(f"Papers to process: {len(folders)}")
    
    results = []
    
    for i, folder in enumerate(folders):
        paper_id = os.path.basename(folder)
        
        # Check if already done in v4
        v4_result_path = os.path.join(ConfigV4.OUTPUT_DIR, f"{paper_id}_v4.json")
        if os.path.exists(v4_result_path):
            print(f"[{i+1}/{len(folders)}] ⏩ {paper_id} - already processed (v4)")
            with open(v4_result_path, 'r') as f:
                results.append(json.load(f))
            continue
        
        print(f"[{i+1}/{len(folders)}] 🔨 Processing: {paper_id}")
        
        # 1. Load Content (Markdown + Visuals)
        md_files = glob.glob(os.path.join(folder, "**", "*.md"), recursive=True)
        if not md_files:
            print(f"   ❌ No markdown found for {paper_id}")
            continue
            
        with open(md_files[0], 'r', encoding='utf-8') as f:
            paper_text = f.read()
            
        vis_file = os.path.join(folder, "visual_analysis.txt")
        visual_content = ""
        if os.path.exists(vis_file):
            with open(vis_file, 'r', encoding='utf-8') as f:
                visual_content = f.read()
        
        # 2. Run CoT Assembler
        try:
            # We call the assembler relative to project root
            recipe_rel_path = "analysis/cot_laboratory/recipes/experiment_v1_full_analysis.yaml"
            
            output = assembler.run_extraction(
                recipe_path=recipe_rel_path,
                paper_text=paper_text[:Config.MAX_CONTEXT_CHARS], # Safety truncate
                paper_id=paper_id,
                visual_content=visual_content
            )
            
            if output["status"] == "success":
                data = output["parsed_output"]
                data["Paper_ID"] = paper_id # Ensure ID is present
                
                # Save Individual Result
                with open(v4_result_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)
                
                checkpoint.mark_complete(paper_id, "hash_placeholder", "extraction_v4")
                results.append(data)
                print(f"   ✅ Success")
            else:
                print(f"   ❌ Error: {output.get('error_message')}")
                checkpoint.add_error(paper_id, "extraction_v4", output.get('error_message'))
                
        except Exception as e:
            print(f"   ❌ Critical Error: {e}")
            checkpoint.add_error(paper_id, "extraction_v4", str(e))
            
    # Aggregate Rules
    save_aggregated_results(results)
    return results

def save_aggregated_results(results):
    if not results:
        return

    # Save Full JSON
    json_path = os.path.join(ConfigV4.OUTPUT_DIR, "extraction_v4_unified.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print(f"\n📁 Aggregated JSON saved: {json_path}")
    
    # Flatten to CSV (Simplified for immediate view)
    # Reuse v3 CSV logic or simple flatten
    try:
        rows = []
        for r in results:
            sl = r.get("study_level", {}).get("bibliographic", {})
            # Handle list vs dict structure if schema varies
            # (Assuming standard schema v2.1 structure)
            
            # Simple flattening for key fields
            row = {"Paper_ID": r.get("Paper_ID")}
            
            # Extract Reasoning Trace
            trace = r.get("reasoning_trace", [])
            if isinstance(trace, list):
                for step in trace:
                    row[step.get("key", "unknown")] = step.get("value", "")[:100] + "..." # Truncate for CSV
            
            rows.append(row)
            
        pd.DataFrame(rows).to_csv(os.path.join(ConfigV4.OUTPUT_DIR, "extraction_v4_summary.csv"), index=False)
        print("📊 Summary CSV saved.")
    except Exception as e:
        print(f"⚠️ CSV flatten warning: {e}")

# =============================================================================
# MAIN RUNNER
# =============================================================================
def run_v4_pipeline(skip_phase1=False, skip_phase2=False, limit=None, force_all=False):
    """
    The Optimized V4 Pipeline.
    """
    print("\n" + "="*70)
    print("🚀 O-ISAC INTEGRATED PIPELINE v4.0 (Factory Mode)")
    print("="*70)
    print(f"📅 Started: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    ConfigV4.init_dirs()
    checkpoint = CheckpointManager(ConfigV4.CHECKPOINT_FILE) # Reuse v3 checkpoint logic but maybe separate file? 
    # Let's use v4 checkpoint
    checkpoint = CheckpointManager(os.path.join(ConfigV4.OUTPUT_DIR, "checkpoint_v4.json"))
    
    # Phase 1: PDF -> Markdown (Reuse v3)
    if not skip_phase1:
        v3.phase1_marker_conversion(checkpoint, force_all=force_all)
    
    # Phase 2: Visual Analyis (Reuse v3)
    if not skip_phase2:
        v3.phase2_visual_analysis(checkpoint)
        
    # Phase 3: Integrated Extraction (NEW)
    results = phase3_integrated_extraction(checkpoint, limit=limit)
    
    print("\n" + "="*70)
    print(f"🎉 V4 PIPELINE COMPLETE - {len(results)} papers")
    print("="*70)
    
    return results
