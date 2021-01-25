# -*- coding: utf-8 -*-


import requests

headers = {"Connection": "keep-alive"
    , "Upgrade-Insecure-Requests": "1"
    ,
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

url1 = "https://play-tx-recpub.douyucdn2.cn/live/high_live-7513035r9wlZUvBu--20210124221025/transcode_live-7513035r9wlZUvBu--20210124221025_121264_0000"
url2 = ".ts?tlink=600e411b&tplay=600ecdbb&exper=0&nlimit=5&us=ab7003ae17ec9f15dc4a3dc800081501&sign=6267cff97793f7f14116c106bff19eb2&u=0&d=ab7003ae17ec9f15dc4a3dc800081501&ct=web&vid=18556518&pt=2&cdn=tx"

h = 412

while (h < 469):
    hhh = str(h)
    reb = requests.get(url1 + hhh + url2, headers=headers)
    with open("C:\\Users\\19144\\Desktop\\777\\{}.ts".format(hhh), 'wb') as f:
        f.write(reb.content)
        f.close()
    print(h)
    h = h + 1
