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


# 用户新增
class User_Add(unittest.TestCase):
    user_add_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
    # "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[3]/div/button[1]/span"
    # "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]/span"
    user_name_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/form/div[1]/div/div[1]/input"  # 输入名称编辑框的xpath
    # "//*[@id="app"]/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/form/div[1]/div/div[1]/input"
    # "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[1]/div/div/input"
    Mailbox_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/form/div[3]/div/div[1]/input"  # 输入邮箱编辑框的xpath
    # "//*[@id="app"]/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/form/div[3]/div/div[1]/input"
    # "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[3]/div/div[1]/input"
    org_list_show_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/form/div[6]/div/div/div[1]/span/span"  # 打开选择组织下拉框的xpath
    # "//*[@id="app"]/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/form/div[6]/div/div/div[1]/span/span"
    # "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[6]/div/div/div/span"
    org_choice_xpath = "/html/body/div[3]/div[1]/div[1]/ul/li[1]/span"  # 选择第一个组织的xpath
    role_list_show_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/form/div[7]/div/div/div/span/span"  # 打开选择角色下拉框的xpath
    # "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/form/div[7]/div/div/div/span/span"
    # "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[7]/div/div/div[1]/span"
    role_choice_xpath = "/html/body/div[4]/div[1]/div[1]/ul/li[1]/span"  # 选择第一个角色的xpath
    Password_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/form/div[5]/div/div[1]/input"  # 输入初始密码编辑框的xpath
    # "//*[@id="app"]/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/form/div[5]/div/div[1]/input"
    # "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[5]/div/div/input"
    Password_eye_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[5]/div/span"  # 初始密码小眼睛的xpath
    Phonenumber_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/form/div[4]/div/div/input"  # 输入手机号编辑框的xpath
    # "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/form/div[4]/div/div/input"
    # "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[4]/div/div/input"
    Man_choice_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/form/div[2]/div/div/label[1]/span[1]"  # 性别选择男的xpath
    # "//*[@id="app"]/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/form/div[2]/div/div/label[2]/span[1]"
    Woman_choice_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[2]/div/div/label[2]/span[1]"  # 性别选择女的xpath
    user_add_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div[1]/button"  # 新增用户按钮的xpath
    # "/html/body/div/div/div[2]/section/section/div/div/div[2]/div[1]/button/span"
    # "/html/body/div/div/div[2]/section/section/div/div/div[1]/div[1]/button/span"
    user_add_cancel_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[3]/div/button[2]/span"  # 取消按钮的xpath
    # "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[3]/div/button[2]/span"
    # "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[2]/span"
    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 用户新增用例
    def test_User_Add(self):
        driver = self.driver
        # driver.refresh()  # 刷新一下页面，8月18号执行时，页面没有自动刷新，所以添加了这一句，其它脚本可能也需要用上
        name = data.get_some_name()  # 获取一些名字字符串
        time.sleep(1)
        # 点击菜单栏用户管理
        driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[4]").click()
        time.sleep(1)  # 预留时间查看
        # 点击新增用户按钮，弹出新增框
        time.sleep(2)  # 0820加载比较卡，预留时间加载
        driver.find_element_by_xpath(User_Add.user_add_button_xpath).click()
        time.sleep(1)
        # driver = self.Reopen_edit_form(driver)  # 点击取消，重新打开编辑界面
        # # 什么都不输入，点击确定，提示报错
        # driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        # time.sleep(1)
        # # 检查用户名
        # driver = self.Reopen_edit_form(driver)  # 点击取消，重新打开编辑界面
        # driver = self.CheckUsername(driver)
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
        # # 按钮检查，新增成功
        # driver = self.Reopen_edit_form(driver)  # 点击取消，重新打开编辑界面
        # driver = self.Checkconfirmb(driver)
        driver = self.UserAdd(driver)

        time.sleep(3)
        time.sleep(3)
        driver.close()

    @staticmethod
    def Checkconfirmb(driver):  # 检查确定按钮
        name = data.get_some_name()
        mail = data.get_some_mailbox()
        phonenum = data.get_some_phonenum()
        psd = data.get_new_passwrod()
        # 不填用户名，点击确定，报错
        driver = User_Add.UserImWrite(driver, mail=mail[0], phonenum=phonenum[0], psd=psd[5])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 不填邮箱，点击确定，报错
        driver = User_Add.Reopen_edit_form(driver)  # 点击取消，重新打开编辑界面
        driver = User_Add.UserImWrite(driver, name=name[13], phonenum=phonenum[0], psd=psd[5])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 不填初始密码，点击确定，报错
        driver = User_Add.Reopen_edit_form(driver)  # 点击取消，重新打开编辑界面
        driver = User_Add.UserImWrite(driver, name=name[13], mail=mail[0], phonenum=phonenum[0])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 不填电话号码，点击确定，新增成功
        driver = User_Add.Reopen_edit_form(driver)  # 点击取消，重新打开编辑界面
        driver = User_Add.UserImWrite(driver, name=name[13], mail=mail[0], psd=psd[5])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        user1 = [name[13], mail[0], "0", psd[5]]
        # 填写电话号码，点击确定，新增成功
        time.sleep(3)  # 预留时间加载页面
        name = data.get_some_name()  # 重新获取一个name。邮箱，手机号，密码(相同)不需要重新获取
        driver.find_element_by_xpath(User_Add.user_add_button_xpath).click()  # 重新点击新增用户按钮
        driver = User_Add.UserImWrite(driver, name=name[13], mail=mail[1], phonenum=phonenum[0], psd=psd[5])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        user2 = [name[13], mail[1], phonenum[0], psd[5]]
        # 填写用户名 和已存在的用户名相同，点击确定，报错
        time.sleep(3)  # 预留时间加载页面
        driver.find_element_by_xpath(User_Add.user_add_button_xpath).click()  # 重新点击新增用户按钮
        driver = User_Add.UserImWrite(driver, name=name[13], mail=mail[2], phonenum=phonenum[1], psd=psd[5])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 填写邮箱 和已存在的邮箱相同，点击确定，报错
        name = data.get_some_name()  # 重新获取一个name。
        driver = User_Add.Reopen_edit_form(driver)  # 点击取消，重新打开编辑界面
        driver = User_Add.UserImWrite(driver, name=name[13], mail=mail[0], phonenum=phonenum[1], psd=psd[5])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 填写手机号 和已存在的手机号相同，点击确定，报错
        driver = User_Add.Reopen_edit_form(driver)  # 点击取消，重新打开编辑界面
        driver = User_Add.UserImWrite(driver, name=name[13], mail=mail[2], phonenum=phonenum[0], psd=psd[5])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        data.write_imf(user1[0], user1[1], user1[2], user1[3])
        data.write_imf(user2[0], user2[1], user2[2], user2[3])
        return driver

    @staticmethod
    def CheckOrgandRole(driver):  # 检查组织和角色
        # 组织下拉框为空，光标移至角色下拉框
        # above = driver.find_element_by_xpath(User_Add.role_list_show_xpath)
        # ActionChains(driver).move_to_element(above).perform()
        # time.sleep(3)
        # 组织下拉框
        driver.find_element_by_xpath(User_Add.org_list_show_xpath).click()
        time.sleep(3)
        driver.find_element_by_xpath(User_Add.org_choice_xpath).click()
        time.sleep(1)
        # 角色下拉框
        driver.find_element_by_xpath(User_Add.role_list_show_xpath).click()
        time.sleep(3)
        driver.find_element_by_xpath(User_Add.role_choice_xpath).click()
        time.sleep(1)
        return driver

    @staticmethod
    def CheckPasswrod(driver):  # 检查初始密码
        psd = data.get_new_passwrod()  # 获取一些密码字符串
        # 输入5种格式不正确的密码，点击确定，提示报错
        driver.find_element_by_xpath(User_Add.Password_input_xpath).send_keys(psd[0])
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Password_eye_input_xpath).click()  # 点击小眼睛查看密码
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Password_eye_input_xpath).click()  # 点击小眼睛隐藏密码
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Password_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Password_input_xpath).send_keys(psd[1])
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Password_eye_input_xpath).click()  # 点击小眼睛查看密码
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Password_eye_input_xpath).click()  # 点击小眼睛隐藏密码
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Password_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Password_input_xpath).send_keys(psd[2])
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Password_eye_input_xpath).click()  # 点击小眼睛查看密码
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Password_eye_input_xpath).click()  # 点击小眼睛隐藏密码
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，重新打开编辑界面
        driver = User_Add.Reopen_edit_form(driver)
        driver.find_element_by_xpath(User_Add.Password_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Password_input_xpath).send_keys(psd[3])
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Password_eye_input_xpath).click()  # 点击小眼睛查看密码
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Password_eye_input_xpath).click()  # 点击小眼睛隐藏密码
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Password_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Password_input_xpath).send_keys(psd[4])
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Password_eye_input_xpath).click()  # 点击小眼睛查看密码
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Password_eye_input_xpath).click()  # 点击小眼睛隐藏密码
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入正确格式的密码，点击确定，不提示错误
        driver.find_element_by_xpath(User_Add.Password_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Password_input_xpath).send_keys(psd[5])
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Password_eye_input_xpath).click()  # 点击小眼睛查看密码
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Password_eye_input_xpath).click()  # 点击小眼睛隐藏密码
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        return driver

    @staticmethod
    def CheckPhonenumber(driver):  # 检查手机号码
        phonenupmber = ["13231", "wwwcom", "汉字163", "1334637287", "weq3#!@efgg", "sjh汉字12英文", "17628372938",
                        "19026757372"]
        # 输入6种格式不正确的手机号码，点击确定，提示报错
        driver.find_element_by_xpath(User_Add.Phonenumber_input_xpath).send_keys(phonenupmber[0])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Phonenumber_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Phonenumber_input_xpath).send_keys(phonenupmber[1])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Phonenumber_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Phonenumber_input_xpath).send_keys(phonenupmber[2])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，重新打开编辑界面
        driver = User_Add.Reopen_edit_form(driver)
        driver.find_element_by_xpath(User_Add.Phonenumber_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Phonenumber_input_xpath).send_keys(phonenupmber[3])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Phonenumber_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Phonenumber_input_xpath).send_keys(phonenupmber[4])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Phonenumber_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Phonenumber_input_xpath).send_keys(phonenupmber[5])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入2种格式正确的邮箱，点击确定，合法，不提示报错
        driver.find_element_by_xpath(User_Add.Phonenumber_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Phonenumber_input_xpath).send_keys(phonenupmber[6])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，重新打开编辑界面
        driver = User_Add.Reopen_edit_form(driver)
        driver.find_element_by_xpath(User_Add.Phonenumber_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Phonenumber_input_xpath).send_keys(phonenupmber[7])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)

        return driver

    @staticmethod
    def CheckMailbox(driver):  # 检查邮箱
        mail = ["13231", "@www.com", "汉字@163.com", "#$au@qq.com", "weqe", "sj12", "liulei@deepait.com",
                "690267573@qq.com"]
        # 输入6种格式不正确的邮箱，点击确定，提示报错
        driver.find_element_by_xpath(User_Add.Mailbox_input_xpath).send_keys(mail[0])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Mailbox_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Mailbox_input_xpath).send_keys(mail[1])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Mailbox_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Mailbox_input_xpath).send_keys(mail[2])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，重新打开编辑界面
        driver = User_Add.Reopen_edit_form(driver)
        driver.find_element_by_xpath(User_Add.Mailbox_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Mailbox_input_xpath).send_keys(mail[3])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Mailbox_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Mailbox_input_xpath).send_keys(mail[4])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.Mailbox_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Mailbox_input_xpath).send_keys(mail[5])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 输入2种格式正确的邮箱，点击确定，合法，不提示报错
        driver.find_element_by_xpath(User_Add.Mailbox_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Mailbox_input_xpath).send_keys(mail[6])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，重新打开编辑界面
        driver = User_Add.Reopen_edit_form(driver)
        driver.find_element_by_xpath(User_Add.Mailbox_input_xpath).clear()
        driver.find_element_by_xpath(User_Add.Mailbox_input_xpath).send_keys(mail[7])
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
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

    @staticmethod
    def Reopen_edit_form(driver):  # 点击取消，重新打开编辑界面
        # 点击取消，回到界面
        driver.find_element_by_xpath(User_Add.user_add_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.user_add_button_xpath).click()  # 重新点击新增用户按钮
        time.sleep(1)
        return driver

    @staticmethod
    def ChoiceOrg(driver):
        org_choice_xpath1 = "/html/body/div[4]/div[1]/div[1]/ul/li[{}]/span"  # 选择组织的xpath
        # "/html/body/div[4]/div[1]/div[1]/ul/li[3]/span"
        driver.find_element_by_xpath(User_Add.org_list_show_xpath).click()
        time.sleep(1)
        try:  # 选择组织的xpath在变化，所以用一个判断来选到正确的组织xpath
            driver.implicitly_wait(1)
            org_name_str = driver.find_element_by_xpath(org_choice_xpath1.format(1)).text
        except:
            org_choice_xpath1 = "/html/body/div[3]/div[1]/div[1]/ul/li[{}]/span"
        finally:
            driver.implicitly_wait(30)
        time.sleep(1)
        # print(org_choice_xpath1)
        # time.sleep(10000)
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
        return driver, org_name_str

    @staticmethod
    def ChoiceRole(driver):
        # role_list_show_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[7]/div/div/div[1]/span"  # 打开选择角色下拉框的xpath
        role_choice_xpath1 = "/html/body/div[4]/div[1]/div[1]/ul/li[{}]/span"  # 选择第一个角色的xpath
        # /html/body/div[4]/div[1]/div[1]/ul/li[2]/span
        driver.find_element_by_xpath(User_Add.role_list_show_xpath).click()
        role_conut = 1
        while (role_conut):
            try:
                driver.implicitly_wait(1)
                role_name_str = driver.find_element_by_xpath(role_choice_xpath1.format(role_conut)).text
                driver.implicitly_wait(30)
            except:
                driver.implicitly_wait(30)
                break
            role_conut = role_conut + 1
        if (role_conut == 1):
            return driver, ''
        role_conut = random.randint(1, role_conut - 1)
        role_name_str = driver.find_element_by_xpath(role_choice_xpath1.format(role_conut)).text
        driver.find_element_by_xpath(role_choice_xpath1.format(role_conut)).click()
        return driver, role_name_str

    @staticmethod
    def UserImWrite(driver, name="a", mail="a", phonenum="a", psd="a", writedata=0):
        if (name != "a"):
            driver.find_element_by_xpath(User_Add.user_name_input_xpath).send_keys(name)
            time.sleep(1)
        if (writedata == 0):
            driver.find_element_by_xpath(User_Add.Man_choice_xpath).click()
            time.sleep(1)
        if (mail != "a"):
            driver.find_element_by_xpath(User_Add.Mailbox_input_xpath).send_keys(mail)
            time.sleep(1)
        if (phonenum != "a"):
            driver.find_element_by_xpath(User_Add.Phonenumber_input_xpath).send_keys(phonenum)
            time.sleep(1)
        if (psd != "a"):
            driver.find_element_by_xpath(User_Add.Password_input_xpath).send_keys(psd)
            time.sleep(1)
        if (writedata == 0):
            driver.find_element_by_xpath(User_Add.org_list_show_xpath).click()
            time.sleep(1)
            try:  # 选择组织的xpath在变化，所以用一个判断来选到正确的组织
                driver.implicitly_wait(1)
                driver.find_element_by_xpath(User_Add.org_choice_xpath).click()
            except:
                driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[1]/span").click()
            finally:
                driver.implicitly_wait(30)
            time.sleep(1)
            driver.find_element_by_xpath(User_Add.role_list_show_xpath).click()
            time.sleep(1)
            driver.find_element_by_xpath(User_Add.role_choice_xpath).click()
            time.sleep(1)
        else:
            role_name_str = ''
            while (role_name_str == ''):
                driver, org_name_str = User_Add.ChoiceOrg(driver)
                driver, role_name_str = User_Add.ChoiceRole(driver)
            timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            workxls.writedata('userdata.xls', name, '女', org_name_str, role_name_str, phonenum, mail, timestr, psd)
        return driver

    @staticmethod
    def UserAdd(driver, writedata=0, sorf=0):
        name = data.get_some_name()
        if sorf:
            name[13] = driver.find_element_by_xpath(
                "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div").text
        mail = data.get_some_mailbox()
        phonenum = data.get_some_phonenum()
        psd = data.get_new_passwrod()
        # # 新增特定用户
        # name = ["组织A角色1", "组织A角色2", "组织B角色1", "组织B角色2", "组织B管理员"]
        # for i in name:
        #     driver = User_Add.UserImWrite(driver, i, mail[0], phonenum[0], psd[5])
        #     driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        #     data.write_imf(name[13], mail[0], phonenum[0], psd[5])
        #     time.sleep(2)
        #     driver.find_element_by_xpath(User_Add.user_add_button_xpath).click()

        # 填写所有要素
        if (writedata):
            print('=============================')
            time.sleep(2)
            driver.find_element_by_xpath(User_Add.user_add_button_xpath).click()
            driver = User_Add.UserImWrite(driver, name[13], mail[0], phonenum[0], psd[5], writedata)
        else:
            driver = User_Add.UserImWrite(driver, name[13], mail[0], phonenum[0], psd[5])
        time.sleep(1)
        driver.find_element_by_xpath(User_Add.user_add_confirm_button_xpath).click()
        # 记录要素信息
        data.write_imf(name[13], mail[0], phonenum[0], psd[5])
        if sorf:
            driver.find_element_by_xpath(User_Add.user_add_cancel_button_xpath).click()
        return driver

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
