
import pandas as pd
import os

# Paths
base_dir = r'c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST'
included_csv_path = os.path.join(base_dir, 'analysis/ph1_scr/included_studies_list.csv')
log_csv_path = os.path.join(base_dir, 'analysis/ph1_scr/screening_log.csv')
pdf_dir = os.path.join(base_dir, 'data/ret_docs')

# 1. Identify Missing PDFs
if not os.path.exists(included_csv_path):
    print("❌ Error: included_studies_list.csv not found.")
    exit()

df_included = pd.read_csv(included_csv_path)
existing_files = set(f.lower() for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf'))

ids_to_exclude = []
indices_to_drop = []

print(f"🔍 Scanning {len(df_included)} included studies...")

for idx, row in df_included.iterrows():
    track_id = str(row['Track_ID']).strip()
    expected_file = f'{track_id}.pdf'.lower()
    
    if expected_file not in existing_files:
        ids_to_exclude.append(track_id)
        indices_to_drop.append(idx)

print(f"⚠️ Found {len(ids_to_exclude)} missing PDFs to exclude.")
if len(ids_to_exclude) == 0:
    print("No missing PDFs found. Nothing to update.")
    exit()

# 2. Update Included List (Remove them)
df_included_updated = df_included.drop(indices_to_drop)
df_included_updated.to_csv(included_csv_path, index=False)
print(f"✅ Removed {len(indices_to_drop)} entries from included_studies_list.csv. New count: {len(df_included_updated)}")

# 3. Update Screening Log (Change Decision to Excluded)
if os.path.exists(log_csv_path):
    df_log = pd.read_csv(log_csv_path)
    
    # Check if 'Track_ID' exists in log
    # Based on previous interaction, we know 'Track_ID' was NOT in screening_log originally, 
    # but we were matching by Title. 
    # HOWEVER, we might have added it or not. Let's handle both.
    
    updated_count = 0
    reason_msg = "Full text not available"
    
    # We'll use a map of Track_ID in ids_to_exclude -> Title from df_included (the original rows)
    # to find them in the log if Track_ID is missing in log.
    
    # Create map: Track_ID -> Title (from the rows we are dropping)
    id_title_map = df_included.loc[indices_to_drop].set_index('Track_ID')['Title'].to_dict()
    
    # Also standardize titles for matching
    id_title_map_norm = {k: str(v).strip().lower() for k, v in id_title_map.items()}
    
    # Assuming log has 'Title' column
    # Normalize log titles
    df_log['Title_Norm'] = df_log['Title'].str.strip().str.lower()
    
    for track_id, title_norm in id_title_map_norm.items():
        # Update row where Title matches
        mask = df_log['Title_Norm'] == title_norm
        if mask.any():
            df_log.loc[mask, 'Decision'] = 'Excluded'
            # Handle Reason column name variation ('Reason' vs ' Reason')
            reason_col = ' Reason' if ' Reason' in df_log.columns else 'Reason'
            df_log.loc[mask, reason_col] = reason_msg
            updated_count += df_log.loc[mask].shape[0]
            
    # Drop temp col
    df_log.drop(columns=['Title_Norm'], inplace=True)
    
    df_log.to_csv(log_csv_path, index=False)
    print(f"✅ Updated {updated_count} entries in screening_log.csv to 'Excluded'.")

else:
    print("⚠️ screening_log.csv not found. Could not update log.")

print("\n--- IDs Excluded ---")
print(", ".join(ids_to_exclude))
