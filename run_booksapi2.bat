@echo off
cd /d D:\projects\SELF\Python

tasklist | findstr /I "python" > nul
if errorlevel 1 (
    echo No Python process found.
) else (
    taskkill /F /IM python.exe
    echo Python processes killed.
)

REM Activate the virtual environment
call .venv\Scripts\activate.bat

REM Run Uvicorn
python -m uvicorn bookapi.books2:app --reload --reload-dir=./bookapi
