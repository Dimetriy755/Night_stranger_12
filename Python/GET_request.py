import requests
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

while 1 == 1:
    try:
        print("")
        url = str(input(" Enter request URL: "))
        response = requests.get(url)
        break
    except BaseException:
        print("")
        print(" Invalid URL, try entering URL again!")
        continue

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
print("Status Code:", response.status_code)

time.sleep(100)





