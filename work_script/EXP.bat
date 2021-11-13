@echo off 
Color 71
SET /A x=0

:initialize 
cd /c C:\Users\User\Desktop\test-docs\3snet.co\apileads PE
TASKKILL /F /IM export.py /IM export.py
echo export NO working
waitfor SomethingThatIsNeverHappening /t 3 >nul 2>&1

:start 
echo export working
cd /c C:\Users\User\Desktop\test-docs\3snet.co\apileads PE
start "" "export.py"  
SET /A x=1+x
echo %x%
waitfor SomethingThatIsNeverHappening /t 5 >nul 2>&1
goto initialize