"""Preserve user-supplied PDFs and extract page-addressable local reading material."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
from pypdf import PdfReader

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parents[1]
POPPLER = Path(r'C:/Users/fatih/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin')
PAPERS = [('P01', '1.pdf'), ('P02', '2.pdf')]

def dump(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

catalog = []
for paper_id, filename in PAPERS:
    source = Path(r'C:/Users/fatih/Downloads') / filename
    directory = ROOT / paper_id
    directory.mkdir(exist_ok=True)
    pdf = directory / filename
    if pdf.exists() and sha(pdf) != sha(source):
        raise RuntimeError(f'Destination differs: {pdf}')
    if not pdf.exists():
        shutil.copy2(source, pdf)
    assert sha(source) == sha(pdf)
    reader = PdfReader(pdf)
    for layout, outname in [(False, 'fulltext.txt'), (True, 'fulltext_layout.txt')]:
        command = [shutil.which('pdftotext') or str(POPPLER / 'pdftotext.exe'), '-enc', 'UTF-8']
        if layout:
            command.append('-layout')
        subprocess.run(command + [str(pdf), str(directory / outname)], check=True)
    page_texts = (directory / 'fulltext.txt').read_text(encoding='utf-8').split('\f')
    if not page_texts[-1].strip():
        page_texts.pop()
    assert len(page_texts) == len(reader.pages), (paper_id, len(page_texts), len(reader.pages))
    pages = []
    links = []
    for index, (page, content) in enumerate(zip(reader.pages, page_texts), 1):
        pages.append({'paper_id': paper_id, 'pdf_page': index, 'text': content.strip(), 'characters': len(content.strip())})
        for ref in page.get('/Annots', []):
            annotation = ref.get_object()
            action = annotation.get('/A')
            if action:
                action = action.get_object()
                if action.get('/URI'):
                    links.append({'pdf_page': index, 'uri': str(action['/URI'])})
    (directory / 'pages.jsonl').write_text(''.join(json.dumps(p, ensure_ascii=False) + '\n' for p in pages), encoding='utf-8')
    (directory / 'reading_text.md').write_text('\n\n'.join(f'## PDF page {p["pdf_page"]}\n\n{p["text"]}' for p in pages) + '\n', encoding='utf-8')
    metadata = {'paper_id': paper_id, 'source_path': str(source), 'archive_path': str(pdf), 'filename': filename,
                'sha256': sha(pdf), 'bytes': pdf.stat().st_size, 'page_count': len(reader.pages),
                'pdf_metadata': {str(k): str(v) for k, v in (reader.metadata or {}).items()},
                'embedded_attachment_names': list(reader.attachments.keys()),
                'extraction': {'tool': 'Poppler pdftotext', 'variants': ['reading_order', 'layout'],
                               'all_pages_have_text': all(p['characters'] > 0 for p in pages),
                               'note': 'Automatic extraction; equations, table alignment and ligatures require PDF visual checking. Raw experimental data availability must not be inferred from PDF text.'}}
    dump(directory / 'metadata.json', metadata)
    dump(directory / 'pdf_links.json', links)
    catalog.append(metadata)
    renders = directory / 'rendered_pages'
    renders.mkdir(exist_ok=True)
    subprocess.run([str(POPPLER / 'pdftoppm.exe'), '-r', '90', '-png', str(pdf), str(renders / 'page')], check=True, capture_output=True)
    print(json.dumps({'paper_id': paper_id, 'pages': len(pages), 'sha256_copy_verified': True,
                      'render_count': len(list(renders.glob('page-*.png'))), 'attachments': metadata['embedded_attachment_names']}, ensure_ascii=False))
dump(ROOT / 'source_manifest.json', catalog)
