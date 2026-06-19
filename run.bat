@echo off
REM ============================================================
REM  Flow Control Valves - local dev server launcher
REM  Starts the static site server and opens it in the browser
REM ============================================================

setlocal
cd /d "%~dp0"

set PORT=3000

echo.
echo  ============================================
echo   Flow Control Valves - starting server...
echo   URL: http://localhost:%PORT%
echo   Press Ctrl+C in this window to stop.
echo  ============================================
echo.

REM Open the site in the default browser after a short delay
start "" cmd /c "timeout /t 2 >nul & start http://localhost:%PORT%"

REM Start the server (blocks until you close it)
python serve.py %PORT%

endlocal
