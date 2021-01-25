# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, random
import sys

sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")
import login, data, workxls
from selenium.webdriver.common.action_chains import ActionChains


# 角色新增
class Role_Add(unittest.TestCase):
    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 角色新增用例
    def test_Role_Add(self):
        driver = self.driver
        name = data.get_some_name()  # 获取一些名字字符串
        role_add_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[1]/button/span"  # 新增角色按钮的xpath
        role_name_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[2]/div/div[1]/input"  # 输入名称编辑框的xpath
        role_add_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
        role_add_cancel_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[2]/span"  # 取消按钮的xpath
        org_list_show_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[1]/div/div/div/span"  # 打开选择组织下拉框
        org_choice_xpath = "/html/body/div[3]/div[1]/div[1]/ul/li[1]/span"  # 选择第一个组织
        time.sleep(1)
        # 点击菜单栏角色管理
        driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[6]").click()
        time.sleep(1)  # 预留时间查看
        # 点击新增角色按钮，弹出新增框
        driver.find_element_by_xpath(role_add_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(role_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(role_add_button_xpath).click()  # 重新点击新增角色按钮
        time.sleep(1)
        # 什么都不输入，点击确定，提示报错
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(1)
        # 选择一个组织，点击确定，提示报错
        driver.find_element_by_xpath(org_list_show_xpath).click()
        driver.find_element_by_xpath(org_choice_xpath).click()
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入一个汉字字符，点击确定，提示报错
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(name[0])
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入一个数字字符，点击确定，提示报错
        driver.find_element_by_xpath(role_name_input_xpath).clear()
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(name[1])
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(role_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(role_add_button_xpath).click()  # 重新点击新增角色按钮
        time.sleep(1)
        # 输入一个英文字符，点击确定，提示报错
        driver.find_element_by_xpath(role_name_input_xpath).clear()
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(name[2])
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入一个特殊符号，点击确定，提示报错
        driver.find_element_by_xpath(role_name_input_xpath).clear()
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(name[3])
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(role_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(role_add_button_xpath).click()  # 重新点击新增角色按钮
        time.sleep(1)
        # 输入13个汉字字符，点击确定，提示报错
        driver.find_element_by_xpath(role_name_input_xpath).clear()
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(name[4])
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(1)
        # 选择一个组织
        driver.find_element_by_xpath(org_list_show_xpath).click()
        driver.find_element_by_xpath(org_choice_xpath).click()
        # 输入12个数字字符，点击确定，提示报错
        driver.find_element_by_xpath(role_name_input_xpath).clear()
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(name[5])
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入11个英文字符，点击确定，提示报错
        driver.find_element_by_xpath(role_name_input_xpath).clear()
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(name[6])
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入6个汉字+符号，点击确定，提示报错
        driver.find_element_by_xpath(role_name_input_xpath).clear()
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(name[7])
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(role_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(role_add_button_xpath).click()  # 重新点击新增角色按钮
        time.sleep(1)
        # 输入6个数字+符号，点击确定，提示报错
        driver.find_element_by_xpath(role_name_input_xpath).clear()
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(name[8])
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(1)
        # 选择一个组织
        driver.find_element_by_xpath(org_list_show_xpath).click()
        driver.find_element_by_xpath(org_choice_xpath).click()
        # 输入6个字母+符号，点击确定，提示报错
        driver.find_element_by_xpath(role_name_input_xpath).clear()
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(name[9])
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入2个汉字，点击确定，新增成功
        driver.find_element_by_xpath(role_name_input_xpath).clear()
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(name[10])
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(3)
        # 输入5个数字，点击确定，新增成功
        driver.find_element_by_xpath(role_add_button_xpath).click()  # 点击新增角色
        driver.find_element_by_xpath(org_list_show_xpath).click()  # 选择一个组织
        driver.find_element_by_xpath(org_choice_xpath).click()
        driver.find_element_by_xpath(role_name_input_xpath).clear()
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(name[11])
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(3)
        # 点击取消，回到界面
        driver.find_element_by_xpath(role_add_button_xpath).click()  # 点击新增角色
        driver.find_element_by_xpath(role_add_cancel_button_xpath).click()
        time.sleep(1)
        # 输入10个字母，点击确定，新增成功
        driver.find_element_by_xpath(role_add_button_xpath).click()  # 点击新增角色
        driver.find_element_by_xpath(org_list_show_xpath).click()  # 选择一个组织
        driver.find_element_by_xpath(org_choice_xpath).click()
        driver.find_element_by_xpath(role_name_input_xpath).clear()
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(name[12])
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(3)
        # 输入6位汉字数字字母混合，点击确定，新增成功
        driver.find_element_by_xpath(role_add_button_xpath).click()  # 点击新增角色
        driver.find_element_by_xpath(org_list_show_xpath).click()  # 选择一个组织
        driver.find_element_by_xpath(org_choice_xpath).click()
        driver.find_element_by_xpath(role_name_input_xpath).clear()
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(name[13])
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(3)
        # 同一组织下输入已存在的角色名称，点击确定，提示报错
        driver.find_element_by_xpath(role_add_button_xpath).click()  # 点击新增角色
        driver.find_element_by_xpath(org_list_show_xpath).click()  # 选择一个组织
        driver.find_element_by_xpath(org_choice_xpath).click()
        driver.find_element_by_xpath(role_name_input_xpath).clear()
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(name[13])
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(3)
        # 不同组织下输入已存在的角色名称，点击确定，新增成功
        driver.find_element_by_xpath(role_add_cancel_button_xpath).click()  # 点击取消
        time.sleep(3)
        driver.find_element_by_xpath(role_add_button_xpath).click()  # 点击新增角色
        driver.find_element_by_xpath(org_list_show_xpath).click()  # 选择一个组织
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[2]/span").click()
        driver.find_element_by_xpath(role_name_input_xpath).clear()
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(name[13])
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        time.sleep(1)

        time.sleep(3)
        time.sleep(3)
        driver.close()

    @staticmethod
    def RoleAdd(driver, writedata=0, sorf=0, orgname=""):
        name = data.get_some_name()
        namestr = name[13]
        time.sleep(1)
        role_add_button_xpath = "/html/body/div/div/div[2]/section/section/div/div/div[1]/div[1]/button"  # 新增角色按钮的xpath
        role_name_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[2]/div/div[1]/input"  # 输入名称编辑框的xpath
        role_add_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
        role_add_cancel_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[2]/span"  # 取消按钮的xpath
        org_list_show_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[1]/div/div/div/span"
        org_choice_xpath = "/html/body/div[3]/div[1]/div[1]/ul/li[1]/span"
        org_choice_xpath1 = "/html/body/div[3]/div[1]/div[1]/ul/li[{}]/span"
        role_element_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[{}]/div"
        # 点击新增角色按钮，弹出新增框
        if sorf:
            hope_org_str = driver.find_element_by_xpath(role_element_xpath.format(3)).text
            hope_role_str = driver.find_element_by_xpath(role_element_xpath.format(2)).text
        driver.find_element_by_xpath(role_add_button_xpath).click()  # 点击新增角色
        driver.find_element_by_xpath(org_list_show_xpath).click()  # 打开组织下拉框
        time.sleep(1)
        if sorf:
            org_conut = 1
            while (org_conut):
                org_name_str = driver.find_element_by_xpath(org_choice_xpath1.format(org_conut)).text
                if (org_name_str == hope_org_str):
                    driver.find_element_by_xpath(org_choice_xpath1.format(org_conut)).click()
                    break
                org_conut = org_conut + 1
            namestr = hope_role_str
        else:
            if writedata:
                org_conut = 1
                while (org_conut):
                    try:
                        driver.implicitly_wait(1)
                        org_name_str = driver.find_element_by_xpath(org_choice_xpath1.format(org_conut)).text
                        driver.implicitly_wait(30)
                    except:
                        driver.implicitly_wait(30)
                        break
                    org_conut = org_conut + 1
                org_conut = random.randint(1, org_conut - 1)
                org_name_str = driver.find_element_by_xpath(org_choice_xpath1.format(org_conut)).text
                driver.find_element_by_xpath(org_choice_xpath1.format(org_conut)).click()
            else:
                driver.find_element_by_xpath(org_choice_xpath).click()  # 选择第一个组织
        if (orgname != ""):
            time.sleep(1)
            driver.find_element_by_xpath(org_list_show_xpath).click()  # 打开组织下拉框
            org_conut = 1
            while (org_conut):
                org_name_str = driver.find_element_by_xpath(org_choice_xpath1.format(org_conut)).text
                # print(org_conut)
                # print(org_name_str)
                if (org_name_str == orgname):
                    driver.find_element_by_xpath(org_choice_xpath1.format(org_conut)).click()
                    break
                org_conut = org_conut + 1
            namestr = name[13]
        driver.find_element_by_xpath(role_name_input_xpath).clear()
        driver.find_element_by_xpath(role_name_input_xpath).send_keys(namestr)
        driver.find_element_by_xpath(role_add_confirm_button_xpath).click()
        if writedata:
            timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            workxls.writedata('roledata.xls', namestr, org_name_str, timestr)
        if sorf:
            driver.find_element_by_xpath(role_add_cancel_button_xpath).click()
        time.sleep(1)
        return driver

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
