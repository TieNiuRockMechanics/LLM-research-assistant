param(
    [string]$Model,
    [string]$Prompt = "Reply with ok only."
)

$ErrorActionPreference = "Stop"

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$ArgsList = @("deepseek-chat", "--prompt", $Prompt)
if ($Model) {
    $ArgsList += @("--model", $Model)
}

python (Join-Path $ProjectRoot "scripts\check-providers.py") @ArgsList
exit $LASTEXITCODE
