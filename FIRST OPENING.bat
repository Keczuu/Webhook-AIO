@echo off
title Keczuu AIO Installer
choice /C YN /M "Do you want to install Keczuu AIO"

IF ERRORLEVEL 2 GOTO two
IF ERRORLEVEL 1 GOTO three
GOTO end

:two
ECHO Exiting...
timeout /t 3
EXIT /B

:three
ECHO Installing...
pip install -r requirements.txt
ECHO Installed!

:end
@PAUSE
