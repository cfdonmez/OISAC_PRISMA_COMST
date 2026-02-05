# codex_batch_prompter_v2_anchor.py
# Generates copy-paste Codex prompts for sequential O_ISAC batches,
# now with Section II (A–E) anchor mapping + coverage bookkeeping.

from __future__ import annotations
import argparse
import json
import os
import re
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Set, Tuple, Optional

OISAC_RE = re.compile(r"(O_ISAC_(\d{3}))")
DEFAULT_BATCH_SIZE = 12
STATE_PATH = os.path.join("analysis", "codex_batch_state.json")

# -------------------------
# Anchor parsing (Section II)
# -------------------------

ANCHOR_HDR_RE = re.compile(r"^\s*#{1,6}\s*(?:(?:Section\s*)?II[\.\-\s:]*)?([A-E])[\.\:\-\s]+(.+?)\s*$", re.IGNORECASE)

DEFAULT_ANCHORS = [
    {"anchor_id": "II-A", "title": "Unified system model + integration modes", "keywords": ["system model", "unified", "integration", "architecture", "modality"]},
    {"anchor_id": "II-B", "title": "Fiber and wireless channel fundamentals", "keywords": ["channel", "turbulence", "path loss", "impulse response", "fiber", "FSO", "VLC"]},
    {"anchor_id": "II-C", "title": "Hardware blocks and enablers", "keywords": ["transceiver", "OPA", "RIS", "laser", "photodetector", "front-end", "ADC", "DSP"]},
    {"anchor_id": "II-D", "title": "Sensing principles + metric contract (Δr_min/Δz/CRQ_Δ, planes)", "keywords": ["range resolution", "Δr", "dr_min", "gauge length", "Δz", "CRQ", "OSNR", "SNR"]},
    {"anchor_id": "II-E", "title": "ISAC coupling and trade-offs", "keywords": ["trade-off", "coupling", "joint", "communication-sensing", "resource allocation"]},
]

def ensure_analysis_dir() -> None:
    os.makedirs("analysis", exist_ok=True)

def find_file_in_repo(filename: str, roots: List[str] | None = None) -> Optional[str]:
    roots = roots or [".", "analysis", "drafts", "reference_compendium", "data"]
    # direct checks
    for r in roots:
        p = os.path.join(r, filename)
        if os.path.exists(p):
            return p
    # deep search (bounded)
    for r in roots:
        if not os.path.exists(r):
            continue
        for dirpath, _, filenames in os.walk(r):
            if filename in filenames:
                return os.path.join(dirpath, filename)
    return None

def load_section2_anchors(template_hint: Optional[str] = None) -> Tuple[str, List[Dict]]:
    """
    Try to locate and parse Section II template anchors (A–E).
    Returns (resolved_path, anchors_list).
    If parsing fails, returns fallback DEFAULT_ANCHORS with path 'NOT_FOUND_OR_UNPARSEABLE'.
    """
    candidate_names = []
    if template_hint:
        candidate_names.append(template_hint)

    # common names you used
    candidate_names += [
        "section_02_fundamentals_template.md",
        "Section_02_fundamentals_template.md",
        "section_02_template.md",
        "section_02_fundamentals.md",
    ]

    resolved = None
    for name in candidate_names:
        if os.path.isabs(name) and os.path.exists(name):
            resolved = name
            break
        resolved = find_file_in_repo(os.path.basename(name))
        if resolved:
            break

    if not resolved or not os.path.exists(resolved):
        return "NOT_FOUND_OR_UNPARSEABLE", DEFAULT_ANCHORS

    try:
        with open(resolved, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception:
        return "NOT_FOUND_OR_UNPARSEABLE", DEFAULT_ANCHORS

    anchors: List[Dict] = []
    seen_letters: Set[str] = set()

    for line in lines:
        m = ANCHOR_HDR_RE.match(line)
        if not m:
            continue
        letter = m.group(1).upper()
        title = m.group(2).strip()
        if letter in {"A", "B", "C", "D", "E"} and letter not in seen_letters:
            seen_letters.add(letter)
            anchors.append({
                "anchor_id": f"II-{letter}",
                "title": title,
                # lightweight keywords from title; Codex will still decide using HeadingPath semantics
                "keywords": [w.lower() for w in re.findall(r"[A-Za-zΔ_]+", title) if len(w) >= 3][:10]
            })

        if len(seen_letters) == 5:
            break

    if len(anchors) < 3:
        # too weak => fallback
        return resolved, DEFAULT_ANCHORS

    # ensure all A–E exist; fill missing from default
    by_id = {a["anchor_id"]: a for a in anchors}
    merged = []
    for d in DEFAULT_ANCHORS:
        merged.append(by_id.get(d["anchor_id"], d))
    return resolved, merged

def format_anchor_map(anchors: List[Dict]) -> str:
    # Render a compact anchor map block for the prompt
    out = []
    for a in anchors:
        kws = ", ".join(a.get("keywords", [])[:8])
        out.append(f"- {a['anchor_id']}: {a['title']} | keywords: {kws}")
    return "\n".join(out)

# -------------------------
# Prompt template (two-stage + anchors)
# -------------------------

PROMPT_TEMPLATE_ANCHOR = r"""ROLE
You are an evidence-mining metric-governance auditor. Process ONE batch only, then STOP.

BATCH
- batch_id: {batch_id}
- paper_ids ({n}): {paper_ids_block}

REPO PATHS (RELATIVE)
- extraction repo: data/extraction_results_v4/
- markdown repo:   data/processed_markdowns/
- outputs:         analysis/

SECTION II ANCHOR MAP (MUST USE)
You MUST assign each VALID candidate/evidence hit to exactly one anchor:
{anchor_map}

Anchor assignment rule:
- Use the HeadingPath + local content semantics.
- If uncertain, set section2_anchor = "II-UNK" and explain briefly in invalid_reason.

CONTEXT (LOCKED TO SECTION I)
- Δr_min := v/(2 B_eff) (two-way bandwidth-limited ranging resolution concept)
- Δz := fiber spatial granularity / gauge length / segment length (NOT Δr_min)
- CRQ_Δ := R/Δr_min comparable ONLY where Δr_min is defensible
- Do NOT mix planes: OSNR (optical plane) vs electrical SNR (post-detection)

HARD RULES
1) Do not edit any manuscript or prose files.
2) Do not add or modify citation keys [O_ISAC_XXX].
3) Conservative labeling (Stage-2): if not defensible => AMBIGUOUS.
4) NO-REFERENCES EVIDENCE: any match under headings containing "References", "Bibliography", "Ref." is INVALID.
5) Evidence excerpt must be ≤25 words and MUST contain the key term(s).
6) STOP after this batch.

DISCOVERY (STRUCTURED)
A) Locate canonical extraction source(s) under data/extraction_results_v4/.
   - Use unified JSON/JSONL/CSV if present, else per-paper JSON.
   - For each paper_id, record exact extraction_json_path.
B) For each paper_id, locate processed markdown:
   - Search under data/processed_markdowns/** for a .md containing the paper_id.
   - Record markdown_path.

TWO-STAGE EVIDENCE MECHANISM (RECALL↑ then PRECISION↑)
Stage-1 (Candidate Harvest; NOT conservative)
- Scan FULL FILE (windowed around hits) and collect candidates even if only partial clues exist.
- Candidate flags:
  (C1) DRMIN_CANDIDATE if ANY of:
       - "range resolution" / "ranging resolution" / "distance resolution"
       - OR "c/(2B" / "v/(2B" / "c/2B" / "(2B" near delta-r tokens
       - OR "bandwidth-limited" AND "resolution"
  (C2) DZ_CANDIDATE if ANY of:
       - "gauge length" / "segment length" / "spatial resolution along" / "Rayleigh" + ("fiber"/"DAS"/"DFOS")
  (C3) OSNR_CANDIDATE if "OSNR" or "O-SNR"
  (C4) ESNR_CANDIDATE if:
       - "electrical SNR" OR
       - ("SNR" AND ("after photodetection" OR "post-detection" OR "after detection"))
- For each candidate, store HeadingPath + ≤25-word excerpt + where_hint.
- Discard candidates under References headings.

Stage-2 (Verification; conservative, COMST-safe)
Verified Evidence flags:

(1) DRMIN_TEXT_EVIDENCE = 1 ONLY if BOTH are satisfied in SAME local window (±200 chars):
    - ranging phrase: "range resolution" OR "ranging resolution" OR "distance resolution"
    AND
    - formula token: "c/2B" OR "c/(2B" OR "v/(2B"
    Locator must include BOTH.

(2) DZ_TEXT_EVIDENCE = 1 ONLY if ALL THREE appear in SAME local window:
    - fiber anchor: "fiber" OR "DAS" OR "DFOS" OR "φ-OTDR" OR "Rayleigh"
    AND
    - Δz semantics: "gauge length" OR "segment length" OR "spatial resolution along" OR "spatial resolution of DAS"
    AND
    - numeric+unit: number immediately followed by "m" or "meter"
    Locator must include numeric+unit plus Δz cue.

(3) OSNR_TEXT_EVIDENCE = 1 if "OSNR" or "O-SNR" appears in non-References window.
(4) ESNR_TEXT_EVIDENCE = 1 if:
    - exact "electrical SNR" OR
    - ("SNR" AND ("after photodetection" OR "post-detection" OR "after detection"))
    in non-References window.

OVERRIDE LOGIC (STRICT)
- If extraction indicates co-occurrence (range_resolution_m AND spatial_resolution_m):
    default AMBIGUOUS.
    Override to DRMIN_DEFENSIBLE only if DRMIN_TEXT_EVIDENCE=1.
    Override to DZ_DEFENSIBLE only if DZ_TEXT_EVIDENCE=1.
    If both evidences present => keep AMBIGUOUS and flag CONFLICT.
- If no co-occurrence:
    still require verified text evidence to override away from AMBIGUOUS.

- SNR plane:
  - If osnr_db and snr_db co-occur => default AMBIGUOUS.
    Override OSNR_PLANE only if OSNR_TEXT_EVIDENCE=1.
    Override ESNR_PLANE only if ESNR_TEXT_EVIDENCE=1.

OUTPUTS (WRITE / APPEND SAFELY)
Create analysis/ if missing.

1) analysis/II_text_candidates_index.csv   (Stage-1 output)
   - If rows for (batch_id, paper_id) exist, remove them first, then append.
   Columns:
   batch_id, paper_id, section2_anchor, extraction_json_path, markdown_path,
   DRMIN_CANDIDATE, DZ_CANDIDATE, OSNR_CANDIDATE, ESNR_CANDIDATE,
   candidate_locator_drmin, candidate_locator_dz, candidate_locator_osnr, candidate_locator_esnr,
   invalid_reason

2) analysis/II_text_evidence_index.csv     (Stage-2 verified output)
   - If rows for (batch_id, paper_id) exist, remove them first, then append.
   Columns:
   batch_id, paper_id, section2_anchor, extraction_json_path, markdown_path,
   DRMIN_TEXT_EVIDENCE, DZ_TEXT_EVIDENCE, OSNR_TEXT_EVIDENCE, ESNR_TEXT_EVIDENCE,
   evidence_locator_drmin, evidence_locator_dz, evidence_locator_osnr, evidence_locator_esnr,
   invalid_reason

3) analysis/II_high_confidence_metric_index_v2_partial_{batch_id}.csv
   Columns:
   paper_id, section2_anchor, resolution_defensibility_label, snr_plane_label, rule_applied,
   markdown_path, extraction_json_path

4) analysis/II_anchor_coverage_running.csv   (append/update)
   - Maintain running counts per anchor over ALL batches processed so far.
   Columns:
   section2_anchor,
   cand_drmin, cand_dz, cand_osnr, cand_esnr,
   ev_drmin, ev_dz, ev_osnr, ev_esnr,
   last_updated_batch

5) analysis/II_batch_report_{batch_id}.md
   - paper_ids processed
   - Stage-1 candidate counts (global + per anchor)
   - Stage-2 verified counts (global + per anchor)
   - overrides applied (paper_id, from→to, locator)
   - discarded matches due to References rule
   - STOP instruction

STOP after writing outputs. Do not process the next batch until user approval.
"""

# -------------------------
# State + batching
# -------------------------

@dataclass
class BatchState:
    batch_size: int
    paper_ids: List[str]
    next_index: int
    next_batch_num: int
    batches: Dict[str, List[str]]  # batch_id -> paper_ids
    created_at: str
    section2_template_path: str
    anchors: List[Dict]

    def to_dict(self) -> dict:
        return {
            "batch_size": self.batch_size,
            "paper_ids": self.paper_ids,
            "next_index": self.next_index,
            "next_batch_num": self.next_batch_num,
            "batches": self.batches,
            "created_at": self.created_at,
            "section2_template_path": self.section2_template_path,
            "anchors": self.anchors,
        }

    @staticmethod
    def from_dict(d: dict) -> "BatchState":
        return BatchState(
            batch_size=int(d["batch_size"]),
            paper_ids=list(d["paper_ids"]),
            next_index=int(d["next_index"]),
            next_batch_num=int(d["next_batch_num"]),
            batches=dict(d.get("batches", {})),
            created_at=str(d.get("created_at", datetime.utcnow().isoformat())),
            section2_template_path=str(d.get("section2_template_path", "NOT_SET")),
            anchors=list(d.get("anchors", DEFAULT_ANCHORS)),
        )

def load_state(path: str = STATE_PATH) -> Optional[BatchState]:
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return BatchState.from_dict(json.load(f))

def save_state(st: BatchState, path: str = STATE_PATH) -> None:
    ensure_analysis_dir()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(st.to_dict(), f, ensure_ascii=False, indent=2)

def collect_paper_ids_from_tree(root: str) -> Set[str]:
    ids: Set[str] = set()
    if not os.path.exists(root):
        return ids
    for dirpath, dirnames, filenames in os.walk(root):
        for name in dirnames + filenames:
            m = OISAC_RE.search(name)
            if m:
                ids.add(m.group(1))
    return ids

def numeric_key(paper_id: str) -> int:
    m = OISAC_RE.match(paper_id)
    return int(m.group(2)) if m else 10**9

def discover_all_paper_ids() -> List[str]:
    ids = set()
    ids |= collect_paper_ids_from_tree(os.path.join("data", "processed_markdowns"))
    ids |= collect_paper_ids_from_tree(os.path.join("data", "extraction_results_v4"))
    ids = {x for x in ids if OISAC_RE.match(x)}
    return sorted(ids, key=numeric_key)

def format_paper_ids_block(paper_ids: List[str], per_line: int = 6) -> str:
    lines = []
    for i in range(0, len(paper_ids), per_line):
        chunk = paper_ids[i:i+per_line]
        lines.append("  " + ", ".join(chunk))
    return "\n".join(lines)

def make_batch_id(batch_num: int) -> str:
    return f"B{batch_num:02d}"

def get_next_batch(st: BatchState) -> Tuple[str, List[str]]:
    batch_id = make_batch_id(st.next_batch_num)
    batch = st.paper_ids[st.next_index: st.next_index + st.batch_size]
    return batch_id, batch

def render_prompt(st: BatchState, batch_id: str, paper_ids: List[str]) -> str:
    return PROMPT_TEMPLATE_ANCHOR.format(
        batch_id=batch_id,
        n=len(paper_ids),
        paper_ids_block=format_paper_ids_block(paper_ids),
        anchor_map=format_anchor_map(st.anchors),
    )

# -------------------------
# CLI commands
# -------------------------

def cmd_init(args: argparse.Namespace) -> None:
    ensure_analysis_dir()
    paper_ids = discover_all_paper_ids()

    if args.start_from_paper:
        if args.start_from_paper not in paper_ids:
            raise SystemExit(f"start_from_paper not found: {args.start_from_paper}")
        start_idx = paper_ids.index(args.start_from_paper)
    else:
        start_idx = 0

    template_path, anchors = load_section2_anchors(args.template)

    st = BatchState(
        batch_size=args.batch_size,
        paper_ids=paper_ids,
        next_index=start_idx,
        next_batch_num=args.start_batch,
        batches={},
        created_at=datetime.utcnow().isoformat(),
        section2_template_path=template_path,
        anchors=anchors,
    )
    save_state(st)
    print(f"[OK] Initialized state at {STATE_PATH}")
    print(f"Total paper_ids discovered: {len(paper_ids)}")
    print(f"Section II template: {template_path}")
    print(f"Anchors loaded: {[a['anchor_id'] for a in anchors]}")
    print(f"Next batch: {make_batch_id(st.next_batch_num)} starting at index {st.next_index}")

def cmd_status(args: argparse.Namespace) -> None:
    st = load_state()
    if not st:
        raise SystemExit("No state found. Run: python codex_batch_prompter_v2_anchor.py init")
    remaining = max(0, len(st.paper_ids) - st.next_index)
    print(f"State: {STATE_PATH}")
    print(f"batch_size = {st.batch_size}")
    print(f"discovered paper_ids = {len(st.paper_ids)}")
    print(f"next_index = {st.next_index} (remaining {remaining})")
    print(f"next_batch_num = {st.next_batch_num} ({make_batch_id(st.next_batch_num)})")
    print(f"stored batches = {len(st.batches)}")
    print(f"Section II template: {st.section2_template_path}")
    print("Anchors:")
    for a in st.anchors:
        print(f"  {a['anchor_id']}: {a['title']}")

def cmd_peek(args: argparse.Namespace) -> None:
    st = load_state()
    if not st:
        raise SystemExit("No state found. Run: python codex_batch_prompter_v2_anchor.py init")
    batch_id, batch = get_next_batch(st)
    if not batch:
        print("[DONE] No more papers left.")
        return
    print(render_prompt(st, batch_id, batch))

def cmd_advance(args: argparse.Namespace) -> None:
    st = load_state()
    if not st:
        raise SystemExit("No state found. Run: python codex_batch_prompter_v2_anchor.py init")
    batch_id, batch = get_next_batch(st)
    if not batch:
        print("[DONE] No more papers left.")
        return

    # Print prompt first
    print(render_prompt(st, batch_id, batch))

    # Advance
    st.batches[batch_id] = batch
    st.next_index += len(batch)
    st.next_batch_num += 1
    save_state(st)

def cmd_rerun(args: argparse.Namespace) -> None:
    st = load_state()
    if not st:
        raise SystemExit("No state found. Run: python codex_batch_prompter_v2_anchor.py init")
    batch_id = args.batch_id.strip().upper()
    if batch_id not in st.batches:
        known = sorted(st.batches.keys())
        raise SystemExit(f"Batch not in state: {batch_id}. Known (sample): {known[:12]} ...")
    print(render_prompt(st, batch_id, st.batches[batch_id]))

def cmd_reload_anchors(args: argparse.Namespace) -> None:
    st = load_state()
    if not st:
        raise SystemExit("No state found. Run: python codex_batch_prompter_v2_anchor.py init")
    template_path, anchors = load_section2_anchors(args.template)
    st.section2_template_path = template_path
    st.anchors = anchors
    save_state(st)
    print(f"[OK] Reloaded anchors from: {template_path}")
    print(f"Anchors: {[a['anchor_id'] for a in anchors]}")

def build_argparser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Generate Codex batch prompts (with Section II anchor mapping).")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init", help="Discover O_ISAC paper_ids and initialize state.")
    p_init.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    p_init.add_argument("--start-batch", type=int, default=1, help="e.g., 6 to start at B06")
    p_init.add_argument("--start-from-paper", type=str, default=None, help="e.g., O_ISAC_061")
    p_init.add_argument("--template", type=str, default=None, help="Template filename/path hint (optional).")
    p_init.set_defaults(func=cmd_init)

    p_status = sub.add_parser("status", help="Show current state.")
    p_status.set_defaults(func=cmd_status)

    p_peek = sub.add_parser("peek", help="Print next batch prompt without advancing state.")
    p_peek.set_defaults(func=cmd_peek)

    p_adv = sub.add_parser("advance", help="Print next batch prompt and advance state.")
    p_adv.set_defaults(func=cmd_advance)

    p_rerun = sub.add_parser("rerun", help="Print a previously generated batch prompt (no state advance).")
    p_rerun.add_argument("batch_id", type=str, help="e.g., B03")
    p_rerun.set_defaults(func=cmd_rerun)

    p_ra = sub.add_parser("reload-anchors", help="Re-parse template anchors and update state.")
    p_ra.add_argument("--template", type=str, default=None)
    p_ra.set_defaults(func=cmd_reload_anchors)

    return p

def main() -> None:
    args = build_argparser().parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
