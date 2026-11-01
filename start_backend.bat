@echo off
title NeuroVision Backend API
cd /d "%~dp0backend"
echo ============================================================
echo Starting NeuroVision FastAPI Backend on http://127.0.0.1:8000
echo ============================================================
call venv\Scripts\activate.bat
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
pause
