# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time
import sys

sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")
import login, data
from selenium.webdriver.common.action_chains import ActionChains


# 用户新增
class User_Add(unittest.TestCase):
    user_add_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
    user_name_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[1]/div/div/input"  # 输入名称编辑框的xpath

    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 用户新增用例
    def test_User_Add(self):
        driver = self.driver
        driver.refresh()  # 刷新一下页面，8月18号执行时，页面没有自动刷新，所以添加了这一句，其它脚本可能也需要用上
        name = data.get_some_name()  # 获取一些名字字符串
        user_add_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[1]/button/span"  # 新增用户按钮的xpath
        user_add_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
        time.sleep(1)
        # 点击菜单栏用户管理
        driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[4]").click()
        time.sleep(1)  # 预留时间查看
        # 点击新增用户按钮，弹出新增框
        driver.find_element_by_xpath(user_add_button_xpath).click()
        time.sleep(1)
        driver = self.Reopen_edit_form(driver)  # 点击取消，重新打开编辑界面
        # 什么都不输入，点击确定，提示报错
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 检查用户名
        driver = self.Reopen_edit_form(driver)  # 点击取消，重新打开编辑界面
        driver = self.CheckUsername(driver)
        # # 检查邮箱
        # driver = self.Reopen_edit_form(driver)  # 点击取消，重新打开编辑界面
        # driver = self.CheckMailbox(driver)
        # # 检查手机号
        # driver = self.Reopen_edit_form(driver)  # 点击取消，重新打开编辑界面
        # driver = self.CheckPhonenumber(driver)
        # # 检查初始密码
        # driver = self.Reopen_edit_form(driver)  # 点击取消，重新打开编辑界面
        # driver = self.CheckPasswrod(driver)
        # # 检查组织和角色下拉框
        # driver = self.Reopen_edit_form(driver)  # 点击取消，重新打开编辑界面
        # driver = self.CheckOrgandRole(driver)
        # # 填写所有要素，点击确定，新增成功
        # driver = self.Reopen_edit_form(driver)  # 点击取消，重新打开编辑界面
        # driver = self.WriteallSpace(driver)

        # # 选择一个组织，点击确定，提示报错
        # driver.find_element_by_xpath(org_list_show_xpath).click()
        # driver.find_element_by_xpath(org_choice_xpath).click()
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(1)
        # # 输入一个汉字字符，点击确定，提示报错
        # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[0])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(1)
        # # 输入一个数字字符，点击确定，提示报错
        # driver.find_element_by_xpath(user_name_input_xpath).clear()
        # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[1])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(1)
        # # 点击取消，回到界面
        # driver.find_element_by_xpath(user_add_cancel_button_xpath).click()
        # time.sleep(1)
        # driver.find_element_by_xpath(user_add_button_xpath).click()  # 重新点击新增用户按钮
        # time.sleep(1)
        # # 输入一个英文字符，点击确定，提示报错
        # driver.find_element_by_xpath(user_name_input_xpath).clear()
        # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[2])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(1)
        # # 输入一个特殊符号，点击确定，提示报错
        # driver.find_element_by_xpath(user_name_input_xpath).clear()
        # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[3])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(1)
        # # 点击取消，回到界面
        # driver.find_element_by_xpath(user_add_cancel_button_xpath).click()
        # time.sleep(1)
        # driver.find_element_by_xpath(user_add_button_xpath).click()  # 重新点击新增用户按钮
        # time.sleep(1)
        # # 输入13个汉字字符，点击确定，提示报错
        # driver.find_element_by_xpath(user_name_input_xpath).clear()
        # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[4])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(1)
        # # 选择一个组织
        # driver.find_element_by_xpath(org_list_show_xpath).click()
        # driver.find_element_by_xpath(org_choice_xpath).click()
        # # 输入12个数字字符，点击确定，提示报错
        # driver.find_element_by_xpath(user_name_input_xpath).clear()
        # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[5])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(1)
        # # 输入11个英文字符，点击确定，提示报错
        # driver.find_element_by_xpath(user_name_input_xpath).clear()
        # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[6])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(1)
        # # 输入6个汉字+符号，点击确定，提示报错
        # driver.find_element_by_xpath(user_name_input_xpath).clear()
        # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[7])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(1)
        # # 点击取消，回到界面
        # driver.find_element_by_xpath(user_add_cancel_button_xpath).click()
        # time.sleep(1)
        # driver.find_element_by_xpath(user_add_button_xpath).click()  # 重新点击新增用户按钮
        # time.sleep(1)
        # # 输入6个数字+符号，点击确定，提示报错
        # driver.find_element_by_xpath(user_name_input_xpath).clear()
        # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[8])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(1)
        # # 选择一个组织
        # driver.find_element_by_xpath(org_list_show_xpath).click()
        # driver.find_element_by_xpath(org_choice_xpath).click()
        # # 输入6个字母+符号，点击确定，提示报错
        # driver.find_element_by_xpath(user_name_input_xpath).clear()
        # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[9])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(1)
        # # 输入2个汉字，点击确定，新增成功
        # driver.find_element_by_xpath(user_name_input_xpath).clear()
        # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[10])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(3)
        # # 输入5个数字，点击确定，新增成功
        # driver.find_element_by_xpath(user_add_button_xpath).click()  # 点击新增用户
        # driver.find_element_by_xpath(org_list_show_xpath).click()  # 选择一个组织
        # driver.find_element_by_xpath(org_choice_xpath).click()
        # driver.find_element_by_xpath(user_name_input_xpath).clear()
        # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[11])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(3)
        # # 点击取消，回到界面
        # driver.find_element_by_xpath(user_add_button_xpath).click()  # 点击新增用户
        # driver.find_element_by_xpath(user_add_cancel_button_xpath).click()
        # time.sleep(1)
        # # 输入10个字母，点击确定，新增成功
        # driver.find_element_by_xpath(user_add_button_xpath).click()  # 点击新增用户
        # driver.find_element_by_xpath(org_list_show_xpath).click()  # 选择一个组织
        # driver.find_element_by_xpath(org_choice_xpath).click()
        # driver.find_element_by_xpath(user_name_input_xpath).clear()
        # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[12])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(3)
        # # 输入6位汉字数字字母混合，点击确定，新增成功
        # driver.find_element_by_xpath(user_add_button_xpath).click()  # 点击新增用户
        # driver.find_element_by_xpath(org_list_show_xpath).click()  # 选择一个组织
        # driver.find_element_by_xpath(org_choice_xpath).click()
        # driver.find_element_by_xpath(user_name_input_xpath).clear()
        # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[13])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(3)
        # # 同一组织下输入已存在的用户名称，点击确定，提示报错
        # driver.find_element_by_xpath(user_add_button_xpath).click()  # 点击新增用户
        # driver.find_element_by_xpath(org_list_show_xpath).click()  # 选择一个组织
        # driver.find_element_by_xpath(org_choice_xpath).click()
        # driver.find_element_by_xpath(user_name_input_xpath).clear()
        # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[13])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(3)
        # # 不同组织下输入已存在的用户名称，点击确定，新增成功
        # driver.find_element_by_xpath(user_add_cancel_button_xpath).click()  # 点击取消
        # time.sleep(3)
        # driver.find_element_by_xpath(user_add_button_xpath).click()  # 点击新增用户
        # driver.find_element_by_xpath(org_list_show_xpath).click()  # 选择一个组织
        # driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[2]/span").click()
        # driver.find_element_by_xpath(user_name_input_xpath).clear()
        # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[13])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(1)

        time.sleep(3)
        time.sleep(3)
        driver.close()

    @staticmethod
    def WriteallSpace(driver):  # 填写所有要素
        org_list_show_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[6]/div/div/div/span"  # 打开选择组织下拉框的xpath
        org_choice_xpath = "/html/body/div[4]/div[1]/div[1]/ul/li[1]"  # 选择第一个组织的xpath
        role_list_show_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[7]/div/div/div[1]/span"
        role_choice_xpath = ""
        psd = data.get_new_passwrod()  # 获取一些密码字符串
        user_add_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
        Password_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[5]/div/div/input"  # 输入初始密码编辑框的xpath
        Password_eye_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[5]/div/span"  # 初始密码小眼睛的xpath
        phonenupmber = ["13231", "wwwcom", "汉字163", "1334637287", "weq3#!@efgg", "sjh汉字12英文", "17628372938",
                        "19026757372"]
        Phonenumber_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[4]/div/div/input"  # 输入手机号编辑框的xpath
        mail = ["13231", "@www.com", "汉字@163.com", "#$au@qq.com", "weqe", "sj12", "liulei@deepait.com",
                "690267573@qq.com"]
        Mailbox_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[3]/div/div[1]/input"  # 输入邮箱编辑框的xpath
        name = data.get_some_name()
        user_name_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[1]/div/div/input"  # 输入名称编辑框的xpath

        driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[13])


        return driver

    @staticmethod
    def CheckOrgandRole(driver):  # 检查组织和角色
        org_list_show_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[6]/div/div/div/span"  # 打开选择组织下拉框的xpath
        org_choice_xpath = "/html/body/div[4]/div[1]/div[1]/ul/li[1]"  # 选择第一个组织的xpath

        role_list_show_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[7]/div/div/div[1]/span"
        role_choice_xpath = ""
        # 组织下拉框为空，光标移至角色下拉框
        above = driver.find_element_by_xpath(role_list_show_xpath)
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(3)
        # 组织下拉框
        driver.find_element_by_xpath(org_list_show_xpath).click()
        time.sleep(3)
        driver.find_element_by_xpath(org_choice_xpath).click()
        time.sleep(3)
        # 角色下拉框
        return driver

    @staticmethod
    def CheckPasswrod(driver):  # 检查初始密码
        psd = data.get_new_passwrod()  # 获取一些密码字符串
        user_add_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
        Password_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[5]/div/div/input"  # 输入初始密码编辑框的xpath
        Password_eye_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[5]/div/span"  # 初始密码小眼睛的xpath
        # 输入5种格式不正确的密码，点击确定，提示报错
        driver.find_element_by_xpath(Password_input_xpath).send_keys(psd[0])
        time.sleep(1)
        driver.find_element_by_xpath(Password_eye_input_xpath).click()  # 点击小眼睛查看密码
        time.sleep(1)
        driver.find_element_by_xpath(Password_eye_input_xpath).click()  # 点击小眼睛隐藏密码
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Password_input_xpath).clear()
        driver.find_element_by_xpath(Password_input_xpath).send_keys(psd[1])
        time.sleep(1)
        driver.find_element_by_xpath(Password_eye_input_xpath).click()  # 点击小眼睛查看密码
        time.sleep(1)
        driver.find_element_by_xpath(Password_eye_input_xpath).click()  # 点击小眼睛隐藏密码
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Password_input_xpath).clear()
        driver.find_element_by_xpath(Password_input_xpath).send_keys(psd[2])
        time.sleep(1)
        driver.find_element_by_xpath(Password_eye_input_xpath).click()  # 点击小眼睛查看密码
        time.sleep(1)
        driver.find_element_by_xpath(Password_eye_input_xpath).click()  # 点击小眼睛隐藏密码
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，重新打开编辑界面
        driver = User_Add.Reopen_edit_form(driver)
        driver.find_element_by_xpath(Password_input_xpath).clear()
        driver.find_element_by_xpath(Password_input_xpath).send_keys(psd[3])
        time.sleep(1)
        driver.find_element_by_xpath(Password_eye_input_xpath).click()  # 点击小眼睛查看密码
        time.sleep(1)
        driver.find_element_by_xpath(Password_eye_input_xpath).click()  # 点击小眼睛隐藏密码
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Password_input_xpath).clear()
        driver.find_element_by_xpath(Password_input_xpath).send_keys(psd[4])
        time.sleep(1)
        driver.find_element_by_xpath(Password_eye_input_xpath).click()  # 点击小眼睛查看密码
        time.sleep(1)
        driver.find_element_by_xpath(Password_eye_input_xpath).click()  # 点击小眼睛隐藏密码
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入正确格式的密码，点击确定，不提示错误
        driver.find_element_by_xpath(Password_input_xpath).clear()
        driver.find_element_by_xpath(Password_input_xpath).send_keys(psd[5])
        time.sleep(1)
        driver.find_element_by_xpath(Password_eye_input_xpath).click()  # 点击小眼睛查看密码
        time.sleep(1)
        driver.find_element_by_xpath(Password_eye_input_xpath).click()  # 点击小眼睛隐藏密码
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        return driver

    @staticmethod
    def CheckPhonenumber(driver):  # 检查手机号码
        phonenupmber = ["13231", "wwwcom", "汉字163", "1334637287", "weq3#!@efgg", "sjh汉字12英文", "17628372938",
                        "19026757372"]
        user_add_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
        Phonenumber_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[4]/div/div/input"  # 输入手机号编辑框的xpath
        # 输入6种格式不正确的邮箱，点击确定，提示报错
        driver.find_element_by_xpath(Phonenumber_input_xpath).send_keys(phonenupmber[0])
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Phonenumber_input_xpath).clear()
        driver.find_element_by_xpath(Phonenumber_input_xpath).send_keys(phonenupmber[1])
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Phonenumber_input_xpath).clear()
        driver.find_element_by_xpath(Phonenumber_input_xpath).send_keys(phonenupmber[2])
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，重新打开编辑界面
        driver = User_Add.Reopen_edit_form(driver)
        driver.find_element_by_xpath(Phonenumber_input_xpath).clear()
        driver.find_element_by_xpath(Phonenumber_input_xpath).send_keys(phonenupmber[3])
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Phonenumber_input_xpath).clear()
        driver.find_element_by_xpath(Phonenumber_input_xpath).send_keys(phonenupmber[4])
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Phonenumber_input_xpath).clear()
        driver.find_element_by_xpath(Phonenumber_input_xpath).send_keys(phonenupmber[5])
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入2种格式正确的邮箱，点击确定，合法，不提示报错
        driver.find_element_by_xpath(Phonenumber_input_xpath).clear()
        driver.find_element_by_xpath(Phonenumber_input_xpath).send_keys(phonenupmber[6])
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，重新打开编辑界面
        driver = User_Add.Reopen_edit_form(driver)
        driver.find_element_by_xpath(Phonenumber_input_xpath).clear()
        driver.find_element_by_xpath(Phonenumber_input_xpath).send_keys(phonenupmber[7])
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)

        return driver

    @staticmethod
    def CheckMailbox(driver):  # 检查邮箱
        mail = ["13231", "@www.com", "汉字@163.com", "#$au@qq.com", "weqe", "sj12", "liulei@deepait.com",
                "690267573@qq.com"]
        user_add_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
        Mailbox_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[3]/div/div[1]/input"  # 输入邮箱编辑框的xpath
        # 输入6种格式不正确的邮箱，点击确定，提示报错
        driver.find_element_by_xpath(Mailbox_input_xpath).send_keys(mail[0])
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Mailbox_input_xpath).clear()
        driver.find_element_by_xpath(Mailbox_input_xpath).send_keys(mail[1])
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Mailbox_input_xpath).clear()
        driver.find_element_by_xpath(Mailbox_input_xpath).send_keys(mail[2])
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，重新打开编辑界面
        driver = User_Add.Reopen_edit_form(driver)
        driver.find_element_by_xpath(Mailbox_input_xpath).clear()
        driver.find_element_by_xpath(Mailbox_input_xpath).send_keys(mail[3])
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Mailbox_input_xpath).clear()
        driver.find_element_by_xpath(Mailbox_input_xpath).send_keys(mail[4])
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Mailbox_input_xpath).clear()
        driver.find_element_by_xpath(Mailbox_input_xpath).send_keys(mail[5])
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入2种格式正确的邮箱，点击确定，合法，不提示报错
        driver.find_element_by_xpath(Mailbox_input_xpath).clear()
        driver.find_element_by_xpath(Mailbox_input_xpath).send_keys(mail[6])
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，重新打开编辑界面
        driver = User_Add.Reopen_edit_form(driver)
        driver.find_element_by_xpath(Mailbox_input_xpath).clear()
        driver.find_element_by_xpath(Mailbox_input_xpath).send_keys(mail[7])
        driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        time.sleep(1)

        return driver



    @staticmethod
    def CheckUsername(driver):  # 检查用户名
        name = data.get_some_name()
        # 输入一个汉字字符，点击确定，提示报错
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).send_keys(name[0])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入一个数字字符，点击确定，提示报错
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).send_keys(name[1])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，重新打开编辑界面
        driver = User_Add.Reopen_edit_form(driver)
        # 输入一个英文字符，点击确定，提示报错
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).send_keys(name[2])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入一个特殊符号，点击确定，提示报错
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).send_keys(name[3])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入13个汉字字符，点击确定，提示报错
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).send_keys(name[4])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入12个数字字符，点击确定，提示报错
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).send_keys(name[5])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，重新打开编辑界面
        driver = User_Add.Reopen_edit_form(driver)
        # 输入11个英文字符，点击确定，提示报错
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).send_keys(name[6])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入6个汉字+符号，点击确定，提示报错
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).send_keys(name[7])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，重新打开编辑界面
        driver = User_Add.Reopen_edit_form(driver)
        # 输入6个数字+符号，点击确定，提示报错
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).send_keys(name[8])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入6个字母+符号，点击确定，提示报错
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).send_keys(name[9])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入2个汉字，点击确定，合法，不提示报错
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).send_keys(name[10])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入5个数字，点击确定，合法，不提示报错
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).send_keys(name[11])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，重新打开编辑界面
        driver = User_Add.Reopen_edit_form(driver)
        # 输入10个字母，点击确定，合法，不提示报错
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).send_keys(name[12])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入6位汉字数字字母混合，点击确定，合法，不提示报错
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.user_name_input_xpath).send_keys(name[13])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # # 输入已存在的用户名称，点击确定，提示报错
        # driver.find_element_by_xpath(user_add_button_xpath).click()  # 点击新增用户
        # driver.find_element_by_xpath(user_name_input_xpath).clear()
        # # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[13])
        # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
        # time.sleep(1)

        return driver
    # @staticmethod
    # def CheckUsername(driver):  # 检查用户名
    #     name = data.get_some_name()
    #     user_add_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
    #     user_name_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[1]/div/div/input"  # 输入名称编辑框的xpath
    #     # 输入一个汉字字符，点击确定，提示报错
    #     driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[0])
    #     driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
    #     time.sleep(1)
    #     # 输入一个数字字符，点击确定，提示报错
    #     driver.find_element_by_xpath(user_name_input_xpath).clear()
    #     driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[1])
    #     driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
    #     time.sleep(1)
    #     # 点击取消，重新打开编辑界面
    #     driver = User_Add.Reopen_edit_form(driver)
    #     # 输入一个英文字符，点击确定，提示报错
    #     driver.find_element_by_xpath(user_name_input_xpath).clear()
    #     driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[2])
    #     driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
    #     time.sleep(1)
    #     # 输入一个特殊符号，点击确定，提示报错
    #     driver.find_element_by_xpath(user_name_input_xpath).clear()
    #     driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[3])
    #     driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
    #     time.sleep(1)
    #     # 输入13个汉字字符，点击确定，提示报错
    #     driver.find_element_by_xpath(user_name_input_xpath).clear()
    #     driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[4])
    #     driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
    #     time.sleep(1)
    #     # 输入12个数字字符，点击确定，提示报错
    #     driver.find_element_by_xpath(user_name_input_xpath).clear()
    #     driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[5])
    #     driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
    #     time.sleep(1)
    #     # 点击取消，重新打开编辑界面
    #     driver = User_Add.Reopen_edit_form(driver)
    #     # 输入11个英文字符，点击确定，提示报错
    #     driver.find_element_by_xpath(user_name_input_xpath).clear()
    #     driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[6])
    #     driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
    #     time.sleep(1)
    #     # 输入6个汉字+符号，点击确定，提示报错
    #     driver.find_element_by_xpath(user_name_input_xpath).clear()
    #     driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[7])
    #     driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
    #     time.sleep(1)
    #     # 点击取消，重新打开编辑界面
    #     driver = User_Add.Reopen_edit_form(driver)
    #     # 输入6个数字+符号，点击确定，提示报错
    #     driver.find_element_by_xpath(user_name_input_xpath).clear()
    #     driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[8])
    #     driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
    #     time.sleep(1)
    #     # 输入6个字母+符号，点击确定，提示报错
    #     driver.find_element_by_xpath(user_name_input_xpath).clear()
    #     driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[9])
    #     driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
    #     time.sleep(1)
    #     # 输入2个汉字，点击确定，合法，不提示报错
    #     driver.find_element_by_xpath(user_name_input_xpath).clear()
    #     driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[10])
    #     driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
    #     time.sleep(1)
    #     # 输入5个数字，点击确定，合法，不提示报错
    #     driver.find_element_by_xpath(user_name_input_xpath).clear()
    #     driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[11])
    #     driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
    #     time.sleep(1)
    #     # 点击取消，重新打开编辑界面
    #     driver = User_Add.Reopen_edit_form(driver)
    #     # 输入10个字母，点击确定，合法，不提示报错
    #     driver.find_element_by_xpath(user_name_input_xpath).clear()
    #     driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[12])
    #     driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
    #     time.sleep(1)
    #     # 输入6位汉字数字字母混合，点击确定，合法，不提示报错
    #     driver.find_element_by_xpath(user_name_input_xpath).clear()
    #     driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[13])
    #     driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
    #     time.sleep(1)
    #     # # 输入已存在的用户名称，点击确定，提示报错
    #     # driver.find_element_by_xpath(user_add_button_xpath).click()  # 点击新增用户
    #     # driver.find_element_by_xpath(user_name_input_xpath).clear()
    #     # # driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[13])
    #     # driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
    #     # time.sleep(1)
    #
    #     return driver

    @staticmethod
    def Reopen_edit_form(driver):  # 点击取消，重新打开编辑界面
        user_add_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[1]/button/span"  # 新增用户按钮的xpath
        user_add_cancel_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[2]/span"  # 取消按钮的xpath
        # 点击取消，回到界面
        driver.find_element_by_xpath(user_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(user_add_button_xpath).click()  # 重新点击新增用户按钮
        time.sleep(1)
        return driver

    # @staticmethod
    # def UserAdd(driver):
    #     name = data.get_some_name()
    #     user_add_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[1]/button/span"  # 新增用户按钮的xpath
    #     user_name_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[2]/div/div[1]/input"  # 输入名称编辑框的xpath
    #     user_add_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
    #     org_list_show_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[1]/div/div/div/span"
    #     org_choice_xpath = "/html/body/div[3]/div[1]/div[1]/ul/li[1]/span"
    #     # 点击新增用户按钮，弹出新增框
    #     driver.find_element_by_xpath(user_add_button_xpath).click()  # 点击新增用户
    #     driver.find_element_by_xpath(org_list_show_xpath).click()  # 选择一个组织
    #     driver.find_element_by_xpath(org_choice_xpath).click()
    #     driver.find_element_by_xpath(user_name_input_xpath).clear()
    #     driver.find_element_by_xpath(user_name_input_xpath).send_keys(name[13])
    #     driver.find_element_by_xpath(user_add_confirm_button_xpath).click()
    #     time.sleep(2)
    #     return driver

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
