"""Record the compared versions and inspect the V3 metric input without changes."""
from pathlib import Path
import hashlib, json, csv, collections, re, subprocess
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parent
V3=Path(r'C:/OISAC/worktrees/comst-v3-20260906')
ARCHIVE=Path(r'C:/OISAC/outputs/IKI_CALISMA_OKUMA_2026-09-06')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
sources=[]
for key,path in [('V3',V3/'output/pdf/OISAC_COMST_V3_WORKING_DRAFT_2026-09-06.pdf'),('P01',ARCHIVE/'P01/1.pdf'),('P02',ARCHIVE/'P02/2.pdf')]:
    sources.append(dict(id=key,path=str(path),pdf_pages=len(PdfReader(path).pages),sha256=sha(path)))
metric=V3/'evidence/inputs/ST-19_PRIMARY_METRIC_RESULTS_4779.csv'
with metric.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
candidates=[r for r in rows if r['cross_study_quantitative_comparison_allowed']=='yes_with_conditions']
groups=collections.defaultdict(set)
for r in candidates: groups[r['comparison_group_id']].add(r['study_cluster_id'])
assert len(rows)==4779 and len(candidates)==118
audit=dict(input_path=str(metric),sha256=sha(metric),total_metric_rows=len(rows),candidate_selector={'cross_study_quantitative_comparison_allowed':'yes_with_conditions'},
    candidate_metric_rows=len(candidates),candidate_studies=len(set(r['study_cluster_id'] for r in candidates)),
    nonempty_candidate_groups=len([k for k in groups if k]),candidate_rows_with_blank_group=sum(not r['comparison_group_id'] for r in candidates),
    candidate_groups_with_multiple_studies={k:sorted(v) for k,v in groups.items() if k and len(v)>1},
    independent_human_status_in_candidate_rows=dict(collections.Counter(r['independent_human_status'] for r in candidates)),
    interpretation='The 118 conditional metric records do not form independent cross-study comparison groups in this V3 input. This audit checks the input file, not primary papers or review events in other worktrees.')
snapshot=dict(date='2026-09-06',sources=sources,version_boundary='V3 author-review draft from V2 baseline; Section II is the first rewrite. Not the separate RC1 worktree.',
    git_head=subprocess.check_output(['git','-C',str(V3),'rev-parse','HEAD'],text=True).strip(),
    v3_section_hashes={p.name:sha(p) for p in sorted((V3/'manuscript/sections').glob('*.tex'))},
    v3_metric_input_audit=audit,external_web_used=False,primary_studies_reverified=False,manuscript_edited=False)
(ROOT/'COMPARISON_SNAPSHOT.json').write_text(json.dumps(snapshot,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'pages':[s['pdf_pages'] for s in sources],'candidate_rows':len(candidates),'candidate_studies':audit['candidate_studies'],'candidate_groups':audit['nonempty_candidate_groups'],'multi_study_candidate_groups':len(audit['candidate_groups_with_multiple_studies'])}))
