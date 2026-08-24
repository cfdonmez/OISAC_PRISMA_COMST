$ErrorActionPreference = 'Stop'

$manuscriptRoot = Split-Path -Parent $PSScriptRoot
$evidenceRoot = Join-Path $manuscriptRoot 'supplements\evidence'
$sourcePath = Join-Path $evidenceRoot 'ST-16B_EXCLUDED_REPORTS_39.csv'
$outputPath = Join-Path $evidenceRoot 'ST-16B_EXCLUDED_REPORTS_39_FOR_REPORTING.csv'

$source = Import-Csv -LiteralPath $sourcePath
if ($source.Count -ne 39) {
    throw "Expected 39 excluded reports, found $($source.Count)."
}

$projection = $source | Select-Object `
    screening_record_id, `
    report_id, `
    citation, `
    title, `
    authors, `
    year, `
    source_title, `
    doi, `
    exclusion_code, `
    exclusion_reason, `
    decision_date, `
    qa_status, `
    record_lock_status, `
    citation_token

$projection | Export-Csv -LiteralPath $outputPath -NoTypeInformation -Encoding utf8

$reloaded = Import-Csv -LiteralPath $outputPath
$uniqueReports = @($reloaded.report_id | Sort-Object -Unique).Count
$missingReasons = @($reloaded | Where-Object {
    [string]::IsNullOrWhiteSpace($_.exclusion_code) -or
    [string]::IsNullOrWhiteSpace($_.exclusion_reason)
}).Count
if ($reloaded.Count -ne 39 -or $uniqueReports -ne 39 -or $missingReasons -ne 0) {
    throw "Excluded-report projection failed QA: rows=$($reloaded.Count), unique=$uniqueReports, missingReasons=$missingReasons."
}

[pscustomobject]@{
    status = 'PASS'
    rows = $reloaded.Count
    unique_reports = $uniqueReports
    missing_reason_fields = $missingReasons
    output = $outputPath
} | ConvertTo-Json
