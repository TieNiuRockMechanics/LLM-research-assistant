param(
    [Parameter(Mandatory = $true)]
    [string]$Question,
    [string]$IndexName = "papers",
    [ValidateSet("auto", "paper", "chat")]
    [string]$Route = "auto",
    [ValidateSet("direct", "agent")]
    [string]$PaperMode = "direct",
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
    "ask" `
    "--index-name" $IndexName `
    "--route" $Route `
    "--paper-mode" $PaperMode `
    "--format" $Format `
    $Question `
    @ExtraArgs

exit $LASTEXITCODE
