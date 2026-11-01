@echo off
echo ============================================================
echo Launching NeuroVision Platform (Backend + Frontend)
echo ============================================================
start "NeuroVision Backend" cmd /k "cd /d %~dp0backend && call venv\Scripts\activate.bat && python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload"
start "NeuroVision Frontend" cmd /k "cd /d %~dp0frontend && npm run dev"
echo Both Backend and Frontend servers launched in dedicated terminal windows!
