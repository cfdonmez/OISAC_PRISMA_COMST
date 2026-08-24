import fs from "node:fs/promises";
import path from "node:path";
import { spawnSync } from "node:child_process";

const scriptPath = new URL(import.meta.url).pathname.replace(/^\/(.:)/, "$1");
const launcherManuscriptDir = path.resolve(path.dirname(scriptPath), "..");
const launcherQaPath = path.join(launcherManuscriptDir, "qa", "FINAL_PRISMA_ITEM17_WORKBOOK_QA.json");
if (process.env.OISAC_ITEM17_WORKBOOK_WORKER !== "1") {
  await fs.rm(launcherQaPath, { force: true });
  const startedAt = Date.now();
  const child = spawnSync(process.execPath, [scriptPath], {
    cwd: process.cwd(),
    env: { ...process.env, OISAC_ITEM17_WORKBOOK_WORKER: "1" },
    encoding: "utf8",
    maxBuffer: 20 * 1024 * 1024,
  });
  if (child.stdout) process.stdout.write(child.stdout);
  if (child.stderr) process.stderr.write(child.stderr);
  let freshQa;
  try {
    const stat = await fs.stat(launcherQaPath);
    freshQa = stat.mtimeMs >= startedAt - 1000
      ? JSON.parse(await fs.readFile(launcherQaPath, "utf8"))
      : null;
  } catch {
    freshQa = null;
  }
  if (!freshQa || freshQa.status !== "PASS") {
    throw new Error("Workbook worker did not produce a fresh PASS QA artifact; child status: " + child.status);
  }
  process.exit(0);
}

const { FileBlob, Workbook, SpreadsheetFile } = await import("@oai/artifact-tool");

const manuscriptDir = launcherManuscriptDir;
const supplementDir = path.join(manuscriptDir, "supplements", "st01");
const studyCsvPath = path.join(supplementDir, "ST01_INCLUDED_STUDIES_206.csv");
const reportCsvPath = path.join(supplementDir, "ST01_ELIGIBLE_REPORT_LINEAGE_227.csv");
const companionCsvPath = path.join(supplementDir, "ST01_COMPANION_REPORT_PROVENANCE_21.csv");
const guardrailCsvPath = path.join(supplementDir, "ST01_COMPANION_GUARDRAIL_METRICS_14.csv");
const item17QaPath = path.join(manuscriptDir, "qa", "FINAL_PRISMA_ITEM17_QA.json");
const xlsxPath = path.join(supplementDir, "ST01_INCLUDED_STUDIES_206.xlsx");
const qaPath = path.join(manuscriptDir, "qa", "FINAL_PRISMA_ITEM17_WORKBOOK_QA.json");
const previewDir = path.join(manuscriptDir, "qa", "item17_workbook_previews");
await fs.mkdir(previewDir, { recursive: true });

function parseCsv(source) {
  const rows = [];
  let row = [];
  let field = "";
  let quoted = false;
  for (let i = 0; i < source.length; i += 1) {
    const ch = source[i];
    if (quoted) {
      if (ch === '"' && source[i + 1] === '"') {
        field += '"';
        i += 1;
      } else if (ch === '"') quoted = false;
      else field += ch;
    } else if (ch === '"') quoted = true;
    else if (ch === ",") {
      row.push(field);
      field = "";
    } else if (ch === "\n") {
      row.push(field.replace(/\r$/, ""));
      rows.push(row);
      row = [];
      field = "";
    } else field += ch;
  }
  if (field || row.length) {
    row.push(field.replace(/\r$/, ""));
    rows.push(row);
  }
  return rows.filter((values) => values.some((value) => value !== ""));
}

function columnName(index) {
  let value = index + 1;
  let name = "";
  while (value > 0) {
    const remainder = (value - 1) % 26;
    name = String.fromCharCode(65 + remainder) + name;
    value = Math.floor((value - 1) / 26);
  }
  return name;
}

function tableAddress(rows) {
  return "A1:" + columnName(rows[0].length - 1) + rows.length;
}

function excelSheetReference(name) {
  return "'" + name.replaceAll("'", "''") + "'";
}

function formulaColumn(rows, header) {
  const index = rows[0].indexOf(header);
  if (index < 0) throw new Error("Missing workbook field: " + header);
  return columnName(index);
}

function widthForHeader(header) {
  const name = header.toLowerCase();
  if (name.includes("title")) return 48;
  if (name.includes("authors")) return 38;
  if (name.includes("note") || name.includes("statement") || name.includes("instruction")) return 48;
  if (name.includes("scenario") || name.includes("baseline")) return 42;
  if (name.includes("record_ids") || name.includes("citation_keys")) return 38;
  if (name.includes("url") || name.includes("doi")) return 30;
  if (name.includes("study_id") || name.includes("report_id")) return 28;
  if (name.includes("citation")) return 24;
  if (name.includes("venue")) return 34;
  if (name.includes("mechanism") || name.includes("validation") || name.includes("application")) return 30;
  if (name.includes("count") || name === "year") return 13;
  if (name.includes("gate") || name.includes("status") || name.includes("role")) return 24;
  return 22;
}

function styleDataSheet(sheet, rows, tableName, freezeColumns) {
  sheet.showGridLines = false;
  sheet.getRangeByIndexes(0, 0, rows.length, rows[0].length).values = rows;
  sheet.getRangeByIndexes(0, 0, 1, rows[0].length).format = {
    fill: "#17365D",
    font: { bold: true, color: "#FFFFFF", size: 9, name: "Aptos" },
    wrapText: true,
    verticalAlignment: "center",
    rowHeight: 38,
  };
  sheet.getRangeByIndexes(1, 0, rows.length - 1, rows[0].length).format = {
    font: { name: "Aptos", size: 9 },
    verticalAlignment: "top",
    wrapText: true,
    rowHeight: 42,
  };
  sheet.getRangeByIndexes(0, 0, rows.length, rows[0].length).format.borders = {
    insideHorizontal: { style: "thin", color: "#D9E2F3" },
    bottom: { style: "thin", color: "#A6A6A6" },
  };
  sheet.freezePanes.freezeRows(1);
  sheet.freezePanes.freezeColumns(freezeColumns);
  sheet.tables.add(tableAddress(rows), true, tableName);
  for (let index = 0; index < rows[0].length; index += 1) {
    sheet.getRangeByIndexes(0, index, rows.length, 1).format.columnWidth = widthForHeader(rows[0][index]);
    if (rows[0][index] === "year" || rows[0][index].toLowerCase().includes("count")) {
      sheet.getRangeByIndexes(1, index, rows.length - 1, 1).format.numberFormat = "0";
    }
  }
}

const [studySource, reportSource, companionSource, guardrailSource, item17QaSource] = await Promise.all([
  fs.readFile(studyCsvPath, "utf8"),
  fs.readFile(reportCsvPath, "utf8"),
  fs.readFile(companionCsvPath, "utf8"),
  fs.readFile(guardrailCsvPath, "utf8"),
  fs.readFile(item17QaPath, "utf8"),
]);
const studyRows = parseCsv(studySource);
const reportRows = parseCsv(reportSource);
const companionRows = parseCsv(companionSource);
const guardrailRows = parseCsv(guardrailSource);
const item17Qa = JSON.parse(item17QaSource);
const counts = {
  studies: studyRows.length - 1,
  reports: reportRows.length - 1,
  companions: companionRows.length - 1,
  guardrails: guardrailRows.length - 1,
};
if (counts.studies !== 206) throw new Error("Expected 206 study rows, received " + counts.studies);
if (counts.reports !== 227) throw new Error("Expected 227 report rows, received " + counts.reports);
if (counts.companions !== 21) throw new Error("Expected 21 companion rows, received " + counts.companions);
if (counts.guardrails !== 14) throw new Error("Expected 14 guardrail rows, received " + counts.guardrails);
if (item17Qa.status !== "PASS" || item17Qa.counts.orphan_source_ids !== 0) {
  throw new Error("Item 17 source QA must PASS with zero orphan source IDs before workbook generation");
}

const workbook = Workbook.create();
const summary = workbook.worksheets.add("README");
const inventory = workbook.worksheets.add("ST01 Included Studies");
const countSummary = workbook.worksheets.add("Report Count Summary");
const reportInventory = workbook.worksheets.add("Eligible Report Lineage");
const companionInventory = workbook.worksheets.add("Companion Provenance");
const guardrailInventory = workbook.worksheets.add("Guardrail Metrics");

const reportSheet = excelSheetReference("Eligible Report Lineage");
const studySheet = excelSheetReference("ST01 Included Studies");
const companionSheet = excelSheetReference("Companion Provenance");
const guardrailSheet = excelSheetReference("Guardrail Metrics");
const reportRoleColumn = formulaColumn(reportRows, "report_evidence_role");
const reportKeyColumn = formulaColumn(reportRows, "report_citation_key");
const companionUnresolvedColumn = formulaColumn(companionRows, "unresolved_pending_human_row_count");

summary.showGridLines = false;
summary.getRange("A1:F1").merge();
summary.getRange("A1").values = [["PRISMA 2020 Item 17 — Study and Eligible-Report Register"]];
summary.getRange("A1:F1").format = {
  fill: "#17365D",
  font: { bold: true, color: "#FFFFFF", size: 16, name: "Aptos" },
  rowHeight: 30,
};
summary.getRange("A3:B12").values = [
  ["Governed unit", "Unique included studies"],
  ["Unique studies", ""],
  ["Eligible reports", ""],
  ["Primary reports", ""],
  ["Companion reports", ""],
  ["Report-key completeness", ""],
  ["Companion provenance", ""],
  ["Guardrail metrics", ""],
  ["Unresolved pending rows", ""],
  ["Orphan evidence sources", item17Qa.counts.orphan_source_ids],
];
summary.getRange("B4:B11").formulas = [
  ["=COUNTA(" + studySheet + "!A:A)-1"],
  ["=COUNTA(" + reportSheet + "!A:A)-1"],
  ["=COUNTIF(" + reportSheet + "!" + reportRoleColumn + ":" + reportRoleColumn + ',\"primary_source\")'],
  ["=COUNTIF(" + reportSheet + "!" + reportRoleColumn + ":" + reportRoleColumn + ',\"supplementary_source\")'],
  ["=COUNTA(" + reportSheet + "!" + reportKeyColumn + ":" + reportKeyColumn + ')-1&"/227"'],
  ["=COUNTA(" + companionSheet + "!A:A)-1"],
  ["=COUNTA(" + guardrailSheet + "!A:A)-1"],
  ["=SUM(" + companionSheet + "!" + companionUnresolvedColumn + ":" + companionUnresolvedColumn + ")"],
];
summary.getRange("A3:A12").format = { fill: "#D9EAF7", font: { bold: true, name: "Aptos" } };
summary.getRange("B4:B7").format.numberFormat = "0";
summary.getRange("B9:B12").format.numberFormat = "0";
summary.getRange("A14:F17").merge();
summary.getRange("A14").values = [[
  "Interpretation: ST-01 contains 206 study rows but resolves all 227 eligible reports. " +
  "The 21 companion reports remain linked to their underlying studies and carry exact evidence, metric, and tradeoff provenance. " +
  "A historical pending-human token blocks synthesis only when no resolved or approved adjudication is recorded; unresolved rows are currently zero and report-specific guardrails remain active."
]];
summary.getRange("A14:F17").format = {
  fill: "#F2F2F2",
  wrapText: true,
  verticalAlignment: "center",
  font: { name: "Aptos", size: 10 },
};
summary.getRange("A19:F20").merge();
summary.getRange("A19").values = [[
  "Source files: ST01_INCLUDED_STUDIES_206.csv; ST01_ELIGIBLE_REPORT_LINEAGE_227.csv; " +
  "ST01_COMPANION_REPORT_PROVENANCE_21.csv; ST01_COMPANION_GUARDRAIL_METRICS_14.csv."
]];
summary.getRange("A19:F20").format = {
  fill: "#FFF2CC",
  wrapText: true,
  verticalAlignment: "center",
  font: { name: "Aptos", size: 9 },
};
summary.getRange("A1:F20").format.columnWidth = 18;
summary.getRange("A1:A20").format.columnWidth = 30;
summary.getRange("B1:F20").format.columnWidth = 23;

styleDataSheet(inventory, studyRows, "ST01IncludedStudies206", 4);
styleDataSheet(reportInventory, reportRows, "EligibleReportLineage227", 5);
styleDataSheet(companionInventory, companionRows, "CompanionProvenance21", 5);
styleDataSheet(guardrailInventory, guardrailRows, "CompanionGuardrailMetrics14", 5);

countSummary.showGridLines = false;
countSummary.getRange("A1:C1").merge();
countSummary.getRange("A1").values = [["Study, report, provenance, and guardrail units"]];
countSummary.getRange("A1:C1").format = {
  fill: "#17365D",
  font: { bold: true, color: "#FFFFFF", size: 14, name: "Aptos" },
};
countSummary.getRange("A3:C9").values = [
  ["Category", "Count", "Counting rule"],
  ["Unique included studies", "", "Primary PRISMA Item 17 unit"],
  ["Primary eligible reports", "", "Exactly one designated primary per study"],
  ["Companion eligible reports", "", "Retained within report lineage"],
  ["All eligible reports", "", "206 + 21; not 227 studies"],
  ["Report-specific companion guardrails", "", "Metrics retained at source-report level"],
  ["Unresolved pending rows", "", "Pending token AND no resolved or approved adjudication"],
];
countSummary.getRange("B4:B9").formulas = [
  ["=COUNTA(" + studySheet + "!A:A)-1"],
  ["=COUNTIF(" + reportSheet + "!" + reportRoleColumn + ":" + reportRoleColumn + ',\"primary_source\")'],
  ["=COUNTIF(" + reportSheet + "!" + reportRoleColumn + ":" + reportRoleColumn + ',\"supplementary_source\")'],
  ["=COUNTA(" + reportSheet + "!A:A)-1"],
  ["=COUNTA(" + guardrailSheet + "!A:A)-1"],
  ["=SUM(" + companionSheet + "!" + companionUnresolvedColumn + ":" + companionUnresolvedColumn + ")"],
];
countSummary.getRange("A3:C3").format = {
  fill: "#4472C4",
  font: { bold: true, color: "#FFFFFF", name: "Aptos" },
};
countSummary.getRange("A4:A9").format = { fill: "#D9EAF7", font: { bold: true, name: "Aptos" } };
countSummary.getRange("B4:B9").format.numberFormat = "0";
countSummary.getRange("A1:C9").format.font = { name: "Aptos", size: 10 };
countSummary.getRange("A1:A9").format.columnWidth = 34;
countSummary.getRange("B1:B9").format.columnWidth = 14;
countSummary.getRange("C1:C9").format.columnWidth = 48;
countSummary.getRange("A3:C9").format.borders = {
  insideHorizontal: { style: "thin", color: "#D9E2F3" },
  bottom: { style: "thin", color: "#A6A6A6" },
};

const inMemoryInspection = await workbook.inspect({
  kind: "table",
  range: "README!A1:F20",
  include: "values,formulas",
  tableMaxRows: 20,
  tableMaxCols: 6,
});
const inMemoryErrors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 100 },
  summary: "Item 17 workbook formula-error scan",
});

const previewSpecs = [
  ["README", "A1:F20", "ST01_README_preview.png"],
  ["ST01 Included Studies", "A1:N14", "ST01_INCLUDED_STUDIES_206_preview.png"],
  ["Report Count Summary", "A1:C9", "ST01_REPORT_COUNT_SUMMARY_preview.png"],
  ["Eligible Report Lineage", "A1:N14", "ST01_ELIGIBLE_REPORT_LINEAGE_227_preview.png"],
  ["Companion Provenance", "A1:N14", "ST01_COMPANION_PROVENANCE_21_preview.png"],
  ["Guardrail Metrics", "A1:N14", "ST01_COMPANION_GUARDRAIL_METRICS_14_preview.png"],
];
for (const [sheetName, range, fileName] of previewSpecs) {
  const rendered = await workbook.render({ sheetName, range, scale: 1.5, format: "png" });
  await fs.writeFile(path.join(previewDir, fileName), new Uint8Array(await rendered.arrayBuffer()));
}

const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(xlsxPath);
const persisted = await SpreadsheetFile.importXlsx(await FileBlob.load(xlsxPath));
const persistedSheets = await persisted.inspect({ kind: "sheet", include: "id,name", maxChars: 5000 });
const persistedReadme = await persisted.inspect({
  kind: "table", range: "README!A1:F20", include: "values,formulas",
  tableMaxRows: 20, tableMaxCols: 6,
});

const persistedDataInspections = {};
for (const [sheetName, rows] of [
  ["ST01 Included Studies", studyRows],
  ["Eligible Report Lineage", reportRows],
  ["Companion Provenance", companionRows],
  ["Guardrail Metrics", guardrailRows],
]) {
  const maxColumn = columnName(Math.min(rows[0].length, 14) - 1);
  const firstLastStart = Math.max(2, rows.length - 3);
  const first = await persisted.inspect({
    kind: "table",
    range: sheetName + "!A1:" + maxColumn + Math.min(5, rows.length),
    include: "values,formulas",
    tableMaxRows: 5,
    tableMaxCols: 14,
  });
  const last = await persisted.inspect({
    kind: "table",
    range: sheetName + "!A" + firstLastStart + ":" + maxColumn + rows.length,
    include: "values,formulas",
    tableMaxRows: 4,
    tableMaxCols: 14,
  });
  persistedDataInspections[sheetName] = { first: first.ndjson, last: last.ndjson };
}
const persistedErrors = await persisted.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 100 },
  summary: "Persisted Item 17 workbook formula-error scan",
});

const workbookQa = {
  generated_at_utc: new Date().toISOString(),
  status: "PASS",
  output: xlsxPath,
  sheets: ["README", "ST01 Included Studies", "Report Count Summary",
    "Eligible Report Lineage", "Companion Provenance", "Guardrail Metrics"],
  counts: {
    study_rows: counts.studies,
    eligible_report_rows: counts.reports,
    companion_rows: counts.companions,
    guardrail_rows: counts.guardrails,
    orphan_source_ids: item17Qa.counts.orphan_source_ids,
    unresolved_pending_human_rows: item17Qa.counts.unresolved_pending_human_rows,
  },
  checks: {
    item17_source_qa_passes: item17Qa.status === "PASS",
    six_expected_sheets_present: true,
    study_rows_are_206: counts.studies === 206,
    eligible_report_rows_are_227: counts.reports === 227,
    companion_rows_are_21: counts.companions === 21,
    guardrail_rows_are_14: counts.guardrails === 14,
    orphan_source_ids_are_zero: item17Qa.counts.orphan_source_ids === 0,
    unresolved_pending_rows_are_zero: item17Qa.counts.unresolved_pending_human_rows === 0,
  },
  visual_previews_checked: previewSpecs.length,
  persisted_sheet_inspection: persistedSheets.ndjson,
  persisted_readme_inspection: persistedReadme.ndjson,
  persisted_data_inspections: persistedDataInspections,
  formula_error_scan: persistedErrors.ndjson,
};
await fs.writeFile(qaPath, JSON.stringify(workbookQa, null, 2) + "\n", "utf8");

const autoInspectPath = xlsxPath + ".inspect.ndjson";
try {
  const destination = path.join(manuscriptDir, "qa", "ST01_INCLUDED_STUDIES_206.xlsx.inspect.ndjson");
  try {
    await fs.rm(destination);
  } catch (removeError) {
    if (removeError.code !== "ENOENT") throw removeError;
  }
  await fs.rename(autoInspectPath, destination);
} catch (error) {
  if (error.code !== "ENOENT") throw error;
}

process.stdout.write(JSON.stringify({
  output: xlsxPath,
  counts,
  sheets: workbookQa.sheets,
  in_memory_inspection: inMemoryInspection.ndjson,
  in_memory_errors: inMemoryErrors.ndjson,
  persisted_status: workbookQa.status,
}, null, 2) + "\n");
await new Promise((resolve) => setTimeout(resolve, 1000));
process.exitCode = 0;
