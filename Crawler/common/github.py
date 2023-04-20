import requests
# from bs4 import BeautifulSoup
import re

url = 'https://github.com/login'

session = requests.Session()
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
                  "Safari/537.36 Edg/112.0.1722.48"
}

login_url = 'https://github.com/login'

html = session.get(login_url).text
# print(html)
# soup = BeautifulSoup(html, 'lxml')
# authenticity_token = soup.find('input', attrs={'name': 'authenticity_token'}).get('value')
# print(authenticity_token)

authenticity_token = re.findall('<input type="hidden" name="authenticity_token" value="(.*?)" />', html, re.S)[0]
print(authenticity_token)

timestamp = re.findall('<input type="hidden" name="timestamp" value="(.*?)" autocomplete="off" class="form-control" />',
                       html, re.S)[0]
print(timestamp)
timestamp_secret = re.findall('<input type="hidden" name="timestamp_secret" value="(.*?)" autocomplete="off" '
                              'class="form-control" />', html, re.S)[0]
print(timestamp_secret)

params = {
    'commit': 'Sign in',
    'authenticity_token': authenticity_token,
    'login': '',
    'password': '',
    'webauthn-support': 'supported',
    'webauthn-iuvpaa-support': 'supported',
    'return_to': 'https://github.com/login',
    'allow_signup': '',
    'client_id': '',
    'integration': '',
    # 'required_field_e835': '',
    'timestamp': timestamp,
    'timestamp_secret': timestamp_secret,
}

response = session.post('https://github.com/session', data=params)
response2 = session.get(login_url)
print(response2.text)
