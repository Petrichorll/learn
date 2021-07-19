# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import requests
import re, time
import lxml.html

headers = {"Connection": "keep-alive"
    , "Upgrade-Insecure-Requests": "1"
    ,
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    , "Host": "m.x55zw.org"}

url = "https://m.x55zw.org/wapbook/11723_"
num = 951175
url2 = ".html"

url_book = "http://www.zhuishushenqi.com"
f = open("C:\\Users\\19144\\Desktop\\xs\\keai.txt", 'a',encoding='gbk')

i = 0
while (i < 928):
    i = i + 1
    num = num + 1
    time.sleep(1)
    reb = requests.get(url + str(num) + url2, headers=headers)
    rebstr = reb.content.decode(encoding='gbk')
    selector = lxml.html.fromstring(rebstr)
    data2 = selector.xpath("//*[@id='nr_title']//text()")
    data = selector.xpath("//*[@id='nr1']//text()")

    tit = re.split("\d+", data2[0])
    print(tit[1])
    f.writelines("第{}章 ".format(i) + tit[1])
    for strr in data:
        strr.encode("gbk")
        f.writelines(strr)
    time.sleep(1000)

    j = 0
    for bookstr in booklist:
        j = j + 1
        tmp = re.sub("<a href=\"", "", bookstr)
        bookurl = re.sub("\" class=\"book\"", "", tmp)
        print("第{}页第{}本：{}。".format(i, j, bookurl))

        time.sleep(0.1)
        reb = requests.get(url_book + bookurl, headers=headers)

        data = selector.xpath("//p[@class='sup']//text()")
        book_allnum = data[4]
        booknum = int(re.sub("万字", "", book_allnum))

        if (booknum > 300):
            data = selector.xpath("/html/body/div[3]/div[2]/div[1]/div/h1//text()")
            book_name = data[0]
            data = selector.xpath("/html/body/div[3]/div[2]/div[3]/p//text()")
            book_section = data[0]
            book_section = book_section.strip()
            bookinfo = book_name + "," + book_allnum + "," + book_section
            print(bookinfo)

            if (re.findall("系统", book_name)):
                f = open("C:\\Users\\19144\\Desktop\\xs\\xz\\booklist1.csv", "a")
                f.writelines("\n" + bookinfo)
                f.close()
            elif (re.findall("医", book_name)):
                f = open("C:\\Users\\19144\\Desktop\\xs\\xz\\booklist2.csv", "a")
                f.writelines("\n" + bookinfo)
                f.close()
            elif (re.findall("修", book_name) or re.findall("仙", book_name)):
                f = open("C:\\Users\\19144\\Desktop\\xs\\xz\\booklist3.csv", "a")
                f.writelines("\n" + bookinfo)
                f.close()
            else:
                f = open("C:\\Users\\19144\\Desktop\\xs\\xz\\booklist.csv", "a")
                f.writelines("\n" + bookinfo)
                f.close()
