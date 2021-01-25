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


# 用户编辑(修改)
class User_Edit(unittest.TestCase):
    user_edit_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
    user_edit_cancel_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[3]/div/button[2]/span"  # 取消按钮的xpath
    # "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]"
    # "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[2]"
    phonenumber_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/form/div[5]/div/div/input"
    # "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/form/div[5]/div/div/input"
    # "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[5]/div/div/input"
    org_list_show_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[6]/div/div/div/span"  # 打开选择组织下拉框的xpath
    org_choice_xpath = "/html/body/div[3]/div[1]/div[1]/ul/li[1]/span"  # 选择第一个组织的xpath
    role_list_show_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[7]/div/div/div[1]/span"  # 打开选择角色下拉框的xpath
    role_choice_xpath = "/html/body/div[4]/div[1]/div[1]/ul/li[1]/span"  # 选择第一个角色的xpath
    n_user_imf_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[{}]/td[{}]/div"  # 某条用户信息的xpath

    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 用户编辑用例
    def test_User_Edit(self):
        driver = self.driver
        time.sleep(1)

        # 点击菜单栏用户管理
        driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[4]").click()
        time.sleep(1)  # 预留时间查看
        # 选一个编辑用户按钮，点击，弹出编辑框
        driver.find_element_by_xpath(User_Edit.get_user_edit_button_xpath(driver)).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(self.user_edit_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(self.get_user_edit_button_xpath(driver)).click()  # 重新选一个编辑用户按钮，点击，弹出编辑框
        time.sleep(1)
        # 直接点击确定，未作修改，提示操作成功
        driver.find_element_by_xpath(self.user_edit_confirm_button_xpath).click()
        time.sleep(1)
        # # 输入6种格式不正确的手机号码，点击确定，提示报错
        # driver.find_element_by_xpath(self.get_user_edit_button_xpath(driver)).click()  # 重新选一个编辑用户按钮，点击，弹出编辑框
        # time.sleep(1)
        # phonenupmber = ["13231", "wwwcom", "汉字163", "1334637287", "weq3#!@efgg", "sjh汉字12英文", "17628372938",
        #                 "19026757372"]
        # driver.find_element_by_xpath(self.phonenumber_input_xpath).send_keys(phonenupmber[0])
        # driver.find_element_by_xpath(self.user_edit_confirm_button_xpath).click()
        # time.sleep(1)
        # driver.find_element_by_xpath(self.phonenumber_input_xpath).clear()
        # driver.find_element_by_xpath(self.phonenumber_input_xpath).send_keys(phonenupmber[1])
        # driver.find_element_by_xpath(self.user_edit_confirm_button_xpath).click()
        # time.sleep(1)
        # driver.find_element_by_xpath(self.phonenumber_input_xpath).clear()
        # driver.find_element_by_xpath(self.phonenumber_input_xpath).send_keys(phonenupmber[2])
        # driver.find_element_by_xpath(self.user_edit_confirm_button_xpath).click()
        # time.sleep(1)
        # driver.find_element_by_xpath(self.get_user_edit_button_xpath(driver)).click()  # 重新选一个编辑用户按钮，点击，弹出编辑框
        # time.sleep(1)
        # driver.find_element_by_xpath(self.phonenumber_input_xpath).clear()
        # driver.find_element_by_xpath(self.phonenumber_input_xpath).send_keys(phonenupmber[3])
        # driver.find_element_by_xpath(self.user_edit_confirm_button_xpath).click()
        # time.sleep(1)
        # driver.find_element_by_xpath(self.phonenumber_input_xpath).clear()
        # driver.find_element_by_xpath(self.phonenumber_input_xpath).send_keys(phonenupmber[4])
        # driver.find_element_by_xpath(self.user_edit_confirm_button_xpath).click()
        # time.sleep(1)
        # driver.find_element_by_xpath(self.phonenumber_input_xpath).clear()
        # driver.find_element_by_xpath(self.phonenumber_input_xpath).send_keys(phonenupmber[5])
        # driver.find_element_by_xpath(self.user_edit_confirm_button_xpath).click()
        # time.sleep(1)
        # # 输入2种格式正确的手机号码，点击确定，合法，不提示报错
        # driver.find_element_by_xpath(self.phonenumber_input_xpath).clear()
        # driver.find_element_by_xpath(self.phonenumber_input_xpath).send_keys(phonenupmber[6])
        # driver.find_element_by_xpath(self.user_edit_confirm_button_xpath).click()
        # time.sleep(1)
        # driver.find_element_by_xpath(self.get_user_edit_button_xpath(driver)).click()  # 重新选一个编辑用户按钮，点击，弹出编辑框
        # time.sleep(1)
        # driver.find_element_by_xpath(self.phonenumber_input_xpath).clear()
        # driver.find_element_by_xpath(self.phonenumber_input_xpath).send_keys(phonenupmber[7])
        # driver.find_element_by_xpath(self.user_edit_confirm_button_xpath).click()
        # time.sleep(1)

        # # 检查组织下拉框
        # driver.find_element_by_xpath(org_list_show_xpath).click()
        # time.sleep(3)
        # driver.find_element_by_xpath(org_choice_xpath).click()
        # time.sleep(1)
        # # 检查角色下拉框
        # driver.find_element_by_xpath(role_list_show_xpath).click()
        # time.sleep(3)
        # driver.find_element_by_xpath(role_choice_xpath).click()
        # time.sleep(1)

        # 输入已存在的手机号，点击确定，提示"手机号已存在"，修改失败
        phone_num = self.find_diffrent_phonenum(driver)
        if (phone_num):
            xstr = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div/ul/li[1]"
            driver.find_element_by_xpath(self.get_user_edit_button_xpath(driver, 1)).click()
            driver.find_element_by_xpath(self.phonenumber_input_xpath).clear()
            driver.find_element_by_xpath(self.phonenumber_input_xpath).send_keys(phone_num)
            driver.find_element_by_xpath(self.user_edit_confirm_button_xpath).click()
            time.sleep(1)
        else:
            raise NameError("输入已存在的手机号用例失败，建议手工测试，失败原因：没有其他可用的的手机号码!")

        time.sleep(3)
        time.sleep(3)
        driver.close()

    @staticmethod
    def get_user_edit_button_xpath(driver, i=0):  # 获取编辑用户按钮的xpath，页面上随机选取一个来编辑，并将光标移动至编辑按钮上
        driver.implicitly_wait(1)
        if (i == 0):
            i = random.randint(1, 10)
        ret = ""
        # driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[5]").click()
        # driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div/ul/li[7]").click()
        while (i):
            # print(i)
            ret = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[" + str(
                i) + "]/td[9]/div/a[1]/span"
            try:
                driver.find_element_by_xpath(ret)
                driver.implicitly_wait(30)
                break
            except:
                i = i - 1
        if i > 5:  # 如果选到了6-10的用户，下拉滚动条至底部
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
    @staticmethod
    def find_diffrent_phonenum(driver):  # 每一页都去find_diffrent_phonenum_d返回手机号
        while (1):
            lstr = User_Edit.find_diffrent_phonenum_d(driver)
            if (lstr == ""):
                hstr = driver.find_element_by_xpath(
                    "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div/button[2]").get_attribute(
                    'outerHTML')  # 获取">"的html
                # print(hstr)
                if (re.search("disabled", hstr)):  # 获取">"的html里面包含"disabled"，则它不能被点击，找了所有页面都没有符合条件的数据，返回空
                    return lstr
                driver.find_element_by_xpath(
                    "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div/button[2]").click()
            else:
                break
        return lstr

    @staticmethod
    def find_diffrent_phonenum_d(driver):
        ret = ""
        i = 2
        while (i < 11):
            try:
                driver.implicitly_wait(1)
                # str2记录当前页面第2-10条用户信息的组织名称
                str1 = driver.find_element_by_xpath(
                    "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[2]/div[3]/table/tbody/tr[" + str(
                        i) + "]/td[6]/div").text
            except:
                break
            if (str1 != "-"):
                ret = str1
                driver.implicitly_wait(30)
                return ret
            i = i + 1
        driver.implicitly_wait(30)
        return ret

    @staticmethod
    def UserEdit(driver, sorf=0):
        phonenum = data.get_some_phonenum()
        name = driver.find_element_by_xpath(User_Edit.n_user_imf_xpath.format(1, 2)).text
        org_name_str = driver.find_element_by_xpath(User_Edit.n_user_imf_xpath.format(1, 4)).text
        role_name_str = driver.find_element_by_xpath(User_Edit.n_user_imf_xpath.format(1, 5)).text
        mail = driver.find_element_by_xpath(User_Edit.n_user_imf_xpath.format(1, 7)).text
        time.sleep(1)
        # 如果成功或者失败参数为1，则添加一个和第一个角色相同组织的角色，再执行
        if (sorf == 1):
            phonenum = org_name_str = driver.find_element_by_xpath(User_Edit.n_user_imf_xpath.format(2, 6)).text
        time.sleep(1)
        # 选第一个用户，点击编辑按钮，弹出编辑框
        user_edit_button_xpath = User_Edit.get_user_edit_button_xpath(driver, 1)  # 参数选1，表示选第一个角色的编辑按钮xpath
        driver.find_element_by_xpath(user_edit_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(User_Edit.phonenumber_input_xpath).clear()
        driver.find_element_by_xpath(User_Edit.phonenumber_input_xpath).send_keys(phonenum)
        time.sleep(1)
        driver.find_element_by_xpath(User_Edit.user_edit_confirm_button_xpath).click()

        timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        workxls.writedata('userdata.xls', name, '女', org_name_str, role_name_str, phonenum, mail, timestr)

        # 如果成功或者失败参数为1，则需要点击取消
        if (sorf == 1):
            time.sleep(1)
            driver.find_element_by_xpath(User_Edit.user_edit_cancel_button_xpath).click()
        return driver

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
