param(
    [Parameter(Mandatory = $true)]
    [string]$Question,
    [string]$IndexName = "papers",
    [ValidateSet("auto", "always", "never")]
    [string]$Knowledge = "auto",
    [ValidateSet("text", "json")]
    [string]$Format = "text",
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ExtraArgs
)

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Python = "python"
$VenvPython = Join-Path $ProjectRoot ".venv\Scripts\python.exe"

if (Test-Path $VenvPython) {
    $Python = $VenvPython
}

$env:PYTHONUTF8 = "1"
& $Python `
    (Join-Path $ProjectRoot "scripts\pqa-api.py") `
    "chat" `
    "--index-name" $IndexName `
    "--knowledge" $Knowledge `
    "--format" $Format `
    $Question `
    @ExtraArgs

exit $LASTEXITCODE
