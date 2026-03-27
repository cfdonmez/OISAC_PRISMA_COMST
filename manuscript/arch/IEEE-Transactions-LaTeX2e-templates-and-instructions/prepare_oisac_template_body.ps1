$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$localSource = Join-Path $root "OISAC_COMST_review_body.md"
$canonicalSource = Join-Path $root "..\current_bundle\OISAC_COMST_review_body.md"
$source = if (Test-Path $localSource) { $localSource } else { $canonicalSource }
$target = Join-Path $root "oisac_review_template_body.md"
$remainingTarget = Join-Path $root "oisac_review_remaining_body.md"

$text = Get-Content -Raw -Encoding UTF8 -Path $source

# Remove BOM artifacts that break markdown heading detection after bundle merges.
$text = $text -replace [string][char]0xFEFF, ""

# Remove the Introduction-local reference block so Section II follows Section I
# directly in the template draft. The canonical bundle stays untouched.
$text = [regex]::Replace(
    $text,
    '(?ms)^# REFERENCES\s*\r?\n.*?(?=^# II\. TECHNICAL FUNDAMENTALS OF O-ISAC\b)',
    ""
)

# Table labels should read like captions in the draft, not as heading nodes.
$text = [regex]::Replace(
    $text,
    '(?m)^### (Table [^\r\n]+)$',
    '**$1**'
)

# Replace symbol-heavy table markers with ASCII-safe words for the draft build.
function Get-Mojibake([int]$codepoint) {
    $symbol = [string][char]$codepoint
    return [System.Text.Encoding]::GetEncoding(1252).GetString(
        [System.Text.Encoding]::UTF8.GetBytes($symbol)
    )
}

$replacements = @(
    @{ From = (Get-Mojibake 0x25CF); To = "Full" }
    @{ From = [string][char]0x25CF; To = "Full" }
    @{ From = (Get-Mojibake 0x25D0); To = "Part" }
    @{ From = [string][char]0x25D0; To = "Part" }
    @{ From = (Get-Mojibake 0x25CB); To = "Out" }
    @{ From = [string][char]0x25CB; To = "Out" }
    @{ From = (Get-Mojibake 0x2013); To = "-" }
    @{ From = [string][char]0x2013; To = "-" }
    @{ From = (Get-Mojibake 0x2014); To = "-" }
    @{ From = [string][char]0x2014; To = "-" }
)

foreach ($entry in $replacements) {
    $text = $text.Replace($entry.From, $entry.To)
}

# Keep corpus identifiers visible but markdown-safe in the template draft.
$text = [regex]::Replace(
    $text,
    '\[O_ISAC_([0-9]+)(:[0-9]+)?\]',
    {
        param($match)
        return "O-ISAC-$($match.Groups[1].Value)$($match.Groups[2].Value)"
    }
)

# Strip inline strong markers from pipe-table rows to keep markdown table parsing stable.
$lines = $text -split '\r?\n'
for ($i = 0; $i -lt $lines.Length; $i++) {
    if ($lines[$i].TrimStart().StartsWith('|')) {
        $lines[$i] = $lines[$i] -replace '\*\*', ''
    }
}
$text = [string]::Join("`r`n", $lines)

# Keep spacing stable after block removal.
$text = [regex]::Replace($text, '(\r?\n){3,}', "`r`n`r`n")

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($target, $text, $utf8NoBom)

$remainingMatch = [regex]::Match(
    $text,
    '(?ms)^# II\. TECHNICAL FUNDAMENTALS OF O-ISAC\b.*$'
)

if (-not $remainingMatch.Success) {
    throw "Could not isolate Section II onward for staged native LaTeX migration."
}

[System.IO.File]::WriteAllText($remainingTarget, $remainingMatch.Value, $utf8NoBom)

Write-Host "Prepared template body: $target"
Write-Host "Prepared remaining body: $remainingTarget"
Write-Host "Source body: $source"
