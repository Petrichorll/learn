# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, random
import sys, re

sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")
import login, data, workxls, role_add
from selenium.webdriver.common.action_chains import ActionChains


# 角色编辑(修改)
class Role_Edit(unittest.TestCase):
    role_name_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[2]/form/div[2]/div/div/input"  # 输入名称编辑框的xpath
    role_edit_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath
    role_edit_cancel_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div/div/div[3]/div/button[2]/span"  # 取消按钮的xpath

    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 角色编辑用例
    def test_Role_Edit(self):
        driver = self.driver
        name = data.get_some_name()  # 获取一些名字字符串
        # organization_edit_button_xpath = self.get_role_edit_button_xpath(driver)  # 编辑角色按钮的xpath
        time.sleep(1)

        # 点击菜单栏角色管理
        driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[6]").click()
        time.sleep(1)  # 预留时间查看
        # 选一个编辑角色按钮，点击，弹出编辑框
        driver.find_element_by_xpath(self.get_role_edit_button_xpath(driver)).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(self.role_edit_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(self.get_role_edit_button_xpath(driver)).click()  # 重新选一个编辑角色按钮，点击，弹出编辑框
        time.sleep(1)
        # 直接点击确定，未作修改，提示操作成功
        driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
        time.sleep(1)
        # # 什么都不输入，点击确定，提示报错
        # driver.find_element_by_xpath(self.get_role_edit_button_xpath(driver)).click()  # 重新选一个编辑角色按钮，点击，弹出编辑框
        # driver.find_element_by_xpath(self.role_name_input_xpath).clear()
        # driver.find_element_by_xpath(self.role_name_input_xpath).send_keys("")
        # time.sleep(1)
        # driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
        # time.sleep(7)
        # 输入一个汉字字符，点击确定，提示报错
        driver.find_element_by_xpath(self.get_role_edit_button_xpath(driver)).click()  # 重新选一个编辑角色按钮，点击，弹出编辑框
        driver.find_element_by_xpath(self.role_name_input_xpath).clear()
        driver.find_element_by_xpath(self.role_name_input_xpath).send_keys(name[0])
        driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入一个数字字符，点击确定，提示报错
        driver.find_element_by_xpath(self.role_name_input_xpath).clear()
        driver.find_element_by_xpath(self.role_name_input_xpath).send_keys(name[1])
        driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入一个英文字符，点击确定，提示报错
        driver.find_element_by_xpath(self.role_name_input_xpath).clear()
        driver.find_element_by_xpath(self.role_name_input_xpath).send_keys(name[2])
        driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入一个特殊符号，点击确定，提示报错
        driver.find_element_by_xpath(self.role_name_input_xpath).clear()
        driver.find_element_by_xpath(self.role_name_input_xpath).send_keys(name[3])
        driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(self.role_edit_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(self.get_role_edit_button_xpath(driver)).click()  # 重新选一个编辑角色按钮，点击，弹出编辑框
        time.sleep(1)
        # 输入13个汉字字符，点击确定，提示报错
        driver.find_element_by_xpath(self.role_name_input_xpath).clear()
        driver.find_element_by_xpath(self.role_name_input_xpath).send_keys(name[4])
        driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入12个数字字符，点击确定，提示报错
        driver.find_element_by_xpath(self.role_name_input_xpath).clear()
        driver.find_element_by_xpath(self.role_name_input_xpath).send_keys(name[5])
        driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入11个英文字符，点击确定，提示报错
        driver.find_element_by_xpath(self.role_name_input_xpath).clear()
        driver.find_element_by_xpath(self.role_name_input_xpath).send_keys(name[6])
        driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入6个汉字+符号，点击确定，提示报错
        driver.find_element_by_xpath(self.role_name_input_xpath).clear()
        driver.find_element_by_xpath(self.role_name_input_xpath).send_keys(name[7])
        driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(self.role_edit_cancel_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(self.get_role_edit_button_xpath(driver)).click()  # 重新选一个编辑角色按钮，点击，弹出编辑框
        time.sleep(1)
        # 输入6个数字+符号，点击确定，提示报错
        driver.find_element_by_xpath(self.role_name_input_xpath).clear()
        driver.find_element_by_xpath(self.role_name_input_xpath).send_keys(name[8])
        driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入6个字母+符号，点击确定，提示报错
        driver.find_element_by_xpath(self.role_name_input_xpath).clear()
        driver.find_element_by_xpath(self.role_name_input_xpath).send_keys(name[9])
        driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入2个汉字，点击确定，修改成功
        driver.find_element_by_xpath(self.role_name_input_xpath).clear()
        driver.find_element_by_xpath(self.role_name_input_xpath).send_keys(name[10])
        driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入5个数字，点击确定，修改成功
        driver.find_element_by_xpath(self.get_role_edit_button_xpath(driver)).click()  # 重新选一个编辑角色按钮，点击，弹出编辑框
        driver.find_element_by_xpath(self.role_name_input_xpath).clear()
        driver.find_element_by_xpath(self.role_name_input_xpath).send_keys(name[11])
        driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(self.get_role_edit_button_xpath(driver)).click()  # 重新选一个编辑角色按钮，点击，弹出编辑框
        driver.find_element_by_xpath(self.role_edit_cancel_button_xpath).click()
        time.sleep(1)
        # 输入10个字母，点击确定，修改成功
        driver.find_element_by_xpath(self.get_role_edit_button_xpath(driver)).click()  # 重新选一个编辑角色按钮，点击，弹出编辑框
        driver.find_element_by_xpath(self.role_name_input_xpath).clear()
        driver.find_element_by_xpath(self.role_name_input_xpath).send_keys(name[12])
        driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入6位汉字数字字母混合，点击确定，修改成功
        driver.find_element_by_xpath(self.get_role_edit_button_xpath(driver)).click()  # 重新选一个编辑角色按钮，点击，弹出编辑框
        driver.find_element_by_xpath(self.role_name_input_xpath).clear()
        driver.find_element_by_xpath(self.role_name_input_xpath).send_keys(name[13])
        driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
        time.sleep(1)
        # 输入已存在的角色名称
        llist = self.is_exit_diffrent_org_roles(driver)
        if (llist):
            Lname = driver.find_element_by_xpath(
                "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[2]/div[3]/table/tbody/tr[" + str(
                    llist[0]) + "]/td[2]/div").text
            print(Lname)
            # 选择不同组织下的另一个角色，改为已存在的名字，修改成功
            driver.find_element_by_xpath(self.get_role_edit_button_xpath(driver, llist[2])).click()
            driver.find_element_by_xpath(self.role_name_input_xpath).clear()
            driver.find_element_by_xpath(self.role_name_input_xpath).send_keys(Lname)
            driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
            time.sleep(3)
            # 选择相同组织下的另一个角色，改为已存在的名字，提示报错
            driver.find_element_by_xpath(self.get_role_edit_button_xpath(driver, llist[1])).click()
            driver.find_element_by_xpath(self.role_name_input_xpath).clear()
            driver.find_element_by_xpath(self.role_name_input_xpath).send_keys(Lname)
            driver.find_element_by_xpath(self.role_edit_confirm_button_xpath).click()
            time.sleep(3)
        else:
            raise NameError("输入已存在的角色名称用例失败，建议手工测试，失败原因：一页中没有相同或者相异的组织名称!")
        time.sleep(3)
        time.sleep(3)
        driver.close()

    @staticmethod
    def get_role_edit_button_xpath(driver, i=0):  # 获取编辑角色按钮的xpath，页面上随机选取一个来编辑，并将光标移动至编辑按钮上
        driver.implicitly_wait(1)
        if (i == 0):
            i = random.randint(1, 10)
        ret = ""
        # driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[5]").click()
        # driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div/ul/li[7]").click()
        while (i):
            # print(i)
            ret = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[2]/div[3]/table/tbody/tr[" + str(
                i) + "]/td[5]/div/a[1]/span"
            try:
                driver.find_element_by_xpath(ret)
                driver.implicitly_wait(30)
                break
            except:
                i = i - 1
        if i > 5:  # 如果选到了6-10的角色，下拉滚动条至底部
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
    def is_exit_diffrent_org_roles(driver):  # 每一页都去find_diffrent_org_roles返回list，如果有0，则返回[],否则返回list
        while (1):
            list = Role_Edit.find_diffrent_org_roles(driver)
            if (list[1] == 0 or list[2] == 0):
                hstr = driver.find_element_by_xpath(
                    "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div/button[2]").get_attribute(
                    'outerHTML')  # 获取">"的html
                # print(hstr)
                if (re.search("disabled", hstr)):  # 获取">"的html里面包含"disabled"，则它不能被点击，找了所有页面都没有符合条件的数据，返回空
                    return []
                driver.find_element_by_xpath(
                    "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div/button[2]").click()
            else:
                break
        return list

    @staticmethod
    def find_diffrent_org_roles(driver):
        ret = [1, 0, 0]
        # driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[6]").click()
        # str1记录当前页面第1条角色信息的组织名称
        str1 = driver.find_element_by_xpath(
            "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[3]/div").text
        i = 2
        while (i < 11):
            try:
                driver.implicitly_wait(1)
                # str2记录当前页面第2-10条角色信息的组织名称
                str2 = driver.find_element_by_xpath(
                    "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[2]/div[3]/table/tbody/tr[" + str(
                        i) + "]/td[3]/div").text
            except:
                break
            # 如果当前条组织名称和第1条相同，给ret[1]赋予上当前条的i
            if (str1 == str2 and ret[1] == 0):
                ret[1] = i
            # 如果当前条组织名称和第1条不同，给ret[2]赋予上当前条的i
            if (str1 != str2 and ret[2] == 0):
                ret[2] = i
            i = i + 1
        driver.implicitly_wait(30)
        return ret  # 返回元素中：ret[0]和ret[1]相同，ret[0]和ret[2]不同

    @staticmethod
    def RoleEdit(driver, sorf=0):
        name = data.get_some_name()
        namestr = name[13]
        time.sleep(1)
        # 如果成功或者失败参数为1，则添加一个和第一个角色相同组织的角色，再执行
        if (sorf == 1):
            role_edit_button_xpath = Role_Edit.get_role_edit_button_xpath(driver, 1)  # 参数选1，表示选第一个角色的编辑按钮xpath
            role_orgname_xpath = role_edit_button_xpath.replace("5]/div/a[1]/span", "3]/div")
            role_rolename_xpath = role_edit_button_xpath.replace("5]/div/a[1]/span", "2]/div")
            namestr = driver.find_element_by_xpath(role_rolename_xpath).text
            org_name_str = driver.find_element_by_xpath(role_orgname_xpath).text
            driver = role_add.Role_Add.RoleAdd(driver, 1, orgname=org_name_str)
        time.sleep(1)
        # 选第一个编辑角色按钮，点击，弹出编辑框
        role_edit_button_xpath = Role_Edit.get_role_edit_button_xpath(driver, 1)  # 参数选1，表示选第一个角色的编辑按钮xpath
        role_orgname_xpath = role_edit_button_xpath.replace("5]/div/a[1]/span", "3]/div")
        org_name_str = driver.find_element_by_xpath(role_orgname_xpath).text
        # "//*[@id="app"]/div/div[2]/section/section/div/div/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/a[1]/span"
        # "//*[@id="app"]/div/div[2]/section/section/div/div/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[3]/div"
        driver.find_element_by_xpath(role_edit_button_xpath).click()
        time.sleep(1)
        driver.find_element_by_xpath(Role_Edit.role_name_input_xpath).clear()
        driver.find_element_by_xpath(Role_Edit.role_name_input_xpath).send_keys(namestr)
        time.sleep(1)
        driver.find_element_by_xpath(Role_Edit.role_edit_confirm_button_xpath).click()

        timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        workxls.writedata('roledata.xls', namestr, org_name_str, timestr)

        # 如果成功或者失败参数为1，则需要点击取消
        if (sorf == 1):
            time.sleep(1)
            driver.find_element_by_xpath(Role_Edit.role_edit_cancel_button_xpath).click()
        return driver

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
