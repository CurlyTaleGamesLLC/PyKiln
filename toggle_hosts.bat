@echo off
set "installed=false"

where py >nul 2>&1 && set "installed=true"
if "%installed%" == "true" (
    py -3 ./toggle_hosts.py
    exit /b
)

where python3 >nul 2>&1 && set "installed=true"
if "%installed%" == "true" (
    python3 ./toggle_hosts.py
    exit /b
)

cls
echo Python 3 was NOT detected on your computer
echo.
echo Download the latest version, install it,
echo and make sure the "Add Python 3.x to PATH" checkbox is checked
echo.
START https://www.python.org/downloads/
pause