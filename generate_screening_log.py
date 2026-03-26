import pandas as pd
import os
import datetime

# Define paths
base_dir = r"g:\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST"
search_csv_path = os.path.join(base_dir, "data", "search_logs", "export2025.12.28-05.30.23.csv")
included_csv_path = os.path.join(base_dir, "analysis", "phase1_screening", "included_studies_list.csv")
log_csv_path = os.path.join(base_dir, "analysis", "phase1_screening", "screening_log.csv")

# Approved DOIs (O_ISAC_159 to O_ISAC_163)
approved_dois = [
    "10.1109/OJCOMS.2025.3545896", # O_ISAC_159
    "10.1109/OJCS.2024.3386733",    # O_ISAC_160
    "10.1109/JSTEAP.2025.3610564",  # O_ISAC_161
    "10.1109/JSTEAP.2025.3603540",  # O_ISAC_162
    "10.1109/COMST.2024.3519785"    # O_ISAC_163
]

try:
    print("Reading files...")
    # Use python engine for more robust parsing of quoted fields
    new_df = pd.read_csv(search_csv_path, quotechar='"', engine='python', on_bad_lines='skip')
    included_df = pd.read_csv(included_csv_path, quotechar='"', engine='python', on_bad_lines='warn')

    # Normalize DOIs
    new_df['DOI_clean'] = new_df['DOI'].astype(str).str.lower().str.strip()
    included_df['DOI_clean'] = included_df['DOI'].astype(str).str.lower().str.strip()
    
    # Existing DOIs (excluding the ones we just added, effectively)
    # Actually, we just added them to included_studies_list, so they ARE in included_df now.
    # We want to log the "Decision" for this batch.
    
    log_entries = []
    
    for _, row in new_df.iterrows():
        doi = str(row['DOI']).strip()
        doi_clean = doi.lower()
        title = row['Document Title']
        year = row['Publication Year']
        
        status = "Excluded"
        reason = "Does not meet O-ISAC criteria (Optical+Sensing+Comm)"
        
        # Check if it's one of the approved ones
        if doi in approved_dois:
            status = "Included"
            reason = "Met inclusion criteria (New)"
        
        # Check if it was already in the list (Duplicate)
        # Note: Since we added approved ones to list, we must check if it was there BEFORE.
        # But included_df has them now. 
        # Logic: If it's NOT in approved_list but IS in included_df, it's a Duplicate.
        # If it IS in approved_list, it's New Included.
        
        is_in_db = doi_clean in included_df['DOI_clean'].values
        
        if is_in_db and doi not in approved_dois:
             status = "Duplicate"
             reason = "Already in database"
        elif doi in approved_dois:
             status = "Included"
             reason = "Met criteria (Collaborative Screening 2025-12-28)"
        
        log_entries.append({
            "Date": datetime.date.today(),
            "Title": title,
            "Year": year,
            "DOI": doi,
            "Decision": status,
            " Reason": reason
        })

    log_df = pd.DataFrame(log_entries)
    
    # Save/Append to log
    if os.path.exists(log_csv_path):
        log_df.to_csv(log_csv_path, mode='a', header=False, index=False)
    else:
        log_df.to_csv(log_csv_path, index=False)
        
    print(f"Successfully logged {len(log_df)} items to {log_csv_path}")

except Exception as e:
    print(f"Error: {e}")
