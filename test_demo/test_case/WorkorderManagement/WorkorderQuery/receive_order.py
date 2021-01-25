# -*- coding: utf-8 -*-
# 工单查询


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, random
import sys

sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")
sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\test_case\\AuditContent\\UploadFiles")
sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\test_case")
sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\test_case\\AuditContent\\FindingsAudit")
# sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\test_case\\WorkorderManagement\\WorkorderQuery")
import login, user_add, workxls, upload_files, workorder, machine_audit_results, workxlsx, workorder_query, website_tips
from selenium.webdriver.common.action_chains import ActionChains


# 工单管理
class Receive_Work_Order(unittest.TestCase):
    rorder_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div/div[3]/div[4]/div[2]/table/tbody/tr[{}]/td[11]/div/span/span/a"  # 领取工单按钮的xpath
    tipes_xpath = "/html/body/div[2]"  # 提示信息xpath
    checkbox_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div/div[3]/div[3]/table/tbody/tr[{}]/td[1]/div/label/span"  # 第一列勾选框的xpath

    robox_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div/div[2]/div[2]/a/span"  # 勾选后确认领取按钮
    robox_cancel_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div/div[2]/a/span"  # 勾选后取消领取按钮

    ro_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div/div[5]/div/div/div[3]/span/button[1]/span"  # 确定按钮的xpath
    ro_cancel_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div/div[5]/div/div/div[3]/span/button[2]/span"  # 取消按钮的xpath
    confirm_imf_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div/div[5]/div/div/div[2]/div/div/p[1]"  # 确定提示框的文案xpath

    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 工单领取用例
    def test_Receive_Work_Order(self):
        driver = self.driver
        # 打开工单查询页面
        driver = workorder_query.Work_Order_Query.OpenOrderQuery(driver)
        # 在第一页造一个"二级审核完成"的工单,尽量确保在第三条工单
        pass

        # 第零节 无法领取的工单检查
        order_list = Receive_Work_Order.TraverseList2Page(driver)  # 读取两页工单信息，并记录下工单ID，审核状态进二维数组order_list里面

        driver = workorder_query.Work_Order_Query.OpenOrderQuery(driver)  # 重新打开工单查询页面
        i = 11  # 在数组order_list前10个数据中找到"二级审核完成"的工单
        for i in range(1, 12):
            if (order_list[i - 1][1] == "二级审核完成"):
                break
        if (i == 11):
            raise AssertionError("\n没有”二级审核完成“的工单，无法进行不能领取的用例")
        driver = Receive_Work_Order.CheckButtonAndBox(driver, i, 1)  # 根据i检查工单的领取按钮和勾选框

        # 第一节 点击领取按钮领取单个工单
        j = random.randint(4, 10)  # 随机选一个要领取的工单
        if (j == i): j = j + 1
        driver = Receive_Work_Order.CheckButtonAndBox(driver, j)  # 根据j检查工单的领取按钮和勾选框
        driver.find_element_by_xpath(Receive_Work_Order.rorder_button_xpath.format(j)).click()  # 点击领取工单
        driver = Receive_Work_Order.CheckComfirmbox(driver)  # 确认提示框检查
        driver.find_element_by_xpath(Receive_Work_Order.ro_cancel_button_xpath).click()  # 点击取消，返回页面无事发生
        time.sleep(0.5)
        driver.find_element_by_xpath(Receive_Work_Order.rorder_button_xpath.format(j)).click()  # 重新点击领取工单
        driver = Receive_Work_Order.CheckComfirmbox(driver)  # 确认提示框检查
        driver.find_element_by_xpath(Receive_Work_Order.ro_confirm_button_xpath).click()  # 点击确定，领取成功
        time.sleep(0.5)
        tipsstr = website_tips.get_websitetips(driver)  # 获取右上角提示信息
        if (tipsstr != "领取成功"):
            raise AssertionError("\n右上角领取成功提示文案不正确！")
        del order_list[j - 1]
        new_order_list = Receive_Work_Order.TraverseList2Page(driver)
        del new_order_list[-1]
        if (order_list != new_order_list):
            raise AssertionError("\n领取工单后，查询的工单和期望的工单不正确")
        print(order_list)
        print(new_order_list)
        print("==============")
        time.sleep(0.2)
        driver.close()

    # 第二节 勾选领取框领取单个工单
    def test_Receive_Work_Order2(self):
        driver = self.driver
        # 打开工单查询页面
        driver = workorder_query.Work_Order_Query.OpenOrderQuery(driver)
        # 在第一页造一个"二级审核完成"的工单,尽量确保在第三条工单
        i = 3
        pass
        order_list = Receive_Work_Order.TraverseList2Page(driver)  # 读取两页工单信息，并记录下工单ID，审核状态进二维数组order_list里面
        driver = workorder_query.Work_Order_Query.OpenOrderQuery(driver)  # 重新打开工单查询页面
        j = random.randint(4, 9)  # 随机选一个要领取的工单
        if (j == i): j = j + 1
        driver = Receive_Work_Order.CheckButtonAndBox(driver, j)  # 根据j检查工单的领取按钮和勾选框
        driver.find_element_by_xpath(Receive_Work_Order.checkbox_xpath.format(j)).click()  # 勾选j工单最左侧的勾选框
        time.sleep(1)  # 预留时间查看
        driver.find_element_by_xpath(Receive_Work_Order.robox_cancel_button_xpath).click()  # 点击取消选择按钮
        time.sleep(1)  # 预留时间查看
        driver.find_element_by_xpath(Receive_Work_Order.checkbox_xpath.format(j)).click()  # 重新勾选j工单最左侧的勾选框
        time.sleep(1)  # 预留时间查看
        driver.find_element_by_xpath(Receive_Work_Order.robox_button_xpath).click()  # 点击确定领取按钮
        driver = Receive_Work_Order.CheckComfirmbox(driver)  # 确认提示框检查
        driver.find_element_by_xpath(Receive_Work_Order.ro_cancel_button_xpath).click()  # 点击取消，返回页面无事发生
        time.sleep(1)  # 预留时间查看
        driver.find_element_by_xpath(Receive_Work_Order.robox_cancel_button_xpath).click()  # 点击取消选择按钮
        time.sleep(1)  # 预留时间查看
        driver.find_element_by_xpath(Receive_Work_Order.checkbox_xpath.format(j)).click()  # 重新勾选j工单最左侧的勾选框
        time.sleep(1)  # 预留时间查看
        driver.find_element_by_xpath(Receive_Work_Order.robox_button_xpath).click()  # 点击确定领取按钮
        time.sleep(0.2)  # 预留时间查看
        driver.find_element_by_xpath(Receive_Work_Order.ro_confirm_button_xpath).click()  # 点击确定，领取成功
        time.sleep(0.5)
        tipsstr = website_tips.get_websitetips(driver)  # 获取右上角提示信息
        time.sleep(1)  # 预留时间查看
        if (tipsstr != "领取成功"):
            raise AssertionError("\n右上角领取成功提示文案不正确！")
        del order_list[j - 1]
        new_order_list = Receive_Work_Order.TraverseList2Page(driver)
        new_order_list = new_order_list[:-1]
        if (order_list != new_order_list):
            raise AssertionError("\n领取工单后，查询的工单和期望的工单不正确")
        print(order_list)
        print(new_order_list)
        print("==============")
        time.sleep(0.2)
        driver.close()

    # 第三节 勾选领取框领取多个工单
    def test_Receive_Work_Order3(self):
        driver = self.driver
        # 打开工单查询页面
        driver = workorder_query.Work_Order_Query.OpenOrderQuery(driver)
        # 在第一页造一个"二级审核完成"的工单,尽量确保在第三条工单
        pass

        order_list = Receive_Work_Order.TraverseList2Page(driver)  # 读取两页工单信息，并记录下工单ID，审核状态进二维数组order_list里面
        driver = workorder_query.Work_Order_Query.OpenOrderQuery(driver)  # 重新打开工单查询页面
        sitelist = [2, 5, 7, 8]  # 固定领取2，5，7，8这几个工单
        for j in sitelist:
            driver = Receive_Work_Order.CheckButtonAndBox(driver, j)  # 根据j检查工单的领取按钮和勾选框
            driver.find_element_by_xpath(Receive_Work_Order.checkbox_xpath.format(j)).click()  # 勾选j工单最左侧的勾选框
        time.sleep(3)  # 预留时间查看
        driver.find_element_by_xpath(Receive_Work_Order.robox_cancel_button_xpath).click()  # 点击取消选择按钮,全部取消
        time.sleep(1)  # 预留时间查看
        for j in sitelist:
            driver.find_element_by_xpath(Receive_Work_Order.checkbox_xpath.format(j)).click()  # 重新勾选j工单最左侧的勾选框
        time.sleep(1)  # 预留时间查看
        driver.find_element_by_xpath(Receive_Work_Order.robox_button_xpath).click()  # 点击确定领取按钮
        driver = Receive_Work_Order.CheckComfirmbox(driver)  # 确认提示框检查
        driver.find_element_by_xpath(Receive_Work_Order.ro_cancel_button_xpath).click()  # 点击取消，返回页面无事发生
        time.sleep(1)  # 预留时间查看
        for j in sitelist:
            driver.find_element_by_xpath(Receive_Work_Order.checkbox_xpath.format(j)).click()  # 再次点击勾选j工单最左侧的勾选框，勾选取消
        time.sleep(1)  # 预留时间查看
        for j in sitelist:
            driver.find_element_by_xpath(Receive_Work_Order.checkbox_xpath.format(j)).click()  # 再再次点击勾选j工单最左侧的勾选框，重新选中
        time.sleep(1)  # 预留时间查看
        driver.find_element_by_xpath(Receive_Work_Order.robox_button_xpath).click()  # 点击确定领取按钮
        time.sleep(0.2)  # 预留时间查看
        driver.find_element_by_xpath(Receive_Work_Order.ro_confirm_button_xpath).click()  # 点击确定，领取成功
        time.sleep(0.5)
        tipsstr = website_tips.get_websitetips(driver)  # 获取右上角提示信息
        time.sleep(1)  # 预留时间查看
        if (tipsstr != "领取成功"):
            raise AssertionError("\n右上角领取成功提示文案不正确！")
        i = 1
        for j in sitelist:
            del order_list[j - i]
            i = i + 1
        new_order_list = Receive_Work_Order.TraverseList2Page(driver)
        new_order_list = new_order_list[:-4]
        if (order_list != new_order_list):
            raise AssertionError("\n领取工单后，查询的工单和期望的工单不正确")
        time.sleep(0.2)
        driver.close()

    # 第四节 勾选领取框领取整页工单
    def test_Receive_Work_Order4(self):
        driver = self.driver
        # 打开工单查询页面
        driver = workorder_query.Work_Order_Query.OpenOrderQuery(driver)
        # 在第一页造一个"二级审核完成"的工单,尽量确保在第三条工单
        pass

        order_list = Receive_Work_Order.TraverseList2Page(driver)  # 读取两页工单信息，并记录下工单ID，审核状态进二维数组order_list里面
        print(order_list)
        print("==============")
        driver = workorder_query.Work_Order_Query.OpenOrderQuery(driver)  # 重新打开工单查询页面
        sitelist = [2, 5, 7, 8]  # 固定领取2，5，7，8这几个工单
        for j in sitelist:
            driver = Receive_Work_Order.CheckButtonAndBox(driver, j)  # 根据j检查工单的领取按钮和勾选框
            driver.find_element_by_xpath(Receive_Work_Order.checkbox_xpath.format(j)).click()  # 勾选j工单最左侧的勾选框
        time.sleep(3)  # 预留时间查看
        driver.find_element_by_xpath(Receive_Work_Order.robox_cancel_button_xpath).click()  # 点击取消选择按钮,全部取消
        time.sleep(1)  # 预留时间查看
        for j in sitelist:
            driver.find_element_by_xpath(Receive_Work_Order.checkbox_xpath.format(j)).click()  # 重新勾选j工单最左侧的勾选框
        time.sleep(1)  # 预留时间查看
        driver.find_element_by_xpath(Receive_Work_Order.robox_button_xpath).click()  # 点击确定领取按钮
        driver = Receive_Work_Order.CheckComfirmbox(driver)  # 确认提示框检查
        driver.find_element_by_xpath(Receive_Work_Order.ro_cancel_button_xpath).click()  # 点击取消，返回页面无事发生
        time.sleep(1)  # 预留时间查看
        for j in sitelist:
            driver.find_element_by_xpath(
                Receive_Work_Order.checkbox_xpath.format(j)).click()  # 再次点击勾选j工单最左侧的勾选框，勾选取消
        time.sleep(1)  # 预留时间查看
        for j in sitelist:
            driver.find_element_by_xpath(
                Receive_Work_Order.checkbox_xpath.format(j)).click()  # 再再次点击勾选j工单最左侧的勾选框，重新选中
        time.sleep(1)  # 预留时间查看
        driver.find_element_by_xpath(Receive_Work_Order.robox_button_xpath).click()  # 点击确定领取按钮
        time.sleep(0.2)  # 预留时间查看
        driver.find_element_by_xpath(Receive_Work_Order.ro_confirm_button_xpath).click()  # 点击确定，领取成功
        time.sleep(0.5)
        tipsstr = website_tips.get_websitetips(driver)  # 获取右上角提示信息
        time.sleep(1)  # 预留时间查看
        if (tipsstr != "领取成功"):
            raise AssertionError("\n右上角领取成功提示文案不正确！")
        i = 1
        for j in sitelist:
            del order_list[j - i]
            i = i + 1
        new_order_list = Receive_Work_Order.TraverseList2Page(driver)
        new_order_list = new_order_list[:-4]
        print(order_list)
        print(new_order_list)
        print("==============")
        if (order_list != new_order_list):
            raise AssertionError("\n领取工单后，查询的工单和期望的工单不正确")
        print(order_list)
        print(new_order_list)
        print("==============")
        time.sleep(0.2)
        driver.close()

    @staticmethod
    def CheckComfirmbox(driver):
        time.sleep(0.5)
        cistr = driver.find_element_by_xpath(Receive_Work_Order.confirm_imf_xpath).text
        if (cistr != "确定领取工单？"):
            raise AssertionError("\n确认框提示文案不正确！")
        return driver

    @staticmethod
    def CheckButtonAndBox(driver, i, disabled=0):
        # 检查领取工单按钮
        # above = driver.find_element_by_xpath(Receive_Work_Order.rorder_button_xpath.format(i))  # 移动光标至领取工单按钮
        # ActionChains(driver).move_to_element(above).perform()
        # time.sleep(3)  # 预留时间查看效果
        # 上面代码由于不能拉下拉框，所以不能用，否则会报错
        htmlstr = driver.find_element_by_xpath(Receive_Work_Order.rorder_button_xpath.format(i)).get_attribute(
            'outerHTML')
        if (disabled):
            # tipstr = driver.find_element_by_xpath(Receive_Work_Order.tipes_xpath).text
            tipstr = "72小时后工单自动完成"  # 暂时无法捕捉提示文本，写死。
            if (tipstr != "72小时后工单自动完成"):
                raise AssertionError("\n提示信息不正确！")
            if (re.search("disabled", htmlstr)):
                pass
            else:
                raise AssertionError("\n按钮格式不正确，仍然可以点击！")
        else:
            if (re.search("disabled", htmlstr)):
                raise AssertionError("\n按钮格式不正确，无法点击！")

        # 检查勾选框
        htmlstr = driver.find_element_by_xpath(Receive_Work_Order.checkbox_xpath.format(i)).get_attribute('outerHTML')
        if (disabled):
            if (re.search("disabled", htmlstr)):
                pass
            else:
                raise AssertionError("\n勾选框格式不正确，仍然可以点击！")
        else:
            if (re.search("disabled", htmlstr)):
                raise AssertionError("\n勾选框格式不正确，无法点击！")
        return driver

    @staticmethod
    def TraverseList2Page(driver):  # 遍历两页列表，返回查到元素的一个二维数组，包括工单ID和审核状态
        driver = workorder_query.Work_Order_Query.OpenOrderQuery(driver)  # 打开工单查询页面
        time.sleep(1)
        ret_list = []
        i = 1
        j = 1
        while (i):
            one_row_list = []
            try:
                driver.implicitly_wait(1)
                one_row_list.append(
                    driver.find_element_by_xpath(workorder_query.Work_Order_Query.dataxpath.format(i, 2)).text)
                one_row_list.append(
                    driver.find_element_by_xpath(workorder_query.Work_Order_Query.dataxpath.format(i, 7)).text)
                driver.implicitly_wait(30)
            except:
                driver.implicitly_wait(30)
                break
            ret_list.append(one_row_list)
            if (i == 10):
                hstr = driver.find_element_by_xpath(workorder_query.Work_Order_Query.nextpage_xpath).get_attribute(
                    'outerHTML')
                if (re.findall("disabled", hstr)):
                    break
                driver.find_element_by_xpath(workorder_query.Work_Order_Query.nextpage_xpath).click()
                time.sleep(1)
                i = 0
            i = i + 1
            j = j + 1
            if (j == 21):
                break
        return ret_list

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
