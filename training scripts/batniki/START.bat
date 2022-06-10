@ECHO OFF

START "" /MAX "C:\Program Files\ShareX\ShareX.exe"

TIMEOUT /T 10 /NOBREAK

START "" /MAX "C:\Users\User\Downloads\PuntoSwitcherPortable\PuntoSwitcherPortable.exe"

TIMEOUT /T 10 /NOBREAK

START "" /MAX "C:\Users\User\Desktop\test-docs\3snet.co" 

TIMEOUT /T 2 /NOBREAK

START "" /MAX "C:\Users\User\Desktop\test-docs\3snet.co\Заметки по 3snet, apileads и newx.txt" 

TIMEOUT /T 2 /NOBREAK

START "" /MAX "C:\Program Files\Google\Chrome\Application\chrome.exe"

TIMEOUT /T 5 /NOBREAK

START "" "C:\Users\User\AppData\Roaming\Telegram Desktop\Telegram.exe" 

TIMEOUT /T 10 /NOBREAK 

exit 



