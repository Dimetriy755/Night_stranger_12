@ECHO OFF

cd /c C:\Program Files\Google\Chrome\Application PE >nul 2>&1

TASKKILL /IM chrome.exe >nul 2>&1

TIMEOUT /T 2 /NOBREAK

echo.
echo START: 0-2.py

CMD /c > ./my_test_results-2.txt "C:\Users\User\Desktop\2\my_experiments\0-2.py"

echo.
echo END: 0-2.py

TIMEOUT /T 4 /NOBREAK

@REM pause

exit


