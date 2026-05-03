@echo off
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\watch_wifi.ps1" -Ssid "IMMF_5G" -IntervalSeconds 15 -ReconnectWaitSeconds 8 -ConsecutiveFailuresToReconnect 3 -CreateProfileIfMissing
pause
