import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const scriptDir = path.dirname(new URL(import.meta.url).pathname.replace(/^\/(.:)/, "$1"));
const root = path.resolve(scriptDir, "..");
const sectionDir = path.join(root, "sections");
const st01Path = path.join(root, "supplements", "st01", "ST01_INCLUDED_STUDIES_206.csv");
const categoryPath = path.join(root, "qa", "study_category_citation_map_206.csv");
const tradeoffPath = path.join(root, "supplements", "evidence", "ST-19_SUBSTANTIVE_TRADEOFFS_402.csv");
const evidencePath = path.join(root, "supplements", "evidence", "ST-19_PRIMARY_EVIDENCE_RESULTS_3020.csv");
const metricPath = path.join(root, "supplements", "evidence", "ST-19_PRIMARY_METRIC_RESULTS_4779.csv");
const csvOut = path.join(root, "qa", "CITATION_PLACEMENT_CROSSWALK_206.csv");
const xlsxOut = path.join(root, "qa", "CITATION_PLACEMENT_CROSSWALK_206.xlsx");
const jsonOut = path.join(root, "qa", "FINAL_MAIN_CITATION_COVERAGE_206.json");
const mdOut = path.join(root, "qa", "FINAL_MAIN_CITATION_COVERAGE_206.md");
const previewDir = path.join(root, "qa", "citation_completion_previews");

function parseCsv(source) {
  const rows = [];
  let row = [];
  let field = "";
  let quoted = false;
  for (let i = 0; i < source.length; i += 1) {
    const ch = source[i];
    if (quoted) {
      if (ch === '"' && source[i + 1] === '"') { field += '"'; i += 1; }
      else if (ch === '"') quoted = false;
      else field += ch;
    } else if (ch === '"') quoted = true;
    else if (ch === ",") { row.push(field); field = ""; }
    else if (ch === "\n") { row.push(field.replace(/\r$/, "")); rows.push(row); row = []; field = ""; }
    else field += ch;
  }
  if (field || row.length) { row.push(field.replace(/\r$/, "")); rows.push(row); }
  return rows.filter((values) => values.some((value) => value !== ""));
}

function objectsFromCsv(source) {
  const rows = parseCsv(source);
  const headers = rows[0];
  return rows.slice(1).map((row) => Object.fromEntries(headers.map((header, index) => [header, row[index] ?? ""])));
}

function csvEscape(value) {
  const text = String(value ?? "");
  return /[",\r\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}

function serializeCsv(headers, rows) {
  return `${[headers, ...rows.map((row) => headers.map((header) => row[header] ?? ""))]
    .map((row) => row.map(csvEscape).join(","))
    .join("\r\n")}\r\n`;
}

function lineNumberAt(text, index) {
  let count = 1;
  for (let i = 0; i < index; i += 1) if (text.charCodeAt(i) === 10) count += 1;
  return count;
}

function headingAt(text, index) {
  const prefix = text.slice(0, index);
  const matches = [...prefix.matchAll(/\\(section|subsection|subsubsection)\{([^}]*)\}/g)];
  const hierarchy = { section: "", subsection: "", subsubsection: "" };
  for (const match of matches) {
    if (match[1] === "section") {
      hierarchy.section = match[2];
      hierarchy.subsection = "";
      hierarchy.subsubsection = "";
    } else if (match[1] === "subsection") {
      hierarchy.subsection = match[2];
      hierarchy.subsubsection = "";
    } else hierarchy.subsubsection = match[2];
  }
  return [hierarchy.section, hierarchy.subsection, hierarchy.subsubsection].filter(Boolean).join(" > ");
}

function isInsideTable(text, index) {
  const prefix = text.slice(0, index);
  const begin = Math.max(prefix.lastIndexOf("\\begin{table}"), prefix.lastIndexOf("\\begin{table*}"));
  const end = Math.max(prefix.lastIndexOf("\\end{table}"), prefix.lastIndexOf("\\end{table*}"));
  return begin > end;
}

function sectionPriority(fileName) {
  const prefix = Number.parseInt(fileName.slice(0, 2), 10);
  const order = new Map([[5, 1], [6, 2], [7, 3], [4, 4], [2, 5], [8, 6], [1, 7], [3, 8], [9, 9], [0, 10], [10, 11]]);
  return order.get(prefix) ?? 99;
}

const st01 = objectsFromCsv(await fs.readFile(st01Path, "utf8"));
const categories = objectsFromCsv(await fs.readFile(categoryPath, "utf8"));
const tradeoffs = objectsFromCsv(await fs.readFile(tradeoffPath, "utf8"));
const evidence = objectsFromCsv(await fs.readFile(evidencePath, "utf8"));
const metrics = objectsFromCsv(await fs.readFile(metricPath, "utf8"));

if (st01.length !== 206) throw new Error(`Expected 206 ST-01 rows, received ${st01.length}`);
if (tradeoffs.length !== 402) throw new Error(`Expected 402 substantive tradeoff rows, received ${tradeoffs.length}`);

const categoryByKey = new Map(categories.map((row) => [row.candidate_bib_key, row]));
const substantiveTradeoffStudies = new Set(tradeoffs.map((row) => row.study_cluster_id));
const pendingByStudy = new Map();
for (const row of [...evidence, ...metrics]) {
  const pendingToken = [row.qa_flag, row.independent_human_status, row.adjudication_status]
    .some((value) => /pending_human/i.test(value ?? ""));
  const resolved = /resolved|approved|survey_use_determined/i.test(row.adjudication_status ?? "") ||
    /verified|survey_claim_eligible_gated/i.test(row.verification_status ?? "") ||
    /human_reviewed_approved/i.test(row.qa_flag ?? "");
  const pending = pendingToken && !resolved;
  if (pending) pendingByStudy.set(row.study_cluster_id, (pendingByStudy.get(row.study_cluster_id) ?? 0) + 1);
}

const occurrences = new Map(st01.map((row) => [row.citation_key, []]));
const citationClusters = [];
let nociteCount = 0;
let manualNumericCitationCount = 0;
let citationFootnoteCount = 0;
const sectionFiles = (await fs.readdir(sectionDir)).filter((name) => name.endsWith(".tex")).sort();
for (const fileName of sectionFiles) {
  const text = await fs.readFile(path.join(sectionDir, fileName), "utf8");
  nociteCount += [...text.matchAll(/\\nocite\{/g)].length;
  manualNumericCitationCount += [...text.matchAll(/\[(?:\d+[\s,;\-–—]*){2,}\]/g)].length;
  citationFootnoteCount += [...text.matchAll(/\\footnote\{[^}]*\\cite/gs)].length;
  for (const match of text.matchAll(/\\cite(?:\[[^\]]*\])?\{([^}]*)\}/gs)) {
    const keys = match[1].split(",").map((key) => key.trim()).filter(Boolean);
    const studyKeys = keys.filter((key) => occurrences.has(key));
    citationClusters.push({
      file: fileName,
      line: lineNumberAt(text, match.index),
      heading: headingAt(text, match.index),
      carrier: isInsideTable(text, match.index) ? "table" : "prose",
      all_keys: keys.join("; "),
      included_study_keys: studyKeys.join("; "),
      included_study_count: studyKeys.length,
    });
    for (const key of keys) {
      if (!occurrences.has(key)) continue;
      occurrences.get(key).push({
        file: fileName,
        line: lineNumberAt(text, match.index),
        heading: headingAt(text, match.index),
        carrier: isInsideTable(text, match.index) ? "table" : "prose",
      });
    }
  }
}

const crosswalk = st01.map((study) => {
  const category = categoryByKey.get(study.citation_key) ?? {};
  const uses = occurrences.get(study.citation_key) ?? [];
  const sorted = [...uses].sort((a, b) => sectionPriority(a.file) - sectionPriority(b.file) || a.line - b.line);
  const primary = sorted[0];
  const proseUses = uses.filter((use) => use.carrier === "prose").length;
  const tableUses = uses.filter((use) => use.carrier === "table").length;
  return {
    study_id: study.study_id,
    citation_key: study.citation_key,
    title: study.title,
    year: study.year,
    modality: study.modality,
    integration_mechanisms: study.integration_mechanisms,
    validation_maturity_max: study.validation_maturity_max,
    validation_types: study.validation_types,
    application_domains: study.application_domains,
    substantive_tradeoff_member: substantiveTradeoffStudies.has(study.study_id) ? "yes" : "no",
    eligible_report_count: study.eligible_report_count,
    companion_eligible_report_count: study.companion_eligible_report_count,
    eligible_report_ids: study.eligible_report_ids,
    cited_in_main: uses.length ? "yes" : "no",
    prose_use_count: proseUses,
    table_use_count: tableUses,
    total_use_count: uses.length,
    primary_narrative_home: primary ? `${primary.file}:${primary.line} | ${primary.heading} | ${primary.carrier}` : "",
    all_main_locations: uses.map((use) => `${use.file}:${use.line}:${use.carrier}`).join("; "),
    pending_human_row_count: pendingByStudy.get(study.study_id) ?? 0,
    canonical_integration_mechanisms: category.canonical_integration_mechanisms ?? "",
    canonical_validation_types: category.canonical_validation_types ?? "",
    canonical_enabling_technologies: category.canonical_enabling_technologies ?? "",
    canonical_application_domains: category.canonical_application_domains ?? "",
    qa_status: uses.length && !(pendingByStudy.get(study.study_id) ?? 0) ? "PASS" : uses.length ? "REQUIRES_PENDING_HUMAN_GUARD" : "MISSING_MAIN_CITATION",
  };
});

const headers = Object.keys(crosswalk[0]);
await fs.writeFile(csvOut, serializeCsv(headers, crosswalk), "utf8");

const cited = crosswalk.filter((row) => row.cited_in_main === "yes");
const missing = crosswalk.filter((row) => row.cited_in_main !== "yes");
const pending = crosswalk.filter((row) => Number(row.pending_human_row_count) > 0);
const citationUses = crosswalk.reduce((sum, row) => sum + Number(row.total_use_count), 0);
const clustersOverSeven = citationClusters.filter((row) => row.included_study_count > 7);
const modalitySummary = [...new Set(crosswalk.map((row) => row.modality))].sort().map((modality) => {
  const rows = crosswalk.filter((row) => row.modality === modality);
  return {
    modality,
    studies: rows.length,
    cited: rows.filter((row) => row.cited_in_main === "yes").length,
    missing: rows.filter((row) => row.cited_in_main !== "yes").length,
  };
});

const status = missing.length === 0 ? (pending.length === 0 ? "PASS" : "PASS_COVERAGE_WITH_PENDING_HUMAN_GUARDS") : "FAIL";
const qa = {
  generated_at_utc: new Date().toISOString(),
  status,
  counts: {
    included_studies: crosswalk.length,
    cited_in_main: cited.length,
    missing_in_main: missing.length,
    included_study_citation_uses: citationUses,
    citation_commands: citationClusters.length,
    included_study_clusters_over_seven: clustersOverSeven.length,
    maximum_included_study_cluster: Math.max(0, ...citationClusters.map((row) => row.included_study_count)),
    nocite_commands: nociteCount,
    manual_numeric_citation_patterns: manualNumericCitationCount,
    citation_bearing_footnotes: citationFootnoteCount,
    substantive_tradeoff_studies: substantiveTradeoffStudies.size,
    studies_with_pending_human_rows: pending.length,
  },
  checks: {
    study_rows_are_206: crosswalk.length === 206,
    all_206_studies_have_semantic_main_citation: missing.length === 0,
    substantive_tradeoff_view_is_402_rows: tradeoffs.length === 402,
    no_duplicate_study_ids: new Set(crosswalk.map((row) => row.study_id)).size === 206,
    no_duplicate_citation_keys: new Set(crosswalk.map((row) => row.citation_key)).size === 206,
    no_nocite_commands: nociteCount === 0,
    no_manual_numeric_citation_patterns: manualNumericCitationCount === 0,
    no_citation_inventory_footnotes: citationFootnoteCount === 0,
    no_included_study_cluster_exceeds_seven: clustersOverSeven.length === 0,
  },
  modality_summary: modalitySummary,
  missing_keys: missing.map((row) => row.citation_key),
  pending_human_studies: pending.map((row) => ({ study_id: row.study_id, citation_key: row.citation_key, pending_rows: row.pending_human_row_count })),
  clusters_over_seven: clustersOverSeven,
};
await fs.writeFile(jsonOut, `${JSON.stringify(qa, null, 2)}\n`, "utf8");

const md = `# Final Main-Citation Coverage QA\n\n` +
  `Status: **${status}**\n\n` +
  `- Included studies: ${crosswalk.length}\n` +
  `- Studies cited in the main article: ${cited.length}\n` +
  `- Missing studies: ${missing.length}\n` +
  `- Included-study citation uses: ${citationUses}\n` +
  `- Citation commands: ${citationClusters.length}\n` +
  `- Included-study clusters above seven: ${clustersOverSeven.length}\n` +
  `- Largest included-study cluster: ${Math.max(0, ...citationClusters.map((row) => row.included_study_count))}\n` +
  `- Nocite commands: ${nociteCount}\n` +
  `- Citation-bearing footnotes: ${citationFootnoteCount}\n` +
  `- Substantive tradeoff studies: ${substantiveTradeoffStudies.size}\n` +
  `- Studies with pending-human source rows: ${pending.length}\n\n` +
  `## Modality reconciliation\n\n` +
  `| Modality | Studies | Cited | Missing |\n|---|---:|---:|---:|\n` +
  modalitySummary.map((row) => `| ${row.modality} | ${row.studies} | ${row.cited} | ${row.missing} |`).join("\n") +
  `\n\n## Interpretation\n\nA citation establishes coverage only when it occurs in an active section or main table. ` +
  `The crosswalk separately exposes studies with unresolved source rows; those rows cannot support narrative or synthesis until resolved or quarantined.\n`;
await fs.writeFile(mdOut, md, "utf8");

const workbook = Workbook.create();
const summary = workbook.worksheets.add("README");
const sheet = workbook.worksheets.add("Citation Crosswalk");
const modalitySheet = workbook.worksheets.add("Modality Summary");
const clusterSheet = workbook.worksheets.add("Citation Clusters");

summary.showGridLines = false;
summary.getRange("A1:F1").merge();
summary.getRange("A1").values = [["O-ISAC Citation Completion Crosswalk"]];
summary.getRange("A1:F1").format = { fill: "#17365D", font: { bold: true, color: "#FFFFFF", size: 16 }, rowHeight: 30 };
summary.getRange("A3:B9").values = [
  ["Status", status],
  ["Included studies", crosswalk.length],
  ["Cited in main article", cited.length],
  ["Missing in main article", missing.length],
  ["Included-study citation uses", citationUses],
  ["Substantive tradeoff studies", substantiveTradeoffStudies.size],
  ["Studies with pending-human rows", pending.length],
];
summary.getRange("A3:A9").format = { fill: "#D9EAF7", font: { bold: true } };
summary.getRange("B4:B9").format.numberFormat = "0";
summary.getRange("A11:F13").merge();
summary.getRange("A11").values = [["Every row is one unique included study. Main-article coverage is based on semantic citations in active section text or main tables; report-level provenance is governed separately by the 227-report ST-01 lineage."]];
summary.getRange("A11:F13").format = { fill: "#F2F2F2", wrapText: true, verticalAlignment: "center" };
summary.getRange("A1:F13").format.font = { name: "Aptos", size: 10 };
summary.getRange("A1:A13").format.columnWidth = 32;
summary.getRange("B1:F13").format.columnWidth = 22;

sheet.showGridLines = false;
const matrix = [headers, ...crosswalk.map((row) => headers.map((header) => row[header]))];
sheet.getRangeByIndexes(0, 0, matrix.length, headers.length).values = matrix;
sheet.getRangeByIndexes(0, 0, 1, headers.length).format = { fill: "#17365D", font: { bold: true, color: "#FFFFFF", size: 9 }, wrapText: true, rowHeight: 38 };
sheet.getRangeByIndexes(1, 0, crosswalk.length, headers.length).format = { font: { name: "Aptos", size: 9 }, verticalAlignment: "top", wrapText: true, rowHeight: 42 };
sheet.getRangeByIndexes(0, 0, matrix.length, headers.length).format.borders = { insideHorizontal: { style: "thin", color: "#D9E2F3" } };
sheet.freezePanes.freezeRows(1);
sheet.freezePanes.freezeColumns(2);
const lastCol = (() => { let number = headers.length; let label = ""; while (number) { number -= 1; label = String.fromCharCode(65 + (number % 26)) + label; number = Math.floor(number / 26); } return label; })();
sheet.tables.add(`A1:${lastCol}${matrix.length}`, true, "CitationCrosswalk206");
const widths = [26, 18, 50, 9, 16, 30, 10, 30, 30, 14, 10, 10, 32, 11, 10, 10, 10, 55, 55, 10, 30, 30, 30, 30, 25];
for (let index = 0; index < headers.length; index += 1) sheet.getRangeByIndexes(0, index, matrix.length, 1).format.columnWidth = widths[index] ?? 22;

modalitySheet.showGridLines = false;
const modalityMatrix = [["Modality", "Studies", "Cited", "Missing"], ...modalitySummary.map((row) => [row.modality, row.studies, row.cited, row.missing])];
modalitySheet.getRangeByIndexes(0, 0, modalityMatrix.length, 4).values = modalityMatrix;
modalitySheet.getRange("A1:D1").format = { fill: "#17365D", font: { bold: true, color: "#FFFFFF" } };
modalitySheet.getRange("A2:A20").format = { fill: "#D9EAF7", font: { bold: true } };
modalitySheet.getRange("B2:D20").format.numberFormat = "0";
modalitySheet.getRange("A1:A20").format.columnWidth = 24;
modalitySheet.getRange("B1:D20").format.columnWidth = 14;

clusterSheet.showGridLines = false;
const clusterHeaders = ["file", "line", "heading", "carrier", "included_study_count", "included_study_keys", "all_keys"];
const clusterMatrix = [clusterHeaders, ...citationClusters.map((row) => clusterHeaders.map((header) => row[header]))];
clusterSheet.getRangeByIndexes(0, 0, clusterMatrix.length, clusterHeaders.length).values = clusterMatrix;
clusterSheet.getRangeByIndexes(0, 0, 1, clusterHeaders.length).format = { fill: "#17365D", font: { bold: true, color: "#FFFFFF", size: 9 }, wrapText: true, rowHeight: 34 };
clusterSheet.getRangeByIndexes(1, 0, citationClusters.length, clusterHeaders.length).format = { font: { name: "Aptos", size: 9 }, verticalAlignment: "top", wrapText: true, rowHeight: 36 };
clusterSheet.freezePanes.freezeRows(1);
clusterSheet.tables.add(`A1:G${clusterMatrix.length}`, true, "CitationClusters");
for (const [index, width] of [22, 9, 45, 12, 14, 60, 60].entries()) clusterSheet.getRangeByIndexes(0, index, clusterMatrix.length, 1).format.columnWidth = width;

await fs.mkdir(previewDir, { recursive: true });
for (const [sheetName, range, fileName] of [
  ["README", "A1:F13", "citation_crosswalk_readme.png"],
  ["Citation Crosswalk", "A1:J12", "citation_crosswalk_sample.png"],
  ["Modality Summary", `A1:D${modalityMatrix.length}`, "citation_crosswalk_modality.png"],
  ["Citation Clusters", `A1:G${Math.min(clusterMatrix.length, 14)}`, "citation_clusters_sample.png"],
]) {
  const rendered = await workbook.render({ sheetName, range, scale: 1.5, format: "png" });
  await fs.writeFile(path.join(previewDir, fileName), new Uint8Array(await rendered.arrayBuffer()));
}
const errors = await workbook.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, summary: "citation crosswalk formula-error scan" });
const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(xlsxOut);
const persisted = await SpreadsheetFile.importXlsx(await FileBlob.load(xlsxOut));
const persistedRows = await persisted.inspect({ kind: "table", range: "Citation Crosswalk!A1:J8", include: "values,formulas", tableMaxRows: 8, tableMaxCols: 10 });
const persistedLast = await persisted.inspect({ kind: "table", range: "Citation Crosswalk!A203:J207", include: "values,formulas", tableMaxRows: 5, tableMaxCols: 10 });
const persistedErrors = await persisted.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, summary: "persisted citation crosswalk formula-error scan" });
qa.workbook = {
  output: xlsxOut,
  previews: 4,
  initial_error_scan: errors.ndjson,
  persisted_first_rows: persistedRows.ndjson,
  persisted_last_rows: persistedLast.ndjson,
  persisted_error_scan: persistedErrors.ndjson,
};
await fs.writeFile(jsonOut, `${JSON.stringify(qa, null, 2)}\n`, "utf8");

process.stdout.write(`${JSON.stringify({ status, cited: cited.length, missing: missing.length, citationUses, csvOut, xlsxOut }, null, 2)}\n`);
