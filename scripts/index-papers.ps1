param(
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

New-Item -ItemType Directory -Force $PaperDirectory | Out-Null
New-Item -ItemType Directory -Force $IndexDirectory | Out-Null

& (Join-Path $ProjectRoot "scripts\\pqa.ps1") `
    "--index" $IndexName `
    "--agent.index.paper_directory" $PaperDirectory `
    "--agent.index.index_directory" $IndexDirectory `
    "--agent.index.concurrency" "1" `
    "--parsing.multimodal" "false" `
    "--parsing.use_doc_details" "false" `
    "index" `
    $PaperDirectory `
    @ExtraArgs

exit $LASTEXITCODE
