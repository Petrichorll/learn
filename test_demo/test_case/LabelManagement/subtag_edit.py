# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, random
import sys, re

sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")
import login, data, workxls, subtag_add
from selenium.webdriver.common.action_chains import ActionChains


# 子标签编辑(修改)
class Subtag_Edit(unittest.TestCase):
    label_management_xpath = "/html/body/div/div/div[1]/div[2]/div[1]/div/ul[1]/div[10]/a/li"  # 标签管理菜单的xpath
    subtag_edit_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div[3]/table/tbody/tr[{}]/td[5]/div/a[1]/span"  # 编辑子标签按钮
    subtag_name_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[2]/div/div/input"  # 输入子标签名称编辑框的xpath
    subtag_edit_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
    subtag_edit_cancel_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[2]/span"  # 取消按钮的xpath
    subtag_all_from_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div[3]/table/tbody"

    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    @staticmethod
    def get_subtag_edit_button_xpath(driver):  # 获取编辑子标签按钮的xpath，页面上随机选取一个来编辑，并将光标移动至编辑按钮上
        time.sleep(1)
        all_tr_str = driver.find_element_by_xpath(Subtag_Edit.subtag_all_from_xpath).get_attribute('outerHTML')
        tr_list = re.findall('tr', all_tr_str)
        tr_count = int(len(tr_list) / 2)
        i = random.randint(1, tr_count)
        ret = Subtag_Edit.subtag_edit_button_xpath.format(str(i))
        if i > 5:  # 如果选到了6-10的子标签，下拉滚动条至底部
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
        return ret

    # 子标签编辑用例
    def test_Subtag_Edit(self):
        driver = self.driver
        name = data.get_some_name()  # 获取一些名字字符串

        # 点击菜单栏标签管理
        driver.find_element_by_xpath(Subtag_Edit.label_management_xpath).click()
        time.sleep(1)  # 预留时间查看
        # 选择一个主标签，点击查看子标签按钮
        driver = subtag_add.Subtag_Add.open_subtag_page(driver)
        # 选一个编辑子标签按钮，点击，弹出编辑框
        driver.find_element_by_xpath(Subtag_Edit.get_subtag_edit_button_xpath(driver)).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(
            Subtag_Edit.get_subtag_edit_button_xpath(driver)).click()  # 重新选一个编辑子标签按钮，点击，弹出编辑框
        time.sleep(1)
        # 直接点击确定，提示报错
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_confirm_button_xpath).click()
        time.sleep(1)
        # driver.find_element_by_xpath(self.organization_edit_cancel_button_xpath).click()  # 点击取消
        # # 什么都不输入，点击确定，提示报错
        # driver.find_element_by_xpath(self.get_organization_edit_button_xpath(driver)).click()  # 重新选一个编辑子标签按钮，点击，弹出编辑框
        # driver.find_element_by_xpath(self.organization_name_input_xpath).clear()
        # driver.find_element_by_xpath(self.organization_name_input_xpath).send_keys("")
        # time.sleep(1)
        # driver.find_element_by_xpath(self.organization_edit_confirm_button_xpath).click()
        # time.sleep(100)
        # 输入一个汉字字符，点击确定，提示报错
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).send_keys(name[0])
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入一个数字字符，点击确定，提示报错
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).send_keys(name[1])
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入一个英文字符，点击确定，提示报错
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).send_keys(name[2])
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入一个特殊符号，点击确定，提示报错
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).send_keys(name[3])
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(
            Subtag_Edit.get_subtag_edit_button_xpath(driver)).click()  # 重新选一个编辑子标签按钮，点击，弹出编辑框
        time.sleep(1)
        # 输入13个汉字字符，点击确定，提示报错
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).send_keys(name[4])
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入12个数字字符，点击确定，提示报错
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).send_keys(name[5])
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入11个英文字符，点击确定，提示报错
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).send_keys(name[6])
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入6个汉字+符号，点击确定，提示报错
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).send_keys(name[7])
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(
            Subtag_Edit.get_subtag_edit_button_xpath(driver)).click()  # 重新选一个编辑子标签按钮，点击，弹出编辑框
        time.sleep(1)
        # 输入6个数字+符号，点击确定，提示报错
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).send_keys(name[8])
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入6个字母+符号，点击确定，提示报错
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).send_keys(name[9])
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入2个汉字，点击确定，修改成功
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).send_keys(name[10])
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入5个数字，点击确定，修改成功
        driver.find_element_by_xpath(
            Subtag_Edit.get_subtag_edit_button_xpath(driver)).click()  # 重新选一个编辑子标签按钮，点击，弹出编辑框
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).send_keys(name[11])
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(
            Subtag_Edit.get_subtag_edit_button_xpath(driver)).click()  # 重新选一个编辑子标签按钮，点击，弹出编辑框
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_cancel_button_xpath).click()
        time.sleep(1)
        # 输入10个字母，点击确定，修改成功
        driver.find_element_by_xpath(
            Subtag_Edit.get_subtag_edit_button_xpath(driver)).click()  # 重新选一个编辑子标签按钮，点击，弹出编辑框
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).send_keys(name[12])
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入6位汉字数字字母混合，点击确定，修改成功
        driver.find_element_by_xpath(
            Subtag_Edit.get_subtag_edit_button_xpath(driver)).click()  # 重新选一个编辑子标签按钮，点击，弹出编辑框
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).send_keys(name[13])
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入已存在的子标签名称，点击确定，提示报错
        driver.find_element_by_xpath(
            Subtag_Edit.get_subtag_edit_button_xpath(driver)).click()  # 重新选一个编辑子标签按钮，点击，弹出编辑框
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).clear()
        driver.find_element_by_xpath(Subtag_Edit.subtag_name_input_xpath).send_keys(name[13])
        driver.find_element_by_xpath(Subtag_Edit.subtag_edit_confirm_button_xpath).click()
        time.sleep(1)

        time.sleep(3)
        time.sleep(3)
        driver.close()

    # @staticmethod
    # def OrganizationEdit(driver, writedata=0, sorf=0):
    #     name = data.get_some_name()
    #     namestr = name[13]
    #     time.sleep(1)
    #     # 如果成功或者失败参数为1，则找一个存在的子标签名称，赋值给namestr
    #     if (sorf == 1):
    #         namestr = driver.find_element_by_xpath(
    #             "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div").text
    #     time.sleep(1)
    #     # 选一个编辑子标签按钮，点击，弹出编辑框
    #     driver.find_element_by_xpath(Organization_Edit.get_organization_edit_button_xpath(driver)).click()
    #     time.sleep(1)
    #     driver.find_element_by_xpath(Organization_Edit.organization_name_input_xpath).clear()
    #     driver.find_element_by_xpath(Organization_Edit.organization_name_input_xpath).send_keys(namestr)
    #     driver.find_element_by_xpath(Organization_Edit.organization_edit_confirm_button_xpath).click()
    #     if writedata:
    #         timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #         workxls.writedata('orgdata.xls', namestr, timestr)
    #
    #     # 如果成功或者失败参数为1，则需要点击取消
    #     if (sorf == 1):
    #         time.sleep(1)
    #         driver.find_element_by_xpath(Organization_Edit.organization_edit_cancel_button_xpath).click()
    #     return driver

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
