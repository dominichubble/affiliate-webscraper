#!/usr/bin/env python3
"""
Browser launcher for Streamlit UI
This script ensures the browser opens automatically when starting the UI
"""

import webbrowser
import time
import threading
import subprocess
import sys
import os

def open_browser():
    """Open the browser after a short delay"""
    time.sleep(3)  # Wait for Streamlit to start
    print("Opening browser...")
    webbrowser.open('http://localhost:8501')

def main():
    """Start Streamlit and open browser automatically"""
    print("Starting E-Gaming Affiliate Scraper Web UI...")
    print("Your browser will open automatically in a few seconds...")
    print("If it doesn't, go to: http://localhost:8501")
    print("")
    
    # Start browser opening in background
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()
    
    # Start Streamlit
    try:
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', 'simple_ui.py',
            '--server.port=8501',
            '--server.headless=true'
        ])
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
    except Exception as e:
        print(f"Error starting application: {e}")
        input("Press Enter to exit...")

if __name__ == '__main__':
    main()
