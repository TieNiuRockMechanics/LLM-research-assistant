param(
    [string]$ProjectRoot = "F:\shuixin code\zotero-paperqa-assistant",
    [string]$Model = "deepseek/deepseek-v4-pro",
    [string]$ShardGroup = ""
)

$ErrorActionPreference = "Stop"

Set-Location $ProjectRoot

$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$group = if ($ShardGroup.Trim()) { $ShardGroup.Trim() } else { "paper-pro-sharded-$stamp" }
$script = Join-Path $ProjectRoot "scripts\run_pro_papers_shard.ps1"
$powershell = "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe"
$logDir = Join-Path $ProjectRoot "logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$started = @()

foreach ($index in 0, 1) {
    $argumentLine = (
        "-NoProfile -ExecutionPolicy Bypass " +
        "-File `"$script`" " +
        "-ProjectRoot `"$ProjectRoot`" " +
        "-Model `"$Model`" " +
        "-ShardGroup `"$group`" " +
        "-ShardCount 2 " +
        "-ShardIndex $index"
    )
    $launcherOut = Join-Path $logDir "launcher-$group-shard$index.out.log"
    $launcherErr = Join-Path $logDir "launcher-$group-shard$index.err.log"
    $process = Start-Process `
        -FilePath $powershell `
        -ArgumentList $argumentLine `
        -WindowStyle Hidden `
        -RedirectStandardOutput $launcherOut `
        -RedirectStandardError $launcherErr `
        -PassThru
    $started += $process
    Write-Host "Started shard $index/2 PID=$($process.Id) group=$group"
}

Write-Host "Shard group: $group"
Write-Host "Check progress with: python scripts\wiki_progress.py --format text"
