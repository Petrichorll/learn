# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, random
import sys, re

sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")
import login, data, workxls,subtag_add
from selenium.webdriver.common.action_chains import ActionChains


# 子标签删除
class Subtag_Delete(unittest.TestCase):
    label_management_xpath = "/html/body/div/div/div[1]/div[2]/div[1]/div/ul[1]/div[10]/a/li"  # 标签管理菜单的xpath
    subtag_delete_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div[3]/table/tbody/tr[{}]/td[5]/div/a[2]/span"  # 删除子标签按钮
    subtag_delete_tips_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[2]/div/div/p[1]"  # 子标签删除提示信息的xpath
    subtag_delete_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[3]/span/button[1]/span"  # 确定按钮的xpath
    subtag_delete_cancel_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[3]/span/button[2]/span"  # 取消按钮的xpath
    subtag_all_from_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div[3]/table/tbody"

    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    @staticmethod
    def get_subtag_delete_button_xpath(driver):  # 获取删除子标签按钮的xpath，页面上随机选取一个来编辑，并将光标移动至删除按钮上
        time.sleep(1)
        all_tr_str = driver.find_element_by_xpath(Subtag_Delete.subtag_all_from_xpath).get_attribute('outerHTML')
        tr_list = re.findall('tr', all_tr_str)
        tr_count = int(len(tr_list) / 2)
        i = random.randint(1, tr_count)
        ret = Subtag_Delete.subtag_delete_button_xpath.format(str(i))
        if i > 5:  # 如果选到了6-10的组织，下拉滚动条至底部
            js = "var q=document.documentElement.scrollTop=10000"
            driver.execute_script(js)
            time.sleep(1)
        else:
            js = "var q=document.documentElement.scrollTop=0"
            driver.execute_script(js)
            time.sleep(1)
        above = driver.find_element_by_xpath(ret)  # 移动光标至删除按钮
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(3)  # 预留时间查看效果
        return ret

    # 子标签删除用例
    def test_Subtag_Delete(self):
        driver = self.driver

        # 点击菜单栏标签管理
        driver.find_element_by_xpath(Subtag_Delete.label_management_xpath).click()
        time.sleep(1)  # 预留时间查看
        # 选择一个主标签，点击查看子标签按钮
        driver = subtag_add.Subtag_Add.open_subtag_page(driver)
        # 选一个删除子标签按钮，点击，弹出确认框
        driver.find_element_by_xpath(Subtag_Delete.get_subtag_delete_button_xpath(driver)).click()
        tips = driver.find_element_by_xpath(Subtag_Delete.subtag_delete_tips_xpath).text
        if (tips != "确定删除子标签吗？"):
            raise AssertionError("\n删除子标签时，提示信息不正确！")
        time.sleep(1)
        # 点击取消，回到界面
        driver.find_element_by_xpath(Subtag_Delete.subtag_delete_cancel_button_xpath).click()
        time.sleep(1)
        # 点击确定，直接删除
        driver.find_element_by_xpath(
            Subtag_Delete.get_subtag_delete_button_xpath(driver)).click()  # 重新选一个删除子标签按钮，点击，弹出确认框
        time.sleep(1)
        driver.find_element_by_xpath(Subtag_Delete.subtag_delete_confirm_button_xpath).click()
        time.sleep(1)

        return driver

        # @staticmethod
        # def OrganizationDelete(driver):
        #     # 选一个删除组织按钮，点击，弹出确认框
        #     one_orgd_xpath = Orga
        #     nization_Delete.get_organization_delete_button_xpath(driver)
        #     # 记录一下删除组织的名称
        #     one_orgn_xpath = one_orgd_xpath
        #     one_orgn_xpath = one_orgn_xpath.replace("]/td[5]/div/a[2]/span", "]/td[2]/div")
        #     namestr = driver.find_element_by_xpath(one_orgn_xpath).text
        #     driver.find_element_by_xpath(one_orgd_xpath).click()
        #     time.sleep(1)
        #     # 点击确定，直接删除
        #     driver.find_element_by_xpath(Organization_Delete.organization_delete_confirm_button_xpath).click()
        #     timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        #     time.sleep(2)
        #     workxls.writedata('orgdata.xls', namestr, timestr)
        #     return driver

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
