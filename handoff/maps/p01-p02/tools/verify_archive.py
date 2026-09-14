from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
from pypdf import PdfReader
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
json_files=list(ROOT.rglob('*.json'))
for p in json_files:
    json.loads(p.read_text(encoding='utf-8'))
checks.append({'check':'json_parse','status':'PASS','files':len(json_files)})
for paper,filename,expected_pages,expected_refs,tables,figures in [('P01','1.pdf',35,248,7,14),('P02','2.pdf',37,174,10,25)]:
    d=ROOT/paper
    src=Path(r'C:/Users/fatih/Downloads')/filename
    dest=d/filename
    assert digest(src)==digest(dest)
    assert len(PdfReader(dest).pages)==expected_pages
    pages=[json.loads(s) for s in (d/'pages.jsonl').read_text(encoding='utf-8').splitlines()]
    assert [p['pdf_page'] for p in pages]==list(range(1,expected_pages+1))
    assert all(p['text'].strip() for p in pages)
    renders=list((d/'rendered_pages').glob('page-*.png'))
    assert len(renders)==expected_pages
    for render in renders:
        with Image.open(render) as im: im.verify()
    numbers=set(map(int,re.findall(r'^\[(\d+)\]',(d/'references_pages.txt').read_text(encoding='utf-8'),re.M)))
    assert numbers==set(range(1,expected_refs+1))
    inventory=json.loads((d/'table_figure_inventory.json').read_text(encoding='utf-8'))['items']
    for kind,count in [('table',tables),('figure',figures)]:
        assert [i['number'] for i in inventory if i['kind']==kind]==list(range(1,count+1))
    for item in inventory:
        assert all(1<=p<=expected_pages for p in item['pdf_pages'])
        assert (d/item['source_render']).exists()
    evidence=json.loads((d/'structured_evidence.json').read_text(encoding='utf-8'))
    assert evidence['source_sha256']==digest(dest)
    assert all(1<=e['pdf_page']<=expected_pages for e in evidence['records'])
    assert (d/'OKUMA_NOTLARI.md').stat().st_size>10000
    checks.append(dict(check=paper,status='PASS',pdf_pages=expected_pages,text_pages=len(pages),readable_renders=len(renders),
                       references_numbered=expected_refs,tables=tables,figures=figures,source_copy_sha256_equal=True,sha256=digest(dest)))
experiment=json.loads((ROOT/'P02/EXPERIMENT_TABLES.json').read_text(encoding='utf-8'))
assert experiment['source_sha256']==digest(ROOT/'P02/2.pdf')
assert [len(t['rows']) for t in experiment['tables']]==[9,8,7]
for t in experiment['tables']:
    for row in t['rows']: assert set(row['cells'])==set(t['column_names'])
datasets=json.loads((ROOT/'P01/DATASET_CATALOGUE.json').read_text(encoding='utf-8'))['datasets']
assert len(datasets)==10
checks.append(dict(check='structured_tables',status='PASS',p02_rows=24,p01_dataset_rows=10))
badlinks=[]
for md in ROOT.glob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)',md.read_text(encoding='utf-8')):
        if '://' not in target and not (md.parent/target).exists() and target not in ['QA_REPORT.json','SHA256SUMS.txt']:
            badlinks.append({'file':md.name,'target':target})
assert not badlinks,badlinks
checks.append(dict(check='entrypoint_local_links',status='PASS'))
report=dict(status='PASS',checked_at_utc=datetime.now(timezone.utc).isoformat(),checks=checks,
    content_review={'P01':'Full text and references read; all numbered figure/table pages inspected by reading agent.',
                    'P02':'Full text and references read; key table/figure pages inspected; targeted independent notes QA completed and two wording refinements applied.',
                    'p02_tables_5_6_7':'All 24 rows visually transcribed and checked at 180 dpi.',
                    'p01_dataset_table':'All 10 rows read from raster table; source signs retained.'},
    boundaries=['Technical archive integrity is not independent verification of primary experiments.',
                'No external dataset or cited primary-paper download was performed.',
                'No human-review approval was recorded.',
                'Existing manuscript and frozen review data were not edited in this task.'])
(ROOT/'QA_REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
files=sorted(p for p in ROOT.rglob('*') if p.is_file() and p.name!='SHA256SUMS.txt')
entries=[f'{digest(p)}  {p.relative_to(ROOT).as_posix()}' for p in files]
(ROOT/'SHA256SUMS.txt').write_text('\n'.join(entries)+'\n',encoding='utf-8')
for line in (ROOT/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
    expected,relative=line.split('  ',1)
    assert digest(ROOT/relative)==expected
print(json.dumps(dict(status='PASS',manifest_files=len(files),pages=72,figures=39,tables=17,table_rows=24,dataset_rows=10),ensure_ascii=False))
