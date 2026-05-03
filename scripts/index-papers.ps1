param(
    [string]$IndexName = "papers",
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ExtraArgs
)

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$PaperDirectory = Join-Path $ProjectRoot "data\papers"
$IndexDirectory = Join-Path $ProjectRoot "data\indexes"
$Python = "python"
$VenvPython = Join-Path $ProjectRoot ".venv\Scripts\python.exe"

if (Test-Path $VenvPython) {
    $Python = $VenvPython
}

New-Item -ItemType Directory -Force $PaperDirectory | Out-Null
New-Item -ItemType Directory -Force $IndexDirectory | Out-Null

$env:PYTHONUTF8 = "1"
& $Python `
    (Join-Path $ProjectRoot "scripts\pqa-api.py") `
    "index" `
    "--index-name" $IndexName `
    @ExtraArgs

exit $LASTEXITCODE
