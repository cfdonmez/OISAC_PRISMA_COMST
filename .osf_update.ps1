# OSF File Update Script - updates existing files via Waterbutler API
# Reads token from .env

$envFile = Join-Path $PSScriptRoot ".env"
$envVars = @{}
Get-Content $envFile | ForEach-Object {
    if ($_ -match '^\s*([^#][^=]+)=(.+)$') {
        $envVars[$matches[1].Trim()] = $matches[2].Trim()
    }
}
$token = $envVars["OSF_TOKEN"]
$nodeId = $envVars["OSF_PROJECT_ID"]
$baseDir = $PSScriptRoot
$wbBase = "https://files.osf.io/v1/resources/$nodeId/providers/osfstorage"

function Get-FileUploadUrl {
    param([string]$folderPath)
    $url = "${wbBase}${folderPath}"
    try {
        $listing = Invoke-RestMethod -Uri "$url" -Headers @{"Authorization" = "Bearer $token" } -Method Get
        $fileMap = @{}
        foreach ($item in $listing.data) {
            if ($item.attributes.kind -eq "file") {
                $fileMap[$item.attributes.name] = $item.links.upload
            }
        }
        return $fileMap
    }
    catch {
        return @{}
    }
}

function Upload-OrUpdate {
    param([string]$localPath, [string]$folderPath, [string]$fileName)
    Write-Host "  $fileName ..." -NoNewline
    
    # First try to find existing file and update it
    $fileMap = Get-FileUploadUrl -folderPath $folderPath
    $fileBytes = [System.IO.File]::ReadAllBytes($localPath)
    
    try {
        if ($fileMap.ContainsKey($fileName)) {
            # Update existing file
            $updateUrl = $fileMap[$fileName]
            $null = Invoke-RestMethod -Uri $updateUrl -Headers @{"Authorization" = "Bearer $token" } -Method Put -Body $fileBytes -ContentType "application/octet-stream"
            Write-Host " UPDATED" -ForegroundColor Green
        }
        else {
            # Upload new file
            $uploadUrl = "${wbBase}${folderPath}?kind=file&name=${fileName}"
            $null = Invoke-RestMethod -Uri $uploadUrl -Headers @{"Authorization" = "Bearer $token" } -Method Put -Body $fileBytes -ContentType "application/octet-stream"
            Write-Host " NEW" -ForegroundColor Green
        }
        return $true
    }
    catch {
        Write-Host " FAIL: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Get folder paths
Write-Host "=== Listing OSF Storage ===" -ForegroundColor Cyan
$listing = Invoke-RestMethod -Uri "$wbBase/?meta=" -Headers @{"Authorization" = "Bearer $token" } -Method Get
$fp = @{}
foreach ($item in $listing.data) {
    if ($item.attributes.kind -eq "folder") {
        $fp[$item.attributes.name] = $item.attributes.path
    }
}

$ok = 0; $fail = 0

# Only update the 3 changed files
Write-Host "`n=== Updating changed files ===" -ForegroundColor Cyan

# osf_registration_pack.md (protocol/)
if (Upload-OrUpdate (Join-Path $baseDir "protocol\osf_registration_pack.md") $fp["protocol"] "osf_registration_pack.md") { $ok++ } else { $fail++ }

# section_03_methodology.md (drafts/)
if (Upload-OrUpdate (Join-Path $baseDir "drafts\section_03_methodology.md") $fp["drafts"] "section_03_methodology.md") { $ok++ } else { $fail++ }

# README.md (root)
if (Upload-OrUpdate (Join-Path $baseDir "README.md") "/" "README.md") { $ok++ } else { $fail++ }

Write-Host "`n=== SUMMARY: $ok OK / $fail FAIL ===" -ForegroundColor $(if ($fail -eq 0) { "Green" }else { "Red" })
