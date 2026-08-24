import fs from "node:fs/promises";
import path from "node:path";
import crypto from "node:crypto";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const toolDir = path.dirname(new URL(import.meta.url).pathname.replace(/^\/(.:)/, "$1"));
const manuscriptDir = path.resolve(toolDir, "..");
const sourceDir = path.join(manuscriptDir, "supplements", "evidence");
const xlsxPath = path.join(sourceDir, "OISAC_JOURNAL_EVIDENCE_SUPPLEMENTS_2026-08-13.xlsx");
const qaPath = path.join(manuscriptDir, "qa", "JOURNAL_EVIDENCE_WORKBOOK_QA_2026-08-13.json");
const workbookChecksumPath = path.join(sourceDir, "WORKBOOK_SHA256.txt");

const expected = new Map([
  ["FT Exclusions", 39],
  ["Primary Evidence", 3020],
  ["Primary Metrics", 4779],
  ["Governed Tradeoffs", 404],
  ["Substantive Tradeoffs", 402],
  ["Study TQAF", 206],
  ["Evidence Bodies", 115],
  ["Body Membership", 4931],
]);

const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(xlsxPath));
const observed = {};
const checks = {};
for (const [sheetName, expectedRows] of expected.entries()) {
  const sheet = workbook.worksheets.getItem(sheetName);
  const used = sheet.getUsedRange()?.values ?? [];
  const actualRows = Math.max(0, used.length - 1);
  observed[sheetName] = actualRows;
  checks[`${sheetName}_row_count`] = actualRows === expectedRows;
  checks[`${sheetName}_header_nonblank`] = Boolean(used[0]?.length) && used[0].every((value) => String(value ?? "").trim() !== "");
}

const readme = workbook.worksheets.getItem("README");
const readmeValues = readme.getUsedRange()?.values ?? [];
checks.readme_present = readmeValues.length >= 16;
checks.worksheet_count = workbook.worksheets.items.length === 9;
const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 200 },
  summary: "Reopened journal evidence workbook formula-error scan",
});
const errorText = errors.ndjson ?? "";
checks.no_formula_errors = !/#REF!|#DIV\/0!|#VALUE!|#NAME\?|#N\/A/.test(errorText);
const pass = Object.values(checks).every(Boolean);
const workbookBytes = await fs.readFile(xlsxPath);
const workbookSha256 = crypto.createHash("sha256").update(workbookBytes).digest("hex");
const qa = {
  status: pass ? "PASS" : "FAIL",
  workbook: path.basename(xlsxPath),
  worksheets: workbook.worksheets.items.map((sheet) => sheet.name),
  observedRows: observed,
  checks,
  formulaErrorInspection: errorText,
  workbookSha256,
};
await fs.writeFile(qaPath, `${JSON.stringify(qa, null, 2)}\n`, "utf8");
await fs.writeFile(workbookChecksumPath, `${workbookSha256}  ${path.basename(xlsxPath)}\n`, "ascii");
process.stdout.write(`${JSON.stringify(qa, null, 2)}\n`);
if (!pass) process.exitCode = 1;
