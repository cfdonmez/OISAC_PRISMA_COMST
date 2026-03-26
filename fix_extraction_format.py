import os
import json
import pandas as pd

results_dir = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\extraction_results_v4"
summary_path = os.path.join(results_dir, "extraction_v4_summary.csv")

def fix_and_summarize():
    all_results = []
    files = [f for f in os.listdir(results_dir) if f.endswith("_v4.json")]
    print(f"Processing {len(files)} files...")
    
    for filename in files:
        file_path = os.path.join(results_dir, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # 1. Standardize reasoning_trace to list
            trace = data.get("reasoning_trace")
            if isinstance(trace, dict):
                new_trace = []
                for k, v in trace.items():
                    new_trace.append({"key": k, "value": v})
                data["reasoning_trace"] = new_trace
                
                # Save back to file
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)
            
            # 2. Extract info for summary
            paper_id = data.get("Paper_ID", filename.replace("_v4.json", ""))
            row = {"Paper_ID": paper_id}
            
            trace_list = data.get("reasoning_trace", [])
            for item in trace_list:
                key = item.get("key")
                val = item.get("value", "")
                if key:
                    row[key] = val[:1000] # Increased limit for better visibility
            
            all_results.append(row)
            
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    # 3. Save Summary CSV
    if all_results:
        df = pd.DataFrame(all_results)
        # Ensure column order
        cols = ["Paper_ID", "step_0_visual_inspection", "step_1_concept_analysis", "step_2_benchmark_verification", "step_3_strategic_critique"]
        existing_cols = [c for c in cols if c in df.columns]
        other_cols = [c for c in df.columns if c not in cols]
        df = df[existing_cols + other_cols]
        
        df.sort_values("Paper_ID").to_csv(summary_path, index=False)
        print(f"Summary saved to {summary_path}")

if __name__ == "__main__":
    fix_and_summarize()
