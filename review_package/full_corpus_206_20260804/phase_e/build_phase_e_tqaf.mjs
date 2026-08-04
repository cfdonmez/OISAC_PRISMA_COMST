import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const sourceInput = String(process.env.OISAC_PHASE_D_WORKBOOK ?? "").trim();
if (!sourceInput) throw new Error("Set OISAC_PHASE_D_WORKBOOK to the authoritative Phase-D workbook path.");
const SOURCE = path.resolve(sourceInput);
const EXPECTED_SOURCE_SHA256 = "c1b3b89789c6ed3e20da5a6283e480875c1913e21af88ff59ac747a6aa949348";
const CROSSWALK_PATH = path.join(HERE, "PHASE_E_TQAF_NORMALIZATION_CROSSWALK_DRAFT_2026-08-04.json");
const METHOD_VERSION = "phase_e_tqaf_deterministic_v1.0_2026-08-04";
const LEGACY_RESOLUTION = "insufficient_information_due_legacy_extraction";
const OUTPUTS = {
  risk: path.join(HERE, "risk_of_bias_PHASE_E_DRAFT_2026-08-04.csv"),
  certainty: path.join(HERE, "certainty_grade_PHASE_E_DRAFT_2026-08-04.csv"),
  synthesis: path.join(HERE, "synthesis_matrix_PHASE_E_DRAFT_2026-08-04.csv"),
  audit: path.join(HERE, "phase_e_tqaf_dimension_audit_2026-08-04.csv"),
  bodyNormalizationAudit: path.join(HERE, "phase_e_tqaf_body_normalization_audit_2026-08-04.csv"),
  legacy: path.join(HERE, "phase_e_tqaf_resolved_legacy_metric_rows_2026-08-04.csv"),
  qa: path.join(HERE, "phase_e_tqaf_QA_2026-08-04.json"),
  summary: path.join(HERE, "phase_e_tqaf_summary_2026-08-04.md"),
};

const DIMENSIONS = [
  "technical_relevance",
  "metric_clarity",
  "reporting_completeness",
  "validation_maturity",
  "reproducibility",
  "benchmark_readiness",
  "comparison_admissibility",
  "limitation_transparency",
];

function clean(value) {
  if (value === null || value === undefined) return "";
  return String(value).trim();
}
function lower(value) { return clean(value).toLowerCase(); }
function sha256(filePath) { return crypto.createHash("sha256").update(fs.readFileSync(filePath)).digest("hex"); }
function asNumber(value) {
  if (typeof value === "number" && Number.isFinite(value)) return value;
  const parsed = Number(clean(value));
  return Number.isFinite(parsed) ? parsed : null;
}
function splitCodes(value) {
  return clean(value).split(/[|;]/).map((item) => item.trim()).filter(Boolean);
}
function exactMissing(value) {
  return /^(?:|nr|n\/r|na|n\/a|unc|unknown|unclear|none|absent|not reported|not_reported|not applicable|not_applicable|insufficient)$/i.test(clean(value));
}
function presence(value) {
  const text = clean(value);
  if (exactMissing(text)) return 0;
  if (/^(?:nr|not reported|not available)\b/i.test(text)) return 0;
  if (/\b(?:partial|incomplete|uncertain|unclear)\b/i.test(text)) return 0.5;
  return 1;
}
function authorPresence(value) {
  const text = clean(value);
  if (exactMissing(text) || /^(?:nr|not reported|no explicit|not explicitly)\b/i.test(text)) return 0;
  return presence(text);
}
function avg(values) {
  const usable = values.filter((value) => value !== null && value !== undefined && Number.isFinite(value));
  return usable.length ? usable.reduce((sum, value) => sum + value, 0) / usable.length : 0;
}
function median(values) {
  const ordered = values.filter(Number.isFinite).sort((a, b) => a - b);
  if (!ordered.length) return 0;
  const middle = Math.floor(ordered.length / 2);
  return ordered.length % 2 ? ordered[middle] : (ordered[middle - 1] + ordered[middle]) / 2;
}
function scoreComposite(value) {
  if (value < 0.25) return 0;
  if (value < 0.5) return 1;
  if (value < 0.8) return 2;
  return 3;
}
function overallFromMean(value) {
  if (value < 0.75) return 0;
  if (value < 1.5) return 1;
  if (value < 2.25) return 2;
  return 3;
}
function capScore(score, cap, code, caps) {
  if (!caps.includes(code)) caps.push(code);
  return Math.min(score, cap);
}
function groupBy(rows, key) {
  const grouped = new Map();
  for (const row of rows) {
    const value = clean(row[key]);
    if (!grouped.has(value)) grouped.set(value, []);
    grouped.get(value).push(row);
  }
  return grouped;
}
function slug(value) {
  return lower(value).normalize("NFKD").replace(/[^a-z0-9]+/g, "_").replace(/^_+|_+$/g, "").slice(0, 80) || "unspecified";
}
function csvEscape(value) {
  const text = value === null || value === undefined ? "" : String(value);
  return /[",\r\n]/.test(text) ? `"${text.replace(/"/g, '""')}"` : text;
}
function writeCsv(filePath, headers, rows) {
  const lines = [headers.join(",")];
  for (const row of rows) lines.push(headers.map((header) => csvEscape(row[header])).join(","));
  fs.writeFileSync(filePath, `${lines.join("\n")}\n`, "utf8");
}
function countBy(values) {
  const counts = {};
  for (const value of values) counts[String(value)] = (counts[String(value)] ?? 0) + 1;
  return Object.fromEntries(Object.entries(counts).sort(([a], [b]) => a.localeCompare(b, undefined, { numeric: true })));
}
function isQuarantinedClaim(row) {
  return /quarantin|exclude_disputed_claim/i.test([
    row.claim_status, row.survey_use_class, row.reason_code, row.resolution_rationale,
  ].map(clean).join("|"));
}
function readSheet(workbook, name) {
  const sheet = workbook.worksheets.getItem(name);
  const values = sheet.getUsedRange()?.values ?? [];
  if (!values.length) throw new Error(`Empty worksheet: ${name}`);
  const headers = values[0].map(clean);
  const rows = values.slice(1).map((cells, offset) => Object.fromEntries([
    ...headers.map((header, index) => [header, cells[index]]),
    ["__row_number", offset + 2],
  ]));
  return { name, headers, rows };
}
function locator(row) {
  const parts = [];
  const page = clean(row.pdf_page);
  if (page) parts.push(`pdf_page=${page}`);
  for (const key of ["printed_page", "section_heading", "table_id", "figure_id", "equation_id"]) {
    const value = clean(row[key]);
    if (value) parts.push(`${key}=${value}`);
  }
  return parts.join("; ") || "locator_not_reported";
}
function traceRows(rows, type, idField, limit = 8) {
  return rows.slice(0, limit).map((row) => ({
    record_id: clean(row[idField]),
    record_type: type,
    source_screening_record_id: clean(row.source_screening_record_id ?? row.source_scr_id),
    locator: clean(row.source_locator) || locator(row),
  }));
}
function pickEvidence(rows, pattern, limit = 6) {
  return rows.filter((row) => pattern.test(`${clean(row.evidence_domain)}|${clean(row.variable_code)}`)).slice(0, limit);
}
function metricDomains(row) {
  const value = lower(row.metric_domain);
  if (/joint|both|integrated/.test(value)) return ["communication", "sensing"];
  const domains = [];
  if (/comm|data|transmission|network/.test(value)) domains.push("communication");
  if (/sens|radar|lidar|locali|rang|detect|perception|imaging|vibration|strain|temperature/.test(value)) domains.push("sensing");
  return domains;
}
function metricMaturity(value) {
  const text = lower(value);
  if (/operational|deployment/.test(text)) return 7;
  if (/field/.test(text)) return 6;
  if (/prototype|testbed|proof.?of.?concept|poc/.test(text)) return 5;
  if (/laboratory|experiment|measurement/.test(text)) return 4;
  if (/emulat|trace|dataset/.test(text)) return 3;
  if (/simulat|numerical|monte.?carlo/.test(text)) return 2;
  if (/analytical|theoretical|model/.test(text)) return 1;
  return 0;
}
function availabilityValue(value) {
  const text = lower(value);
  if (text === "na") return null;
  if (/^open$|public|repository|fully_available/.test(text)) return 1;
  if (/partial/.test(text)) return 0.75;
  if (/request/.test(text)) return 0.5;
  return 0;
}
function repeatabilityValue(value) {
  const text = lower(value);
  if (/complete|substantial/.test(text)) return 1;
  if (/partial/.test(text)) return 0.5;
  return 0;
}
function compClass(value) {
  const text = lower(value);
  if (!text) return LEGACY_RESOLUTION;
  if (/not.?comparable/.test(text)) return "not_comparable";
  if (/conditional/.test(text)) return "conditionally_comparable";
  if (/direct/.test(text)) return "directly_comparable";
  if (/descriptive/.test(text)) return "descriptive_only";
  if (/insufficient/.test(text)) return "insufficient_information";
  return text;
}
function admClass(value) {
  const text = lower(value);
  if (!text) return LEGACY_RESOLUTION;
  if (/not.?admissible/.test(text)) return "not_admissible";
  if (/conditional/.test(text)) return "conditionally_admissible";
  if (/^admissible$|directly.?admissible/.test(text)) return "admissible";
  if (/insufficient/.test(text)) return "insufficient_information";
  return text;
}
function operationalMetric(row, quarantinedIds) {
  const status = lower(row.value_status);
  if (quarantinedIds.has(clean(row.metric_record_id))) return false;
  if (/^(?:|nr|na|unc|not_reported|not reported|insufficient|unknown)$/.test(status)) return false;
  const representation = lower(row.result_representation);
  if (/^(?:|qualitative|conceptual|not_reported)$/.test(representation) && asNumber(row.value_numeric) === null && !clean(row.value_low) && !clean(row.value_high)) return false;
  return asNumber(row.value_numeric) !== null || clean(row.value_low) || clean(row.value_high) || presence(row.value_reported_text) > 0;
}
function dimensionlessMetric(row) {
  return /ber|ser|bler|error.?rate|probability|accuracy|precision|recall|f1|mape|correlation|ratio|efficiency|q.?factor|normalized|index|score/i.test(`${clean(row.metric_family_code)}|${clean(row.metric_name_reported)}`);
}
function metricRowCompleteness(row, quarantinedIds) {
  const status = lower(row.value_status);
  const reported = !/^(?:|nr|na|unc|not_reported|not reported|insufficient|unknown)$/.test(status) ? 1 : 0;
  const family = presence(row.metric_family_code) || presence(row.metric_definition_reported) ? 1 : 0;
  const plane = presence(row.measurement_plane_code);
  const context = avg([presence(row.validation_type_code), presence(row.scenario_summary)]);
  const operation = operationalMetric(row, quarantinedIds) && (presence(row.unit_reported) || presence(row.normalized_unit) || dimensionlessMetric(row)) ? 1 : 0;
  const conflict = quarantinedIds.has(clean(row.metric_record_id)) || (/conflict|unc/i.test(clean(row.conflict_flag)) && !/no.?conflict|resolved/i.test(clean(row.conflict_flag)));
  const completeness = conflict ? 0 : avg([reported, family, plane, context, operation]);
  return { reported, family, plane, context, operation, conflict, completeness };
}
function normalizeMechanism(code) {
  const text = lower(code);
  if (/waveform|same_signal|joint_signal/.test(text)) return "shared_waveform";
  if (/hardware|device|front.?end|aperture|detector|laser|transceiver/.test(text)) return "shared_hardware";
  if (/carrier|wavelength/.test(text)) return "shared_optical_carrier";
  if (/link|channel|fiber|path/.test(text)) return "shared_link_or_channel";
  if (/resource|allocation|spectrum|time|frequency|spatial/.test(text)) return "shared_resource_allocation";
  if (/joint|optim|co.?design/.test(text)) return "joint_design_or_optimization";
  if (/application|scenario|co.?located/.test(text)) return "shared_application_scenario";
  return "other_integration_mechanism";
}
function normalizeTradeoff(row) {
  const text = lower([row.communication_axis_or_variable, row.sensing_axis_or_variable, row.optimization_objective, row.result_summary].join(" "));
  if (/rate|throughput|capacity/.test(text) && /accur|error|mape|detect|locali/.test(text)) return "rate_accuracy";
  if (/rate|throughput|capacity/.test(text) && /resolution/.test(text)) return "rate_resolution";
  if (/rate|throughput|capacity/.test(text) && /range|distance/.test(text)) return "rate_range";
  if (/power|energy|snr|osnr/.test(text)) return "power_resource_allocation";
  if (/bandwidth|spectral|subcarrier/.test(text)) return "bandwidth_spectral_efficiency";
  if (/pilot|guard|waveform|modulation|chirp/.test(text)) return "waveform_pilot_guard";
  if (/interference|coexist|crosstalk/.test(text)) return "interference_coexistence";
  if (/complex|latency|comput/.test(text)) return "complexity_latency";
  if (/security|privacy/.test(text)) return "security";
  return "other_tradeoff";
}

function normalizeMetricFamily(row, domain) {
  const text = lower([row.metric_family_code, row.metric_name_reported, row.metric_definition_reported].join(" "));
  if (/ber|bit.?error|ser|symbol.?error|bler|block.?error|packet.?error|fer|frame.?error/.test(text)) return "error_rate";
  if (/throughput|data.?rate|bit.?rate|line.?rate|symbol.?rate|baud|capacity|achievable.?rate|traffic.?rate/.test(text)) return "throughput_rate_capacity";
  if (/spectral.?efficien|spectrum.?efficien|bits?\/?s\/?hz/.test(text)) return "spectral_efficiency";
  if (/snr|sinr|osnr|esnr|signal.?to.?noise|carrier.?to.?noise/.test(text)) return domain === "communication" ? "communication_signal_quality" : "sensing_signal_quality";
  if (/evm|error.?vector|ngmi|gmi|q.?factor|eye.?opening|constellation/.test(text)) return "received_signal_quality";
  if (/outage|availability|reliab|success.?probability|coverage.?probability/.test(text)) return "reliability_outage";
  if (/latency|delay|processing.?time|runtime|convergence|execution.?time/.test(text)) return "latency_complexity";
  if (/secrecy|security|privacy|eavesdrop|key.?rate|jamming/.test(text)) return "security_resilience";
  if (/crosstalk|interference|isolation|aclr|leakage/.test(text)) return "interference_crosstalk";
  if (/attenuation|path.?loss|insertion.?loss|link.?loss|channel.?gain/.test(text)) return "channel_loss_gain";
  if (/power|energy|photon|current|voltage|responsivity|quantum.?efficien|noise.?figure/.test(text)) return "power_energy_device_response";
  if (/bandwidth|frequency|wavelength|subcarrier|sampling.?rate|symbol.?duration|cyclic.?prefix|modulation.?order/.test(text)) return "bandwidth_waveform_configuration";
  if (domain === "communication" && /distance|range|reach|coverage|link.?length/.test(text)) return "communication_reach_coverage";
  if (/range|ranging|distance|tof|time.?of.?flight/.test(text) && /error|rmse|mae|resolution|accuracy|precision|estimate|bias|crb|bound/.test(text)) return "range_error_resolution";
  if (/velocity|speed|doppler/.test(text) && /error|rmse|mae|resolution|accuracy|precision|estimate|bias|crb|bound/.test(text)) return "velocity_doppler_error_resolution";
  if (/angle|azimuth|direction|position|locali|coordinate|tracking/.test(text) && /error|rmse|mae|resolution|accuracy|precision|estimate|bias|crb|bound/.test(text)) return "angle_position_localization";
  if (/detection.?probability|probability.?of.?detection|false.?alarm|roc|miss.?detection|detection.?rate/.test(text)) return "detection_false_alarm";
  if (/mse|rmse|mae|mape|mean.?absolute|estimation.?error|prediction.?error|reconstruction.?error|crb|fim|fisher/.test(text)) return "estimation_error_bound";
  if (/resolution|resolvability|point.?spread|ambiguity.?function/.test(text)) return "sensing_resolution";
  if (/sensitivity|limit.?of.?detection|minimum.?detect|dynamic.?range/.test(text)) return "sensitivity_detection_limit";
  if (/image|imaging|reconstruction|psnr|ssim|point.?cloud|profile/.test(text)) return "imaging_reconstruction_quality";
  if (/classification|recognition|precision|recall|f1.?score|confusion|accuracy/.test(text)) return "classification_inference_accuracy";
  if (/temperature|strain|vibration|displacement|pressure|humidity|concentration|refractive.?index/.test(text)) return "physical_quantity_estimation";
  if (/range|distance|velocity|speed|doppler|angle|position|locali|target|radar|lidar|sensing/.test(text)) return "sensing_task_output_or_configuration";
  if (/count|number|size|length|width|spacing|ratio|coefficient|parameter|setting|threshold|sweep|iteration|sample/.test(text)) return "system_configuration_or_input_parameter";
  return domain === "communication" ? "other_communication_metric" : "other_sensing_metric";
}

function normalizeTechnology(value) {
  const text = lower(value);
  if (/ofdm|multicarrier|dmt|otfs|fbmc/.test(text)) return "multicarrier_waveforms";
  if (/vlc|li.?fi|visible.?light|led|illumination/.test(text)) return "vlc_lifi_illumination";
  if (/fso|free.?space|lidar|laser.?radar/.test(text)) return "fso_lidar";
  if (/distributed.?fiber|fiber.?sensing|das|phi.?otdr|otdr|brillouin|rayleigh/.test(text)) return "distributed_fiber_sensing";
  if (/coherent|homodyne|heterodyne|iq.?receiver|digital.?signal.?processing|dsp/.test(text)) return "coherent_detection_and_dsp";
  if (/terahertz|thz|mmwave|millimeter|microwave.?photon|photomix|utc.?pd/.test(text)) return "microwave_photonics_and_photonic_thz";
  if (/silicon|integrated.?photon|photonic.?integrat|waveguide|microring|resonator|metasurface/.test(text)) return "integrated_photonics";
  if (/machine.?learning|deep.?learning|neural|artificial.?intelligence|\bai\b|reinforcement/.test(text)) return "ai_ml_and_data_driven_methods";
  if (/mimo|beamform|optical.?phased.?array|\bopa\b|beam.?steer/.test(text)) return "mimo_beamforming_and_opa";
  if (/frequency.?comb|optical.?comb|microcomb/.test(text)) return "optical_frequency_combs";
  if (/fbg|fiber.?bragg|interferometer|interferometric|fabry|mach.?zehnder/.test(text)) return "gratings_and_interferometry";
  if (/quantum|photon.?count|single.?photon|spad/.test(text)) return "quantum_and_photon_counting";
  if (/ris|reconfigurable.?intelligent|intelligent.?surface/.test(text)) return "reconfigurable_intelligent_surfaces";
  if (/radio.?over.?fiber|rof|fronthaul/.test(text)) return "radio_over_fiber";
  if (/fmcw|chirp|radar/.test(text)) return "radar_and_fmcw_processing";
  if (/optimization|resource.?allocation|precod|coding|equaliz|channel.?estimat|synchron/.test(text)) return "optimization_and_communications_dsp";
  if (/sensor|sensing|locali|position|tracking|imaging/.test(text)) return "sensing_and_inference_processing";
  return "other_enabling_technology";
}

function normalizeApplication(value) {
  const text = lower(value);
  if (/6g|beyond.?5g|future.?network/.test(text)) return "six_g_and_future_networks";
  if (/access|backhaul|fronthaul|datacenter|data.?center|telecom|transport.?network|pon|fiber.?network/.test(text)) return "telecom_access_transport_datacenter";
  if (/autonom|automotive|vehicle|driving|uav|drone|transportation|traffic|robot/.test(text)) return "transportation_autonomy_and_uav";
  if (/locali|position|navigation|tracking|indoor.?position/.test(text)) return "localization_positioning_navigation";
  if (/industrial|manufactur|factory|infrastructure|bridge|rail|pipeline|power.?grid|cable|structural/.test(text)) return "industrial_and_infrastructure";
  if (/vibration|strain|structural.?health|fault|condition.?monitor/.test(text)) return "structural_health_and_vibration_monitoring";
  if (/health|medical|biomedical|wearable|vital|ppg|patient/.test(text)) return "healthcare_biomedical_wearables";
  if (/environment|atmospher|weather|turbulence|pollution|temperature|humidity|ocean|water/.test(text)) return "environmental_and_atmospheric_monitoring";
  if (/security|surveillance|intrusion|anti.?jamming|privacy|authentication/.test(text)) return "security_surveillance_resilience";
  if (/smart.?city|iot|internet.?of.?things|indoor|home|building/.test(text)) return "smart_city_iot_indoor";
  if (/aerospace|satellite|space|aircraft/.test(text)) return "aerospace_satellite_space";
  if (/imaging|lidar|mapping|point.?cloud|remote.?sensing/.test(text)) return "imaging_lidar_mapping";
  return "other_application_domain";
}

async function loadData() {
  const sourceSha = sha256(SOURCE);
  if (sourceSha !== EXPECTED_SOURCE_SHA256) throw new Error(`Source SHA-256 mismatch: ${sourceSha}`);
  const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(SOURCE));
  const sheets = {
    master: readSheet(workbook, "01_STUDY_MASTER"),
    evidence: readSheet(workbook, "03_EVIDENCE_ITEMS"),
    metrics: readSheet(workbook, "04_METRIC_RESULTS"),
    tradeoffs: readSheet(workbook, "05_TRADEOFF_EVIDENCE"),
    ledger: readSheet(workbook, "22_SURVEY_CLAIM_LEDGER"),
    conflicts: readSheet(workbook, "23_CONFLICT_REGISTER"),
    surveyUse: readSheet(workbook, "24_STUDY_SURVEY_USE"),
  };
  const crosswalk = JSON.parse(fs.readFileSync(CROSSWALK_PATH, "utf8"));
  return { sourceSha, sheets, crosswalk };
}

function buildStudyScores(data) {
  const { sourceSha, sheets, crosswalk } = data;
  const evidenceByStudy = groupBy(sheets.evidence.rows, "study_cluster_id");
  const metricsByStudy = groupBy(sheets.metrics.rows, "study_cluster_id");
  const tradeoffsByStudy = groupBy(sheets.tradeoffs.rows, "study_cluster_id");
  const ledgerByStudy = groupBy(sheets.ledger.rows, "study_cluster_id");
  const conflictsByStudy = groupBy(sheets.conflicts.rows, "study_cluster_id");
  const useByStudy = new Map(sheets.surveyUse.rows.map((row) => [clean(row.study_cluster_id), row]));
  const crossByStudy = new Map(crosswalk.per_study_crosswalk.map((row) => [clean(row.study_cluster_id), row]));
  const quarantineClaims = sheets.ledger.rows.filter(isQuarantinedClaim);
  const quarantineIds = new Set(quarantineClaims.map((row) => clean(row.record_id)));
  const legacyRows = sheets.metrics.rows.filter((row) => !clean(row.metric_comparability_class) || !clean(row.metric_comparison_admissibility_class));

  const scored = [];
  const auditRows = [];
  for (const master of sheets.master.rows) {
    const id = clean(master.study_cluster_id);
    const evidence = evidenceByStudy.get(id) ?? [];
    const metrics = metricsByStudy.get(id) ?? [];
    const tradeoffs = tradeoffsByStudy.get(id) ?? [];
    const ledger = ledgerByStudy.get(id) ?? [];
    const conflicts = conflictsByStudy.get(id) ?? [];
    const surveyUse = useByStudy.get(id) ?? {};
    const cross = crossByStudy.get(id);
    if (!cross) throw new Error(`No crosswalk row for ${id}`);
    const quarantined = ledger.filter(isQuarantinedClaim);
    const qMetric = quarantined.filter((row) => clean(row.record_type) === "metric");
    const qEvidence = quarantined.filter((row) => clean(row.record_type) === "evidence");
    const qTradeoff = quarantined.filter((row) => clean(row.record_type) === "tradeoff");
    const architectureQuarantine = qEvidence.some((claim) => /4\.3|4\.4|taxonomy|architect|integration/i.test(`${clean(claim.survey_section)}|${clean(claim.claim_preview)}`));

    const audits = {};
    const commPresent = presence(master.communication_functions);
    const sensingPresent = presence(master.sensing_tasks);
    const mechanisms = splitCodes(master.integration_mechanism_codes).map(normalizeMechanism);
    const strongMechanism = mechanisms.some((code) => code !== "shared_application_scenario" && code !== "other_integration_mechanism");
    let technicalBefore = 0;
    if (presence(master.primary_optical_modality_code) && commPresent && sensingPresent) {
      if (!strongMechanism || ["weak", "not_applicable"].includes(cross.six_g)) technicalBefore = 1;
      else if (cross.six_g === "direct") technicalBefore = 3;
      else technicalBefore = 2;
    }
    const technicalCaps = [];
    let technical = technicalBefore;
    if (architectureQuarantine) technical = capScore(technical, 2, "quarantined_architecture_or_integration_claim_cap_2", technicalCaps);
    audits.technical_relevance = {
      before: technicalBefore, score: technical, caps: technicalCaps,
      inputs: { modality: cross.modality, communication_present: commPresent, sensing_present: sensingPresent, integration_mechanisms: [...new Set(mechanisms)], strong_shared_mechanism: strongMechanism, six_g_relevance: cross.six_g },
      trace: [...traceRows(pickEvidence(evidence, /taxonomy|integration|architecture|application|communication|sensing/i), "evidence", "evidence_id", 6), ...traceRows(qEvidence, "claim_ledger", "claim_ledger_id", 4)],
    };

    const domainRows = { communication: [], sensing: [] };
    for (const metric of metrics) for (const domain of metricDomains(metric)) domainRows[domain].push(metric);
    const metricStats = {};
    for (const domain of ["communication", "sensing"]) {
      const rows = domainRows[domain];
      const details = rows.map((row) => metricRowCompleteness(row, quarantineIds));
      metricStats[domain] = {
        rows: rows.length,
        reported_rows: details.filter((item) => item.reported).length,
        operational_rows: rows.filter((row) => operationalMetric(row, quarantineIds)).length,
        complete_rows: details.filter((item) => item.completeness >= 0.8).length,
        complete_ratio: rows.length ? details.filter((item) => item.completeness >= 0.8).length / rows.length : 0,
        unresolved_conflicts: details.filter((item) => item.conflict).length,
      };
    }
    const bothDomains = metricStats.communication.rows > 0 && metricStats.sensing.rows > 0;
    const reportedOutcomes = metricStats.communication.reported_rows + metricStats.sensing.reported_rows;
    const minComplete = bothDomains ? Math.min(metricStats.communication.complete_ratio, metricStats.sensing.complete_ratio) : 0;
    const anyMetricConflict = metricStats.communication.unresolved_conflicts + metricStats.sensing.unresolved_conflicts > 0;
    let metricBefore = reportedOutcomes === 0 ? 0 : (!bothDomains || minComplete < 0.5 || anyMetricConflict ? 1 : (minComplete < 0.8 ? 2 : 3));
    const metricCaps = [];
    let metricClarity = metricBefore;
    if (qMetric.length) metricClarity = capScore(metricClarity, 2, "quarantined_metric_claim_cap_2", metricCaps);
    audits.metric_clarity = {
      before: metricBefore, score: metricClarity, caps: metricCaps,
      inputs: { domains: metricStats, both_domains: bothDomains, minimum_domain_complete_ratio: Number(minComplete.toFixed(4)), quarantined_metric_claims: qMetric.length },
      trace: [...traceRows([...domainRows.communication, ...domainRows.sensing], "metric", "metric_record_id", 10), ...traceRows(qMetric, "claim_ledger", "claim_ledger_id", 5)],
    };

    const coreMetrics = [...domainRows.communication, ...domainRows.sensing];
    const metricLocatorRatio = coreMetrics.length ? coreMetrics.filter((row) => clean(row.pdf_page) && (clean(row.section_heading) || clean(row.table_id) || clean(row.figure_id) || clean(row.equation_id))).length / coreMetrics.length : 0;
    const reportingComponents = {
      modality_and_integration: avg([presence(master.primary_optical_modality_code), presence(master.integration_level_code), presence(master.integration_mechanism_codes)]),
      shared_resource_and_functions: avg([presence(master.shared_hardware_waveform_resource), commPresent, sensingPresent]),
      waveform_and_front_end: avg([presence(master.waveform_modulation), presence(master.optical_front_end)]),
      context: avg([presence(master.network_setting), presence(master.scenario_environment), presence(master.application_domain_codes)]),
      channel_and_hardware: avg([presence(master.channel_models), presence(master.hardware_assumptions)]),
      dsp_and_design: avg([presence(master.signal_processing_methods), presence(master.system_design_strategies)]),
      validation: avg([presence(master.validation_type_codes), presence(master.scenario_environment)]),
      outcome_provenance: metricLocatorRatio,
    };
    const reportingComposite = avg(Object.values(reportingComponents));
    let reportingBefore = scoreComposite(reportingComposite);
    const reportingCaps = [];
    let reporting = reportingBefore;
    if (architectureQuarantine) reporting = capScore(reporting, 2, "quarantined_scope_reporting_claim_cap_2", reportingCaps);
    audits.reporting_completeness = {
      before: reportingBefore, score: reporting, caps: reportingCaps,
      inputs: { components: reportingComponents, composite: Number(reportingComposite.toFixed(4)), metric_locator_rows: coreMetrics.length },
      trace: [...traceRows(pickEvidence(evidence, /taxonomy|integration|waveform|hardware|channel|method|signal|design|scenario|validation/i), "evidence", "evidence_id", 8), ...traceRows(coreMetrics, "metric", "metric_record_id", 5)],
    };

    const maturityMax = Number(cross.validation_maturity_max ?? 0);
    const fieldByDomain = Object.fromEntries(["communication", "sensing"].map((domain) => [domain, domainRows[domain].some((row) => operationalMetric(row, quarantineIds) && metricMaturity(row.validation_type_code) >= 6)]));
    let validationBefore = maturityMax === 0 ? 0 : maturityMax <= 2 ? 1 : maturityMax <= 5 ? 2 : (fieldByDomain.communication && fieldByDomain.sensing ? 3 : 2);
    audits.validation_maturity = {
      before: validationBefore, score: validationBefore, caps: [],
      inputs: { canonical_maturity_max: maturityMax, canonical_categories: cross.validation_categories, field_or_deployment_outcome_by_domain: fieldByDomain, strong_requires_both_functions: true },
      trace: [...traceRows(pickEvidence(evidence, /validation|experiment|simulation|prototype|field/i), "evidence", "evidence_id", 7), ...traceRows(coreMetrics.filter((row) => presence(row.validation_type_code)), "metric", "metric_record_id", 5)],
    };

    const P = repeatabilityValue(cross.repeatability);
    const D = availabilityValue(cross.dataset_availability);
    const C = availabilityValue(cross.code_model_availability);
    const S = avg([presence(master.waveform_modulation), presence(master.optical_front_end), presence(master.channel_models), presence(master.hardware_assumptions), presence(master.signal_processing_methods), presence(master.system_design_strategies)]);
    const V = avg([presence(master.validation_type_codes), presence(master.scenario_environment), metricLocatorRatio]);
    const reproComposite = avg([P, D, C, S, V]);
    let reproducibilityBefore = scoreComposite(reproComposite);
    const reproCaps = [];
    let reproducibility = reproducibilityBefore;
    if (reproducibility === 3 && !(P === 1 && (D === 1 || C === 1))) reproducibility = capScore(reproducibility, 2, "strong_reproducibility_requires_complete_parameters_and_open_data_or_code", reproCaps);
    audits.reproducibility = {
      before: reproducibilityBefore, score: reproducibility, caps: reproCaps,
      inputs: { P_repeatable_parameters: P, D_dataset: D, C_code_or_model: C, S_setup: Number(S.toFixed(4)), V_protocol_and_locator: Number(V.toFixed(4)), composite: Number(reproComposite.toFixed(4)) },
      trace: traceRows(pickEvidence(evidence, /availability|parameter|validation|scenario|channel|hardware|waveform|method/i), "evidence", "evidence_id", 9),
    };

    const compDomain = {};
    for (const domain of ["communication", "sensing"]) {
      const rows = domainRows[domain];
      compDomain[domain] = {
        direct: rows.filter((row) => operationalMetric(row, quarantineIds) && compClass(row.metric_comparability_class) === "directly_comparable" && admClass(row.metric_comparison_admissibility_class) === "admissible").length,
        conditional: rows.filter((row) => operationalMetric(row, quarantineIds) && ["directly_comparable", "conditionally_comparable"].includes(compClass(row.metric_comparability_class)) && ["admissible", "conditionally_admissible"].includes(admClass(row.metric_comparison_admissibility_class))).length,
        descriptive_or_operational: rows.filter((row) => operationalMetric(row, quarantineIds)).length,
        legacy_insufficient: rows.filter((row) => compClass(row.metric_comparability_class) === LEGACY_RESOLUTION || admClass(row.metric_comparison_admissibility_class) === LEGACY_RESOLUTION).length,
      };
    }
    let comparisonBefore = 0;
    if (compDomain.communication.direct && compDomain.sensing.direct) comparisonBefore = 3;
    else if (compDomain.communication.conditional && compDomain.sensing.conditional) comparisonBefore = 2;
    else if (compDomain.communication.descriptive_or_operational || compDomain.sensing.descriptive_or_operational) comparisonBefore = 1;
    const comparisonCaps = [];
    let comparison = comparisonBefore;
    const surveyComparisonUse = lower(surveyUse.cross_study_comparison_use);
    if (/descriptive_only|not_allowed|prohibit/.test(surveyComparisonUse)) comparison = capScore(comparison, 1, "phase_d_survey_use_descriptive_only_cap_1", comparisonCaps);
    if (qMetric.length || qTradeoff.length) comparison = capScore(comparison, 1, "quarantined_metric_or_tradeoff_claim_cap_1", comparisonCaps);
    audits.comparison_admissibility = {
      before: comparisonBefore, score: comparison, caps: comparisonCaps,
      inputs: { domain_counts: compDomain, survey_use_class: clean(surveyUse.cross_study_comparison_use), legacy_blank_resolution: LEGACY_RESOLUTION },
      trace: [...traceRows(coreMetrics, "metric", "metric_record_id", 10), ...traceRows([...qMetric, ...qTradeoff], "claim_ledger", "claim_ledger_id", 5)],
    };

    const B = Number(cross.baseline?.value ?? 0);
    const A = Math.max(D ?? 0, C ?? 0);
    const Pr = avg([P, S, V]);
    const M = comparison / 3;
    const Vm = validationBefore / 3;
    const benchmarkComposite = avg([B, A, Pr, M, Vm]);
    let benchmarkBefore = scoreComposite(benchmarkComposite);
    const benchmarkCaps = [];
    let benchmark = benchmarkBefore;
    const benchmarkStrongGuard = cross.baseline?.canonical === "external_or_common" && A === 1 && comparison === 3 && validationBefore >= 2 && reproducibility >= 2 && !quarantined.length;
    if (benchmark === 3 && !benchmarkStrongGuard) benchmark = capScore(benchmark, 2, "strong_benchmark_requires_external_common_baseline_open_artifact_direct_admissibility", benchmarkCaps);
    if (qMetric.length || qTradeoff.length) benchmark = capScore(benchmark, 2, "quarantined_quantitative_claim_cap_2", benchmarkCaps);
    audits.benchmark_readiness = {
      before: benchmarkBefore, score: benchmark, caps: benchmarkCaps,
      inputs: { B_baseline: B, baseline_class: cross.baseline?.canonical, A_open_artifact: A, Pr_protocol: Number(Pr.toFixed(4)), M_comparison: Number(M.toFixed(4)), V_validation: Number(Vm.toFixed(4)), composite: Number(benchmarkComposite.toFixed(4)), strong_guard_pass: benchmarkStrongGuard },
      trace: [...traceRows(pickEvidence(evidence, /comparator|baseline|availability|validation|parameter/i), "evidence", "evidence_id", 7), ...traceRows(coreMetrics.filter((row) => presence(row.baseline_comparator)), "metric", "metric_record_id", 5)],
    };

    const L = authorPresence(master.author_reported_limitations);
    const G = authorPresence(master.author_reported_research_gaps);
    const As = presence(master.assumptions_summary);
    const validationBoundaryRows = pickEvidence(evidence, /validation_boundary|limitation|assumption/i, 10).filter((row) => lower(row.value_origin) === "reported" || !clean(row.value_origin));
    const Vb = validationBoundaryRows.length ? 1 : 0;
    const tradeoffStatus = lower(master.rate_sensing_tradeoff_screening_status);
    let T = null;
    if (!/absent|not_applicable|none/.test(tradeoffStatus)) {
      const positiveTradeoffs = tradeoffs.filter((row) => !/absent|no/.test(lower(row.reported_status)) && presence(row.result_summary));
      T = positiveTradeoffs.length ? avg(positiveTradeoffs.map((row) => avg([presence(row.result_summary), presence(row.constraints), clean(row.pdf_page) ? 1 : 0]))) : 0;
    }
    const limitationComposite = avg([L, G, As, Vb, T]);
    let limitationBefore = scoreComposite(limitationComposite);
    const limitationCaps = [];
    let limitation = limitationBefore;
    if (quarantined.length) limitation = capScore(limitation, 2, "material_quarantined_source_conflict_limitation_cap_2", limitationCaps);
    if (L === 0) limitation = capScore(limitation, 1, "author_origin_limitation_required_cap_1", limitationCaps);
    audits.limitation_transparency = {
      before: limitationBefore, score: limitation, caps: limitationCaps,
      inputs: { L_author_limitations: L, G_author_gaps: G, A_assumptions: As, V_validation_boundary: Vb, T_tradeoff_transparency: T, composite: Number(limitationComposite.toFixed(4)) },
      trace: [...traceRows(pickEvidence(evidence, /limitation|research_gap|assumption|validation_boundary/i), "evidence", "evidence_id", 8), ...traceRows(tradeoffs, "tradeoff", "tradeoff_id", 5)],
    };

    const dimensionScores = Object.fromEntries(DIMENSIONS.map((dimension) => [dimension, audits[dimension].score]));
    const overallMean = avg(Object.values(dimensionScores));
    const overallBefore = overallFromMean(overallMean);
    const overallCaps = [];
    let overall = overallBefore;
    if (quarantined.length) overall = capScore(overall, 2, "any_quarantined_claim_overall_cap_2", overallCaps);
    if (technical === 0 || metricClarity === 0) overall = capScore(overall, 1, "zero_core_relevance_or_metric_clarity_overall_cap_1", overallCaps);
    if (overall === 3 && [technical, metricClarity, reporting, validationBefore].some((score) => score < 2)) overall = capScore(overall, 2, "overall_3_requires_technical_metric_reporting_validation_all_at_least_2", overallCaps);
    if (metricClarity <= 1 && validationBefore <= 1) overall = capScore(overall, 1, "metric_clarity_1_or_lower_and_validation_1_or_lower_overall_cap_1", overallCaps);
    audits.overall_evidence_contribution = {
      before: overallBefore, score: overall, caps: overallCaps,
      inputs: { dimension_scores: dimensionScores, arithmetic_mean: Number(overallMean.toFixed(4)), quarantined_claims: quarantined.length, unresolved_conflict_register_rows: conflicts.filter((row) => /unresolved|claim_restricted|exclude/i.test(`${clean(row.resolution_status)}|${clean(row.survey_use)}`)).length },
      trace: traceRows(quarantined, "claim_ledger", "claim_ledger_id", 10),
    };

    const noteAudit = Object.fromEntries([...DIMENSIONS, "overall_evidence_contribution"].map((dimension) => [dimension, {
      score: audits[dimension].score,
      inputs: audits[dimension].inputs,
      record_trace: audits[dimension].trace,
      caps: audits[dimension].caps,
    }]));
    const result = {
      study_id: id,
      citation: clean(master.preferred_citation) || [clean(master.authors), clean(master.year), clean(master.title)].filter(Boolean).join(". "),
      ...dimensionScores,
      overall_evidence_contribution: overall,
      notes: JSON.stringify({ method_version: METHOD_VERSION, source_workbook_sha256: sourceSha, legacy_blank_policy: LEGACY_RESOLUTION, audit: noteAudit }),
      __master: master,
      __cross: cross,
      __surveyUse: surveyUse,
      __audits: audits,
      __quarantineCount: quarantined.length,
      __quarantineTypes: [...new Set(quarantined.map((row) => clean(row.record_type)))],
    };
    scored.push(result);

    for (const dimension of [...DIMENSIONS, "overall_evidence_contribution"]) {
      const item = audits[dimension];
      auditRows.push({
        study_id: id,
        citation: result.citation,
        dimension,
        score_before_cap: item.before,
        score_final: item.score,
        cap_codes: item.caps.join("|"),
        inputs_json: JSON.stringify(item.inputs),
        record_trace_json: JSON.stringify(item.trace),
        method_version: METHOD_VERSION,
        source_workbook_sha256: sourceSha,
      });
    }
  }
  return { scored, auditRows, legacyRows, quarantineClaims };
}

function buildEvidenceBodies(scored, sheets, quarantineClaims) {
  const byId = new Map(scored.map((row) => [row.study_id, row]));
  const bodyMap = new Map();
  const normalizationAudit = [];
  const add = (section, key, theme, studyId, rawToken = "") => {
    const bodyId = `${section}-${slug(key)}`;
    if (!bodyMap.has(bodyId)) bodyMap.set(bodyId, { section, key, theme, studyIds: new Set(), rawTokenCounts: new Map() });
    const body = bodyMap.get(bodyId);
    body.studyIds.add(studyId);
    if (clean(rawToken)) body.rawTokenCounts.set(clean(rawToken), (body.rawTokenCounts.get(clean(rawToken)) ?? 0) + 1);
  };
  for (const row of scored) add("S1", row.__cross.modality, `O-ISAC modality taxonomy: ${row.__cross.modality}`, row.study_id);
  for (const row of scored) {
    const codes = splitCodes(row.__master.integration_mechanism_codes);
    for (const mechanism of new Set(codes.map(normalizeMechanism))) add("S2", mechanism, `Architecture and integration mechanism: ${mechanism}`, row.study_id);
  }
  const qIds = new Set(quarantineClaims.map((row) => clean(row.record_id)));
  const metricsByStudy = groupBy(sheets.metrics.rows, "study_cluster_id");
  for (const study of scored) {
    const studyMetrics = metricsByStudy.get(study.study_id) ?? [];
    for (const domain of ["communication", "sensing"]) {
      const allDomainEntries = studyMetrics.flatMap((metric) => {
        if (!metricDomains(metric).includes(domain)) return [];
        const rawToken = clean(metric.metric_family_code) || clean(metric.metric_name_reported);
        if (!rawToken || exactMissing(rawToken)) return [];
        return [{ metric, rawToken, canonical: normalizeMetricFamily(metric, domain), quarantined: qIds.has(clean(metric.metric_record_id)) }];
      });
      const eligibleEntries = allDomainEntries.filter((entry) => !entry.quarantined);
      const recognizedEntries = eligibleEntries.filter((entry) => !entry.canonical.startsWith("other_"));
      const recognizedCategories = [...new Set(recognizedEntries.map((entry) => entry.canonical))].sort();
      const fallbackCategory = domain === "communication" ? "other_communication_metric" : "other_sensing_metric";
      const fallbackBodyId = `S3-${slug(`${domain}_${fallbackCategory}`)}`;
      const fallbackIncluded = eligibleEntries.length > 0 && recognizedCategories.length === 0;

      if (recognizedCategories.length) {
        for (const entry of recognizedEntries) add("S3", `${domain}_${entry.canonical}`, `Metric reporting map: ${domain} / ${entry.canonical}`, study.study_id, entry.rawToken);
      } else if (fallbackIncluded) {
        const fallbackTokens = eligibleEntries.map((entry) => entry.rawToken);
        for (const rawToken of fallbackTokens) add("S3", `${domain}_${fallbackCategory}`, `Metric reporting map: ${domain} / ${fallbackCategory} (mixed/unclassified; non-substantive)`, study.study_id, rawToken);
      }

      normalizationAudit.push({
        row_type: "axis_summary", section: "S3", study_id: study.study_id, axis: domain, record_id: "", raw_token: "", normalized_category: fallbackCategory,
        record_eligibility: "study_domain_summary", is_recognized: "NA", body_membership_included: fallbackIncluded ? "yes" : "no",
        recognized_categories_for_study_axis: recognizedCategories.join("|"), recognized_category_count_for_study_axis: recognizedCategories.length,
        eligible_raw_token_count_for_study_axis: eligibleEntries.length,
        fallback_body_id: fallbackBodyId, fallback_body_included_for_study_axis: fallbackIncluded ? "yes" : "no",
        decision_reason: fallbackIncluded ? "fallback_included_because_unmatched_eligible_metric_exists_and_no_recognized_category_in_study_domain" : recognizedCategories.length ? "fallback_suppressed_because_recognized_category_exists_in_study_domain" : "fallback_not_created_because_no_eligible_metric_token_in_study_domain",
      });
      for (const entry of allDomainEntries) {
        const recognized = !entry.canonical.startsWith("other_");
        const included = !entry.quarantined && (recognized || fallbackIncluded);
        normalizationAudit.push({
          row_type: "raw_token", section: "S3", study_id: study.study_id, axis: domain, record_id: clean(entry.metric.metric_record_id), raw_token: entry.rawToken, normalized_category: entry.canonical,
          record_eligibility: entry.quarantined ? "quarantined_excluded" : "eligible", is_recognized: recognized ? "yes" : "no", body_membership_included: included ? "yes" : "no",
          recognized_categories_for_study_axis: recognizedCategories.join("|"), recognized_category_count_for_study_axis: recognizedCategories.length,
          eligible_raw_token_count_for_study_axis: eligibleEntries.length,
          fallback_body_id: fallbackBodyId, fallback_body_included_for_study_axis: fallbackIncluded ? "yes" : "no",
          decision_reason: entry.quarantined ? "quarantined_claim_excluded_from_body_membership" : recognized ? "recognized_category_included" : fallbackIncluded ? "unmatched_token_supports_study_domain_fallback" : "unmatched_token_audit_only_because_recognized_category_exists",
        });
      }
    }
  }
  for (const tradeoff of sheets.tradeoffs.rows) {
    if (qIds.has(clean(tradeoff.tradeoff_id)) || /absent|no/.test(lower(tradeoff.reported_status))) continue;
    add("S4", normalizeTradeoff(tradeoff), `Communication-sensing tradeoff: ${normalizeTradeoff(tradeoff)}`, clean(tradeoff.study_cluster_id));
  }
  for (const row of scored) {
    const category = row.validation_maturity === 0 ? "not_reported" : row.validation_maturity === 1 ? "analytical_or_simulation" : row.validation_maturity === 2 ? "laboratory_or_prototype" : "field_or_deployment";
    add("S5", category, `Validation maturity and benchmark readiness: ${category}`, row.study_id);
  }
  for (const row of scored) {
    const axes = [
      { axis: "technology", rawTokens: splitCodes(row.__master.enabling_technology_codes), normalize: normalizeTechnology, fallbackCategory: "other_enabling_technology", label: "Enabling technology" },
      { axis: "application", rawTokens: splitCodes(row.__master.application_domain_codes), normalize: normalizeApplication, fallbackCategory: "other_application_domain", label: "Application domain" },
    ];
    for (const config of axes) {
      const entries = config.rawTokens.map((rawToken) => ({ rawToken, canonical: config.normalize(rawToken) }));
      const recognizedEntries = entries.filter((entry) => entry.canonical !== config.fallbackCategory);
      const recognizedCategories = [...new Set(recognizedEntries.map((entry) => entry.canonical))].sort();
      const fallbackIncluded = recognizedCategories.length === 0;
      const fallbackBodyId = `S6-${slug(`${config.axis}_${config.fallbackCategory}`)}`;
      if (recognizedCategories.length) {
        for (const entry of recognizedEntries) add("S6", `${config.axis}_${entry.canonical}`, `${config.label}: ${entry.canonical}`, row.study_id, entry.rawToken);
      } else if (entries.length) {
        for (const entry of entries) add("S6", `${config.axis}_${config.fallbackCategory}`, `${config.label}: ${config.fallbackCategory} (mixed/unclassified; non-substantive)`, row.study_id, entry.rawToken);
      } else {
        add("S6", `${config.axis}_${config.fallbackCategory}`, `${config.label}: ${config.fallbackCategory} (mixed/unclassified; non-substantive)`, row.study_id);
      }
      normalizationAudit.push({
        row_type: "axis_summary", section: "S6", study_id: row.study_id, axis: config.axis, record_id: "", raw_token: "", normalized_category: config.fallbackCategory,
        record_eligibility: "study_axis_summary", is_recognized: "NA", body_membership_included: fallbackIncluded ? "yes" : "no",
        recognized_categories_for_study_axis: recognizedCategories.join("|"), recognized_category_count_for_study_axis: recognizedCategories.length,
        eligible_raw_token_count_for_study_axis: entries.length,
        fallback_body_id: fallbackBodyId, fallback_body_included_for_study_axis: fallbackIncluded ? "yes" : "no",
        decision_reason: fallbackIncluded ? "fallback_included_because_no_recognized_category_in_study_axis" : "fallback_suppressed_because_recognized_category_exists_in_study_axis",
      });
      for (const entry of entries) {
        const recognized = entry.canonical !== config.fallbackCategory;
        normalizationAudit.push({
          row_type: "raw_token", section: "S6", study_id: row.study_id, axis: config.axis, record_id: "", raw_token: entry.rawToken, normalized_category: entry.canonical,
          record_eligibility: "eligible", is_recognized: recognized ? "yes" : "no", body_membership_included: (recognized || fallbackIncluded) ? "yes" : "no",
          recognized_categories_for_study_axis: recognizedCategories.join("|"), recognized_category_count_for_study_axis: recognizedCategories.length,
          eligible_raw_token_count_for_study_axis: entries.length,
          fallback_body_id: fallbackBodyId, fallback_body_included_for_study_axis: fallbackIncluded ? "yes" : "no",
          decision_reason: recognized ? "recognized_category_included" : fallbackIncluded ? "unmatched_token_supports_study_axis_fallback" : "unmatched_token_audit_only_because_recognized_category_exists",
        });
      }
    }
  }
  for (const row of scored) {
    const combinedGapText = lower([row.__master.author_reported_limitations, row.__master.author_reported_research_gaps, row.__master.missing_data_summary, row.__master.assumptions_summary].join(" "));
    if (row.reporting_completeness <= 1 || row.metric_clarity <= 1) add("S7", "metric_definition_and_reporting", "Research gap: standardized metric definitions and complete reporting", row.study_id);
    if (row.comparison_admissibility <= 1) add("S7", "measurement_plane_and_comparability", "Research gap: measurement-plane harmonization and comparison admissibility", row.study_id);
    if (row.validation_maturity <= 1) add("S7", "field_validation", "Research gap: field validation and deployment evidence", row.study_id);
    if (row.reproducibility <= 1) add("S7", "open_artifacts_and_reproducibility", "Research gap: open datasets, code/models and reproducibility", row.study_id);
    if (row.benchmark_readiness <= 1) add("S7", "common_benchmarks", "Research gap: common baselines and benchmark protocols", row.study_id);
    if (row.technical_relevance <= 1 || /time.?division|sequential|application_scenario/.test(lower(row.__master.integration_mechanism_codes))) add("S7", "concurrent_integration", "Research gap: genuinely concurrent shared-resource O-ISAC integration", row.study_id);
    if (row.__cross.six_g !== "direct") add("S7", "six_g_scalability", "Research gap: explicit 6G scalability and network-level evaluation", row.study_id);
    if (/hardware|power|energy|complex|latency|cost|size|footprint/.test(combinedGapText)) add("S7", "hardware_power_complexity", "Research gap: hardware, power and complexity constraints", row.study_id);
    if (/robust|channel|mobility|weather|turbulence|blockage|misalignment|noise/.test(combinedGapText)) add("S7", "robustness_channel_mobility", "Research gap: channel robustness, mobility and environmental realism", row.study_id);
    if (/ai|machine.?learning|generaliz|security|privacy/.test(combinedGapText)) add("S7", "ai_generalization_security", "Research gap: AI generalization, security and privacy", row.study_id);
  }

  const bodies = [];
  for (const [bodyId, body] of [...bodyMap.entries()].sort(([a], [b]) => a.localeCompare(b))) {
    const studyRows = [...body.studyIds].map((id) => byId.get(id)).filter(Boolean);
    const dimensions = Object.fromEntries(DIMENSIONS.map((dimension) => [dimension, Math.floor(median(studyRows.map((row) => row[dimension]))) ]));
    const overall = Math.floor(median(studyRows.map((row) => row.overall_evidence_contribution)));
    const corePerStudy = studyRows.map((row) => median(DIMENSIONS.map((dimension) => row[dimension])));
    const coreMedian = median(corePerStudy);
    const adequateShare = corePerStudy.length ? corePerStudy.filter((value) => value >= 2).length / corePerStudy.length : 0;
    const modalities = [...new Set(studyRows.map((row) => row.__cross.modality))].sort();
    const nonSubstantiveFallback = /other_(?:communication|sensing)_metric|other_enabling_technology|other_application_domain/.test(body.key);
    let certainty = "unclear";
    if (nonSubstantiveFallback) certainty = "unclear";
    else if (body.section === "S7") {
      certainty = studyRows.length >= 10 && modalities.length >= 3 ? "high" : studyRows.length >= 5 && modalities.length >= 2 ? "moderate" : studyRows.length >= 2 ? "limited" : "unclear";
    } else if (studyRows.length < 3 || coreMedian < 1.5) certainty = "limited";
    else if (studyRows.length >= 5 && coreMedian >= 2.5 && adequateShare >= 0.75) certainty = "high";
    else certainty = "moderate";
    bodies.push({
      evidence_body_id: bodyId,
      evidence_theme: body.theme,
      optical_modality: modalities.join("|") || "unclear",
      number_of_studies: studyRows.length,
      ...dimensions,
      overall_evidence_contribution: overall,
      certainty_summary: certainty,
      notes: JSON.stringify({ section: body.section, deterministic_rule: nonSubstantiveFallback ? "mixed_unclassified_fallback_not_eligible_for_substantive_survey_certainty_conclusion" : body.section === "S7" ? "gap_triangulation_by_study_and_modality" : "floor_of_dimension_medians_with_n_core_median_and_adequate_share_certainty", substantive_for_survey_conclusion: !nonSubstantiveFallback, core_median: Number(coreMedian.toFixed(4)), adequate_share: Number(adequateShare.toFixed(4)), raw_token_unique_count: body.rawTokenCounts.size, raw_token_samples: [...body.rawTokenCounts.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0])).slice(0, 20).map(([token, count]) => ({ token, count })), contributing_study_ids: studyRows.map((row) => row.study_id).sort() }),
    });
  }
  return { bodies, normalizationAudit };
}

function buildSynthesisRows(scored, bodies, sheets) {
  const modalities = [...new Set(scored.map((row) => row.__cross.modality))].sort();
  const sectionBodies = (section) => bodies.filter((body) => body.evidence_body_id.startsWith(`${section}-`));
  const sectionStudies = (section) => new Set(sectionBodies(section).flatMap((body) => JSON.parse(body.notes).contributing_study_ids));
  const common = (section) => ({
    synthesis_id: section,
    contributing_studies: `${sectionStudies(section).size} unique studies; exact IDs in certainty_grade_PHASE_E_DRAFT_2026-08-04.csv`,
    modalities_covered: modalities.join("; "),
  });
  const scoreDist = Object.fromEntries(DIMENSIONS.map((dimension) => [dimension, countBy(scored.map((row) => row[dimension]))]));
  return [
    { ...common("S1"), synthesis_domain: "O-ISAC modality taxonomy", key_metrics: "study counts by canonical optical modality", comparability_status: "descriptive taxonomy", validation_types: "all extracted validation types", main_findings: `${scored.length} studies mapped to ${modalities.length} canonical modalities; body-level counts are in the certainty draft.`, evidence_limitations: "Modality is study-level and does not imply comparable outcome definitions.", roadmap_implications: "Use modality-stratified narrative synthesis." },
    { ...common("S2"), synthesis_domain: "Architecture and integration mechanism synthesis", key_metrics: "shared waveform; hardware; carrier; link/channel; resource allocation; joint design", comparability_status: "descriptive mechanism mapping", validation_types: "all", main_findings: `${sectionBodies("S2").length} normalized mechanism bodies were generated with one-study weighting.`, evidence_limitations: "Co-location or a shared application scenario is not treated as strong shared-resource integration.", roadmap_implications: "Distinguish genuinely concurrent shared-resource designs from boundary cases." },
    { ...common("S3"), synthesis_domain: "Sensing/communication metric reporting map", key_metrics: `${sectionBodies("S3").length} communication/sensing metric-domain-family bodies`, comparability_status: `study-level admissibility score distribution ${JSON.stringify(scoreDist.comparison_admissibility)}`, validation_types: "metric-specific source validation context", main_findings: "Metric bodies retain study, measurement-plane, validation and locator provenance; quarantined claims are excluded.", evidence_limitations: `${sheets.metrics.rows.filter((row) => !clean(row.metric_comparability_class)).length} legacy comparability blanks and ${sheets.metrics.rows.filter((row) => !clean(row.metric_comparison_admissibility_class)).length} admissibility blanks were scored only after explicit insufficient-information resolution.`, roadmap_implications: "Standardize definitions, planes, conditions and units before cross-study comparison." },
    { ...common("S4"), synthesis_domain: "Rate-sensing and rate-resolution tradeoff synthesis", key_metrics: `${sectionBodies("S4").length} normalized tradeoff families from ${sheets.tradeoffs.rows.length} extracted rows`, comparability_status: "claim-gated; no unsupported pooling", validation_types: "tradeoff-row source context", main_findings: "Reported tradeoffs were grouped by axes and objective; quarantined tradeoff claims were excluded from bodies.", evidence_limitations: "Qualitative, partial and heterogeneous axes limit numerical aggregation.", roadmap_implications: "Report Pareto fronts with fixed scenarios and common constraints." },
    { ...common("S5"), synthesis_domain: "Validation maturity and benchmark readiness", key_metrics: "TQAF validation maturity; reproducibility; benchmark readiness", comparability_status: "ordinal deterministic assessment", validation_types: "analytical/simulation; laboratory/prototype; field/deployment", main_findings: `Validation score distribution ${JSON.stringify(scoreDist.validation_maturity)}; benchmark score distribution ${JSON.stringify(scoreDist.benchmark_readiness)}.`, evidence_limitations: "A maximum validation mode does not yield score 3 unless both communication and sensing outcomes have field/deployment evidence.", roadmap_implications: "Prioritize paired-function field validation and open benchmark artifacts." },
    { ...common("S6"), synthesis_domain: "Enabling technologies and application domains", key_metrics: `${sectionBodies("S6").length} technology/application bodies`, comparability_status: "descriptive mapping", validation_types: "all", main_findings: "Enabling technologies and applications were mapped directly from Phase-D study-level codes.", evidence_limitations: "Code granularity is heterogeneous and does not imply causal effectiveness.", roadmap_implications: "Develop modality-aware application benchmarks." },
    { ...common("S7"), synthesis_domain: "Research gaps and 6G roadmap", key_metrics: `${sectionBodies("S7").length} deterministic gap themes`, comparability_status: "triangulated narrative evidence", validation_types: "all", main_findings: "Gap themes combine low TQAF dimensions with author-reported limitations, gaps and assumptions.", evidence_limitations: "Reviewer-derived low-score gaps are separated conceptually from author-origin text; certainty uses study/modality triangulation.", roadmap_implications: "Focus on standardized metrics, common baselines, open artifacts, realistic channels, field validation and explicit 6G scaling." },
  ];
}

function buildLegacyRows(rows) {
  return rows.map((row) => ({
    metric_record_id: clean(row.metric_record_id),
    study_id: clean(row.study_cluster_id),
    source_screening_record_id: clean(row.source_screening_record_id),
    source_locator: locator(row),
    raw_comparability: clean(row.metric_comparability_class),
    raw_admissibility: clean(row.metric_comparison_admissibility_class),
    resolved_comparability: clean(row.metric_comparability_class) || LEGACY_RESOLUTION,
    resolved_admissibility: clean(row.metric_comparison_admissibility_class) || LEGACY_RESOLUTION,
    resolution_reason: LEGACY_RESOLUTION,
  }));
}

function buildQa(data, scoreResult, bodies, legacyAudit, normalizationAudit) {
  const { sourceSha, sheets, crosswalk } = data;
  const { scored, auditRows, quarantineClaims } = scoreResult;
  const scoreFields = [...DIMENSIONS, "overall_evidence_contribution"];
  const qStudyIds = new Set(quarantineClaims.map((row) => clean(row.study_cluster_id)));
  const qMetricStudyIds = new Set(quarantineClaims.filter((row) => clean(row.record_type) === "metric").map((row) => clean(row.study_cluster_id)));
  const qTradeoffStudyIds = new Set(quarantineClaims.filter((row) => clean(row.record_type) === "tradeoff").map((row) => clean(row.study_cluster_id)));
  const byId = new Map(scored.map((row) => [row.study_id, row]));
  const blankComparability = sheets.metrics.rows.filter((row) => !clean(row.metric_comparability_class)).length;
  const blankAdmissibility = sheets.metrics.rows.filter((row) => !clean(row.metric_comparison_admissibility_class)).length;
  const capCounts = {};
  for (const audit of auditRows) for (const cap of splitCodes(audit.cap_codes)) capCounts[cap] = (capCounts[cap] ?? 0) + 1;
  const bodyStudyUnion = (section) => new Set(bodies.filter((row) => row.evidence_body_id.startsWith(`${section}-`)).flatMap((row) => JSON.parse(row.notes).contributing_study_ids));
  const fallbackBodies = bodies.filter((row) => /other_(?:communication|sensing)_metric|other_enabling_technology|other_application_domain/.test(row.evidence_body_id));
  const bodyById = new Map(bodies.map((row) => [row.evidence_body_id, row]));
  const axisSummaries = normalizationAudit.filter((row) => row.row_type === "axis_summary");
  const rawTokenAudits = normalizationAudit.filter((row) => row.row_type === "raw_token");
  const fallbackSpecs = [
    { key: "S3_communication", section: "S3", axis: "communication", bodyId: "S3-communication_other_communication_metric", expected: 2 },
    { key: "S3_sensing", section: "S3", axis: "sensing", bodyId: "S3-sensing_other_sensing_metric", expected: 2 },
    { key: "S6_technology", section: "S6", axis: "technology", bodyId: "S6-technology_other_enabling_technology", expected: 19 },
    { key: "S6_application", section: "S6", axis: "application", bodyId: "S6-application_other_application_domain", expected: 15 },
  ];
  const fallbackMembershipCounts = Object.fromEntries(fallbackSpecs.map((spec) => [spec.key, Number(bodyById.get(spec.bodyId)?.number_of_studies ?? 0)]));
  const fallbackSummarySets = Object.fromEntries(fallbackSpecs.map((spec) => [spec.key, new Set(axisSummaries.filter((row) => row.section === spec.section && row.axis === spec.axis && row.fallback_body_included_for_study_axis === "yes").map((row) => row.study_id))]));
  const fallbackBodySets = Object.fromEntries(fallbackSpecs.map((spec) => [spec.key, new Set(JSON.parse(bodyById.get(spec.bodyId)?.notes ?? '{"contributing_study_ids":[]}').contributing_study_ids)]));
  const sameSet = (a, b) => a.size === b.size && [...a].every((value) => b.has(value));
  const s3CommunicationNoRecognized = axisSummaries.filter((row) => row.section === "S3" && row.axis === "communication" && Number(row.recognized_category_count_for_study_axis) === 0);
  const s3CommunicationNoEligibleToken = s3CommunicationNoRecognized.filter((row) => Number(row.eligible_raw_token_count_for_study_axis) === 0);
  const s3CommunicationEligibleUnmatched = s3CommunicationNoRecognized.filter((row) => Number(row.eligible_raw_token_count_for_study_axis) > 0);
  const checks = {
    source_sha_matches_locked_phase_d: sourceSha === EXPECTED_SOURCE_SHA256,
    source_sha_unchanged_after_scoring: sha256(SOURCE) === EXPECTED_SOURCE_SHA256,
    crosswalk_passed_before_scoring: crosswalk.qa?.pass === true && Number(crosswalk.qa?.unmapped_count) === 0,
    exact_206_study_rows: scored.length === 206,
    study_ids_unique: new Set(scored.map((row) => row.study_id)).size === 206,
    all_master_studies_crosswalked: scored.every((row) => row.__cross && row.__cross.study_cluster_id === row.study_id),
    exact_92_blank_comparability_rows: blankComparability === 92,
    exact_92_blank_admissibility_rows: blankAdmissibility === 92,
    every_legacy_blank_has_explicit_resolution: legacyAudit.length === new Set(sheets.metrics.rows.filter((row) => !clean(row.metric_comparability_class) || !clean(row.metric_comparison_admissibility_class)).map((row) => clean(row.metric_record_id))).size && legacyAudit.every((row) => row.resolution_reason === LEGACY_RESOLUTION && row.resolved_comparability && row.resolved_admissibility),
    exact_72_quarantined_claims: quarantineClaims.length === 72,
    all_scores_integer_0_to_3: scored.every((row) => scoreFields.every((field) => Number.isInteger(row[field]) && row[field] >= 0 && row[field] <= 3)),
    no_blank_final_scores: scored.every((row) => scoreFields.every((field) => row[field] !== null && row[field] !== undefined && row[field] !== "")),
    every_risk_row_has_full_audit_note: scored.every((row) => { try { const parsed = JSON.parse(row.notes); return [...DIMENSIONS, "overall_evidence_contribution"].every((dimension) => parsed.audit?.[dimension]?.inputs && Array.isArray(parsed.audit?.[dimension]?.record_trace)); } catch { return false; } }),
    dimension_audit_has_1854_rows: auditRows.length === 206 * 9,
    quarantined_studies_overall_capped_at_2: [...qStudyIds].every((id) => byId.get(id)?.overall_evidence_contribution <= 2),
    quarantined_studies_record_overall_cap_policy: [...qStudyIds].every((id) => byId.get(id)?.__audits.overall_evidence_contribution.caps.includes("any_quarantined_claim_overall_cap_2")),
    quarantined_metric_or_tradeoff_studies_comparison_capped_at_1: [...new Set([...qMetricStudyIds, ...qTradeoffStudyIds])].every((id) => byId.get(id)?.comparison_admissibility <= 1),
    quarantined_metric_or_tradeoff_studies_record_comparison_cap_policy: [...new Set([...qMetricStudyIds, ...qTradeoffStudyIds])].every((id) => byId.get(id)?.__audits.comparison_admissibility.caps.includes("quarantined_metric_or_tradeoff_claim_cap_1")),
    overall_score_3_requires_four_core_dimensions_at_least_2: scored.filter((row) => row.overall_evidence_contribution === 3).every((row) => row.technical_relevance >= 2 && row.metric_clarity >= 2 && row.reporting_completeness >= 2 && row.validation_maturity >= 2),
    low_metric_clarity_and_low_validation_are_overall_capped_at_1: scored.filter((row) => row.metric_clarity <= 1 && row.validation_maturity <= 1).every((row) => row.overall_evidence_contribution <= 1 && row.__audits.overall_evidence_contribution.caps.includes("metric_clarity_1_or_lower_and_validation_1_or_lower_overall_cap_1")),
    absent_author_reported_limitations_cap_limitation_transparency_at_1: scored.filter((row) => row.__audits.limitation_transparency.inputs.L_author_limitations === 0).every((row) => row.limitation_transparency <= 1 && row.__audits.limitation_transparency.caps.includes("author_origin_limitation_required_cap_1")),
    material_quarantined_source_conflicts_cap_limitation_transparency_at_2: [...qStudyIds].every((id) => byId.get(id)?.limitation_transparency <= 2 && byId.get(id)?.__audits.limitation_transparency.caps.includes("material_quarantined_source_conflict_limitation_cap_2")),
    benchmark_score_3_guardrails_hold: scored.filter((row) => row.benchmark_readiness === 3).every((row) => row.__cross.baseline?.canonical === "external_or_common" && Math.max(availabilityValue(row.__cross.dataset_availability) ?? 0, availabilityValue(row.__cross.code_model_availability) ?? 0) === 1 && row.comparison_admissibility === 3 && row.validation_maturity >= 2 && row.reproducibility >= 2 && row.__quarantineCount === 0),
    comparison_score_3_guardrails_hold: scored.filter((row) => row.comparison_admissibility === 3).every((row) => !/descriptive_only|not_allowed|prohibit/i.test(clean(row.__surveyUse.cross_study_comparison_use)) && row.__quarantineCount === 0),
    evidence_body_ids_unique: new Set(bodies.map((row) => row.evidence_body_id)).size === bodies.length,
    evidence_bodies_have_valid_study_counts: bodies.every((row) => row.number_of_studies > 0 && JSON.parse(row.notes).contributing_study_ids.length === row.number_of_studies),
    no_unmapped_study_ids_in_bodies: bodies.every((row) => JSON.parse(row.notes).contributing_study_ids.every((id) => byId.has(id))),
    s3_metric_bodies_cover_all_206_studies: bodyStudyUnion("S3").size === 206,
    s6_technology_application_bodies_cover_all_206_studies: bodyStudyUnion("S6").size === 206,
    mixed_unclassified_fallback_bodies_are_non_substantive_and_unclear: fallbackBodies.length === 4 && fallbackBodies.every((row) => row.certainty_summary === "unclear" && JSON.parse(row.notes).substantive_for_survey_conclusion === false),
    exact_47_s3_metric_bodies_preserved: bodies.filter((row) => row.evidence_body_id.startsWith("S3-")).length === 47,
    exact_31_s6_technology_application_bodies_preserved: bodies.filter((row) => row.evidence_body_id.startsWith("S6-")).length === 31,
    exact_824_study_axis_summary_rows: axisSummaries.length === 206 * 4,
    s3_fallback_included_iff_eligible_unmatched_metric_exists_and_no_recognized_category: axisSummaries.filter((row) => row.section === "S3").every((row) => ((Number(row.recognized_category_count_for_study_axis) === 0 && Number(row.eligible_raw_token_count_for_study_axis) > 0) === (row.fallback_body_included_for_study_axis === "yes"))),
    s6_fallback_included_iff_no_recognized_category_in_study_axis: axisSummaries.filter((row) => row.section === "S6").every((row) => ((Number(row.recognized_category_count_for_study_axis) === 0) === (row.fallback_body_included_for_study_axis === "yes"))),
    unmatched_tokens_with_recognized_category_are_audit_only: rawTokenAudits.filter((row) => row.record_eligibility === "eligible" && row.is_recognized === "no" && Number(row.recognized_category_count_for_study_axis) > 0).every((row) => row.body_membership_included === "no" && /audit_only/.test(row.decision_reason)),
    eligible_recognized_tokens_are_body_members: rawTokenAudits.filter((row) => row.record_eligibility === "eligible" && row.is_recognized === "yes").every((row) => row.body_membership_included === "yes"),
    quarantined_metric_tokens_are_excluded_from_body_membership: rawTokenAudits.filter((row) => row.record_eligibility === "quarantined_excluded").every((row) => row.body_membership_included === "no"),
    exact_fallback_membership_counts_2_2_19_15: fallbackSpecs.every((spec) => fallbackMembershipCounts[spec.key] === spec.expected && fallbackSummarySets[spec.key].size === spec.expected),
    fallback_body_members_exactly_match_no_recognized_axis_summary_sets: fallbackSpecs.every((spec) => sameSet(fallbackBodySets[spec.key], fallbackSummarySets[spec.key])),
    s3_communication_reconciliation_has_8_no_recognized_candidates: s3CommunicationNoRecognized.length === 8,
    s3_communication_reconciliation_excludes_6_no_token_candidates: s3CommunicationNoEligibleToken.length === 6 && s3CommunicationNoEligibleToken.every((row) => row.fallback_body_included_for_study_axis === "no" && /no_eligible_metric_token/.test(row.decision_reason)),
    s3_communication_reconciliation_includes_2_eligible_unmatched_candidates: s3CommunicationEligibleUnmatched.length === 2 && s3CommunicationEligibleUnmatched.every((row) => row.fallback_body_included_for_study_axis === "yes"),
  };
  return {
    report_id: "PHASE_E_TQAF_QA_DRAFT_2026-08-04",
    generated_at: new Date().toISOString(),
    method_version: METHOD_VERSION,
    source: { workbook: SOURCE, sha256: sourceSha, crosswalk: CROSSWALK_PATH, crosswalk_sha256: sha256(CROSSWALK_PATH) },
    input_counts: { studies: sheets.master.rows.length, evidence_items: sheets.evidence.rows.length, metric_results: sheets.metrics.rows.length, tradeoff_rows: sheets.tradeoffs.rows.length, claim_ledger_rows: sheets.ledger.rows.length, conflict_rows: sheets.conflicts.rows.length, survey_use_rows: sheets.surveyUse.rows.length },
    output_counts: { risk_rows: scored.length, dimension_audit_rows: auditRows.length, body_normalization_audit_rows: normalizationAudit.length, legacy_resolution_rows: legacyAudit.length, evidence_body_rows: bodies.length },
    legacy_blank_resolution: { exact_label: LEGACY_RESOLUTION, comparability_blank_rows: blankComparability, admissibility_blank_rows: blankAdmissibility, affected_studies: [...new Set(legacyAudit.map((row) => row.study_id))].sort() },
    quarantine: { claim_count: quarantineClaims.length, study_count: qStudyIds.size, by_record_type: countBy(quarantineClaims.map((row) => clean(row.record_type))), study_ids: [...qStudyIds].sort() },
    score_distributions: Object.fromEntries(scoreFields.map((field) => [field, countBy(scored.map((row) => row[field]))])),
    certainty_distributions: countBy(bodies.map((row) => row.certainty_summary)),
    evidence_body_counts_by_section: countBy(bodies.map((row) => row.evidence_body_id.split("-")[0])),
    fallback_membership_counts: fallbackMembershipCounts,
    fallback_reconciliation: {
      s3_communication_no_recognized_candidate_studies: s3CommunicationNoRecognized.map((row) => row.study_id).sort(),
      s3_communication_excluded_no_eligible_token_studies: s3CommunicationNoEligibleToken.map((row) => row.study_id).sort(),
      s3_communication_included_eligible_unmatched_studies: s3CommunicationEligibleUnmatched.map((row) => row.study_id).sort(),
      included_raw_tokens: rawTokenAudits.filter((row) => row.section === "S3" && row.axis === "communication" && s3CommunicationEligibleUnmatched.some((summary) => summary.study_id === row.study_id)).map((row) => ({ study_id: row.study_id, record_id: row.record_id, raw_token: row.raw_token, normalized_category: row.normalized_category, record_eligibility: row.record_eligibility, body_membership_included: row.body_membership_included })),
    },
    cap_counts: capCounts,
    checks,
    pass: Object.values(checks).every(Boolean),
  };
}

function writeOutputs(data, scoreResult, bodies, synthesisRows, legacyAudit, normalizationAudit, qa) {
  const riskHeaders = ["study_id", "citation", ...DIMENSIONS, "overall_evidence_contribution", "notes"];
  writeCsv(OUTPUTS.risk, riskHeaders, scoreResult.scored);
  writeCsv(OUTPUTS.audit, ["study_id", "citation", "dimension", "score_before_cap", "score_final", "cap_codes", "inputs_json", "record_trace_json", "method_version", "source_workbook_sha256"], scoreResult.auditRows);
  writeCsv(OUTPUTS.bodyNormalizationAudit, ["row_type", "section", "study_id", "axis", "record_id", "raw_token", "normalized_category", "record_eligibility", "is_recognized", "body_membership_included", "recognized_categories_for_study_axis", "recognized_category_count_for_study_axis", "eligible_raw_token_count_for_study_axis", "fallback_body_id", "fallback_body_included_for_study_axis", "decision_reason"], normalizationAudit);
  writeCsv(OUTPUTS.legacy, ["metric_record_id", "study_id", "source_screening_record_id", "source_locator", "raw_comparability", "raw_admissibility", "resolved_comparability", "resolved_admissibility", "resolution_reason"], legacyAudit);
  writeCsv(OUTPUTS.certainty, ["evidence_body_id", "evidence_theme", "optical_modality", "number_of_studies", ...DIMENSIONS, "overall_evidence_contribution", "certainty_summary", "notes"], bodies);
  writeCsv(OUTPUTS.synthesis, ["synthesis_id", "synthesis_domain", "contributing_studies", "modalities_covered", "key_metrics", "comparability_status", "validation_types", "main_findings", "evidence_limitations", "roadmap_implications"], synthesisRows);
  fs.writeFileSync(OUTPUTS.qa, `${JSON.stringify(qa, null, 2)}\n`, "utf8");
  const lines = [
    "# Phase-E TQAF deterministic draft — 2026-08-04",
    "",
    `- Source workbook: \`${path.basename(SOURCE)}\``,
    `- Locked source SHA-256: \`${data.sourceSha}\``,
    `- Method: \`${METHOD_VERSION}\``,
    `- Study rows: ${qa.output_counts.risk_rows} (one row per unique study cluster).`,
    `- Evidence bodies: ${qa.output_counts.evidence_body_rows} across S1–S7.`,
    `- Body-normalization audit rows: ${qa.output_counts.body_normalization_audit_rows}; fallback memberships S3 communication=${qa.fallback_membership_counts.S3_communication}, S3 sensing=${qa.fallback_membership_counts.S3_sensing}, S6 technology=${qa.fallback_membership_counts.S6_technology}, S6 application=${qa.fallback_membership_counts.S6_application}.`,
    `- Quarantined claims: ${qa.quarantine.claim_count} in ${qa.quarantine.study_count} studies; type-specific caps applied.`,
    `- Legacy blank resolution: ${qa.legacy_blank_resolution.comparability_blank_rows} comparability and ${qa.legacy_blank_resolution.admissibility_blank_rows} admissibility blanks explicitly mapped to \`${LEGACY_RESOLUTION}\`.`,
    `- QA: **${qa.pass ? "PASS" : "FAIL"}** (${Object.values(qa.checks).filter(Boolean).length}/${Object.keys(qa.checks).length} checks).`,
    "",
    "## Deterministic scoring method",
    "",
    "Eight study-level dimensions use the protocol-locked 0–3 scale (0 insufficient, 1 weak/incomplete, 2 adequate, 3 strong/benchmark-ready). Composite indicators use fixed thresholds: <0.25=0, 0.25–<0.50=1, 0.50–<0.80=2, >=0.80=3. Overall contribution uses the arithmetic mean of the eight final dimension scores (<0.75=0, <1.50=1, <2.25=2, otherwise 3), followed by source-conflict and core-relevance caps.",
    "",
    "Metric clarity requires both communication and sensing outcome rows and evaluates source reporting, family/definition, measurement plane, validation/scenario context, operational value/unit, and unresolved conflict status. Validation score 3 requires field/deployment evidence for both functions. Reproducibility score 3 requires complete/substantial parameters and open data or code/model. Benchmark score 3 requires an external/common baseline, an open artifact, direct admissibility, adequate validation/reproducibility, and no quarantined claim. Comparison score 3 requires directly comparable/admissible outcomes in both domains.",
    "",
    "Quarantined metric/tradeoff claims cap comparison admissibility at 1; affected quantitative dimensions are capped at 2; any quarantined claim caps overall contribution at 2. Quarantined records remain in the audit trace and are excluded from evidence-body claim aggregation.",
    "",
    "## Score distributions",
    "",
    "```json",
    JSON.stringify(qa.score_distributions, null, 2),
    "```",
    "",
    "## Outputs",
    "",
    ...Object.values(OUTPUTS).map((filePath) => `- \`${path.basename(filePath)}\``),
    "",
    "These are temporary Phase-E drafts. No canonical workbook or canonical CSV was modified.",
  ];
  fs.writeFileSync(OUTPUTS.summary, `${lines.join("\n")}\n`, "utf8");
}

async function inspect() {
  const data = await loadData();
  const output = Object.fromEntries(Object.entries(data.sheets).map(([key, sheet]) => [key, { sheet: sheet.name, row_count: sheet.rows.length, headers: sheet.headers }]));
  process.stdout.write(`${JSON.stringify(output, null, 2)}\n`);
}

async function build() {
  const data = await loadData();
  const scoreResult = buildStudyScores(data);
  const legacyAudit = buildLegacyRows(scoreResult.legacyRows);
  const bodyResult = buildEvidenceBodies(scoreResult.scored, data.sheets, scoreResult.quarantineClaims);
  const bodies = bodyResult.bodies;
  const normalizationAudit = bodyResult.normalizationAudit;
  const synthesisRows = buildSynthesisRows(scoreResult.scored, bodies, data.sheets);
  const qa = buildQa(data, scoreResult, bodies, legacyAudit, normalizationAudit);
  writeOutputs(data, scoreResult, bodies, synthesisRows, legacyAudit, normalizationAudit, qa);
  const result = { pass: qa.pass, outputs: OUTPUTS, counts: qa.output_counts, score_distributions: qa.score_distributions, certainty_distributions: qa.certainty_distributions, failed_checks: Object.entries(qa.checks).filter(([, pass]) => !pass).map(([name]) => name) };
  process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
  if (!qa.pass) process.exitCode = 2;
}

async function main() {
  if (!fs.existsSync(SOURCE)) throw new Error(`Missing source workbook: ${SOURCE}`);
  if (!fs.existsSync(CROSSWALK_PATH)) throw new Error(`Missing crosswalk: ${CROSSWALK_PATH}`);
  const command = process.argv[2] ?? "--build";
  if (command === "--inspect") return inspect();
  if (command === "--build") return build();
  throw new Error(`Unsupported command: ${command}`);
}

main().catch((error) => {
  process.stderr.write(`${error.stack ?? error.message}\n`);
  process.exitCode = 1;
});
