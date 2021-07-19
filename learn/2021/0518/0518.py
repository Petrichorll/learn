# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import requests
import re, time, os, threading
import lxml.html

headers = {"Connection": "keep-alive"
    , "Upgrade-Insecure-Requests": "1"
    ,
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    , "Host": "mm.yaojiwu.com"}

url = "http://mm.yaojiwu.com/meitu/"
num = 0
url2 = ".html"
x = 0
y = 0
h = 1


def getimg(path1, hstr, i):
    response = requests.get(hstr, headers=headers)
    img = response.content
    with open(path1 + "{}.jpg".format(i), 'wb') as f:
        f.write(img)


while (1):
    num = num + 1
    try:
        reb = requests.get(url + str(num) + url2, headers=headers)
    except:
        break
    rebstr = reb.content.decode(encoding='utf-8')
    selector = lxml.html.fromstring(rebstr)
    while (1):
        x = x + 1
        try:
            data = selector.xpath("/html/body/div[5]/div/div[1]/div[1]/ul/li[{}]//@href".format(x))
            data2 = selector.xpath("/html/body/div[5]/div/div[1]/div[1]/ul/li[{}]/a/span//text()".format(x))
        except:
            x = 0
            continue
        fpath = "C:\\Users\\19144\\Desktop\\图库\\{}\\".format(data2[0])
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        reb1 = requests.get(data[0], headers=headers)
        rebstr1 = reb1.content.decode(encoding='utf-8')
        selector1 = lxml.html.fromstring(rebstr1)
        while (1):
            y = y + 1
            try:
                data3 = selector1.xpath("/html/body/div[5]/div/div[1]/div/div[2]/div[{}]/img//@lz-src".format(y))
            except:
                y = 0
                h = 1
                continue

            t1 = threading.Thread(target=getimg, args=(fpath, data3[0], h,))
            h = h + 1
            t1.start()
            while (threading.active_count() > 5):
                print("当前下载任务超过5个，等待下载完成...")
                time.sleep(1)
