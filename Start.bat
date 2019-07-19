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
set wantedpet=%wantedpet: =-_-%
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
echo 3. Load a different config file (usefull for alts or reloading config)
echo.
echo 4. Exit
echo.
set /P mainmenu=Where do you wanna go? 
if %mainmenu% EQU 1 goto choosemethod
if %mainmenu% EQU 2 goto selfbotmenu
if %mainmenu% EQU 3 goto loadconfig
if %mainmenu% EQU 4 exit
cls
echo invalid value :/
Timeout /T 2 > NUL
cls
goto mainmenu

:loadconfig:
set oldcd=%cd%
echo.
echo Enter the name of the config file
echo (it can be only the name if it's in the same folder as this script or full path)
echo.
set /P loadconfig=Name of the config: 

If NOT exist "%cd%\%loadconfig%" goto addtxt
If %errorlevel% EQU 3 goto addtxt
cls
echo Loading config...
for /f "delims=" %%x in (%loadconfig%) do (set "%%x")
cls
echo Loaded config!
Timeout /T 2 > NUL
goto mainmenu

:addtxt:
If NOT exist "%cd%\%loadconfig%.txt" goto completepath
If %errorlevel% EQU 3 goto completepath
cls
echo Loading config...
for /f "delims=" %%x in (%loadconfig%.txt) do (set "%%x")
cls
echo Loaded config!
Timeout /T 2 > NUL
goto mainmenu

:completepath:
If NOT exist "%loadconfig%" goto confignotfoundloader
If %errorlevel% EQU 3 goto confignotfoundloader
cls
echo Loading config...
for /f "delims=" %%x in (%loadconfig%) do (set "%%x")
cls
echo Loaded config!
Timeout /T 2 > NUL
goto mainmenu

:confignotfoundloader:
cls
echo Config not found
echo Names are case sensitive so be careful
echo.
echo Press any key to continue
pause > NUL
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
echo 4. XP and Credits farmer (it just send random messages)
echo 5. Get the daily directly on your main accout (you will gain way more but higher risk of bot detection)
echo 6. Transfer all the money to your account (take long, a little less than 10 sec per account)
echo 7. Make the tokens join a server (not working, use raid toolbox to make them join)
echo.
set /P what=type the number of the method you want: 
if %what% EQU 0 goto mainmenu
if %what% EQU 1 goto epicdaily
if %what% EQU 2 goto epicrep
if %what% EQU 3 goto epiccookies
if %what% EQU 4 goto epicmsgfarmbots
if %what% EQU 5 goto epicdailydirect
if %what% EQU 6 goto epicmoney
if %what% EQU 7 goto joinserver
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

:epicmsgfarmbots:
start cmd /K "%cd%\Scripts\XPcreditsfarmbots.bat" %userid% %channelid% %pythonexe%
goto choosemethod

:epicdailydirect:
start /wait /min python "%cd%\Scripts\Dailydirectlauncher.py" %userid% %channelid% %pythonexe%
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
echo 3. XP and Credits farmer (it just send random messages)
echo 4. Custom pet getter
echo 5. Cookie sender
echo.
set /P selfbotmenu=type the number of the method you want: 
if %selfbotmenu% EQU 0 goto mainmenu
if %selfbotmenu% EQU 1 goto epicfish
if %selfbotmenu% EQU 2 goto epictgtrain
if %selfbotmenu% EQU 3 goto epicmsgfarm
if %selfbotmenu% EQU 4 goto getepicpets
if %selfbotmenu% EQU 5 goto sendcookies
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

:epicmsgfarm:
start cmd /K python "%cd%\Scripts\XPcreditsfarm.py" %mytoken% %channelid%
goto selfbotmenu

:getepicpets:
if %wantedpet% EQU None goto nopetslol
echo.
echo WARNING
echo THIS WILL REMOVE YOUR CURRENT PET
echo if you're fine with that, press any key to continue
pause > NUL
start python "%cd%\Scripts\Getepicpets.py" %mytoken% %channelid% "%wantedpet%"
goto selfbotmenu

:sendcookies:
if /I %cookiesendertarget% EQU Prompt goto promptcookie
if /I %cookiesenderserver% EQU True goto promptcookieserver
start cmd /K python "%cd%\Scripts\Selfcookie.py" %mytoken% %channelid% %cookiesendertarget%
goto selfbotmenu

:promptcookie:
echo.
echo Enter the id of the person to send cookie to
echo you can also enter "Random" to send cookie to random peoples
echo.
set /P cookiesendertargetprompt=Enter the id or Random: 
if /I %cookiesenderserver% EQU True goto promptcookieserver
start cmd /K python "%cd%\Scripts\Selfcookie.py" %mytoken% %channelid% %cookiesendertargetprompt%
goto selfbotmenu

:promptcookieserver:
echo.
echo Enter the id of the channel to send the cookies (can be on any server your on)
echo you can also enter "default" to send cookie to the default text channel in config
echo.
set /P channelidcustom=Enter the id or default: 
if /I %channelidcustom% EQU default start cmd /K python "%cd%\Scripts\Selfcookie.py" %mytoken% %channelid% %cookiesendertargetprompt%
if /I NOT %channelidcustom% EQU default start cmd /K python "%cd%\Scripts\Selfcookie.py" %mytoken% %channelidcustom% %cookiesendertargetprompt%
goto selfbotmenu


:nopetslol:
echo look like u haven't set the pet you want in your config file
echo go set it and restart the script
pause > NUL
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
