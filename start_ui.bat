@echo off
echo ==========================================
echo   E-Gaming Affiliate Scraper Web UI
echo ==========================================
echo.
echo This will start a web interface for the scraper.
echo Choose which interface you'd like to use:
echo.
echo 1. Simple UI (recommended for beginners)
echo 2. Advanced UI (more features and controls)
echo.
set /p choice="Enter your choice (1 or 2): "

if "%choice%"=="1" (
    set app_file=simple_ui.py
    echo Starting Simple UI...
) else if "%choice%"=="2" (
    set app_file=app.py
    echo Starting Advanced UI...
) else (
    echo Invalid choice. Starting Simple UI by default...
    set app_file=simple_ui.py
)

echo.
echo Checking Python environment...

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

%PYTHON_CMD% --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not accessible
    echo Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python found! Checking packages...
%PYTHON_CMD% -c "import streamlit" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing required packages (this may take a few minutes)...
    %PYTHON_CMD% -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install required packages
        echo Please check your internet connection and try again
        pause
        exit /b 1
    )
    echo Packages installed successfully!
)

echo.
echo Starting web interface...
echo A browser window will open automatically.
echo If it doesn't, go to: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

if exist ".venv\Scripts\streamlit.exe" (
    ".venv\Scripts\streamlit.exe" run %app_file% --server.headless=false --server.port=8501 --server.address=localhost
) else (
    streamlit run %app_file% --server.headless=false --server.port=8501 --server.address=localhost
)

pause
