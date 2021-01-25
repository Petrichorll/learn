# -*- coding: utf-8 -*-

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
import login, user_add, workxls
from selenium.webdriver.common.action_chains import ActionChains


# 用户查询
class User_Query(unittest.TestCase):

    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 用户查询用例
    def test_User_Query(self):
        driver = self.driver
        # 点击菜单栏用户管理
        driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div[1]/div/ul[1]/div[4]/a/li/span").click()
        print('6666666')
        time.sleep(1)
        count = count1 = 6
        # 新增x个用户,并记录到userdata.xls，以供检查
        while (count):
            if (count > 10):  # 限制10个
                count = 10
                count1 = 10
            # driver = user_add.User_Add.UserAdd(driver, 1)
            time.sleep(2)
            driver.find_element_by_xpath(
                "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div[1]/button").click()
            time.sleep(1)
            driver = user_add.User_Add.UserAdd(driver)
            time.sleep(1)
            count = count - 1

        time.sleep(10000)
        # 重新点击菜单栏角色管理，检查查询结果，和roledata.xls里的数据对比
        dataxpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[{}]/td[{}]/div"
        # "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div"
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[4]").click()
        time.sleep(1)
        i = 0
        while (i < count1):
            data1 = workxls.getimf('userdata.xls', i)
            data2 = driver.find_element_by_xpath(dataxpath.format(i + 1, 2)).text
            data3 = driver.find_element_by_xpath(dataxpath.format(i + 1, 3)).text
            data4 = driver.find_element_by_xpath(dataxpath.format(i + 1, 4)).text
            data5 = driver.find_element_by_xpath(dataxpath.format(i + 1, 5)).text
            data6 = driver.find_element_by_xpath(dataxpath.format(i + 1, 6)).text
            data7 = driver.find_element_by_xpath(dataxpath.format(i + 1, 7)).text
            data8 = driver.find_element_by_xpath(dataxpath.format(i + 1, 8)).text
            print(data1, data2, data3, data4, data5, data6, data7, data8)
            if (data1[0] != data2):
                raise AssertionError('网页的用户名称\"{}\"和本地记录里的用户名称\"{}\"不一致！'.format(data1[0], data2))
            if (data1[1] != data3):
                raise AssertionError('用户名：\"{}\"，网页的性别：\"{}\"和本地记录里的性别\"{}\"不一致！'.format(data1[0], data1[1], data3))
            if (data1[2] != data4):
                raise AssertionError('用户名：\"{}\"，网页的组织名称\"{}\"和本地记录里的组织名称\"{}\"不一致！'.format(data1[0], data1[2], data4))
            if (data1[3] != data5):
                raise AssertionError('用户名：\"{}\"，网页的角色名称\"{}\"和本地记录里的角色名称\"{}\"不一致！'.format(data1[0], data1[3], data5))
            if (data1[4] != data6):
                raise AssertionError('用户名：\"{}\"，网页的手机号\"{}\"和本地记录里的手机号\"{}\"不一致！'.format(data1[0], data1[4], data6))
            if (data1[5] != data7):
                raise AssertionError('用户名：\"{}\"，网页的邮箱\"{}\"和本地记录里的邮箱\"{}\"不一致！'.format(data1[0], data1[5], data7))
            if (data1[6][:-1] != data8[:-1]):
                raise AssertionError('用户名：\"{}\"，网页的操作时间\"{}\"和本地记录里的新增时间\"{}\"不一致！'.format(data1[0], data1[6], data8))
            i = i + 1
        driver.close()

    # 用户查询排序检查用例
    def test_User_Query_Sort(self):
        driver = self.driver
        # 点击菜单栏用户管理
        driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[4]").click()
        time.sleep(1)
        dataxpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[{}]/td[{}]/div"
        # 下一页箭头的xpath
        nextpagexpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div[3]/div/button[2]/i"
        time.sleep(1)
        i = 2
        while (i):
            timestr1 = driver.find_element_by_xpath(dataxpath.format(i - 1, 8)).text
            if (i == 11):
                try:
                    driver.find_element_by_xpath(nextpagexpath).click()
                    time.sleep(1)
                except:
                    break
                i = 1
            try:
                self.driver.implicitly_wait(1)
                timestr2 = driver.find_element_by_xpath(dataxpath.format(i, 8)).text
                self.driver.implicitly_wait(30)
            except:
                self.driver.implicitly_wait(30)
                break
            print(timestr1, timestr2)
            if (timestr1 < timestr2):
                if(i==1):
                    orgname1 = driver.find_element_by_xpath(dataxpath.format(10, 2)).text
                else:
                    orgname1 = driver.find_element_by_xpath(dataxpath.format(i - 1, 2)).text
                orgname2 = driver.find_element_by_xpath(dataxpath.format(i, 2)).text
                raise AssertionError(
                    '用户名称：{} 的操作时间\"{}\"和用户名称：{} 的操作时间\"{}\"排序不对！'.format(orgname1, timestr1, orgname2, timestr2))
            i = i + 1

        driver.close()

    # 角色查询搜索框检查用例
    def test_Role_Query_Seek(self):
        driver = self.driver
        # 点击菜单栏用户管理
        driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[4]").click()
        time.sleep(1)
        dataxpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[{}]/td[{}]/div"
        nextpagexpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div[3]/div/button[2]/i"
        # "/html/body/div/div/div[2]/section/section/div/div/div[1]/div[3]/div/button[2]/i"
        searchinputxpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div[1]/div/div/input"
        searchbuttonxpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[2]/div[1]/div/div/span/span/i"
        time.sleep(1)
        i = 1
        all_userorgrole_name = []
        # 遍历查到的用户，把所有用户名称、组织名称和角色名称放入all_orgrole_name列表
        while (i):
            all_userorgrole_name.append(driver.find_element_by_xpath(dataxpath.format(i, 2)).text)
            all_userorgrole_name.append(driver.find_element_by_xpath(dataxpath.format(i, 4)).text)
            all_userorgrole_name.append(driver.find_element_by_xpath(dataxpath.format(i, 5)).text)
            if (i == 10):
                try:
                    driver.find_element_by_xpath(nextpagexpath).click()
                    time.sleep(1)
                except:
                    break
                i = 0
            try:
                self.driver.implicitly_wait(1)
                timestr2 = driver.find_element_by_xpath(dataxpath.format(i + 1, 2)).text
                self.driver.implicitly_wait(30)
            except:
                self.driver.implicitly_wait(30)
                break
            i = i + 1
        # print(all_orgrole_name)
        # print(len(all_orgrole_name))
        search_data = ['', '1', '组织', 'haus']  # 搜索框要输入的字段，分别对应：1.不输入字；2.输入一个字；3.输入多个字；4.输入不存在的字，这四个用例
        # 遍历搜索数据，把搜索数据填入搜索框，进行检查
        for sdata in search_data:
            driver.find_element_by_xpath(searchinputxpath).clear()
            driver.find_element_by_xpath(searchinputxpath).send_keys(sdata)
            driver.find_element_by_xpath(searchbuttonxpath).click()

            # 遍历查到的角色，把所有用户名称、角色名称和组织名称放入some_userorgrole_name列表
            i = 1
            some_userorgrole_name = []
            time.sleep(1)
            while (i):
                try:
                    self.driver.implicitly_wait(1)
                    some_userorgrole_name.append(driver.find_element_by_xpath(dataxpath.format(i, 2)).text)
                    some_userorgrole_name.append(driver.find_element_by_xpath(dataxpath.format(i, 4)).text)
                    some_userorgrole_name.append(driver.find_element_by_xpath(dataxpath.format(i, 5)).text)
                    self.driver.implicitly_wait(30)
                except:
                    self.driver.implicitly_wait(30)
                    break
                if (i == 10):
                    try:
                        time.sleep(1)
                        driver.find_element_by_xpath(nextpagexpath).click()
                        time.sleep(1)
                    except:
                        break
                    i = 0
                i = i + 1
            # 遍历所有用户名称，预计应该查到的数据，填入hope_userorgrole_name列表
            hope_userorgrole_name = []
            i = 0
            while (i < len(all_userorgrole_name)):
                if(re.search(sdata, all_userorgrole_name[i])):
                    if (i % 3 == 0):
                        hope_userorgrole_name.append(all_userorgrole_name[i])
                        hope_userorgrole_name.append(all_userorgrole_name[i + 1])
                        hope_userorgrole_name.append(all_userorgrole_name[i + 2])
                        i = i + 3
                        continue
                    if (i % 3 == 1):
                        hope_userorgrole_name.append(all_userorgrole_name[i - 1])
                        hope_userorgrole_name.append(all_userorgrole_name[i])
                        hope_userorgrole_name.append(all_userorgrole_name[i + 1])
                        i = i + 2
                        continue
                    if (i % 3 == 2):
                        hope_userorgrole_name.append(all_userorgrole_name[i - 2])
                        hope_userorgrole_name.append(all_userorgrole_name[i - 1])
                        hope_userorgrole_name.append(all_userorgrole_name[i])
                i = i + 1
            # 比较some_userorgrole_name和hope_userorgrole_name，如有误，则测试不通过
            print(some_userorgrole_name)
            print(hope_userorgrole_name)
            print(len(some_userorgrole_name))
            print(len(hope_userorgrole_name))
            if (some_userorgrole_name != hope_userorgrole_name):
                raise AssertionError(
                    '搜索功能不正确！应该搜索出的用户：{}；实际搜索出的用户：{}。'.format(hope_userorgrole_name, some_userorgrole_name))
        driver.close()

    # # 角色查询用例
    # def test_User_Query(self):
    #     driver = self.driver
    #     # 点击菜单栏用户管理
    #     driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[4]").click()
    #     time.sleep(1)
    #     # 新增n个用户，需要的时候才释放出来执行
    #     count = 5
    #     while (count):
    #         driver = user_add.User_Add.UserAdd(driver)
    #         time.sleep(1.5)
    #         count = count - 1
    #
    #
    #     driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
