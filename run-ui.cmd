@echo off
setlocal
cd /d "%~dp0"
set PYTHONUTF8=1
if "%PQA_UI_PORT%"=="" set PQA_UI_PORT=12555
set PQA_UI_URL=http://localhost:%PQA_UI_PORT%

start "Zotero Research Assistant" /min cmd /c python -m streamlit run app.py --server.headless true --server.port %PQA_UI_PORT% --browser.gatherUsageStats false
timeout /t 3 /nobreak >nul
start "" "%PQA_UI_URL%"
