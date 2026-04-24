@echo off
setlocal
cd /d "%~dp0"
set PYTHONUTF8=1
python -m streamlit run app.py --server.headless true --server.port 8501 --browser.gatherUsageStats false
