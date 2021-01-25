# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import sys

sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")
sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\test_case")
import login, organization_add, workxls
from selenium.webdriver.common.action_chains import ActionChains


# 组织查询
class Organization_Query(unittest.TestCase):
    menubar_orgmanagement_xpath = "//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[5]"  # 菜单栏组织管理按钮的xpath
    data_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[{}]/div"  # 组织查询的任一行任一元素的xpath
    data_xpath2 = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[2]/div"  # 组织查询的任一行第二个元素的xpath
    nextpage_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div/button[2]/i"  # 下一页按钮的xpath
    nextpage_xpath2 = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div/button[2]"  # 下一页按钮的html位置
    search_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[1]/div/div/input"  # 搜索框的输入框的xpath
    search_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[1]/div/div/span/span/i"  # 搜索框的搜索按钮的xpath

    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 组织查询用例
    def test_Organization_Query(self):
        driver = self.driver
        # 点击菜单栏组织管理
        driver.find_element_by_xpath(Organization_Query.menubar_orgmanagement_xpath).click()
        time.sleep(1)
        # # 新增50个组织，需要的时候才释放出来执行
        # count = 50
        # while (count):
        #     driver = organization_add.Organization_Add.OrganizationAdd(driver)
        #     time.sleep(1)
        #     count = count - 1
        count = count1 = 3
        # 新增x个组织,并记录到orgdata.xls，以供检查      
        while (count):
            driver = organization_add.Organization_Add.OrganizationAdd(driver, 1)
            time.sleep(1)
            count = count - 1
        # 重新点击菜单栏组织管理，检查查询结果，和orgdata.xls里的数据对比
        driver.find_element_by_xpath(Organization_Query.menubar_orgmanagement_xpath).click()
        time.sleep(1)
        i = 0
        while (i < count1):
            data1 = workxls.getimf('orgdata.xls', i)
            data2 = driver.find_element_by_xpath(Organization_Query.data_xpath.format(i + 1, 2)).text
            data3 = driver.find_element_by_xpath(Organization_Query.data_xpath.format(i + 1, 4)).text
            print(data1, data2, data3)
            if (data1[0] != data2):
                raise AssertionError('网页的组织名称\"{}\"和本地记录里的组织名称\"{}\"不一致！'.format(data1[0], data2))
            if (data1[1][:-1] != data3[:-1]):
                raise AssertionError('组织名称：{}，网页的操作时间\"{}\"和本地记录里的新增时间\"{}\"不一致！'.format(data1[0], data1[1], data3))
            i = i + 1
        driver.close()

    # 组织查询排序检查用例
    def test_Organization_Query_Sort(self):
        driver = self.driver
        # 点击菜单栏组织管理
        driver.find_element_by_xpath(Organization_Query.menubar_orgmanagement_xpath).click()
        time.sleep(1)
        time.sleep(1)
        i = 2
        while (i):
            timestr1 = driver.find_element_by_xpath(Organization_Query.data_xpath.format(i - 1, 4)).text
            if (i == 11):
                next_button_str = driver.find_element_by_xpath(Organization_Query.nextpage_xpath2).get_attribute(
                    'outerHTML')
                if (re.search('disabled="disabled"', next_button_str)):
                    break
                time.sleep(1)
                driver.find_element_by_xpath(Organization_Query.nextpage_xpath).click()
                i = 1
                # try:
                #     self.driver.implicitly_wait(1)
                #     driver.find_element_by_xpath(Organization_Query.nextpage_xpath).click()
                #     self.driver.implicitly_wait(30)
                #     time.sleep(1)
                # except:
                #     self.driver.implicitly_wait(30)
                #     print(i)
                #     break
                # i = 1
            try:
                self.driver.implicitly_wait(1)
                timestr2 = driver.find_element_by_xpath(Organization_Query.data_xpath.format(i, 4)).text
                self.driver.implicitly_wait(30)
            except:
                self.driver.implicitly_wait(30)
                break
            print(timestr1, timestr2)
            if (timestr1 < timestr2):
                if (i == 1):
                    orgname1 = driver.find_element_by_xpath(Organization_Query.data_xpath.format(10, 2)).text
                else:
                    orgname1 = driver.find_element_by_xpath(Organization_Query.data_xpath.format(i - 1, 2)).text
                orgname2 = driver.find_element_by_xpath(Organization_Query.data_xpath.format(i, 2)).text
                raise AssertionError(
                    '\n组织名称：{} 的操作时间\"{}\"和组织名称：{} 的操作时间\"{}\"排序不对！'.format(orgname1, timestr1, orgname2, timestr2))
            i = i + 1

        driver.close()

    # 组织查询搜索框检查用例
    def test_Organization_Query_Seek(self):
        driver = self.driver
        # 点击菜单栏组织管理
        driver.find_element_by_xpath(Organization_Query.menubar_orgmanagement_xpath).click()
        time.sleep(1)
        i = 1
        all_organization_name = []
        # 遍历查到的组织，把所有组织名称放入all_organization_name列表
        while (i):
            all_organization_name.append(driver.find_element_by_xpath(Organization_Query.data_xpath2.format(i)).text)
            if (i == 10):
                try:
                    driver.find_element_by_xpath(Organization_Query.nextpage_xpath).click()
                    time.sleep(1)
                except:
                    break
                i = 0
            try:
                self.driver.implicitly_wait(1)
                timestr2 = driver.find_element_by_xpath(Organization_Query.data_xpath2.format(i + 1)).text
                self.driver.implicitly_wait(30)
            except:
                self.driver.implicitly_wait(30)
                break
            i = i + 1
        # print(all_organization_name)
        # print(len(all_organization_name))
        search_data = ['', '5', '组织', 'haus']  # 搜索框要输入的字段，分别对应：1.不输入字；2.输入一个字；3.输入多个字；4.输入不存在的字，这四个用例

        # 遍历搜索数据，把搜索数据填入搜索框，进行检查
        for sdata in search_data:
            driver.find_element_by_xpath(Organization_Query.search_input_xpath).clear()
            driver.find_element_by_xpath(Organization_Query.search_input_xpath).send_keys(sdata)
            driver.find_element_by_xpath(Organization_Query.search_button_xpath).click()

            # 遍历查到的组织，把所有组织名称放入some_organization_name列表
            i = 1
            some_organization_name = []
            time.sleep(1)
            while (i):
                try:
                    self.driver.implicitly_wait(1)
                    some_organization_name.append(
                        driver.find_element_by_xpath(Organization_Query.data_xpath2.format(i)).text)
                    self.driver.implicitly_wait(30)
                except:
                    self.driver.implicitly_wait(30)
                    break
                if (i == 10):
                    try:
                        time.sleep(1)
                        driver.find_element_by_xpath(Organization_Query.nextpage_xpath).click()
                        time.sleep(1)
                    except:
                        break
                    i = 0
                i = i + 1
            # 遍历所有组织名称，预计应该查到的数据，填入hope_organization_name列表
            hope_organization_name = []
            for adata in all_organization_name:
                if (re.search(sdata, adata)):
                    hope_organization_name.append(adata)

            # 比较some_organization_name和hope_organization_name，如有误，则测试不通过
            # print(some_organization_name)
            # print(hope_organization_name)
            if (some_organization_name != hope_organization_name):
                raise AssertionError(
                    '搜索功能不正确！应该搜索出的组织：{}；实际搜索出的组织：{}。'.format(hope_organization_name, some_organization_name))
        driver.close()

    # # 组织查询分页检查用例
    # def test_Organization_Query_Page(self):
    #     driver = self.driver
    #     # 滚动条拉到底部
    #     js = "var q=document.documentElement.scrollTop=10000"
    #     driver.execute_script(js)
    #     time.sleep(3)
    #     # 光标移动到<按键上
    #     above = driver.find_element_by_xpath(
    #         "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div/button[1]")
    #     ActionChains(driver).move_to_element(above).perform()
    #     time.sleep(3)
    #     driver.find_element_by_xpath(
    #         "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div/button[1]").click()
    #     time.sleep(5)
    #     driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
    # print(1)
