import pandas as pd
import os

# Define paths
base_dir = r"g:\Drive'ım\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST"
new_csv_path = os.path.join(base_dir, "data", "search_logs", "export2025.12.28-05.30.23.csv")
included_csv_path = os.path.join(base_dir, "analysis", "phase1_screening", "included_studies_list.csv")

try:
    # Read the CSVs
    print(f"Reading new CSV from: {new_csv_path}")
    new_df = pd.read_csv(new_csv_path)
    print(f"Reading included CSV from: {included_csv_path}")
    included_df = pd.read_csv(included_csv_path)

    # Convert DOIs to string and lowercase for comparison, handling NaNs
    new_df['DOI_clean'] = new_df['DOI'].astype(str).str.lower().str.strip()
    included_df['DOI_clean'] = included_df['DOI'].astype(str).str.lower().str.strip()

    # Convert Titles to string and lowercase for comparison
    new_df['Title_clean'] = new_df['Document Title'].astype(str).str.lower().str.strip()
    included_df['Title_clean'] = included_df['Document Title'].astype(str).str.lower().str.strip()

    # Identify duplicates
    doi_duplicates = new_df[new_df['DOI_clean'].isin(included_df['DOI_clean']) & (new_df['DOI_clean'] != 'nan')]
    title_duplicates = new_df[new_df['Title_clean'].isin(included_df['Title_clean'])]
    
    # Combine duplicates
    all_duplicates = pd.concat([doi_duplicates, title_duplicates]).drop_duplicates()
    
    # Identify fresh candidates
    fresh_candidates = new_df[~new_df.index.isin(all_duplicates.index)]

    print("-" * 30)
    print(f"Total New Entries: {len(new_df)}")
    print(f"Duplicates Found: {len(all_duplicates)}")
    print(f"Fresh Candidates: {len(fresh_candidates)}")
    print("-" * 30)

    if not fresh_candidates.empty:
        print("Fresh Candidates List:")
        # Print Title and DOI for candidates
        print(fresh_candidates[['Document Title', 'DOI']].to_string())
    else:
        print("No fresh candidates found.")

except Exception as e:
    print(f"An error occurred: {e}")
