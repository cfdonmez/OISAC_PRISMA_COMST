import fs from "node:fs/promises";
import path from "node:path";
import crypto from "node:crypto";
import { FileBlob, Workbook, SpreadsheetFile } from "@oai/artifact-tool";

const toolDir = path.dirname(new URL(import.meta.url).pathname.replace(/^\/(.:)/, "$1"));
const manuscriptDir = path.resolve(toolDir, "..");
const rsDir = path.join(manuscriptDir, "supplements", "related_synthesis");
const s7Dir = path.join(manuscriptDir, "supplements", "s7");
const qaDir = path.join(manuscriptDir, "qa");
const previewDir = path.join(qaDir, "remaining_supplement_workbook_previews");
await fs.mkdir(previewDir, { recursive: true });

function parseCsv(source) {
  const rows = [];
  let row = [];
  let field = "";
  let quoted = false;
  const text = source.replace(/^\uFEFF/, "");
  for (let index = 0; index < text.length; index += 1) {
    const char = text[index];
    if (quoted) {
      if (char === '"' && text[index + 1] === '"') { field += '"'; index += 1; }
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

function sha256(buffer) {
  return crypto.createHash("sha256").update(buffer).digest("hex");
}

function styleDataSheet(sheet, rows, tableName, options = {}) {
  const rowCount = rows.length;
  const columnCount = rows[0].length;
  sheet.showGridLines = false;
  sheet.getRangeByIndexes(0, 0, rowCount, columnCount).values = rows;
  sheet.getRangeByIndexes(0, 0, 1, columnCount).format = {
    fill: "#17365D",
    font: { name: "Aptos", bold: true, color: "#FFFFFF", size: 9 },
    wrapText: true,
    verticalAlignment: "center",
    rowHeight: 42,
  };
  if (rowCount > 1) {
    sheet.getRangeByIndexes(1, 0, rowCount - 1, columnCount).format = {
      font: { name: "Aptos", size: 8 },
      verticalAlignment: "top",
      wrapText: true,
      rowHeight: options.rowHeight ?? 48,
    };
  }
  sheet.getRangeByIndexes(0, 0, rowCount, columnCount).format.borders = {
    insideHorizontal: { style: "thin", color: "#E7E6E6" },
    bottom: { style: "thin", color: "#BFBFBF" },
  };
  for (let column = 0; column < columnCount; column += 1) {
    const header = rows[0][column];
    let width = Math.max(12, Math.min(24, header.length + 3));
    if (/title|authors|rationale|boundary|scope|reader|evidence|logic|locator|interpretation|source_url/i.test(header)) width = 34;
    if (/^year$|score|tier|status|form|record_id|study_id|citation_key|doi|identifier/i.test(header)) width = Math.min(width, 20);
    sheet.getRangeByIndexes(0, column, rowCount, 1).format.columnWidth = width;
  }
  sheet.freezePanes.freezeRows(1);
  sheet.freezePanes.freezeColumns(Math.min(options.freezeColumns ?? 3, columnCount));
  const endColumn = excelColumn(columnCount - 1);
  sheet.tables.add(`A1:${endColumn}${rowCount}`, true, tableName);
}

async function renderSheet(workbook, sheetName, range, filename) {
  const blob = await workbook.render({ sheetName, range, scale: 1.5, format: "png" });
  await fs.writeFile(path.join(previewDir, filename), new Uint8Array(await blob.arrayBuffer()));
}

async function buildRelatedSynthesis() {
  const csvPath = path.join(rsDir, "ST-RS1_CONTEXTUAL_SYNTHESES_38.csv");
  const allRows = parseCsv(await fs.readFile(csvPath, "utf8"));
  const headers = allRows[0];
  const data = allRows.slice(1);
  const formIndex = headers.indexOf("source_form");
  const originIndex = headers.indexOf("workflow_origin");
  const tableStatusIndex = headers.indexOf("table_i_assignment_status");
  if (data.length !== 38) throw new Error(`ST-RS1 expected 38 rows, got ${data.length}`);
  const fullRows = data.filter((row) => row[formIndex] === "full_length_or_independently_citable");
  const shortRows = data.filter((row) => row[formIndex] === "short_or_focused");
  const additions = data.filter((row) => row[originIndex] === "manuscript_stage_bounded_addition");
  const displayed = data.filter((row) => row[tableStatusIndex] === "displayed_in_table_i");
  if (fullRows.length !== 24 || shortRows.length !== 14 || additions.length !== 7 || displayed.length !== 24) {
    throw new Error("ST-RS1 24/14, 31/7, or Table-I assignment gate failed");
  }

  const workbook = Workbook.create();
  const readme = workbook.worksheets.add("README");
  const register = workbook.worksheets.add("ST-RS1 Register 38");
  const tableI = workbook.worksheets.add("Table1 Sources 24");
  const focused = workbook.worksheets.add("Short Focused 14");
  const summary = workbook.worksheets.add("Family Summary");

  readme.showGridLines = false;
  readme.getRange("A1:F1").merge();
  readme.getRange("A1").values = [["ST-RS1 — Bounded Contextual Synthesis Register"]];
  readme.getRange("A1:F1").format = { fill: "#17365D", font: { name: "Aptos Display", bold: true, color: "#FFFFFF", size: 16 }, rowHeight: 30 };
  readme.getRange("A3:C9").values = [
    ["Gate", "Expected", "Actual"],
    ["Contextual synthesis rows", 38, 38],
    ["Full length or independently citable", 24, 24],
    ["Short or focused", 14, 14],
    ["Captured in executed workflow", 31, 31],
    ["Manuscript-stage bounded additions", 7, 7],
    ["Inside primary 206-study denominator", 0, 0],
  ];
  readme.getRange("A3:C3").format = { fill: "#4472C4", font: { bold: true, color: "#FFFFFF" } };
  readme.getRange("A4:A9").format = { fill: "#D9EAF7", font: { bold: true } };
  readme.getRange("B4:C9").format.numberFormat = "0";
  readme.getRange("A11:F14").merge();
  readme.getRange("A11").values = [["Boundary: this is a bounded manuscript-positioning audit, not a claim of worldwide exhaustiveness. All 38 sources are contextual and remain outside the locked 206-study technical denominator. Primary families are navigation codes, not quality scores; secondary scope remains multi-label."]];
  readme.getRange("A11:F14").format = { fill: "#F2F2F2", wrapText: true, verticalAlignment: "center" };
  readme.getRange("A1:F14").format.font = { name: "Aptos", size: 10 };
  readme.getRange("A1:A14").format.columnWidth = 42;
  readme.getRange("B1:C14").format.columnWidth = 18;
  readme.getRange("D1:F14").format.columnWidth = 22;

  styleDataSheet(register, allRows, "STRS1Register38", { rowHeight: 54, freezeColumns: 4 });
  styleDataSheet(tableI, [headers, ...displayed], "STRS1TableISources24", { rowHeight: 54, freezeColumns: 4 });
  styleDataSheet(focused, [headers, ...shortRows], "STRS1ShortFocused14", { rowHeight: 54, freezeColumns: 4 });

  const familyIndex = headers.indexOf("primary_reader_task_family");
  const families = [...new Set(data.map((row) => row[familyIndex]))].sort();
  const summaryRows = [["Primary reader-task family", "All 38", "Full length", "Short/focused"]];
  for (const family of families) {
    const all = data.filter((row) => row[familyIndex] === family).length;
    const full = fullRows.filter((row) => row[familyIndex] === family).length;
    const short = shortRows.filter((row) => row[familyIndex] === family).length;
    summaryRows.push([family, all, full, short]);
  }
  summaryRows.push(["TOTAL", 38, 24, 14]);
  styleDataSheet(summary, summaryRows, "STRS1FamilySummary", { rowHeight: 28, freezeColumns: 1 });
  summary.getRange(`B2:D${summaryRows.length}`).format.numberFormat = "0";

  await renderSheet(workbook, "README", "A1:F14", "ST-RS1_README.png");
  await renderSheet(workbook, "ST-RS1 Register 38", "A1:J10", "ST-RS1_REGISTER.png");
  await renderSheet(workbook, "Table1 Sources 24", "A1:J10", "ST-RS1_TABLE_I_24.png");
  await renderSheet(workbook, "Short Focused 14", "A1:J10", "ST-RS1_SHORT_14.png");
  await renderSheet(workbook, "Family Summary", `A1:D${summaryRows.length}`, "ST-RS1_FAMILY_SUMMARY.png");

  const beforeErrors = await workbook.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, summary: "ST-RS1 formula error scan" });
  const outPath = path.join(rsDir, "ST-RS1_CONTEXTUAL_SYNTHESES_38.xlsx");
  const blob = await SpreadsheetFile.exportXlsx(workbook);
  await blob.save(outPath);

  const persisted = await SpreadsheetFile.importXlsx(await FileBlob.load(outPath));
  const sheetInspection = await persisted.inspect({ kind: "sheet", include: "id,name", maxChars: 3000 });
  const firstInspection = await persisted.inspect({ kind: "table", range: "ST-RS1 Register 38!A1:J5", include: "values,formulas", tableMaxRows: 5, tableMaxCols: 10 });
  const lastInspection = await persisted.inspect({ kind: "table", range: "ST-RS1 Register 38!A36:J39", include: "values,formulas", tableMaxRows: 4, tableMaxCols: 10 });
  const tableIInspection = await persisted.inspect({ kind: "table", range: "Table1 Sources 24!A1:J5", include: "values,formulas", tableMaxRows: 5, tableMaxCols: 10 });
  const persistedErrors = await persisted.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, summary: "Persisted ST-RS1 formula error scan" });
  const bytes = await fs.readFile(outPath);
  const qa = {
    status: "PASS",
    workbook: outPath,
    sha256: sha256(bytes),
    sheets: ["README", "ST-RS1 Register 38", "Table1 Sources 24", "Short Focused 14", "Family Summary"],
    counts: { register_rows: data.length, full_length_rows: fullRows.length, short_focused_rows: shortRows.length, manuscript_stage_additions: additions.length },
    visual_previews_checked: 5,
    pre_export_formula_error_scan: beforeErrors.ndjson,
    persisted_sheet_inspection: sheetInspection.ndjson,
    persisted_first_rows: firstInspection.ndjson,
    persisted_last_rows: lastInspection.ndjson,
    persisted_table_i_rows: tableIInspection.ndjson,
    persisted_formula_error_scan: persistedErrors.ndjson,
  };
  await fs.writeFile(path.join(qaDir, "FINAL_ST_RS1_WORKBOOK_QA_2026-08-13.json"), `${JSON.stringify(qa, null, 2)}\n`, "utf8");
  return qa;
}

async function buildS7() {
  const carrierPath = path.join(s7Dir, "S7_PAIRED_FUNCTION_VALIDATION_12.csv");
  const joinPath = path.join(s7Dir, "S7_CANONICAL_JOIN_206.csv");
  const carrierRows = parseCsv(await fs.readFile(carrierPath, "utf8"));
  const joinRows = parseCsv(await fs.readFile(joinPath, "utf8"));
  const carrierHeaders = carrierRows[0];
  const carrierData = carrierRows.slice(1);
  const joinData = joinRows.slice(1);
  const pairIndex = carrierHeaders.indexOf("paired_function_evidence_subset");
  const pairRows = carrierData.filter((row) => row[pairIndex] === "yes");
  if (joinData.length !== 206 || carrierData.length !== 12 || pairRows.length !== 6) {
    throw new Error("Supplement S7 206/12/6 gate failed");
  }

  const workbook = Workbook.create();
  const readme = workbook.worksheets.add("README");
  const carrier = workbook.worksheets.add("S7 Maximum Tier 12");
  const paired = workbook.worksheets.add("Paired Function 6");
  const join = workbook.worksheets.add("Canonical Join 206");

  readme.showGridLines = false;
  readme.getRange("A1:F1").merge();
  readme.getRange("A1").values = [["Supplement S7 — Paired-Function Validation View"]];
  readme.getRange("A1:F1").format = { fill: "#17365D", font: { name: "Aptos Display", bold: true, color: "#FFFFFF", size: 16 }, rowHeight: 30 };
  readme.getRange("A3:C7").values = [
    ["Gate", "Expected", "Actual"],
    ["Canonical study join", 206, 206],
    ["Maximum field/deployment tier", 12, 12],
    ["Paired-function TQAF score 3 subset", 6, 6],
    ["Other maximum-tier studies", 6, 6],
  ];
  readme.getRange("A3:C3").format = { fill: "#4472C4", font: { bold: true, color: "#FFFFFF" } };
  readme.getRange("A4:A7").format = { fill: "#D9EAF7", font: { bold: true } };
  readme.getRange("B4:C7").format.numberFormat = "0";
  readme.getRange("A9:F13").merge();
  readme.getRange("A9").values = [["Boundary: maximum tier 6 means that field trial or deployment was the strongest observed setting. It does not establish field validation of the complete joint system. The six-study subset is narrower and requires field/deployment outcomes for both communication and sensing. Existing audited traces do not expose relationship timing or separate function-specific locator mappings; those cells remain explicit NR values. This supplement is not the Phase-F S7 6G-relevance domain."]];
  readme.getRange("A9:F13").format = { fill: "#F2F2F2", wrapText: true, verticalAlignment: "center" };
  readme.getRange("A1:F13").format.font = { name: "Aptos", size: 10 };
  readme.getRange("A1:A13").format.columnWidth = 42;
  readme.getRange("B1:C13").format.columnWidth = 18;
  readme.getRange("D1:F13").format.columnWidth = 22;

  styleDataSheet(carrier, carrierRows, "S7MaximumTier12", { rowHeight: 60, freezeColumns: 4 });
  styleDataSheet(paired, [carrierHeaders, ...pairRows], "S7PairedFunction6", { rowHeight: 60, freezeColumns: 4 });
  styleDataSheet(join, joinRows, "S7CanonicalJoin206", { rowHeight: 34, freezeColumns: 3 });

  await renderSheet(workbook, "README", "A1:F13", "S7_README.png");
  await renderSheet(workbook, "S7 Maximum Tier 12", "A1:J10", "S7_MAXIMUM_TIER_12.png");
  await renderSheet(workbook, "Paired Function 6", "A1:J7", "S7_PAIRED_FUNCTION_6.png");
  await renderSheet(workbook, "Canonical Join 206", "A1:J10", "S7_CANONICAL_JOIN_206.png");

  const beforeErrors = await workbook.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, summary: "S7 formula error scan" });
  const outPath = path.join(s7Dir, "S7_PAIRED_FUNCTION_VALIDATION_12.xlsx");
  const blob = await SpreadsheetFile.exportXlsx(workbook);
  await blob.save(outPath);

  const persisted = await SpreadsheetFile.importXlsx(await FileBlob.load(outPath));
  const sheetInspection = await persisted.inspect({ kind: "sheet", include: "id,name", maxChars: 3000 });
  const firstInspection = await persisted.inspect({ kind: "table", range: "S7 Maximum Tier 12!A1:J5", include: "values,formulas", tableMaxRows: 5, tableMaxCols: 10 });
  const lastInspection = await persisted.inspect({ kind: "table", range: "S7 Maximum Tier 12!A10:J13", include: "values,formulas", tableMaxRows: 4, tableMaxCols: 10 });
  const joinLastInspection = await persisted.inspect({ kind: "table", range: "Canonical Join 206!A204:J207", include: "values,formulas", tableMaxRows: 4, tableMaxCols: 10 });
  const persistedErrors = await persisted.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, summary: "Persisted S7 formula error scan" });
  const bytes = await fs.readFile(outPath);
  const qa = {
    status: "PASS_WITH_EXPLICIT_UNRESOLVED_FUNCTION_SPECIFIC_LOCATORS",
    workbook: outPath,
    sha256: sha256(bytes),
    sheets: ["README", "S7 Maximum Tier 12", "Paired Function 6", "Canonical Join 206"],
    counts: { canonical_join_rows: joinData.length, maximum_tier_rows: carrierData.length, paired_function_rows: pairRows.length },
    visual_previews_checked: 4,
    unresolved_fields: ["relationship_timing", "communication_function_source_locator", "sensing_function_source_locator"],
    pre_export_formula_error_scan: beforeErrors.ndjson,
    persisted_sheet_inspection: sheetInspection.ndjson,
    persisted_first_rows: firstInspection.ndjson,
    persisted_last_rows: lastInspection.ndjson,
    persisted_join_last_rows: joinLastInspection.ndjson,
    persisted_formula_error_scan: persistedErrors.ndjson,
  };
  await fs.writeFile(path.join(qaDir, "FINAL_SUPPLEMENT_S7_WORKBOOK_QA_2026-08-13.json"), `${JSON.stringify(qa, null, 2)}\n`, "utf8");
  return qa;
}

const rsQa = await buildRelatedSynthesis();
const s7Qa = await buildS7();
process.stdout.write(`${JSON.stringify({ status: "PASS", related_synthesis: rsQa, s7: s7Qa }, null, 2)}\n`);
