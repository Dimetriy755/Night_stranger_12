@ECHO OFF

cd /c C:\Program Files\Google\Chrome\Application PE >nul 2>&1

TASKKILL /IM chrome.exe >nul 2>&1

TIMEOUT /T 2 /NOBREAK

echo.
echo START: good_test.py

CMD /c > ./my_good_test_results.txt "C:\Users\User\Desktop\2\my_experiments\good_test.py"

echo.
echo END: good_test.py

TIMEOUT /T 2 /NOBREAK

@REM pause

exit


