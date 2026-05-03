param(
    [string]$ZoteroDir = (Join-Path $env:USERPROFILE "Zotero"),
    [string]$PaperDirectory,
    [string]$ManifestPath,
    [int]$Limit = 10,
    [switch]$UseBackup
)

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
if (-not $PaperDirectory) {
    $PaperDirectory = Join-Path $ProjectRoot "data\papers"
}
if (-not $ManifestPath) {
    $ManifestPath = Join-Path $ProjectRoot "data\zotero-import-manifest.json"
}

$ImportScript = Join-Path $ProjectRoot "scripts\import-zotero.ps1"

if ($UseBackup) {
    & $ImportScript -ZoteroDir $ZoteroDir -PaperDirectory $PaperDirectory -ManifestPath $ManifestPath -Limit $Limit -UseBackup
} else {
    & $ImportScript -ZoteroDir $ZoteroDir -PaperDirectory $PaperDirectory -ManifestPath $ManifestPath -Limit $Limit
}

exit $LASTEXITCODE
