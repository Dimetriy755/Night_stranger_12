@ECHO OFF

cd /c C:\Program Files\Google\Chrome\Application PE >nul 2>&1

:: TASKKILL /F /IM chrome.exe /T > nul

TASKKILL /IM chrome.exe >nul 2>&1

TIMEOUT /T 2 /NOBREAK

echo.
echo START: 0-1.py

CMD /c > ./my_test_results-1.txt "C:\Users\User\Desktop\2\my_experiments\0-1.py"

echo.
echo END: 0-1.py

TIMEOUT /T 4 /NOBREAK

rem echo.
rem echo START: remove_all.py

:: CMD /c >> ./my_test_results-1.txt "C:\Users\User\Desktop\2\my_experiments\remove_all.py"

@REM pause

exit