import os
import re
import requests
import json
import time

# Configuration
BASE_DIR = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\processed_markdowns"
BIB_FILE = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\references.bib"
LOG_FILE = r"c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\bib_log.json"

def extract_title(md_path):
    """Extracts the title from the markdown file (usually the first # line)."""
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('#'):
                    # Remove #, **, and leading/trailing whitespace
                    title = re.sub(r'#+\s*', '', line)
                    title = re.sub(r'\*\*+', '', title)
                    return title.strip()
    except Exception as e:
        print(f"Error reading {md_path}: {e}")
    return None

def get_doi_from_crossref(title):
    """Searches CrossRef for a DOI given a title."""
    url = "https://api.crossref.org/works"
    params = {
        "query.title": title,
        "rows": 1
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            items = data.get('message', {}).get('items', [])
            if items:
                item = items[0]
                # Basic validation: check if title is similar (optional but good)
                return item.get('DOI')
    except Exception as e:
        print(f"Error searching CrossRef for '{title}': {e}")
    return None

def get_bibtex_from_doi(doi):
    """Fetches BibTeX from doi.org using content negotiation."""
    url = f"https://doi.org/{doi}"
    headers = {"Accept": "application/x-bibtex"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text.strip()
    except Exception as e:
        print(f"Error fetching BibTeX for DOI {doi}: {e}")
    return None

def run():
    processed_folders = [f for f in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, f)) and f.startswith('O_ISAC')]
    processed_folders.sort()
    
    # Load existing log to skip already fetched ones (if any)
    results_log = {}
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            results_log = json.load(f)

    with open(BIB_FILE, 'a', encoding='utf-8') as bib_out:
        for folder in processed_folders:
            if folder in results_log and results_log[folder].get('status') == 'success':
                continue
            
            if folder == 'O_ISAC_001': # Already done manually
                continue

            md_file = os.path.join(BASE_DIR, folder, f"{folder}.md")
            if not os.path.exists(md_file):
                # Fallback: check if it's nested (saw data\processed_markdowns\O_ISAC_001\O_ISAC_001\O_ISAC_001.md in find_by_name)
                md_file = os.path.join(BASE_DIR, folder, folder, f"{folder}.md")
                if not os.path.exists(md_file):
                    print(f"Skipping {folder}: Markdown file not found.")
                    continue

            print(f"Processing {folder}...")
            title = extract_title(md_file)
            if not title:
                print(f"Could not extract title for {folder}")
                results_log[folder] = {"status": "error", "error": "No title found"}
                continue

            print(f"  Title: {title}")
            doi = get_doi_from_crossref(title)
            if doi:
                print(f"  DOI Found: {doi}")
                bibtex = get_bibtex_from_doi(doi)
                if bibtex:
                    # Replace the generated bib-key with our O_ISAC_xxx ID
                    # Regex to find @type{KEY,
                    bibtex = re.sub(r'(@\w+\{)[^,]+', rf'\1{folder}', bibtex, count=1)
                    
                    bib_out.write(f"\n% ============================================\n")
                    bib_out.write(f"% {folder}\n")
                    bib_out.write(f"% ============================================\n")
                    bib_out.write(bibtex + "\n")
                    bib_out.write("\n")
                    bib_out.flush()
                    
                    results_log[folder] = {"status": "success", "doi": doi, "title": title}
                    print(f"  Successfully added to BibTeX.")
                else:
                    print(f"  Could not get BibTeX for DOI {doi}")
                    results_log[folder] = {"status": "error", "error": "BibTeX fetch failed", "doi": doi, "title": title}
            else:
                print(f"  DOI not found on CrossRef.")
                results_log[folder] = {"status": "error", "error": "DOI not found", "title": title}
            
            # Simple rate limiting for API courtesy
            time.sleep(1)
            
            # Save log periodically
            with open(LOG_FILE, 'w', encoding='utf-8') as f:
                json.dump(results_log, f, indent=2)

    print("\nTask complete. Check data/references.bib and data/bib_log.json")

if __name__ == "__main__":
    run()
