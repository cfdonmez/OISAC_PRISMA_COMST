$ErrorActionPreference = 'Stop'

$manuscriptRoot = Split-Path -Parent $PSScriptRoot
$projectRoot = [System.IO.Path]::GetFullPath((Join-Path $manuscriptRoot '..\..\..\..\..\..'))
$supplementRoot = Join-Path $manuscriptRoot 'supplements'
$packageName = 'submission_supplement_final_v10_2026-08-17'
$packageRoot = Join-Path $projectRoot $packageName
$zipPath = Join-Path $projectRoot 'OISAC_COMST_SUPPLEMENT_FINAL_V10_2026-08-17.zip'

# Keep the standalone ST-01 source bundle synchronized with the governed
# manuscript bibliography before hashing and packaging.
Copy-Item -LiteralPath (Join-Path $manuscriptRoot 'references_206_candidate.bib') `
    -Destination (Join-Path $supplementRoot 'st01\ST01_REFERENCES_206.bib') -Force

if (Test-Path -LiteralPath $zipPath) {
    throw "Package archive already exists: $zipPath"
}

$relativeFiles = @(
    'README.md',
    'st01\README.md',
    'st01\ST01_INCLUDED_STUDIES_206.csv',
    'st01\ST01_INCLUDED_STUDIES_206.tex',
    'st01\ST01_INCLUDED_STUDIES_206.xlsx',
    'st01\ST01_ELIGIBLE_REPORT_LINEAGE_227.csv',
    'st01\ST01_COMPANION_REPORT_PROVENANCE_21.csv',
    'st01\ST01_COMPANION_REPORT_PROVENANCE_21.tex',
    'st01\ST01_COMPANION_GUARDRAIL_METRICS_14.csv',
    'st01\INCLUDED_STUDIES_206_EXPLICIT_BIBLIOGRAPHY.tex',
    'st01\ST01_SUPPLEMENT_DRIVER.tex',
    'st01\ST01_SUPPLEMENT_DRIVER.pdf',
    'st01\ST01_REFERENCES_206.bib',
    'st01\ST01_REFERENCES_227.bib',
    'evidence\README.md',
    'evidence\ST-16B_EXCLUDED_REPORTS_39_FOR_REPORTING.csv',
    'evidence\ST-18_STUDY_LEVEL_TQAF_206.csv',
    'evidence\ST-19_GOVERNED_TRADEOFFS_404.csv',
    'evidence\ST-19_PRIMARY_EVIDENCE_RESULTS_3020.csv',
    'evidence\ST-19_PRIMARY_METRIC_RESULTS_4779.csv',
    'evidence\ST-19_SUBSTANTIVE_TRADEOFFS_402.csv',
    'evidence\ST-22_EVIDENCE_BODY_CERTAINTY_115.csv',
    'evidence\ST-22_EVIDENCE_BODY_MEMBERSHIP_4931.csv',
    's7\README.md',
    's7\S7_CANONICAL_JOIN_206.csv',
    's7\S7_PAIRED_FUNCTION_VALIDATION_12.csv',
    's7\S7_PAIRED_FUNCTION_VALIDATION_12.xlsx',
    'reporting\README.md',
    'reporting\MANIFEST.json',
    'reporting\S_DATA_DICTIONARY_446.csv',
    'reporting\S_PROTOCOL_DEVIATIONS_2026-08-13.csv',
    'reporting\S_REVIEW_CONDUCT_AND_REPORTING_BOUNDARIES.md',
    'reporting\protocol\contextual_synthesis_positioning_update_2026-08-13.md',
    'reporting\protocol\contextual_synthesis_reporting_disposition_2026-08-17.md',
    'reporting\protocol\protocol_amendment_actual_workflow_2026-08-04.md',
    'reporting\protocol\protocol_initial_2026-06-17.md',
    'reporting\protocol\protocol_registration_lineage_correction_2026-08-07.md',
    'reporting\search\README.md',
    'reporting\search\FINAL_SEARCH_EXECUTION_AND_STRATEGIES_FOR_REPORTING_2026-08-14.csv',
    'reporting\search\FINAL_SEARCH_METHODS_AND_EXECUTION_FOR_REPORTING_2026-08-14.md'
)

function Get-Role([string]$relativePath) {
    if ($relativePath -eq 'README.md') { return 'package_readme' }
    if ($relativePath.StartsWith('st01\')) { return 'included_study_and_report_lineage' }
    if ($relativePath.StartsWith('evidence\')) { return 'governed_evidence_and_appraisal' }
    if ($relativePath.StartsWith('s7\')) { return 'paired_function_validation' }
    if ($relativePath.StartsWith('reporting\protocol\')) { return 'protocol_and_amendment' }
    if ($relativePath.StartsWith('reporting\search\')) { return 'executed_search_record' }
    if ($relativePath.StartsWith('reporting\')) { return 'reporting_contract' }
    return 'other'
}

$records = foreach ($relativePath in $relativeFiles) {
    $sourcePath = Join-Path $supplementRoot $relativePath
    if (-not (Test-Path -LiteralPath $sourcePath -PathType Leaf)) {
        throw "Missing allowlisted file: $sourcePath"
    }
    $item = Get-Item -LiteralPath $sourcePath
    $hash = (Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash.ToLowerInvariant()
    [pscustomobject]@{
        relative_path = $relativePath.Replace('\', '/')
        role = Get-Role $relativePath
        bytes = $item.Length
        sha256 = $hash
    }
}

$packingList = Join-Path $supplementRoot 'SUPPLEMENT_PACKING_LIST_2026-08-17.csv'
$hashList = Join-Path $supplementRoot 'SUPPLEMENT_SHA256_2026-08-17.txt'
$records | Export-Csv -LiteralPath $packingList -NoTypeInformation -Encoding utf8
$hashLines = $records | ForEach-Object { "$($_.sha256) *$($_.relative_path)" }
[System.IO.File]::WriteAllLines($hashList, $hashLines, [System.Text.UTF8Encoding]::new($false))

New-Item -ItemType Directory -Path $packageRoot -Force | Out-Null
foreach ($relativePath in $relativeFiles) {
    $sourcePath = Join-Path $supplementRoot $relativePath
    $destinationPath = Join-Path $packageRoot $relativePath
    $destinationDirectory = Split-Path -Parent $destinationPath
    New-Item -ItemType Directory -Path $destinationDirectory -Force | Out-Null
    Copy-Item -LiteralPath $sourcePath -Destination $destinationPath -Force
}
Copy-Item -LiteralPath $packingList -Destination (Join-Path $packageRoot (Split-Path -Leaf $packingList)) -Force
Copy-Item -LiteralPath $hashList -Destination (Join-Path $packageRoot (Split-Path -Leaf $hashList)) -Force

Compress-Archive -Path (Join-Path $packageRoot '*') -DestinationPath $zipPath -CompressionLevel Optimal

$copiedRecords = foreach ($record in $records) {
    $copiedPath = Join-Path $packageRoot ($record.relative_path.Replace('/', '\'))
    $copiedHash = (Get-FileHash -LiteralPath $copiedPath -Algorithm SHA256).Hash.ToLowerInvariant()
    [pscustomobject]@{
        relative_path = $record.relative_path
        hash_matches = ($copiedHash -eq $record.sha256)
    }
}
if ($copiedRecords.hash_matches -contains $false) {
    throw 'A copied supplement file failed SHA-256 verification.'
}

[pscustomobject]@{
    status = 'PASS'
    file_count = $records.Count
    package_directory = $packageRoot
    zip_path = $zipPath
    zip_sha256 = (Get-FileHash -LiteralPath $zipPath -Algorithm SHA256).Hash.ToLowerInvariant()
} | ConvertTo-Json
