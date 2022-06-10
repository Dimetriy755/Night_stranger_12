@ECHO OFF

del %Temp%\*.* /S /F /Q
del C:\Windows\Temp\*.* /S /F /Q
SET Path2Del=C:\Windows\Temp\
for /R "%Path2Del%" %%F in (.) DO IF NOT "%%F"=="%Path2Del%." (RD /S /Q "%%F") ELSE (Del /F /S /Q "%Path2Del%*")
SET Path2Del=%Temp%\
for /R "%Path2Del%" %%F in (.) DO IF NOT "%%F"=="%Path2Del%." (RD /S /Q "%%F") ELSE (Del /F /S /Q "%Path2Del%*")
echo.
echo All temporary files and folders have been deleted!
pause