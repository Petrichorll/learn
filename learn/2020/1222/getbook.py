# -*- coding: utf-8 -*-
import requests
import re, time
import lxml.html

headers = {"Connection": "keep-alive"
    , "Upgrade-Insecure-Requests": "1"
    ,
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    , "Host": "www.zhuishushenqi.com"}

url = "http://www.zhuishushenqi.com/category?gender=male&major=玄幻&minor=&type=over&page="
#url = "http://www.zhuishushenqi.com/category?gender=male&type=over&major=历史&minor=&page=2"
url_book = "http://www.zhuishushenqi.com"

i = 234
while (i < 928):
    i = i + 1
    time.sleep(1)
    reb = requests.get(url + str(i), headers=headers)
    rebstr = reb.content.decode()
    booklist = re.findall("<a href=\".*\" class=\"book\"", rebstr)

    # print(booklist)
    j = 0
    # while (j < 20):
    #     j = j + 1
    #     bookstr = booklist[j]
    for bookstr in booklist:
        j = j + 1
        tmp = re.sub("<a href=\"", "", bookstr)
        bookurl = re.sub("\" class=\"book\"", "", tmp)
        print("第{}页第{}本：{}。".format(i, j, bookurl))

        time.sleep(0.1)
        reb = requests.get(url_book + bookurl, headers=headers)
        rebstr = reb.content.decode()

        selector = lxml.html.fromstring(rebstr)
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
