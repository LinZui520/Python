import requests
from bs4 import BeautifulSoup


def main():
    baseurl = 'https://movie.douban.com/top250?start='
    data = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = ask_url(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            data.append(item.find_all('span', class_="title")[0].text)
    print(data)


def ask_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return response.text


if __name__ == "__main__":
    main()
