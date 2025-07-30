@echo off
title E-Gaming Affiliate Scraper - Application
echo ==========================================
echo   E-Gaming Affiliate Scraper
echo   WEB APPLICATION
echo ==========================================
echo.

REM Check if setup was completed
if not exist ".venv\Scripts\python.exe" (
    echo ❌ The application is not set up yet.
    echo.
    echo Please run "EASY_SETUP.bat" first to install the application.
    echo.
    pause
    exit /b 1
)

echo Starting the web application...
echo.
echo ⏳ Please wait while the application loads...
echo 📱 A web browser will open automatically
echo 🌐 If it doesn't open, go to: http://localhost:8501
echo.
echo ⚠️  IMPORTANT: Keep this window open while using the application
echo ❌ Closing this window will stop the application
echo.

REM Start the application
.venv\Scripts\python.exe -m streamlit run simple_ui.py --server.headless true --server.port 8501 --browser.gatherUsageStats false

echo.
echo Application stopped.
echo Press any key to close this window...
pause >nul
