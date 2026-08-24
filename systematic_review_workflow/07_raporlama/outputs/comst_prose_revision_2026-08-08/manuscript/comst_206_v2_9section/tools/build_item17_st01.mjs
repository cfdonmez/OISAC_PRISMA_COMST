import fs from "node:fs/promises";
import path from "node:path";

const manuscriptDir = path.resolve(path.dirname(new URL(import.meta.url).pathname.replace(/^\/(.:)/, "$1")), "..");
const projectRoot = path.resolve(manuscriptDir, "..", "..", "..", "..", "..", "..");
const publicDataDir = path.join(projectRoot, "systematic_review_workflow", "07_raporlama", "outputs",
  "public_release_v1_0_0_staging_2026-08-07", "OISAC_PRISMA_206_v1.0.0_DRAFT", "data");
const dedupPath = path.join(projectRoot, "systematic_review_workflow", "03_secim", "deduplication",
  "final_2026-06-22", "deduplicated_records_for_title_abstract_screening_APPROVED_2026-06-22.csv");
const categoryMapPath = path.join(manuscriptDir, "qa", "study_category_citation_map_206.csv");
const includedStudiesPath = path.join(publicDataDir, "included_studies_206_public.csv");
const reportLineagePath = path.join(publicDataDir, "report_lineage_232_public.csv");
const primaryBibliographyPath = path.join(manuscriptDir, "references_206_candidate.bib");
const companionBibliographyPath = path.join(manuscriptDir, "references_companion_21_candidate.bib");
const supplementDir = path.join(manuscriptDir, "supplements", "st01");
const evidenceDir = path.join(manuscriptDir, "supplements", "evidence");
const evidencePath = path.join(evidenceDir, "ST-19_PRIMARY_EVIDENCE_RESULTS_3020.csv");
const metricPath = path.join(evidenceDir, "ST-19_PRIMARY_METRIC_RESULTS_4779.csv");
const tradeoffPath = path.join(evidenceDir, "ST-19_GOVERNED_TRADEOFFS_404.csv");
const supplementDriverPath = path.join(supplementDir, "ST01_SUPPLEMENT_DRIVER.tex");
const mainTexPath = path.join(manuscriptDir, "main.tex");
const qaDir = path.join(manuscriptDir, "qa");
const specialPendingSources = new Set(["SCR-00083", "SCR-00553"]);

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
  const headers = rows.shift().map((header) => header.replace(/^\uFEFF/, ""));
  return rows.filter((values) => values.some((value) => value !== ""))
    .map((values) => Object.fromEntries(headers.map((header, index) => [header, values[index] || ""])));
}

function csvEscape(value) {
  const text = String(value == null ? "" : value);
  return /[",\r\n]/.test(text) ? '"' + text.replaceAll('"', '""') + '"' : text;
}

function serializeCsv(rows) {
  if (!rows.length) throw new Error("Cannot serialize an empty governed table");
  const columns = Object.keys(rows[0]);
  return [columns.map(csvEscape).join(","),
    ...rows.map((row) => columns.map((column) => csvEscape(row[column])).join(","))]
    .join("\r\n") + "\r\n";
}

function texEscape(value) {
  return String(value == null ? "" : value)
    .replaceAll("µ", "XTEXMICROX").replaceAll("μ", "XTEXMICROX")
    .replaceAll("ϕ", "XTEXPHIX").replaceAll("φ", "XTEXPHIX")
    .replaceAll("λ", "XTEXLAMBDAX").replaceAll("–", "--").replaceAll("—", "---")
    .replaceAll("\\", "\\textbackslash{}").replaceAll("&", "\\&")
    .replaceAll("%", "\\%").replaceAll("#", "\\#").replaceAll("_", "\\_")
    .replaceAll("$", "\\$").replaceAll("{", "\\{").replaceAll("}", "\\}")
    .replaceAll("~", "\\textasciitilde{}").replaceAll("^", "\\textasciicircum{}")
    .replaceAll("XTEXMICROX", "\\ensuremath{\\mu}")
    .replaceAll("XTEXPHIX", "\\ensuremath{\\phi}")
    .replaceAll("XTEXLAMBDAX", "\\ensuremath{\\lambda}");
}

function texTableEscape(value) {
  return texEscape(value).replaceAll("\\_", "\\_\\allowbreak{}").replaceAll("-", "-\\allowbreak{}");
}

function stripNonLatinSubtitle(value) {
  return String(value == null ? "" : value)
    .replace(/;\s*\[[^\]]*[\u3400-\u9fff][^\]]*\]\s*$/gu, "")
    .replace(/\[[^\]]*[\u3400-\u9fff][^\]]*\]/gu, "").trim();
}

function bibEscape(value) {
  return stripNonLatinSubtitle(value)
    .replaceAll("µ", "{$\\mu$}").replaceAll("μ", "{$\\mu$}")
    .replaceAll("ϕ", "{$\\phi$}").replaceAll("φ", "{$\\phi$}")
    .replaceAll("λ", "{$\\lambda$}").replaceAll("&", "\\&")
    .replaceAll("%", "\\%").replaceAll("#", "\\#").replaceAll("_", "\\_");
}

function authorLabel(authors) {
  const parts = String(authors || "").split(/\s*;\s*/).filter(Boolean);
  if (!parts.length) return "NR";
  const tokens = parts[0].trim().split(/\s+/);
  const firstLooksLikeInitial = /^(?:[A-Z]\.?|[A-Z]\.-[A-Z]\.?)$/i.test(tokens[0]);
  const surname = (firstLooksLikeInitial ? tokens.at(-1) : tokens[0]).replace(/[.,]$/, "");
  return parts.length === 1 ? surname : surname + " et al.";
}

function normalizeDoi(value) {
  return String(value || "").trim().toLowerCase()
    .replace(/^https?:\/\/(?:dx\.)?doi\.org\//, "").replace(/^doi:\s*/, "")
    .replace(/[\s.,;]+$/, "");
}

function normalizeTitle(value) {
  return stripNonLatinSubtitle(value).replace(/[{}]/g, "").replace(/\\ensuremath/g, "")
    .replace(/\\(?:mu|phi|lambda)/g, "").replace(/\\&/g, "&").replace(/\\_/g, "_")
    .toLowerCase().replace(/[^a-z0-9]+/g, " ").trim();
}

function normalizeText(value) {
  return String(value || "").toLowerCase().replace(/[^a-z0-9]+/g, " ").trim();
}

function parseBibEntries(source) {
  const entries = [];
  let cursor = 0;
  while (cursor < source.length) {
    const at = source.indexOf("@", cursor);
    if (at < 0) break;
    const open = source.indexOf("{", at);
    if (open < 0) break;
    let depth = 0;
    let end = open;
    for (; end < source.length; end += 1) {
      if (source[end] === "{") depth += 1;
      if (source[end] === "}") {
        depth -= 1;
        if (depth === 0) {
          end += 1;
          break;
        }
      }
    }
    const raw = source.slice(at, end);
    const header = raw.match(/^@([^\s{]+)\s*\{\s*([^,\s]+)\s*,/i);
    if (header) {
      const field = (name) => {
        const match = new RegExp("\\b" + name + "\\s*=\\s*\\{", "i").exec(raw);
        if (!match) return "";
        const start = match.index + match[0].length;
        let fieldDepth = 1;
        let fieldEnd = start;
        for (; fieldEnd < raw.length; fieldEnd += 1) {
          if (raw[fieldEnd] === "{") fieldDepth += 1;
          if (raw[fieldEnd] === "}") {
            fieldDepth -= 1;
            if (fieldDepth === 0) break;
          }
        }
        return raw.slice(start, fieldEnd).replace(/\s+/g, " ").trim();
      };
      entries.push({ type: header[1].toLowerCase(), key: header[2], author: field("author"),
        title: field("title"), year: field("year"), venue: field("journal") || field("booktitle"),
        doi: normalizeDoi(field("doi")), url: field("url"), raw });
    }
    cursor = Math.max(end, at + 1);
  }
  return entries;
}

function pipeOrNr(value) {
  const text = String(value || "").trim();
  return text ? text.replaceAll("|", "; ") : "NR";
}

function groupBy(rows, field) {
  const grouped = new Map();
  for (const row of rows) {
    const key = row[field];
    const current = grouped.get(key) || [];
    current.push(row);
    grouped.set(key, current);
  }
  return grouped;
}

function duplicateValues(values) {
  return [...new Set(values.filter((value, index) => values.indexOf(value) !== index))];
}

function reportCitationKey(report, mapped) {
  if (report.evidence_use_role === "primary_source") return mapped.candidate_bib_key;
  return "OISAC_" + String(report.screening_record_id).replace(/[^A-Za-z0-9]/g, "");
}

function stableSourceUrl(report, dedup) {
  const doi = normalizeDoi(report.doi);
  if (doi) return "https://doi.org/" + doi;
  const raw = String((dedup && dedup.url) || "").trim();
  const ieee = raw.match(/[?&]arnumber=(\d+)/i);
  if (ieee) return "https://ieeexplore.ieee.org/document/" + ieee[1];
  return raw;
}

function hasPendingHumanToken(row) {
  return [row.qa_flag, row.independent_human_status, row.adjudication_status, row.verification_status]
    .some((value) => /pending_human/i.test(String(value || "")));
}

function resolvedOrApproved(row) {
  return /resolved|approved/i.test(String(row.adjudication_status || "")) ||
    /human_reviewed_approved/i.test(String(row.qa_flag || ""));
}

function pendingHuman(row) {
  return hasPendingHumanToken(row) && !resolvedOrApproved(row);
}

function recordLocator(row) {
  const parts = [];
  if (row.pdf_page) parts.push("PDF p. " + row.pdf_page);
  if (row.section_heading) parts.push(row.section_heading);
  if (row.table_id) parts.push(row.table_id);
  if (row.figure_id) parts.push(row.figure_id);
  if (row.equation_id) parts.push(row.equation_id);
  return parts.length ? parts.join("; ") : "locator not reported";
}

function bibAuthorList(authors, screeningRecordId) {
  const overrides = new Map([
    ["SCR-01184", "Qihang Wang; Wen Zhou; Jie Zhang; Jingtao Ge; Sicong Xu; Siqi Wang; Xin Lu; Jiali Chen; Chengzhen Bian; Xiongwei Yang; Weiping Li; Kaihui Wang; Jianjun Yu"],
  ]);
  const source = overrides.get(screeningRecordId) || String(authors || "");
  return source.split(/\s*;\s*/).filter(Boolean).map((author) => {
    const tokens = author.trim().split(/\s+/);
    if (tokens.length < 2) return author.trim();
    const first = tokens[0];
    const last = tokens.at(-1);
    const firstLooksLikeInitials = /^[A-Z.\-]+$/.test(first);
    const lastLooksLikeInitials = /^[A-Z.\-]+$/.test(last);
    if (!firstLooksLikeInitials && lastLooksLikeInitials) {
      return tokens.slice(0, -1).join(" ") + ", " + last;
    }
    return author.trim();
  }).join(" and ");
}

function makeCompanionBibEntry(report) {
  const conference = /conference|proceeding/i.test((report.document_type || "") + " " + (report.venue || ""));
  const fields = [];
  fields.push("  author = {" + bibEscape(bibAuthorList(report.authors, report.screening_record_id)) + "}");
  fields.push("  title = {{" + bibEscape(report.title) + "}}");
  fields.push("  " + (conference ? "booktitle" : "journal") + " = {" + bibEscape(report.venue || "Venue not reported") + "}");
  fields.push("  year = {" + bibEscape(report.year || "n.d.") + "}");
  if (report.doi) fields.push("  doi = {" + normalizeDoi(report.doi) + "}");
  fields.push("  url = {" + report.source_url + "}");
  fields.push("  note = {Eligible companion report in the governed 206-study/227-report O-ISAC evidence base}");
  return "@" + (conference ? "inproceedings" : "article") + "{" + report.report_citation_key + ",\n" +
    fields.join(",\n") + "\n}";
}

const sources = await Promise.all([
  fs.readFile(categoryMapPath, "utf8"), fs.readFile(includedStudiesPath, "utf8"),
  fs.readFile(reportLineagePath, "utf8"), fs.readFile(primaryBibliographyPath, "utf8"),
  fs.readFile(dedupPath, "utf8"), fs.readFile(evidencePath, "utf8"),
  fs.readFile(metricPath, "utf8"), fs.readFile(tradeoffPath, "utf8"),
  fs.readFile(supplementDriverPath, "utf8"), fs.readFile(mainTexPath, "utf8"),
]);
const [mapSource, studySource, lineageSource, primaryBibSource, dedupSource,
  evidenceSource, metricSource, tradeoffSource, supplementDriverSource, mainTexSource] = sources;
const mapRows = parseCsv(mapSource);
const studyRows = parseCsv(studySource);
const lineageRows = parseCsv(lineageSource);
const dedupRows = parseCsv(dedupSource);
const evidenceRows = parseCsv(evidenceSource);
const metricRows = parseCsv(metricSource);
const tradeoffRows = parseCsv(tradeoffSource);
const primaryBibEntries = parseBibEntries(primaryBibSource);
const mapByStudy = new Map(mapRows.map((row) => [row.study_cluster_id, row]));
const dedupByScreening = new Map(dedupRows.map((row) => [row.screening_record_id, row]));
const evidenceBySource = groupBy(evidenceRows, "source_screening_record_id");
const metricsBySource = groupBy(metricRows, "source_screening_record_id");
const tradeoffsBySource = groupBy(tradeoffRows, "source_screening_record_id");
const eligibleReports = lineageRows.filter((row) =>
  ["primary_source", "supplementary_source"].includes(row.evidence_use_role) &&
  String(row.final_decision).startsWith("include"));
const eligibleScreeningIds = new Set(eligibleReports.map((row) => row.screening_record_id));
const reportStudyBySource = new Map(eligibleReports.map((row) => [row.screening_record_id, row.study_cluster_id]));

const reportRows = eligibleReports.map((report) => {
  const mapped = mapByStudy.get(report.study_cluster_id);
  if (!mapped) throw new Error("No study citation map row for report " + report.report_id);
  const evidence = evidenceBySource.get(report.screening_record_id) || [];
  const metrics = metricsBySource.get(report.screening_record_id) || [];
  const tradeoffs = tradeoffsBySource.get(report.screening_record_id) || [];
  const guardrails = metrics.filter((row) => row.final_claim_status === "supported_with_source_specific_guardrail");
  const pendingTokenRows = [...evidence, ...metrics, ...tradeoffs].filter(hasPendingHumanToken);
  const pendingRows = [...evidence, ...metrics].filter(pendingHuman);
  const specialPendingCount = specialPendingSources.has(report.screening_record_id) ? pendingRows.length : 0;
  let gate = "eligible_with_study_context";
  if (specialPendingCount) gate = "blocked_pending_human";
  else if (guardrails.length) gate = "report_specific_guardrail";
  const sourceUrl = stableSourceUrl(report, dedupByScreening.get(report.screening_record_id));
  return {
    study_id: report.study_cluster_id,
    study_citation_key: mapped.candidate_bib_key,
    report_id: report.report_id,
    screening_record_id: report.screening_record_id,
    report_citation_key: reportCitationKey(report, mapped),
    report_citation_command: "",
    report_evidence_role: report.evidence_use_role,
    report_relation_code: report.final_relation_code,
    report_role: report.final_report_role,
    title: report.title,
    authors: report.authors,
    year: report.year,
    venue: report.venue,
    doi: normalizeDoi(report.doi),
    source_url: sourceUrl,
    document_type: report.document_type,
    extracted_evidence_row_count: evidence.length,
    extracted_metric_row_count: metrics.length,
    governed_tradeoff_row_count: tradeoffs.length,
    report_specific_guardrail_metric_count: guardrails.length,
    pending_human_token_count_all_statuses: pendingTokenRows.length,
    pending_human_token_resolved_or_approved_count: pendingTokenRows.filter(resolvedOrApproved).length,
    unresolved_pending_human_row_count: pendingRows.length,
    unresolved_pending_human_row_count_companion_lineage_gate: specialPendingCount,
    synthesis_use_gate: gate,
    provenance_status: evidence.length && sourceUrl ? "complete" : "incomplete",
    provenance_note: "Source " + report.screening_record_id + " supplies " + evidence.length +
      " evidence, " + metrics.length + " metric, and " + tradeoffs.length +
      " governed tradeoff rows; use gate: " + gate + ".",
  };
}).sort((a, b) => a.study_id.localeCompare(b.study_id) ||
  (a.report_evidence_role === b.report_evidence_role ? 0 : a.report_evidence_role === "primary_source" ? -1 : 1) ||
  a.report_id.localeCompare(b.report_id));
for (const report of reportRows) report.report_citation_command = "\\cite{" + report.report_citation_key + "}";

const reportBySource = new Map(reportRows.map((row) => [row.screening_record_id, row]));
const reportKeys = reportRows.map((row) => row.report_citation_key);
const companionRows = reportRows.filter((row) => row.report_evidence_role === "supplementary_source");
const companionBibText = companionRows.map(makeCompanionBibEntry).join("\n\n") + "\n";
const combinedBibText = primaryBibSource.trimEnd() + "\n\n" + companionBibText;
const combinedBibEntries = parseBibEntries(combinedBibText);
const combinedBibByKey = new Map(combinedBibEntries.map((entry) => [entry.key, entry]));
const primaryBibKeys = new Set(primaryBibEntries.map((entry) => entry.key));

const st01Rows = studyRows.map((study) => {
  const mapped = mapByStudy.get(study.study_cluster_id);
  if (!mapped) throw new Error("No citation map row for " + study.study_cluster_id);
  const reports = reportRows.filter((row) => row.study_id === study.study_cluster_id);
  const primaryReports = reports.filter((row) => row.report_evidence_role === "primary_source");
  if (primaryReports.length !== 1) {
    throw new Error(study.study_cluster_id + " has " + primaryReports.length + " primary eligible reports");
  }
  if (String(mapped.primary_extraction_screening_record_id) !== String(primaryReports[0].screening_record_id)) {
    throw new Error(study.study_cluster_id + " primary-report join mismatch");
  }
  if (Number(study.eligible_report_count) !== reports.length) {
    throw new Error(study.study_cluster_id + " eligible-report count mismatch");
  }
  const keys = reports.map((row) => row.report_citation_key);
  const companions = reports.filter((row) => row.report_evidence_role === "supplementary_source");
  const blocked = reports.filter((row) => row.synthesis_use_gate === "blocked_pending_human");
  return {
    study_id: study.study_cluster_id,
    primary_screening_record_id: primaryReports[0].screening_record_id,
    citation_key: mapped.candidate_bib_key,
    primary_report_citation_key: primaryReports[0].report_citation_key,
    companion_report_citation_keys: companions.map((row) => row.report_citation_key).join("; "),
    eligible_report_citation_keys: keys.join("; "),
    citation_command: "\\cite{" + keys.join(",") + "}",
    author_year: authorLabel(study.authors) + " (" + (study.year || "NR") + ")",
    title: study.title,
    year: study.year,
    venue: study.venue,
    doi: study.doi,
    primary_report_id: primaryReports[0].report_id,
    eligible_report_count: reports.length,
    companion_eligible_report_count: companions.length,
    eligible_report_ids: reports.map((row) => row.report_id).join("; "),
    report_citation_count: keys.length,
    extracted_evidence_row_count: reports.reduce((sum, row) => sum + Number(row.extracted_evidence_row_count), 0),
    extracted_metric_row_count: reports.reduce((sum, row) => sum + Number(row.extracted_metric_row_count), 0),
    governed_tradeoff_row_count: reports.reduce((sum, row) => sum + Number(row.governed_tradeoff_row_count), 0),
    report_specific_guardrail_metric_count: reports.reduce((sum, row) => sum + Number(row.report_specific_guardrail_metric_count), 0),
    pending_human_blocked_report_ids: blocked.map((row) => row.report_id).join("; "),
    synthesis_use_gate: blocked.length ? "blocked_pending_human_report_rows" : "governed_eligible",
    modality: mapped.canonical_modality || study.primary_optical_modality_code || "NR",
    integration_mechanisms: pipeOrNr(mapped.canonical_integration_mechanisms || study.integration_mechanism_codes),
    communication_functions: pipeOrNr(study.communication_functions),
    sensing_tasks: pipeOrNr(study.sensing_tasks),
    validation_maturity_max: mapped.validation_maturity_max || "NR",
    validation_types: pipeOrNr(mapped.canonical_validation_types || study.validation_type_codes),
    application_domains: pipeOrNr(mapped.canonical_application_domains || study.application_domain_codes),
    six_g_relevance: mapped.canonical_six_g_relevance || study.six_g_relevance_code || "NR",
  };
}).sort((a, b) => a.study_id.localeCompare(b.study_id));

const companionProvenanceRows = companionRows.map((report) => {
  const evidence = evidenceBySource.get(report.screening_record_id) || [];
  const metrics = metricsBySource.get(report.screening_record_id) || [];
  const tradeoffs = tradeoffsBySource.get(report.screening_record_id) || [];
  const sourceHashes = [...new Set([...evidence, ...metrics, ...tradeoffs]
    .map((row) => row.source_workbook_sha256).filter(Boolean))];
  return {
    study_id: report.study_id,
    study_primary_citation_key: report.study_citation_key,
    companion_report_id: report.report_id,
    companion_screening_record_id: report.screening_record_id,
    companion_report_citation_key: report.report_citation_key,
    companion_report_citation_command: report.report_citation_command,
    relation_code: report.report_relation_code,
    report_role: report.report_role,
    title: report.title,
    year: report.year,
    venue: report.venue,
    doi: report.doi,
    source_url: report.source_url,
    extracted_evidence_row_count: evidence.length,
    evidence_record_ids: evidence.map((row) => row.evidence_id).join("; "),
    extracted_metric_row_count: metrics.length,
    metric_record_ids: metrics.map((row) => row.metric_record_id).join("; "),
    governed_tradeoff_row_count: tradeoffs.length,
    tradeoff_record_ids: tradeoffs.map((row) => row.tradeoff_id).join("; "),
    report_specific_guardrail_metric_count: report.report_specific_guardrail_metric_count,
    pending_human_token_count: report.pending_human_token_count_all_statuses,
    pending_human_token_resolved_or_approved_count: report.pending_human_token_resolved_or_approved_count,
    unresolved_pending_human_row_count: report.unresolved_pending_human_row_count_companion_lineage_gate,
    synthesis_use_gate: report.synthesis_use_gate,
    source_workbook_sha256: sourceHashes.join("; "),
    exact_provenance_statement: report.provenance_note,
  };
});

const guardrailRows = companionRows.flatMap((report) =>
  (metricsBySource.get(report.screening_record_id) || [])
    .filter((metric) => metric.final_claim_status === "supported_with_source_specific_guardrail")
    .map((metric) => ({
      study_id: report.study_id,
      companion_report_id: report.report_id,
      companion_screening_record_id: report.screening_record_id,
      companion_report_citation_key: report.report_citation_key,
      metric_record_id: metric.metric_record_id,
      metric_domain: metric.metric_domain,
      metric_family_code: metric.metric_family_code,
      metric_name_reported: metric.metric_name_reported,
      value_numeric: metric.value_numeric,
      value_low: metric.value_low,
      value_high: metric.value_high,
      unit_reported: metric.unit_reported,
      condition_set_id: metric.condition_set_id,
      scenario_summary: metric.scenario_summary,
      baseline_comparator: metric.baseline_comparator,
      source_locator: recordLocator(metric),
      conflict_flag: metric.conflict_flag,
      final_claim_status: metric.final_claim_status,
      final_survey_use_class: metric.final_survey_use_class,
      final_comparison_admissibility: metric.final_comparison_admissibility,
      cross_study_quantitative_comparison_allowed: metric.cross_study_quantitative_comparison_allowed,
      final_reason_code: metric.final_reason_code,
      synthesis_use_gate: report.synthesis_use_gate === "blocked_pending_human"
        ? "blocked_pending_human" : "retain_report_specific_only",
      guardrail_instruction: "Keep this value report specific; do not merge, average, substitute, or normalize it across primary and companion reports.",
    }))
).sort((a, b) => a.companion_screening_record_id.localeCompare(b.companion_screening_record_id) ||
  String(a.metric_record_id || "").localeCompare(String(b.metric_record_id || "")));

const tableRows = st01Rows.map((row) => [
  "\\seqsplit{" + texEscape(row.study_id) + "}", row.citation_command, texEscape(row.title),
  texTableEscape(row.modality), texTableEscape(row.integration_mechanisms),
  texTableEscape(row.validation_types), texEscape(String(row.eligible_report_count)),
].join(" & ") + " \\\\");
const tablePages = [];
for (let index = 0; index < tableRows.length; index += 7) {
  const pageRows = tableRows.slice(index, index + 7);
  const first = index + 1;
  const last = index + pageRows.length;
  const heading = index === 0
    ? "Electronic Table ST-01A: Included-study inventory for the 206 unique studies"
    : "Electronic Table ST-01A (continued): studies " + first + "--" + last + " of 206";
  tablePages.push("\\vspace*{8mm}\n\\begin{center}\n\\textbf{" + heading + "}\\\\[-1mm]\n" +
    "\\small Each study row cites its primary report and every eligible companion report; companions remain within the same study.\n" +
    "\\end{center}\n" +
    "\\begin{tabularx}{\\linewidth}{@{}p{0.09\\linewidth}p{0.055\\linewidth}Yp{0.07\\linewidth}p{0.18\\linewidth}p{0.15\\linewidth}r@{}}\n" +
    "\\toprule\nStudy ID & Report citations & Title & Modality & Integration mechanisms & Validation & Reports \\\\\n" +
    "\\midrule\n" + pageRows.join("\n") + "\n\\bottomrule\n\\end{tabularx}" +
    (last < tableRows.length ? "\n\\clearpage" : ""));
}
const st01Tex = "% Auto-generated by tools/build_item17_st01.mjs. Do not edit manually.\n" +
  "% PRISMA 2020 Item 17: 206 study rows carry all 227 eligible report keys.\n" +
  tablePages.join("\n") + "\n";

const companionTexRows = companionProvenanceRows.map((row) => [
  "\\seqsplit{" + texEscape(row.study_id) + "}", row.companion_report_citation_command,
  texEscape(row.report_role),
  texEscape(row.extracted_evidence_row_count + "/" + row.extracted_metric_row_count + "/" + row.governed_tradeoff_row_count),
  texEscape(row.report_specific_guardrail_metric_count), texEscape(row.unresolved_pending_human_row_count),
  texTableEscape(row.synthesis_use_gate),
].join(" & ") + " \\\\");
const companionPages = [];
for (let index = 0; index < companionTexRows.length; index += 7) {
  const pageRows = companionTexRows.slice(index, index + 7);
  const first = index + 1;
  const last = index + pageRows.length;
  const heading = index === 0
    ? "Electronic Table ST-01B: Exact provenance of the 21 eligible companion reports"
    : "Electronic Table ST-01B (continued): companions " + first + "--" + last + " of 21";
  companionPages.push("\\vspace*{8mm}\n\\begin{center}\n\\textbf{" + heading + "}\\\\[-1mm]\n" +
    "\\small E/M/T gives extracted evidence, metric, and governed tradeoff row counts. Guard identifies report-specific metric guardrails.\n" +
    "\\end{center}\n" +
    "\\begin{tabularx}{\\linewidth}{@{}p{0.17\\linewidth}p{0.055\\linewidth}p{0.17\\linewidth}p{0.08\\linewidth}p{0.06\\linewidth}p{0.06\\linewidth}Y@{}}\n" +
    "\\toprule\nStudy ID & Citation & Companion role & E/M/T & Guard & Pending & Synthesis use gate \\\\\n" +
    "\\midrule\n" + pageRows.join("\n") + "\n\\bottomrule\n\\end{tabularx}" +
    (last < companionTexRows.length ? "\n\\clearpage" : ""));
}
const companionTex = "% Auto-generated by tools/build_item17_st01.mjs. Do not edit manually.\n" +
  companionPages.join("\n") + "\n";

const explicitIncludeLines = [];
for (let index = 0; index < reportKeys.length; index += 25) {
  explicitIncludeLines.push("\\nocite{" + reportKeys.slice(index, index + 25).join(",") + "}");
}
const explicitIncludeTex = "% Auto-generated explicit-key inclusion for controlled bibliography builds.\n" +
  "% All 227 governed eligible-report keys are enumerated; no wildcard is used.\n" +
  explicitIncludeLines.join("\n") + "\n";

const combinedBibKeys = combinedBibEntries.map((entry) => entry.key);
const companionBibEntries = parseBibEntries(companionBibText);
const missingBibKeys = reportKeys.filter((key) => !combinedBibByKey.has(key));
const metadataMismatches = reportRows.flatMap((report) => {
  const bib = combinedBibByKey.get(report.report_citation_key);
  if (!bib) return [{ report_citation_key: report.report_citation_key,
    field: "entry", expected: "present", actual: "missing" }];
  const mismatches = [];
  if (!bib.author) mismatches.push({ report_citation_key: report.report_citation_key,
    field: "author", expected: "nonblank", actual: "blank" });
  if (normalizeTitle(bib.title) !== normalizeTitle(report.title)) {
    mismatches.push({ report_citation_key: report.report_citation_key, field: "title",
      expected: normalizeTitle(report.title), actual: normalizeTitle(bib.title) });
  }
  if (String(bib.year) !== String(report.year)) {
    mismatches.push({ report_citation_key: report.report_citation_key, field: "year",
      expected: report.year, actual: bib.year });
  }
  if (!bib.venue) {
    mismatches.push({ report_citation_key: report.report_citation_key, field: "venue",
      expected: "nonblank", actual: "blank" });
  }
  if (normalizeDoi(bib.doi) !== normalizeDoi(report.doi)) {
    mismatches.push({ report_citation_key: report.report_citation_key, field: "doi",
      expected: normalizeDoi(report.doi), actual: normalizeDoi(bib.doi) });
  }
  return mismatches;
});

const primaryDois = new Set(primaryBibEntries.map((entry) => entry.doi).filter(Boolean));
const primaryTitles = new Set(primaryBibEntries.map((entry) => normalizeTitle(entry.title)));
const companionDuplicateDois = companionBibEntries.map((entry) => entry.doi)
  .filter((doi) => doi && primaryDois.has(doi));
const companionDuplicateTitles = companionBibEntries.map((entry) => normalizeTitle(entry.title))
  .filter((title) => primaryTitles.has(title));
const combinedDois = combinedBibEntries.map((entry) => entry.doi).filter(Boolean);
const combinedNormalizedTitles = combinedBibEntries.map((entry) => normalizeTitle(entry.title));
const reportIdentityTokens = reportRows.map((row) =>
  row.doi ? "doi:" + row.doi : "url:" + row.source_url.toLowerCase());
const titleCollisionGroups = [...new Set(duplicateValues(combinedNormalizedTitles))].map((title) => {
  const entries = combinedBibEntries.filter((entry) => normalizeTitle(entry.title) === title);
  const reports = entries.map((entry) => reportRows.find((row) => row.report_citation_key === entry.key));
  return {
    title,
    keys: entries.map((entry) => entry.key),
    study_ids: reports.map((report) => report && report.study_id),
    identity_tokens: reports.map((report) =>
      report && (report.doi ? "doi:" + report.doi : "url:" + report.source_url.toLowerCase())),
    authorized: reports.every(Boolean) &&
      new Set(reports.map((report) => report.study_id)).size === 1 &&
      new Set(reports.map((report) =>
        report.doi ? "doi:" + report.doi : "url:" + report.source_url.toLowerCase())).size === reports.length,
  };
});
const allEvidenceSourceIds = new Set([
  ...evidenceRows.map((row) => row.source_screening_record_id),
  ...metricRows.map((row) => row.source_screening_record_id),
  ...tradeoffRows.map((row) => row.source_screening_record_id),
]);
const orphanSourceIds = [...allEvidenceSourceIds].filter((id) => !eligibleScreeningIds.has(id));
const sourceStudyMismatches = [...evidenceRows, ...metricRows, ...tradeoffRows]
  .filter((row) => reportStudyBySource.get(row.source_screening_record_id) !== row.study_cluster_id)
  .map((row) => ({ source_screening_record_id: row.source_screening_record_id,
    source_study_id: row.study_cluster_id,
    lineage_study_id: reportStudyBySource.get(row.source_screening_record_id) || "missing" }));
const companionEvidenceCount = companionRows.reduce((sum, row) => sum + Number(row.extracted_evidence_row_count), 0);
const companionMetricCount = companionRows.reduce((sum, row) => sum + Number(row.extracted_metric_row_count), 0);
const companionTradeoffCount = companionRows.reduce((sum, row) => sum + Number(row.governed_tradeoff_row_count), 0);
const specialSourceRows = [...evidenceRows, ...metricRows, ...tradeoffRows]
  .filter((row) => specialPendingSources.has(row.source_screening_record_id));
const specialPendingTokenRows = specialSourceRows.filter(hasPendingHumanToken);
const specialResolvedPendingTokenRows = specialPendingTokenRows.filter(resolvedOrApproved);
const specialUnresolvedPendingRows = specialPendingTokenRows.filter(pendingHuman);
const specialPendingTokenCounts = Object.fromEntries([...specialPendingSources].map((source) => [
  source, specialPendingTokenRows.filter((row) => row.source_screening_record_id === source).length,
]));
const specialUnresolvedCounts = Object.fromEntries([...specialPendingSources].map((source) => [
  source, specialUnresolvedPendingRows.filter((row) => row.source_screening_record_id === source).length,
]));
const multiReportStudies = st01Rows.filter((row) => Number(row.eligible_report_count) > 1);
const studyCitationKeyUnion = new Set(st01Rows.flatMap((row) =>
  row.eligible_report_citation_keys.split(/\s*;\s*/).filter(Boolean)));
const reportCountMismatches = st01Rows.filter((row) =>
  Number(row.report_citation_count) !== Number(row.eligible_report_count));
const specialPendingReportRows = reportRows.filter((row) =>
  specialPendingSources.has(row.screening_record_id));
const noDoiRows = reportRows.filter((row) => !row.doi);
const delimitedCount = (value) => String(value || "").split(/\s*;\s*/).filter(Boolean).length;

const checks = {
  st01_rows_are_206: st01Rows.length === 206,
  unique_study_ids_are_206: new Set(st01Rows.map((row) => row.study_id)).size === 206,
  eligible_report_rows_are_227: reportRows.length === 227,
  report_ids_are_227_unique: new Set(reportRows.map((row) => row.report_id)).size === 227,
  screening_record_ids_are_227_unique: new Set(reportRows.map((row) => row.screening_record_id)).size === 227,
  report_citation_keys_are_227_unique: new Set(reportKeys).size === 227,
  primary_reports_are_206: reportRows.filter((row) => row.report_evidence_role === "primary_source").length === 206,
  companion_reports_are_21: companionRows.length === 21,
  multi_report_studies_are_19: multiReportStudies.length === 19,
  study_rows_cite_every_linked_report: reportCountMismatches.length === 0 && studyCitationKeyUnion.size === 227,
  primary_bibliography_has_206_unique_entries:
    primaryBibEntries.length === 206 && primaryBibKeys.size === 206,
  companion_bibliography_has_21_unique_entries:
    companionBibEntries.length === 21 &&
    new Set(companionBibEntries.map((entry) => entry.key)).size === 21,
  combined_bibliography_has_227_unique_entries:
    combinedBibEntries.length === 227 && new Set(combinedBibKeys).size === 227,
  every_report_key_resolves: missingBibKeys.length === 0,
  every_report_metadata_matches_bibliography: metadataMismatches.length === 0,
  all_227_reports_have_stable_url_or_doi: reportRows.every((row) => Boolean(row.source_url)),
  combined_bibliography_has_220_dois_and_7_url_fallbacks:
    combinedDois.length === 220 && noDoiRows.length === 7,
  combined_dois_are_unique: new Set(combinedDois).size === combinedDois.length,
  report_identity_tokens_are_227_unique:
    new Set(reportIdentityTokens).size === 227,
  title_only_collisions_are_authorized_same_study_distinct_reports:
    titleCollisionGroups.every((group) => group.authorized),
  companions_do_not_duplicate_primary_report_identity:
    companionDuplicateDois.length === 0,
  every_eligible_report_has_extracted_evidence:
    reportRows.every((row) => Number(row.extracted_evidence_row_count) > 0),
  evidence_sources_have_zero_orphans: orphanSourceIds.length === 0,
  evidence_sources_have_zero_study_mismatches: sourceStudyMismatches.length === 0,
  companion_exact_provenance_is_21_rows: companionProvenanceRows.length === 21,
  companion_exact_record_ids_match_all_row_counts:
    companionProvenanceRows.every((row) =>
      delimitedCount(row.evidence_record_ids) === Number(row.extracted_evidence_row_count) &&
      delimitedCount(row.metric_record_ids) === Number(row.extracted_metric_row_count) &&
      delimitedCount(row.tradeoff_record_ids) === Number(row.governed_tradeoff_row_count)),
  companion_extracted_evidence_is_95_rows: companionEvidenceCount === 95,
  companion_extracted_metrics_are_123_rows_across_20_reports:
    companionMetricCount === 123 &&
    companionRows.filter((row) => Number(row.extracted_metric_row_count) > 0).length === 20,
  companion_tradeoffs_are_9_rows_across_8_reports:
    companionTradeoffCount === 9 &&
    companionRows.filter((row) => Number(row.governed_tradeoff_row_count) > 0).length === 8,
  companion_report_specific_guardrails_are_14_metrics: guardrailRows.length === 14,
  guardrail_metric_ids_are_14_nonblank_unique:
    guardrailRows.every((row) => Boolean(row.metric_record_id)) &&
    new Set(guardrailRows.map((row) => row.metric_record_id)).size === 14,
  historical_pending_tokens_are_59_and_all_resolved_or_approved:
    specialPendingTokenRows.length === 59 &&
    specialResolvedPendingTokenRows.length === 59 &&
    specialPendingTokenCounts["SCR-00083"] === 40 &&
    specialPendingTokenCounts["SCR-00553"] === 19,
  hard_pending_gate_has_zero_unresolved_rows:
    specialUnresolvedPendingRows.length === 0 &&
    specialUnresolvedCounts["SCR-00083"] === 0 &&
    specialUnresolvedCounts["SCR-00553"] === 0,
  resolved_pending_tokens_do_not_auto_block_reports:
    specialPendingReportRows.length === 2 &&
    specialPendingReportRows.every((row) => row.synthesis_use_gate !== "blocked_pending_human"),
  report_specific_conflict_guardrails_remain_active:
    specialPendingReportRows.every((row) =>
      Number(row.report_specific_guardrail_metric_count) > 0 &&
      row.synthesis_use_gate === "report_specific_guardrail"),
  explicit_include_is_not_wildcard: !explicitIncludeTex.includes("\\nocite{*}"),
  explicit_include_contains_all_227_keys: reportKeys.every((key) => explicitIncludeTex.includes(key)),
  standalone_supplement_inputs_both_tables:
    supplementDriverSource.includes("\\input{ST01_INCLUDED_STUDIES_206.tex}") &&
    supplementDriverSource.includes("\\input{ST01_COMPANION_REPORT_PROVENANCE_21.tex}"),
  standalone_supplement_uses_227_report_bibliography:
    supplementDriverSource.includes("\\bibliography{ST01_REFERENCES_227}"),
  main_manuscript_loads_companion_carrier:
    mainTexSource.includes("references_companion_21_candidate"),
};
const failures = Object.entries(checks).filter(([, passed]) => !passed).map(([name]) => name);
const diagnostics = {
  duplicate_study_ids: duplicateValues(st01Rows.map((row) => row.study_id)),
  duplicate_report_ids: duplicateValues(reportRows.map((row) => row.report_id)),
  duplicate_screening_record_ids: duplicateValues(reportRows.map((row) => row.screening_record_id)),
  duplicate_report_citation_keys: duplicateValues(reportKeys),
  duplicate_combined_bibliography_keys: duplicateValues(combinedBibKeys),
  duplicate_combined_dois: duplicateValues(combinedDois),
  duplicate_combined_titles: duplicateValues(combinedNormalizedTitles),
  authorized_title_only_collision_groups: titleCollisionGroups.filter((group) => group.authorized),
  unauthorized_title_collision_groups: titleCollisionGroups.filter((group) => !group.authorized),
  missing_bibliography_keys: missingBibKeys,
  bibliography_metadata_mismatches: metadataMismatches,
  companion_duplicate_primary_dois: companionDuplicateDois,
  companion_duplicate_primary_titles: companionDuplicateTitles,
  evidence_orphan_source_ids: orphanSourceIds,
  evidence_source_study_mismatches: sourceStudyMismatches,
  study_report_count_mismatches: reportCountMismatches.map((row) => row.study_id),
};
const qa = {
  generated_at_utc: new Date().toISOString(),
  status: failures.length ? "FAIL" : "PASS",
  counts: {
    unique_studies: st01Rows.length,
    eligible_reports: reportRows.length,
    primary_reports: reportRows.filter((row) => row.report_evidence_role === "primary_source").length,
    companion_reports: companionRows.length,
    multi_report_studies: multiReportStudies.length,
    report_citation_keys: new Set(reportKeys).size,
    primary_bibliography_entries: primaryBibEntries.length,
    companion_bibliography_entries: companionBibEntries.length,
    combined_bibliography_entries: combinedBibEntries.length,
    doi_entries: combinedDois.length,
    url_fallback_entries: noDoiRows.length,
    companion_evidence_rows: companionEvidenceCount,
    companion_metric_rows: companionMetricCount,
    companion_tradeoff_rows: companionTradeoffCount,
    report_specific_guardrail_metrics: guardrailRows.length,
    historical_pending_human_tokens: specialPendingTokenRows.length,
    resolved_or_approved_pending_tokens: specialResolvedPendingTokenRows.length,
    unresolved_pending_human_rows: specialUnresolvedPendingRows.length,
    orphan_source_ids: orphanSourceIds.length,
  },
  checks,
  failures,
  diagnostics,
  pending_gate: {
    rule: "A pending_human token blocks synthesis only when the same row lacks a resolved or approved adjudication.",
    audited_sources: [...specialPendingSources],
    historical_token_counts: specialPendingTokenCounts,
    unresolved_counts: specialUnresolvedCounts,
    outcome: "No unresolved row remains in these two sources; report-specific conflict guardrails remain active.",
  },
  interpretation: "The review contains 206 unique studies represented by 227 eligible reports: 206 designated primary reports and 21 eligible companion reports. ST-01 retains one row per study while carrying a resolvable citation key for every report.",
};

const qaMarkdown = "# PRISMA 2020 Item 17 and companion-lineage hard-gate QA\n\n" +
  "Status: **" + qa.status + "**\n\n" +
  "## Governed units\n\n" +
  "- Unique included studies: " + qa.counts.unique_studies + "\n" +
  "- Eligible reports: " + qa.counts.eligible_reports + "\n" +
  "- Primary reports: " + qa.counts.primary_reports + "\n" +
  "- Eligible companion reports: " + qa.counts.companion_reports + "\n" +
  "- Multi-report studies: " + qa.counts.multi_report_studies + "\n" +
  "- Unique resolvable report citation keys: " + qa.counts.report_citation_keys + "\n" +
  "- Bibliography entries: " + qa.counts.combined_bibliography_entries + "\n" +
  "- Orphan evidence source IDs: " + qa.counts.orphan_source_ids + "\n\n" +
  "## Companion provenance\n\n" +
  "- Exact companion provenance rows: " + companionProvenanceRows.length + "\n" +
  "- Companion-sourced evidence rows: " + companionEvidenceCount + "\n" +
  "- Companion-sourced metric rows: " + companionMetricCount + " across 20 reports\n" +
  "- Companion-sourced governed tradeoffs: " + companionTradeoffCount + " across 8 reports\n" +
  "- Report-specific companion metric guardrails: " + guardrailRows.length + "\n\n" +
  "## Adjudication-aware pending gate\n\n" +
  "SCR-00083 retains " + specialPendingTokenCounts["SCR-00083"] +
  " historical pending-human tokens and SCR-00553 retains " +
  specialPendingTokenCounts["SCR-00553"] + ". All 59 rows record resolved or approved adjudication, so none is automatically quarantined. " +
  "The hard gate is conjunctive: a pending-human token blocks synthesis only when the row lacks resolved or approved adjudication. " +
  "Report-specific conflict guardrails remain in force.\n\n" +
  "## Citation architecture\n\n" +
  "ST-01A remains a 206-study table. Each row cites its designated primary report and every eligible companion report. " +
  "ST-01B exposes the 21 companion reports and their exact evidence, metric, tradeoff, guardrail, and adjudication provenance. " +
  "The standalone supplement resolves all 227 keys through ST01_REFERENCES_227.bib; the main manuscript loads the separate duplicate-free 21-entry companion carrier.\n";

const companionQa = {
  generated_at_utc: qa.generated_at_utc,
  status: qa.status,
  counts: {
    companion_reports: companionRows.length,
    companion_bibliography_entries: companionBibEntries.length,
    companion_evidence_rows: companionEvidenceCount,
    companion_metric_rows: companionMetricCount,
    companion_tradeoff_rows: companionTradeoffCount,
    report_specific_guardrail_metrics: guardrailRows.length,
    historical_pending_human_tokens: specialPendingTokenRows.length,
    unresolved_pending_human_rows: specialUnresolvedPendingRows.length,
    orphan_source_ids: orphanSourceIds.length,
  },
  exact_companion_reports: companionProvenanceRows.map((row) => ({
    study_id: row.study_id, report_id: row.companion_report_id,
    source: row.companion_screening_record_id,
    report_citation_key: row.companion_report_citation_key,
    evidence_rows: row.extracted_evidence_row_count,
    metric_rows: row.extracted_metric_row_count,
    tradeoff_rows: row.governed_tradeoff_row_count,
    guardrail_metrics: row.report_specific_guardrail_metric_count,
    pending_human_tokens: row.pending_human_token_count,
    unresolved_pending_human_rows: row.unresolved_pending_human_row_count,
    synthesis_use_gate: row.synthesis_use_gate,
  })),
  pending_gate: qa.pending_gate,
  failures,
};
const companionQaMarkdown = "# Companion-report provenance QA\n\n" +
  "Status: **" + companionQa.status + "**\n\n" +
  "- Companion reports: 21\n" +
  "- Duplicate-free companion BibTeX entries: 21\n" +
  "- Exact extracted provenance: 95 evidence rows, 123 metric rows, and 9 governed tradeoff rows\n" +
  "- Report-specific companion metric guardrails: 14\n" +
  "- Orphan source IDs: 0\n" +
  "- Historical pending-human tokens in SCR-00083/SCR-00553: 59; unresolved after adjudication: 0\n\n" +
  "A PASS requires all 21 companion keys to resolve without DOI/title duplication against the 206 primary entries, all evidence sources to join to the same study as the report lineage, and the adjudication-aware hard gate to preserve report-specific conflict guardrails.\n";

const readme = "# Electronic Supplement ST-01\n\n" +
  "ST-01 implements the PRISMA 2020 study/report distinction for this survey. The inclusion unit is 206 unique studies; those studies are represented by 227 eligible reports (206 primary and 21 companion reports).\n\n" +
  "## Files\n\n" +
  "- ST01_INCLUDED_STUDIES_206.csv and .tex: one row per included study; each row cites all eligible reports linked to the study.\n" +
  "- ST01_ELIGIBLE_REPORT_LINEAGE_227.csv: one row per eligible report with a unique report_citation_key, direct source URL, extracted-data counts, and synthesis gate.\n" +
  "- ST01_COMPANION_REPORT_PROVENANCE_21.csv and .tex: exact report-level provenance for all 21 companions.\n" +
  "- ST01_COMPANION_GUARDRAIL_METRICS_14.csv: the 14 companion metrics that must remain report specific.\n" +
  "- ST01_REFERENCES_227.bib: standalone bibliography resolving all 227 report keys.\n" +
  "- ST01_REFERENCES_206.bib: synchronized primary-report-only compatibility bibliography.\n" +
  "- INCLUDED_STUDIES_206_EXPLICIT_BIBLIOGRAPHY.tex: explicit enumeration of all 227 eligible-report keys; no wildcard inclusion.\n" +
  "- ST01_INCLUDED_STUDIES_206.xlsx: styled workbook view of the governed tables.\n" +
  "- ST01_SUPPLEMENT_DRIVER.tex and .pdf: standalone electronic supplement.\n\n" +
  "## Adjudication-aware synthesis gate\n\n" +
  "A pending-human token triggers exclusion only when the same row lacks resolved or approved adjudication. " +
  "The 59 historical tokens in SCR-00083 and SCR-00553 are resolved or approved; they are not automatically quarantined. " +
  "Report-specific conflict guardrails remain active, and any future unresolved pending row cannot support numerical, tradeoff, or prevalence synthesis.\n\n" +
  "## Bibliography carriers\n\n" +
  "The manuscript-level primary carrier is ../../references_206_candidate.bib; the duplicate-free companion carrier is ../../references_companion_21_candidate.bib. " +
  "The standalone ST-01 driver uses the combined 227-entry ST01_REFERENCES_227.bib.\n";

await fs.mkdir(supplementDir, { recursive: true });
await fs.mkdir(qaDir, { recursive: true });
await Promise.all([
  fs.writeFile(path.join(supplementDir, "ST01_INCLUDED_STUDIES_206.csv"), serializeCsv(st01Rows), "utf8"),
  fs.writeFile(path.join(supplementDir, "ST01_INCLUDED_STUDIES_206.tex"), st01Tex, "utf8"),
  fs.writeFile(path.join(supplementDir, "ST01_ELIGIBLE_REPORT_LINEAGE_227.csv"), serializeCsv(reportRows), "utf8"),
  fs.writeFile(path.join(supplementDir, "ST01_COMPANION_REPORT_PROVENANCE_21.csv"), serializeCsv(companionProvenanceRows), "utf8"),
  fs.writeFile(path.join(supplementDir, "ST01_COMPANION_REPORT_PROVENANCE_21.tex"), companionTex, "utf8"),
  fs.writeFile(path.join(supplementDir, "ST01_COMPANION_GUARDRAIL_METRICS_14.csv"), serializeCsv(guardrailRows), "utf8"),
  fs.writeFile(path.join(supplementDir, "INCLUDED_STUDIES_206_EXPLICIT_BIBLIOGRAPHY.tex"), explicitIncludeTex, "utf8"),
  fs.writeFile(path.join(supplementDir, "ST01_REFERENCES_206.bib"), primaryBibSource, "utf8"),
  fs.writeFile(path.join(supplementDir, "ST01_REFERENCES_227.bib"), combinedBibText, "utf8"),
  fs.writeFile(companionBibliographyPath, companionBibText, "utf8"),
  fs.writeFile(path.join(supplementDir, "README.md"), readme, "utf8"),
  fs.writeFile(path.join(qaDir, "FINAL_PRISMA_ITEM17_QA.json"), JSON.stringify(qa, null, 2) + "\n", "utf8"),
  fs.writeFile(path.join(qaDir, "FINAL_PRISMA_ITEM17_QA.md"), qaMarkdown, "utf8"),
  fs.writeFile(path.join(qaDir, "FINAL_COMPANION_PROVENANCE_QA.json"), JSON.stringify(companionQa, null, 2) + "\n", "utf8"),
  fs.writeFile(path.join(qaDir, "FINAL_COMPANION_PROVENANCE_QA.md"), companionQaMarkdown, "utf8"),
]);

if (failures.length) throw new Error("PRISMA Item 17 companion-lineage QA failed: " + failures.join(", "));
process.stdout.write(JSON.stringify(qa, null, 2) + "\n");
