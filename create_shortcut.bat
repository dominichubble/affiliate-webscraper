@echo off
echo Creating desktop shortcut for Gaming Scraper UI...

set SCRIPT_DIR=%~dp0
set SHORTCUT_NAME=Gaming Scraper UI
set DESKTOP=%USERPROFILE%\Desktop

REM Create VBS script to create shortcut
echo Set oWS = WScript.CreateObject("WScript.Shell") > "%TEMP%\CreateShortcut.vbs"
echo sLinkFile = "%DESKTOP%\%SHORTCUT_NAME%.lnk" >> "%TEMP%\CreateShortcut.vbs"
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> "%TEMP%\CreateShortcut.vbs"
echo oLink.TargetPath = "%SCRIPT_DIR%start_ui.bat" >> "%TEMP%\CreateShortcut.vbs"
echo oLink.WorkingDirectory = "%SCRIPT_DIR%" >> "%TEMP%\CreateShortcut.vbs"
echo oLink.Description = "E-Gaming Affiliate Scraper Web UI" >> "%TEMP%\CreateShortcut.vbs"
echo oLink.IconLocation = "%SystemRoot%\System32\shell32.dll,277" >> "%TEMP%\CreateShortcut.vbs"
echo oLink.Save >> "%TEMP%\CreateShortcut.vbs"

REM Execute VBS script
cscript "%TEMP%\CreateShortcut.vbs" >nul

REM Clean up
del "%TEMP%\CreateShortcut.vbs"

echo Desktop shortcut created successfully!
echo You can now double-click "Gaming Scraper UI" on your desktop to start the application.
pause
