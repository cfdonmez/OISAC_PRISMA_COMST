
import pandas as pd

try:
    df = pd.read_csv('analysis/phase1_screening/ai_screening_decisions_scopus.csv')
    included = df[df['Decision'] == 'Included']
    
    md_content = '# 🤖 AI-Screened Included Candidates (Scopus)\n\n'
    md_content += f'**Total Included:** {len(included)}\n\n'
    md_content += '| Track ID | Title | Confidence | Reason |\n'
    md_content += '|---|---|---|---|\n'
    
    for _, row in included.iterrows():
        title = str(row['Title']).replace('|', '-') # Escape pipes for markdown table
        reason = str(row['Reason']).replace('|', '-')
        md_content += f"| {row['Track_ID']} | {title} | {row.get('Confidence', 'N/A')} | {reason} |\n"
    
    output_path = 'analysis/phase1_screening/ai_included_candidates.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    print(f'✅ Summary report generated at {output_path}')
    
except Exception as e:
    print(f'❌ Error: {e}')
