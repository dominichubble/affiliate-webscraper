# E-Gaming Affiliate Scraper - PowerShell Launcher
# This script provides a user-friendly way to start the web UI

Write-Host "===========================================" -ForegroundColor Cyan
Write-Host "   E-Gaming Affiliate Scraper Web UI" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Starting the web interface..." -ForegroundColor Green
Write-Host ""

# Check if virtual environment exists
if (Test-Path ".venv\Scripts\python.exe") {
    Write-Host "✓ Virtual environment found" -ForegroundColor Green
    $pythonCmd = ".venv\Scripts\python.exe"
    $streamlitCmd = ".venv\Scripts\streamlit.exe"
} else {
    Write-Host "Using system Python..." -ForegroundColor Yellow
    $pythonCmd = "python"
    $streamlitCmd = "streamlit"
}

# Check if Python is installed
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = & $pythonCmd --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "Python not found"
    }
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ ERROR: Python is not installed or not accessible" -ForegroundColor Red
    Write-Host "Please install Python from https://python.org" -ForegroundColor Yellow
    Write-Host "Make sure to check 'Add Python to PATH' during installation" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if required packages are installed
Write-Host "Checking required packages..." -ForegroundColor Yellow
try {
    & $pythonCmd -c "import streamlit" 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw "Streamlit not found"
    }
    Write-Host "✓ All packages are installed" -ForegroundColor Green
} catch {
    Write-Host "Installing required packages..." -ForegroundColor Yellow
    Write-Host "This may take a few minutes..." -ForegroundColor Yellow
    & $pythonCmd -m pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "✗ ERROR: Failed to install required packages" -ForegroundColor Red
        Write-Host "Please check your internet connection and try again" -ForegroundColor Yellow
        Read-Host "Press Enter to exit"
        exit 1
    }
    Write-Host "✓ Packages installed successfully!" -ForegroundColor Green
}

Write-Host ""
Write-Host "Starting web interface..." -ForegroundColor Yellow
Write-Host "A browser window will open automatically." -ForegroundColor Cyan
Write-Host "If it doesn't, go to: http://localhost:8501" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the application" -ForegroundColor Yellow
Write-Host ""

# Start the Streamlit app
try {
    if (Test-Path $streamlitCmd) {
        & $streamlitCmd run simple_ui.py --server.headless=false --server.port=8501 --server.address=localhost
    } else {
        & $pythonCmd -m streamlit run simple_ui.py --server.headless=false --server.port=8501 --server.address=localhost
    }
} catch {
    Write-Host "Error starting the application: $_" -ForegroundColor Red
    Read-Host "Press Enter to exit"
}
