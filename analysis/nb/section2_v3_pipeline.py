from __future__ import annotations

import hashlib
import json
import os
import random
import re
import time
from collections import defaultdict, deque
from pathlib import Path

import pandas as pd
from rapidfuzz import fuzz
from tqdm import tqdm

try:
    from groq import Groq
except Exception:  # pragma: no cover
    Groq = None


ROOT = Path(".")
PROCESSED_MD_DIR = ROOT / "data/proc_markdowns"
JSON_DIR = ROOT / "data/ext_res_v4"
UNIFIED_CSV = ROOT / "data/ext_v4_uni.csv"
OUTPUT_DIR = ROOT / "analysis/II_ev_v3"
CHECKPOINT_DIR = OUTPUT_DIR / "checkpoints"

RUN_PROFILE = "FULL_RESCAN"
RESUME = True
LLM_CALLS = True
REQUIRE_GROQ = True
MODEL_PASS1 = "meta-llama/llama-4-scout-17b-16e-instruct"
MODEL_PASS2 = "llama-3.3-70b-versatile"
MODEL_VARIANT_GEN = MODEL_PASS1
USE_ESCALATION = True
ESCALATE_LABELS = {"INDIRECT", "NONE", "WEAK"}
RPM_BY_MODEL = {
    MODEL_PASS1: 120,
    MODEL_PASS2: 40,
    MODEL_VARIANT_GEN: 120,
}
DEFAULT_RPM = 30

MAX_HITS_PER_CONCEPT_PER_PAPER = 0
MAX_CONTEXT_CHARS = 900
MAX_VARIANTS_PER_CONCEPT = 12
MAX_RETRIES = 4
RETRY_BASE_SECONDS = 1.5
SCAN_VISUAL_ANALYSIS = True
MARKDOWN_FUZZY_THRESHOLD = 86
JSON_FUZZY_THRESHOLD = 92
PROGRESS_DOC_INTERVAL = 10
PROGRESS_TIME_INTERVAL_SECONDS = 30
PROGRESS_CALL_INTERVAL = 50

_GROQ_CLIENT = None
REQUEST_LOG_BY_MODEL: dict[str, deque] = {}
VARIANT_CACHE_PATH = OUTPUT_DIR / "variant_cache.json"
if VARIANT_CACHE_PATH.exists():
    try:
        VARIANT_CACHE = json.loads(VARIANT_CACHE_PATH.read_text(encoding="utf-8"))
    except Exception:
        VARIANT_CACHE = {}
else:
    VARIANT_CACHE = {}

REQUIRED_INPUTS = {
    "section2_governance": [
        "analysis/II_met_gov.md",
        "analysis/II_sch_map.md",
        "analysis/II_met_eval_gov_2D.md",
        "analysis/II_trade_gov_2E.md",
        "analysis/II_ev_v2/metric_index_v2.csv",
        "analysis/II_ev_v2/section2A_evidence.csv",
        "analysis/II_ev_v2/section2A_plane_evidence.csv",
        "analysis/II_ev_v2/section2B_evidence.csv",
        "analysis/II_ev_v2/section2C_evidence_LLM.csv",
        "analysis/II_ev_v2/section2D_evidence_LLM.csv",
        "analysis/II_ev_v2/section2E_evidence_LLM.csv",
    ],
    "comst_recipes": [
        "writing_recipes/COMST_master_recipe.md",
        "docs/surv_write_guide.md",
        "memory-bank/master_writing_guide.md",
        "memory-bank/body_section_templates.md",
        "memory-bank/goldenModel.md",
        "memory-bank/surveyOutline.md",
        "manuscript/comst_template.tex",
        "review_package/COMST_review_bundle_02_rules_methodology.md",
        "review_package/COMST_review_bundle_03_audits.md",
    ],
    "prisma_protocol": [
        "protocol/prisma_proto.md",
        "protocol/prisma_2020_chk.md",
        "screening/prisma_flow_counts.csv",
        "screening/excluded_fulltext_log.csv",
        "search/search_strings.md",
        "search/search_log.csv",
        "search/dedup_log.csv",
        "analysis/PRISMA_stat.md",
    ],
    "survey_flow": [
        "drafts/section_01_introduction.md",
        "drafts/section_02_fundamentals_draft.md",
        "drafts/section_03_methodology.md",
        "drafts/section_04_taxonomy.md",
    ],
    "corpus": [
        "data/proc_markdowns",
        "data/ext_res_v4",
        "data/ext_v4_uni.csv",
    ],
}

SECTION2_CONCEPTS = {
    "2A": {
        "observation_plane": [
            "osnr",
            "electrical snr",
            "esnr",
            "optical plane",
            "electrical plane",
            "coherent detection",
            "im/dd",
            "direct detection",
        ],
        "integration_paradigm": [
            "communication-centric",
            "sensing-centric",
            "joint design",
            "co-design",
            "integrated sensing and communication",
        ],
    },
    "2B": {
        "channel_models": [
            "beer-lambert",
            "gamma-gamma",
            "log-normal turbulence",
            "pointing error",
            "multipath",
            "lambertian",
            "impulse response",
        ]
    },
    "2C": {
        "transceiver_hardware": [
            "laser diode",
            "vcsel",
            "led",
            "photodiode",
            "apd",
            "balanced pd",
            "mzm",
            "iq modulator",
            "opa",
            "ris",
            "photonic integrated circuit",
        ]
    },
    "2D": {
        "performance_metrics": [
            "range resolution",
            "spatial resolution",
            "rmse",
            "crb",
            "crlb",
            "ber",
            "evm",
            "throughput",
            "capacity",
            "spectral efficiency",
            "osnr",
            "snr",
        ]
    },
    "2E": {
        "coupling_tradeoff": [
            "trade-off",
            "pareto",
            "weighted sum",
            "multi-objective",
            "resource coupling",
            "waveform coupling",
            "hardware coupling",
            "algorithmic coupling",
            "joint optimization",
        ]
    },
}

CANDIDATE_COLUMNS = [
    "paper_id",
    "source_type",
    "source_path",
    "md_path",
    "section_key",
    "concept_key",
    "variant",
    "match_type",
    "quote",
    "line_start",
    "line_end",
    "heading_path",
    "context",
    "label",
    "strength",
    "rationale",
    "model_used",
]

ANCHOR_COLUMNS = [
    "claim_id",
    "claim_key",
    "section",
    "paper_id",
    "concept",
    "strength",
    "quote",
    "line_start",
    "line_end",
    "heading_path",
    "claim_supported",
]

RUNTIME_STATS = {
    "start_time": None,
    "llm_attempts_total": 0,
    "llm_success_total": 0,
    "llm_fail_total": 0,
    "llm_attempts_by_model": {},
    "llm_success_by_model": {},
    "llm_fail_by_model": {},
}


def p(path: str) -> Path:
    return ROOT / path


def _progress_log_path() -> Path:
    return OUTPUT_DIR / "runtime_progress.log"


def _progress_json_path() -> Path:
    return CHECKPOINT_DIR / "runtime_progress.json"


def _progress_csv_path() -> Path:
    return CHECKPOINT_DIR / "runtime_prog_snaps.csv"


def _runtime_summary_path() -> Path:
    return OUTPUT_DIR / "runtime_summary.json"


def _inc_counter(store: dict, key: str, delta: int = 1) -> None:
    store[key] = int(store.get(key, 0)) + delta


def _fmt_eta(seconds: float | None) -> str:
    if seconds is None or seconds < 0:
        return "unknown"
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins}m{secs:02d}s"


def init_runtime_stats() -> None:
    RUNTIME_STATS["start_time"] = time.time()
    RUNTIME_STATS["llm_attempts_total"] = 0
    RUNTIME_STATS["llm_success_total"] = 0
    RUNTIME_STATS["llm_fail_total"] = 0
    RUNTIME_STATS["llm_attempts_by_model"] = {}
    RUNTIME_STATS["llm_success_by_model"] = {}
    RUNTIME_STATS["llm_fail_by_model"] = {}
    _progress_log_path().write_text("", encoding="utf-8")


def log_progress(message: str, **kwargs) -> None:
    ts = pd.Timestamp.utcnow().isoformat()
    parts = [f"[{ts}] {message}"]
    for k, v in kwargs.items():
        parts.append(f"{k}={v}")
    line = " | ".join(parts)
    print(line)
    try:
        with _progress_log_path().open("a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass


def write_progress_snapshot(stage: str, **kwargs) -> None:
    payload = {
        "timestamp_utc": pd.Timestamp.utcnow().isoformat(),
        "stage": stage,
        "llm_attempts_total": int(RUNTIME_STATS.get("llm_attempts_total", 0)),
        "llm_success_total": int(RUNTIME_STATS.get("llm_success_total", 0)),
        "llm_fail_total": int(RUNTIME_STATS.get("llm_fail_total", 0)),
        "llm_attempts_by_model": dict(RUNTIME_STATS.get("llm_attempts_by_model", {})),
        "llm_success_by_model": dict(RUNTIME_STATS.get("llm_success_by_model", {})),
        "llm_fail_by_model": dict(RUNTIME_STATS.get("llm_fail_by_model", {})),
    }
    payload.update(kwargs)
    _progress_json_path().write_text(json.dumps(payload, indent=2), encoding="utf-8")
    snap = pd.DataFrame([payload])
    cpath = _progress_csv_path()
    if cpath.exists():
        snap.to_csv(cpath, mode="a", index=False, header=False)
    else:
        snap.to_csv(cpath, index=False)


def get_groq_client():
    global _GROQ_CLIENT
    if not LLM_CALLS or Groq is None:
        if REQUIRE_GROQ:
            raise RuntimeError("Groq client is unavailable, but REQUIRE_GROQ=True.")
        return None
    if _GROQ_CLIENT is not None:
        return _GROQ_CLIENT

    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        try:
            from google.colab import userdata  # type: ignore

            api_key = userdata.get("GROQ_API_KEY")
        except Exception:
            api_key = None

    if not api_key:
        if REQUIRE_GROQ:
            raise RuntimeError(
                "GROQ_API_KEY is required for Section2 v3. "
                "Set it in Colab Secrets or environment variable."
            )
        return None
    _GROQ_CLIENT = Groq(api_key=api_key)
    return _GROQ_CLIENT


def get_model_rpm(model_name: str) -> int:
    return RPM_BY_MODEL.get(model_name, DEFAULT_RPM)


def throttle_requests(model_name: str) -> None:
    rpm = get_model_rpm(model_name)
    if rpm <= 0:
        return
    q = REQUEST_LOG_BY_MODEL.setdefault(model_name, deque())
    now = time.time()
    while q and now - q[0] > 60:
        q.popleft()
    if len(q) >= rpm:
        wait_s = max(60 - (now - q[0]) + 0.1, 0.1)
        time.sleep(wait_s)
        now = time.time()
        while q and now - q[0] > 60:
            q.popleft()
    q.append(time.time())


def safe_chat_completion(model_name: str, messages: list[dict], expect_json: bool = True) -> str | None:
    client = get_groq_client()
    if client is None:
        return None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            RUNTIME_STATS["llm_attempts_total"] = int(RUNTIME_STATS.get("llm_attempts_total", 0)) + 1
            _inc_counter(RUNTIME_STATS["llm_attempts_by_model"], model_name, 1)
            throttle_requests(model_name)
            kwargs = {
                "model": model_name,
                "messages": messages,
                "temperature": 0.1,
            }
            if expect_json:
                kwargs["response_format"] = {"type": "json_object"}
            resp = client.chat.completions.create(**kwargs)
            RUNTIME_STATS["llm_success_total"] = int(RUNTIME_STATS.get("llm_success_total", 0)) + 1
            _inc_counter(RUNTIME_STATS["llm_success_by_model"], model_name, 1)
            if int(RUNTIME_STATS.get("llm_attempts_total", 0)) % PROGRESS_CALL_INTERVAL == 0:
                log_progress(
                    "llm-progress",
                    attempts=int(RUNTIME_STATS.get("llm_attempts_total", 0)),
                    success=int(RUNTIME_STATS.get("llm_success_total", 0)),
                    fail=int(RUNTIME_STATS.get("llm_fail_total", 0)),
                    model=model_name,
                )
            return resp.choices[0].message.content
        except Exception:
            if attempt >= MAX_RETRIES:
                RUNTIME_STATS["llm_fail_total"] = int(RUNTIME_STATS.get("llm_fail_total", 0)) + 1
                _inc_counter(RUNTIME_STATS["llm_fail_by_model"], model_name, 1)
                return None
            time.sleep(RETRY_BASE_SECONDS * (2 ** (attempt - 1)) + random.uniform(0.0, 0.4))
    return None


def get_variants(seed: str) -> list[str]:
    seed = str(seed).strip()
    if not seed:
        return []
    if seed in VARIANT_CACHE:
        vals = VARIANT_CACHE.get(seed, [])
        if isinstance(vals, list):
            return [str(v) for v in vals][:MAX_VARIANTS_PER_CONCEPT]

    defaults = [seed, seed.replace("-", " "), seed.replace(" ", "-"), seed.replace("/", " ")]
    variants = []
    seen = set()
    for d in defaults:
        k = d.strip().lower()
        if k and k not in seen:
            seen.add(k)
            variants.append(d.strip())

    content = safe_chat_completion(
        model_name=MODEL_VARIANT_GEN,
        messages=[
            {
                "role": "system",
                "content": (
                    "Generate concise retrieval variants. "
                    "Return JSON only: {\"variants\": [\"...\"]}. "
                    "Keep phrases short and domain-consistent."
                ),
            },
            {"role": "user", "content": f"Seed concept: {seed}. Return up to 10 variants."},
        ],
        expect_json=True,
    )
    if content:
        try:
            data = json.loads(content)
            raw = data.get("variants", [])
            if isinstance(raw, list):
                for item in raw:
                    v = str(item).strip()
                    k = v.lower()
                    if v and k not in seen:
                        seen.add(k)
                        variants.append(v)
        except Exception:
            pass

    variants = variants[:MAX_VARIANTS_PER_CONCEPT]
    VARIANT_CACHE[seed] = variants
    VARIANT_CACHE_PATH.write_text(json.dumps(VARIANT_CACHE, indent=2), encoding="utf-8")
    return variants


def heuristic_label(match_type: str) -> tuple[str, str]:
    mt = str(match_type).lower()
    if "lexical" in mt:
        return "DIRECT", "heuristic lexical hit"
    if "fuzzy" in mt:
        return "INDIRECT", "heuristic fuzzy hit"
    return "NONE", "heuristic no match"


def classify_hit(section_key: str, concept_key: str, quote: str, context: str, heading: str, match_type: str, model_name: str) -> tuple[str, str]:
    fallback_label, fallback_rationale = heuristic_label(match_type)
    payload = {
        "section": section_key,
        "concept": concept_key,
        "quote": quote[:320],
        "heading": heading[:220],
        "context": context[:700],
        "match_type": match_type,
    }
    system_prompt = (
        "You classify evidence rows for Section II fundamentals. "
        "Return strict JSON: {\"label\":\"DIRECT|INDIRECT|NONE\",\"rationale\":\"...\"}. "
        "DIRECT: explicit support. INDIRECT: weak but relevant context. NONE: unrelated/ambiguous. "
        "Do not mix OSNR(optical) and SNR/ESNR(electrical). Do not alias Delta z and Delta r_min."
    )
    user_prompt = "Classify this row:\\n" + json.dumps(payload, ensure_ascii=False)
    content = safe_chat_completion(
        model_name=model_name,
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
    )
    if not content:
        return fallback_label, fallback_rationale
    try:
        data = json.loads(content)
        label = str(data.get("label", fallback_label)).upper().strip()
        if label not in {"DIRECT", "INDIRECT", "NONE"}:
            label = fallback_label
        rationale = str(data.get("rationale", fallback_rationale))
        return label, rationale
    except Exception:
        return fallback_label, fallback_rationale


def path_status(path: Path) -> dict:
    return {
        "path": str(path),
        "exists": path.exists(),
        "type": "dir" if path.is_dir() else ("file" if path.is_file() else "missing"),
    }


def write_input_manifest() -> None:
    manifest = {
        "generated_at_utc": pd.Timestamp.utcnow().isoformat(),
        "categories": [],
    }
    lines = ["# Section II v3 Input Manifest", ""]
    for cat, values in REQUIRED_INPUTS.items():
        rows = [path_status(p(v)) for v in values]
        n_ok = sum(1 for r in rows if r["exists"])
        manifest["categories"].append(
            {"category": cat, "n_total": len(rows), "n_ok": n_ok, "n_missing": len(rows) - n_ok, "items": rows}
        )
        lines.append(f"## {cat}")
        lines.append(f"- status: {n_ok}/{len(rows)} present")
        for row in rows:
            mark = "OK" if row["exists"] else "MISSING"
            lines.append(f"- {mark}: `{row['path']}` ({row['type']})")
        lines.append("")
    (OUTPUT_DIR / "input_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (OUTPUT_DIR / "input_manifest.md").write_text("\n".join(lines), encoding="utf-8")


def load_json_index() -> dict:
    idx = {}
    for fp in sorted(JSON_DIR.glob("O_ISAC_*_v4.json")):
        pid = fp.stem.replace("_v4", "")
        try:
            idx[pid] = json.loads(fp.read_text(encoding="utf-8", errors="ignore"))
        except Exception as exc:
            idx[pid] = {"_error": str(exc)}
    return idx


def _doc_id(paper_id: str, source_type: str, source_path: str, text: str) -> str:
    key = f"{paper_id}|{source_type}|{source_path}|{hashlib.sha1(text.encode('utf-8', errors='ignore')).hexdigest()[:12]}"
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:16]


def load_markdown_documents() -> list[dict]:
    all_md = list(PROCESSED_MD_DIR.rglob("*.md")) if PROCESSED_MD_DIR.exists() else []
    rows = []
    seen = set()
    for fp in sorted(all_md):
        if "O_ISAC_" not in fp.name:
            continue
        m = re.search(r"(O_ISAC_\d+)", fp.name)
        if not m:
            continue
        pid = m.group(1)
        text = fp.read_text(encoding="utf-8", errors="ignore")
        doc_hash = hashlib.sha1(text.encode("utf-8", errors="ignore")).hexdigest()[:16]
        dkey = (pid, "markdown", doc_hash)
        if dkey not in seen:
            seen.add(dkey)
            rows.append(
                {
                    "doc_id": _doc_id(pid, "markdown", str(fp), text),
                    "paper_id": pid,
                    "source_type": "markdown",
                    "source_path": str(fp),
                    "md_path": str(fp),
                    "lines": text.splitlines(),
                    "fuzzy_threshold": MARKDOWN_FUZZY_THRESHOLD,
                }
            )
        if SCAN_VISUAL_ANALYSIS:
            va = fp.parent / "visual_analysis.txt"
            if va.exists():
                vtext = va.read_text(encoding="utf-8", errors="ignore")
                vhash = hashlib.sha1(vtext.encode("utf-8", errors="ignore")).hexdigest()[:16]
                vkey = (pid, "visual_analysis", vhash)
                if vkey not in seen:
                    seen.add(vkey)
                    rows.append(
                        {
                            "doc_id": _doc_id(pid, "visual_analysis", str(va), vtext),
                            "paper_id": pid,
                            "source_type": "visual_analysis",
                            "source_path": str(va),
                            "md_path": str(fp),
                            "lines": vtext.splitlines(),
                            "fuzzy_threshold": MARKDOWN_FUZZY_THRESHOLD,
                        }
                    )
    return rows


def flatten_json_to_lines(obj, prefix: str = "") -> list[str]:
    out: list[str] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            key = f"{prefix}.{k}" if prefix else str(k)
            out.extend(flatten_json_to_lines(v, key))
        return out
    if isinstance(obj, list):
        for i, v in enumerate(obj):
            key = f"{prefix}[{i}]"
            out.extend(flatten_json_to_lines(v, key))
        return out
    if obj is None:
        return out
    sval = str(obj).strip()
    if not sval:
        return out
    if len(sval) > 360:
        sval = sval[:360] + " ..."
    out.append(f"{prefix}: {sval}" if prefix else sval)
    return out


def load_json_documents(json_index: dict) -> list[dict]:
    rows = []
    for pid, rec in sorted(json_index.items()):
        if not isinstance(rec, dict) or rec.get("_error"):
            continue
        lines = flatten_json_to_lines(rec)
        if not lines:
            continue
        text = "\n".join(lines)
        rows.append(
            {
                "doc_id": _doc_id(pid, "json", f"{JSON_DIR}/{pid}_v4.json", text),
                "paper_id": pid,
                "source_type": "json",
                "source_path": str(JSON_DIR / f"{pid}_v4.json"),
                "md_path": str(JSON_DIR / f"{pid}_v4.json"),
                "lines": lines,
                "fuzzy_threshold": JSON_FUZZY_THRESHOLD,
            }
        )
    return rows


def build_heading_map(lines: list[str]) -> dict[int, str]:
    current: list[str] = []
    out: dict[int, str] = {}
    for i, line in enumerate(lines):
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            title = line.strip("#").strip()
            if level <= len(current):
                current = current[: level - 1]
            current.append(title)
        out[i] = " > ".join(current) if current else "no_heading"
    return out


def get_context(lines: list[str], idx: int, window: int = 2) -> str:
    start = max(0, idx - window)
    end = min(len(lines), idx + window + 1)
    return "\n".join(lines[start:end])


def scan_hits(lines: list[str], variants: list[str], fuzzy_threshold: int = 86) -> list[tuple[int, str, str, str]]:
    hits = []
    for i, line in enumerate(lines):
        low = line.strip().lower()
        if not low:
            continue
        for v in variants:
            vlow = v.lower()
            if vlow in low:
                hits.append((i, line.strip(), v, "lexical"))
                break
            score = fuzz.partial_ratio(vlow, low)
            if score >= fuzzy_threshold:
                hits.append((i, line.strip(), v, f"fuzzy:{score}"))
                break
    return hits


def ensure_columns(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    out = df.copy()
    for col in cols:
        if col not in out.columns:
            out[col] = ""
    return out[cols]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_source_inventory(docs: list[dict], json_index: dict) -> None:
    if not docs:
        pd.DataFrame(columns=["source_type", "n_docs", "n_unique_papers"]).to_csv(
            OUTPUT_DIR / "source_inventory.csv", index=False
        )
        return
    df = pd.DataFrame(docs)
    inv = (
        df.groupby("source_type", as_index=False)
        .agg(n_docs=("doc_id", "nunique"), n_unique_papers=("paper_id", "nunique"))
        .sort_values("source_type")
    )
    inv.to_csv(OUTPUT_DIR / "source_inventory.csv", index=False)
    stats = {
        "n_json_papers": len(json_index),
        "n_doc_records": int(len(df)),
        "n_unique_papers_from_docs": int(df["paper_id"].nunique()),
        "by_source_type": inv.to_dict(orient="records"),
    }
    (OUTPUT_DIR / "source_inventory.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")


def build_anchor_table(all_df: pd.DataFrame) -> pd.DataFrame:
    all_df = ensure_columns(all_df, CANDIDATE_COLUMNS)
    if all_df.empty:
        return pd.DataFrame(columns=ANCHOR_COLUMNS)

    anc_rows = []
    for _, r in all_df.iterrows():
        claim_key = f"{r['section_key']}|{r['paper_id']}|{r['concept_key']}"
        claim_id = hashlib.sha1(claim_key.encode("utf-8")).hexdigest()[:12]
        anc_rows.append(
            {
                "claim_id": claim_id,
                "claim_key": claim_key,
                "section": r["section_key"],
                "paper_id": r["paper_id"],
                "concept": r["concept_key"],
                "strength": r["strength"],
                "quote": r["quote"],
                "line_start": r["line_start"],
                "line_end": r["line_end"],
                "heading_path": r["heading_path"],
            }
        )
    anc = pd.DataFrame(anc_rows)
    agg = anc.assign(
        is_direct=anc["strength"].astype(str).str.upper().eq("DIRECT"),
        is_indirect=anc["strength"].astype(str).str.upper().eq("INDIRECT"),
    ).groupby("claim_id", as_index=False)[["is_direct", "is_indirect"]].sum()
    agg["claim_supported"] = (agg["is_direct"] >= 1) | (agg["is_indirect"] >= 2)
    anc = anc.merge(agg[["claim_id", "claim_supported"]], on="claim_id", how="left")
    return ensure_columns(anc, ANCHOR_COLUMNS)


def write_retrieval_hits(all_df: pd.DataFrame) -> None:
    all_df = ensure_columns(all_df, CANDIDATE_COLUMNS)
    rows = []
    for _, r in all_df.iterrows():
        rows.append(
            {
                "paper_id": r["paper_id"],
                "source_type": r["source_type"],
                "source_path": r["source_path"],
                "section_key": r["section_key"],
                "concept_key": r["concept_key"],
                "variant": r["variant"],
                "match_type": r["match_type"],
                "strength": r["strength"],
                "label": r["label"],
                "model_used": r["model_used"],
                "line_start": r["line_start"],
                "line_end": r["line_end"],
                "heading_path": r["heading_path"],
                "md_path": r["md_path"],
                "quote": r["quote"],
            }
        )
    write_jsonl(OUTPUT_DIR / "retrieval_hits.jsonl", rows)


def write_evidence_graph(all_df: pd.DataFrame, anc: pd.DataFrame) -> None:
    all_df = ensure_columns(all_df, CANDIDATE_COLUMNS)
    anc = ensure_columns(anc, ANCHOR_COLUMNS)
    support_map = {}
    if not anc.empty:
        support_map = anc.drop_duplicates("claim_id").set_index("claim_id")["claim_supported"].to_dict()

    rows = []
    for _, r in all_df.iterrows():
        if str(r["strength"]).upper() not in {"DIRECT", "INDIRECT"}:
            continue
        claim_key = f"{r['section_key']}|{r['paper_id']}|{r['concept_key']}"
        claim_id = hashlib.sha1(claim_key.encode("utf-8")).hexdigest()[:12]
        rows.append(
            {
                "source_type": "paper",
                "source_id": r["paper_id"],
                "evidence_source_type": r["source_type"],
                "evidence_source_path": r["source_path"],
                "target_type": "concept",
                "target_id": f"{r['section_key']}::{r['concept_key']}",
                "claim_id": claim_id,
                "section_key": r["section_key"],
                "concept_key": r["concept_key"],
                "relation": "supports" if str(r["strength"]).upper() == "DIRECT" else "mentions",
                "strength": str(r["strength"]).upper(),
                "claim_supported": bool(support_map.get(claim_id, False)),
                "line_start": r["line_start"],
                "line_end": r["line_end"],
                "quote": r["quote"],
            }
        )
    write_jsonl(OUTPUT_DIR / "evidence_graph.jsonl", rows)


def write_cluster_map(all_df: pd.DataFrame, anc: pd.DataFrame) -> None:
    all_df = ensure_columns(all_df, CANDIDATE_COLUMNS)
    anc = ensure_columns(anc, ANCHOR_COLUMNS)
    if all_df.empty:
        pd.DataFrame(
            columns=[
                "cluster_id",
                "section_key",
                "concept_key",
                "n_rows",
                "n_unique_papers",
                "n_direct",
                "n_indirect",
                "n_none",
                "n_supported_claims",
            ]
        ).to_csv(OUTPUT_DIR / "cluster_map.csv", index=False)
        return

    tmp = all_df.copy()
    tmp["strength_u"] = tmp["strength"].astype(str).str.upper()
    base = tmp.groupby(["section_key", "concept_key"], as_index=False).agg(
        n_rows=("paper_id", "size"),
        n_unique_papers=("paper_id", "nunique"),
    )

    ctab = (
        tmp.pivot_table(
            index=["section_key", "concept_key"],
            columns="strength_u",
            values="paper_id",
            aggfunc="size",
            fill_value=0,
        )
        .reset_index()
        .rename_axis(None, axis=1)
    )
    for col in ["DIRECT", "INDIRECT", "NONE"]:
        if col not in ctab.columns:
            ctab[col] = 0

    claim_support = (
        anc.drop_duplicates(["claim_id", "section", "concept"])
        .groupby(["section", "concept"], as_index=False)["claim_supported"]
        .sum()
        .rename(columns={"section": "section_key", "concept": "concept_key", "claim_supported": "n_supported_claims"})
    )

    out = (
        base.merge(ctab[["section_key", "concept_key", "DIRECT", "INDIRECT", "NONE"]], on=["section_key", "concept_key"], how="left")
        .merge(claim_support, on=["section_key", "concept_key"], how="left")
        .fillna(0)
    )
    out = out.rename(columns={"DIRECT": "n_direct", "INDIRECT": "n_indirect", "NONE": "n_none"})
    out["cluster_id"] = out.apply(lambda r: f"{r['section_key']}::{r['concept_key']}", axis=1)
    out = out[
        [
            "cluster_id",
            "section_key",
            "concept_key",
            "n_rows",
            "n_unique_papers",
            "n_direct",
            "n_indirect",
            "n_none",
            "n_supported_claims",
        ]
    ]
    out.to_csv(OUTPUT_DIR / "cluster_map.csv", index=False)


def write_section2f_summary(all_df: pd.DataFrame, anc: pd.DataFrame, n_json_papers: int) -> None:
    all_df = ensure_columns(all_df, CANDIDATE_COLUMNS)
    anc = ensure_columns(anc, ANCHOR_COLUMNS)

    if all_df.empty:
        pd.DataFrame(
            columns=[
                "section_key",
                "concept_key",
                "n_rows",
                "n_unique_papers",
                "n_direct",
                "n_indirect",
                "n_none",
                "n_supported_claims",
            ]
        ).to_csv(OUTPUT_DIR / "section2F_summary_table.csv", index=False)
        summary = {
            "n_json_papers": n_json_papers,
            "n_markdown_rows": 0,
            "n_unique_papers": 0,
            "n_claims": 0,
            "n_supported_claims": 0,
            "by_section": [],
        }
        (OUTPUT_DIR / "section2F_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
        return

    tmp = all_df.copy()
    tmp["strength_u"] = tmp["strength"].astype(str).str.upper()
    table = tmp.groupby(["section_key", "concept_key"], as_index=False).agg(
        n_rows=("paper_id", "size"),
        n_unique_papers=("paper_id", "nunique"),
    )
    pivot = (
        tmp.pivot_table(
            index=["section_key", "concept_key"],
            columns="strength_u",
            values="paper_id",
            aggfunc="size",
            fill_value=0,
        )
        .reset_index()
        .rename_axis(None, axis=1)
    )
    for col in ["DIRECT", "INDIRECT", "NONE"]:
        if col not in pivot.columns:
            pivot[col] = 0
    support = (
        anc.drop_duplicates(["claim_id", "section", "concept"])
        .groupby(["section", "concept"], as_index=False)["claim_supported"]
        .sum()
        .rename(columns={"section": "section_key", "concept": "concept_key", "claim_supported": "n_supported_claims"})
    )
    table = (
        table.merge(pivot[["section_key", "concept_key", "DIRECT", "INDIRECT", "NONE"]], on=["section_key", "concept_key"], how="left")
        .merge(support, on=["section_key", "concept_key"], how="left")
        .fillna(0)
        .rename(columns={"DIRECT": "n_direct", "INDIRECT": "n_indirect", "NONE": "n_none"})
    )
    table = table[
        [
            "section_key",
            "concept_key",
            "n_rows",
            "n_unique_papers",
            "n_direct",
            "n_indirect",
            "n_none",
            "n_supported_claims",
        ]
    ]
    table.to_csv(OUTPUT_DIR / "section2F_summary_table.csv", index=False)

    claim_df = anc.drop_duplicates("claim_id") if not anc.empty else pd.DataFrame(columns=["claim_id", "claim_supported", "section"])
    by_section = []
    for sec in ["2A", "2B", "2C", "2D", "2E"]:
        sub = table[table["section_key"] == sec]
        csub = claim_df[claim_df["section"] == sec] if "section" in claim_df.columns else pd.DataFrame()
        by_section.append(
            {
                "section_key": sec,
                "n_rows": int(sub["n_rows"].sum()) if not sub.empty else 0,
                "n_unique_papers": int(tmp[tmp["section_key"] == sec]["paper_id"].nunique()),
                "n_claims": int(len(csub)),
                "n_supported_claims": int(csub["claim_supported"].sum()) if not csub.empty else 0,
            }
        )

    summary = {
        "n_json_papers": int(n_json_papers),
        "n_candidate_rows": int(len(all_df)),
        "n_unique_papers": int(all_df["paper_id"].nunique()),
        "n_claims": int(len(claim_df)),
        "n_supported_claims": int(claim_df["claim_supported"].sum()) if not claim_df.empty else 0,
        "source_types": sorted(all_df["source_type"].astype(str).unique().tolist()) if "source_type" in all_df.columns else [],
        "by_section": by_section,
    }
    (OUTPUT_DIR / "section2F_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")


def write_section2g_dual_view(all_df: pd.DataFrame, anc: pd.DataFrame) -> None:
    all_df = ensure_columns(all_df, CANDIDATE_COLUMNS)
    anc = ensure_columns(anc, ANCHOR_COLUMNS)
    sections = ["2A", "2B", "2C", "2D", "2E"]
    cmp_rows = []
    ex_rows = []
    for sec in sections:
        raw = set(all_df[all_df["section_key"] == sec]["paper_id"].astype(str)) if not all_df.empty else set()
        direct = set(
            all_df[(all_df["section_key"] == sec) & (all_df["strength"].astype(str).str.upper() == "DIRECT")]["paper_id"].astype(str)
        ) if not all_df.empty else set()
        supported = set(
            anc[(anc["section"] == sec) & (anc["claim_supported"] == True)]["paper_id"].astype(str)
        ) if not anc.empty else set()

        cmp_rows.append(
            {
                "section_key": sec,
                "raw_paper_count": len(raw),
                "direct_paper_count": len(direct),
                "supported_paper_count": len(supported),
                "raw_vs_supported_intersection": len(raw & supported),
                "raw_only_count": len(raw - supported),
                "supported_only_count": len(supported - raw),
                "supported_ratio": round((len(supported) / len(raw)) if raw else 0.0, 4),
            }
        )
        ex_rows.append({"section_key": sec, "group": "raw_only", "paper_ids": ";".join(sorted(list(raw - supported))[:30])})
        ex_rows.append({"section_key": sec, "group": "supported_only", "paper_ids": ";".join(sorted(list(supported - raw))[:30])})

    cmp_df = pd.DataFrame(cmp_rows)
    cmp_df.to_csv(OUTPUT_DIR / "s2g_dual_view_cmp.csv", index=False)
    pd.DataFrame(ex_rows).to_csv(OUTPUT_DIR / "s2g_dual_view_ex.csv", index=False)

    md_lines = ["# Section 2G Dual-View Comparison", ""]
    md_lines.append("This audit compares raw retrieval coverage against claim-supported coverage by section.")
    md_lines.append("")
    for _, r in cmp_df.iterrows():
        md_lines.append(f"## {r['section_key']}")
        md_lines.append(f"- raw_paper_count: {int(r['raw_paper_count'])}")
        md_lines.append(f"- direct_paper_count: {int(r['direct_paper_count'])}")
        md_lines.append(f"- supported_paper_count: {int(r['supported_paper_count'])}")
        md_lines.append(f"- raw_vs_supported_intersection: {int(r['raw_vs_supported_intersection'])}")
        md_lines.append(f"- raw_only_count: {int(r['raw_only_count'])}")
        md_lines.append(f"- supported_only_count: {int(r['supported_only_count'])}")
        md_lines.append(f"- supported_ratio: {float(r['supported_ratio']):.4f}")
        md_lines.append("")
    (OUTPUT_DIR / "section2G_dual_view_report.md").write_text("\n".join(md_lines), encoding="utf-8")


def run_pipeline() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    init_runtime_stats()
    write_input_manifest()
    log_progress("stage-start", stage="input_manifest_written", output_dir=str(OUTPUT_DIR))

    json_index = load_json_index()
    markdown_docs = load_markdown_documents()
    json_docs = load_json_documents(json_index)
    scan_docs = markdown_docs + json_docs
    write_source_inventory(scan_docs, json_index)
    log_progress(
        "source-inventory",
        json_papers=len(json_index),
        markdown_docs=len(markdown_docs),
        json_docs=len(json_docs),
        total_scan_docs=len(scan_docs),
    )
    write_progress_snapshot(
        "source_inventory",
        json_papers=len(json_index),
        markdown_docs=len(markdown_docs),
        json_docs=len(json_docs),
        total_scan_docs=len(scan_docs),
    )
    print("JSON papers:", len(json_index))
    print("Markdown docs:", len(markdown_docs))
    print("JSON docs:", len(json_docs))
    print("Total scan docs:", len(scan_docs))
    has_llm = get_groq_client() is not None
    if REQUIRE_GROQ and not has_llm:
        raise RuntimeError("REQUIRE_GROQ=True but Groq client is unavailable.")
    print("LLM classification:", "enabled" if has_llm else "disabled (REQUIRE_GROQ=False)")
    candidate_path = OUTPUT_DIR / "s2_all_cand_v3.csv"
    checkpoint_path = CHECKPOINT_DIR / "section2_scan_checkpoint.jsonl"
    full_rescan = str(RUN_PROFILE).upper() == "FULL_RESCAN"
    use_resume = RESUME and (not full_rescan)

    if use_resume and candidate_path.exists():
        all_df = pd.read_csv(candidate_path)
        all_df = ensure_columns(all_df, CANDIDATE_COLUMNS)
        print("Resume active: loaded existing candidate file:", candidate_path, "rows=", len(all_df))
        log_progress("resume-candidates", path=str(candidate_path), rows=len(all_df))
        write_progress_snapshot("resume_candidates", rows=len(all_df), path=str(candidate_path))
    else:
        if full_rescan and candidate_path.exists():
            print("RUN_PROFILE=FULL_RESCAN: ignoring existing candidate file and rescanning all sources.")
            log_progress("full-rescan", action="ignoring_existing_candidates", path=str(candidate_path))
        concept_variants: dict[tuple[str, str], list[str]] = {}
        log_progress("stage-start", stage="variant_generation")
        for sec, cdict in SECTION2_CONCEPTS.items():
            for concept, seeds in cdict.items():
                variants = []
                for s in seeds:
                    variants.extend(get_variants(s))
                # Defensive fallback when variant generation is unavailable.
                if not variants:
                    variants = list(seeds)
                dedup = []
                seen = set()
                for v in variants:
                    k = str(v).strip().lower()
                    if k and k not in seen:
                        seen.add(k)
                        dedup.append(str(v).strip())
                concept_variants[(sec, concept)] = dedup[:MAX_VARIANTS_PER_CONCEPT]
        log_progress(
            "variant-generation-done",
            concept_groups=len(concept_variants),
            cached_terms=len(VARIANT_CACHE),
            llm_attempts=int(RUNTIME_STATS.get("llm_attempts_total", 0)),
        )
        write_progress_snapshot(
            "variant_generation_done",
            concept_groups=len(concept_variants),
            cached_terms=len(VARIANT_CACHE),
        )

        rows = []
        ckf = checkpoint_path.open("w", encoding="utf-8")
        stats = {
            "docs_processed": 0,
            "hits_total": 0,
            "rows_total": 0,
            "hits_by_source": defaultdict(int),
            "rows_by_source": defaultdict(int),
            "hits_by_section": defaultdict(int),
            "rows_by_section": defaultdict(int),
            "start_ts": time.time(),
        }
        next_log_ts = time.time() + PROGRESS_TIME_INTERVAL_SECONDS
        try:
            for doc in tqdm(scan_docs, desc="scan"):
                stats["docs_processed"] += 1
                heading = build_heading_map(doc["lines"])
                doc_hits = 0
                doc_rows = 0
                for sec, cdict in SECTION2_CONCEPTS.items():
                    for concept in cdict.keys():
                        variants = concept_variants.get((sec, concept), [])
                        hits = scan_hits(doc["lines"], variants, fuzzy_threshold=int(doc.get("fuzzy_threshold", MARKDOWN_FUZZY_THRESHOLD)))
                        if MAX_HITS_PER_CONCEPT_PER_PAPER > 0:
                            hits = hits[:MAX_HITS_PER_CONCEPT_PER_PAPER]
                        doc_hits += len(hits)
                        stats["hits_by_section"][sec] += len(hits)
                        for idx, quote, variant, mtype in hits:
                            ctx = get_context(doc["lines"], idx, 2)[:MAX_CONTEXT_CHARS]
                            label, rationale = classify_hit(
                                section_key=sec,
                                concept_key=concept,
                                quote=quote,
                                context=ctx,
                                heading=heading.get(idx, "no_heading"),
                                match_type=mtype,
                                model_name=MODEL_PASS1,
                            )
                            model_used = MODEL_PASS1
                            if USE_ESCALATION and label in ESCALATE_LABELS:
                                lbl2, rat2 = classify_hit(
                                    section_key=sec,
                                    concept_key=concept,
                                    quote=quote,
                                    context=ctx,
                                    heading=heading.get(idx, "no_heading"),
                                    match_type=mtype,
                                    model_name=MODEL_PASS2,
                                )
                                label, rationale = lbl2, rat2
                                model_used = MODEL_PASS2
                            rec = {
                                "paper_id": doc["paper_id"],
                                "source_type": doc["source_type"],
                                "source_path": doc["source_path"],
                                "md_path": doc["md_path"],
                                "section_key": sec,
                                "concept_key": concept,
                                "variant": variant,
                                "match_type": mtype,
                                "quote": quote,
                                "line_start": idx + 1,
                                "line_end": idx + 1,
                                "heading_path": heading.get(idx, "no_heading"),
                                "context": ctx,
                                "label": label,
                                "strength": "DIRECT" if label == "DIRECT" else ("INDIRECT" if label == "INDIRECT" else "NONE"),
                                "rationale": rationale,
                                "model_used": model_used,
                            }
                            rows.append(rec)
                            doc_rows += 1
                            stats["rows_by_section"][sec] += 1
                            ckf.write(json.dumps(rec, ensure_ascii=False) + "\n")

                stats["hits_total"] += doc_hits
                stats["rows_total"] += doc_rows
                stype = str(doc.get("source_type", "unknown"))
                stats["hits_by_source"][stype] += doc_hits
                stats["rows_by_source"][stype] += doc_rows

                should_log = False
                if stats["docs_processed"] % PROGRESS_DOC_INTERVAL == 0:
                    should_log = True
                if time.time() >= next_log_ts:
                    should_log = True
                if stats["docs_processed"] == len(scan_docs):
                    should_log = True
                if should_log:
                    elapsed = max(time.time() - stats["start_ts"], 1e-9)
                    rate = stats["docs_processed"] / elapsed
                    remaining = max(len(scan_docs) - stats["docs_processed"], 0)
                    eta = (remaining / rate) if rate > 0 else None
                    pct = (100.0 * stats["docs_processed"] / len(scan_docs)) if scan_docs else 100.0
                    log_progress(
                        "scan-progress",
                        docs=f"{stats['docs_processed']}/{len(scan_docs)}",
                        pct=f"{pct:.2f}",
                        rows=stats["rows_total"],
                        hits=stats["hits_total"],
                        llm_attempts=int(RUNTIME_STATS.get("llm_attempts_total", 0)),
                        llm_success=int(RUNTIME_STATS.get("llm_success_total", 0)),
                        eta=_fmt_eta(eta),
                    )
                    write_progress_snapshot(
                        "scan_progress",
                        docs_processed=stats["docs_processed"],
                        docs_total=len(scan_docs),
                        pct=round(pct, 4),
                        rows_total=stats["rows_total"],
                        hits_total=stats["hits_total"],
                        hits_by_source=dict(stats["hits_by_source"]),
                        rows_by_source=dict(stats["rows_by_source"]),
                        hits_by_section=dict(stats["hits_by_section"]),
                        rows_by_section=dict(stats["rows_by_section"]),
                        eta_seconds=eta if eta is not None else -1,
                    )
                    next_log_ts = time.time() + PROGRESS_TIME_INTERVAL_SECONDS
        finally:
            ckf.close()

        all_df = ensure_columns(pd.DataFrame(rows), CANDIDATE_COLUMNS)
        all_df.to_csv(candidate_path, index=False)
        print("Saved:", candidate_path, "rows=", len(all_df))
        log_progress("stage-done", stage="scan_complete", candidate_rows=len(all_df), path=str(candidate_path))
        write_progress_snapshot("scan_complete", candidate_rows=len(all_df), path=str(candidate_path))
    for sec in ["2A", "2B", "2C", "2D", "2E"]:
        fp = OUTPUT_DIR / f"section{sec}_evidence_v3.csv"
        d = all_df[all_df["section_key"] == sec].copy() if not all_df.empty else pd.DataFrame()
        d.to_csv(fp, index=False)
        print("Saved:", fp, "rows=", len(d))
    all_df.to_csv(OUTPUT_DIR / "s2_all_cand_v3.csv", index=False)

    anc = build_anchor_table(all_df)
    anc.to_csv(OUTPUT_DIR / "anchor_table.csv", index=False)
    write_retrieval_hits(all_df)
    write_evidence_graph(all_df, anc)
    write_cluster_map(all_df, anc)

    violations = []
    seen = set()
    for sec in ["2A", "2B", "2C", "2D", "2E"]:
        d = all_df[all_df["section_key"] == sec].copy()
        if d.empty:
            continue
        for pid, grp in d.groupby("paper_id"):
            direct = (grp["strength"].astype(str).str.upper() == "DIRECT").sum()
            indirect = (grp["strength"].astype(str).str.upper() == "INDIRECT").sum()
            if direct < 1 and indirect < 2:
                key = (pid, sec, "EVIDENCE_WEAK")
                if key not in seen:
                    seen.add(key)
                    violations.append(
                        {
                            "paper_id": pid,
                            "section": sec,
                            "category": "EVIDENCE_WEAK",
                            "severity": "MINOR",
                            "reason": "support gate failed",
                            "evidence": f"direct={direct}; indirect={indirect}",
                        }
                    )
        for _, r in d.iterrows():
            quote = str(r.get("quote", "")).lower()
            pid = str(r.get("paper_id", ""))
            if "osnr" in quote and (" snr" in quote or "esnr" in quote):
                key = (pid, sec, "METRIC_PLANE")
                if key not in seen:
                    seen.add(key)
                    violations.append(
                        {
                            "paper_id": pid,
                            "section": sec,
                            "category": "METRIC_PLANE",
                            "severity": "MAJOR",
                            "reason": "osnr/snr co-mention",
                            "evidence": quote[:180],
                        }
                    )
            alias_mix = (("spatial resolution" in quote) or ("delta z" in quote)) and (
                ("range resolution" in quote) or ("delta r" in quote) or ("drmin" in quote)
            )
            if alias_mix:
                key = (pid, sec, "METRIC_ALIASING")
                if key not in seen:
                    seen.add(key)
                    violations.append(
                        {
                            "paper_id": pid,
                            "section": sec,
                            "category": "METRIC_ALIASING",
                            "severity": "MAJOR",
                            "reason": "delta z / delta r risk",
                            "evidence": quote[:180],
                        }
                    )

    viol_cols = ["paper_id", "section", "category", "severity", "reason", "evidence"]
    pd.DataFrame(violations, columns=viol_cols).to_csv(OUTPUT_DIR / "contract_violations.csv", index=False)
    write_section2f_summary(all_df, anc, n_json_papers=len(json_index))
    write_section2g_dual_view(all_df, anc)
    (OUTPUT_DIR / "axis_definitions.md").write_text(
        "\n".join(
            [
                "# Section 2 Axis Definitions (v3)",
                "",
                "Axis-1: 2A model/plane, 2B channel, 2C hardware, 2D metrics, 2E coupling.",
                "Axis-2: claim_supported gate = >=1 DIRECT or >=2 INDIRECT.",
                "Axis-3: section2 governance lock for plane-separation and metric aliasing.",
            ]
        ),
        encoding="utf-8",
    )
    (OUTPUT_DIR / "mapping_rules.md").write_text(
        "\n".join(
            [
                "# Section 2 Mapping Rules (v3)",
                "",
                "1. Full scan over processed markdowns + O_ISAC JSON.",
                "2. No OSNR/SNR plane conflation.",
                "3. No Delta z / Delta r_min substitution.",
                "4. COMST + PRISMA input paths are tracked via input_manifest.",
            ]
        ),
        encoding="utf-8",
    )
    duration_s = None
    if RUNTIME_STATS.get("start_time") is not None:
        duration_s = max(time.time() - float(RUNTIME_STATS["start_time"]), 0.0)
    runtime_summary = {
        "timestamp_utc": pd.Timestamp.utcnow().isoformat(),
        "duration_seconds": duration_s,
        "llm_attempts_total": int(RUNTIME_STATS.get("llm_attempts_total", 0)),
        "llm_success_total": int(RUNTIME_STATS.get("llm_success_total", 0)),
        "llm_fail_total": int(RUNTIME_STATS.get("llm_fail_total", 0)),
        "llm_attempts_by_model": dict(RUNTIME_STATS.get("llm_attempts_by_model", {})),
        "llm_success_by_model": dict(RUNTIME_STATS.get("llm_success_by_model", {})),
        "llm_fail_by_model": dict(RUNTIME_STATS.get("llm_fail_by_model", {})),
    }
    _runtime_summary_path().write_text(json.dumps(runtime_summary, indent=2), encoding="utf-8")
    write_progress_snapshot("postprocess_complete", runtime_summary_path=str(_runtime_summary_path()))
    log_progress(
        "run-summary",
        duration_seconds=round(duration_s, 2) if duration_s is not None else "unknown",
        llm_attempts=int(RUNTIME_STATS.get("llm_attempts_total", 0)),
        llm_success=int(RUNTIME_STATS.get("llm_success_total", 0)),
        llm_fail=int(RUNTIME_STATS.get("llm_fail_total", 0)),
    )

    files = [
        "input_manifest.json",
        "input_manifest.md",
        "source_inventory.csv",
        "source_inventory.json",
        "runtime_progress.log",
        "runtime_summary.json",
        "retrieval_hits.jsonl",
        "evidence_graph.jsonl",
        "cluster_map.csv",
        "section2A_evidence_v3.csv",
        "section2B_evidence_v3.csv",
        "section2C_evidence_v3.csv",
        "section2D_evidence_v3.csv",
        "section2E_evidence_v3.csv",
        "section2F_summary.json",
        "section2F_summary_table.csv",
        "s2g_dual_view_cmp.csv",
        "s2g_dual_view_ex.csv",
        "section2G_dual_view_report.md",
        "s2_all_cand_v3.csv",
        "anchor_table.csv",
        "contract_violations.csv",
        "axis_definitions.md",
        "mapping_rules.md",
    ]
    lines = []
    for name in files:
        lines.append(f"{name}: {'OK' if (OUTPUT_DIR / name).exists() else 'MISSING'}")
    lines.append(f"checkpoints/runtime_progress.json: {'OK' if _progress_json_path().exists() else 'MISSING'}")
    lines.append(f"checkpoints/runtime_prog_snaps.csv: {'OK' if _progress_csv_path().exists() else 'MISSING'}")
    lines.append("")
    lines.append(f"n_total_json_papers: {len(json_index)}")
    sinv = OUTPUT_DIR / "source_inventory.json"
    if sinv.exists():
        try:
            meta = json.loads(sinv.read_text(encoding="utf-8"))
            lines.append(f"n_total_scan_docs: {meta.get('n_doc_records', 0)}")
            lines.append(f"n_unique_papers_from_docs: {meta.get('n_unique_papers_from_docs', 0)}")
            for row in meta.get("by_source_type", []):
                st = str(row.get("source_type", "unknown"))
                lines.append(f"docs_{st}: {int(row.get('n_docs', 0))}")
                lines.append(f"papers_{st}: {int(row.get('n_unique_papers', 0))}")
        except Exception as exc:
            lines.append(f"source_inventory_error: {exc}")
    for sec in ["A", "B", "C", "D", "E"]:
        fp = OUTPUT_DIR / f"section2{sec}_evidence_v3.csv"
        if fp.exists():
            d = pd.read_csv(fp)
            lines.append(f"section2{sec}_rows: {len(d)}")
            lines.append(f"section2{sec}_unique_papers: {d['paper_id'].nunique() if 'paper_id' in d.columns else 0}")
    vpath = OUTPUT_DIR / "contract_violations.csv"
    if vpath.exists():
        try:
            v = pd.read_csv(vpath)
        except pd.errors.EmptyDataError:
            v = pd.DataFrame(columns=["paper_id", "section", "category", "severity", "reason", "evidence"])
        lines.append(f"contract_violations_rows: {len(v)}")
    (OUTPUT_DIR / "readiness_report.md").write_text("\n".join(lines), encoding="utf-8")
    print("Saved:", OUTPUT_DIR / "readiness_report.md")


if __name__ == "__main__":
    run_pipeline()
