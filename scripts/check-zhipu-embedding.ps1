param(
    [string]$Model,
    [int]$Dimensions = 0,
    [string]$InputText = "embedding connectivity test"
)

$ErrorActionPreference = "Stop"

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$ArgsList = @("zhipu-embedding", "--input", $InputText)
if ($Model) {
    $ArgsList += @("--model", $Model)
}
if ($Dimensions -gt 0) {
    $ArgsList += @("--dimensions", $Dimensions)
}

python (Join-Path $ProjectRoot "scripts\check-providers.py") @ArgsList
exit $LASTEXITCODE
