$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

$prepScript = Join-Path $root "prepare_oisac_template_body.ps1"
powershell -ExecutionPolicy Bypass -File $prepScript

if ($LASTEXITCODE -ne 0) {
    throw "Template body preparation failed with exit code $LASTEXITCODE"
}

$passes = 2
$jobName = "oisac_review_working_build"

for ($pass = 1; $pass -le $passes; $pass++) {
    Write-Host "pdflatex pass $pass/$passes"
    pdflatex --shell-escape -interaction=nonstopmode -halt-on-error -jobname="$jobName" oisac_review_working.tex

    if ($LASTEXITCODE -ne 0) {
        throw "pdflatex failed on pass $pass with exit code $LASTEXITCODE"
    }
}

Write-Host "Build output: $root\\$jobName.pdf"
