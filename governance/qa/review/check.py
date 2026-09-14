from pathlib import Path
from collections import Counter
import hashlib
import json
import re
import shutil
import subprocess
from pypdf import PdfReader

root = Path(__file__).resolve().parents[3]
qa = Path(__file__).resolve().parent
man = root / 'manuscript'
manifest = (man / 'MANUSCRIPT_BODY_INPUTS.tex').read_text(encoding='utf-8')
inputs = re.findall(r'\\input\{([^}]+)\}', manifest)
sources = {name: (man / name).read_text(encoding='utf-8') for name in inputs}
body = '\n'.join(sources.values())
labels = re.findall(r'\\label\{([^}]+)\}', body)
refs = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', body)
duplicates = [k for k, v in Counter(labels).items() if v > 1]
missing = sorted(set(refs) - set(labels))
sections = re.findall(r'^\\section\{([^}]+)\}', body, re.M)
intro = sources['sections/01_INTRODUCTION.tex']
order = re.findall(r'\\subsection\{([^}]+)\}', intro)
method = intro.split(r'\subsection{Review Methodology}', 1)[1].split(r'\subsection{Scope and Contributions}', 1)[0]
method = re.sub(r'\\begin\{figure\*\}.*?\\end\{figure\*\}', '', method, flags=re.S)
method = re.sub(r'\\(?:label|cite|ref|url)\{[^}]*\}', '', method)
method = re.sub(r'\\footnote\{\}', '', method)
method_words = len(method.split())
supp = (root / 'supplement/methods.md').read_text(encoding='utf-8')
checks = {
    'eight_sections': len(sections) == 8,
    'intro_order': order == ['Background and Motivation', 'Related Surveys', 'Review Methodology', 'Scope and Contributions'],
    'method_length': 180 <= method_words <= 230,
    'unique_labels': not duplicates,
    'resolved_internal_refs': not missing,
    'no_old_methods_section': 'REVIEW PROCESS AND EVIDENCE BASE' not in body,
    'one_selection_figure': body.count(r'\label{fig:prisma_report_study_flow}') == 1,
    'one_tqaf_figure': body.count(r'\label{fig:tqaf_profile}') == 1,
    'tqaf_in_validation': r'\label{fig:tqaf_profile}' in sources['sections/06_VALIDATION_REPRODUCIBILITY_AND_BENCHMARK_READINESS.tex'],
    'unit_table_in_supplement': all(v in supp for v in ['8,203', '4,779', '402', '115', '111', '404', '8,306', '206', '227', '21']),
    'explicit_unperformed_analyses_in_supplement': 'Formal missing-results or publication-bias assessments and formal sensitivity analyses were not performed.' in supp,
    'osf_final_state_sentence': 'are available in the OSF' in intro,
    'no_ai_workflow_in_intro': 'artificial intelligence' not in intro.lower() and 'AI tools' not in intro,
}
log = (man / 'main.log').read_text(encoding='utf-8', errors='replace')
problems = [line for line in log.splitlines() if re.search(r'Overfull|undefined|multiply defined|Missing character|^!', line, re.I)]
checks['no_build_errors_or_overfull'] = not problems
before = json.loads((qa / 'before.json').read_text(encoding='utf-8-sig'))
changed, removed, preserved_figures = [], [], []
for entry in before:
    p = root / entry['path']
    if not p.exists():
        removed.append(entry['path'])
    elif hashlib.sha256(p.read_bytes()).hexdigest() != entry['sha256']:
        changed.append(entry['path'])
    elif entry['path'].startswith('manuscript\\figures\\'):
        preserved_figures.append(entry['path'])
checks['existing_figure_assets_preserved'] = not any(p.startswith('manuscript\\figures\\') for p in changed + removed)
diffcheck = subprocess.run(['git', '-C', str(root), 'diff', '--check'], capture_output=True, text=True)
checks['git_diff_check'] = diffcheck.returncode == 0
reader = PdfReader(man / 'main.pdf')
texts = [page.extract_text() or '' for page in reader.pages]
needles = ['Review Methodology', 'Scope and Contributions', 'Fig. 2.', 'Technical appraisal of the 206', 'Validation settings and methods', 'VIII. CONCLUSION']
page_map = {n: [i+1 for i, text in enumerate(texts) if n in text] for n in needles}
graphics = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', body)
checks['all_graphic_paths_resolve'] = all((man / p).exists() for p in graphics)
result = {
    'checks': checks,
    'pass': all(checks.values()),
    'section_titles': sections,
    'intro_subsections': order,
    'method_words': method_words,
    'pages': len(reader.pages),
    'page_map': page_map,
    'missing_refs': missing,
    'duplicate_labels': duplicates,
    'log_problems': problems,
    'underfull_warnings': len(re.findall('Underfull', log)),
    'changed_baseline_files': changed,
    'removed_baseline_files': removed,
    'preserved_existing_figure_assets': preserved_figures,
    'osf_update': 'Separate joint task; no remote update performed. Manuscript uses the author-approved final-state wording.',
}
assert result['pass'], json.dumps(result, indent=2)
out = root / 'output/pdf/review.pdf'
shutil.copy2(man / 'main.pdf', out)
result['pdf'] = str(out)
result['sha256'] = hashlib.sha256(out.read_bytes()).hexdigest()
assert out.read_bytes() == (man / 'main.pdf').read_bytes()
(qa / 'result.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
diff = subprocess.run(['git', '-C', str(root), 'diff', '--', 'manuscript', 'governance/V3_ACTIVE_WRITING_RULES.md', 'README_V3_WORKING_DRAFT.md'], capture_output=True).stdout
(qa / 'change.diff').write_bytes(diff)
print(json.dumps({k: result[k] for k in ['pass', 'pages', 'method_words', 'page_map', 'sha256']}, indent=2))
