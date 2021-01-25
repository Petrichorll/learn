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
import login, role_add, workxls
from selenium.webdriver.common.action_chains import ActionChains


# 角色查询
class role_Query(unittest.TestCase):
    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 角色查询用例
    def test_Role_Query(self):
        driver = self.driver
        # 点击菜单栏角色管理
        driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[6]").click()
        time.sleep(1)
        count = count1 = 3
        # 新增x个角色,并记录到roledata.xls，以供检查
        # while (count):
        #     driver = role_add.Role_Add.RoleAdd(driver, 1)
        #     time.sleep(1)
        #     count = count - 1
        # 重新点击菜单栏角色管理，检查查询结果，和roledata.xls里的数据对比
        dataxpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[{}]/div"
        driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[6]").click()
        time.sleep(1)
        i = 0
        while (i < count1):
            data1 = workxls.getimf('roledata.xls', i)
            data2 = driver.find_element_by_xpath(dataxpath.format(i + 1, 2)).text
            data3 = driver.find_element_by_xpath(dataxpath.format(i + 1, 3)).text
            data4 = driver.find_element_by_xpath(dataxpath.format(i + 1, 4)).text
            print(data1, data2, data3, data4)

            if (data1[0] != data2):
                raise AssertionError('网页的角色名称\"{}\"和本地记录里的角色名称\"{}\"不一致！'.format(data1[0], data2))
            if (data1[1] != data3):
                raise AssertionError('网页的组织名称\"{}\"和本地记录里的组织名称\"{}\"不一致！'.format(data1[1], data3))
            if (data1[2][:-1] != data4[:-1]):
                raise AssertionError('角色名称：{}，网页的操作时间\"{}\"和本地记录里的新增时间\"{}\"不一致！'.format(data1[0], data1[2], data4))
            i = i + 1
        driver.close()

    # 角色查询排序检查用例
    def test_Role_Query_Sort(self):
        driver = self.driver
        # 点击菜单栏角色管理
        driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[6]").click()
        time.sleep(1)
        dataxpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[{}]/div"
        # 下一页箭头的xpath
        nextpagexpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div/button[2]/i"
        time.sleep(1)
        i = 2
        while (i):
            timestr1 = driver.find_element_by_xpath(dataxpath.format(i - 1, 4)).text
            if (i == 11):
                try:
                    driver.find_element_by_xpath(nextpagexpath).click()
                    time.sleep(1)
                except:
                    break
                i = 1
            try:
                self.driver.implicitly_wait(1)
                timestr2 = driver.find_element_by_xpath(dataxpath.format(i, 4)).text
                self.driver.implicitly_wait(30)
            except:
                self.driver.implicitly_wait(30)
                break
            print(timestr1, timestr2)
            if (timestr1 > timestr2):
                if(i==1):
                    orgname1 = driver.find_element_by_xpath(dataxpath.format(10, 2)).text
                else:
                    orgname1 = driver.find_element_by_xpath(dataxpath.format(i - 1, 2)).text
                orgname2 = driver.find_element_by_xpath(dataxpath.format(i, 2)).text
                raise AssertionError(
                    '角色名称：{} 的操作时间\"{}\"和角色名称：{} 的操作时间\"{}\"排序不对！'.format(orgname1, timestr1, orgname2, timestr2))
            i = i + 1

        driver.close()

    # 角色查询搜索框检查用例
    def test_Role_Query_Seek(self):
        driver = self.driver
        # 点击菜单栏角色管理
        driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[6]").click()
        time.sleep(1)
        dataxpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[2]/div[3]/table/tbody/tr[{}]/td[{}]/div"
        nextpagexpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div/button[2]/i"
        # "/html/body/div/div/div[2]/section/section/div/div/div[1]/div[3]/div/button[2]/i"
        searchinputxpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[1]/div/div/input"
        searchbuttonxpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[1]/div/div/span/span/i"
        time.sleep(1)
        i = 1
        all_orgrole_name = []
        # 遍历查到的角色，把所有角色名称和组织名称放入all_orgrole_name列表
        while (i):
            all_orgrole_name.append(driver.find_element_by_xpath(dataxpath.format(i, 2)).text)
            all_orgrole_name.append(driver.find_element_by_xpath(dataxpath.format(i, 3)).text)
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
        search_data = ['', '5', '组织', 'haus']  # 搜索框要输入的字段，分别对应：1.不输入字；2.输入一个字；3.输入多个字；4.输入不存在的字，这四个用例
        # 遍历搜索数据，把搜索数据填入搜索框，进行检查
        for sdata in search_data:
            driver.find_element_by_xpath(searchinputxpath).clear()
            driver.find_element_by_xpath(searchinputxpath).send_keys(sdata)
            driver.find_element_by_xpath(searchbuttonxpath).click()

            # 遍历查到的角色，把所有角色名称和组织名称放入some_orgrole_name列表
            i = 1
            some_orgrole_name = []
            time.sleep(1)
            while (i):
                try:
                    self.driver.implicitly_wait(1)
                    some_orgrole_name.append(driver.find_element_by_xpath(dataxpath.format(i, 2)).text)
                    some_orgrole_name.append(driver.find_element_by_xpath(dataxpath.format(i, 3)).text)
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
            # 遍历所有组织名称，预计应该查到的数据，填入hope_orgrole_name列表
            hope_orgrole_name = []
            i = 0
            while (i < len(all_orgrole_name)):
                if (re.search(sdata, all_orgrole_name[i]) and i % 2 == 0):
                    hope_orgrole_name.append(all_orgrole_name[i])
                    hope_orgrole_name.append(all_orgrole_name[i + 1])
                    i = i + 2
                    continue
                if (re.search(sdata, all_orgrole_name[i]) and i % 2 == 1):
                    hope_orgrole_name.append(all_orgrole_name[i - 1])
                    hope_orgrole_name.append(all_orgrole_name[i])
                i = i + 1
            # 比较some_orgrole_name和hope_orgrole_name，如有误，则测试不通过
            print(some_orgrole_name)
            print(hope_orgrole_name)
            if (some_orgrole_name != hope_orgrole_name):
                raise AssertionError(
                    '搜索功能不正确！应该搜索出的角色：{}；实际搜索出的角色：{}。'.format(hope_orgrole_name, some_orgrole_name))
        driver.close()

    # # 角色查询用例
    # def test_Role_Query(self):
    #     driver = self.driver
    #     # 点击菜单栏角色管理
    #     driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[6]").click()
    #     time.sleep(1)
    #     # 新增50个角色，需要的时候才释放出来执行
    #     count = 50
    #     while (count):
    #         driver = role_add.Role_Add.RoleAdd(driver)
    #         #time.sleep(1)
    #         count = count - 1
    #
    #     # time.sleep(3)  # 预留时间查看元素
    #     # # 滚动条拉到底部
    #     # js = "var q=document.documentElement.scrollTop=10000"
    #     # driver.execute_script(js)
    #     # time.sleep(3)
    #     # # 光标移动到<按键上
    #     # above = driver.find_element_by_xpath(
    #     #     "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div/button[1]")
    #     # ActionChains(driver).move_to_element(above).perform()
    #     # time.sleep(3)
    #     # driver.find_element_by_xpath(
    #     #     "//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[3]/div/button[1]").click()
    #     #
    #     # time.sleep(5)
    #     driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
