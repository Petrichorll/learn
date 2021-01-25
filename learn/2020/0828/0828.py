# -*- coding: utf-8 -*-

import requests, re

# url = "https://cn.bing.com/images/search?q=%E4%B8%AD%E5%9B%BD%E6%94%BF%E6%B2%BB%E4%BA%BA%E7%89%A9%E5%9B%BE%E7%89%87&go=%E6%90%9C%E7%B4%A2&qs=ds&form=QBIR&first=1&scenario=ImageBasicHover&cw=1117&ch=706"
url = "https://cn.bing.com/images/search?q=%E7%9C%81%E9%95%BF&first=1&scenario=ImageBasicHover&ensearch=1&form=BESBTB"
e = "aaa"
c = 35

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63"}

html = requests.get(url=url, headers=headers)

strr = html.content.decode()

list = re.findall('<img class.*?alt=', strr)
a = c + 1
b = len(list) + c
while (a < b):
    # print(list[a])
    l = list[a - c - 1]
    s = re.findall('src=.*?alt=', l)
    if (s):
        sstr = re.sub("src=\"", "", s[0])

        sstr = re.sub("\" alt=", "", sstr)
        pic = requests.get(sstr)
        loa = "C:\\Users\\19144\\Desktop\\图片\\p" + e + str(a) + ".jpg"
        with open(loa, 'wb') as file:
            file.write(pic.content)

    a = a + 1

print(len(list))
