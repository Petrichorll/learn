# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, lxml


class Baidu(unittest.TestCase):
    eurl = []
    furl = []

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://jtj.cq.gov.cn"
        self.verificationErrors = []

    # 搜索
    def test_12345(self):
        driver = self.driver

        lstr = r"http://www.cq.gov.cn/"
        f = open("C:\\Users\\19144\\Desktop\\eurl.txt", 'r')
        i = 1
        for surl in f.readlines():
            surl = surl.replace('\n', '')
            if (i == 1):
                self.furl.append(surl)
                if (surl == lstr):
                    i = 0
            else:
                self.eurl.append(surl)
        f.close()

        # self.eurl.append(self.base_url)
        while (self.eurl != None):
            driver.get(self.eurl[0])
            driver.maximize_window()
            time.sleep(0.1)
            Baidu.ppp(driver)
            try:
                html = driver.find_element_by_xpath("/html/body").get_attribute('outerHTML')
            except:
                html = "网页解析失败(项目五标段)"

            a0 = re.findall("项目五标段", html)
            a1 = re.findall("薄熙来", html)
            a2 = re.findall("邓恢林", html)
            a3 = re.findall("孙政才", html)
            a4 = re.findall("王立军", html)
            a5 = re.findall("薄王", html)
            a6 = re.findall("遗毒", html)
            if (a0 != []):
                f = open("C:\\Users\\19144\\Desktop\\55.txt", 'a')
                f.writelines("项目五标段," + self.eurl[0] + '\n')
                f.close()
            if (a1 != []):
                f = open("C:\\Users\\19144\\Desktop\\33.txt", 'a')
                f.writelines("薄熙来," + self.eurl[0] + '\n')
                f.close()
            if (a2 != []):
                f = open("C:\\Users\\19144\\Desktop\\33.txt", 'a')
                f.writelines("邓恢林," + self.eurl[0] + '\n')
                f.close()
            if (a3 != []):
                f = open("C:\\Users\\19144\\Desktop\\33.txt", 'a')
                f.writelines("孙政才," + self.eurl[0] + '\n')
                f.close()
            if (a4 != []):
                f = open("C:\\Users\\19144\\Desktop\\33.txt", 'a')
                f.writelines("王立军," + self.eurl[0] + '\n')
                f.close()
            if (a5 != []):
                f = open("C:\\Users\\19144\\Desktop\\33.txt", 'a')
                f.writelines("薄王," + self.eurl[0] + '\n')
                f.close()
            if (a6 != []):
                f = open("C:\\Users\\19144\\Desktop\\33.txt", 'a')
                f.writelines("遗毒," + self.eurl[0] + '\n')
                f.close()

            hz = re.findall(r'[\u4e00-\u9fa5]', html)
            count_zh = str(len(hz))
            h = open("C:\\Users\\19144\\Desktop\\44.txt", 'a')
            h.writelines(self.eurl[0] + "," + str(count_zh) + '\n')
            h.close()
            self.furl.append(self.eurl[0])
            del (self.eurl[0])
            '''
            while (self.eurl[0] in Baidu.furl):
                del (self.eurl[0])
                if (self.eurl is None):
                    break
            '''

    @staticmethod
    def ppp(driver):

        urls = driver.find_elements_by_xpath("//a")
        for ur3l in urls:

            try:
                uurl = ur3l.get_attribute("href")
            except:
                continue
            try:
                if (uurl in Baidu.eurl):
                    continue
            except:
                continue
            try:
                if (uurl in Baidu.furl):
                    continue
            except:
                continue

            try:
                aaa = re.findall("www\.cq\.gov\.cn", uurl)
            except:
                continue

            # try:
            #     tt1 = re.findall("\.doc", uurl)
            # except:
            #     continue
            #
            # try:
            #     tt2 = re.findall("\.docx", uurl)
            # except:
            #     continue
            # try:
            #     tt3 = re.findall("\.xls", uurl)
            # except:
            #     continue
            # try:
            #     tt4 = re.findall("\.xlsx", uurl)
            # except:
            #     continue
            # try:
            #     tt5 = re.findall("\.pdf", uurl)
            # except:
            #     continue
            # try:
            #     tt6 = re.findall("\.rar", uurl)
            # except:
            #     continue
            # try:
            #     tt7 = re.findall("\.zip", uurl)
            # except:
            #     continue
            # try:
            #     tt8 = re.findall("\.7z", uurl)
            # except:
            #     continue
            # if (tt1 or tt2 or tt3 or tt4 or tt5 or tt6 or tt7 or tt8):
            #     continue

            if (aaa):
                if (uurl[-5:] == ".html" or uurl[-1] == "/"):
                    Baidu.eurl.append(uurl)
                    l = open("C:\\Users\\19144\\Desktop\\eurl.txt", 'a')
                    l.writelines(uurl + "\n")
                    l.close()
