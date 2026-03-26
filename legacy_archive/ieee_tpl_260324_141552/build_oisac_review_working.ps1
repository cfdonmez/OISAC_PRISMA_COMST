$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

pdflatex --shell-escape -interaction=nonstopmode -halt-on-error oisac_review_working.tex
