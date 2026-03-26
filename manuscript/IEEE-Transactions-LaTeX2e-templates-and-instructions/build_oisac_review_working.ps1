$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

$jobNameBase = "oisac_review_working_build"
$jobName = "{0}_{1}" -f $jobNameBase, (Get-Date -Format "yyyyMMdd_HHmmss")
$bblPath = Join-Path $root "$jobName.bbl"
$blgPath = Join-Path $root "$jobName.blg"

# Remove stale bibliography outputs so the first pdflatex pass cannot be blocked
# by an older malformed .bbl file.
if (Test-Path $bblPath) {
    Remove-Item $bblPath -Force
}
if (Test-Path $blgPath) {
    Remove-Item $blgPath -Force
}

Write-Host "pdflatex pass 1/3"
pdflatex --shell-escape -interaction=nonstopmode -halt-on-error -jobname="$jobName" oisac_review_working.tex

if ($LASTEXITCODE -ne 0) {
    throw "pdflatex failed on pass 1 with exit code $LASTEXITCODE"
}

Write-Host "bibtex pass"
bibtex "$jobName"

if ($LASTEXITCODE -ne 0) {
    throw "bibtex failed with exit code $LASTEXITCODE"
}

for ($pass = 2; $pass -le 3; $pass++) {
    Write-Host "pdflatex pass $pass/3"
    pdflatex --shell-escape -interaction=nonstopmode -halt-on-error -jobname="$jobName" oisac_review_working.tex

    if ($LASTEXITCODE -ne 0) {
        throw "pdflatex failed on pass $pass with exit code $LASTEXITCODE"
    }
}

Write-Host "Build output: $root\\$jobName.pdf"
