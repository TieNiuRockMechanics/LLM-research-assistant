param(
    [string]$PackageSpec = "paper-qa>=5"
)

$ErrorActionPreference = "Stop"

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$PackagesDir = Join-Path $ProjectRoot ".packages"
$TmpDir = Join-Path $ProjectRoot "tmp"
$PipSupportDir = Join-Path $ProjectRoot "scripts\_pip_sitecustomize"

New-Item -ItemType Directory -Force $PackagesDir | Out-Null
New-Item -ItemType Directory -Force $TmpDir | Out-Null

$env:TEMP = $TmpDir
$env:TMP = $TmpDir
$env:PIP_NO_CACHE_DIR = "1"
$env:PYTHONPATH = if ($env:PYTHONPATH) { "$PipSupportDir;$env:PYTHONPATH" } else { $PipSupportDir }

python -m pip install --upgrade --target $PackagesDir $PackageSpec
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
