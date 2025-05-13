@echo off
tasklist | findstr /I "python" > nul
if errorlevel 1 (
    echo No Python process found.
) else (
    taskkill /F /IM python.exe
    echo Python processes killed.
)
python -m uvicorn bookapi.books2:app --reload --reload-dir=./bookapi
