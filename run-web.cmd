@echo off
setlocal
cd /d "%~dp0"

echo === Starting Research Assistant ===
echo.

echo [1/2] Starting API backend (port 12556)...
start "API Backend" /min cmd /c "python server.py"
timeout /t 3 /nobreak >nul

echo [2/2] Starting React frontend (port 5173)...
cd web
start "React Frontend" /min cmd /c "npm run dev"
timeout /t 2 /nobreak >nul

echo.
echo === Ready ===
echo   Frontend: http://localhost:5173
echo   Backend:  http://127.0.0.1:12556
echo.
echo Close this window and the two service windows to stop.
echo.

start "" "http://localhost:5173"
pause
