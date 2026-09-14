"""Read-only corpus inventory and approximate narrative counts.
Excludes headings, table rows, figure/table captions, image markup, citations,
display/inline math, equation-only numbers. COMST_067's extracted outline figure
text (lines 135-189) is manually excluded. Counts are approximate OCR prose words,
not texcount and not an editorial standard. Never modifies source documents.
"""
from pathlib import Path
import re, json, html

BASE = Path(r'C:\GH\OISAC_PRISMA_COMST\data\corp_std')
OUT = Path(r'C:\OISAC\outputs\SECTION2_KARSILASTIRMA_2026-09-07')
SELECTED = {'014':(101,149),'026':(113,263),'044':(127,243),'054':(197,232),'067':(123,272),'073':(53,167)}
FIRST = {'014':103,'026':115,'044':131,'054':199,'067':125,'073':57}

def strip_tags(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s))

def clean(lines, id='', start=1):
    kept=[]
    for i,s in enumerate(lines,start):
        if id=='067' and (135<=i<=189 or 232<=i<=234): continue
        s=strip_tags(s).strip()
        if not s or s.startswith('|') or s.startswith('#'): continue
        if re.match(r'^(?:Fig\.?|Figure|TABLE)\s*[IVX\d]',s,re.I): continue
        if s.startswith('!['): continue
        if re.fullmatch(r'\(?\d+\)?',s): continue
        # Remove inline descriptive labels preceding substantive text.
        s=re.sub(r'^[-•]?\s*\*[^*]+\*:\s*','',s)
        kept.append(s)
    s='\n'.join(kept)
    s=re.sub(r'\$\$[\s\S]*?\$\$', ' ', s)
    s=re.sub(r'\$[^$\n]*\$', ' ', s)
    s=re.sub(r'\[\\\[[^\]]+\\\]\]\([^)]*\)', ' ', s)
    s=re.sub(r'\[([^]]*)\]\([^)]*\)',r'\1',s)
    s=re.sub(r'\[(?:\d+[,\s–-]*)+\]', ' ', s)
    return s

def wc(s):
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'’][A-Za-z0-9]+)*",s))

inventory=[]; selected=[]
for path in sorted(BASE.glob('COMST_*/*.md')):
    lines=path.read_text(encoding='utf-8-sig').splitlines()
    title=next((strip_tags(s).lstrip('# ').strip() for s in lines if s.startswith('# ')), '')
    match=next(((i,strip_tags(s).lstrip('# ').strip()) for i,s in enumerate(lines,1) if re.match(r'^II\.\s',strip_tags(s).lstrip('# ').strip())),(None,''))
    inventory.append({'id':path.stem,'title':title,'section_ii_line':match[0],'section_ii':match[1],'file':str(path)})
    id=path.stem[-3:]
    if id not in SELECTED: continue
    a,b=SELECTED[id]
    body=clean(lines[a-1:b],id,a)
    first=clean([lines[FIRST[id]-1]],id,FIRST[id])
    selected.append({'id':path.stem,'title':title,'start_line':a,'end_line':b,'body_words_approx':wc(body),'first_paragraph_line':FIRST[id],'first_paragraph_words_approx':wc(first),'file':str(path)})

OUT.mkdir(parents=True,exist_ok=True)
(OUT/'std_structure_inventory.json').write_text(json.dumps(inventory,indent=2,ensure_ascii=False),encoding='utf-8')
(OUT/'std_structure_counts.json').write_text(json.dumps(selected,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'count':len(inventory),'selected':selected},indent=2,ensure_ascii=False))
