# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, random
import sys, re

sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")
import login, data, workxls
from selenium.webdriver.common.action_chains import ActionChains


# 组织删除
class Organization_Delete(unittest.TestCase):
    organization_delete_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[3]/span/button[1]/span"  # 确定按钮的xpath
    organization_delete_cancel_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[3]/span/button[2]/span"  # 取消按钮的xpath
    menubar_orgmanagement_xpath = "//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[5]"
    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    @staticmethod
    def get_organization_delete_button_xpath(driver):  # 获取删除组织按钮的xpath，页面上随机选取一个来编辑，并将光标移动至删除按钮上
        driver.implicitly_wait(1)
        i = random.randint(1, 10)
        ret = ""
        # driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[5]").click()
        # driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div/ul/li[7]").click()
        while (i):
            # print(i)
            ret = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[2]/div[3]/table/tbody/tr[" + str(
                i) + "]/td[5]/div/a[2]/span"
            try:
                driver.find_element_by_xpath(ret)
                driver.implicitly_wait(30)
                break
            except:
                i = i - 1
        if i > 5:  # 如果选到了6-10的组织，下拉滚动条至底部
            js = "var q=document.documentElement.scrollTop=10000"
            driver.execute_script(js)
            time.sleep(1)
        else:
            js = "var q=document.documentElement.scrollTop=0"
            driver.execute_script(js)
            time.sleep(1)
        above = driver.find_element_by_xpath(ret)  # 移动光标至删除按钮
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(3)  # 预留时间查看效果
        return ret

    # 组织删除用例
    def test_Organization_Delete(self):
        driver = self.driver

        # 点击菜单栏组织管理
        driver.find_element_by_xpath(Organization_Delete.menubar_orgmanagement_xpath).click()
        time.sleep(1)  # 预留时间查看
        # 选一个删除组织按钮，点击，弹出确认框
        driver.find_element_by_xpath(self.get_organization_delete_button_xpath(driver)).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(self.organization_delete_cancel_button_xpath).click()
        time.sleep(1)
        # 点击确定，直接删除
        driver.find_element_by_xpath(self.get_organization_delete_button_xpath(driver)).click()  # 重新选一个删除组织按钮，点击，弹出确认框
        time.sleep(1)
        driver.find_element_by_xpath(self.organization_delete_confirm_button_xpath).click()
        time.sleep(1)

    @staticmethod
    def OrganizationDelete(driver):
        # 选一个删除组织按钮，点击，弹出确认框
        one_orgd_xpath = Organization_Delete.get_organization_delete_button_xpath(driver)
        # 记录一下删除组织的名称
        one_orgn_xpath = one_orgd_xpath
        one_orgn_xpath = one_orgn_xpath.replace("]/td[5]/div/a[2]/span", "]/td[2]/div")
        namestr = driver.find_element_by_xpath(one_orgn_xpath).text
        driver.find_element_by_xpath(one_orgd_xpath).click()
        time.sleep(1)
        # 点击确定，直接删除
        driver.find_element_by_xpath(Organization_Delete.organization_delete_confirm_button_xpath).click()
        timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        time.sleep(2)
        workxls.writedata('orgdata.xls', namestr, timestr)
        return driver

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
