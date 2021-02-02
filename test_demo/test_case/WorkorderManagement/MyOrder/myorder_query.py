# -*- coding: utf-8 -*-
# 我的工单-查询

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
sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\test_case\\AuditContent\\FindingsAudit")
sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\test_case\\WorkorderManagement\\WorkorderQuery")
import login, user_add, workxls, upload_files, workorder, machine_audit_results, workxlsx, receive_order
from selenium.webdriver.common.action_chains import ActionChains


# 我的工单-查询
class MyOrder_Query(unittest.TestCase):
    workorder_management_xpath = "/html/body/div/div/div[1]/div[2]/div[1]/div/ul[1]/div[2]/li/div/span"  # 菜单栏-一级菜单-工单管理按钮的xpath
    myorder_xpath = "/html/body/div/div/div[1]/div[2]/div[1]/div/ul[1]/div[2]/li/ul/div[2]/a/li/span"  # 菜单栏-二级菜单-我的工单按钮的xpath
    dataxpath = "/html/body/div/div/div[2]/section/section/div/div/div/div/div[3]/div[3]/table/tbody/tr[{}]/td[{}]/div"  # 我的工单内容的xpath

    # order_details_xpath = "/html/body/div/div/div[2]/section/section/div/div/div/div/div[3]/div[4]/div[2]/table/tbody/tr[{}]/td[11]/div/a/span"  # 详情按钮的xpath
    nextpage_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div/div[4]/div/button[2]"  # 下一页按钮的xpath

    # details_orderid_xpath = "/html/body/div/div/div[2]/section/section/div/div/div[1]/div[1]/div[1]/div[1]/span[2]"  # 详情页工单ID的xpath
    # details_auditlog_xpath = "/html/body/div/div/div[2]/section/section/div/div/div[1]/div[1]/div[1]/div[2]/div/p[1]/span[{}]"  # 详情页审核日志xpath
    # details_back_xpath = "/html/body/div/div/div[2]/section/section/div/div/div[1]/div[1]/div[2]/button"  # 详情页面的返回按钮

    ordetype_sdp_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div/div[3]/div[2]/table/thead/tr/th[{}]/div/div/i"  # 筛选列下拉框
    option_xpath = "/html/body/ul[{}]/li[{}]"

    search_input_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div/div[1]/div/div/input"
    search_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div/div[1]/div/div/span/span/i"

    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 我的工单-查询用例
    def test_MyOrder_Query(self):
        driver = self.driver
        # 打开我的工单页面
        driver = MyOrder_Query.OpenMyOrderQuery(driver)
        # 记录第一条工单的工单id
        befor_first_order_id = MyOrder_Query.GetOderID(driver, 1)
        print(befor_first_order_id)
        time.sleep(1)
        # 上传3张工单,并记录到orkorderdata.xls
        count = 3
        driver = machine_audit_results.Machine_Audit_Results.UploadOrederAndWrite(driver, count)
        # 到工单查询页面，领取这3张工单。
        driver = receive_order.Receive_Work_Order.ReceiveOrders(driver, count)
        # 重新打开我的工单页面
        driver = MyOrder_Query.OpenMyOrderQuery(driver)
        # 读取orkorderdata.xls的数据，和页面查询的比对
        i = 1
        while (i <= count):
            data2 = []
            data1 = workxls.getimf('workorderdata.xls', count - i)
            print(data1)
            time.sleep(0.2)
            data2.append(driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i, 2)).text)  # 工单ID
            data2.append(driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i, 4)).text)  # 工单类型
            data2.append(driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i, 5)).text)  # 工单来源
            data2.append(driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i, 6)).text)  # 当前负责人
            data2.append(driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i, 7)).text)  # 工单状态
            data2.append(driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i, 8)).text)  # AI审核结果
            data2.append(driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i, 9)).text)  # 人工审核结果
            data2.append(driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i, 10)).text)  # 操作时间
            if (data2[0] != data1[3]):
                raise AssertionError('\n工单查询的工单ID\"{}\"和本地excle记录里的工单ID\"{}\"不一致！'.format(data2[0], data1[3]))
            if (data2[1] != data1[1]):
                raise AssertionError('\n工单查询的工单类型\"{}\"和本地excle记录里的工单类型\"{}\"不一致！'.format(data2[0], data1[1]))
            if (data2[2] != data1[9]):
                raise AssertionError('\n工单查询的工单来源\"{}\"和本地excle记录里的工单来源\"{}\"不一致！'.format(data2[2], data1[9]))
            if (data2[3] != data1[7]):
                raise AssertionError('\n工单查询的工单当前负责人\"{}\"和本地excle记录里的工单当前负责人\"{}\"不一致！'.format(data2[3], data1[7]))
            if (data2[4] != data1[8]):
                raise AssertionError('\n工单查询的工单状态\"{}\"和本地excle记录里的工单状态\"{}\"不一致！'.format(data2[4], data1[8]))
            if (data2[5] != data1[4]):
                raise AssertionError('\n工单查询的工单机审结果\"{}\"和本地excle记录里的工单机审结果\"{}\"不一致！'.format(data2[5], data1[4]))
            if (data2[6] != data1[5]):
                raise AssertionError('\n工单查询的工单人审结果\"{}\"和本地excle记录里的工单人审结果\"{}\"不一致！'.format(data2[6], data1[5]))
            if (data2[7] != data1[2]):  # 检查操作时间，秒数相差忽略
                if (abs(int(data2[7][-1]) - int(data1[2][-1])) < 3):
                    if (int(data2[7][-1]) != 9 and int(data1[2][-1]) != 9):
                        raise AssertionError('\n工单查询的操作时间\"{}\"和本地excle记录里的操作时间\"{}\"不一致！'.format(data2[7], data1[2]))
            # 更新一下操作时间
            workxls.changetime('workorderdata.xls', count - i + 1, data2[7])
            i = i + 1
            # print(data1, "\n", data2)
        # 检查一下本次上传的个数
        # driver = Work_Order_Query.CheckOrderConut(driver, befor_first_order_id, i)
        time.sleep(1)

        driver.close()

    # 工单详情查看用例
    def test_Work_Order_Details(self):
        driver = self.driver
        # 打开工单查询页面
        driver = Work_Order_Query.OpenOrderQuery(driver)
        # 记录第一条工单的工单id
        befor_first_order_id = Work_Order_Query.GetOderID(driver, 1)
        print(befor_first_order_id)
        time.sleep(1)
        # 上传3张工单,并记录到orkorderdata.xls
        count = 3
        # driver = machine_audit_results.Machine_Audit_Results.UploadOrederAndWrite(driver, count)
        # 打开工单查询页面
        driver = Work_Order_Query.OpenOrderQuery(driver)
        # 读取orkorderdata.xls的数据，和页面查询的比对
        i = 1
        while (i <= count):
            data2 = []
            data1 = workxls.getimf('workorderdata.xls', i - 1)
            # 点击详情按钮
            driver.find_element_by_xpath(Work_Order_Query.order_details_xpath.format(i)).click()
            time.sleep(1)  # 等待加载数据
            data2.append(driver.find_element_by_xpath(Work_Order_Query.details_orderid_xpath).text)
            data2.append(driver.find_element_by_xpath(Work_Order_Query.details_auditlog_xpath.format(1)).text)
            data2.append(driver.find_element_by_xpath(Work_Order_Query.details_auditlog_xpath.format(2)).text)
            data2.append(driver.find_element_by_xpath(Work_Order_Query.details_auditlog_xpath.format(3)).text)
            if (data2[0] != data1[3]):
                raise AssertionError('\n工单查询的工单ID\"{}\"和本地excle记录里的工单ID\"{}\"不一致！'.format(data2[0], data1[3]))
            if (data2[1] != data1[2]):  # 检查操作时间，秒数相差忽略
                if (abs(int(data2[5][-1]) - int(data1[2][-1])) < 3):
                    if (int(data2[5][-1]) != 9 and int(data1[2][-1]) != 9):
                        raise AssertionError('\n工单查询的操作时间\"{}\"和本地excle记录里的操作时间\"{}\"不一致！'.format(data2[5], data1[2]))
            if (data2[2] != data1[4]):
                raise AssertionError('\n工单查询的工单机审结果\"{}\"和本地excle记录里的工单机审结果\"{}\"不一致！'.format(data2[2], data1[4]))
            if (data2[3] != "AI审核"):
                raise AssertionError('\n工单查询的工单日志不是AI审核!')
            i = i + 1
            print(data1, "\n", data2)
            # 点击返回按钮
            driver.find_element_by_xpath(Work_Order_Query.details_back_xpath).click()
            time.sleep(1)

        # order_id = driver.find_element_by_xpath(Work_Order_Query.dataxpath.format(i, 2)).text
        # if (befor_first_order_id == "nothing"):
        #     pass
        # elif (befor_first_order_id != order_id):
        #     raise AssertionError('\n工单查询的工单个数不正确')
        # else:
        #     raise AssertionError('\n工单查询的工单个数不正确')

        time.sleep(1000)

        driver.close()

    # 我的工单-查询排序检查用例
    def test_Work_Order_Query_Sort(self):
        driver = self.driver
        # 打开我的工单页面
        driver = MyOrder_Query.OpenMyOrderQuery(driver)
        time.sleep(1)
        i = 2
        while (i):
            timestr1 = driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i - 1, 10)).text
            if (i == 11):
                next_button_str = driver.find_element_by_xpath(MyOrder_Query.nextpage_xpath).get_attribute(
                    'outerHTML')
                if (re.search('disabled="disabled"', next_button_str)):
                    break
                driver.find_element_by_xpath(MyOrder_Query.nextpage_xpath).click()
                time.sleep(1)
                i = 1
            try:
                self.driver.implicitly_wait(1)
                timestr2 = driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i, 10)).text
                self.driver.implicitly_wait(30)
            except:
                self.driver.implicitly_wait(30)
                break
            print(timestr1, timestr2)
            if (timestr1 < timestr2):
                if (i == 1):
                    orderID1 = driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(10, 2)).text
                else:
                    orderID1 = driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i - 1, 2)).text
                orderID2 = driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i, 2)).text
                raise AssertionError(
                    '\n工单ID：{} 的操作时间\"{}\"和工单ID：{} 的操作时间\"{}\"排序不对！'.format(orderID1, timestr1, orderID2, timestr2))
            i = i + 1

        driver.close()

    # 我的工单查询搜索框检查用例
    def test_Work_Order_Query_Seek(self):
        driver = self.driver
        # 打开我的工单页面
        driver = MyOrder_Query.OpenMyOrderQuery(driver)
        time.sleep(1)
        # 遍历工单查询列表，把查到的工单ID、工单类型、文件来源、工单状态、AI审核结果、人工审核结果填入screen_elements_list
        screen_elements_list = MyOrder_Query.TraverseList(driver)
        search_data = ['', '3', '52', 'haus']  # 搜索框要输入的字段，分别对应：1.不输入字；2.输入一个字；3.输入多个字；4.输入不存在的字，这四个用例

        # 遍历搜索数据，把搜索数据填入搜索框，进行检查
        for sdata in search_data:
            driver.find_element_by_xpath(MyOrder_Query.search_input_xpath).clear()
            driver.find_element_by_xpath(MyOrder_Query.search_input_xpath).send_keys(sdata)
            driver.find_element_by_xpath(MyOrder_Query.search_button_xpath).click()

            # 遍历工单查询列表，把查到的工单ID、工单类型、文件来源、工单状态、AI审核结果、人工审核结果填入screen_elements_list
            time.sleep(1)
            seeked_elements_list = MyOrder_Query.TraverseList(driver)
            # 遍历所有screen_elements_list元素，预计应该查到的数据，填入hope_elements_list列表
            hope_elements_list = []
            for adata in screen_elements_list:
                if (re.search(sdata, adata[0])):
                    hope_elements_list.append(adata)

            # 比较seeked_elements_list和hope_elements_list，如有误，则测试不通过
            print(seeked_elements_list)
            print(hope_elements_list)
            if (seeked_elements_list != hope_elements_list):
                raise AssertionError(
                    '\n搜索功能不正确！\n应该搜索出的工单信息：{}。\n实际搜索出的工单信息：{}。'.format(hope_elements_list, seeked_elements_list))
        driver.close()

    # 工单筛选用例
    def test_Work_Order_Screen(self):
        driver = self.driver
        # 打开工单查询页面
        driver = MyOrder_Query.OpenMyOrderQuery(driver)
        # 清空workorderquery.xlsx文件，以便填入。
        workxlsx.cleandata("workorderquery.xlsx")
        # 遍历工单查询列表，把查到的工单ID、工单类型、文件来源、工单状态、AI审核结果、人工审核结果填入workorderquery.xlsx文件
        screen_elements_list = MyOrder_Query.TraverseList(driver)
        workxlsx.writedata("workorderquery.xlsx", screen_elements_list)
        # 点击工单类型过滤菜单，筛选文本，并在查询后比较
        driver = MyOrder_Query.ScreenAndComparOrder(driver, "文本")
        # 点击工单类型过滤菜单，筛选视频，默认...并在查询后比较
        driver = MyOrder_Query.ScreenAndComparOrder(driver, "视频", "默认", "AI通过")
        # 点击工单类型过滤菜单，筛选条件为参数，并在查询后比较
        driver = MyOrder_Query.ScreenAndComparOrder(driver, "视频", "默认", "AI不通过")
        # 点击工单类型过滤菜单，筛选条件为参数，并在查询后比较
        driver = MyOrder_Query.ScreenAndComparOrder(driver, "mht")
        # 点击工单类型过滤菜单，筛选条件为参数，并在查询后比较
        driver = MyOrder_Query.ScreenAndComparOrder(driver, "mht", "AI不通过")
        # 点击工单类型过滤菜单，筛选条件为参数，并在查询后比较
        driver = MyOrder_Query.ScreenAndComparOrder(driver, "二级审核中")
        # 点击工单类型过滤菜单，筛选条件为参数，并在查询后比较
        driver = MyOrder_Query.ScreenAndComparOrder(driver, "通过")
        # 点击工单类型过滤菜单，筛选条件为参数，并在查询后比较
        driver = MyOrder_Query.ScreenAndComparOrder(driver, "一级审核中", "通过")
        # 点击工单类型过滤菜单，筛选条件为参数，并在查询后比较
        driver = MyOrder_Query.ScreenAndComparOrder(driver, "二级审核中", "通过")
        # 点击工单类型过滤菜单，筛选条件为参数，并在查询后比较
        driver = MyOrder_Query.ScreenAndComparOrder(driver, "二级审核中", "不通过")
        # 点击工单类型过滤菜单，筛选条件为参数，并在查询后比较
        driver = MyOrder_Query.ScreenAndComparOrder(driver, "通过")
        # 点击工单类型过滤菜单，筛选条件为参数，并在查询后比较
        driver = MyOrder_Query.ScreenAndComparOrder(driver, "图片", "mht", "一级审核中", "AI不通过")
        # 点击工单类型过滤菜单，筛选条件为参数，并在查询后比较
        driver = MyOrder_Query.ScreenAndComparOrder(driver, "图片")
        # 点击工单类型过滤菜单，筛选条件为参数，并在查询后比较
        driver = MyOrder_Query.ScreenAndComparOrder(driver, "图片", "mht")
        # 点击工单类型过滤菜单，筛选条件为参数，并在查询后比较
        driver = MyOrder_Query.ScreenAndComparOrder(driver, "图片", "mht", "二级审核中", "AI不通过")
        # 点击工单类型过滤菜单，筛选条件为参数，并在查询后比较
        driver = MyOrder_Query.ScreenAndComparOrder(driver, "图片", "mht", "二级审核中", "AI通过", "通过")

        time.sleep(1000)
        driver.close()

    @staticmethod
    def ScreenAndComparOrder(driver, *args):  # 筛选和对比工单
        driver = MyOrder_Query.OpenMyOrderQuery(driver)  # 重新打开工单查询界面
        time.sleep(0.5)
        i = 0
        for conditionstr in args:
            i = i + 1
            if (conditionstr == "图片"):
                driver = MyOrder_Query.ClickFilterWP(driver, 4, i, 2)
            elif (conditionstr == "文本"):
                driver = MyOrder_Query.ClickFilterWP(driver, 4, i, 3)
            elif (conditionstr == "视频"):
                driver = MyOrder_Query.ClickFilterWP(driver, 4, i, 4)
            elif (conditionstr == "默认"):
                driver = MyOrder_Query.ClickFilterWP(driver, 5, i, 2)
            elif (conditionstr == "mht"):
                driver = MyOrder_Query.ClickFilterWP(driver, 5, i, 3)
            elif (conditionstr == "一级审核中"):
                driver = MyOrder_Query.ClickFilterWP(driver, 7, i, 2)
            elif (conditionstr == "二级审核中"):
                driver = MyOrder_Query.ClickFilterWP(driver, 7, i, 3)
            elif (conditionstr == "AI通过"):
                driver = MyOrder_Query.ClickFilterWP(driver, 8, i, 2)
            elif (conditionstr == "AI不通过"):
                driver = MyOrder_Query.ClickFilterWP(driver, 8, i, 3)
            elif (conditionstr == "通过"):
                driver = MyOrder_Query.ClickFilterWP(driver, 9, i, 2)
            elif (conditionstr == "不通过"):
                driver = MyOrder_Query.ClickFilterWP(driver, 9, i, 3)
            else:
                pass
        screen_elements_list = MyOrder_Query.TraverseList(driver)
        # 取保存的数据，筛选，比对
        se_list = workxlsx.ScreenData1("workorderquery.xlsx", *args)
        print("筛选条件为:{}\n网页结果为：{}\n实际结果为：{}".format(args, screen_elements_list, se_list))
        print("结果个数：{}\n\n\n".format(len(se_list)))
        if (se_list != screen_elements_list):
            raise AssertionError('\n筛选条件为:{}，筛选结果错误!\n网页结果为：{}\n实际结果为：{}'.format(args, screen_elements_list, se_list))
        return driver

    @staticmethod
    def ClickFilterWP(driver, k, i, j):  # 点击筛选网页
        time.sleep(0.5)
        driver.find_element_by_xpath(MyOrder_Query.ordetype_sdp_xpath.format(k)).click()
        time.sleep(0.4)
        driver.find_element_by_xpath(MyOrder_Query.option_xpath.format(i, j)).click()
        time.sleep(0.8)
        return driver

    @staticmethod
    def OpenMyOrderQuery(driver):  # 打开工单查询页面
        time.sleep(1)
        # 点击菜单栏工单查询
        try:
            driver.implicitly_wait(1)
            driver.find_element_by_xpath(MyOrder_Query.myorder_xpath).click()
            time.sleep(1)
        except:
            driver.find_element_by_xpath(MyOrder_Query.workorder_management_xpath).click()
            time.sleep(1)
            driver.find_element_by_xpath(MyOrder_Query.myorder_xpath).click()
            time.sleep(1)
        finally:
            driver.implicitly_wait(30)
        return driver

    @staticmethod
    def GetOderID(driver, tr=1):  # 获取工单ID
        time.sleep(1)
        try:
            driver.implicitly_wait(1)
            order_id = driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(tr, 2)).text
        except:
            order_id = "nothing"
        finally:
            driver.implicitly_wait(30)

        return order_id

    @staticmethod
    def TraverseList(driver):  # 遍历列表，返回查到元素的一个二维数组,personincharge参数表示是否把负责人这一列加入返回列表
        time.sleep(1)
        ret_list = []
        i = 1
        while (i):
            one_row_list = []
            try:
                driver.implicitly_wait(1)
                one_row_list.append(driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i, 2)).text)
                one_row_list.append(driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i, 4)).text)
                one_row_list.append(driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i, 5)).text)
                one_row_list.append(driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i, 7)).text)
                one_row_list.append(driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i, 8)).text)
                one_row_list.append(driver.find_element_by_xpath(MyOrder_Query.dataxpath.format(i, 9)).text)
                driver.implicitly_wait(30)
            except:
                driver.implicitly_wait(30)
                break
            ret_list.append(one_row_list)
            if (i == 10):
                hstr = driver.find_element_by_xpath(MyOrder_Query.nextpage_xpath).get_attribute('outerHTML')
                if (re.findall("disabled", hstr)):
                    break
                driver.find_element_by_xpath(MyOrder_Query.nextpage_xpath).click()
                time.sleep(1)
                i = 0
            i = i + 1
        return ret_list

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
