@setlocal enableextensions
@setlocal EnableDelayedExpansion
@echo off
set messagesent=0
for /f "delims=" %%x in (Config.txt) do (set "%%x")
for /f %%a in ('!cmd!') do set linetokens=%%a
set /A epictokens=%linetokens% * 2
cls
:info:
cls
echo #=======================#
echo + XP and credits farmer +
echo #=======================#
echo.
SET /A waitintemp=120/%epictokens%
SET /A waitin=%waitintemp% + 1
echo Sent %messagesent% message
echo.
for /F "tokens=*" %%A in (tokens.txt) do (
    echo Sending message with %%A
    start /MIN /WAIT python "%cd%\Scripts\XPcreditsfarmbots.pyw" %%A %channelid%
    set /a "messagesent=!messagesent!+1"
    timeout /T %waitin% /Nobreak
    cls
    echo #=======================#
    echo + XP and credits farmer +
    echo #=======================#
    echo.
    echo Sent !messagesent! message
)
goto info
exit