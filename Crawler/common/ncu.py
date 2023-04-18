import requests

url = 'https://jwdata.ncu.edu.cn/aauc/api/authentication/form'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
                  "Safari/537.36 Edg/112.0.1722.39"
}
session = requests.Session()
data = {
    'username': '8008121268',
    'password': 'hym.....20',
}
response = session.post(url, data=data, headers=headers)
print(response.text)
