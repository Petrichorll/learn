# -*- coding: utf-8 -*-

from selenium import webdriver
import time, re, requests, os, threading

driver = webdriver.Edge()
driver.get(
    "https://static.sporttery.cn/res_1_0/jcw/default/html/kj/dlt.html?url=//www.lottery.gov.cn&cmData={%22advUrl%22:%22/adv%22,%22webApi%22:%22//webapi.sporttery.cn%22,%22resDomain%22:%22//static.sporttery.cn%22,%22res%22:%22//static.sporttery.cn/res_1_0/tcw/default%22,%22domain1%22:%22www.lottery.gov.cn%22,%22domain2%22:%22www.sporttery.cn%22,%22domain3%22:%22m.lottery.gov.cn%22,%22domain4%22:%22m.sporttery.cn%22,%22domain5%22:%22www.lottery.gov.cn%22,%22domain6%22:%22www.sporttery.cn%22,%22domain7%22:%22www.lottery.gov.cn%22,%22domain8%22:%22www.sporttery.cn%22}")
driver.maximize_window()

path1 = "/html/body/div/div/table/tbody/tr[{}]"
path2 = "/html/body/div/div/table/tbody/tr[{}]/td[{}]"
path3 = "/html/body/div/div/div[3]/ul/li[13]"

time.sleep(3)

j = 0
while (True):
    j = j + 1
    i = 0
    hh = driver.find_element_by_xpath(path2.format(j, i + 1)).text
    if (re.findall("21", hh) == []):
        print(hh)
        continue
    while (True):
        i = i + 1
        hh = driver.find_element_by_xpath(path2.format(j, i)).text
        if (i == 1):
            f = open("444.txt", "a")
            f.writelines(hh)
            f.close()
        else:
            f = open("444.txt", "a")
            f.writelines("," + hh)
            f.close()
        if (i == 9):
            f = open("444.txt", "a")
            f.writelines("\n")
            f.close()
            break
    if (j == 30):
        break
