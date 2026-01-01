import pandas as pd
import re
import os

# --- Configuration ---
SCOPUS_FILE = r"data/search_logs/scopus_export_Dec 28-2025_b7fbefb1-055d-45f8-a240-8163c71acaa5.csv"
INCLUDED_LIST = r"analysis/phase1_screening/included_studies_list.csv"
SCREENING_LOG = r"analysis/phase1_screening/screening_log.csv"
OUTPUT_CANDIDATES = r"scopus_candidates.csv"
OUTPUT_SCREENING_ENTRIES = r"scopus_screening_entries.csv"

START_ID = 165

def normalize_text(text):
    if not isinstance(text, str):
        return ""
    return re.sub(r'[^a-z0-9]', '', text.lower())

def normalize_doi(doi):
    if not isinstance(doi, str):
        return ""
    return doi.lower().strip()

def format_authors(scopus_authors):
    """
    Converts Scopus 'Last, I.; Last, I.' to 'I. Last; I. Last'
    This is best-effort.
    """
    if not isinstance(scopus_authors, str):
        return ""
    
    # Split by semicolon
    authors = [a.strip() for a in scopus_authors.split(';')]
    formatted = []
    for auth in authors:
        parts = auth.split(',')
        if len(parts) == 2:
            last = parts[0].strip()
            initials = parts[1].strip()
            # If initials ends with '.', keep it, else add it? 
            # Usually Scopus gives "Smith, J." or "Smith, J.A."
            formatted.append(f"{initials} {last}")
        else:
            formatted.append(auth)
    return "; ".join(formatted)

def main():
    print("--- Starting Scopus Duplicate Check ---")
    
    # 1. Load Existing DB
    existing_dois = set()
    existing_titles = set()
    
    # Load Included List
    try:
        df_inc = pd.read_csv(INCLUDED_LIST, encoding='utf-8')
        print(f"Loaded {len(df_inc)} included studies.")
        for _, row in df_inc.iterrows():
            if pd.notna(row['DOI']): existing_dois.add(normalize_doi(row['DOI']))
            if pd.notna(row['Document Title']): existing_titles.add(normalize_text(row['Document Title']))
    except Exception as e:
        print(f"Warning: Could not load included list: {e}")

    # Load Screening Log (to catch excluded duplicates too)
    try:
        df_log = pd.read_csv(SCREENING_LOG, encoding='utf-8')
        print(f"Loaded {len(df_log)} screening log entries.")
        for _, row in df_log.iterrows():
            if pd.notna(row.get('DOI')): existing_dois.add(normalize_doi(row['DOI']))
            if pd.notna(row.get('Title')): existing_titles.add(normalize_text(row['Title']))
    except Exception as e:
        print(f"Warning: Could not load screening log: {e}")

    # 2. Load Scopus File
    try:
        # Scopus export might be utf-8 or utf-8-sig
        df_scopus = pd.read_csv(SCOPUS_FILE, encoding='utf-8')
        print(f"Loaded Scopus Result: {len(df_scopus)} rows.")
    except Exception as e:
        print(f"CRITICAL: Could not read Scopus file: {e}")
        return

    new_candidates = []
    screening_entries = []
    
    current_id = START_ID
    duplicates_found = 0

    for _, row in df_scopus.iterrows():
        title = str(row.get('Title', '')).strip()
        doi = str(row.get('DOI', '')).strip()
        authors_raw = row.get('Authors', '')
        year = row.get('Year', '')
        venue = row.get('Source title', '')
        
        # Normalize for check
        norm_title = normalize_text(title)
        norm_doi = normalize_doi(doi)
        
        is_dup = False
        if norm_doi and norm_doi in existing_dois:
            is_dup = True
        elif norm_title and norm_title in existing_titles:
            is_dup = True
            
        # Determine Status
        status = "Duplicate" if is_dup else "Included" # Default to Included for now, user checks later
        
        if is_dup:
            duplicates_found += 1
            # Add to screening log only
            screening_entries.append({
                'Date': '2025-12-28',
                'Title': title,
                'Year': year,
                'DOI': doi,
                'Decision': 'Duplicate',
                ' Reason': 'Already in database'
            })
        else:
            # Check Year for Protocol Exclusion
            try:
                pub_year = int(float(year)) if pd.notna(year) else 0
            except:
                pub_year = 0
                
            if pub_year < 2020:
                # Excluded by Date
                screening_entries.append({
                    'Date': '2025-12-28',
                    'Title': title,
                    'Year': year,
                    'DOI': doi,
                    'Decision': 'Excluded',
                    ' Reason': 'Published before 2020 (Protocol 4.4)'
                })
            else:
                # NEW & RELEVANT DATE
                track_id = f"O_ISAC_{current_id:03d}"
                
                # Format Authors
                formatted_authors = format_authors(authors_raw)
                
                # Category Heuristic
                cat_text = (title + " " + str(row.get('Author Keywords', ''))).lower()
                category = "WIRELESS"
                if any(x in cat_text for x in ['fiber', 'fibre', 'cable', 'wired', 'pon', 'optical network']):
                    category = "FIBER"
                
                # Add to Candidates List
                new_candidates.append({
                    'Track_ID': track_id,
                    'Document Title': title,
                    'Authors': formatted_authors,
                    'Publication Title': venue,
                    'Publication Year': year,
                    'DOI': doi,
                    'CATEGORY': category
                })
                
                # Add to Screening Log
                screening_entries.append({
                    'Date': '2025-12-28',
                    'Title': title,
                    'Year': year,
                    'DOI': doi,
                    'Decision': 'Unscreened',
                    ' Reason': f'Scopus New (ID: {track_id})'
                })
                
                current_id += 1
            
            # Update known sets for subsequent iterations (even if excluded, we don't want to process again)
            if norm_doi: existing_dois.add(norm_doi)
            if norm_title: existing_titles.add(norm_title)

    # 3. Output Results
    print(f"--- Processing Complete ---")
    print(f"Duplicates: {duplicates_found}")
    print(f"New Candidates (2020+): {len(new_candidates)}")
    
    if new_candidates:
        pd.DataFrame(new_candidates).to_csv(OUTPUT_CANDIDATES, index=False)
        print(f"SAVED: {OUTPUT_CANDIDATES}")
        
    if screening_entries:
        # Match screening log columns: Date,Title,Year,DOI,Decision, Reason
        # Ensure column order matches exactly the file on disk associated with screening_log keys
        
        # Note: The keys in dict must match CSV headers.
        # Based on view_file: Date,Title,Year,DOI,Decision, Reason
        pd.DataFrame(screening_entries).to_csv(OUTPUT_SCREENING_ENTRIES, index=False)
        print(f"SAVED: {OUTPUT_SCREENING_ENTRIES} (Append these to your main log)")

if __name__ == "__main__":
    main()
