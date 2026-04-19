$src  = 'c:\Users\fdonmez\Documents\githubRepos\manuscript\finalShortened'
$dest = "$src\manuscript_submission.zip"
$tmp  = "$env:TEMP\manuscript_sub_tmp"

if (Test-Path $dest) { Remove-Item $dest }
if (Test-Path $tmp)  { Remove-Item $tmp -Recurse -Force }

New-Item -ItemType Directory -Path $tmp | Out-Null
New-Item -ItemType Directory -Path "$tmp\figures" | Out-Null

Copy-Item "$src\bare_jrnl_new_sample4.tex" "$tmp\"
Copy-Item "$src\references.bib"             "$tmp\"
Copy-Item "$src\IEEEtran.cls"               "$tmp\"
Copy-Item "$src\bare_jrnl_new_sample4.bbl"  "$tmp\"

Get-ChildItem "$src\figures" |
    Where-Object { $_.Name -notmatch '_eski|_esk' } |
    ForEach-Object { Copy-Item $_.FullName "$tmp\figures\" }

Compress-Archive -Path "$tmp\*" -DestinationPath $dest -Force
Remove-Item $tmp -Recurse -Force

$f = Get-Item $dest
Write-Host "ZIP olusturuldu:" $f.FullName
Write-Host "Boyut:" ([math]::Round($f.Length / 1MB, 2)) "MB"
