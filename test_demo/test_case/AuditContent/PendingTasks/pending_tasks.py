# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import sys

sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")
sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\test_case\\AuditContent\\UploadFiles")
sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\test_case")
import login, user_add, workxls, upload_files, workorder
from selenium.webdriver.common.action_chains import ActionChains


# 机器审核结果查询
class Machine_Audit_Results(unittest.TestCase):
    audit_content_xpath = "//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul[1]/div[1]/li/div/span"  # 菜单栏-一级菜单-审核内容按钮的xpath
    audit_results_xpath = "//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul[1]/div[1]/li/ul/div[3]/a/li/span"  # 菜单栏-二级菜单-审核结果按钮的xpath
    dataxpath = "/html/body/div/div/div[2]/section/section/div/div/div/div[2]/div[1]/div/div[2]/div[3]/table/tbody/tr[{}]/td[{}]/div"  # 机审结果内容的xpath
    dataxpath2 = "/html/body/div/div/div[2]/section/section/div/div/div/div[2]/div[1]/div/div[2]/div[3]/table/tbody"  # 统计机审结果内容的xpath

    # "/html/body/div[1]/div/div[2]/section/section/div/div/div/div[3]/div[3]/table/tbody/tr[1]/td[2]/div"
    # # upload_file_xpath按钮在页面中是隐藏的
    # upload_xpath = "/html/body/div[1]/div/div[2]/section/section/div/div[1]/div/div/p[1]/button/span"  # 上传按钮的xpath，实际没作用，鼠标悬停查看效果
    # files_path = "C:/Users/19144/PycharmProjects/学习/test_demo/data/PendingDocuments/test1/"
    # tips_xpath = "/html/body/div[1]/div/div[2]/section/section/div/div[1]/div/div/p[2]"  # 上传文件页面内提示信息的xpath
    # page_sec_name_xpath = "/html/body/div[1]/div/div[2]/section/div/span/span[2]/span[1]/span"  # 页面二级名称的xpath

    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 机器审核结果查询用例
    def test_Machine_Audit_Results(self):
        driver = self.driver
        # 打开审核结果页面
        driver = Machine_Audit_Results.OpenAuditResults(driver)
        # 记录第一条工单的工单id
        befor_first_order_id = Machine_Audit_Results.GetOderID(driver, 1)
        print(befor_first_order_id)
        time.sleep(1)
        # 上传x张工单,并记录到orkorderdata.xls，以供检查
        count = count1 = 3
        if (count > 9):  # 限制9个
            count = count1 = 9
        while (count):
            time.sleep(1)
            driver = upload_files.Upload_Files.UploadFile(driver, 1)
            count = count - 1
        # 打开审核结果页面
        driver = Machine_Audit_Results.OpenAuditResults(driver)
        time.sleep(1)
        # 等待机器审核，可限定时间
        limtime = 60
        nowtime = time.time()
        checkI = 0
        while (nowtime + limtime > time.time()):
            driver.refresh()
            time.sleep(1)
            if (befor_first_order_id == "nothing"):
                htmlstr = driver.find_element_by_xpath(Machine_Audit_Results.dataxpath2).get_attribute('innerHTML')
                trlist = re.findall('<tr', htmlstr)
                if (count1 == len(trlist)):
                    checkI = 1
                    break  # 如果之前没有工单
            else:
                hope_order_id = Machine_Audit_Results.GetOderID(driver, count1 + 1)
                if (hope_order_id == befor_first_order_id):
                    checkI = 1
                    break
        if (checkI == 0):
            raise AssertionError("\n机器审核超时。。。。。。。。。。")
        time.sleep(1)
        # 分析对比机审结果,记录机审结果要素
        i = 0
        while (i < count1):
            data1 = workxls.getimf('workorderdata.xls', i)
            data2 = driver.find_element_by_xpath(Machine_Audit_Results.dataxpath.format(i + 1, 3)).text
            print(data1, data2)
            # 判断工单类型
            if (data1[1] != data2):
                raise AssertionError('\n网页的工单类型\"{}\"和本地记录里的工单类型\"{}\"不一致！'.format(data1[1], data2))
            # 填写工单机审要素
            data3 = driver.find_element_by_xpath(Machine_Audit_Results.dataxpath.format(i + 1, 1)).text  # 工单ID
            data4 = driver.find_element_by_xpath(Machine_Audit_Results.dataxpath.format(i + 1, 4)).text  # 工单机器审核结果
            data5 = driver.find_element_by_xpath(Machine_Audit_Results.dataxpath.format(i + 1, 5)).text  # 工单违规标签
            wod = workorder.WorkOrder(id=data3, machineauditresults=data4, illegallabel=data5)  # 组成工单对象
            workxls.additionaldata('workorderdata.xls', i + 1, wod)  # 填入表单
            i = i + 1

        time.sleep(1000)

        driver.close()

    @staticmethod
    def OpenAuditResults(driver):  # 打开审核结果页面
        time.sleep(1)
        # 点击菜单栏系统管理
        try:
            driver.implicitly_wait(1)
            driver.find_element_by_xpath(Machine_Audit_Results.audit_results_xpath).click()
            time.sleep(1)
        except:
            driver.find_element_by_xpath(Machine_Audit_Results.audit_content_xpath).click()
            time.sleep(1)
            # 点击菜单栏操作日志
            driver.find_element_by_xpath(Machine_Audit_Results.audit_results_xpath).click()
            time.sleep(1)
        finally:
            driver.implicitly_wait(30)

        return driver

    @staticmethod
    def GetOderID(driver, tr=1):  # 获取工单ID
        time.sleep(1)
        try:
            driver.implicitly_wait(1)
            order_id = driver.find_element_by_xpath(Machine_Audit_Results.dataxpath.format(tr, 1)).text
        except:
            order_id = "nothing"
        finally:
            driver.implicitly_wait(30)

        return order_id

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
