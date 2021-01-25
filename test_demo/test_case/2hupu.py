# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re


class Hupu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://bbs.hupu.com/pubg/"
        self.verificationErrors = []
        self.accept_next_alert = True

    # 用例
    def test_hupu(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='ajaxtable']/div[1]/ul/li[2]/div[1]/a").click()
        time.sleep(200)
        driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
