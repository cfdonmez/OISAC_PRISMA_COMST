
import pandas as pd
import os

# Paths
base_dir = r'c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST'
csv_path = os.path.join(base_dir, 'analysis/ph1_scr/included_studies_list.csv')
pdf_dir = os.path.join(base_dir, 'data/ret_docs')
output_md = os.path.join(base_dir, 'analysis/ph2_ext/pdf_download_todo.md')

# Ensure PDF Dir exists
os.makedirs(pdf_dir, exist_ok=True)

try:
    # Load Data
    if not os.path.exists(csv_path):
        print(f"❌ Error: {csv_path} not found.")
        exit()
        
    df = pd.read_csv(csv_path)
    existing_pdfs = set(os.listdir(pdf_dir))
    
    # Exclude files that are not pdfs from check if needed, but existing_pdfs is just listdir
    
    # 2. Find Missing
    missing = []
    found_count = 0
    
    print(f"🔍 Checking {len(df)} studies against {len(existing_pdfs)} existing files...")
    
    for _, row in df.iterrows():
        track_id = str(row['Track_ID']).strip()
        expected_pdf = f'{track_id}.pdf'
        
        if expected_pdf in existing_pdfs:
            found_count += 1
        else:
            # Create DOI Link
            doi = str(row['DOI']).strip()
            if doi and doi.lower() != 'nan':
                if 'doi.org' in doi:
                    link = doi
                else:
                    link = f'https://doi.org/{doi}'
            else:
                link = 'No DOI Available'
            
            missing.append({
                'ID': track_id,
                'Title': row['Title'],
                'Link': link
            })
    
    # 3. Generate Markdown
    if missing:
        md_content = '# 📥 PDF Download Checklist\n\n'
        md_content += f'**Durum:** {found_count} Mevcut | {len(missing)} Eksik\n'
        md_content += '**Hedef Klasör:** `data/ret_docs`\n'
        md_content += '**Format:** `O_ISAC_XXX.pdf`\n\n'
        md_content += '| Download Status | Track ID | Title | DOI Link |\n'
        md_content += '|---|---|---|---|\n'
        
        for item in missing:
            title = str(item['Title']).replace('|', '-').strip()
            if len(title) > 100: title = title[:97] + '...'
            
            # Format: [ ] O_ISAC_XXX | Title | [Open](Link)
            md_content += f"| [ ] | **{item['ID']}** | {title} | [Open Link]({item['Link']}) |\n"
            
        with open(output_md, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f'✅ Generated checklist with {len(missing)} missing items at: {output_md}')
    else:
        print('🎉 No missing PDFs! All up to date.')
        # Write a dummy success file or clear the todo
        with open(output_md, 'w', encoding='utf-8') as f:
            f.write('# ✅ All PDFs Retrieved!\n\nNo missing files detected.')

except Exception as e:
    print(f"❌ Error: {e}")
