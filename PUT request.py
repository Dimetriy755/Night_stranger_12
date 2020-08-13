import requests

url = "https://petfriends1.herokuapp.com/api/pets/70e75b7d-9d8d-4e4a-95d1-562dfb408e81"

payload = {'name': 'СТРАШНАЯ_БАБАЯ_ненасытная_ЛЮТАЯ',
           'animal_type': 'ВСЕХ_ВСЕХ_СЪЕСТ_она!!!',
           'age': '100500'}

headers = {
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'session=.eJwlzjluAzEMQNG7qE7BVaR8GUPigqQdx1WQu2eA9B_472c8-6rX53h8X-_6GM-vHI8BvCnTzZbFDCTCU1YmxbTY8rByGuVMLt3idcK1c4PhhrYDKLC2lWeTATJElLpM6QlRyxsMjoeCsZhahrZMnmsKBbntGjfk_arrX3M3i3pDeKNgw9HbEojAR9VZWhBmFR4SYFhtdN9Tavz-ASbjPNw.Xx-Ong.-uOFwrQxtlMIIWxiZXEK-14MJEE; session=.eJwlzjlqBDEQQNG7KHZQq6o0lxmkWhiDo2kcGd_dDc4__Pcznv2u6zUevb-u-hjPzxyPAbwp082WxQwkwlNWJsW02PKwchrlTC7d4nXCtXOD4Ya2AyiwtpVnkwEyRJS6TOkJUcsbDI6HgrGYWoa2TJ5rCgW57Ro35Puq97_mbhb1hvBGwYajtyUQgY-qs7QgzCo8JMCw2ui-p9T4_QNo4D0n.Xx-TVQ.GFTbuaidvHVnRKstB8I0bg1xva8'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(payload)
print("Status Code:", response.status_code)

try:
    assert response.status_code == 200
except BaseException:
    print("Status Code not 200! Error! Status Code:", response.status_code)
