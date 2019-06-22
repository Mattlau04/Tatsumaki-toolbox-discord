@setlocal enableextensions
@setlocal EnableDelayedExpansion
@echo off
if NOT EXIST tokens.txt echo. 2>tokens.txt
FOR /F "usebackq" %%A IN ('tokens.txt') DO set TOKENsize=%%~zA
if %TOKENsize% EQU 0 goto notokens
set "cmd=findstr /R /N "^^" tokens.txt | find /C ":""
for /f %%a in ('!cmd!') do set linetokens=%%a
if %linetokens% GEQ 50 echo That's a lot of tokens, be careful as it may lag your computer or even make the script not work at all
if %linetokens% GEQ 50 echo press any key to continue
if %linetokens% GEQ 50 pause > NUL
for /f "delims=" %%x in (Config.txt) do (set "%%x")
cls
if %mytoken% EQU urtokenhere goto nomytoken

:mainmenu:
cls
echo #=============================#
echo + Mattlau's tatsumaki toolbox +
echo #=============================#
echo.
echo 1. Mass bot menu
echo 2. Self bot menu
echo 3. Exit
echo.
set /P mainmenu=Where do you wanna go? 
if %mainmenu% EQU 1 goto choosemethod
if %mainmenu% EQU 2 goto selfbotmenu
if %mainmenu% EQU 3 exit
cls
echo invalid value :/
Timeout /T 2 > NUL
cls
goto mainmenu

:choosemethod:
cls
echo #===============#
echo + Mass bot menu +
echo #===============#
echo 0. go back
echo.
echo 1. Collect daily
echo 2. Collect rep
echo 3. Get cookies
echo 4. Transfer all the money to your account (take long, a little less than 10 sec per account)
echo 5. Make the tokens join a server (not working, use raid toolbox to make them join)
echo.
set /P what=type the number of the method you want: 
if %what% EQU 0 goto mainmenu
if %what% EQU 1 goto epicdaily
if %what% EQU 2 goto epicrep
if %what% EQU 3 goto epiccookies
if %what% EQU 4 goto epicmoney
if %what% EQU 5 goto joinserver
cls
echo invalid value :/
Timeout /T 2 > NUL
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

:selfbotmenu:
cls
echo #===============#
echo + Self bot menu +
echo #===============#
echo 0. go back
echo.
echo 1. Fish farmer
echo 2. Train tatsugotchi
echo.
set /P selfbotmenu=type the number of the method you want: 
if %selfbotmenu% EQU 0 goto mainmenu
if %selfbotmenu% EQU 1 goto epicfish
if %selfbotmenu% EQU 2 goto epictgtrain
cls
echo invalid value :/
Timeout /T 2 > NUL
cls
goto selfbotmenu

:epicfish:
start cmd /K python "%cd%\Scripts\Fish.py" %mytoken% %channelid% %minimumsellfish%
goto selfbotmenu

:epictgtrain:
start cmd /K python "%cd%\Scripts\Tgtrain.py" %mytoken% %channelid%
goto selfbotmenu


:notokens:
cls
echo You don't have any tokens in tokens.txt
echo go add some and run the script again
echo.
echo press any key to exit
pause > NUL
exit

:nomytoken:
cls
echo You don't have your token in your config file
echo go add it
echo.
echo press any key to exit
pause > NUL
exit
