# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, random
import sys

sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")

import login, data,workxls
from selenium.webdriver.common.action_chains import ActionChains


class Subtag_Add(unittest.TestCase):
    label_management_xpath = "/html/body/div/div/div[1]/div[2]/div[1]/div/ul[1]/div[10]/a/li"  # 标签管理菜单的xpath
    subtag_in_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div[3]/table/tbody/tr[{}]/td[5]/div/a[1]/span"  # 进入主标签按钮

    subtag_add_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[1]/button/span"  # 新增子标签按钮的xpath
    subtag_name_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[2]/div/div[1]/input"  # 输入子标签名称编辑框的xpath
    subtag_add_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
    subtag_add_cancel_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[2]/span"  # 取消按钮的xpath
    ml_all_from_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div[3]/table/tbody"
    form_bland_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[1]"  # 窗口空白处的xpath

    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    @staticmethod
    def open_subtag_page(driver):  # 选择一个主标签，打开其子标签页面
        # driver.implicitly_wait(1)
        # i = random.randint(1, 10)
        # i = 1
        # ret = ""
        # while (i):
        #     # print(i)
        #     ret = Subtag_Add.subtag_in_button_xpath.format(str(i))
        #     try:
        #         driver.find_element_by_xpath(ret)
        #         driver.implicitly_wait(30)
        #         break
        #     except:
        #         i = i - 1
        time.sleep(1)
        all_tr_str = driver.find_element_by_xpath(Subtag_Add.ml_all_from_xpath).get_attribute('outerHTML')
        tr_list = re.findall('tr', all_tr_str)
        tr_count = int(len(tr_list) / 2)
        i = random.randint(1, tr_count)
        i = 1
        ret = Subtag_Add.subtag_in_button_xpath.format(str(i))
        if i > 5:  # 如果选到了6-10的主标签，下拉滚动条至底部
            js = "var q=document.documentElement.scrollTop=10000"
            driver.execute_script(js)
            time.sleep(1)
        else:
            js = "var q=document.documentElement.scrollTop=0"
            driver.execute_script(js)
            time.sleep(1)
        above = driver.find_element_by_xpath(ret)  # 移动光标至编辑按钮
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(2)  # 预留时间查看效果
        driver.find_element_by_xpath(ret).click()
        return driver

    # 增加子标签
    def test_Subtag_Add(self):
        driver = self.driver
        time.sleep(1)
        # 点击菜单栏标签管理
        driver.find_element_by_xpath(Subtag_Add.label_management_xpath).click()
        time.sleep(1)  # 预留时间查看
        name = data.get_some_name()
        # 选择一个主标签，点击查看子标签按钮
        driver = Subtag_Add.open_subtag_page(driver)
        time.sleep(1)
        # 点击新增子标签按钮，弹出新增框
        driver.find_element_by_xpath(Subtag_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(Subtag_Add.subtag_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Subtag_Add.subtag_add_button_xpath).click()  # 重新点击新增标签按钮
        time.sleep(1)
        # 不输入任何字符，点击确定，提示报错
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).send_keys(name[0])
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Add.subtag_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入一个汉字字符，点击空白处，提示报错
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).send_keys(name[0])
        driver.find_element_by_xpath(Subtag_Add.form_bland_xpath).click()
        time.sleep(1)
        # 输入一个数字字符，点击空白处，提示报错
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).send_keys(name[1])
        driver.find_element_by_xpath(Subtag_Add.form_bland_xpath).click()
        time.sleep(1)
        # 输入一个英文字符，点击空白处，提示报错
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).send_keys(name[2])
        driver.find_element_by_xpath(Subtag_Add.form_bland_xpath).click()
        time.sleep(1)
        # 输入一个特殊符号，点击空白处，提示报错
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).send_keys(name[3])
        driver.find_element_by_xpath(Subtag_Add.form_bland_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(Subtag_Add.subtag_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Subtag_Add.subtag_add_button_xpath).click()  # 重新点击新增标签按钮
        time.sleep(1)
        # 输入13个汉字字符，点击空白处，提示报错
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).send_keys(name[4])
        driver.find_element_by_xpath(Subtag_Add.form_bland_xpath).click()
        time.sleep(1)
        # 输入12个数字字符，点击空白处，提示报错
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).send_keys(name[5])
        driver.find_element_by_xpath(Subtag_Add.form_bland_xpath).click()
        time.sleep(1)
        # 输入11个英文字符，点击空白处，提示报错
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).send_keys(name[6])
        driver.find_element_by_xpath(Subtag_Add.form_bland_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(Subtag_Add.subtag_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Subtag_Add.subtag_add_button_xpath).click()  # 重新点击新增标签按钮
        time.sleep(1)
        # 输入6个汉字+符号，点击空白处，提示报错
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).send_keys(name[7])
        driver.find_element_by_xpath(Subtag_Add.form_bland_xpath).click()
        time.sleep(1)
        # 输入6个数字+符号，点击空白处，提示报错
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).send_keys(name[8])
        driver.find_element_by_xpath(Subtag_Add.form_bland_xpath).click()
        time.sleep(1)
        # 输入6个字母+符号，点击空白处，提示报错
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).send_keys(name[9])
        driver.find_element_by_xpath(Subtag_Add.form_bland_xpath).click()
        time.sleep(1)
        # 输入2个汉字，点击空白处，合法，不提示报错
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).send_keys(name[10])
        driver.find_element_by_xpath(Subtag_Add.form_bland_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(Subtag_Add.subtag_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Subtag_Add.subtag_add_button_xpath).click()  # 重新点击新增标签按钮
        time.sleep(1)
        # 输入5个数字，点击空白处，合法，不提示报错
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).send_keys(name[11])
        driver.find_element_by_xpath(Subtag_Add.form_bland_xpath).click()
        time.sleep(1)
        # 输入10个字母，点击空白处，合法，不提示报错
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).send_keys(name[12])
        driver.find_element_by_xpath(Subtag_Add.form_bland_xpath).click()
        time.sleep(1)

        # 输入6位汉字数字字母混合，点击空白处，合法，不提示报错
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).send_keys(name[13])
        driver.find_element_by_xpath(Subtag_Add.form_bland_xpath).click()
        time.sleep(1)

        # 点击确定，新增成功
        driver.find_element_by_xpath(Subtag_Add.subtag_add_confirm_button_xpath).click()

        time.sleep(1)
        driver.close()

    @staticmethod
    def SubtagAdd(driver, writedata=0, sorf=0):  # 新增子标签
        name = data.get_some_name()
        namestr = name[13]
        time.sleep(1)
        # 如果成功或者失败参数为1，则找一个存在的主标签名称，赋值给namestr
        if (sorf == 1):
            pass
            # namestr = driver.find_element_by_xpath(Organization_Add.organization_1_name_xpath).text
        time.sleep(1)
        # 点击新增标签按钮，弹出新增框
        driver.find_element_by_xpath(Subtag_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Add.subtag_name_input_xpath).send_keys(name[13])
        driver.find_element_by_xpath(Subtag_Add.form_bland_xpath).click()
        time.sleep(1)
        # 点击确定，新增成功
        driver.find_element_by_xpath(Subtag_Add.subtag_add_confirm_button_xpath).click()
        if writedata:
            timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            workxls.writedata('subtagdata.xls', namestr, timestr)

        # 如果成功或者失败参数为1，则需要点击取消
        if (sorf == 1):
            time.sleep(1)
            pass
            # driver.find_element_by_xpath(Organization_Add.organization_add_cancel_button_xpath).click()
        return driver

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
