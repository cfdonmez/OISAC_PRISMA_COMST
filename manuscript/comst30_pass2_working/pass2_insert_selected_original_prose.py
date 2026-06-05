from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TEX = ROOT / "bare_jrnl_new_sample4.tex"
ORIG = ROOT.parent.parent / "manuscript_submission" / "bare_jrnl_new_sample4.tex"


def clean_chunk(lines: list[str]) -> str:
    s = "\n".join(lines)
    for env in ["table*", "table", "figure*", "figure", "equation", "algorithm"]:
        s = re.sub(r"\\begin\{" + re.escape(env) + r"\}.*?\\end\{" + re.escape(env) + r"\}", "", s, flags=re.S)
    s = re.sub(r"^\\(sub)*section\*?\{[^}]*\}\s*$", "", s, flags=re.M)
    s = re.sub(r"\\cite\{[^}]*\}", "", s)
    s = re.sub(r"(Fig\.|Figure|Table)~?\\ref\{[^}]*\}", "the corresponding synthesis element", s)
    s = re.sub(r"Sections?~?\\ref\{[^}]*\}", "the corresponding section", s)
    s = s.replace("Evidence alignment:", "Representative evidence shows that")
    s = s.replace("Design rationale:", "Rationale:")
    s = s.replace("Metric Governance", "metric governance")
    s = re.sub(r"\n{3,}", "\n\n", s).strip()
    return s


def chunk(start: int, end: int) -> str:
    lines = ORIG.read_text(encoding="utf-8").splitlines()
    return clean_chunk(lines[start - 1 : end])


def insert_before(text: str, marker: str, addition: str) -> str:
    if addition in text:
        return text
    idx = text.find(marker)
    if idx < 0:
        raise RuntimeError(f"Missing marker: {marker}")
    return text[:idx] + addition + "\n\n" + text[idx:]


def main() -> None:
    text = TEX.read_text(encoding="utf-8")
    additions = [
        (
            r"\section{Background and Metric-Governance Contract}",
            "\\subsection{Optical Advantage and Fragmentation Detail}\n\n" + chunk(222, 265),
        ),
        (
            r"\section{Review Methodology}",
            "\\subsection{Additional Metric-Governance Detail}\n\n" + chunk(360, 533) + "\n\n" + chunk(586, 627),
        ),
        (
            r"\section{Unified O-ISAC Taxonomy}",
            "\\subsection{Additional Methodological Detail}\n\n" + chunk(743, 865),
        ),
        (
            r"\section{Communication-Sensing Tradeoff Synthesis}",
            "\\subsection{Additional Axis-Level Taxonomy Detail}\n\n" + chunk(872, 1050) + "\n\n" + chunk(1114, 1195),
        ),
        (
            r"\section{Enabling Technologies and System-Level Co-Design}",
            "\\subsection{Additional Tradeoff Interpretation}\n\n" + chunk(1314, 1509),
        ),
        (
            r"\section{Applications and Use Cases Across Domains}",
            "\\subsection{Additional Enabler Detail}\n\n" + chunk(1578, 1807),
        ),
        (
            r"\section{Open Challenges and Research Roadmap}",
            "\\subsection{Additional Application Detail}\n\n" + chunk(1923, 2058),
        ),
        (
            r"\section{Conclusions}",
            "\\subsection{Additional Roadmap Detail}\n\n" + chunk(2136, 2322),
        ),
    ]
    for marker, addition in additions:
        text = insert_before(text, marker, addition)
    TEX.write_text(text, encoding="utf-8")
    print("Inserted selected original prose expansions.")


if __name__ == "__main__":
    main()
