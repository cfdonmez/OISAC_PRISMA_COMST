"""Count current manuscript prose without changing its source. Requires TeXcount."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess

ROOT = Path(r'C:\OISAC\worktrees\comst-v3-20260906\manuscript\sections')
OUT = Path(__file__).resolve().parent
names = ['01_INTRODUCTION.tex', '02_FOUNDATIONS_AND_COMPARISON_FRAMEWORK.tex']
records = []
for name in names:
    path = ROOT / name
    proc = subprocess.run([shutil.which('texcount'), '-utf8', '-sub', str(path)],
                          capture_output=True, text=True, encoding='utf-8', errors='replace')
    if proc.returncode:
        raise RuntimeError(proc.stdout + proc.stderr)
    (OUT / (path.stem + '_texcount.txt')).write_text(proc.stdout, encoding='utf-8')
    record = {'file': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
    for key, pattern in [('body_words', r'Words in text: (\d+)'),
                         ('heading_words', r'Words in headers: (\d+)'),
                         ('caption_words', r'Words outside text \(captions, etc\.\): (\d+)'),
                         ('display_equations', r'Number of math displayed: (\d+)'),
                         ('float_count', r'Number of floats/tables/figures: (\d+)')]:
        match = re.search(pattern, proc.stdout)
        if not match:
            raise ValueError(f'Missing {key}: {proc.stdout}')
        record[key] = int(match.group(1))
    record['subcounts'] = [
        {'body_words': int(m[0]), 'heading_words': int(m[1]), 'caption_words': int(m[2]), 'title': m[3]}
        for m in re.findall(r'^\s+(\d+)\+(\d+)\+(\d+) \([^\n]+\) (.+)$', proc.stdout, re.M)
    ]
    records.append(record)
(OUT / 'current_counts.json').write_text(json.dumps({
    'method': 'TeXcount -utf8 -sub. Prose, headings and captions reported separately; excludes equations, tabular cell text, and imported figure labels. External Markdown/OCR counts use different extraction and are approximate; do not interpret small numeric differences.',
    'records': records
}, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(records, indent=2))
