param(
    [string]$ProjectRoot = "F:\shuixin code\zotero-paperqa-assistant",
    [string]$Model = "deepseek/deepseek-v4-pro",
    [string]$RunId = ""
)

$ErrorActionPreference = "Continue"

Set-Location $ProjectRoot

$logDir = Join-Path $ProjectRoot "logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$checkpointRunId = if ($RunId.Trim()) { $RunId.Trim() } else { $stamp }
$outLog = Join-Path $logDir "wiki-pro-aggregate-$stamp.out.log"
$errLog = Join-Path $logDir "wiki-pro-aggregate-$stamp.err.log"
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) { $pythonCmd = Get-Command python3 -ErrorAction SilentlyContinue }
$python = if ($pythonCmd) { $pythonCmd.Source } else { "python" }
$pythonHome = if ($pythonCmd) { Split-Path -Parent $pythonCmd.Source } else { "" }

try {
    "START $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') model=$Model aggregate-only checkpoint=$checkpointRunId python=$python" | Out-File -FilePath $outLog -Encoding utf8

    if ($pythonHome) {
        $env:Path = "$pythonHome;$pythonHome\Scripts;$pythonHome\Library\bin;$env:SystemRoot\System32;$env:SystemRoot;$env:SystemRoot\System32\WindowsPowerShell\v1.0"
    }
    $pkg = Join-Path $ProjectRoot ".packages"
    $scripts = Join-Path $ProjectRoot "scripts"
    $env:PYTHONPATH = $pkg + [System.IO.Path]::PathSeparator + $ProjectRoot + [System.IO.Path]::PathSeparator + $scripts
    $env:PYTHONUTF8 = "1"
    $env:PQA_LLM_MODEL = $Model
    $env:PQA_SUMMARY_LLM_MODEL = $Model
    $env:PQA_AGENT_LLM_MODEL = $Model
    $env:PQA_ENRICHMENT_LLM_MODEL = $Model
    $env:LLM_WIKI_PAPER_TIMEOUT = "900"
    $env:LLM_WIKI_AGGREGATE_TIMEOUT = "1800"
    $env:LLM_WIKI_AGGREGATE_BATCH_CHAR_BUDGET = "700000"
    $env:LLM_WIKI_AGGREGATE_MERGE_CHAR_BUDGET = "700000"
    $env:LLM_WIKI_AGGREGATE_CARD_CHAR_BUDGET = "70000"
    $env:LLM_WIKI_AGGREGATE_MAX_MERGE_ROUNDS = "6"
    $env:LLM_WIKI_AGGREGATE_FINAL_THINKING = "1"
    $env:LLM_WIKI_AGGREGATE_FINAL_REASONING_EFFORT = "max"
    $env:LLM_WIKI_AGGREGATE_FINAL_MAX_TOKENS = "65536"
    $env:LLM_WIKI_BATCH_MAX_CONCEPTS = "80"
    $env:LLM_WIKI_BATCH_MAX_METHODS = "80"
    $env:LLM_WIKI_BATCH_MAX_CLAIMS = "140"
    $env:LLM_WIKI_BATCH_MAX_SYNTHESES = "40"
    $env:LLM_WIKI_BATCH_MAX_OPEN_QUESTIONS = "35"
    $env:LLM_WIKI_MAX_CONCEPTS = "160"
    $env:LLM_WIKI_MAX_METHODS = "160"
    $env:LLM_WIKI_MAX_CLAIMS = "320"
    $env:LLM_WIKI_MAX_SYNTHESES = "120"
    $env:LLM_WIKI_MAX_OPEN_QUESTIONS = "90"
    $env:LLM_WIKI_AGGREGATE_RUN_ID = $checkpointRunId
    $env:DEEPSEEK_RETRY_ATTEMPTS = "3"

    $pythonCommand = "`"$python`" `".\scripts\wiki_compile.py`" ingest --index-name papers --aggregate-only 1>> `"$outLog`" 2>> `"$errLog`""
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
