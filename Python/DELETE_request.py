import requests

url = "https://petfriends1.herokuapp.com/api/pets/4c81a709-2d86-4785-bb46-3725b015c744"

payload = {}
headers = {
    'Cookie': 'session=.eJwlzjluAzEMQNG7qE7BVaR8GUPigqQdx1WQu2eA9B_472c8-6rX53h8X-_6GM-vHI8BvCnTzZbFDCTCU1YmxbTY8rByGuVMLt3idcK1c4PhhrYDKLC2lWeTATJElLpM6QlRyxsMjoeCsZhahrZMnmsKBbntGjfk_arrX3M3i3pDeKNgw9HbEojAR9VZWhBmFR4SYFhtdN9Tavz-ASbjPNw.Xx-Ong.-uOFwrQxtlMIIWxiZXEK-14MJEE; session=.eJwlzjlqBDEQQNG7KHZQq6o0lxmkWhiDo2kcGd_dDc4__Pcznv2u6zUevb-u-hjPzxyPAbwp082WxQwkwlNWJsW02PKwchrlTC7d4nXCtXOD4Ya2AyiwtpVnkwEyRJS6TOkJUcsbDI6HgrGYWoa2TJ5rCgW57Ro35Puq97_mbhb1hvBGwYajtyUQgY-qs7QgzCo8JMCw2ui-p9T4_QNo4D0n.Xx-TVQ.GFTbuaidvHVnRKstB8I0bg1xva8'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
print("Status Code:", response.status_code)

try:
    assert response.status_code == 200
except BaseException:
    print("Status Code not 200! Error! Status Code:", response.status_code)

