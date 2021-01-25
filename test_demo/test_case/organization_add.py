# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time

import sys

sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")

import login, data, workxls
from selenium.webdriver.common.action_chains import ActionChains


# 组织新增
class Organization_Add(unittest.TestCase):
    organization_add_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[1]/button"  # 新增组织按钮的xpath
    organization_name_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div/div/div[1]/input"  # 输入名称编辑框的xpath
    organization_add_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
    organization_add_cancel_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[2]/span"  # 取消按钮的xpath
    organization_1_name_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div"  # 第一条组织名称的xpath
    menubar_orgmanagement_xpath = "//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[5]"

    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 组织新增用例
    def test_Organization_Add(self):
        driver = self.driver
        name = data.get_some_name()  # 获取一些名字字符串
        # time.sleep(1)
        # 点击菜单栏组织管理
        driver.find_element_by_xpath(Organization_Add.menubar_orgmanagement_xpath).click()
        time.sleep(2)  # 预留时间查看
        # 点击新增组织按钮，弹出新增框
        driver.find_element_by_xpath(self.organization_add_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(self.organization_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(self.organization_add_button_xpath).click()  # 重新点击新增组织按钮
        time.sleep(1)
        # 什么都不输入，点击确定，提示报错
        driver.find_element_by_xpath(self.organization_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入一个汉字字符，点击确定，提示报错
        driver.find_element_by_xpath(self.organization_name_input_xpath).send_keys(name[0])
        driver.find_element_by_xpath(self.organization_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入一个数字字符，点击确定，提示报错
        driver.find_element_by_xpath(self.organization_name_input_xpath).clear()
        driver.find_element_by_xpath(self.organization_name_input_xpath).send_keys(name[1])
        driver.find_element_by_xpath(self.organization_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入一个英文字符，点击确定，提示报错
        driver.find_element_by_xpath(self.organization_name_input_xpath).clear()
        driver.find_element_by_xpath(self.organization_name_input_xpath).send_keys(name[2])
        driver.find_element_by_xpath(self.organization_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入一个特殊符号，点击确定，提示报错
        driver.find_element_by_xpath(self.organization_name_input_xpath).clear()
        driver.find_element_by_xpath(self.organization_name_input_xpath).send_keys(name[3])
        driver.find_element_by_xpath(self.organization_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(self.organization_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(self.organization_add_button_xpath).click()  # 重新点击新增组织按钮
        time.sleep(1)
        # 输入13个汉字字符，点击确定，提示报错
        driver.find_element_by_xpath(self.organization_name_input_xpath).clear()
        driver.find_element_by_xpath(self.organization_name_input_xpath).send_keys(name[4])
        driver.find_element_by_xpath(self.organization_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入12个数字字符，点击确定，提示报错
        driver.find_element_by_xpath(self.organization_name_input_xpath).clear()
        driver.find_element_by_xpath(self.organization_name_input_xpath).send_keys(name[5])
        driver.find_element_by_xpath(self.organization_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入11个英文字符，点击确定，提示报错
        driver.find_element_by_xpath(self.organization_name_input_xpath).clear()
        driver.find_element_by_xpath(self.organization_name_input_xpath).send_keys(name[6])
        driver.find_element_by_xpath(self.organization_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入6个汉字+符号，点击确定，提示报错
        driver.find_element_by_xpath(self.organization_name_input_xpath).clear()
        driver.find_element_by_xpath(self.organization_name_input_xpath).send_keys(name[7])
        driver.find_element_by_xpath(self.organization_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(self.organization_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(self.organization_add_button_xpath).click()  # 重新点击新增组织按钮
        time.sleep(1)
        # 输入6个数字+符号，点击确定，提示报错

        driver.find_element_by_xpath(self.organization_name_input_xpath).clear()
        driver.find_element_by_xpath(self.organization_name_input_xpath).send_keys(name[8])
        driver.find_element_by_xpath(self.organization_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入6个字母+符号，点击确定，提示报错
        driver.find_element_by_xpath(self.organization_name_input_xpath).clear()
        driver.find_element_by_xpath(self.organization_name_input_xpath).send_keys(name[9])
        driver.find_element_by_xpath(self.organization_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入2个汉字，点击确定，新增成功
        driver.find_element_by_xpath(self.organization_name_input_xpath).clear()
        driver.find_element_by_xpath(self.organization_name_input_xpath).send_keys(name[10])
        driver.find_element_by_xpath(self.organization_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入5个数字，点击确定，新增成功
        driver.find_element_by_xpath(self.organization_add_button_xpath).click()  # 点击新增组织
        driver.find_element_by_xpath(self.organization_name_input_xpath).clear()
        driver.find_element_by_xpath(self.organization_name_input_xpath).send_keys(name[11])
        driver.find_element_by_xpath(self.organization_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(self.organization_add_button_xpath).click()  # 点击新增组织
        driver.find_element_by_xpath(self.organization_add_cancel_button_xpath).click()
        time.sleep(1)
        # 输入10个字母，点击确定，新增成功
        driver.find_element_by_xpath(self.organization_add_button_xpath).click()  # 点击新增组织
        driver.find_element_by_xpath(self.organization_name_input_xpath).clear()
        driver.find_element_by_xpath(self.organization_name_input_xpath).send_keys(name[12])
        driver.find_element_by_xpath(self.organization_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入6位汉字数字字母混合，点击确定，新增成功
        driver.find_element_by_xpath(self.organization_add_button_xpath).click()  # 点击新增组织
        driver.find_element_by_xpath(self.organization_name_input_xpath).clear()
        driver.find_element_by_xpath(self.organization_name_input_xpath).send_keys(name[13])
        driver.find_element_by_xpath(self.organization_add_confirm_button_xpath).click()
        time.sleep(2)
        # 输入已存在的组织名称，点击确定，提示报错
        driver.find_element_by_xpath(self.organization_add_button_xpath).click()  # 点击新增组织
        driver.find_element_by_xpath(self.organization_name_input_xpath).clear()
        driver.find_element_by_xpath(self.organization_name_input_xpath).send_keys(name[13])
        driver.find_element_by_xpath(self.organization_add_confirm_button_xpath).click()
        time.sleep(1)

        time.sleep(3)
        time.sleep(3)
        driver.close()

    @staticmethod
    def OrganizationAdd(driver, writedata=0, sorf=0):
        name = data.get_some_name()
        namestr = name[13]
        time.sleep(1)
        # 如果成功或者失败参数为1，则找一个存在的组织名称，赋值给namestr
        if (sorf == 1):
            namestr = driver.find_element_by_xpath(Organization_Add.organization_1_name_xpath).text
        time.sleep(1)
        # 点击新增组织按钮，弹出新增框
        driver.find_element_by_xpath(Organization_Add.organization_add_button_xpath).click()
        driver.find_element_by_xpath(Organization_Add.organization_name_input_xpath).clear()
        driver.find_element_by_xpath(Organization_Add.organization_name_input_xpath).send_keys(namestr)
        time.sleep(1)
        driver.find_element_by_xpath(Organization_Add.organization_add_confirm_button_xpath).click()

        if writedata:
            timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            workxls.writedata('orgdata.xls', namestr, timestr)

        # 如果成功或者失败参数为1，则需要点击取消
        if (sorf == 1):
            time.sleep(1)
            driver.find_element_by_xpath(Organization_Add.organization_add_cancel_button_xpath).click()
        return driver

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
