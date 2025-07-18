@echo off
echo ==========================================
echo   E-Gaming Affiliate Scraper Web UI
echo ==========================================
echo.

REM Check if virtual environment exists and use it
if exist ".venv\Scripts\python.exe" (
    echo Using virtual environment...
    ".venv\Scripts\python.exe" launch_ui.py
) else (
    echo Using system Python...
    python launch_ui.py
)

echo.
echo Application stopped.
pause
