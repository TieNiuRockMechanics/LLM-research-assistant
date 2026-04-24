param(
    [string]$Model = "kimi-k2.5",
    [string]$Prompt = "请只回答 ok"
)

$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$DotEnvPath = Join-Path $ProjectRoot ".env"
$PackagesDir = Join-Path $ProjectRoot ".packages"

if (-not (Test-Path $DotEnvPath)) {
    throw "Missing .env. Copy .env.example to .env first."
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

    $key = $parts[0].Trim()
    $value = $parts[1].Trim()

    if (($value.StartsWith('"') -and $value.EndsWith('"')) -or ($value.StartsWith("'") -and $value.EndsWith("'"))) {
        $value = $value.Substring(1, $value.Length - 2)
    }

    [System.Environment]::SetEnvironmentVariable($key, $value, "Process")
}

if (-not $env:OPENAI_API_KEY -and $env:MOONSHOT_API_KEY) {
    $env:OPENAI_API_KEY = $env:MOONSHOT_API_KEY
}

if (-not $env:OPENAI_BASE_URL -and $env:MOONSHOT_API_KEY) {
    $env:OPENAI_BASE_URL = "https://api.moonshot.cn/v1"
}

$env:PYTHONPATH = $PackagesDir

python -c "from openai import OpenAI; import os; client=OpenAI(api_key=os.environ['OPENAI_API_KEY'], base_url=os.environ['OPENAI_BASE_URL']); resp=client.chat.completions.create(model='$Model', messages=[{'role':'user','content':'$Prompt'}]); print(resp.choices[0].message.content)"
