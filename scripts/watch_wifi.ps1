[CmdletBinding()]
param(
    [string]$Ssid = "IMMF_5G",
    [int]$IntervalSeconds = 15,
    [int]$ReconnectWaitSeconds = 8,
    [int]$ConsecutiveFailuresToReconnect = 3,
    [string[]]$CheckHosts = @("223.5.5.5", "114.114.114.114", "1.1.1.1"),
    [switch]$CreateProfileIfMissing,
    [string]$LogPath = ""
)

$ErrorActionPreference = "Stop"

$ScriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
$ProjectRoot = Split-Path -Parent $ScriptDir
if (-not $LogPath) {
    $LogPath = Join-Path $ProjectRoot "logs\wifi-watchdog.log"
}

function Write-Log {
    param([string]$Message)

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $line = "[$timestamp] $Message"
    Write-Host $line

    $logDir = Split-Path -Parent $LogPath
    if ($logDir -and -not (Test-Path -LiteralPath $logDir)) {
        New-Item -ItemType Directory -Path $logDir -Force | Out-Null
    }
    Add-Content -LiteralPath $LogPath -Value $line -Encoding UTF8
}

function Test-Internet {
    foreach ($hostName in $CheckHosts) {
        $null = & ping.exe -n 1 -w 1500 $hostName 2>$null
        if ($LASTEXITCODE -eq 0) {
            return $true
        }
    }
    return $false
}

function Get-ConnectedSsid {
    $output = & netsh.exe wlan show interfaces 2>$null
    if ($LASTEXITCODE -ne 0 -or -not $output) {
        return $null
    }

    foreach ($line in $output) {
        if ($line -match "^\s*SSID\s+:\s*(.+?)\s*$") {
            $value = $Matches[1].Trim()
            if ($value) {
                return $value
            }
        }
    }
    return $null
}

function Test-WifiProfileExists {
    param([string]$ProfileName)

    $profiles = & netsh.exe wlan show profiles 2>$null
    if ($LASTEXITCODE -ne 0 -or -not $profiles) {
        return $false
    }
    return (($profiles -join "`n") -match [regex]::Escape($ProfileName))
}

function Add-WifiProfile {
    param([string]$ProfileName)

    $secure = Read-Host "Windows has no saved profile for '$ProfileName'. Enter Wi-Fi password once" -AsSecureString
    $bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)
    try {
        $plainPassword = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr)
        if (-not $plainPassword) {
            throw "Empty Wi-Fi password."
        }

        $escapedSsid = [System.Security.SecurityElement]::Escape($ProfileName)
        $escapedPassword = [System.Security.SecurityElement]::Escape($plainPassword)
        $profileXml = @"
<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>$escapedSsid</name>
    <SSIDConfig>
        <SSID>
            <name>$escapedSsid</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>$escapedPassword</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>
"@

        $tempProfile = Join-Path $env:TEMP ("wifi-profile-{0}.xml" -f ([guid]::NewGuid().ToString("N")))
        try {
            Set-Content -LiteralPath $tempProfile -Value $profileXml -Encoding UTF8
            $output = & netsh.exe wlan add profile filename="$tempProfile" user=current 2>&1
            if ($LASTEXITCODE -ne 0) {
                throw "netsh wlan add profile failed: $($output -join ' ')"
            }
            Write-Log "Created Windows Wi-Fi profile for '$ProfileName'."
        }
        finally {
            Remove-Item -LiteralPath $tempProfile -Force -ErrorAction SilentlyContinue
        }
    }
    finally {
        if ($bstr -ne [IntPtr]::Zero) {
            [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)
        }
        Remove-Variable plainPassword -ErrorAction SilentlyContinue
        Remove-Variable escapedPassword -ErrorAction SilentlyContinue
        Remove-Variable profileXml -ErrorAction SilentlyContinue
    }
}

function Connect-TargetWifi {
    param([string]$ProfileName)

    if (-not (Test-WifiProfileExists -ProfileName $ProfileName)) {
        if ($CreateProfileIfMissing) {
            Add-WifiProfile -ProfileName $ProfileName
        }
        else {
            Write-Log "No saved Windows Wi-Fi profile for '$ProfileName'. Run once with -CreateProfileIfMissing."
            return $false
        }
    }

    Write-Log "Attempting to connect Wi-Fi '$ProfileName'."
    $output = & netsh.exe wlan connect name="$ProfileName" ssid="$ProfileName" 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Log "Connect command failed: $($output -join ' ')"
        return $false
    }

    Start-Sleep -Seconds $ReconnectWaitSeconds
    return $true
}

$failureCount = 0
Write-Log "Wi-Fi watchdog started. Target SSID='$Ssid', interval=${IntervalSeconds}s, reconnect_after_failures=$ConsecutiveFailuresToReconnect, log='$LogPath'."

while ($true) {
    try {
        $connectedSsid = Get-ConnectedSsid
        $internetOk = Test-Internet

        if ($connectedSsid -eq $Ssid -and $internetOk) {
            $failureCount = 0
            Write-Log "OK: connected to '$Ssid' and internet check passed."
        }
        else {
            $ssidText = if ($connectedSsid) { $connectedSsid } else { "<not connected>" }
            $failureCount += 1
            Write-Log "Network problem ${failureCount}/${ConsecutiveFailuresToReconnect}: current SSID='$ssidText', internet_ok=$internetOk."
            if (($connectedSsid -ne $Ssid) -or ($failureCount -ge $ConsecutiveFailuresToReconnect)) {
                $null = Connect-TargetWifi -ProfileName $Ssid
                $failureCount = 0
            }
        }
    }
    catch {
        Write-Log "ERROR: $($_.Exception.Message)"
    }

    Start-Sleep -Seconds $IntervalSeconds
}
