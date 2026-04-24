param(
    [string]$ZoteroDir = (Join-Path $env:USERPROFILE "Zotero"),
    [string]$PaperDirectory,
    [string]$ManifestPath,
    [int]$Limit = 0,
    [switch]$UseBackup
)

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
if (-not $PaperDirectory) {
    $PaperDirectory = Join-Path $ProjectRoot "data\\papers"
}
if (-not $ManifestPath) {
    $ManifestPath = Join-Path $ProjectRoot "data\\zotero-import-manifest.json"
}

$Python = "python"
$VenvPython = Join-Path $ProjectRoot ".venv\\Scripts\\python.exe"

if (Test-Path $VenvPython) {
    $Python = $VenvPython
}

$Args = @(
    (Join-Path $ProjectRoot "scripts\\import-zotero.py"),
    "--zotero-dir", $ZoteroDir,
    "--paper-directory", $PaperDirectory,
    "--manifest-path", $ManifestPath
)

if ($Limit -gt 0) {
    $Args += @("--limit", "$Limit")
}

if ($UseBackup) {
    $Args += "--use-backup"
}

& $Python @Args
exit $LASTEXITCODE
