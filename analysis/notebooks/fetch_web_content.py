# =============================================================================
# WEB TO MARKDOWN CONVERTER (Prototype)
# =============================================================================
# Purpose: Convert saved HTML files (IEEE Xplore) to O-ISAC Markdown format
# Usage: 
#   1. Save the article webpage as "Complete Webpage" (HTML)
#   2. Place it in 'data/temp_html/'
#   3. Run this script to generate formatting for V4 Pipeline
# =============================================================================

import os
import sys
from bs4 import BeautifulSoup
import markdownify
import re

# Project Paths
PROJECT_ROOT = "/Users/bastt/Library/CloudStorage/GoogleDrive-cfdonmez@gmail.com/My Drive/AKU_WorkSpace/survey_fdgit/OISAC_PRISMA_COMST"
TEMP_HTML_DIR = os.path.join(PROJECT_ROOT, "data/temp_html")
OUTPUT_MD_DIR = os.path.join(PROJECT_ROOT, "data/processed_markdowns")

def convert_html_to_md(paper_id):
    """Converts a specific paper's HTML to Markdown."""
    
    html_path = os.path.join(TEMP_HTML_DIR, f"{paper_id}.html")
    
    if not os.path.exists(html_path):
        print(f"❌ HTML file not found: {html_path}")
        print("   Please save the webpage as '[Paper_ID].html' in data/temp_html/")
        return

    print(f"🔨 Converting {paper_id}...")
    
    with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # --- IEEE Xplore Specific Cleaning ---
    # Try to find the main article content (this selector varies by site)
    # Generic approach: Remove navbars, footers
    for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
        tag.decompose()
        
    # Get text
    html_content = str(soup)
    md_content = markdownify.markdownify(html_content, heading_style="ATX")
    
    # --- Post-Processing ---
    # Remove excessive newlines
    md_content = re.sub(r'\n\s*\n', '\n\n', md_content)
    
    # --- Save to Target Structure ---
    target_folder = os.path.join(OUTPUT_MD_DIR, paper_id)
    os.makedirs(target_folder, exist_ok=True)
    
    target_file = os.path.join(target_folder, f"{paper_id}.md")
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(f"# {paper_id} (Web Scraped)\n\n")
        f.write(md_content)
        
    print(f"✅ Saved to: {target_file}")
    
    # Create empty image folder to satisfy V4 structure
    os.makedirs(os.path.join(target_folder, paper_id), exist_ok=True)
    print("✅ Created structure for V4 pipeline compatibility.")

if __name__ == "__main__":
    # Create temp dir if not exists
    os.makedirs(TEMP_HTML_DIR, exist_ok=True)
    print(f"📂 Temp HTML Directory: {TEMP_HTML_DIR}")
    
    if len(sys.argv) > 1:
        target_id = sys.argv[1]
        convert_html_to_md(target_id)
    else:
        print("ℹ️ Usage: python fetch_web_content.py O_ISAC_XXX")
