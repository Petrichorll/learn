# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import sys

sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")
import login, data


class User_Settings(unittest.TestCase):
    change_psw_button_xpath = "//div[@class='el-card__body']/div/div/div[7]/a/span"  # 修改/绑定密码按钮的xpath
    change_uesrname_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div/div[3]/a/span"  # 修改/绑定用户名按钮的xpath
    change_uesrname_text_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div/div[3]/div/span"  # 用户名文本的xpath
    change_uesrname_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div/div[3]/div/form/div/div/div[1]/input"  # 用户名输入框的xpath
    original_psw_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div[2]/div/form/div/div/div[1]/div/div/input"  # 原始密码输入框
    original_psw_eye_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div[2]/div/form/div/div/div[1]/div/span"  # 原始密码输入框小眼睛
    new_psw_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div[2]/div/form/div/div/div[2]/div/div/input"
    new_psw_eye_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div[2]/div/form/div/div/div[2]/div/span"  # 新密码输入框小眼睛
    change_psw_confirm_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div[3]/span/button[1]/span"
    change_psw_cancel_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div[3]/span/button[2]/span"

    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 修改密码用例
    def test_Change_Password(self):
        driver = self.driver
        driver = User_Settings.open_usersetting_page(driver)

        # 点击修改密码
        driver.find_element_by_xpath(User_Settings.change_psw_button_xpath).click()
        time.sleep(1)
        # old_pwd_str = data.get_un_pw()[1]
        for pwd_str in data.get_new_passwrod():
            # 清空原密码
            driver.find_element_by_xpath(User_Settings.original_psw_input_xpath).clear()
            # 填写原密码
            driver.find_element_by_xpath(User_Settings.original_psw_input_xpath).send_keys(pwd_str)
            time.sleep(1)
            # 点击小眼睛
            driver.find_element_by_xpath(User_Settings.original_psw_eye_xpath).click()
            time.sleep(1)
            # 再次点击小眼睛
            driver.find_element_by_xpath(User_Settings.original_psw_eye_xpath).click()
            time.sleep(1)
            # 清空新密码
            driver.find_element_by_xpath(User_Settings.new_psw_input_xpath).clear()
            # 填写新密码
            driver.find_element_by_xpath(User_Settings.new_psw_input_xpath).send_keys(pwd_str)
            time.sleep(1)
            # 点击小眼睛
            driver.find_element_by_xpath(User_Settings.new_psw_eye_xpath).click()
            time.sleep(1)
            # 再次点击小眼睛
            driver.find_element_by_xpath(User_Settings.new_psw_eye_xpath).click()
            time.sleep(1)
            # 点击确定按钮
            driver.find_element_by_xpath(User_Settings.change_psw_confirm_xpath).click()
            time.sleep(1)
            # 点击取消按钮
            driver.find_element_by_xpath(User_Settings.change_psw_cancel_xpath).click()
            time.sleep(1)
            # 点击修改密码
            driver.find_element_by_xpath(User_Settings.change_psw_button_xpath).click()
            time.sleep(1)
        # 清空原密码
        driver.find_element_by_xpath(User_Settings.original_psw_input_xpath).clear()
        # 填写原密码
        driver.find_element_by_xpath(User_Settings.original_psw_input_xpath).send_keys(data.get_un_pw()[1])
        time.sleep(1)
        # 点击小眼睛
        driver.find_element_by_xpath(User_Settings.original_psw_eye_xpath).click()
        time.sleep(1)
        # 再次点击小眼睛
        driver.find_element_by_xpath(User_Settings.original_psw_eye_xpath).click()
        time.sleep(1)
        # 清空新密码
        driver.find_element_by_xpath(User_Settings.new_psw_input_xpath).clear()
        # 填写新密码
        driver.find_element_by_xpath(User_Settings.new_psw_input_xpath).send_keys(pwd_str)
        time.sleep(1)
        # 点击小眼睛
        driver.find_element_by_xpath(User_Settings.new_psw_eye_xpath).click()
        time.sleep(1)
        # 再次点击小眼睛
        driver.find_element_by_xpath(User_Settings.new_psw_eye_xpath).click()
        time.sleep(1)
        # 修改data文件
        data.change_passwrod(pwd_str)
        # 点击确定按钮
        driver.find_element_by_xpath(User_Settings.change_psw_confirm_xpath).click()
        time.sleep(1)

        time.sleep(2)
        driver.close()

    # 修改用户名用例
    def test_Change_Username(self):
        driver = self.driver
        driver = User_Settings.open_usersetting_page(driver)

        # 判断按钮文本
        username = driver.find_element_by_xpath(User_Settings.change_uesrname_text_xpath).text
        buttontext = driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).text
        if (username == ''):
            if (buttontext != '添加'):
                raise AssertionError("\n按钮文本错误，应该为添加")
        else:
            if (buttontext != '修改'):
                raise AssertionError("\n按钮文本错误，应该为修改")

        # 点击添加/修改按钮,出现输入框
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 检查按钮文本
        buttontext = driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).text
        if (buttontext != '确定'):
            raise AssertionError("\n按钮文本错误，应该为确定")
        name = data.get_some_name()
        # 输入一个汉字字符，点击确定，提示报错
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).clear()
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).send_keys(name[0])
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 输入一个数字字符，点击确定，提示报错
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).clear()
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).send_keys(name[1])
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 输入一个英文字符，点击确定，提示报错
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).clear()
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).send_keys(name[2])
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 输入一个特殊符号，点击确定，提示报错
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).clear()
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).send_keys(name[3])
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 输入13个汉字字符，点击确定，提示报错
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).clear()
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).send_keys(name[4])
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 输入12个数字字符，点击确定，提示报错
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).clear()
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).send_keys(name[5])
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 输入11个英文字符，点击确定，提示报错
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).clear()
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).send_keys(name[6])
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 输入6个汉字+符号，点击确定，提示报错
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).clear()
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).send_keys(name[7])
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 输入6个数字+符号，点击确定，提示报错
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).clear()
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).send_keys(name[8])
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 输入6个字母+符号，点击确定，提示报错
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).clear()
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).send_keys(name[9])
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 输入2个汉字，点击确定，合法，不提示报错，修改成功
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).clear()
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).send_keys(name[10])
        time.sleep(1)
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 检查文本
        username = driver.find_element_by_xpath(User_Settings.change_uesrname_text_xpath).text
        buttontext = driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).text
        if (username == name[10]):
            if (buttontext != '修改'):
                raise AssertionError("\n按钮文本错误，应该为修改")
        else:
            raise AssertionError("\n用户名文本错误，应该为{}".format(name[10]))

        # 点击添加/修改按钮,出现输入框
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 检查按钮文本
        buttontext = driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).text
        if (buttontext != '确定'):
            raise AssertionError("\n按钮文本错误，应该为确定")
        # 输入5个数字，点击确定，合法，不提示报错
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).clear()
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).send_keys(name[11])
        time.sleep(1)
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 检查文本
        username = driver.find_element_by_xpath(User_Settings.change_uesrname_text_xpath).text
        buttontext = driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).text
        print(username)
        if (username == name[11]):
            if (buttontext != '修改'):
                raise AssertionError("\n按钮文本错误，应该为修改")
        else:
            raise AssertionError("\n用户名文本错误，应该为{}".format(name[11]))

        # 点击添加/修改按钮,出现输入框
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 检查按钮文本
        buttontext = driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).text
        if (buttontext != '确定'):
            raise AssertionError("\n按钮文本错误，应该为确定")
        # 输入10个字母，点击确定，合法，不提示报错
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).clear()
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).send_keys(name[12])
        time.sleep(1)
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 检查文本
        username = driver.find_element_by_xpath(User_Settings.change_uesrname_text_xpath).text
        buttontext = driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).text
        if (username == name[12]):
            if (buttontext != '修改'):
                raise AssertionError("\n按钮文本错误，应该为修改")
        else:
            raise AssertionError("\n用户名文本错误，应该为{}".format(name[12]))

        # 点击添加/修改按钮,出现输入框
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 检查按钮文本
        buttontext = driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).text
        if (buttontext != '确定'):
            raise AssertionError("\n按钮文本错误，应该为确定")
        # 输入6位汉字数字字母混合，点击确定，合法，不提示报错
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).clear()
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).send_keys(name[13])
        time.sleep(1)
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 检查文本
        username = driver.find_element_by_xpath(User_Settings.change_uesrname_text_xpath).text
        buttontext = driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).text
        if (username == name[13]):
            if (buttontext != '修改'):
                raise AssertionError("\n按钮文本错误，应该为修改")
        else:
            raise AssertionError("\n用户名文本错误，应该为{}".format(name[13]))

        # 点击添加/修改按钮,出现输入框
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)
        # 检查按钮文本
        buttontext = driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).text
        if (buttontext != '确定'):
            raise AssertionError("\n按钮文本错误，应该为确定")
        # 输入6位汉字数字字母混合，点击确定，合法，不提示报错
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).clear()
        driver.find_element_by_xpath(User_Settings.change_uesrname_input_xpath).send_keys("管理员")
        time.sleep(1)
        driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).click()
        time.sleep(1)# 可截屏
        # 刷新页面
        driver.refresh()
        time.sleep(1)
        # 检查文本
        username = driver.find_element_by_xpath(User_Settings.change_uesrname_text_xpath).text
        buttontext = driver.find_element_by_xpath(User_Settings.change_uesrname_button_xpath).text
        if (username == name[13]):
            if (buttontext != '修改'):
                raise AssertionError("\n按钮文本错误，应该为修改")
        else:
            raise AssertionError("\n用户名文本错误，应该为{}".format(name[13]))
        


        print(buttontext)
        time.sleep(1)
        driver.close()

    @staticmethod
    def open_usersetting_page(driver):  # 打开设置界面
        # 点击下拉框
        driver.find_element_by_class_name("el-icon-caret-bottom").click()
        time.sleep(1)
        # 再点击下拉框下的选项-账号设置
        driver.find_element_by_xpath("/html/body/ul/a/li").click()
        time.sleep(1)
        return driver

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
