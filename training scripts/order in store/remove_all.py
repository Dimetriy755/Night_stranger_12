import sys
import json
import requests
from requests.models import HTTPError

sys.tracebacklimit = 0

url = "https://www.ozon.ru/api/composer-api.bx/_action/addToCart"

# removes only one product from basket by its id
payload = json.dumps([
  {
    "id": 189159041,
    "quantity": 0
  }
])

headers = {
  'authority': 'www.ozon.ru',
  'accept': 'application/json',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,hy;q=0.6',
  'content-type': 'application/json',
  'cookie': '__Secure-ab-group=50; __Secure-ext_xcid=001debbc733519de408710b341772aaf; tmr_lvid=e57a4800b90e222343780cfcf0c2106a; tmr_lvidTS=1655040320888; _gcl_au=1.1.2136328042.1655040321; __exponea_etc__=e91ce348-3699-4ff2-960f-5d0c873276b2; _ga=GA1.1.1468505877.1655040322; __exponea_time2__=-7312.541168928146; __Secure-access-token=3.47399369.pToWliQkSIy4IA4umCT_vg.50.l8cMBQAAAABipeZXOOBerqN3ZWKrNzk3NzkzNzM3NTkAgJCg.20200609235112.20220612151255.DwN1-SaMJK4r_lBlfEhkmJ9-bOx8NdU5Xi_tlSSqs0U; __Secure-refresh-token=3.47399369.pToWliQkSIy4IA4umCT_vg.50.l8cMBQAAAABipeZXOOBerqN3ZWKrNzk3NzkzNzM3NTkAgJCg.20200609235112.20220612151255.U8b-wa5XU5WTuT3brlQ_knyNOp34Ucxx6c4te8CtfhA; __Secure-user-id=47399369; is_adult_confirmed=; is_alco_adult_confirmed=; __cf_bm=9myM1L50DylVGA5JcjeNQVlKBpzcCwuWx4wPdebyl_c-1655042115-0-AYC59OM2TQZtsE7KOLYjSSV9nmZx55kI/cwPvBDJNdRHkfV4PK9w4QU9tS4iK3kKjou0Iao2huzONTmaPRbe1tyrg98Nmn09Z9EjWS5DsxCT3Q9C7xLgMUvwGSCHcLuvCFvjgC+xcSGiD8uzyazg3c84gfciI1d4jDaTJMCnvg9P; tmr_reqNum=75; _ga_JNVTMNXQ6F=GS1.1.1655046848.2.1.1655049806.53',
  'origin': 'https://www.ozon.ru',
  'referer': 'https://www.ozon.ru/category/transmissionnye-masla-8516/nissan-136021052/?from_global=true&isdiscount=t&rating=t&seller=38479&text=трансмиссионное+масло+nissan+cvt+ns-2,+5л'.encode('utf-8'),
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
  'x-o3-app-name': 'dweb_client',
  'x-o3-app-version': 'release_10-5\'-\'2022_f0473de2'
}

response = requests.request("POST", url, headers=headers, data=payload)

data = response.json()

id = data['cart']['cartItems']['id']

# for (.bat) file start / or alternative
if (response.status_code <= 299):
    print("")
    print("")
    print("+ and more info")
    print("----------------------------------------------------------------------")
    print("")
    print("Success! Removal of products from basket was successful!")
    print("Here is all the information on the request for removal:")
    print("")
    print("Transmitted data:", payload)
    print("")
    print("Status Code:", response.status_code)
    print("")
    # also there will be message about this if another product will be in basket with another id (!!!) 
    print("Response from server:", response.text, "\n----------------------------------------------------------------------")    
    print("From basket product id:", id)   
else:
    print("")
    print("")
    print("+ and more info")
    print("----------------------------------------------------------------------")
    print("")
    print("Failure! Attention! There is something goes wrong!")
    print("Detect what's wrong by messages about status code:")
    print("")
    print("Status Code not 200! Error! Status Code:", response.status_code)

try:
    assert response.status_code == 200
    assert response.status_code != 403
    assert response.status_code != 404
    assert response.status_code != 500
except (BaseException, HTTPError):
    print("Status Code not 200! Error! Status Code:", response.status_code)
    if (response.status_code == 403):
        print("Access denied! Update your cookie.")
    else:
        pass      
    print("----------------------------------------------------------------------")