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
Write-Host "Opening browser automatically..." -ForegroundColor Green
Write-Host "If the browser doesn't open, go to: http://localhost:8501" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the application" -ForegroundColor Yellow
Write-Host ""

# Start the Streamlit app in background
try {
    if (Test-Path $streamlitCmd) {
        Start-Process -FilePath $streamlitCmd -ArgumentList "run", "simple_ui.py", "--server.headless=true", "--server.port=8501", "--server.address=localhost" -NoNewWindow
    } else {
        Start-Process -FilePath $pythonCmd -ArgumentList "-m", "streamlit", "run", "simple_ui.py", "--server.headless=true", "--server.port=8501", "--server.address=localhost" -NoNewWindow
    }
    
    # Wait a moment for the server to start
    Start-Sleep -Seconds 3
    
    # Open the browser
    Start-Process "http://localhost:8501"
    
    Write-Host "Web interface is now running in your browser!" -ForegroundColor Green
    Write-Host "Close this window or press Ctrl+C to stop the application." -ForegroundColor Yellow
    Write-Host ""
    
    # Keep the script running
    Read-Host "Press Enter to stop the application"
    
} catch {
    Write-Host "Error starting the application: $_" -ForegroundColor Red
    Read-Host "Press Enter to exit"
}
