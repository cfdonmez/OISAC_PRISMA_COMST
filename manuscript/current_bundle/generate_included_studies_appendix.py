from __future__ import annotations

import csv
import re
import unicodedata
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
CURRENT_BUNDLE = Path(__file__).resolve().parent
INPUT_CSV = REPO_ROOT / "analysis" / "ph1_scr" / "included_studies_list.csv"
SCOPUS_CANDIDATES_CSV = REPO_ROOT / "scopus_candidates.csv"
OUTPUT_TEX = CURRENT_BUNDLE / "included_studies_appendix.tex"


LATEX_REPLACEMENTS = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def escape_tex(text: str) -> str:
    escaped = text
    for src, dst in LATEX_REPLACEMENTS.items():
        escaped = escaped.replace(src, dst)
    return escaped


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def ascii_clean(value: str) -> str:
    cleaned = (value or "").strip()
    replacements = {
        "–": "--",
        "—": "--",
        "−": "-",
        "µ": "mu",
        "μ": "mu",
        "×": "x",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "•": "-",
        "â€“": "--",
        "â€”": "--",
        "â€œ": '"',
        "â€": '"',
        "â€˜": "'",
        "â€™": "'",
        "Ã—": "x",
        "Î¼": "mu",
    }
    for src, dst in replacements.items():
        cleaned = cleaned.replace(src, dst)
    cleaned = unicodedata.normalize("NFKD", cleaned).encode("ascii", "ignore").decode("ascii")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def first_non_empty(*values: str) -> str:
    for value in values:
        cleaned = ascii_clean(value)
        if cleaned:
            return cleaned
    return ""


def extract_surname(author: str) -> str:
    tokens = [token.strip("., ") for token in author.split() if token.strip("., ")]
    return tokens[-1] if tokens else author.strip()


def short_citation(authors: str, year: str) -> str:
    author_list = [item.strip() for item in authors.split(";") if item.strip()]
    clean_year = year.split(".")[0].strip() if year else "n.d."
    if not author_list:
        return f"Unknown ({clean_year})"
    if len(author_list) == 1:
        return f"{extract_surname(author_list[0])} ({clean_year})"
    if len(author_list) == 2:
        return f"{extract_surname(author_list[0])} and {extract_surname(author_list[1])} ({clean_year})"
    return f"{extract_surname(author_list[0])} et al. ({clean_year})"


def normalize_category(value: str) -> str:
    cleaned = ascii_clean(value).upper()
    if cleaned == "FIBER":
        return "Fiber"
    if cleaned == "WIRELESS":
        return "Wireless"
    return ascii_clean(value).title() if ascii_clean(value) else "--"


def track_sort_key(track_id: str) -> tuple[int, str]:
    match = re.search(r"(\d+)$", track_id)
    return (int(match.group(1)) if match else 10**9, track_id)


def normalize_row(row: dict[str, str], fallback: dict[str, str] | None) -> dict[str, str]:
    fallback = fallback or {}
    return {
        "Track_ID": first_non_empty(row.get("Track_ID", ""), fallback.get("Track_ID", "")),
        "Authors": first_non_empty(row.get("Authors", ""), fallback.get("Authors", "")),
        "Publication Year": first_non_empty(
            row.get("Publication Year", ""),
            row.get("Year", ""),
            fallback.get("Publication Year", ""),
            fallback.get("Year", ""),
        ),
        "CATEGORY": first_non_empty(row.get("CATEGORY", ""), fallback.get("CATEGORY", "")),
        "Document Title": first_non_empty(
            row.get("Document Title", ""),
            row.get("Title", ""),
            fallback.get("Document Title", ""),
            fallback.get("Title", ""),
        ),
        "DOI": first_non_empty(row.get("DOI", ""), fallback.get("DOI", "")),
    }


def build_rows() -> list[dict[str, str]]:
    primary_rows = load_csv_rows(INPUT_CSV)
    fallback_rows = load_csv_rows(SCOPUS_CANDIDATES_CSV)
    fallback_by_id = {row["Track_ID"]: row for row in fallback_rows if row.get("Track_ID")}
    rows = [normalize_row(row, fallback_by_id.get(row.get("Track_ID", ""))) for row in primary_rows]
    rows.sort(key=lambda row: track_sort_key(row["Track_ID"]))
    if len(rows) != 220:
        raise ValueError(f"Expected 220 included studies, found {len(rows)}.")
    return rows


def render_row(row: dict[str, str]) -> str:
    study_id = r"\texttt{" + escape_tex(row["Track_ID"]) + "}"
    citation = escape_tex(short_citation(row.get("Authors", ""), row.get("Publication Year", "")))
    category = escape_tex(normalize_category(row.get("CATEGORY", "")))
    title = escape_tex(row.get("Document Title", "") or "--")
    doi = row.get("DOI", "")
    doi_tex = r"\nolinkurl{" + escape_tex(doi) + "}" if doi else "--"
    return f"{study_id} & {citation} & {category} & {title} & {doi_tex} \\\\"


def render_tex(rows: list[dict[str, str]]) -> str:
    body = "\n".join(render_row(row) for row in rows)
    return rf"""\section{{Included Studies Ledger}}
\label{{app:included_studies}}

This appendix provides a study-oriented ledger for the 220 primary studies included in the review. To avoid duplicating the full bibliography in two places, the ledger records each study by its review study ID, a short citation, the screening category used in the corpus, the study title, and the DOI when available. Full narrative references remain in the main bibliography wherever a record is cited in the manuscript text.

{{\setlength{{\tabcolsep}}{{2pt}}
\renewcommand{{\arraystretch}}{{1.05}}
\begin{{longtable}}{{L{{1.45cm}}L{{2.45cm}}C{{1.25cm}}L{{5.55cm}}L{{4.15cm}}}}
\caption{{Study-oriented ledger for the 220 included primary studies.}}\label{{tab:included_studies_ledger}}\\
\toprule
Study ID & Short citation & Category & Study title & DOI \\
\midrule
\endfirsthead
\multicolumn{{5}}{{l}}{{\textit{{Table \thetable\ continued from previous page.}}}}\\
\toprule
Study ID & Short citation & Category & Study title & DOI \\
\midrule
\endhead
\bottomrule
\endfoot
{body}
\end{{longtable}}
}}
"""


def main() -> None:
    rows = build_rows()
    OUTPUT_TEX.write_text(render_tex(rows), encoding="utf-8")
    print(f"Wrote {OUTPUT_TEX} with {len(rows)} included-study rows.")


if __name__ == "__main__":
    main()
