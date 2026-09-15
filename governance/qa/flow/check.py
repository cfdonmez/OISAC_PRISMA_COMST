"""Check build evidence, units, citations and the comparison baseline."""
from pathlib import Path
from collections import Counter
import csv, hashlib, json, re, subprocess, zipfile
from pypdf import PdfReader

root=Path(__file__).resolve().parents[3]
qa=root/'governance/qa/flow'
errors=[]
bodylist=(root/'manuscript/MANUSCRIPT_BODY_INPUTS.tex').read_text(encoding='utf-8')
paths=[root/'manuscript'/x for x in re.findall(r'\\input\{([^}]+)\}',bodylist)]
text='\n'.join(p.read_text(encoding='utf-8') for p in paths)
old='\n'.join(subprocess.check_output(['git','show','0d5d6f8:'+p.relative_to(root).as_posix()],cwd=root).decode('utf-8') for p in paths)
def citations(s):
    return set(k.strip() for v in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',s) for k in v.split(','))
def countwords(s):
    s=re.sub(r'(?<!\\)%[^\n]*','',s)
    s=re.sub(r'\\(?:cite|ref|label|includegraphics)(?:\[[^\]]*\])?\{[^}]*\}','',s)
    s=re.sub(r'\\[a-zA-Z]+',' ',s)
    return len(re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*",s))
def readcsv(p):
    return list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))

units={}
for name,rel,n in [('studies','st01/ST01_INCLUDED_STUDIES_206.csv',206),
                   ('reports','st01/ST01_ELIGIBLE_REPORT_LINEAGE_227.csv',227),
                   ('metrics','evidence/ST-19_PRIMARY_METRIC_RESULTS_4779.csv',4779),
                   ('relationships','evidence/ST-19_SUBSTANTIVE_TRADEOFFS_402.csv',402),
                   ('tradeoff_records','evidence/ST-19_GOVERNED_TRADEOFFS_404.csv',404),
                   ('appraisals','evidence/ST-18_STUDY_LEVEL_TQAF_206.csv',206),
                   ('field_studies','s7/S7_PAIRED_FUNCTION_VALIDATION_12.csv',12)]:
    units[name]=len(readcsv(root/'supplement/v10'/rel))
    if units[name]!=n: errors.append(f'{name}: {units[name]} != {n}')
sel={'retrieved':1733-472-2,'screened':1259-864-61-2,
     'reports_sought':332-2,'assessed':330-58,'eligible':272-39-6,
     'studies':227-21,'context':61+6}
if list(sel.values())!=[1259,332,330,272,227,206,67]: errors.append('Selection arithmetic')

with zipfile.ZipFile(root/'archive/base.zip') as z:
    if z.testzip(): errors.append('Baseline ZIP CRC failure')
    baseline=json.loads(z.read('baseline.json'))
    for p,h in baseline['files'].items():
        if hashlib.sha256(z.read(p)).hexdigest()!=h: errors.append('Baseline archive hash: '+p)

allbib='\n'.join(p.read_text(encoding='utf-8-sig') for p in (root/'manuscript').glob('*.bib'))
bibkeys=set(re.findall(r'@\w+\s*\{\s*([^,\s]+)',allbib))
missing=sorted(citations(text)-bibkeys)
if missing: errors.append('Missing citations: '+','.join(missing))
labels=re.findall(r'\\label\{([^}]+)\}',text)
duplicates=[k for k,v in Counter(labels).items() if v>1]
if duplicates: errors.append('Duplicate labels: '+','.join(duplicates))
refs=set(re.findall(r'\\ref\{([^}]+)\}',text))
if refs-set(labels): errors.append('Missing references: '+','.join(sorted(refs-set(labels))))
for stale in ['fig:oisac_platform_overview','fig:integration_map','fig:tradeoff_profile',
              'fig:technology_application_chain','fig:bandwidth_resolution','fig:tqaf_profile']:
    if stale in refs: errors.append('Removed figure still referenced: '+stale)
if re.search(r'118.{0,90}(?:supported bounded|verified cross-study)',text,re.I):
    errors.append('118 incorrectly characterized')
for p in paths:
    if '\\includegraphics' in p.read_text():
        for asset in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',p.read_text()):
            if not (root/'manuscript'/asset).exists(): errors.append('Missing asset: '+asset)

pdfs={}
for name,src in [('flow','manuscript/main.pdf'),('profiles','supplement/driver.pdf')]:
    p=root/src
    if not p.exists(): errors.append('Missing PDF '+src); continue
    reader=PdfReader(p)
    pages=[p.extract_text() or '' for p in reader.pages]
    if any(len(t.strip())<20 for t in pages): errors.append('Near-empty page '+name)
    log=p.with_suffix('.log').read_text(encoding='utf-8',errors='replace')
    problems=[line for line in log.splitlines() if re.search(r'undefined|multiply defined|Missing character|Overfull|^!',line,re.I)]
    if problems: errors.extend([name+': '+x for x in problems])
    out=root/'output/pdf'/f'{name}.pdf'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_bytes(p.read_bytes())
    pdfs[name]={'pages':len(reader.pages),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
                'underfull_warnings':log.count('Underfull'),
                'section_pages':{str(i+1): [l for l in t.splitlines() if re.match(r'^(?:I|II|III|IV|V|VI|VII|VIII)\.',l)] for i,t in enumerate(pages)},
                'references_start': next((i+1 for i,t in enumerate(pages) if re.search(r'R\s*E\s*F\s*E\s*R\s*E\s*N\s*C\s*E\s*S',t)),None)}
if 'flow' in pdfs and not 20<=pdfs['flow']['pages']<=30: errors.append('Main PDF outside 20-30 page target')

visual={}
for name,rel in [('flow','paper/visual_checks.json'),('profiles','profiles_checks.json')]:
    p=qa/rel
    if p.exists():
        v=json.loads(p.read_text(encoding='utf-8'))
        match=v.get('pdf_sha256')==pdfs.get(name,{}).get('sha256')
        visual[name]={'hash_matches':match,'record':rel,
                      'no_clipping_or_collision':not v.get('observed_clipping_or_collision',True)}
        if not match: errors.append(name+': visual review hash does not match current PDF')
        if v.get('observed_clipping_or_collision',True): errors.append(name+': visual defect flagged')
    else:
        visual[name]={'status':'pending'}
        errors.append(name+': final visual record is missing')

inputs=set(paths+[root/'manuscript/main.tex',root/'manuscript/MANUSCRIPT_BODY_INPUTS.tex'])
inputs.update((root/'manuscript').glob('*.bib'))
inputs.update((root/'supplement').glob('*.tex'))
for p in list(inputs):
    if p.suffix=='.tex':
        base=root/'supplement' if p.parent==root/'supplement' else root/'manuscript'
        for asset in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',p.read_text()):
            inputs.add((base/asset).resolve())

result={'status':'PASS' if not errors else 'FAIL','baseline_commit':baseline['commit'],
        'baseline_pages':29,'baseline_files':len(baseline['files']), 'pdfs':pdfs,
        'approx_words_before':countwords(old),'approx_words_after':countwords(text),
        'words_by_source':{p.name:countwords(p.read_text()) for p in paths},
        'sections':len(re.findall(r'\\section\{',text)),
        'figures':len(re.findall(r'\\begin\{figure\*?\}',text)),
        'tables':len(re.findall(r'\\begin\{table\*?\}',text)),
        'citations_before':len(citations(old)),'citations_after':len(citations(text)),
        'citations_removed':sorted(citations(old)-citations(text)),
        'citations_added':sorted(citations(text)-citations(old)),
        'frozen_units':units,'selection_arithmetic':sel,'errors':errors,
        'visual_review':visual,
        'build_inputs':{p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(inputs)}}
(qa/'result.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['citations_removed','pdfs']},indent=2))
print(json.dumps(pdfs,indent=2))
raise SystemExit(bool(errors))
