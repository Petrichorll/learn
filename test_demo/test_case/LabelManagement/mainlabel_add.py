# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, random
import sys

sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")

import login, data, workxls


class Mainlabel_Add(unittest.TestCase):
    label_management_xpath = "/html/body/div/div/div[1]/div[2]/div[1]/div/ul[1]/div[10]/a/li"  # 标签管理菜单的xpath
    # "//*[@id="app"]/div/div[2]/div[2]/div[1]/div/ul[1]/div[10]/a/li/span"
    mainlabel_add_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[1]/button/span"  # 新增主标签按钮的xpath
    mainlabel_name_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[1]/div/div[1]/input"  # 输入主标签名称编辑框的xpath
    mainlabel_add_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
    mainlabel_add_cancel_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[2]/span"  # 取消按钮的xpath

    subtag_add_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[2]/div/button/span"  # 子标签的预备输入按钮的xpath
    subtag_add_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[2]/div/div[1]/input"
    subtag_text_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[2]/div/span"  # 子标签名字文本的xpath
    form_bland_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[1]"  # 窗口空白处的xpath
    subtag_delete_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[2]/div/span[{}]/i"  # 子标签的删除按钮的xpath

    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 增加主标签
    def test_Mainlabel_Add(self):
        driver = self.driver

        print(Mainlabel_Add.label_management_xpath)
        time.sleep(2)
        # 点击菜单栏标签管理
        driver.find_element_by_xpath(Mainlabel_Add.label_management_xpath).click()
        time.sleep(2)  # 预留时间查看
        name = data.get_some_name()
        # 点击新增标签按钮，弹出新增框
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_add_button_xpath).click()
        time.sleep(1)

        # 点击取消，回到界面
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_add_button_xpath).click()  # 重新点击新增标签按钮
        time.sleep(1)      
        # 不输入任何字符，点击预备输入子标签，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(name[0])
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        # 主标签输入一个汉字字符，点击预备输入子标签，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(name[0])
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        # 输入一个数字字符，点击预备输入子标签，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(name[1])
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        # 输入一个英文字符，点击预备输入子标签，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(name[2])
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        # 输入一个特殊符号，点击预备输入子标签，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(name[3])
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_add_button_xpath).click()  # 重新点击新增标签按钮
        time.sleep(1)
        # 输入13个汉字字符，点击预备输入子标签，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(name[4])
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        # 输入12个数字字符，点击预备输入子标签，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(name[5])
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        # 输入11个英文字符，点击预备输入子标签，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(name[6])
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_add_button_xpath).click()  # 重新点击新增标签按钮
        time.sleep(1)
        # 输入6个汉字+符号，点击预备输入子标签，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(name[7])
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        # 输入6个数字+符号，点击预备输入子标签，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(name[8])
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        # 输入6个字母+符号，点击预备输入子标签，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(name[9])
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        # 输入2个汉字，点击预备输入子标签，合法，不提示报错
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(name[10])
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_add_button_xpath).click()  # 重新点击新增标签按钮
        time.sleep(1)
        # 输入5个数字，点击预备输入子标签，合法，不提示报错
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(name[11])
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        # 输入10个字母，点击预备输入子标签，合法，不提示报错
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(name[12])
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)

        # 输入6位汉字数字字母混合，点击预备输入子标签，合法，不提示报错
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(name[13])
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)

        # 检查子标签的输入和删除，subtagnum表示最终需要子标签的数量,1<=subtagnum<=10
        subtagnum = 1
        conut = 0
        while (conut < subtagnum):
            if (conut != 0):
                driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
            driver = Mainlabel_Add.check_subtag_write(driver)
            conut = conut + 1
            if (conut == subtagnum):
                break
            driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
            driver = Mainlabel_Add.check_subtag_write(driver)
            conut = conut + 1
            i = random.randint(1, conut)
            driver.find_element_by_xpath(Mainlabel_Add.subtag_delete_button_xpath.format(i)).click()
            time.sleep(1)
            conut = conut - 1

        # 点击确定，新增成功
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_add_confirm_button_xpath).click()
        time.sleep(1)


        # 输入相同的主标签名称，新增，提示失败
        # 点击新增标签按钮，弹出新增框
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_add_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(name[13])
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).send_keys("st"+name[13])
        time.sleep(1)
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_add_confirm_button_xpath).click()
        time.sleep(1)


        driver.close()

    @staticmethod
    def check_subtag_write(driver):
        time.sleep(1)
        name = data.get_some_name()
        # 子标签不输入任何字符，点击空白处，提示报错，或者出现下一个子标签输入框

        # try:
        #     tagstr = driver.find_element_by_xpath(Mainlabel_Add.subtag_text_xpath).text
        #     print(tagstr)
        #     move_focus_xpath = Mainlabel_Add.form_bland_xpath
        # except:
        #     move_focus_xpath = Mainlabel_Add.mainlabel_add_confirm_button_xpath
        # driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).send_keys(name[0])
        # driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).clear()

        driver.find_element_by_xpath(Mainlabel_Add.form_bland_xpath).click()  # 直接点击空白
        time.sleep(1)

        # 子标签输入一个汉字字符，点击空白处，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()  # 重新点击子标签输入按钮，触发输入事件
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).send_keys(name[0])
        driver.find_element_by_xpath(Mainlabel_Add.form_bland_xpath).click()
        time.sleep(1)
        # 子标签输入一个数字字符，点击空白处，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).send_keys(name[1])
        driver.find_element_by_xpath(Mainlabel_Add.form_bland_xpath).click()
        time.sleep(1)
        # 子标签输入一个英文字符，点击空白处，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).send_keys(name[2])
        driver.find_element_by_xpath(Mainlabel_Add.form_bland_xpath).click()
        time.sleep(1)
        # 子标签输入一个特殊符号，点击空白处，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).send_keys(name[3])
        driver.find_element_by_xpath(Mainlabel_Add.form_bland_xpath).click()
        time.sleep(1)
        # 子标签输入13个汉字字符，点击空白处，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).send_keys(name[4])
        driver.find_element_by_xpath(Mainlabel_Add.form_bland_xpath).click()
        time.sleep(1)
        # 子标签输入12个数字字符，点击空白处，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).send_keys(name[5])
        driver.find_element_by_xpath(Mainlabel_Add.form_bland_xpath).click()
        time.sleep(1)
        # 子标签输入11个英文字符，点击空白处，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).send_keys(name[6])
        driver.find_element_by_xpath(Mainlabel_Add.form_bland_xpath).click()
        time.sleep(1)
        # 子标签输入6个汉字+符号，点击空白处，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).send_keys(name[7])
        driver.find_element_by_xpath(Mainlabel_Add.form_bland_xpath).click()
        time.sleep(1)
        # 子标签输入6个数字+符号，点击空白处，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).send_keys(name[8])
        driver.find_element_by_xpath(Mainlabel_Add.form_bland_xpath).click()
        time.sleep(1)
        # 子标签输入6个字母+符号，点击空白处，提示报错
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).send_keys(name[9])
        driver.find_element_by_xpath(Mainlabel_Add.form_bland_xpath).click()
        time.sleep(1)
        # 子标签输入6位汉字数字字母混合，点击空白处，合法，不提示报错，显示出下一个子标签输入按钮
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).send_keys(name[13])
        driver.find_element_by_xpath(Mainlabel_Add.form_bland_xpath).click()
        time.sleep(1)

        return driver

    @staticmethod
    def MainlabelAdd(driver, writedata=0, sorf=0):  # 新增主标签
        name = data.get_some_name()
        namestr = name[13]
        time.sleep(1)
        # 如果成功或者失败参数为1，则找一个存在的主标签名称，赋值给namestr
        if (sorf == 1):
            pass
            # namestr = driver.find_element_by_xpath(Organization_Add.organization_1_name_xpath).text
        time.sleep(1)
        # 点击新增标签按钮，弹出新增框
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_add_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).clear()
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_name_input_xpath).send_keys(namestr)
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Mainlabel_Add.subtag_add_input_xpath).send_keys("st" + namestr)
        driver.find_element_by_xpath(Mainlabel_Add.form_bland_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Mainlabel_Add.mainlabel_add_confirm_button_xpath).click()
        if writedata:
            timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            workxls.writedata('mainlabeldata.xls', namestr, timestr)

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
