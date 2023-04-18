import requests

url = 'https://space.bilibili.com/387317763'

cookies = {
    "buvid3": "768961F5-7BEE-949A-0695-DD3BDD5F8F3906170infoc",
    "i-wanna-go-back": "-1",
    "_uuid": "CC11021093-71039-89B4-DB43-F11217D2212B06791infoc",
    "buvid_fp": "84113348f22ba656ebd838da5480856c",
    "FEED_LIVE_VERSION": "V8",
    "home_feed_column": "4",
    "b_nut": "1681655604",
    "CURRENT_FNVAL": "4048",
    "header_theme_version": "CLOSE",
    "nostalgia_conf": "-1",
    "LIVE_BUVID": "AUTO6116814565232236",
    "PVID": "1",
    "CURRENT_PID": "253d1b10-da94-11ed-9f33-fb486fcf450b",
    "rpdid": "|(J|Y||uk~kR0J'uY)uRlYlJJ",
    "SESSDATA": "ee79ca0f%2C1697179864%2Cd2a6f%2A42",
    "bili_jct": "7500c5f7b56683505773db1b78956c35",
    "DedeUserID": "387317763",
    "DedeUserID__ckMd5": "398a6a80ac60f0c2",
    "b_ut": "5",
    "innersign": "0",
    "b_lsid": "39779F4E_1878A3CAFBD",
    "bp_video_offset_387317763": "785124492975276000",
    "buvid4": "2807805D-C6CD-CF23-F24E-40CF66B7529007705-023041218-PdJr0jKE6N47tR/wUKZDNNBcChMGOGeAlwL9CyhAbRt+R"
              "+7K8LJ0eA%3D%3D"
}
headers = {
    # ":authority": "space.bilibili.com",
    # ":method": "GET",
    # ":path": "/387317763/favlist",
    # ":scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5",
    "cache-control": "max-age=0",
    "referer": "https://account.bilibili.com/",
    "sec-ch-ua": '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "windows",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
                  "Safari/537.36 Edg/112.0.1722.39",
}
session = requests.session()
response = session.get(url, headers=headers, cookies=cookies)
print(session.get('https://space.bilibili.com/').text)

