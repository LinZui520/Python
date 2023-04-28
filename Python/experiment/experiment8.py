import requests
import re
from bs4 import BeautifulSoup


def get_url_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return response.text


def main():
    baseurl = 'https://movie.douban.com/top250?start='
    movie = {}
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = get_url_html(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            if item.find('span', class_="inq"):
                movie[item.find('span', class_="title").text] = item.find('span', class_="inq").text
    print(movie)


if __name__ == '__main__':
    main()
