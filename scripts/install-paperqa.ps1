param(
    [string]$PackageSpec = "paper-qa>=5"
)

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$PackagesDir = Join-Path $ProjectRoot ".packages"
$TmpDir = Join-Path $ProjectRoot "tmp"

New-Item -ItemType Directory -Force $PackagesDir | Out-Null
New-Item -ItemType Directory -Force $TmpDir | Out-Null

$env:TEMP = $TmpDir
$env:TMP = $TmpDir

python -m pip install --upgrade --target $PackagesDir $PackageSpec
