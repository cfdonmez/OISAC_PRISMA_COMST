import fs from "node:fs/promises";
import path from "node:path";
import { Workbook, SpreadsheetFile } from "@oai/artifact-tool";

const toolDir = path.dirname(new URL(import.meta.url).pathname.replace(/^\/(.:)/, "$1"));
const manuscriptDir = path.resolve(toolDir, "..");
const sourceDir = path.join(manuscriptDir, "supplements", "evidence");
const outputXlsx = path.join(sourceDir, "OISAC_JOURNAL_EVIDENCE_SUPPLEMENTS_2026-08-13.xlsx");
const previewPng = path.join(sourceDir, "OISAC_JOURNAL_EVIDENCE_SUPPLEMENTS_README_preview.png");

const specs = [
  ["FT Exclusions", "ST-16B_EXCLUDED_REPORTS_39.csv", 39, "PRISMA Item 16b"],
  ["Primary Evidence", "ST-19_PRIMARY_EVIDENCE_RESULTS_3020.csv", 3020, "Primary qualitative evidence"],
  ["Primary Metrics", "ST-19_PRIMARY_METRIC_RESULTS_4779.csv", 4779, "Primary metric results"],
  ["Governed Tradeoffs", "ST-19_GOVERNED_TRADEOFFS_404.csv", 404, "Governed audit view"],
  ["Substantive Tradeoffs", "ST-19_SUBSTANTIVE_TRADEOFFS_402.csv", 402, "Substantive scientific view"],
  ["Study TQAF", "ST-18_STUDY_LEVEL_TQAF_206.csv", 206, "Review-specific study appraisal"],
  ["Evidence Bodies", "ST-22_EVIDENCE_BODY_CERTAINTY_115.csv", 115, "Evidence-body certainty"],
  ["Body Membership", "ST-22_EVIDENCE_BODY_MEMBERSHIP_4931.csv", 4931, "Study-to-body membership"],
];

function parseCsv(source) {
  const rows = [];
  let row = [];
  let field = "";
  let quoted = false;
  for (let index = 0; index < source.length; index += 1) {
    const char = source[index];
    if (quoted) {
      if (char === '"' && source[index + 1] === '"') { field += '"'; index += 1; }
      else if (char === '"') quoted = false;
      else field += char;
    } else if (char === '"') quoted = true;
    else if (char === ",") { row.push(field); field = ""; }
    else if (char === "\n") { row.push(field.replace(/\r$/, "")); rows.push(row); row = []; field = ""; }
    else field += char;
  }
  if (field || row.length) { row.push(field.replace(/\r$/, "")); rows.push(row); }
  return rows.filter((values) => values.some((value) => value !== ""));
}

function excelColumn(index) {
  let value = index + 1;
  let result = "";
  while (value > 0) {
    const remainder = (value - 1) % 26;
    result = String.fromCharCode(65 + remainder) + result;
    value = Math.floor((value - 1) / 26);
  }
  return result;
}

const workbook = Workbook.create();
const readme = workbook.worksheets.add("README");
readme.showGridLines = false;
readme.getRange("A1:E1").merge();
readme.getRange("A1").values = [["O-ISAC Journal Evidence Supplements"]];
readme.getRange("A1:E1").format = {
  fill: "#17365D",
  font: { name: "Aptos Display", bold: true, color: "#FFFFFF", size: 16 },
  rowHeight: 30,
};
readme.getRange("A3:E3").values = [["Carrier", "Purpose", "Expected rows", "Actual rows", "Gate"]];
readme.getRange("A3:E3").format = {
  fill: "#4472C4",
  font: { bold: true, color: "#FFFFFF" },
  wrapText: true,
};

const loaded = [];
for (const [sheetName, filename, expected, purpose] of specs) {
  const csvPath = path.join(sourceDir, filename);
  const rows = parseCsv(await fs.readFile(csvPath, "utf8"));
  if (rows.length - 1 !== expected) throw new Error(`${filename}: expected ${expected}, got ${rows.length - 1}`);
  loaded.push({ sheetName, filename, expected, purpose, rows });
}

for (let index = 0; index < loaded.length; index += 1) {
  const { sheetName, expected, purpose } = loaded[index];
  const row = index + 4;
  readme.getRange(`A${row}:C${row}`).values = [[sheetName, purpose, expected]];
  readme.getRange(`D${row}`).formulas = [[`=COUNTA('${sheetName}'!A:A)-1`]];
  readme.getRange(`E${row}`).formulas = [[`=IF(C${row}=D${row},"PASS","FAIL")`]];
}
readme.getRange("A13:E16").merge();
readme.getRange("A13").values = [[
  "Interpretation boundary: metric rows are condition-bound extractions, not independent effects. The governed tradeoff view contains two explicit absence sentinels; the substantive view excludes them. TQAF is a deterministic review-specific appraisal, not conventional risk of bias or GRADE. This workbook is a manuscript supplement and not a public repository release."
]];
readme.getRange("A13:E16").format = { fill: "#F2F2F2", wrapText: true, verticalAlignment: "center" };
readme.getRange("A1:E16").format.font = { name: "Aptos", size: 10 };
readme.getRange("A1:A16").format.columnWidth = 28;
readme.getRange("B1:B16").format.columnWidth = 38;
readme.getRange("C1:E16").format.columnWidth = 16;
readme.getRange("C4:D11").format.numberFormat = "0";
readme.getRange("A3:E11").format.borders = { preset: "inside", style: "thin", color: "#D9E2F3" };
readme.freezePanes.freezeRows(3);

for (let index = 0; index < loaded.length; index += 1) {
  const { sheetName, rows } = loaded[index];
  const sheet = workbook.worksheets.add(sheetName);
  sheet.showGridLines = false;
  const columnCount = rows[0].length;
  const rowCount = rows.length;
  sheet.getRangeByIndexes(0, 0, rowCount, columnCount).values = rows;
  sheet.getRangeByIndexes(0, 0, 1, columnCount).format = {
    fill: "#17365D",
    font: { name: "Aptos", bold: true, color: "#FFFFFF", size: 9 },
    wrapText: true,
    verticalAlignment: "center",
    rowHeight: 36,
  };
  sheet.getRangeByIndexes(1, 0, rowCount - 1, columnCount).format = {
    font: { name: "Aptos", size: 8 },
    verticalAlignment: "top",
    wrapText: true,
  };
  sheet.getRangeByIndexes(0, 0, rowCount, columnCount).format.borders = {
    insideHorizontal: { style: "thin", color: "#E7E6E6" },
    bottom: { style: "thin", color: "#BFBFBF" },
  };
  for (let column = 0; column < columnCount; column += 1) {
    const header = rows[0][column];
    let width = Math.max(12, Math.min(28, header.length + 4));
    if (/title|note|summary|condition|scenario|rationale|citation|authors/i.test(header)) width = 34;
    if (/id$|_id|code|status|year|count/i.test(header)) width = Math.min(width, 18);
    sheet.getRangeByIndexes(0, column, rowCount, 1).format.columnWidth = width;
  }
  sheet.getRangeByIndexes(1, 0, rowCount - 1, columnCount).format.rowHeight = 36;
  sheet.freezePanes.freezeRows(1);
  sheet.freezePanes.freezeColumns(Math.min(3, columnCount));
  const endColumn = excelColumn(columnCount - 1);
  sheet.tables.add(`A1:${endColumn}${rowCount}`, true, `EvidenceTable${index + 1}`);
}

const readmeInspection = await workbook.inspect({
  kind: "table",
  range: "README!A1:E16",
  include: "values,formulas",
  tableMaxRows: 20,
  tableMaxCols: 6,
});
const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 200 },
  summary: "Journal evidence workbook formula-error scan",
});
const preview = await workbook.render({ sheetName: "README", range: "A1:E16", scale: 2, format: "png" });
await fs.writeFile(previewPng, new Uint8Array(await preview.arrayBuffer()));
const xlsx = await SpreadsheetFile.exportXlsx(workbook);
await xlsx.save(outputXlsx);

process.stdout.write(`${JSON.stringify({
  status: "PASS",
  output: outputXlsx,
  preview: previewPng,
  worksheets: 9,
  sourceCsvs: loaded.map(({ filename, expected }) => ({ filename, rows: expected })),
  readmeInspection: readmeInspection.ndjson,
  formulaErrors: errors.ndjson,
}, null, 2)}\n`);
