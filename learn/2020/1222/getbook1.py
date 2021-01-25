# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import requests
import re, time
import lxml.html

headers = {"Connection": "keep-alive"
    , "Upgrade-Insecure-Requests": "1"
    ,
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    , "Host": "www.ixiatxt.com"}

url = "http://www.ixiatxt.com/soft/2/Soft_002_"
url1 = ".html"

i = 570
while (i < 1111):
    i = i + 1
    # time.sleep(1)
    url333 = url + str(i) + url1
    # print(url333)
    reb = requests.get(url333, headers=headers)
    rebstr = reb.content.decode()

    time.sleep(0.1)
    selector = lxml.html.fromstring(rebstr)
    j = 0
    while (j < 20):
        j = j + 1

        shijiandaxiao = selector.xpath("/html/body/div[4]/div[2]/div/ul/li[{}]/div[1]//text()".format(j))

        daxiao = shijiandaxiao[1]
        daxiao1 = float(re.sub("大小：", "", re.sub("MB", "", daxiao)))
        if (daxiao1 < 5.0):
            continue
        shijian = shijiandaxiao[3]
        shijian1 = int(re.sub("更新：", "", re.sub("-.+", "", shijian)))
        if (shijian1 == 2021):
            continue

        # print(shijiandaxiao)

        data = selector.xpath("/html/body/div[4]/div[2]/div/ul/li[{}]/a//text()".format(j))
        book_name1 = data[0]
        if (re.findall("《", book_name1)):
            book_name2 = re.sub("《", "", book_name1)
        else:
            book_name2 = book_name1
        if (re.findall("》全集", book_name2)):
            book_name = re.sub("》全集", "", book_name2)
        else:
            book_name = book_name2
        # print(book_name)
        # time.sleep(1000)
        data = selector.xpath("/html/body/div[4]/div[2]/div/ul/li[{}]/div[2]//text()".format(j))
        if (data == []):
            book_section = '无简介。'
        else:
            book_section = data[0]
        book_section = book_section.strip()
        book_allnum = re.sub("大小：", "", daxiao)
        bookinfo = book_name + "," + book_allnum + "," + book_section

        print("第{}页第{}本：{}，大小：{}。".format(i, j, book_name, book_allnum))
        # print(bookinfo)

        # print(data)

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
