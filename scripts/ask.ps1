param(
    [Parameter(Mandatory = $true)]
    [string]$Question,
    [string]$IndexName = "papers",
    [string]$PaperDirectory,
    [string]$IndexDirectory,
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ExtraArgs
)

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
if (-not $PaperDirectory) {
    $PaperDirectory = Join-Path $ProjectRoot "data\\papers"
}
if (-not $IndexDirectory) {
    $IndexDirectory = Join-Path $ProjectRoot "data\\indexes"
}

& (Join-Path $ProjectRoot "scripts\\pqa.ps1") `
    "--index" $IndexName `
    "--agent.index.paper_directory" $PaperDirectory `
    "--agent.index.index_directory" $IndexDirectory `
    "ask" `
    $Question `
    @ExtraArgs

exit $LASTEXITCODE
