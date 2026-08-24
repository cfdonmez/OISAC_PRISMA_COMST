$ErrorActionPreference = 'Stop'

$manuscriptRoot = Split-Path -Parent $PSScriptRoot
$outputRoot = Join-Path $manuscriptRoot 'supplements\reporting\search'

function New-SearchRow {
    param(
        [string]$Source,
        [string]$Role,
        [string]$RunId,
        [string]$HistoricalLabel,
        [string]$Query,
        [string]$QueryStatus,
        [string]$Filters,
        [int]$Rows,
        [string]$ExportFile,
        [string]$Format,
        [string]$Notes
    )
    [pscustomobject]@{
        source = $Source
        source_role = $Role
        reporting_run_id = $RunId
        historical_execution_label = $HistoricalLabel
        execution_date = '2026-06-22'
        query_string = $Query
        query_status = $QueryStatus
        filters_and_limits = $Filters
        on_screen_record_count = 'NR_not_recorded_at_execution'
        exported_row_count = $Rows
        canonical_export_file = $ExportFile
        export_format = $Format
        notes = $Notes
    }
}

$coreFiltersScopus = '2020-2026; English intended/applied in interface; Article, Conference Paper, and Review intended'
$coreFiltersIeee = '2020-2026; Journals and Conferences; English if available'
$suppFilters = '2020-2026; English if available; journal articles and reviews where the platform exposed type filters'

$rows = @(
    New-SearchRow 'Scopus' 'core' 'SCO-01' 'SCO-FINAL-S1A' 'TITLE-ABS-KEY("O-ISAC" OR OISAC OR "optical ISAC" OR "optical integrated sensing and communication" OR "integrated optical sensing and communication" OR "joint optical communication and sensing" OR "optical joint communication and sensing")' 'reconstructed_from_final_search_package' $coreFiltersScopus 41 'SCO-FINAL-S1A_export_2026-06-22.csv' 'CSV' 'Exact phrase search.'
    New-SearchRow 'Scopus' 'core' 'SCO-02' 'SCO-FINAL-S1B' 'TITLE-ABS-KEY(("integrated sensing and communication" OR "integrated sensing and communications" OR ISAC OR "joint sensing and communication" OR "joint communication and sensing" OR "sensing-communication" OR "communication-sensing") AND (optical OR photonic OR "free-space optical" OR FSO OR "optical wireless" OR OWC OR VLC OR LiFi OR "visible light communication" OR "visible light communications" OR "optical camera communication" OR OCC OR fiber OR fibre OR "fiber optic" OR "fibre optic" OR "optical fiber" OR "optical fibre" OR "photonic THz" OR "photonic terahertz" OR "photonic mmWave" OR "photonic millimeter wave" OR "THz-over-fiber" OR "terahertz-over-fiber" OR "microwave photonic" OR "microwave photonics"))' 'reconstructed_from_final_search_package' $coreFiltersScopus 1128 'SCO-FINAL-S1B_export_2026-06-22.csv' 'CSV' 'Broad high recall search; screening noise expected.'
    New-SearchRow 'Scopus' 'core' 'SCO-03' 'SCO-FINAL-S1F' 'TITLE-ABS-KEY(("photonic THz" OR "photonic terahertz" OR "photonic mmWave" OR "photonic millimeter wave" OR "microwave photonic" OR "microwave photonics" OR "THz-over-fiber" OR "terahertz-over-fiber" OR "photonics-assisted" OR "photonic-assisted" OR "photonic-aided") AND ("integrated sensing and communication" OR "integrated sensing and communications" OR ISAC OR "joint radar communication" OR "joint radar-communication" OR "joint radar and communication" OR "joint communication and radar" OR "joint sensing and communication" OR "joint communication and sensing"))' 'reconstructed_from_final_search_package' $coreFiltersScopus 104 'SCO-FINAL-S1F_export_2026-06-22.csv' 'CSV' 'Photonics enabled millimeter wave and terahertz search.'
    New-SearchRow 'IEEE Xplore' 'core' 'IEEE-01' 'IEEE-FINAL-S1A' '"All Metadata":"O-ISAC" OR "All Metadata":OISAC OR "All Metadata":"optical ISAC" OR "All Metadata":"optical integrated sensing and communication" OR "All Metadata":"integrated optical sensing and communication" OR "All Metadata":"joint optical communication and sensing" OR "All Metadata":"optical joint communication and sensing"' 'reconstructed_from_recorded_pilot_query_used_for_final_run' $coreFiltersIeee 31 'IEEE-FINAL-S1A_export_2026-06-22.csv' 'CSV' 'Exact phrase search.'
    New-SearchRow 'IEEE Xplore' 'core' 'IEEE-02' 'IEEE-FINAL-S1B' '("Document Title":"integrated sensing and communication" OR "Document Title":"integrated sensing and communications" OR "Document Title":ISAC OR "Document Title":"joint sensing and communication" OR "Document Title":"joint communication and sensing" OR "Document Title":"sensing-communication" OR "Document Title":"communication-sensing" OR "Abstract":"integrated sensing and communication" OR "Abstract":"integrated sensing and communications" OR "Abstract":ISAC OR "Abstract":"joint sensing and communication" OR "Abstract":"joint communication and sensing" OR "Abstract":"sensing-communication" OR "Abstract":"communication-sensing") AND ("Document Title":optical OR "Document Title":photonic OR "Document Title":"free-space optical" OR "Document Title":FSO OR "Document Title":VLC OR "Document Title":LiFi OR "Document Title":"visible light communication" OR "Document Title":"optical wireless" OR "Document Title":"optical fiber" OR "Document Title":"photonic THz" OR "Abstract":optical OR "Abstract":photonic OR "Abstract":"free-space optical" OR "Abstract":FSO OR "Abstract":VLC OR "Abstract":LiFi OR "Abstract":"visible light communication" OR "Abstract":"optical wireless" OR "Abstract":"optical fiber" OR "Abstract":"photonic THz")' 'reconstructed_from_recorded_pilot_query_used_for_final_run' $coreFiltersIeee 252 'IEEE-FINAL-S1B_export_2026-06-22.csv' 'CSV' 'Broad high recall search; screening noise expected.'
    New-SearchRow 'IEEE Xplore' 'core' 'IEEE-03' 'IEEE-FINAL-S1F' '("Document Title":"photonic THz" OR "Document Title":"photonic terahertz" OR "Document Title":"photonic mmWave" OR "Document Title":"photonic millimeter wave" OR "Document Title":"microwave photonic" OR "Document Title":"THz-over-fiber" OR "Document Title":"photonics-assisted" OR "Document Title":"photonic-assisted" OR "Document Title":"photonic-aided" OR "Abstract":"photonic THz" OR "Abstract":"photonic terahertz" OR "Abstract":"photonic mmWave" OR "Abstract":"photonic millimeter wave" OR "Abstract":"microwave photonic" OR "Abstract":"THz-over-fiber" OR "Abstract":"photonics-assisted" OR "Abstract":"photonic-assisted" OR "Abstract":"photonic-aided") AND ("Document Title":"integrated sensing and communication" OR "Document Title":"integrated sensing and communications" OR "Document Title":ISAC OR "Document Title":"joint radar communication" OR "Document Title":"joint radar-communication" OR "Document Title":"joint radar and communication" OR "Document Title":"joint communication and radar" OR "Abstract":"integrated sensing and communication" OR "Abstract":"integrated sensing and communications" OR "Abstract":ISAC)' 'reconstructed_from_recorded_pilot_query_used_for_final_run' $coreFiltersIeee 46 'IEEE-FINAL-S1F_export_2026-06-22.csv' 'CSV' 'Photonics enabled millimeter wave and terahertz search.'
    New-SearchRow 'ScienceDirect' 'supplementary' 'SD-01' 'SD-FINAL-P1' '"optical integrated sensing and communication" OR "optical ISAC" OR "O-ISAC" OR OISAC' 'recorded_in_final_source_summary' $suppFilters 9 'SD-FINAL-P1_export_2026-06-22.txt' 'TXT' 'Exact phrase search.'
    New-SearchRow 'ScienceDirect' 'supplementary' 'SD-02' 'SD-FINAL-P2D' '("integrated sensing and communication" OR ISAC) AND ("photonic THz" OR "photonic terahertz" OR "THz-over-fiber")' 'recorded_in_final_source_summary' $suppFilters 5 'SD-FINAL-P2D_export_2026-06-22.txt' 'TXT' 'Focused terahertz search.'
    New-SearchRow 'ScienceDirect' 'supplementary' 'SD-03' 'SD-FINAL-P2E' '(ISAC OR "joint radar and communication") AND ("photonic-assisted" OR "photonics-assisted" OR "microwave photonic")' 'recorded_in_final_source_summary' $suppFilters 10 'SD-FINAL-P2E_export_2026-06-22.txt' 'TXT' 'Focused microwave photonics search.'
    New-SearchRow 'SpringerLink' 'supplementary' 'SPR-01' 'SPR-FINAL-P1B' '"optical ISAC" OR "O-ISAC"' 'recorded_in_final_source_summary' $suppFilters 4 'SPR-FINAL-P1B_export_2026-06-22.csv' 'CSV' 'Exact phrase search.'
    New-SearchRow 'SpringerLink' 'supplementary' 'SPR-02' 'SPR-FINAL-P2C' '("integrated sensing and communication" OR ISAC) AND ("optical fiber" OR "fiber optic")' 'recorded_in_final_source_summary' $suppFilters 58 'SPR-FINAL-P2C_export_2026-06-22.csv' 'CSV' 'Focused fiber search.'
    New-SearchRow 'SpringerLink' 'supplementary' 'SPR-03' 'SPR-FINAL-P2D' '("integrated sensing and communication" OR ISAC) AND ("photonic THz" OR "photonic terahertz" OR "THz-over-fiber")' 'recorded_in_final_source_summary' $suppFilters 1 'SPR-FINAL-P2D_export_2026-06-22.csv' 'CSV' 'Focused terahertz search.'
    New-SearchRow 'SpringerLink' 'supplementary' 'SPR-04' 'SPR-FINAL-P2E' '(ISAC OR "joint radar and communication") AND ("photonic-assisted" OR "microwave photonic")' 'recorded_in_final_source_summary' $suppFilters 12 'SPR-FINAL-P2E_export_2026-06-22.csv' 'CSV' 'Focused microwave photonics search.'
    New-SearchRow 'Wiley Online Library' 'supplementary' 'WLY-01' 'WLY-FINAL-P1B' '"optical ISAC" OR "O-ISAC" OR OISAC' 'recorded_in_final_source_summary' $suppFilters 5 'WLY-FINAL-P1B_export_2026-06-22.bib' 'BibTeX' 'Exact phrase search.'
    New-SearchRow 'Wiley Online Library' 'supplementary' 'WLY-02' 'WLY-FINAL-P2C' '("integrated sensing and communication" OR ISAC) AND ("optical fiber" OR "fiber optic")' 'recorded_in_final_source_summary' $suppFilters 19 'WLY-FINAL-P2C_export_2026-06-22.bib' 'BibTeX' 'Focused fiber search.'
    New-SearchRow 'Wiley Online Library' 'supplementary' 'WLY-03' 'WLY-FINAL-P2D' '("integrated sensing and communication" OR ISAC) AND ("photonic THz" OR "photonic terahertz" OR "THz-over-fiber")' 'recorded_in_final_source_summary' $suppFilters 3 'WLY-FINAL-P2D_export_2026-06-22.bib' 'BibTeX' 'Focused terahertz search.'
    New-SearchRow 'Wiley Online Library' 'supplementary' 'WLY-04' 'WLY-FINAL-P2E' '(ISAC OR "joint radar and communication") AND ("photonic-assisted" OR "microwave photonic")' 'recorded_in_final_source_summary' $suppFilters 2 'WLY-FINAL-P2E_export_2026-06-22.bib' 'BibTeX' 'Focused microwave photonics search.'
    New-SearchRow 'Taylor & Francis Online' 'supplementary_low_yield' 'TF-01' 'TF-FINAL-MAPPING-PENDING-1' 'NR_query_to_export_mapping_unavailable' 'NR_query_to_export_mapping_unavailable' '2020-2026; Article; English if available' 1 'TF-FINAL-MAPPING-PENDING-1_export_2026-06-22.bib' 'BibTeX' 'The export is retained, but the executed query could not be reconstructed; no query was invented.'
    New-SearchRow 'Taylor & Francis Online' 'supplementary_low_yield' 'TF-02' 'TF-FINAL-MAPPING-PENDING-2' 'NR_query_to_export_mapping_unavailable' 'NR_query_to_export_mapping_unavailable' '2020-2026; Article; English if available' 2 'TF-FINAL-MAPPING-PENDING-2_export_2026-06-22.bib' 'BibTeX' 'The export is retained, but the executed query could not be reconstructed; no query was invented.'
)

if ($rows.Count -ne 19) { throw "Expected 19 executed search rows, found $($rows.Count)." }
$total = ($rows | Measure-Object -Property exported_row_count -Sum).Sum
if ($total -ne 1733) { throw "Expected 1,733 exported rows, found $total." }

$csvPath = Join-Path $outputRoot 'FINAL_SEARCH_EXECUTION_AND_STRATEGIES_FOR_REPORTING_2026-08-14.csv'
$rows | Export-Csv -LiteralPath $csvPath -NoTypeInformation -Encoding utf8

$sourceCounts = $rows | Group-Object source | ForEach-Object {
    [pscustomobject]@{
        source = $_.Name
        runs = $_.Count
        exported_rows = ($_.Group | Measure-Object exported_row_count -Sum).Sum
    }
}

$summaryLines = @(
    '# Final Search Methods and Execution Record',
    '',
    '## Reporting status',
    '',
    'This is the publication-facing search record for the O-ISAC survey. It replaces draft-era status wording in the historical execution notes; it does not overwrite those historical files. All searches were executed on 22 June 2026. The six source totals sum to the 1,733 records reported in the manuscript.',
    '',
    '| Source | Executed runs | Exported rows |',
    '|---|---:|---:|'
)
foreach ($item in $sourceCounts) {
    $summaryLines += "| $($item.source) | $($item.runs) | $($item.exported_rows) |"
}
$summaryLines += @(
    '| **Total** | **19** | **1,733** |',
    '',
    '## Strategy record',
    '',
    'The companion CSV gives one row per executed source query, including the complete available or reconstructed strategy, source limits, export count, and provenance status. Scopus strategies were reconstructed from the frozen final search package. IEEE Xplore strategies were reconstructed from the recorded pilot strings used for the final runs. The ScienceDirect, SpringerLink, and Wiley strings were recorded in their final source summaries. For the two Taylor & Francis exports, the query-to-export mapping was not recorded at execution and could not be reconstructed; the field is therefore reported as `NR_query_to_export_mapping_unavailable` rather than inferred.',
    '',
    'Interface on-screen counts were not recorded for the 19 executions. The CSV reports `NR_not_recorded_at_execution`; exported row counts are the preserved auditable counts. Generic filenames from three supplementary platforms were mapped to query identifiers during the frozen export audit. These mappings are retained as provenance rather than presented as interface-native filenames.',
    '',
    '## Flow and eligibility',
    '',
    'The 1,733 exported rows entered cross-source deduplication and screening. The final flow comprised 1,259 records screened, 330 reports sought, 58 reports not retrieved, 272 full-text reports assessed, 39 full-text exclusions, six contextual reports, and 227 eligible reports mapped to 206 unique studies. Review and survey records used only for field positioning did not enter the 206-study primary evidence denominator.',
    '',
    '## Historical-file boundary',
    '',
    'Earlier source summaries and QA notes remain in the internal audit archive because they document the state of work on 22 June 2026. They contain draft-era phrases such as pending or not yet done and are intentionally excluded from the peer-review upload package. This publication-facing view records the completed state without rewriting the historical audit trail.'
)

$mdPath = Join-Path $outputRoot 'FINAL_SEARCH_METHODS_AND_EXECUTION_FOR_REPORTING_2026-08-14.md'
[System.IO.File]::WriteAllLines($mdPath, $summaryLines, [System.Text.UTF8Encoding]::new($false))

[pscustomobject]@{
    status = 'PASS'
    query_rows = $rows.Count
    exported_rows = $total
    sources = $sourceCounts.Count
    csv = $csvPath
    report = $mdPath
} | ConvertTo-Json
