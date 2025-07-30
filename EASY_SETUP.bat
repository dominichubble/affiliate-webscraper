@echo off
title E-Gaming Affiliate Scraper - Easy Setup
echo ==========================================
echo   E-Gaming Affiliate Scraper
echo   EASY SETUP FOR NON-TECHNICAL USERS
echo ==========================================
echo.
echo This will automatically set up everything you need.
echo Please wait while we prepare the application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed on your system.
    echo.
    echo PLEASE DO THE FOLLOWING:
    echo 1. Visit: https://python.org/downloads
    echo 2. Download and install Python
    echo 3. IMPORTANT: Check "Add Python to PATH" during installation
    echo 4. Restart your computer after installation
    echo 5. Run this setup again
    echo.
    pause
    exit /b 1
)

echo ✓ Python is installed

REM Create virtual environment if it doesn't exist
if not exist ".venv" (
    echo.
    echo Creating isolated Python environment...
    python -m venv .venv
    if %errorlevel% neq 0 (
        echo ❌ Failed to create virtual environment
        echo Please ensure Python is properly installed
        pause
        exit /b 1
    )
    echo ✓ Virtual environment created
)

REM Activate virtual environment and install packages
echo.
echo Installing required packages (this may take a few minutes)...
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ❌ Failed to install packages
    echo Please check your internet connection and try again
    pause
    exit /b 1
)

echo.
echo ✓ All packages installed successfully

REM Test the setup
echo.
echo Testing the setup...
.venv\Scripts\python.exe test_setup.py

if %errorlevel% neq 0 (
    echo ❌ Setup test failed
    echo Please contact technical support
    pause
    exit /b 1
)

echo.
echo ==========================================
echo ✅ SETUP COMPLETE!
echo ==========================================
echo.
echo The application is now ready to use.
echo.
echo To start the application, simply double-click:
echo "START_APPLICATION.bat"
echo.
echo A web browser will open with the scraper interface.
echo.
pause
