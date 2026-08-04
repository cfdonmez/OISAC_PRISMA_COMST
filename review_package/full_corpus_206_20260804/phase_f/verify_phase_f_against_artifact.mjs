import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const HERE = path.dirname(fileURLToPath(import.meta.url));
function requiredInput(envName) {
  const value = String(process.env[envName] ?? "").trim();
  if (!value) throw new Error(`Set ${envName} to the required source artifact path.`);
  return path.resolve(value);
}
const SOURCE = requiredInput("OISAC_PHASE_D_WORKBOOK");
const CROSSWALK = requiredInput("OISAC_PHASE_E_CROSSWALK");
const EXPECTED_SOURCE_SHA = "c1b3b89789c6ed3e20da5a6283e480875c1913e21af88ff59ac747a6aa949348";
const EXPECTED_CROSSWALK_SHA = "41d6f8f574bdd0d6eba04806b2930ade8fa1d3d56e28b083de3d56bb13e7d122";
const OUT = path.join(HERE, "phase_f_artifact_independent_QA_2026-08-04.json");

function clean(value) {
  return value === null || value === undefined ? "" : String(value).replace(/^\uFEFF/, "").trim();
}

function sha256(filePath) {
  return crypto.createHash("sha256").update(fs.readFileSync(filePath)).digest("hex");
}

function readSheet(workbook, name) {
  const sheet = workbook.worksheets.getItem(name);
  const values = sheet.getUsedRange()?.values ?? [];
  if (!values.length) throw new Error(`Empty worksheet: ${name}`);
  const headers = values[0].map(clean);
  return values.slice(1).map((cells) => Object.fromEntries(headers.map((header, index) => [header, cells[index]])));
}

function parseCsv(text) {
  const rows = [];
  let row = [];
  let field = "";
  let quoted = false;
  for (let i = 0; i < text.length; i += 1) {
    const char = text[i];
    if (quoted) {
      if (char === '"' && text[i + 1] === '"') {
        field += '"';
        i += 1;
      } else if (char === '"') {
        quoted = false;
      } else {
        field += char;
      }
    } else if (char === '"') {
      quoted = true;
    } else if (char === ",") {
      row.push(field);
      field = "";
    } else if (char === "\n") {
      row.push(field.replace(/\r$/, ""));
      rows.push(row);
      row = [];
      field = "";
    } else {
      field += char;
    }
  }
  if (field.length || row.length) {
    row.push(field.replace(/\r$/, ""));
    rows.push(row);
  }
  const nonempty = rows.filter((cells) => cells.some((cell) => cell !== ""));
  const headers = nonempty[0].map(clean);
  return nonempty.slice(1).map((cells) => Object.fromEntries(headers.map((header, index) => [header, cells[index] ?? ""])));
}

function readCsv(name) {
  return parseCsv(fs.readFileSync(path.join(HERE, name), "utf8"));
}

function countBy(rows, key) {
  const counts = {};
  for (const row of rows) {
    const value = clean(row[key]);
    counts[value] = (counts[value] ?? 0) + 1;
  }
  return counts;
}

function nestedCount(rows, first, second) {
  const output = {};
  for (const row of rows) {
    const a = clean(row[first]);
    const b = clean(row[second]);
    output[a] ??= {};
    output[a][b] = (output[a][b] ?? 0) + 1;
  }
  return output;
}

function categoryCounts(rows) {
  return Object.fromEntries(rows.map((row) => [clean(row.category), Number(row.study_count)]));
}

function canonicalize(value) {
  if (Array.isArray(value)) return value.map(canonicalize);
  if (value && typeof value === "object") {
    return Object.fromEntries(Object.keys(value).sort().map((key) => [key, canonicalize(value[key])]));
  }
  return value;
}

function sameJson(a, b) {
  return JSON.stringify(canonicalize(a)) === JSON.stringify(canonicalize(b));
}

const sourceShaBefore = sha256(SOURCE);
const crosswalkSha = sha256(CROSSWALK);
const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(SOURCE));
const master = readSheet(workbook, "01_STUDY_MASTER");
const evidence = readSheet(workbook, "03_EVIDENCE_ITEMS");
const metrics = readSheet(workbook, "04_METRIC_RESULTS");
const tradeoffs = readSheet(workbook, "05_TRADEOFF_EVIDENCE");
const ledger = readSheet(workbook, "22_SURVEY_CLAIM_LEDGER");
const surveyUse = readSheet(workbook, "24_STUDY_SURVEY_USE");
const crosswalk = JSON.parse(fs.readFileSync(CROSSWALK, "utf8"));
const phaseFQa = JSON.parse(fs.readFileSync(path.join(HERE, "QA_REPORT.json"), "utf8"));

const expectedCrossTab = {
  evidence: { eligible_qualitative: 3020, quarantined_conflict: 21 },
  metric: { context_only: 31, eligible_quantitative: 4779, quarantined_conflict: 51 },
  tradeoff: { eligible_qualitative: 186, eligible_quantitative: 218 },
};
const actualCrossTab = nestedCount(ledger, "record_type", "survey_use_class");

const modality = categoryCounts(readCsv("s1_modality.csv"));
const maturity = categoryCounts(readCsv("s5_validation_maturity.csv"));
const openData = categoryCounts(readCsv("s5_open_data.csv"));
const openCode = categoryCounts(readCsv("s5_open_code.csv"));
const sixG = categoryCounts(readCsv("s7_six_g_relevance.csv"));
const integration = categoryCounts(readCsv("s2_integration_mechanisms.csv"));
const technologies = categoryCounts(readCsv("s6_enabling_technologies.csv"));
const applications = categoryCounts(readCsv("s6_application_domains.csv"));
const metricDomains = readCsv("s3_metric_domains.csv");
const metricFamilies = readCsv("s3_metric_families.csv");
const tradeoffFamilies = readCsv("s4_tradeoff_families.csv");
const claimUses = Object.fromEntries(readCsv("claim_use_counts.csv").map((row) => [row.survey_use_class, Number(row.claim_count)]));

const expectedModality = { photonic_THz: 69, fiber: 56, VLC_LiFi: 38, FSO: 31, hybrid_optical: 9, other_optical: 3 };
const expectedMaturity = { "2": 32, "3": 18, "4": 78, "5": 66, "6": 12 };
const expectedOpenData = { unavailable_or_NR: 145, on_request: 41, open: 13, NA: 7 };
const expectedOpenCode = { unavailable_or_NR: 197, on_request: 7, partial_components: 1, NA: 1 };
const expectedSixG = { direct: 138, inferred: 64, weak: 1, not_applicable: 3 };

const manifestChecks = Object.fromEntries(Object.entries(phaseFQa.output_manifest_sha256).map(([name, expected]) => [name, fs.existsSync(path.join(HERE, name)) && sha256(path.join(HERE, name)) === expected]));
const phaseFChecksAllTrue = Object.values(phaseFQa.checks).every(Boolean);
const summaryText = fs.readFileSync(path.join(HERE, "PHASE_F_S1_S7_PUBLICATION_SUMMARY.md"), "utf8");

const checks = {
  source_sha_matches_locked_value: sourceShaBefore === EXPECTED_SOURCE_SHA,
  crosswalk_sha_matches_locked_value: crosswalkSha === EXPECTED_CROSSWALK_SHA,
  artifact_import_master_206: master.length === 206,
  artifact_import_study_ids_unique: new Set(master.map((row) => clean(row.study_cluster_id))).size === 206,
  artifact_import_evidence_3041: evidence.length === 3041,
  artifact_import_metrics_4861: metrics.length === 4861,
  artifact_import_tradeoffs_404: tradeoffs.length === 404,
  artifact_import_ledger_8306: ledger.length === 8306,
  artifact_import_survey_use_206: surveyUse.length === 206,
  artifact_ledger_crosstab_exact: sameJson(actualCrossTab, expectedCrossTab),
  claim_use_totals_exact: sameJson(claimUses, { eligible_quantitative: 4997, eligible_qualitative: 3206, context_only: 31, quarantined_conflict: 72 }),
  primary_claim_components_8203: actualCrossTab.evidence.eligible_qualitative + actualCrossTab.metric.eligible_quantitative + actualCrossTab.tradeoff.eligible_qualitative + actualCrossTab.tradeoff.eligible_quantitative === 8203,
  crosswalk_206_unique: crosswalk.per_study_crosswalk.length === 206 && new Set(crosswalk.per_study_crosswalk.map((row) => clean(row.study_cluster_id))).size === 206,
  modality_exact_and_sums_206: sameJson(modality, expectedModality) && Object.values(modality).reduce((a, b) => a + b, 0) === 206,
  maturity_exact_and_sums_206: sameJson(maturity, expectedMaturity) && Object.values(maturity).reduce((a, b) => a + b, 0) === 206,
  open_data_exact_and_sums_206: sameJson(openData, expectedOpenData) && Object.values(openData).reduce((a, b) => a + b, 0) === 206,
  open_code_exact_and_sums_206: sameJson(openCode, expectedOpenCode) && Object.values(openCode).reduce((a, b) => a + b, 0) === 206,
  six_g_exact_and_sums_206: sameJson(sixG, expectedSixG) && Object.values(sixG).reduce((a, b) => a + b, 0) === 206,
  fallback_counts_exact: integration.other === 0 && technologies.other === 19 && applications.other === 15,
  metric_domains_reconcile_4779: metricDomains.reduce((sum, row) => sum + Number(row.claim_count), 0) === 4779,
  metric_families_reconcile_4779: metricFamilies.reduce((sum, row) => sum + Number(row.claim_count), 0) === 4779,
  metric_context_only_columns_zero: metricDomains.every((row) => Number(row.context_only_claim_count) === 0) && metricFamilies.every((row) => Number(row.context_only_claim_count) === 0),
  tradeoff_families_reconcile_404: tradeoffFamilies.reduce((sum, row) => sum + Number(row.claim_count), 0) === 404,
  phase_f_declares_pass: phaseFQa.status === "PASS",
  phase_f_internal_checks_all_true: phaseFChecksAllTrue,
  phase_f_manifest_hashes_all_match: Object.values(manifestChecks).every(Boolean),
  summary_uses_primary_8203: /Primary synthesis therefore uses 8,203 claims/.test(summaryText),
  summary_marks_8234_inclusive_with_context: /8,234 non-quarantined records, but this includes 31 context-only metrics/.test(summaryText),
  source_sha_unchanged_after_artifact_import: sha256(SOURCE) === sourceShaBefore,
};

const report = {
  report_id: "PHASE_F_ARTIFACT_INDEPENDENT_QA_2026-08-04",
  generated_at: new Date().toISOString(),
  source_workbook: SOURCE,
  source_sha256: sourceShaBefore,
  crosswalk_sha256: crosswalkSha,
  counts: {
    studies: master.length,
    evidence: evidence.length,
    metrics: metrics.length,
    tradeoffs: tradeoffs.length,
    claims: ledger.length,
    primary_synthesis_claims: 8203,
    context_only: 31,
    quarantined: 72,
  },
  artifact_ledger_crosstab: actualCrossTab,
  output_manifest_checks: manifestChecks,
  checks,
  pass: Object.values(checks).every(Boolean),
};

fs.writeFileSync(OUT, `${JSON.stringify(report, null, 2)}\n`, "utf8");
if (!report.pass) {
  console.error(JSON.stringify(report, null, 2));
  process.exit(1);
}
console.log(JSON.stringify({ pass: true, checks: Object.keys(checks).length, output: OUT }, null, 2));
