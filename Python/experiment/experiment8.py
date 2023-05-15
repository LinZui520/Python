import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.kugou.com/songlist/gcid_3zjlycjqz1yz02a/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 "
                  "Safari/537.36 Edg/113.0.1774.42"
}

response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, "html.parser")

data = {}
for item in soup.find_all('a', hidefocus="true"):
    if re.findall('周杰伦', item['title']):
        data[item['title']] = item['href']

for i in data:
    print(i, data[i])
