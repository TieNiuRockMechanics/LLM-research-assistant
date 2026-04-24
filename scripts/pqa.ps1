param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$PqaArgs
)

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$PackagesDir = Join-Path $ProjectRoot ".packages"
$DotEnvPath = Join-Path $ProjectRoot ".env"
$TmpDir = Join-Path $ProjectRoot "tmp"
$PqaHome = Join-Path $ProjectRoot ".pqa"

if (-not (Test-Path $PackagesDir)) {
    throw "PaperQA2 is not installed yet. Run .\scripts\install-paperqa.ps1 first."
}

New-Item -ItemType Directory -Force $TmpDir | Out-Null
New-Item -ItemType Directory -Force $PqaHome | Out-Null
New-Item -ItemType Directory -Force (Join-Path $ProjectRoot "data\\papers") | Out-Null
New-Item -ItemType Directory -Force (Join-Path $ProjectRoot "data\\indexes") | Out-Null

if (Test-Path $DotEnvPath) {
    foreach ($line in Get-Content $DotEnvPath) {
        $trimmed = $line.Trim()
        if (-not $trimmed -or $trimmed.StartsWith("#")) {
            continue
        }

        $parts = $trimmed -split "=", 2
        if ($parts.Count -ne 2) {
            continue
        }

        $key = $parts[0].Trim()
        $value = $parts[1].Trim()

        if (($value.StartsWith('"') -and $value.EndsWith('"')) -or ($value.StartsWith("'") -and $value.EndsWith("'"))) {
            $value = $value.Substring(1, $value.Length - 2)
        }

        [System.Environment]::SetEnvironmentVariable($key, $value, "Process")
    }
}

$joinedArgs = ($PqaArgs -join " ")

if (-not $env:OPENAI_API_KEY -and $env:MOONSHOT_API_KEY) {
    $env:OPENAI_API_KEY = $env:MOONSHOT_API_KEY
}

if (-not $env:OPENAI_BASE_URL -and $env:MOONSHOT_API_KEY) {
    $env:OPENAI_BASE_URL = "https://api.moonshot.cn/v1"
}

if (-not $env:DASHSCOPE_API_KEY -and $env:OPENAI_API_KEY -and $env:OPENAI_BASE_URL -like "*dashscope.aliyuncs.com*") {
    $env:DASHSCOPE_API_KEY = $env:OPENAI_API_KEY
}

if (-not $env:DASHSCOPE_API_BASE -and $env:OPENAI_BASE_URL -like "*dashscope.aliyuncs.com*") {
    $env:DASHSCOPE_API_BASE = $env:OPENAI_BASE_URL
}

$env:PYTHONPATH = $PackagesDir
$env:TEMP = $TmpDir
$env:TMP = $TmpDir
$env:PQA_HOME = $PqaHome

$defaultArgs = @()
if ($env:PQA_LLM_MODEL) {
    $defaultArgs += @("--llm", $env:PQA_LLM_MODEL)
}
if ($env:PQA_LLM_CONFIG_JSON) {
    $defaultArgs += @("--llm_config", $env:PQA_LLM_CONFIG_JSON)
}
if ($env:PQA_AGENT_LLM_MODEL) {
    $defaultArgs += @("--agent.agent_llm", $env:PQA_AGENT_LLM_MODEL)
} elseif ($env:PQA_LLM_MODEL) {
    $defaultArgs += @("--agent.agent_llm", $env:PQA_LLM_MODEL)
}
if ($env:PQA_AGENT_LLM_CONFIG_JSON) {
    $defaultArgs += @("--agent.agent_llm_config", $env:PQA_AGENT_LLM_CONFIG_JSON)
} elseif ($env:PQA_LLM_CONFIG_JSON) {
    $defaultArgs += @("--agent.agent_llm_config", $env:PQA_LLM_CONFIG_JSON)
}
if ($env:PQA_SUMMARY_LLM_MODEL) {
    $defaultArgs += @("--summary_llm", $env:PQA_SUMMARY_LLM_MODEL)
}
if ($env:PQA_SUMMARY_LLM_CONFIG_JSON) {
    $defaultArgs += @("--summary_llm_config", $env:PQA_SUMMARY_LLM_CONFIG_JSON)
}
if ($env:PQA_ENRICHMENT_LLM_MODEL) {
    $defaultArgs += @("--parsing.enrichment_llm", $env:PQA_ENRICHMENT_LLM_MODEL)
} elseif ($env:PQA_LLM_MODEL) {
    $defaultArgs += @("--parsing.enrichment_llm", $env:PQA_LLM_MODEL)
}
if ($env:PQA_ENRICHMENT_LLM_CONFIG_JSON) {
    $defaultArgs += @("--parsing.enrichment_llm_config", $env:PQA_ENRICHMENT_LLM_CONFIG_JSON)
} elseif ($env:PQA_LLM_CONFIG_JSON) {
    $defaultArgs += @("--parsing.enrichment_llm_config", $env:PQA_LLM_CONFIG_JSON)
}
if ($env:PQA_EMBEDDING_MODEL) {
    $defaultArgs += @("--embedding", $env:PQA_EMBEDDING_MODEL)
}
if ($env:PQA_EMBEDDING_CONFIG_JSON) {
    $defaultArgs += @("--embedding_config", $env:PQA_EMBEDDING_CONFIG_JSON)
}
if ($env:PQA_EMBEDDING_ENCODING_FORMAT) {
    $defaultArgs += @("--embedding_config.kwargs.encoding_format", $env:PQA_EMBEDDING_ENCODING_FORMAT)
}

$isKimiBaseUrl = $env:OPENAI_BASE_URL -like "*moonshot.cn*"
$needsEmbeddings = $joinedArgs -match "(^| )(index|ask)( |$)"
$hasExplicitEmbeddingConfig = $env:PQA_EMBEDDING_MODEL -or $env:PQA_EMBEDDING_CONFIG_JSON

if ($isKimiBaseUrl -and $needsEmbeddings -and -not $hasExplicitEmbeddingConfig) {
    throw @"
Kimi has been configured as the LLM provider, but no embedding provider is configured.

PaperQA2 needs embeddings for indexing and retrieval.
Kimi's official compatibility docs currently document chat/files endpoints, and its public model list currently shows text-generation models only.

Fastest fix:
1. Keep Kimi for --llm / --summary_llm
2. Add a separate cloud embedding provider through:
   PQA_EMBEDDING_MODEL
   PQA_EMBEDDING_CONFIG_JSON

Example direction:
- PQA_EMBEDDING_MODEL=text-embedding-3-small
- PQA_EMBEDDING_CONFIG_JSON={"model_list":[{"model_name":"text-embedding-3-small","litellm_params":{"model":"text-embedding-3-small","api_key":"YOUR_KEY"}}]}
"@
}

$command = Join-Path $PackagesDir "bin\\pqa.exe"
& $command @defaultArgs @PqaArgs
exit $LASTEXITCODE
