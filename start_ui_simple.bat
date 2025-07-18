@echo off
echo ==========================================
echo   E-Gaming Affiliate Scraper Web UI
echo ==========================================
echo.
echo Starting the web interface...
echo.

REM Check if virtual environment exists
if exist ".venv\Scripts\python.exe" (
    echo ✓ Virtual environment found
    set PYTHON_CMD=".venv\Scripts\python.exe"
    set STREAMLIT_CMD=".venv\Scripts\streamlit.exe"
) else (
    echo Using system Python...
    set PYTHON_CMD=python
    set STREAMLIT_CMD=streamlit
)

REM Quick check for Python
%PYTHON_CMD% --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not accessible
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Quick check for Streamlit
%PYTHON_CMD% -c "import streamlit" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing Streamlit...
    %PYTHON_CMD% -m pip install streamlit
)

echo.
echo Starting web server...
echo Your browser will open automatically in a few seconds...
echo.

REM Create a simple Python script to start Streamlit and open browser
echo import streamlit as st > temp_launcher.py
echo import webbrowser >> temp_launcher.py
echo import time >> temp_launcher.py
echo import threading >> temp_launcher.py
echo import subprocess >> temp_launcher.py
echo import sys >> temp_launcher.py
echo. >> temp_launcher.py
echo def open_browser(): >> temp_launcher.py
echo     time.sleep(3) >> temp_launcher.py
echo     webbrowser.open('http://localhost:8501') >> temp_launcher.py
echo. >> temp_launcher.py
echo if __name__ == '__main__': >> temp_launcher.py
echo     threading.Thread(target=open_browser, daemon=True).start() >> temp_launcher.py
echo     subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'simple_ui.py', '--server.port=8501']) >> temp_launcher.py

REM Run the launcher
%PYTHON_CMD% temp_launcher.py

REM Clean up
del temp_launcher.py 2>nul

echo.
echo Application stopped.
pause
