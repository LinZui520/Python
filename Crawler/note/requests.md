# 定义baseurl
    baseurl = 'https://movie.douban.com/top250?start='
# 定义请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39"
    }
# url列表
    for i in range(0, 10):
        url = baseurl + str(i * 25)

# 请求网页
    response = requests.get(url, headers=headers)
    html = response.text