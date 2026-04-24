param(
    [ValidateSet("chat", "embedding", "both")]
    [string]$Mode = "both"
)

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$DotEnvPath = Join-Path $ProjectRoot ".env"

if (-not (Test-Path $DotEnvPath)) {
    throw "Missing .env. The project needs API settings before validation."
}

foreach ($line in Get-Content $DotEnvPath) {
    $trimmed = $line.Trim()
    if (-not $trimmed -or $trimmed.StartsWith("#")) {
        continue
    }

    $parts = $trimmed -split "=", 2
    if ($parts.Count -ne 2) {
        continue
    }

    [System.Environment]::SetEnvironmentVariable($parts[0].Trim(), $parts[1].Trim(), "Process")
}

if (-not $env:OPENAI_API_KEY) {
    throw "OPENAI_API_KEY is missing in .env."
}

if (-not $env:OPENAI_BASE_URL) {
    throw "OPENAI_BASE_URL is missing in .env."
}

$headers = @{
    Authorization = "Bearer $env:OPENAI_API_KEY"
    "Content-Type" = "application/json"
}

if ($Mode -in @("chat", "both")) {
    $chatBody = @{
        model = $env:PQA_LLM_MODEL
        messages = @(
            @{
                role = "user"
                content = "Reply with ok only."
            }
        )
    } | ConvertTo-Json -Depth 6

    $chatResponse = Invoke-RestMethod -Method Post -Uri "$env:OPENAI_BASE_URL/chat/completions" -Headers $headers -Body $chatBody -TimeoutSec 60
    "chat: $($chatResponse.choices[0].message.content)"
}

if ($Mode -in @("embedding", "both")) {
    $embeddingBody = @{
        model = $env:PQA_EMBEDDING_MODEL
        input = "embedding test"
    } | ConvertTo-Json -Depth 4

    $embeddingResponse = Invoke-RestMethod -Method Post -Uri "$env:OPENAI_BASE_URL/embeddings" -Headers $headers -Body $embeddingBody -TimeoutSec 60
    "embedding: $($embeddingResponse.data[0].embedding.Count)"
}
