@echo off
echo ==========================================
echo   E-Gaming Affiliate Scraper Web UI
echo ==========================================
echo.
echo Starting the web interface...
echo A browser window will open automatically.
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
echo Opening browser automatically...
echo If the browser doesn't open, go to: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

REM Start Streamlit in background and then open browser
if exist ".venv\Scripts\streamlit.exe" (
    start /b ".venv\Scripts\streamlit.exe" run simple_ui.py --server.headless=true --server.port=8501 --server.address=localhost
) else (
    start /b streamlit run simple_ui.py --server.headless=true --server.port=8501 --server.address=localhost
)

REM Wait a moment for the server to start
timeout /t 3 /nobreak >nul

REM Open the browser
start http://localhost:8501

REM Wait for user to stop the application
echo.
echo Web interface is now running in your browser!
echo Close this window or press Ctrl+C to stop the application.
echo.
pause >nul
