from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
import re


TEXT_EXTENSIONS = {
    ".bib",
    ".csv",
    ".json",
    ".md",
    ".ris",
    ".tex",
    ".text",
    ".tsv",
    ".txt",
    ".xml",
    ".yml",
    ".yaml",
}

MAX_TEXT_BYTES = 5_000_000
MAX_PDF_BYTES = 25_000_000
PDF_PAGE_LIMIT = 2
COMMON_TITLE_TOKENS = {
    "and",
    "band",
    "communication",
    "communications",
    "enhanced",
    "frequency",
    "for",
    "improved",
    "integrated",
    "interconnections",
    "millimeter",
    "optical",
    "over",
    "phase",
    "photonic",
    "sensing",
    "spectral",
    "system",
    "systems",
    "the",
    "using",
    "wave",
}


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def load_excluded_targets(repo_root: Path) -> list[dict[str, str]]:
    excluded_path = repo_root / "screening" / "excluded_fulltext_log.csv"
    assessed_path = repo_root / "screening" / "fulltext_assessed_reconstruction.csv"

    doi_by_track: dict[str, str] = {}
    with assessed_path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            track_id = (row.get("track_id") or "").strip()
            doi = (row.get("doi") or "").strip()
            if track_id:
                doi_by_track[track_id] = doi

    targets: list[dict[str, str]] = []
    with excluded_path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            track_id = (row.get("Track_ID") or "").strip()
            title = (row.get("Document Title") or "").strip()
            doi = doi_by_track.get(track_id, "").strip()
            title_tokens = [tok for tok in re.findall(r"[A-Za-z0-9]+", title) if len(tok) >= 4]
            author_text = (row.get("Authors") or "").strip()
            author_tokens = [tok for tok in re.findall(r"[A-Za-z][A-Za-z\\-]+", author_text) if len(tok) >= 3]
            distinctive_tokens = []
            for token in title_tokens:
                low = token.lower()
                if low in COMMON_TITLE_TOKENS:
                    continue
                if low not in distinctive_tokens:
                    distinctive_tokens.append(low)
            targets.append(
                {
                    "track_id": track_id,
                    "title": title,
                    "doi": doi,
                    "exclusion_code": (row.get("Exclusion_Code") or "").strip(),
                    "title_probe": " ".join(title_tokens[:8]),
                    "title_norm": normalize(title),
                    "doi_norm": normalize(doi),
                    "author_probe": " ".join(author_tokens[:3]),
                    "distinctive_tokens": "|".join(distinctive_tokens[:10]),
                }
            )
    return targets


def sniff_text(path: Path) -> str:
    data = path.read_bytes()
    for encoding in ("utf-8", "utf-8-sig", "cp1254", "latin-1"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="ignore")


def search_text_file(path: Path, target: dict[str, str]) -> list[str]:
    reasons: list[str] = []
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return reasons
    if path.stat().st_size > MAX_TEXT_BYTES:
        return reasons

    try:
        text = sniff_text(path)
    except OSError:
        return reasons

    text_lower = text.lower()
    if target["track_id"] and target["track_id"].lower() in text_lower:
        reasons.append("content_track_id")
    if target["doi"] and target["doi"].lower() in text_lower:
        reasons.append("content_doi")
    if target["title"] and target["title"].lower() in text_lower:
        reasons.append("content_exact_title")
    if target["title_probe"] and target["title_probe"].lower() in text_lower:
        reasons.append("content_title_probe")
    if target["author_probe"] and target["author_probe"].lower() in text_lower:
        reasons.append("content_author_probe")
    token_hits = [
        token for token in target["distinctive_tokens"].split("|") if token and token in text_lower
    ]
    if len(token_hits) >= 4:
        reasons.append(f"content_token_overlap_{len(token_hits)}")
    return reasons


def search_pdf(path: Path, target: dict[str, str]) -> list[str]:
    reasons: list[str] = []
    if path.suffix.lower() != ".pdf":
        return reasons
    if path.stat().st_size > MAX_PDF_BYTES:
        return reasons

    try:
        from pypdf import PdfReader  # type: ignore
    except Exception:
        return reasons

    try:
        reader = PdfReader(str(path))
    except Exception:
        return reasons

    metadata_text = " ".join(
        str(value) for value in (reader.metadata or {}).values() if value is not None
    ).lower()
    if target["doi"] and target["doi"].lower() in metadata_text:
        reasons.append("pdf_metadata_doi")
    if target["title"] and target["title"].lower() in metadata_text:
        reasons.append("pdf_metadata_title")
    if target["author_probe"] and target["author_probe"].lower() in metadata_text:
        reasons.append("pdf_metadata_author_probe")
    if not reasons:
        collected_pages: list[str] = []
        for page in reader.pages[:PDF_PAGE_LIMIT]:
            try:
                collected_pages.append(page.extract_text() or "")
            except Exception:
                continue
        pdf_text = "\n".join(collected_pages).lower()
        if target["doi"] and target["doi"].lower() in pdf_text:
            reasons.append("pdf_text_doi")
        if target["title"] and target["title"].lower() in pdf_text:
            reasons.append("pdf_text_exact_title")
        if target["title_probe"] and target["title_probe"].lower() in pdf_text:
            reasons.append("pdf_text_title_probe")
        if target["author_probe"] and target["author_probe"].lower() in pdf_text:
            reasons.append("pdf_text_author_probe")
        token_hits = [
            token for token in target["distinctive_tokens"].split("|") if token and token in pdf_text
        ]
        if len(token_hits) >= 4:
            reasons.append(f"pdf_text_token_overlap_{len(token_hits)}")
    return reasons


def search_path_name(path: Path, target: dict[str, str]) -> list[str]:
    reasons: list[str] = []
    path_norm = normalize(str(path))
    name_norm = normalize(path.name)
    raw_path_lower = str(path).lower()

    if target["track_id"] and normalize(target["track_id"]) in path_norm:
        reasons.append("path_track_id")
    if target["doi_norm"] and target["doi_norm"] in path_norm:
        reasons.append("path_doi")
    if target["title_norm"] and target["title_norm"] in path_norm:
        reasons.append("path_exact_title")

    title_probe_norm = normalize(target["title_probe"])
    if title_probe_norm and title_probe_norm in name_norm:
        reasons.append("path_title_probe")
    if target["author_probe"] and target["author_probe"].lower() in raw_path_lower:
        reasons.append("path_author_probe")
    token_hits = [
        token for token in target["distinctive_tokens"].split("|") if token and token in raw_path_lower
    ]
    if len(token_hits) >= 3:
        reasons.append(f"path_token_overlap_{len(token_hits)}")
    return reasons


def search_root(root: Path, targets: list[dict[str, str]]) -> tuple[list[dict[str, str]], Counter]:
    results: list[dict[str, str]] = []
    stats: Counter = Counter()

    for path in root.rglob("*"):
        stats["paths_scanned"] += 1
        if not path.is_file():
            continue
        stats["files_scanned"] += 1

        suffix = path.suffix.lower()
        for target in targets:
            reasons = []
            reasons.extend(search_path_name(path, target))
            if suffix in TEXT_EXTENSIONS:
                stats["text_candidates"] += 1
                reasons.extend(search_text_file(path, target))
            elif suffix == ".pdf":
                stats["pdf_candidates"] += 1
                reasons.extend(search_pdf(path, target))

            if reasons:
                unique_reasons = sorted(set(reasons))
                results.append(
                    {
                        "track_id": target["track_id"],
                        "doi": target["doi"],
                        "title": target["title"],
                        "exclusion_code": target["exclusion_code"],
                        "matched_path": str(path),
                        "matched_suffix": suffix,
                        "match_reasons": ";".join(unique_reasons),
                    }
                )
                stats["matches"] += 1
    return results, stats


def write_outputs(repo_root: Path, root: Path, results: list[dict[str, str]], stats: Counter) -> tuple[Path, Path]:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path = repo_root / "screening" / f"excluded_studies_folder_query_{stamp}.csv"
    md_path = repo_root / "screening" / f"excluded_studies_folder_query_{stamp}.md"

    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        fieldnames = [
            "track_id",
            "doi",
            "title",
            "exclusion_code",
            "matched_path",
            "matched_suffix",
            "match_reasons",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    grouped: dict[str, list[dict[str, str]]] = {}
    for row in results:
        grouped.setdefault(row["track_id"], []).append(row)

    lines = [
        "# Excluded Studies Folder Query",
        "",
        f"- Search root: `{root}`",
        f"- Paths scanned: `{stats['paths_scanned']}`",
        f"- Files scanned: `{stats['files_scanned']}`",
        f"- Text candidates inspected: `{stats['text_candidates']}`",
        f"- PDF candidates inspected: `{stats['pdf_candidates']}`",
        f"- Match rows: `{stats['matches']}`",
        "",
    ]

    if not results:
        lines.extend(
            [
                "## Result",
                "",
                "No matches were found for the excluded-study targets in the scanned folder tree.",
            ]
        )
    else:
        lines.extend(["## Result", ""])
        for track_id, rows in sorted(grouped.items()):
            exemplar = rows[0]
            lines.append(f"### {track_id}")
            lines.append("")
            lines.append(f"- DOI: `{exemplar['doi'] or 'missing'}`")
            lines.append(f"- Title: {exemplar['title']}")
            lines.append(f"- Matches: `{len(rows)}`")
            lines.append("")
            for row in rows[:20]:
                lines.append(f"- `{row['match_reasons']}` -> `{row['matched_path']}`")
            if len(rows) > 20:
                lines.append(f"- ... `{len(rows) - 20}` additional match rows omitted from markdown summary")
            lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    return csv_path, md_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Search a folder tree for excluded-study traces.")
    parser.add_argument("--root", required=True, help="Folder to scan")
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Repository root containing screening files",
    )
    args = parser.parse_args()

    root = Path(args.root)
    repo_root = Path(args.repo_root)

    if not root.exists():
        print(f"Search root does not exist: {root}", file=sys.stderr)
        return 1

    targets = load_excluded_targets(repo_root)
    print(f"Loaded {len(targets)} excluded-study targets from screening logs.")
    print(f"Scanning folder tree: {root}")

    results, stats = search_root(root, targets)
    csv_path, md_path = write_outputs(repo_root, root, results, stats)

    print(f"Paths scanned: {stats['paths_scanned']}")
    print(f"Files scanned: {stats['files_scanned']}")
    print(f"Text candidates inspected: {stats['text_candidates']}")
    print(f"PDF candidates inspected: {stats['pdf_candidates']}")
    print(f"Match rows: {stats['matches']}")
    print(f"CSV report: {csv_path}")
    print(f"Markdown report: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
