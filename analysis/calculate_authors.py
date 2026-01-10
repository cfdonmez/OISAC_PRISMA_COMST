import json
import os
import re

def count_authors_in_line(line):
    # Keep the text inside the brackets of links: [name part](link) -> name part
    line = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', line)
    
    # Remove IEEE membership titles and other tags
    line = re.sub(r'<sup>.*?</sup>', '', line)
    line = re.sub(r'(Senior\s+)?Member,\s+IEEE', '', line, flags=re.IGNORECASE)
    line = re.sub(r'Fellow,\s+IEEE', '', line, flags=re.IGNORECASE)
    line = re.sub(r'Life\s+Fellow,\s+IEEE', '', line, flags=re.IGNORECASE)
    line = re.sub(r'Student\s+Member,\s+IEEE', '', line, flags=re.IGNORECASE)
    line = re.sub(r'Graduate\s+Student\s+Member', '', line, flags=re.IGNORECASE)
    line = re.sub(r'\(Corresponding author:.*?\)', '', line, flags=re.IGNORECASE)
    line = re.sub(r'\*.*?\*', '', line) # Remove italics
    
    # Remove stray brackets or icons
    line = line.replace('®', '')
    
    # Split by "and" or commas
    # We should be careful about commas in designations like "Member, IEEE"
    # But those are removed now.
    parts = re.split(r',\s*and\s+|\s+and\s+|,', line)
    
    # Clean up names
    names = []
    # Exclusion list for non-name strings
    exclude = ['graduate', 'student', 'corresponding', 'author', 'ieee', 'fellow', 'member', 'senior', 'life']
    
    for p in parts:
        name = p.strip().strip('*').strip()
        # Filter out obvious non-names or noise
        if name and len(name) > 3:
            # Check if name is just a designation that survived
            name_lower = name.lower()
            if not any(x in name_lower for x in exclude):
                names.append(name)
    return names

def analyze_authors():
    manifest_path = r'c:\Users\fatih\gdrive\AKU_WorkSpace\survey_fdgit\OISAC_PRISMA_COMST\data\corpus_manifest.json'
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)
    
    results = []
    
    for paper in manifest:
        paper_id = paper['paper_id']
        if not paper_id.startswith('COMST_'):
            continue
            
        md_path = paper['md_path']
        if not os.path.exists(md_path):
            continue
            
        with open(md_path, 'r', encoding='utf-8') as f:
            # Read first 15 lines
            lines = [f.readline() for _ in range(15)]
            
        # The author line is usually after the # Title
        author_line = ""
        for i, line in enumerate(lines):
            line_clean = line.strip()
            if not line_clean or line_clean.startswith('#') or line_clean.startswith('---'):
                continue
            
            # Author lines usually have multiple names/commas and IEEE keywords
            # Or if they are on line 3-6
            if i > 1 and i < 8 and (',' in line or 'and' in line or 'Member' in line):
                author_line = line
                break
        
        if author_line:
            names = count_authors_in_line(author_line)
            if names:
                results.append({
                    'id': paper_id,
                    'count': len(names),
                    'authors': names,
                    'raw': author_line.strip()
                })
            
    if not results:
        print("No authors found.")
        return

    counts = [r['count'] for r in results]
    avg = sum(counts) / len(counts)
    counts.sort()
    median = counts[len(counts)//2]
    
    print(f"Total Papers: {len(results)}")
    print(f"Average Authors: {avg:.2f}")
    print(f"Median Authors: {median}")
    print(f"Min Authors: {min(counts)}")
    print(f"Max Authors: {max(counts)}")
    
    # Sample output for verification
    print("\nSample (First 5):")
    for r in results[:5]:
        print(f"{r['id']}: {r['count']} authors ({', '.join(r['authors'][:3])}...)")

if __name__ == "__main__":
    analyze_authors()
