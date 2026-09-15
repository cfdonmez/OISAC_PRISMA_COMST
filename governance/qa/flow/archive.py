"""Freeze the pre-revision compile source and PDF without changing the old checkout."""
from pathlib import Path
import hashlib, json, zipfile

root = Path(__file__).resolve().parents[3]
base = root.parent / 'comst-v3-20260906'
out = root / 'archive'
out.mkdir(exist_ok=True)
selected = sorted(p for p in (base/'manuscript').rglob('*') if p.is_file()
                  and p.suffix.lower() in {'.tex','.bib','.pdf','.png','.svg','.md'})
selected += [base/'output/pdf/review.pdf', base/'supplement/methods.md',
             base/'supplement/index.md', base/'handoff/state.md']
manifest = {'commit':'0d5d6f869336266fde80d8e9ad829108c29b1c7e',
            'branch':'rev/comst-v3-20260906','pages':29,'files':{}}
with zipfile.ZipFile(out/'base.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in selected:
        rel=p.relative_to(base).as_posix()
        data=p.read_bytes()
        manifest['files'][rel]=hashlib.sha256(data).hexdigest()
        z.writestr(rel,data)
    z.writestr('baseline.json',json.dumps(manifest,indent=2))
(out/'base.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps({'archive':str(out/'base.zip'),'files':len(selected),
                  'bytes':(out/'base.zip').stat().st_size,
                  'pdf_sha256':manifest['files']['output/pdf/review.pdf']}))
