param(
    [string]$ProjectRoot = "F:\shuixin code\zotero-paperqa-assistant",
    [string]$Model = "deepseek/deepseek-v4-pro",
    [string]$RunId = "",
    [int]$Limit = 0
)

$ErrorActionPreference = "Continue"
Set-Location $ProjectRoot

$logDir = Join-Path $ProjectRoot "logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$paperRunId = if ($RunId.Trim()) { $RunId.Trim() } else { "paper-pro-resume-$stamp" }
$outLog = Join-Path $logDir "wiki-pro-papers-$paperRunId.out.log"
$errLog = Join-Path $logDir "wiki-pro-papers-$paperRunId.err.log"
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    $pythonCmd = Get-Command python3 -ErrorAction SilentlyContinue
}
$python = if ($pythonCmd) { $pythonCmd.Source } else { "python" }
$pythonHome = if ($pythonCmd) { Split-Path -Parent $pythonCmd.Source } else { "" }

try {
    "START $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') model=$Model paper-pages run_id=$paperRunId python=$python" | Out-File -FilePath $outLog -Encoding utf8

    $env:Path = if ($pythonHome) {
        "$pythonHome;$pythonHome\Scripts;$pythonHome\Library\bin;$env:SystemRoot\System32;$env:SystemRoot;$env:SystemRoot\System32\WindowsPowerShell\v1.0"
    } else {
        $env:Path
    }
    $pkg = Join-Path $ProjectRoot ".packages"
    $scripts = Join-Path $ProjectRoot "scripts"
    $env:PYTHONPATH = $pkg + [System.IO.Path]::PathSeparator + $ProjectRoot + [System.IO.Path]::PathSeparator + $scripts
    $env:PYTHONUTF8 = "1"
    $env:PYTHONIOENCODING = "utf-8"
    $env:PQA_LLM_MODEL = $Model
    $env:PQA_SUMMARY_LLM_MODEL = $Model
    $env:PQA_AGENT_LLM_MODEL = $Model
    $env:PQA_ENRICHMENT_LLM_MODEL = $Model
    $env:LLM_WIKI_RUN_ID = $paperRunId
    $env:LLM_WIKI_ALLOWED_ITEM_TYPES = "journalArticle"
    $env:LLM_WIKI_PAPER_SINGLE_PASS_CHAR_BUDGET = "320000"
    $env:LLM_WIKI_PAPER_SINGLE_PASS_TIMEOUT = "1200"
    $env:LLM_WIKI_MAX_CONSECUTIVE_FAILURES = "3"
    $env:DEEPSEEK_RETRY_ATTEMPTS = "3"

    $args = @("`"$python`"", "`".\scripts\wiki_compile.py`"", "ingest", "--index-name", "papers", "--no-aggregate", "--force", "--resume")
    if ($Limit -gt 0) {
        $args += @("--limit", "$Limit")
    }
    $pythonCommand = ($args -join " ") + " 1>> `"$outLog`" 2>> `"$errLog`""
    & cmd.exe /d /c $pythonCommand
    $code = $LASTEXITCODE
    "END $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') exit=$code" | Out-File -FilePath $outLog -Encoding utf8 -Append
    exit $code
}
catch {
    $_ | Out-File -FilePath $errLog -Encoding utf8 -Append
    "END $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') exit=1" | Out-File -FilePath $outLog -Encoding utf8 -Append
    exit 1
}
