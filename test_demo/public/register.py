# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time, os
import data

url = data.get_url()


class Register(unittest.TestCase):
    register_uers_xpath = "/html/body/div/div/form/div[5]/a[2]/span"

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = url
        self.verificationErrors = []
        self.accept_next_alert = True

    # CAS注册账户用例
    def test_CAS_login(self):
        pass

    @staticmethod
    def register(driver):
        up_list = data.get_un_pw()
        user_name = up_list[0]
        user_pwd = up_list[1]
        # 点击注册用户的按钮
        driver.find_element_by_class_name(Register.register_uers_xpath).click()
        time.sleep(1)
        
        driver.find_element_by_name("account").clear()
        driver.find_element_by_name("account").send_keys(user_name)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(user_pwd)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/form/button").click()
        time.sleep(2)
        driver.refresh()  # 刷新一下页面，8月18号执行时，页面没有自动刷新，所以添加了这一句，其它脚本可能也需要用上
        return driver


if __name__ == "__main__":
    pass
