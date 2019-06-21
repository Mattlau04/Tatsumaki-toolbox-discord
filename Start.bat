@setlocal enableextensions disabledelayedexpansion
@echo off
if NOT EXIST tokens.txt echo. 2>tokens.txt
FOR /F "usebackq" %%A IN ('tokens.txt') DO set TOKENsize=%%~zA
if %TOKENsize% EQU 0 goto notokens
for /f "delims=" %%x in (Config.txt) do (set "%%x")
cls

:choosemethod:
cls
echo What do you want to do?
echo 1. Collect daily
echo 2. Collect rep
echo 3. Get cookies
echo 4. Transfer all the money to your account (take long, a little less than 10 sec per account)
echo 5. Make the tokens join a server (not working, use raid toolbox to make them join)
echo.
set /P what=type the number of the method you want: 
if %what% EQU debug goto debug
if %what% EQU 1 goto epicdaily
if %what% EQU 2 goto epicrep
if %what% EQU 3 goto epiccookies
if %what% EQU 4 goto epicmoney
if %what% EQU 5 goto joinserver
cls
echo invalid value :/
Timeout /T 3 /NOBREAK > NUL
cls
goto choosemethod

:epicdaily:
start /wait /min python "%cd%\Scripts\DailyLauncher.py" %userid% %channelid% %pythonexe%
goto choosemethod

:epicrep:
start /wait /min python "%cd%\Scripts\RepLauncher.py" %userid% %channelid% %pythonexe%
goto choosemethod

:epiccookies:
start /wait /min python "%cd%\Scripts\CookieLauncher.py" %userid% %channelid% %pythonexe%
goto choosemethod

:epicmoney:
echo.
for /F "tokens=*" %%A in (tokens.txt) do start /wait /min python "%cd%\Scripts\CreditWithdraw.py" %userid% %channelid% %%A & echo Tranfering money from %%A
goto choosemethod

:joinserver:
cls
set /P invite=Invite to the server the tokens should join (ex: 5wVPkk):
for /F "tokens=*" %%A in (tokens.txt) do start /wait /min python "%cd%\Scripts\joiner.py" "%invite%" "%%A"
goto choosemethod

:notokens:
cls
echo You don't have any tokens in tokens.txt
echo go add some and run the script again
echo.
echo press any key to exit
pause > NUL
exit
