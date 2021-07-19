# -*- coding: utf-8 -*-

from selenium import webdriver
import time, re, requests, os, threading

driver = webdriver.Edge()
driver.get("https://weibo.com")
driver.maximize_window()

for i in range(30, 0, -1):
    print(i)
    time.sleep(1)

headers = {"Connection": "keep-alive"
    , "Upgrade-Insecure-Requests": "1"
    ,
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

gjz = ""
fpath = "C:\\Users\\19144\\Desktop\\微博\\{}\\".format(gjz)
i = 1
if not os.path.exists(fpath):
    os.makedirs(fpath)
hh_xpath = "/html/body/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div[1]/div/div/video"
f = open("C:\\Users\\19144\\Desktop\\微博\\322.txt", 'r')


def getmp4(hstr, i):
    reb = requests.get(hstr, headers=headers)
    with open(fpath + "{}{}.mp4".format(gjz, i), 'ab') as file:
        file.write(reb.content)
        file.flush()


for sstr in f.readlines():
    if (re.findall(gjz, sstr)):
        kk = re.split(',', sstr)
        driver.get(kk[1])
        time.sleep(2)

        try:
            mp4str = driver.find_element_by_xpath(hh_xpath).get_attribute('outerHTML')
        except:
            mp4str = "444"
            continue
        rebstr = re.findall("src=.+><", mp4str)
        hstr = re.sub("src=\"", '', rebstr[0])
        hstr = re.sub("\"><", '', hstr)
        hstr = re.sub("&amp;", '&', hstr)
        hstr = "https:" + hstr

        isif = input("是否下载{}的这个视频？".format(gjz))
        if (isif == "0"):
            continue
        else:
            pass

        while (os.path.exists(fpath + "{}{}.mp4".format(gjz, i))):
            i = i + 1
        t1 = threading.Thread(target=getmp4, args=(hstr, i,))
        i = i + 1
        t1.start()
        while (threading.active_count() > 4):
            print("当前下载任务超过4个，等待下载完成...")
            time.sleep(1)
f.close()
