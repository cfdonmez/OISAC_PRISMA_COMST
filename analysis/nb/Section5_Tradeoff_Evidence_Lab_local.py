import os
import re
import json
import glob
import time
import random
import ast
from pathlib import Path
from collections import deque
import pandas as pd
from tqdm import tqdm
from rapidfuzz import fuzz

# =============================================================================
# 1. Configuration & Constants
# =============================================================================

# Determine base directory relative to this script
SCRIPT_DIR = Path(__file__).resolve().parent
# Assume script is in analysis/nb, so base is 2 levels up
BASE_DIR = SCRIPT_DIR.parent.parent

PROCESSED_MD_DIR = BASE_DIR / 'data' / 'processed_markdowns'
JSON_DIR = BASE_DIR / 'data' / 'extraction_results_v4'
UNIFIED_JSON = JSON_DIR / 'extraction_v4_unified.json'
OUTPUT_DIR = BASE_DIR / 'analysis' / 'V_evidence_v1'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
CHECKPOINT_DIR = OUTPUT_DIR / 'checkpoints'
CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)

VARIANT_CACHE_FILE = OUTPUT_DIR / 'variant_cache.json'
SCHEMA_MAP_PATH = BASE_DIR / 'analysis' / 'II_schema_map.md'
GOV_PATH = BASE_DIR / 'analysis' / 'II_metric_governance.md'

# Execution Controls
TARGET_PAPERS = None  # List of IDs or None for full scan
LIMIT = None          # Int limit or None
LLM_CALLS = True      # Set to False to disable LLM calls entirely
USE_ESCALATION = True
RESUME = True

# Metrics & Rate Limits
MAX_VARIANTS_PER_CONCEPT = 10
MAX_HITS_PER_CONCEPT_PER_PAPER = 5
MAX_CONTEXT_CHARS = 1200
CLASSIFY_CHUNK_SIZE = 4
BATCH_SIZE_PAPERS = 10
MAX_RETRIES = 5
RETRY_BASE_SECONDS = 2.0

# Two-Model Strategy Constants
MODEL_PASS1 = 'meta-llama/llama-4-scout-17b-16e-instruct'   # Fast sweep
MODEL_PASS2 = 'llama-3.3-70b-versatile'                      # Strict recheck
MODEL_VARIANT_GEN = MODEL_PASS1                              # Variant generation

USE_ESCALATION = True
ESCALATE_LABELS = {'INDIRECT', 'NONE', 'WEAK'}

# Per-model rate limits (requests/min)
RPM_BY_MODEL = {
    MODEL_PASS1: 120,
    MODEL_PASS2: 40,
    MODEL_VARIANT_GEN: 120,
    'gemini-1.5-flash': 60,
    'gemini-1.5-pro': 10,
}
DEFAULT_RPM = 30

# =============================================================================
# 2. Unified LLM Client (Supporting Google & Groq)
# =============================================================================

class UnifiedLLMClient:
    def __init__(self):
        self.provider = None
        self.client = None
        self.model_map = {}
        self.request_log = {}

        # Prioritize Google/Gemini (User's "Antigravity Agent" preference)
        if os.environ.get('GOOGLE_API_KEY'):
            try:
                import google.generativeai as genai
                genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
                self.provider = 'google'
                self.client = genai
                print("Using Google/Gemini API provider")
                self.model_map = {
                    'fast': 'gemini-1.5-flash',
                    'strong': 'gemini-1.5-pro',
                    'variant': 'gemini-1.5-flash'
                }
            except ImportError:
                print("Warning: GOOGLE_API_KEY found but google-generativeai not installed.")

        # Fallback to Groq
        if not self.provider and os.environ.get('GROQ_API_KEY'):
            try:
                from groq import Groq
                self.provider = 'groq'
                self.client = Groq(api_key=os.environ['GROQ_API_KEY'])
                print("Using Groq API provider")
                self.model_map = {
                    'fast': 'meta-llama/llama-3.3-70b-versatile',
                    'strong': 'llama-3.3-70b-versatile',
                    'variant': 'llama-3.3-70b-versatile'
                }
            except ImportError:
                 print("Warning: GROQ_API_KEY found but groq package not installed.")

        # Interactive Input Fallback
        if not self.provider:
            print("\n[!] No API Key found in environment variables.")
            print("To use the Agent Feature, please enter your GOOGLE_API_KEY now (or press Enter to skip/mock):")
            try:
                key_input = input("GOOGLE_API_KEY: ").strip()
                if key_input:
                    try:
                        import google.generativeai as genai
                        genai.configure(api_key=key_input)
                        self.provider = 'google'
                        self.client = genai
                        print("Using Google/Gemini API provider (Interactive)")
                        self.model_map = {
                            'fast': 'gemini-1.5-flash',
                            'strong': 'gemini-1.5-pro',
                            'variant': 'gemini-1.5-flash'
                        }
                    except ImportError:
                         print("Error: google-generativeai not installed.")
            except Exception as e:
                print(f"Input error: {e}")

        if not self.provider:
            print("Notice: No API key provided. LLM calls will return mocks.")
    
    def get_model_name(self, role):
        # Map roles to specific models based on provider
        if self.provider == 'groq':
            if role == 'fast': return MODEL_PASS1
            if role == 'strong': return MODEL_PASS2
            if role == 'variant': return MODEL_VARIANT_GEN
        elif self.provider == 'google':
            if role == 'fast': return 'gemini-1.5-flash'
            if role == 'strong': return 'gemini-1.5-pro'
            if role == 'variant': return 'gemini-1.5-flash'
        return 'mock-model'

    def throttle(self, model_name):
        rpm = RPM_BY_MODEL.get(model_name, DEFAULT_RPM)
        if rpm <= 0: return

        q = self.request_log.setdefault(model_name, deque())
        now = time.time()
        
        # Clear old timestamps
        while q and now - q[0] > 60:
            q.popleft()
            
        if len(q) >= rpm:
            wait_s = 60 - (now - q[0]) + 0.1
            wait_s = max(wait_s, 0.1)
            print(f"Rate limit guard ({model_name}): sleeping {wait_s:.1f}s")
            time.sleep(wait_s)
            
            # Re-check after sleep
            now = time.time()
            while q and now - q[0] > 60:
                q.popleft()
                
        q.append(time.time())

    def chat_completion(self, role, messages, expect_json=False):
        if not self.provider:
            return None # Mock mode, handled by caller or returns explicit mock?
        
        model_name = self.get_model_name(role)
        self.throttle(model_name)

        if self.provider == 'google':
            # Convert messages to Gemini format
            # Gemini expects history + last message.
            # Simplified: fuse system prompt into user prompt or use system instruction
            
            system_instruction = None
            prompt_parts = []
            
            for m in messages:
                if m['role'] == 'system':
                    system_instruction = m['content']
                elif m['role'] == 'user':
                    prompt_parts.append(m['content'])
            
            full_prompt = "\n\n".join(prompt_parts)
            
            model = self.client.GenerativeModel(
                model_name=model_name,
                system_instruction=system_instruction,
                generation_config={"response_mime_type": "application/json"} if expect_json else None
            )
            
            try:
                resp = model.generate_content(full_prompt)
                return resp.text
            except Exception as e:
                print(f"Gemini Error: {e}")
                raise e

        elif self.provider == 'groq':
            kwargs = {
                'model': model_name,
                'messages': messages,
                'temperature': 0.1
            }
            if expect_json:
                kwargs['response_format'] = {'type': 'json_object'}
            
            resp = self.client.chat.completions.create(**kwargs)
            return resp.choices[0].message.content

        return None

LLM_CLIENT = UnifiedLLMClient()

def safe_chat_completion(role, messages, expect_json=False):
    if not LLM_CALLS:
        return None
    
    if not LLM_CLIENT.provider:
        # Mock Response
        if expect_json:
            # Return valid JSON structure based on role
            if 'variant' in role:
                return json.dumps({"variants": []})
            else:
                return json.dumps({"results": []})
        return "MOCK RESPONSE"

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return LLM_CLIENT.chat_completion(role, messages, expect_json)
        except Exception as e:
            if attempt >= MAX_RETRIES:
                print(f"LLM Failed after retries: {e}")
                return None
            time.sleep(RETRY_BASE_SECONDS * (2 ** (attempt - 1)))

# =============================================================================
# 3. Helpers
# =============================================================================

def load_json_index(json_dir: Path):
    index = {}
    if not json_dir.exists():
        return {}, None
    for p in sorted(json_dir.glob('O_ISAC_*_v4.json')):
        paper_id = p.stem.replace('_v4','')
        try:
            index[paper_id] = json.loads(p.read_text(encoding='utf-8', errors='ignore'))
        except Exception as e:
            index[paper_id] = {'_error': str(e)}
    unified = None
    if UNIFIED_JSON.exists():
        unified = json.loads(UNIFIED_JSON.read_text(encoding='utf-8', errors='ignore'))
    return index, unified

def canonical_md_path(paths, paper_id):
    scored = []
    for p in paths:
        p = Path(p)
        score = 0
        if (p.parent / 'visual_analysis.txt').exists():
            score += 3
        if p.parent.name == paper_id and p.parent.parent.name == paper_id:
            score += 2
        score += len(p.parts) * 0.1
        scored.append((score, p))
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[0][1] if scored else None

def load_processed_markdowns(target_ids=None, limit=None):
    if not PROCESSED_MD_DIR.exists():
        print(f"Path not found: {PROCESSED_MD_DIR}")
        return []
    all_files = list(PROCESSED_MD_DIR.rglob('*.md'))
    md_files = [p for p in all_files if 'O_ISAC_' in p.name]

    grouped = {}
    for p in md_files:
        m = re.search(r'(O_ISAC_\d+)', p.name)
        if not m: continue
        paper_id = m.group(1)
        if target_ids and paper_id not in target_ids:
            continue
        grouped.setdefault(paper_id, []).append(p)

    records = []
    for i, (paper_id, paths) in enumerate(sorted(grouped.items())):
        if limit and i >= limit:
            break
        canon = canonical_md_path(paths, paper_id)
        if not canon: continue
        text = canon.read_text(encoding='utf-8', errors='ignore')
        lines = text.splitlines()
        va_path = canon.parent / 'visual_analysis.txt'
        va_text = va_path.read_text(encoding='utf-8', errors='ignore') if va_path.exists() else ''
        records.append({
            'paper_id': paper_id,
            'md_path': str(canon),
            'text': text,
            'lines': lines,
            'visual_analysis': va_text
        })
    return records

def build_heading_map(lines):
    current = []
    heading_map = {}
    for i, line in enumerate(lines):
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            title = line.strip('#').strip()
            if level <= len(current):
                current = current[:level-1]
            current.append(title)
        heading_map[i] = ' > '.join(current) if current else 'no_heading'
    return heading_map

def get_context(lines, idx, window=2):
    start = max(0, idx - window)
    end = min(len(lines), idx + window + 1)
    return '\n'.join(lines[start:end])

def to_float(x):
    try:
        if x is None: return None
        if isinstance(x, str) and not x.strip(): return None
        return float(x)
    except: return None

def contains_any(text, keywords):
    if not text: return False
    low = str(text).lower()
    return any(k in low for k in keywords)

MEDIUM_ALIAS_MAP = {
    'visible_light': 'wireless_vlc',
    'vlc': 'wireless_vlc',
    'rf': 'wireless_rf',
    'photo_thz': 'terahertz',
    'photonic_thz': 'terahertz',
}

def normalize_medium_label(medium_value):
    m = str(medium_value).lower().strip() if medium_value is not None else ''
    if not m:
        return 'unknown'
    return MEDIUM_ALIAS_MAP.get(m, m)

def normalize_medium(record):
    clsf = record.get('study_level', {}).get('classification', {}) if isinstance(record, dict) else {}
    medium = clsf.get('oisac_medium_class', 'unknown') if isinstance(clsf, dict) else 'unknown'
    return normalize_medium_label(medium)

def normalize_task_label(task_value):
    tokens = []
    if isinstance(task_value, list):
        tokens = [str(t).strip().lower() for t in task_value if str(t).strip()]
    elif isinstance(task_value, str):
        raw = task_value.strip()
        if raw.startswith('[') and raw.endswith(']'):
            try:
                parsed = ast.literal_eval(raw)
                if isinstance(parsed, list):
                    tokens = [str(t).strip().lower() for t in parsed if str(t).strip()]
                elif raw:
                    tokens = [raw.lower()]
            except Exception:
                tokens = [raw.lower()] if raw else []
        elif raw:
            tokens = [raw.lower()]
    elif task_value is not None:
        tokens = [str(task_value).strip().lower()]

    dedup = []
    seen = set()
    for t in tokens:
        if t and t not in seen:
            seen.add(t)
            dedup.append(t)

    if not dedup:
        return 'unknown'
    if len(dedup) == 1:
        return dedup[0]
    return '|_'.join(dedup)

def is_ranging_task(task_text):
    return contains_any(task_text, ['ranging', 'tof', 'fmcw', 'range'])

def is_fiber_task(task_text):
    return contains_any(task_text, ['das', 'otdr', 'ofdr', 'fiber', 'fibre'])

def has_electrical_rx_cue(rx_type):
    return contains_any(
        rx_type,
        ['im/dd', 'direct', 'coherent', 'heterodyne', 'homodyne', 'envelope', 'photo', 'detector', 'pd', 'bpd'],
    )

def extract_rate_bps(scn):
    cm = scn.get('comm_metrics', {}) if isinstance(scn, dict) else {}
    r_gbps = to_float(cm.get('data_rate_gbps')) if isinstance(cm, dict) else None
    if r_gbps is not None and r_gbps > 0:
        return r_gbps * 1e9, 'data_rate_gbps'
    return None, None

def scenario_metric_flags(record):
    medium = normalize_medium(record)
    raw_scenarios = record.get('scenario_level', []) if isinstance(record, dict) else []
    if isinstance(raw_scenarios, list):
        scenarios = [s for s in raw_scenarios if isinstance(s, dict)]
    elif isinstance(raw_scenarios, dict):
        scenarios = [raw_scenarios]
    else:
        scenarios = []

    rows = []
    for idx, scn in enumerate(scenarios):
        sm = scn.get('sensing_metrics', {}) if isinstance(scn, dict) else {}
        cm = scn.get('comm_metrics', {}) if isinstance(scn, dict) else {}
        rx = scn.get('receiver', {}) if isinstance(scn, dict) else {}
        tw = scn.get('tradeoff', {}) if isinstance(scn, dict) else {}

        task_raw = (sm.get('sensing_task_type') if isinstance(sm, dict) else '') or ''
        task = normalize_task_label(task_raw)
        r_bps, r_src = extract_rate_bps(scn)
        drmin = to_float(sm.get('range_resolution_m')) if isinstance(sm, dict) else None
        dz = to_float(sm.get('spatial_resolution_m')) if isinstance(sm, dict) else None
        
        range_acc = to_float(sm.get('range_accuracy_m')) if isinstance(sm, dict) else None
        loc_err = to_float(sm.get('localization_error_m')) if isinstance(sm, dict) else None
        sigma_r = range_acc if range_acc is not None else loc_err
        
        crb = to_float(sm.get('crb_crlb_value')) if isinstance(sm, dict) else None
        crb_param = (sm.get('crb_parameter') if isinstance(sm, dict) else '') or ''
        
        osnr = to_float(cm.get('osnr_db')) if isinstance(cm, dict) else None
        snr = to_float(cm.get('snr_db')) if isinstance(cm, dict) else None
        rx_type = (rx.get('rx_detection_type') if isinstance(rx, dict) else '') or ''
        tradeoff_type = (tw.get('tradeoff_type') if isinstance(tw, dict) else '') or ''
        coupling_mode = (tw.get('coupling_mode') if isinstance(tw, dict) else '') or ''
        
        drmin_eligible = (
            drmin is not None and drmin > 0 and (
                medium in {
                    'wireless_fso', 'wireless_vlc', 'hybrid', 'terahertz', 'wireless',
                    'wireless_rf', 'wireless_retroreflective', 'retroreflective', 'retroreflective_optical'
                } or is_ranging_task(task)
            )
        )
        dz_eligible = (
            dz is not None and dz > 0 and (
                medium == 'cabled_fibre' or is_fiber_task(task)
            )
        )

        plane_mixed = (osnr is not None and snr is not None)
        imdd_osnr_conflict = contains_any(rx_type, ['im/dd', 'direct']) and (osnr is not None)
        snr_ambiguous = (snr is not None) and (osnr is None) and (not has_electrical_rx_cue(rx_type))

        dz_drmin_alias = False
        if drmin is not None and drmin > 0 and dz is not None and dz > 0 and (medium == 'cabled_fibre' or is_fiber_task(task)):
            den = max(abs(drmin), abs(dz), 1e-12)
            dz_drmin_alias = abs(drmin - dz) / den < 1e-9

        crq_candidate = r_bps is not None and drmin_eligible
        governance_blocked = plane_mixed or imdd_osnr_conflict or snr_ambiguous or dz_drmin_alias
        crq_eligible = crq_candidate and (not governance_blocked)
        crq_delta = (r_bps / drmin) if crq_eligible and drmin and drmin > 0 else None
        
        rows.append({
            'scenario_index': idx, 'medium': medium, 'task_type': str(task),
            'r_bps': r_bps, 'r_source': r_src, 'drmin_m': drmin, 'drmin_eligible': drmin_eligible,
            'dz_m': dz, 'dz_eligible': dz_eligible, 'sigma_r_m': sigma_r,
            'crb_value': crb, 'crb_param': str(crb_param), 'osnr_db': osnr,
            'snr_db': snr, 'rx_detection_type': str(rx_type), 'plane_mixed': plane_mixed,
            'tradeoff_type': str(tradeoff_type).strip().lower(),
            'coupling_mode': str(coupling_mode).strip().lower(),
            'imdd_osnr_conflict': imdd_osnr_conflict,
            'snr_ambiguous': snr_ambiguous,
            'dz_drmin_alias': dz_drmin_alias,
            'governance_blocked': governance_blocked,
            'crq_candidate': crq_candidate,
            'crq_eligible': crq_eligible,
            'crq_delta_bps_per_m': crq_delta,
        })
    return rows

def get_variants(concept):
    # Load cache
    if VARIANT_CACHE_FILE.exists():
        variant_cache = json.loads(VARIANT_CACHE_FILE.read_text(encoding='utf-8'))
    else:
        variant_cache = {}

    if concept in variant_cache:
        return variant_cache[concept][:MAX_VARIANTS_PER_CONCEPT]
    
    # Generate via LLM
    print(f"Generating variants for: {concept}")
    system_prompt = 'You generate lexical variants for evidence retrieval. Return JSON: {"variants": ["..."]}.'
    user_prompt = f'Concept: {concept}. Return up to 12 variants including synonyms.'
    
    content = safe_chat_completion('variant', [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt}
    ], expect_json=True)
    
    vals = [concept]
    if content:
        try:
            data = json.loads(content)
            vals.extend(data.get('variants', []))
        except: pass
    
    # Dedup
    dedup = []
    seen = set()
    for v in vals:
        k = str(v).lower().strip()
        if k and k not in seen:
            seen.add(k)
            dedup.append(str(v))
    
    dedup = dedup[:MAX_VARIANTS_PER_CONCEPT]
    variant_cache[concept] = dedup
    VARIANT_CACHE_FILE.write_text(json.dumps(variant_cache, indent=2), encoding='utf-8')
    return dedup

def scan_lines_for_variants(lines, variants, fuzzy_threshold=85):
    hits = []
    for i, line in enumerate(lines):
        text = line.strip()
        if not text: continue
        low = text.lower()
        for v in variants:
            vlow = v.lower()
            if vlow in low:
                hits.append((i, line, v, 'lexical'))
                break
            # Fuzzy check if strict lexical fails? Only checks partial ratio
            score = fuzz.partial_ratio(vlow, low)
            if score >= fuzzy_threshold:
                hits.append((i, line, v, f'fuzzy:{score}'))
                break
    return hits

def clip_text(text, max_chars=MAX_CONTEXT_CHARS):
    text = str(text) if text else ''
    if len(text) <= max_chars: return text
    return text[:max_chars] + ' ...'

def chunk_list(items, n):
    for i in range(0, len(items), n):
        yield items[i:i+n]

def parse_batch_results(content, n):
    fallback = [{'label': 'WEAK', 'rationale': 'LLM parse failed'} for _ in range(n)]
    if not content: return fallback
    try:
        parsed = json.loads(content)
        results = parsed.get('results', [])
        mapped = {int(r.get('idx', -1)): r for r in results if isinstance(r, dict)}
        out = []
        for i in range(n):
            r = mapped.get(i)
            if not r:
                out.append({'label': 'WEAK', 'rationale': 'No label'})
                continue
            label = str(r.get('label', 'WEAK')).upper().strip()
            if label not in {'DIRECT', 'INDIRECT', 'NONE'}: label = 'WEAK'
            out.append({'label': label, 'rationale': str(r.get('rationale', ''))})
        return out
    except: return fallback

def classify_hits_batch(concept, contexts):
    if not contexts: return []
    
    # --- Pass 1: Fast Model ---
    compact = [{'idx': i, 'context': clip_text(ctx)} for i, ctx in enumerate(contexts)]
    
    sys_p = (
        'You are an evidence auditor. '
        'For each snippet, decide if the text supports the concept as DIRECT, INDIRECT, or NONE. '
        'Return strict JSON string: {"results": [{"idx":0,"label":"DIRECT|INDIRECT|NONE","rationale":"..."}]}'
    )
    user_p = f'Concept: {concept}\nSnippets JSON:\n{json.dumps(compact, ensure_ascii=False)}'
    
    pass1_resp = safe_chat_completion('fast', [
        {'role': 'system', 'content': sys_p},
        {'role': 'user', 'content': user_p}
    ], expect_json=True)
    
    pass1_results = parse_batch_results(pass1_resp, len(contexts))
    
    out = []
    for i, r in enumerate(pass1_results):
        out.append({
            'label': r['label'],
            'rationale': r['rationale'],
            'label_pass1': r['label'],
            'rationale_pass1': r['rationale'],
            'model_pass1': LLM_CLIENT.get_model_name('fast'),
            'label_pass2': '',
            'rationale_pass2': '',
            'model_pass2': '',
            'escalated': False
        })
        
    # --- Pass 2: Escalation (Strong Model) ---
    if USE_ESCALATION:
        # Identify hits that need escalation
        idxs_to_escalate = [i for i, r in enumerate(out) if r['label'] in ESCALATE_LABELS]
        
        if idxs_to_escalate:
            # Prepare sub-batch for Pass 2
            sub_contexts = [compact[i] for i in idxs_to_escalate]
            
            # Optional: Add hints from Pass 1? (Section 4 does this: hint_labels=hints)
            # For simplicity in this script, we just re-ask the strong model.
            
            user_p2 = f'Concept: {concept}\nSnippets JSON (Re-evaluate carefully):\n{json.dumps(sub_contexts, ensure_ascii=False)}'
            
            pass2_resp = safe_chat_completion('strong', [
                {'role': 'system', 'content': sys_p},
                {'role': 'user', 'content': user_p2}
            ], expect_json=True)
            
            pass2_results = parse_batch_results(pass2_resp, len(idxs_to_escalate))
            
            # Merge results back
            for j, orig_idx in enumerate(idxs_to_escalate):
                if j < len(pass2_results):
                    r2 = pass2_results[j]
                    out[orig_idx]['label_pass2'] = r2['label']
                    out[orig_idx]['rationale_pass2'] = r2['rationale']
                    out[orig_idx]['model_pass2'] = LLM_CLIENT.get_model_name('strong')
                    out[orig_idx]['escalated'] = True
                    
                    # Update final label if Pass 2 found something valid
                    if r2['label'] in {'DIRECT', 'INDIRECT', 'NONE'}:
                         out[orig_idx]['label'] = r2['label']
                         out[orig_idx]['rationale'] = r2['rationale']

    return out

def classify_hits_chunked(concept, contexts):
    out = []
    for chunk in chunk_list(contexts, CLASSIFY_CHUNK_SIZE):
        out.extend(classify_hits_batch(concept, chunk))
    return out

def llm_fields_from_cls(cls):
    return {
        'llm_model_pass1': cls.get('model_pass1', ''),
        'llm_label_pass1': cls.get('label_pass1', ''),
        'llm_model_pass2': cls.get('model_pass2', ''),
        'llm_label_pass2': cls.get('label_pass2', ''),
        'llm_escalated': cls.get('escalated', False),
    }

def append_rows_csv(out_csv, rows):
    if not rows: return
    df = pd.DataFrame(rows)
    mode = 'a' if out_csv.exists() else 'w'
    header = not out_csv.exists()
    df.to_csv(out_csv, mode=mode, header=header, index=False)

def load_done_ids(section_name):
    if not RESUME: return set()
    cp = CHECKPOINT_DIR / f'{section_name}_done_ids.json'
    if cp.exists():
        return set(json.loads(cp.read_text(encoding='utf-8')))
    return set()

def save_done_ids(section_name, done_ids):
    cp = CHECKPOINT_DIR / f'{section_name}_done_ids.json'
    cp.write_text(json.dumps(sorted(list(done_ids)), indent=2), encoding='utf-8')

# =============================================================================
# 4. Main Execution Logic
# =============================================================================

def run_section_5A(papers, json_index):
    section_name = 'section5A'
    out_csv = OUTPUT_DIR / f'{section_name}_evidence.csv'
    done_ids = load_done_ids(section_name)
    pending = [p for p in papers if p['paper_id'] not in done_ids]
    print(f'{section_name}: pending papers = {len(pending)}')

    concepts = [
        'trade-off', 'multiobjective optimization', 'pareto frontier',
        'weighted sum optimization', 'power allocation', 'communication-centric objective',
        'sensing-centric objective', 'joint design operating point'
    ]
    
    # Pre-fetch variants
    concept_variants = {c: get_variants(c) for c in concepts}

    for batch in chunk_list(pending, BATCH_SIZE_PAPERS):
        batch_rows = []
        for paper in tqdm(batch, desc=f'{section_name} batch'):
            paper_id = paper['paper_id']
            lines = paper['lines']
            heading_map = build_heading_map(lines)
            record = json_index.get(paper_id, {})

            # 1. Text Evidence
            for concept, variants in concept_variants.items():
                hits = scan_lines_for_variants(lines, variants)
                hits = hits[:MAX_HITS_PER_CONCEPT_PER_PAPER]
                contexts = [get_context(lines, idx) for idx, _, _, _ in hits]
                cls_all = classify_hits_chunked(concept, contexts)

                for (hit, cls) in zip(hits, cls_all):
                    idx, line, variant, match_type = hit
                    batch_rows.append({
                        'paper_id': paper_id, 'section': '5A', 'concept': concept,
                        'variant': variant, 'match_type': match_type,
                        'strength': cls.get('label', 'WEAK'),
                        'rationale': cls.get('rationale', ''),
                        'quote': line.strip(), 'line_start': idx + 1, 'line_end': idx + 1,
                        'heading_path': heading_map.get(idx, 'no_heading'),
                        'json_path': '', 'json_value': '',
                        **llm_fields_from_cls(cls),
                    })

            # 2. JSON Summary
            if isinstance(record, dict):
                flags = scenario_metric_flags(record)
                summary = {
                    'n_scenarios': len(flags),
                    'n_rate': sum(1 for f in flags if f.get('r_bps') is not None),
                    'n_drmin_eligible': sum(1 for f in flags if f.get('drmin_eligible')),
                    'n_dz_eligible': sum(1 for f in flags if f.get('dz_eligible')),
                    'n_sigma_r': sum(1 for f in flags if f.get('sigma_r_m') is not None),
                    'n_crb': sum(1 for f in flags if f.get('crb_value') is not None),
                    'n_crq_candidate': sum(1 for f in flags if f.get('crq_candidate')),
                    'n_crq_eligible': sum(1 for f in flags if f.get('crq_eligible')),
                    'n_plane_mixed': sum(1 for f in flags if f.get('plane_mixed')),
                    'n_imdd_osnr_conflict': sum(1 for f in flags if f.get('imdd_osnr_conflict')),
                    'n_snr_ambiguous': sum(1 for f in flags if f.get('snr_ambiguous')),
                    'n_dz_drmin_alias': sum(1 for f in flags if f.get('dz_drmin_alias')),
                    'n_governance_blocked': sum(1 for f in flags if f.get('governance_blocked')),
                }
                batch_rows.append({
                    'paper_id': paper_id, 'section': '5A', 'concept': 'json:tradeoff_eligibility',
                    'variant': '', 'match_type': 'json', 'strength': 'DIRECT',
                    'rationale': 'Structured metric-eligibility summary',
                    'quote': '', 'line_start': '', 'line_end': '', 'heading_path': '',
                    'json_path': 'scenario_level',
                    'json_value': json.dumps(summary),
                    'llm_label_pass1': 'DIRECT', 'llm_escalated': False
                })

            done_ids.add(paper_id)
        
        append_rows_csv(out_csv, batch_rows)
        save_done_ids(section_name, done_ids)

def run_section_5B(papers, json_index):
    print("Running Section 5B...")
    rows = []
    for paper in tqdm(papers, desc='section5B'):
        paper_id = paper['paper_id']
        record = json_index.get(paper_id, {})
        if not isinstance(record, dict): continue
        flags = scenario_metric_flags(record)
        rows.append({
            'paper_id': paper_id,
            'n_scenarios': len(flags),
            'n_rate': sum(1 for f in flags if f.get('r_bps') is not None),
            'n_drmin': sum(1 for f in flags if f.get('drmin_m') is not None),
            'n_drmin_eligible': sum(1 for f in flags if f.get('drmin_eligible')),
            'n_dz': sum(1 for f in flags if f.get('dz_m') is not None),
            'n_dz_eligible': sum(1 for f in flags if f.get('dz_eligible')),
            'n_sigma_r': sum(1 for f in flags if f.get('sigma_r_m') is not None),
            'n_crb': sum(1 for f in flags if f.get('crb_value') is not None),
            'n_osnr': sum(1 for f in flags if f.get('osnr_db') is not None),
            'n_snr': sum(1 for f in flags if f.get('snr_db') is not None),
            'n_plane_mixed': sum(1 for f in flags if f.get('plane_mixed')),
            'n_imdd_osnr_conflict': sum(1 for f in flags if f.get('imdd_osnr_conflict')),
            'n_snr_ambiguous': sum(1 for f in flags if f.get('snr_ambiguous')),
            'n_dz_drmin_alias': sum(1 for f in flags if f.get('dz_drmin_alias')),
            'n_governance_blocked': sum(1 for f in flags if f.get('governance_blocked')),
            'n_crq_candidate': sum(1 for f in flags if f.get('crq_candidate')),
            'n_crq_eligible': sum(1 for f in flags if f.get('crq_eligible')),
        })
    df = pd.DataFrame(rows)
    out_csv = OUTPUT_DIR / 's5b_met_gov.csv'
    df.to_csv(out_csv, index=False)

def run_section_5C(papers, json_index):
    print("Running Section 5C...")
    point_rows = []
    mention_rows = []
    
    concepts = ['rate-resolution trade-off', 'pareto optimal', 'capacity-resolution quotient']
    concept_variants = {c: get_variants(c) for c in concepts}

    for paper in tqdm(papers, desc='section5C'):
        paper_id = paper['paper_id']
        record = json_index.get(paper_id, {})
        lines = paper['lines']
        heading_map = build_heading_map(lines)

        if isinstance(record, dict):
            flags = scenario_metric_flags(record)
            for f in flags:
                point_rows.append({
                    'paper_id': paper_id,
                    'scenario_index': f.get('scenario_index'),
                    'medium': f.get('medium'),
                    'task_type': f.get('task_type'),
                    'tradeoff_type': f.get('tradeoff_type'),
                    'coupling_mode': f.get('coupling_mode'),
                    'r_bps': f.get('r_bps'),
                    'drmin_m': f.get('drmin_m'),
                    'drmin_eligible': f.get('drmin_eligible'),
                    'dz_m': f.get('dz_m'),
                    'sigma_r_m': f.get('sigma_r_m'),
                    'crb_value': f.get('crb_value'),
                    'osnr_db': f.get('osnr_db'),
                    'snr_db': f.get('snr_db'),
                    'rx_detection_type': f.get('rx_detection_type'),
                    'crq_candidate': f.get('crq_candidate'),
                    'crq_eligible': f.get('crq_eligible'),
                    'crq_delta_bps_per_m': f.get('crq_delta_bps_per_m'),
                    'plane_mixed': f.get('plane_mixed'),
                    'imdd_osnr_conflict': f.get('imdd_osnr_conflict'),
                    'snr_ambiguous': f.get('snr_ambiguous'),
                    'dz_drmin_alias': f.get('dz_drmin_alias'),
                    'governance_blocked': f.get('governance_blocked'),
                })

        for concept, variants in concept_variants.items():
            hits = scan_lines_for_variants(lines, variants)
            hits = hits[:MAX_HITS_PER_CONCEPT_PER_PAPER]
            contexts = [get_context(lines, idx) for idx, _, _, _ in hits]
            cls_all = classify_hits_chunked(concept, contexts)
            
            for (hit, cls) in zip(hits, cls_all):
                idx, line, variant, match_type = hit
                mention_rows.append({
                    'paper_id': paper_id, 'concept': concept, 'variant': variant,
                    'strength': cls.get('label', 'WEAK'),
                    'quote': line.strip(),
                })
    
    pd.DataFrame(point_rows).to_csv(OUTPUT_DIR / 'section5C_tradeoff_points.csv', index=False)
    pd.DataFrame(mention_rows).to_csv(OUTPUT_DIR / 's5c_trade_mnts.csv', index=False)

def run_section_5D():
    print("Running Section 5D (Modality Slices)...")
    points_csv = OUTPUT_DIR / 'section5C_tradeoff_points.csv'
    if not points_csv.exists(): return
    
    df = pd.read_csv(points_csv)
    # Convert bool columns carefully
    df['crq_eligible'] = df['crq_eligible'].astype(str).str.lower() == 'true'
    df['drmin_eligible'] = df['drmin_eligible'].astype(str).str.lower() == 'true'
    
    df_valid = df[df['crq_eligible']].copy()
    if df_valid.empty:
        df_valid = df[df['drmin_eligible']].copy()
    
    if df_valid.empty:
        print("Section 5D: No valid points found.")
        return

    # Numeric conversion
    for col in ['r_bps', 'drmin_m', 'sigma_r_m', 'crq_delta_bps_per_m']:
        if col in df_valid.columns:
            df_valid[col] = pd.to_numeric(df_valid[col], errors='coerce')

    if 'medium' in df_valid.columns:
        df_valid['medium'] = df_valid['medium'].map(normalize_medium_label).fillna('unknown')
    
    grouped = df_valid.groupby('medium', dropna=False).agg(
        n_points=('paper_id', 'count'),
        n_unique_papers=('paper_id', 'nunique'),
        median_r_bps=('r_bps', 'median'),
        median_drmin_m=('drmin_m', 'median'),
        median_sigma_r_m=('sigma_r_m', 'median'),
        median_crq=('crq_delta_bps_per_m', 'median'),
        p90_crq=('crq_delta_bps_per_m', lambda s: s.quantile(0.9) if len(s.dropna()) else None),
    ).reset_index()
    
    out_csv = OUTPUT_DIR / 'section5D_modality_slices.csv'
    grouped.to_csv(out_csv, index=False)
    print("Saved Section 5D:", out_csv)

def run_section_5E():
    print("Running Section 5E (Pareto)...")
    points_csv = OUTPUT_DIR / 'section5C_tradeoff_points.csv'
    if not points_csv.exists(): return
    
    df = pd.read_csv(points_csv)
    # Ensure numeric
    for col in ['r_bps', 'drmin_m', 'crq_delta_bps_per_m']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Filter
    df['crq_eligible'] = df['crq_eligible'].astype(str).str.lower() == 'true'
    if 'governance_blocked' in df.columns:
        df['governance_blocked'] = df['governance_blocked'].astype(str).str.lower() == 'true'
        valid = df[df['crq_eligible'] & (~df['governance_blocked'])].copy()
    else:
        valid = df[df['crq_eligible']].copy()
    valid = valid.dropna(subset=['r_bps', 'drmin_m'])
    
    if valid.empty:
        print("Section 5E: No valid points for Pareto.")
        return

    # Pareto Logic
    records = valid[['r_bps', 'drmin_m']].to_numpy()
    pareto_idx = []
    for i in range(len(records)):
        r_i, d_i = records[i]
        dominated = False
        for j in range(len(records)):
            if i == j: continue
            r_j, d_j = records[j]
            # Dominated if another point has higher rate AND lower (better) resolution
            if (r_j >= r_i and d_j <= d_i) and (r_j > r_i or d_j < d_i):
                dominated = True
                break
        if not dominated:
            pareto_idx.append(i)
            
    pareto = valid.iloc[pareto_idx].copy()
    pareto = pareto.sort_values(['r_bps', 'drmin_m'], ascending=[False, True])
    
    pareto_csv = OUTPUT_DIR / 'section5E_pareto_points.csv'
    pareto.to_csv(pareto_csv, index=False)
    
    # Summary Table
    summary_rows = [{
        'n_total_points': int(len(df)),
        'n_valid_crq_points': int(len(valid)),
        'n_pareto_points': int(len(pareto)),
        'max_crq': float(valid['crq_delta_bps_per_m'].max()) if not valid.empty else None,
        'median_crq': float(valid['crq_delta_bps_per_m'].median()) if not valid.empty else None,
    }]
    pd.DataFrame(summary_rows).to_csv(OUTPUT_DIR / 'section5E_summary_table.csv', index=False)
    (OUTPUT_DIR / 'section5E_summary.json').write_text(json.dumps(summary_rows[0], indent=2), encoding='utf-8')
    print("Saved Section 5E outputs.")

def generate_report():
    report_files = [
        'section5A_evidence.csv',
        's5b_met_gov.csv',
        'section5C_tradeoff_points.csv',
        's5c_trade_mnts.csv'
    ]
    report = []
    for fname in report_files:
        p = OUTPUT_DIR / fname
        report.append(f'{fname}: ' + ('OK' if p.exists() else 'MISSING'))
    
    report_path = OUTPUT_DIR / 'readiness_report.md'
    report_path.write_text('\n'.join(report), encoding='utf-8')
    print("Report generated:", report_path)

# Main
if __name__ == "__main__":
    print(f"Starting Local Lab. Base Dir: {BASE_DIR}")
    
    # Load Data
    json_index, unified = load_json_index(JSON_DIR)
    print(f"Loaded JSON Index: {len(json_index)} papers")
    
    papers = load_processed_markdowns(target_ids=TARGET_PAPERS, limit=LIMIT)
    print(f"Loaded Markdown Papers: {len(papers)}")

    if papers:
        run_section_5A(papers, json_index)
        run_section_5B(papers, json_index)
        run_section_5C(papers, json_index)
        run_section_5D()
        run_section_5E()
        generate_report()
    else:
        print("No papers found to process! Check paths.")
