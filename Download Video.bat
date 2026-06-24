@echo off
title Ultimate HD Video Downloader Diagnostics
cls

echo ===================================================
echo     PREPARING DOWNLOADER... 
echo ===================================================
echo.

:: 1. Check Python
echo Checking Python status...
python --version
if %errorlevel% neq 0 (
    echo [!] Python command failed. Trying fallback installer...
    curl -o python_installer.exe https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
    start /wait python_installer.exe /quiet PrependPath=1 Include_test=0
    del python_installer.exe
    echo [+] Re-checking Python...
    python --version
)
echo.

:: 2. Upgrade Pip
echo Upgrading Pip...
python -m pip install --upgrade pip
echo.

:: 3. Install/Upgrade yt-dlp
echo Upgrading yt-dlp...
python -m pip install --upgrade yt-dlp
echo.

:: 4. Check FFmpeg Core
echo Checking FFmpeg status...
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] FFmpeg missing. Triggering Windows Package Manager...
    winget install Gyan.FFmpeg --accept-source-agreements --accept-package-agreements
) else (
    echo [+] FFmpeg is fully functional.
)
echo.

echo ===================================================
echo     SETUP COMPLETE. PRESS ANY KEY TO RUN ENGINE
echo ===================================================
pause

:GET_URL
cls
echo ===================================================
echo             HD VIDEO DOWNLOADER
echo ===================================================
echo.
set "myurl="
set /p "myurl= Right-click to PASTE your YouTube link here and press Enter: "

if not defined myurl goto GET_URL
if "%myurl%"=="" goto GET_URL

echo.
echo Launching downloader_engine.py...
echo.

:: 5. Strictly targeted script launch
python "%~dp0downloader_engine.py" "%myurl%"

echo.
echo ===================================================
echo        DOWNLOAD STREAM PROCESS FINISHED 
echo ===================================================
echo.
pause
goto GET_URL