import sys
import random
import requests
from requests.models import HTTPError
sys.tracebacklimit = 0

url = "https://affiliate.apileads.tech/api/lead-create"
requests.post(url)

i = 1
while i <= 24:
    i += 1

    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

    # b = ['loan', 'general', 'crypto', 'loan', 'general', 'crypto', 'loan', 'general', 'crypto', 'loan', 'general', 'crypto']

    c = ['Mozilla/5.0 (Windows NT 6.3; WOW64)', 'AppleWebKit/537.36 (KHTML, like Gecko)', 'Chrome/94.0.4606.71 Safari/537.36']

    a = ['check1', 'check2', 'check3', 'check4', 'check5', 'check6', 'check7', 'check8', 'check9', 'check10', 'check11', 'check12']

    payload = {
    'phone': '9' + (str(random.randint(1, 999999999))),
    'phone_code': '396698',
    'type': 'general',
    'firstname': 'CheckFirstName' + (str(random.randint(10000, 99999))),
    'lastname': 'CheckLastName' + (str(random.randint(10000, 99999))),
    'email': 'exam' + (str(random.randint(10000, 99999))) + '@check.com',
    'user_agent': random.choice(c),
    'amount': random.choice(a),
    'country': 'do',
    'lang': 'fi',
    'ip': ip, 
    'sub1': '300900'}

    headers = {'key': 'yhUXH1EJ0MSgMFFxNqvFVtsRug4BGhLH'}

    response = requests.request("POST", url, headers=headers, data=payload)

    if (response.status_code <= 299): 
        print(payload)
        print("Status Code:", response.status_code)
        print(response.text)
    else:
        print("Status Code not 200! Error! Status Code:", response.status_code)

    try:
        assert response.status_code == 200
        assert response.status_code != 404
        assert response.status_code != 500
    except (BaseException, HTTPError):
        print("Status Code not 200! Error! Status Code:", response.status_code)