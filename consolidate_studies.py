
import pandas as pd
import os
import shutil

BASE_DIR = r'c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST'
CANDIDATES_PATH = os.path.join(BASE_DIR, 'scopus_candidates.csv')
AI_RESULTS_PATH = os.path.join(BASE_DIR, 'analysis/ph1_scr/ai_scr_dec_scopus.csv')
MAIN_LIST_PATH = os.path.join(BASE_DIR, 'analysis/ph1_scr/included_studies_list.csv')
ARCHIVE_DIR = os.path.join(BASE_DIR, 'analysis/ph1_scr/logs_archive')

os.makedirs(ARCHIVE_DIR, exist_ok=True)

print("📂 Starting Consolidation...")

try:
    # 1. Load DataFrames
    df_candidates = pd.read_csv(CANDIDATES_PATH)
    df_ai = pd.read_csv(AI_RESULTS_PATH)
    
    # 2. Filter AI 'Included'
    included_tracks = df_ai[df_ai['Decision'] == 'Included']['Track_ID'].tolist()
    print(f"👉 AI identified {len(included_tracks)} included studies.")
    
    # 3. Join with Metadata (Candidates)
    # Filter candidates that are in the included list
    # We assume 'Track_ID' is in df_candidates. If not, we might need to map by index or Title.
    # Let's check columns first.
    if 'Track_ID' not in df_candidates.columns:
        # Emergency fallback: Create Track_ID mapping from index or Title match
        print("⚠️ 'Track_ID' missing in candidates file. Attempting Title match...")
        df_candidates['Title_Norm'] = df_candidates['Document Title'].str.strip().str.lower()
        df_ai['Title_Norm'] = df_ai['Title'].str.strip().str.lower()
        
        # Merge on Title
        merged_df = pd.merge(df_ai[df_ai['Decision'] == 'Included'], 
                             df_candidates, 
                             left_on='Title_Norm', 
                             right_on='Title_Norm', 
                             how='left')
    else:
        merged_df = df_candidates[df_candidates['Track_ID'].isin(included_tracks)].copy()

    print(f"✅ Matched {len(merged_df)} studies with full metadata.")

    # 4. Prepare for Main List
    # Mappings: 
    # Document Title -> Title
    # Authors -> Authors
    # Year -> Publication Year
    # DOI -> DOI
    # Source title -> Venue
    # Abstract -> Abstract
    
    entries_to_add = []
    for _, row in merged_df.iterrows():
        entry = {
            'Track_ID': row.get('Track_ID', row.get('Track_ID_x')), # Handle merge artifacts
            'Title': row.get('Document Title', row.get('Title_y')),
            'Authors': row.get('Authors'),
            'Year': row.get('Publication Year', row.get('Year')),
            'DOI': row.get('DOI'),
            'Venue': row.get('Source title', row.get('Source title')), # Might differ
            'Abstract': row.get('Abstract')
        }
        entries_to_add.append(entry)
        
    new_df = pd.DataFrame(entries_to_add)
    
    # 5. Load Existing Main List
    if os.path.exists(MAIN_LIST_PATH):
        existing_df = pd.read_csv(MAIN_LIST_PATH)
        existing_ids = set(existing_df['Track_ID'].astype(str))
    else:
        existing_df = pd.DataFrame(columns=['Track_ID', 'Title', 'Authors', 'Year', 'DOI', 'Venue', 'Abstract'])
        existing_ids = set()
        
    # 6. Append Only New
    final_rows = []
    added_count = 0
    for _, row in new_df.iterrows():
        if str(row['Track_ID']) not in existing_ids:
            final_rows.append(row)
            added_count += 1
            
    if added_count > 0:
        final_df = pd.concat([existing_df, pd.DataFrame(final_rows)], ignore_index=True)
        final_df.to_csv(MAIN_LIST_PATH, index=False)
        print(f"🎉 Successfully added {added_count} new studies to {MAIN_LIST_PATH}")
    else:
        print("ℹ️ No new studies to add (all already exist in main list).")
        
    # 7. Cleanup / Archive
    # Move intermediate files to archive to keep folder clean
    # We keep 'screening_log.csv' as it is the master log.
    # We move 'ai_scr_dec_scopus.csv' and 'ai_included_candidates.md' (optional)
    
    shutil.copy2(AI_RESULTS_PATH, os.path.join(ARCHIVE_DIR, 'ai_scr_dec_scopus_v1.csv'))
    print(f"🧹 Archived intermediate file to {ARCHIVE_DIR}")

except Exception as e:
    print(f"❌ Critical Error: {e}")
    import traceback
    traceback.print_exc()
