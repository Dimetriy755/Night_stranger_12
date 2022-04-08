import random
import requests

url = "http://affiliate.apileads.tech/api/lead-create"

i = 1
while i <= 5:
    i += 1

    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

    a = ['test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9', 'test10', 'test11', 'test12']

    b = ['loan', 'general', 'loan', 'general', 'loan', 'general', 'loan', 'general', 'loan', 'general', 'loan', 'general']

    c = ['Mozilla/5.0 (Windows NT 6.3; WOW64)', 'AppleWebKit/537.36 (KHTML, like Gecko)', 'Chrome/94.0.4606.71 Safari/537.36']

    payload={
    'phone': '9' + (str(random.randint(1, 999999999))),
    'phone_code': '380',
    'type': random.choice(b),
    'firstname': 'TestFirstName' + (str(random.randint(100, 999))),
    'lastname': 'TestLastName' + (str(random.randint(100, 999))),
    'email': 'test' + (str(random.randint(10000, 99999))) + '@test.3snet.tech',
    'user_agent': random.choice(c),
    'amount': random.choice(a),
    'country': 'cn',
    'lang': 'pt',
    'ip': ip }

    files=[]

    headers = {'key': 'md6b9h2qXiOhBlOVHQmYYvyWbzbo8k9O'}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(payload)
    print("Status Code:", response.status_code)
    print(response.text)