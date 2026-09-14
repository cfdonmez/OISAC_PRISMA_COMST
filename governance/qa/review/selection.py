"""Build the compact selection figure from one editable vector geometry.

Run with the bundled Python runtime. All coordinates use top-left PDF points.
The root task recorded the artifact-operation marker before this authoring run.
"""
from pathlib import Path
from html import escape
import json
import hashlib
import subprocess
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[3]
QA = Path(__file__).resolve().parent
OUT = ROOT / "manuscript" / "figures"
W, H = 516, 264
BLUE, GREEN, GOLD = "#0079B5", "#009F78", "#DA9A00"
INK, GRAY = "#172530", "#64717B"
pdfmetrics.registerFont(TTFont("Arial", "C:/Windows/Fonts/arial.ttf"))
pdfmetrics.registerFont(TTFont("ArialBold", "C:/Windows/Fonts/arialbd.ttf"))
pdf = canvas.Canvas(str(OUT / "selection.pdf"), pagesize=(W, H), invariant=1)
pdf.setTitle("Study selection")
pdf.setAuthor("O-ISAC review")
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}pt" height="{H}pt" viewBox="0 0 {W} {H}">',
       '<title>Study selection</title>',
       '<desc>1,733 identified records lead to 1,259 screened records, 332 forwarded records, 330 unique reports sought, 272 full texts assessed, and 227 eligible reports corresponding to 206 studies. The 21 companion reports remain included. The contextual corpus contains 67 records and reports, separately from included studies.</desc>']
texts, boxes, arrows = [], [], []

def box(name, x, y, w, h, stroke, fill):
    boxes.append(dict(name=name, x=x, y=y, width=w, height=h))
    pdf.setStrokeColor(HexColor(stroke))
    pdf.setFillColor(HexColor(fill))
    pdf.setLineWidth(1.05)
    pdf.roundRect(x, H-y-h, w, h, 5, fill=1, stroke=1)
    svg.append(f'<rect id="{name}" x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" stroke="{stroke}" stroke-width="1.05"/>')

def text(label, x, y, size=10, bold=False, color=INK, anchor="middle", parent=None):
    font = "ArialBold" if bold else "Arial"
    width = pdfmetrics.stringWidth(label, font, size)
    left = x-width/2 if anchor == "middle" else x
    entry = dict(text=label, x=left, baseline=y, width=width, size=size, box=parent)
    texts.append(entry)
    if parent:
        b = next(b for b in boxes if b["name"] == parent)
        assert left >= b["x"] + 6, entry
        assert left + width <= b["x"] + b["width"] - 6, entry
        assert y-size >= b["y"] + 1, entry
        assert y+size*0.22 <= b["y"] + b["height"] - 1, entry
    pdf.setFont(font, size)
    pdf.setFillColor(HexColor(color))
    pdf.drawString(left, H-y, label)
    weight = "700" if bold else "400"
    svg.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(label)}</text>')

def arrow(x1, y1, x2, y2, kind, label=None):
    assert x1 == x2 or y1 == y2
    arrows.append(dict(start=[x1,y1], end=[x2,y2], kind=kind, label=label))
    pdf.setStrokeColor(HexColor(GRAY))
    pdf.setFillColor(HexColor(GRAY))
    pdf.setLineWidth(0.9)
    pdf.line(x1, H-y1, x2, H-y2)
    if y1 == y2:
        pts = [(x2, y2), (x2-4, y2-2.1), (x2-4, y2+2.1)]
    else:
        pts = [(x2, y2), (x2-2.1, y2-4), (x2+2.1, y2-4)]
    p = pdf.beginPath()
    p.moveTo(pts[0][0], H-pts[0][1])
    for x, y in pts[1:]: p.lineTo(x, H-y)
    p.close()
    pdf.drawPath(p, fill=1, stroke=0)
    svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{GRAY}" stroke-width="0.9"/>')
    svg.append('<polygon points="' + ' '.join(f'{x},{y}' for x,y in pts) + f'" fill="{GRAY}"/>')

# Five compact main boxes; the unit changes are stated in their labels.
LX, LW, CX = 8, 225, 120.5
RX, RW, RC = 281, 227, 394.5
box("identified", LX, 4, LW, 29, BLUE, "#EAF4F9")
text("Records identified", CX, 16, 10.1, True, parent="identified")
text("1,733", CX, 28, 11, parent="identified")
box("screened", LX, 51, LW, 29, BLUE, "#EAF4F9")
text("Records screened", CX, 63, 10.1, True, parent="screened")
text("1,259", CX, 75, 11, parent="screened")
box("retrieval", LX, 98, LW, 47, GREEN, "#EAF6F1")
text("Source records forwarded: 332", CX, 111, 10, True, BLUE, parent="retrieval")
text("2 bibliographic aliases reconciled", CX, 125, 8.8, False, GRAY, parent="retrieval")
text("Unique reports sought: 330", CX, 139, 10.3, True, GREEN, parent="retrieval")
box("fulltext", LX, 164, LW, 29, GREEN, "#EAF6F1")
text("Full-text reports assessed", CX, 176, 10.1, True, parent="fulltext")
text("272", CX, 188, 11, parent="fulltext")
box("included", LX, 214, LW, 44, GOLD, "#FCF4DF")
text("Included evidence", CX, 227, 10.1, True, parent="included")
text("227 eligible reports / 206 studies", CX, 240, 10.2, True, parent="included")
text("Includes 21 companion reports", CX, 252, 8.8, parent="included")

# Every removal/outcome arrow branches from the relevant stage transition.
box("prescreen", RX, 13, RW, 47, "#87929A", "#F7F9FA")
text("Removed before screening", RC, 26, 9.5, True, parent="prescreen")
text("Duplicate records: 472", RC, 40, 9.3, parent="prescreen")
text("Metadata dispositions: 2", RC, 53, 9.3, parent="prescreen")
box("screen_outcomes", RX, 71, RW, 56, "#87929A", "#F7F9FA")
text("Title/abstract exclusions: 864", RC, 85, 9.5, parent="screen_outcomes")
text("Contextual records: 61", RC, 102, 9.5, parent="screen_outcomes")
text("Related-report flags: 2", RC, 119, 9.5, parent="screen_outcomes")
box("notretrieved", RX, 140, RW, 29, "#87929A", "#F7F9FA")
text("Reports not retrieved: 58", RC, 158, 9.5, parent="notretrieved")
box("fulltext_outcomes", RX, 182, RW, 41, "#87929A", "#F7F9FA")
text("Full-text exclusions: 39", RC, 197, 9.5, parent="fulltext_outcomes")
text("Contextual reports: 6", RC, 213, 9.5, parent="fulltext_outcomes")
box("context", RX, 235, RW, 23, GOLD, "#FCF4DF")
text("Contextual corpus: 67 (61 + 6)", RC, 250, 9.5, True, parent="context")

for top, bottom, mid, label in [(33,51,42,"prescreen"), (80,98,89,"screen_outcomes"),
                                (145,164,154.5,"notretrieved"), (193,214,203.5,"fulltext_outcomes")]:
    arrow(CX, top, CX, bottom, "main")
    arrow(CX, mid, RX, mid, "disposition", label)

svg.append('</svg>')
(OUT / "selection.svg").write_text('\n'.join(svg)+'\n', encoding="utf-8")
pdf.showPage()
pdf.save()

checks = {
    "identification": 1733-472-2 == 1259,
    "screening": 1259-864-61-2 == 332,
    "aliases": 332-2 == 330,
    "retrieval": 330-58 == 272,
    "eligibility": 272-39-6 == 227,
    "included_report_study_mapping": 206+21 == 227,
    "context": 61+6 == 67,
}
assert all(checks.values())
reader = PdfReader(OUT / "selection.pdf")
assert len(reader.pages) == 1
page = reader.pages[0]
extracted = page.extract_text()
for label in [t["text"] for t in texts]:
    assert label in extracted, label
assert len(page.images) == 0, "PDF must contain only vector content and text"
for b in boxes:
    assert b["x"] >= 0 and b["y"] >= 0
    assert b["x"]+b["width"] <= W and b["y"]+b["height"] <= H
assert min(t["size"] for t in texts) >= 8.8
poppler = Path("C:/Users/fatih/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe")
subprocess.run([str(poppler), "-r", "170", "-singlefile", "-png", str(OUT/"selection.pdf"), str(QA/"selection")], check=True)
report = dict(size_pt=[W,H], size_inches=[W/72,H/72], minimum_font_pt=8.8,
              arithmetic=checks, pages=1, raster_images=0, all_text_extracted=True,
              geometry="All boxes within canvas; all labels within their parent boxes with >=6 pt horizontal padding.",
              semantics="Metadata dispositions and report flags are administrative branches; 21 companion reports remain included; context corpus is separate.",
              boxes=boxes, texts=texts, arrows=arrows,
              hashes={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in [OUT/"selection.pdf",OUT/"selection.svg"]})
(QA/"selection.json").write_text(json.dumps(report, indent=2)+'\n', encoding="utf-8")
print(json.dumps({k:v for k,v in report.items() if k not in ("boxes","texts","arrows")}, indent=2))
