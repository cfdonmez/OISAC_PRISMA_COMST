"""Read-only verification of the transferred project; Python standard library."""
from pathlib import Path
import hashlib
import json
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def resolve_local(base, value):
    path = (base / unquote(value).replace('\\', '/')).resolve()
    if not path.is_relative_to(ROOT):
        errors.append(f'Path outside repository: {value}')
    return path

manifest = json.loads((ROOT / 'handoff/files.json').read_text(encoding='utf-8'))
for row in manifest:
    p = resolve_local(ROOT, row['path'])
    if not p.is_file() or digest(p) != row['sha256']:
        errors.append('Missing or changed transferred snapshot: ' + row['path'])

frozen = ROOT / 'supplement/v10'
frozen_count = 0
for line in (frozen / 'SUPPLEMENT_SHA256_2026-08-17.txt').read_text(encoding='utf-8-sig').splitlines():
    if not line.strip():
        continue
    sha, name = line.split(maxsplit=1)
    p = resolve_local(frozen, name.lstrip('*'))
    frozen_count += 1
    if not p.is_file() or digest(p).lower() != sha.lower():
        errors.append('Frozen manifest mismatch: ' + name)

qa = json.loads((ROOT / 'governance/qa/review/result.json').read_text(encoding='utf-8'))
pdf = ROOT / 'output/pdf/review.pdf'
if not pdf.exists() or digest(pdf) != qa['sha256']:
    errors.append('Current reading copy does not match recorded QA hash')

entry = ROOT / 'manuscript/main.tex'
visited = set()
def inspect_tex(p):
    if p in visited:
        return
    visited.add(p)
    if not p.is_file():
        errors.append('Missing TeX source: ' + str(p.relative_to(ROOT)))
        return
    text = re.sub(r'(?<!\\)%[^\n]*', '', p.read_text(encoding='utf-8-sig'))
    for m in re.finditer(r'\\(input|includegraphics|bibliography)(?:\[[^\]]*\])?\{([^}]+)\}', text):
        kind, value = m.groups()
        for name in value.split(','):
            target = resolve_local(ROOT / 'manuscript', name.strip())
            if kind == 'bibliography' and target.suffix != '.bib':
                target = target.with_suffix('.bib')
            if kind == 'input' and not target.suffix:
                target = target.with_suffix('.tex')
            if not target.exists():
                errors.append('Missing build input: ' + str(target.relative_to(ROOT)))
            elif kind == 'input':
                inspect_tex(target)
inspect_tex(entry)

docs = ['README.md', 'AGENTS.md', 'README_V3_WORKING_DRAFT.md',
        'handoff/state.md', 'handoff/index.md', 'supplement/index.md',
        'supplement/methods.md', 'governance/review.md', 'governance/s3a.md']
link_count = 0
for doc in docs:
    p = ROOT / doc
    for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
        if re.match(r'^(https?://|mailto:|#)', link):
            continue
        target = link.split('#')[0].strip('<>')
        if re.match(r'^[A-Za-z]:', target):
            errors.append(f'Nonportable active link in {doc}: {target}')
        elif target:
            link_count += 1
            if not resolve_local(p.parent, target).exists():
                errors.append(f'Broken active link in {doc}: {target}')

print(json.dumps({'status': 'PASS' if not errors else 'FAIL',
                  'snapshot_files': len(manifest), 'frozen_manifest_entries': frozen_count,
                  'tex_sources': len(visited), 'active_local_links': link_count,
                  'reading_pdf_sha256': digest(pdf) if pdf.exists() else None,
                  'errors': errors}, ensure_ascii=False, indent=2))
sys.exit(bool(errors))
