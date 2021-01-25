# -*- coding: utf-8 -*-
# 增删改用户/组织/角色/权限

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

import unittest, time
import sys, re
sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")

import login, data, workxls, organization_add, organization_edit, organization_delete, role_add, role_edit, role_delete, \
    user_add, user_edit, user_delete


# 日志
class Operation_Log(unittest.TestCase):
    menubar_systemmanagement_xpath = "//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[8]"
    menubar_operationlog_xpath = "/html/body/div/div/div[1]/div[3]/div[1]/div/ul/div[8]/li/ul/div/a/li/span"
    menubar_orgmanagement_xpath = "//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[5]"
    menubar_rolemanagement_xpath = "//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[6]"
    menubar_usermanagement_xpath = "//*[@id='app']/div/div[1]/div[3]/div[1]/div/ul/div[4]"
    loglist_1_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div[2]/div[3]/table/tbody/tr[1]/td[{}]/div"
    loglist_n_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div[2]/div[3]/table/tbody/tr[{}]/td[{}]/div"
    nextpage_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div[3]/div/button[2]/i"
    last1month_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div[1]/div[1]/div[1]/label[1]/span"
    last3month_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div[1]/div[1]/div[1]/label[2]/span"
    searchinput_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div[1]/div[2]/div/input"
    searchinput_s_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div/div[1]/div[2]/div/span/span/i"
    ormodestr = ""
    orresultstr = ""
    ortimestr = ""
    orcontentstr = ""

    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 组织新增日志用例
    def test_OperationAdd_Log(self):
        driver = self.driver

        # 打开日志界面，查看一眼
        driver = self.OpenOperationLog(driver)

        # 新增组织成功用例
        # 点击菜单栏组织管理
        driver.find_element_by_xpath(self.menubar_orgmanagement_xpath).click()
        time.sleep(1)
        # 新增1个组织,并记录到orgdata.xls，以供检查
        driver = organization_add.Organization_Add.OrganizationAdd(driver, 1)
        # 获取orgdata.xls的第一条数据
        data1 = workxls.getimf('orgdata.xls', 0)
        # 打开日志界面
        time.sleep(1)
        driver = self.OpenOperationLog(driver)
        print(data1)
        print(self.ormodestr, self.orresultstr, self.ortimestr, self.orcontentstr)
        if (self.ormodestr != "组织管理"):
            raise AssertionError('\n操作模块为：\"{}\"，错误！应该为：\"组织管理\"。'.format(self.ormodestr))
        if (self.orresultstr != "成功"):
            raise AssertionError('\n操作结果为：\"{}\"，错误！应该为：\"成功\"。'.format(self.orresultstr))
        if (self.ortimestr[:-1] != data1[1][:-1]):
            raise AssertionError('\n操作时间为：\"{}\"，错误！应该为：\"{}\"。'.format(self.ortimestr, data1[1]))
        if (self.orcontentstr != "新增组织成功"):
            raise AssertionError('\n操作内容为：\"{}\"，错误！应该为：\"新增组织成功\"。'.format(self.orcontentstr))
        time.sleep(1)  # 预留时间查看

        # 新增组织失败用例
        # 点击菜单栏组织管理
        driver.find_element_by_xpath(self.menubar_orgmanagement_xpath).click()
        time.sleep(1)
        # 发送新增1个组织失败命令
        driver = organization_add.Organization_Add.OrganizationAdd(driver, 1, 1)
        # 获取操作时间
        data1 = workxls.getimf('orgdata.xls', 0)
        # 打开日志界面
        time.sleep(1)
        driver = self.OpenOperationLog(driver)
        print(data1)
        print(self.ormodestr, self.orresultstr, self.ortimestr, self.orcontentstr)
        if (self.ormodestr != "组织管理"):
            raise AssertionError('\n操作模块为：\"{}\"，错误！应该为：\"组织管理\"。'.format(self.ormodestr))
        if (self.orresultstr != "失败"):
            raise AssertionError('\n操作结果为：\"{}\"，错误！应该为：\"失败\"。'.format(self.orresultstr))
        if (self.ortimestr[:-1] != data1[1][:-1]):
            raise AssertionError('\n操作时间为：\"{}\"，错误！应该为：\"{}\"。'.format(self.ortimestr, data1[1]))
        if (self.orcontentstr != "新增组织失败"):
            raise AssertionError('\n操作内容为：\"{}\"，错误！应该为：\"新增组织失败\"。'.format(self.orcontentstr))
        time.sleep(1)  # 预留时间查看

        driver.close()

    # 组织编辑日志用例
    def test_OperationEdit_Log(self):
        driver = self.driver

        # 编辑组织成功用例
        # 点击菜单栏组织管理
        driver.find_element_by_xpath(self.menubar_orgmanagement_xpath).click()
        time.sleep(1)
        # 编辑1个组织,并记录到orgdata.xls，以供检查
        driver = organization_edit.Organization_Edit.OrganizationEdit(driver, 1)
        # 获取orgdata.xls的第一条数据
        data1 = workxls.getimf('orgdata.xls', 0)
        # 打开日志界面
        time.sleep(1)
        driver = self.OpenOperationLog(driver)
        print(data1)
        print(self.ormodestr, self.orresultstr, self.ortimestr, self.orcontentstr)
        if (self.ormodestr != "组织管理"):
            raise AssertionError('\n操作模块为：\"{}\"，错误！应该为：\"组织管理\"。'.format(self.ormodestr))
        if (self.orresultstr != "成功"):
            raise AssertionError('\n操作结果为：\"{}\"，错误！应该为：\"成功\"。'.format(self.orresultstr))
        if (self.ortimestr[:-1] != data1[1][:-1]):
            raise AssertionError('\n操作时间为：\"{}\"，错误！应该为：\"{}\"。'.format(self.ortimestr, data1[1]))
        if (self.orcontentstr != "编辑组织成功"):
            raise AssertionError('\n操作内容为：\"{}\"，错误！应该为：\"编辑组织成功\"。'.format(self.orcontentstr))
        time.sleep(1)  # 预留时间查看

        # 编辑组织失败用例
        # 点击菜单栏组织管理
        driver.find_element_by_xpath(self.menubar_orgmanagement_xpath).click()
        time.sleep(1)
        # 发送编辑1个组织失败命令
        driver = organization_edit.Organization_Edit.OrganizationEdit(driver, 1, 1)
        # 获取操作时间
        data1 = workxls.getimf('orgdata.xls', 0)
        # 打开日志界面
        time.sleep(1)
        driver = self.OpenOperationLog(driver)
        print(data1)
        print(self.ormodestr, self.orresultstr, self.ortimestr, self.orcontentstr)
        if (self.ormodestr != "组织管理"):
            raise AssertionError('\n操作模块为：\"{}\"，错误！应该为：\"组织管理\"。'.format(self.ormodestr))
        if (self.orresultstr != "失败"):
            raise AssertionError('\n操作结果为：\"{}\"，错误！应该为：\"失败\"。'.format(self.orresultstr))
        if (self.ortimestr[:-1] != data1[1][:-1]):
            raise AssertionError('\n操作时间为：\"{}\"，错误！应该为：\"{}\"。'.format(self.ortimestr, data1[1]))
        if (self.orcontentstr != "编辑组织失败"):
            raise AssertionError('\n操作内容为：\"{}\"，错误！应该为：\"编辑组织失败\"。'.format(self.orcontentstr))
        time.sleep(1)  # 预留时间查看

        driver.close()

    # 组织删除日志用例
    def test_OperationDelete_Log(self):
        driver = self.driver
        # 删除组织成功用例
        # 点击菜单栏组织管理
        driver.find_element_by_xpath(self.menubar_orgmanagement_xpath).click()
        time.sleep(1)
        # 删除1个组织,并记录到orgdata.xls，以供检查
        driver = organization_delete.Organization_Delete.OrganizationDelete(driver)
        # 获取orgdata.xls的第一条数据
        data1 = workxls.getimf('orgdata.xls', 0)
        # 打开日志界面
        time.sleep(1)
        driver = self.OpenOperationLog(driver)
        print(data1)
        print(self.ormodestr, self.orresultstr, self.ortimestr, self.orcontentstr)
        if (self.ormodestr != "组织管理"):
            raise AssertionError('\n操作模块为：\"{}\"，错误！应该为：\"组织管理\"。'.format(self.ormodestr))
        if (self.orresultstr != "成功"):
            raise AssertionError('\n操作结果为：\"{}\"，错误！应该为：\"成功\"。'.format(self.orresultstr))
        if (self.ortimestr[:-1] != data1[1][:-1]):
            raise AssertionError('\n操作时间为：\"{}\"，错误！应该为：\"{}\"。'.format(self.ortimestr, data1[1]))
        if (self.orcontentstr != "删除组织成功"):
            raise AssertionError('\n\n操作内容为：\"{}\"，错误！应该为：\"删除组织成功\"。'.format(self.orcontentstr))
        time.sleep(1)  # 预留时间查看

        driver.close()

    # 角色新增日志用例
    def test_RoleAdd_Log(self):
        driver = self.driver

        # 打开日志界面，查看一眼
        driver = self.OpenOperationLog(driver)

        # 新增角色成功用例
        # 点击菜单栏角色管理
        driver.find_element_by_xpath(self.menubar_rolemanagement_xpath).click()
        time.sleep(1)
        # 新增1个角色,并记录到orgdata.xls，以供检查
        driver = role_add.Role_Add.RoleAdd(driver, 1)
        # 获取orgdata.xls的第一条数据
        data1 = workxls.getimf('roledata.xls', 0)
        # 打开日志界面
        time.sleep(1)
        driver = self.OpenOperationLog(driver)
        print(data1)
        print(self.ormodestr, self.orresultstr, self.ortimestr, self.orcontentstr)
        if (self.ormodestr != "角色管理"):
            raise AssertionError('\n操作模块为：\"{}\"，错误！应该为：\"角色管理\"。'.format(self.ormodestr))
        if (self.orresultstr != "成功"):
            raise AssertionError('\n操作结果为：\"{}\"，错误！应该为：\"成功\"。'.format(self.orresultstr))
        if (self.ortimestr[:-1] != data1[2][:-1]):
            raise AssertionError('\n操作时间为：\"{}\"，错误！应该为：\"{}\"。'.format(self.ortimestr, data1[2]))
        if (self.orcontentstr != "新增角色成功"):
            raise AssertionError('\n操作内容为：\"{}\"，错误！应该为：\"新增角色成功\"。'.format(self.orcontentstr))
        time.sleep(1)  # 预留时间查看

        # 新增角色失败用例
        # 点击菜单栏角色管理
        driver.find_element_by_xpath(self.menubar_rolemanagement_xpath).click()
        time.sleep(1)
        # 发送新增1个角色失败命令
        driver = role_add.Role_Add.RoleAdd(driver, 1, 1)
        # 获取操作时间
        data1 = workxls.getimf('roledata.xls', 0)
        # 打开日志界面
        time.sleep(1)
        driver = self.OpenOperationLog(driver)
        print(data1)
        print(self.ormodestr, self.orresultstr, self.ortimestr, self.orcontentstr)
        if (self.ormodestr != "角色管理"):
            raise AssertionError('\n操作模块为：\"{}\"，错误！应该为：\"角色管理\"。'.format(self.ormodestr))
        if (self.orresultstr != "失败"):
            raise AssertionError('\n操作结果为：\"{}\"，错误！应该为：\"失败\"。'.format(self.orresultstr))
        if (self.ortimestr[:-1] != data1[2][:-1]):
            raise AssertionError('\n操作时间为：\"{}\"，错误！应该为：\"{}\"。'.format(self.ortimestr, data1[2]))
        if (self.orcontentstr != "新增角色失败"):
            raise AssertionError('\n操作内容为：\"{}\"，错误！应该为：\"新增角色失败\"。'.format(self.orcontentstr))
        time.sleep(1)  # 预留时间查看

        driver.close()

    # 角色编辑日志用例
    def test_RoleEdit_Log(self):
        driver = self.driver

        # 编辑组织成功用例
        # 点击菜单栏角色管理
        driver.find_element_by_xpath(self.menubar_rolemanagement_xpath).click()
        time.sleep(1)
        # 编辑1个角色,并记录到roledata.xls，以供检查
        driver = role_edit.Role_Edit.RoleEdit(driver, 0)
        # 获取roledata.xls的第一条数据
        data1 = workxls.getimf('roledata.xls', 0)
        # 打开日志界面
        time.sleep(1)
        driver = self.OpenOperationLog(driver)
        print(data1)
        print(self.ormodestr, self.orresultstr, self.ortimestr, self.orcontentstr)
        if (self.ormodestr != "角色管理"):
            raise AssertionError('\n操作模块为：\"{}\"，错误！应该为：\"角色管理\"。'.format(self.ormodestr))
        if (self.orresultstr != "成功"):
            raise AssertionError('\n操作结果为：\"{}\"，错误！应该为：\"成功\"。'.format(self.orresultstr))
        if (self.ortimestr[:-1] != data1[2][:-1]):
            raise AssertionError('\n操作时间为：\"{}\"，错误！应该为：\"{}\"。'.format(self.ortimestr, data1[2]))
        if (self.orcontentstr != "编辑角色成功"):
            raise AssertionError('\n操作内容为：\"{}\"，错误！应该为：\"编辑角色成功\"。'.format(self.orcontentstr))
        time.sleep(1)  # 预留时间查看

        # 编辑角色失败用例
        # 点击菜单栏角色管理
        driver.find_element_by_xpath(self.menubar_rolemanagement_xpath).click()
        time.sleep(1)
        # 发送编辑1个组织失败命令
        driver = role_edit.Role_Edit.RoleEdit(driver, 1)
        # 获取操作时间
        data1 = workxls.getimf('roledata.xls', 0)
        # 打开日志界面
        time.sleep(1)
        driver = self.OpenOperationLog(driver)
        print(data1)
        print(self.ormodestr, self.orresultstr, self.ortimestr, self.orcontentstr)
        if (self.ormodestr != "角色管理"):
            raise AssertionError('\n操作模块为：\"{}\"，错误！应该为：\"角色管理\"。'.format(self.ormodestr))
        if (self.orresultstr != "失败"):
            raise AssertionError('\n操作结果为：\"{}\"，错误！应该为：\"失败\"。'.format(self.orresultstr))
        if (self.ortimestr[:-1] != data1[2][:-1]):
            raise AssertionError('\n操作时间为：\"{}\"，错误！应该为：\"{}\"。'.format(self.ortimestr, data1[1]))
        if (self.orcontentstr != "编辑角色失败"):
            raise AssertionError('\n操作内容为：\"{}\"，错误！应该为：\"编辑角色失败\"。'.format(self.orcontentstr))
        time.sleep(1)  # 预留时间查看

        driver.close()

    # 角色删除日志用例
    def test_RoleDelete_Log(self):
        driver = self.driver
        # 删除角色成功用例
        # 点击菜单栏角色管理
        driver.find_element_by_xpath(self.menubar_rolemanagement_xpath).click()
        time.sleep(1)
        # 删除1个角色,并记录到roledata.xls，以供检查
        # driver = role_delete.Role_Delete.RoleDelete(driver)
        # 获取orgdata.xls的第一条数据
        data1 = workxls.getimf('roledata.xls', 0)
        # 打开日志界面
        time.sleep(1)
        driver = self.OpenOperationLog(driver)
        print(data1)
        print(self.ormodestr, self.orresultstr, self.ortimestr, self.orcontentstr)
        if (self.ormodestr != "角色管理"):
            raise AssertionError('\n操作模块为：\"{}\"，错误！应该为：\"角色管理\"。'.format(self.ormodestr))
        if (self.orresultstr != "成功"):
            raise AssertionError('\n操作结果为：\"{}\"，错误！应该为：\"成功\"。'.format(self.orresultstr))
        if (self.ortimestr[:-1] != data1[2][:-1]):
            raise AssertionError('\n操作时间为：\"{}\"，错误！应该为：\"{}\"。'.format(self.ortimestr, data1[2]))
        if (self.orcontentstr != "删除角色成功"):
            raise AssertionError('\n操作内容为：\"{}\"，错误！应该为：\"删除角色成功\"。'.format(self.orcontentstr))
        time.sleep(1)  # 预留时间查看

        driver.close()

    # 用户新增日志用例
    def test_UserAdd_Log(self):
        driver = self.driver

        # 打开日志界面，查看一眼
        driver = self.OpenOperationLog(driver)

        # 新增用户成功用例
        # 点击菜单栏用户管理
        driver.find_element_by_xpath(self.menubar_usermanagement_xpath).click()
        time.sleep(1)
        # 新增1个用户,并记录到userdata.xls，以供检查
        driver = user_add.User_Add.UserAdd(driver, 1)
        # 获取userdata.xls的第一条数据
        data1 = workxls.getimf('userdata.xls', 0)
        # 打开日志界面
        time.sleep(1)
        driver = self.OpenOperationLog(driver)
        print(data1)
        print(self.ormodestr, self.orresultstr, self.ortimestr, self.orcontentstr)
        if (self.ormodestr != "用户管理"):
            raise AssertionError('\n操作模块为：\"{}\"，错误！应该为：\"用户管理\"。'.format(self.ormodestr))
        if (self.orresultstr != "成功"):
            raise AssertionError('\n操作结果为：\"{}\"，错误！应该为：\"成功\"。'.format(self.orresultstr))
        if (self.ortimestr[:-1] != data1[6][:-1]):
            if (self.ortimestr[:-1][-1] != data1[6][:-1][-1]):
                raise AssertionError('\n操作时间为：\"{}\"，错误！应该为：\"{}\"。'.format(self.ortimestr, data1[6]))
        if (self.orcontentstr != "新增用户成功"):
            raise AssertionError('\n操作内容为：\"{}\"，错误！应该为：\"新增用户成功\"。'.format(self.orcontentstr))
        time.sleep(1)  # 预留时间查看

        # 新增用户失败用例
        # 点击菜单栏用户管理
        driver.find_element_by_xpath(self.menubar_usermanagement_xpath).click()
        time.sleep(1)
        # 发送新增1个用户失败命令
        driver = user_add.User_Add.UserAdd(driver, 1, 1)
        # 获取操作时间
        data1 = workxls.getimf('userdata.xls', 0)
        # 打开日志界面
        time.sleep(1)
        driver = self.OpenOperationLog(driver)
        print(data1)
        print(self.ormodestr, self.orresultstr, self.ortimestr, self.orcontentstr)
        if (self.ormodestr != "用户管理"):
            raise AssertionError('\n操作模块为：\"{}\"，错误！应该为：\"用户管理\"。'.format(self.ormodestr))
        if (self.orresultstr != "失败"):
            raise AssertionError('\n操作结果为：\"{}\"，错误！应该为：\"失败\"。'.format(self.orresultstr))
        if (self.ortimestr[:-1] != data1[6][:-1]):
            if (self.ortimestr[:-1][-1] != data1[6][:-1][-1]):
                raise AssertionError('\n操作时间为：\"{}\"，错误！应该为：\"{}\"。'.format(self.ortimestr, data1[6]))
        if (self.orcontentstr != "新增用户失败"):
            raise AssertionError('\n操作内容为：\"{}\"，错误！应该为：\"新增用户失败\"。'.format(self.orcontentstr))
        time.sleep(1)  # 预留时间查看

        driver.close()

    # 用户编辑日志用例
    def test_UserEdit_Log(self):
        driver = self.driver

        # 编辑用户成功用例
        # 点击菜单栏用户管理
        driver.find_element_by_xpath(self.menubar_usermanagement_xpath).click()
        time.sleep(1)
        # 编辑1个用户,并记录到userdata.xls，以供检查
        driver = user_edit.User_Edit.UserEdit(driver, 0)
        # 获取orgdata.xls的第一条数据
        data1 = workxls.getimf('userdata.xls', 0)
        # 打开日志界面
        time.sleep(1)
        driver = self.OpenOperationLog(driver)
        print(data1)
        print(self.ormodestr, self.orresultstr, self.ortimestr, self.orcontentstr)
        if (self.ormodestr != "用户管理"):
            raise AssertionError('\n操作模块为：\"{}\"，错误！应该为：\"用户管理\"。'.format(self.ormodestr))
        if (self.orresultstr != "成功"):
            raise AssertionError('\n操作结果为：\"{}\"，错误！应该为：\"成功\"。'.format(self.orresultstr))
        if (self.ortimestr[:-1] != data1[6][:-1]):
            if (self.ortimestr[:-1][-1] != data1[6][:-1][-1]):
                raise AssertionError('\n操作时间为：\"{}\"，错误！应该为：\"{}\"。'.format(self.ortimestr, data1[6]))
        if (self.orcontentstr != "编辑用户成功"):
            raise AssertionError('\n操作内容为：\"{}\"，错误！应该为：\"编辑用户成功\"。'.format(self.orcontentstr))
        time.sleep(1)  # 预留时间查看

        # 编辑用户失败用例
        # 点击菜单栏用户管理
        driver.find_element_by_xpath(self.menubar_usermanagement_xpath).click()
        time.sleep(1)
        # 发送编辑1个用户失败命令
        driver = user_edit.User_Edit.UserEdit(driver, 1)
        # 获取操作时间
        data1 = workxls.getimf('userdata.xls', 0)
        # 打开日志界面
        time.sleep(1)
        driver = self.OpenOperationLog(driver)
        print(data1)
        print(self.ormodestr, self.orresultstr, self.ortimestr, self.orcontentstr)
        if (self.ormodestr != "用户管理"):
            raise AssertionError('\n操作模块为：\"{}\"，错误！应该为：\"用户管理\"。'.format(self.ormodestr))
        if (self.orresultstr != "失败"):
            raise AssertionError('\n操作结果为：\"{}\"，错误！应该为：\"失败\"。'.format(self.orresultstr))
        if (self.ortimestr[:-1] != data1[6][:-1]):
            if (self.ortimestr[:-1][-1] != data1[6][:-1][-1]):
                raise AssertionError('\n操作时间为：\"{}\"，错误！应该为：\"{}\"。'.format(self.ortimestr, data1[6]))
        if (self.orcontentstr != "编辑用户失败"):
            raise AssertionError('\n操作内容为：\"{}\"，错误！应该为：\"编辑用户失败\"。'.format(self.orcontentstr))
        time.sleep(1)  # 预留时间查看

        driver.close()

    # 用户删除日志用例
    def test_UserDelete_Log(self):
        driver = self.driver
        # 删除用户成功用例
        # 点击菜单栏用户管理
        driver.find_element_by_xpath(self.menubar_usermanagement_xpath).click()
        time.sleep(1)
        # 删除1个用户,并记录到userdata.xls，以供检查
        driver = user_delete.User_Delete.UserDelete(driver)
        # 获取userdata.xls的第一条数据
        data1 = workxls.getimf('userdata.xls', 0)
        # 打开日志界面
        time.sleep(1)
        driver = self.OpenOperationLog(driver)
        print(data1)
        print(self.ormodestr, self.orresultstr, self.ortimestr, self.orcontentstr)
        if (self.ormodestr != "用户管理"):
            raise AssertionError('\n操作模块为：\"{}\"，错误！应该为：\"用户管理\"。'.format(self.ormodestr))
        if (self.orresultstr != "成功"):
            raise AssertionError('\n操作结果为：\"{}\"，错误！应该为：\"成功\"。'.format(self.orresultstr))
        if (self.ortimestr[:-1] != data1[6][:-1]):
            if (self.ortimestr[:-1][-1] != data1[6][:-1][-1]):
                raise AssertionError('\n操作时间为：\"{}\"，错误！应该为：\"{}\"。'.format(self.ortimestr, data1[6]))
        if (self.orcontentstr != "删除用户成功"):
            raise AssertionError('\n操作内容为：\"{}\"，错误！应该为：\"删除用户成功\"。'.format(self.orcontentstr))
        time.sleep(1)  # 预留时间查看

        driver.close()

    # 日志查询排序检查用例
    def test_Logganization_Query_Sort(self):
        driver = self.driver
        # 打开日志界面，查看一眼
        driver = self.OpenOperationLog(driver)

        time.sleep(1)
        i = 2
        while (i):
            timestr1 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i - 1, 5)).text
            if (i == 11):
                try:
                    driver.find_element_by_xpath(Operation_Log.nextpage_xpath).click()
                    time.sleep(1)
                except:
                    break
                i = 1
            try:
                self.driver.implicitly_wait(1)
                timestr2 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i, 5)).text
                self.driver.implicitly_wait(30)
            except:
                self.driver.implicitly_wait(30)
                break
            print(timestr1, timestr2)
            if (timestr1 > timestr2):
                if (i == 1):
                    omode1 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(10, 2)).text
                    ocontent1 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(10, 6)).text
                else:
                    omode1 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i - 1, 2)).text
                    ocontent1 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i - 1, 6)).text
                omode2 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i, 2)).text
                ocontent2 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i, 6)).text
                raise AssertionError(
                    '\n操作模块和操作内容：{} {} 的操作时间\"{}\"\n操作模块和操作内容：{} {} 的操作时间\"{}\"\n两者排序不对！'.format(omode1, ocontent1,
                                                                                                 timestr1, omode2,
                                                                                                 ocontent2, timestr2))
            i = i + 1

        driver.close()

    # 日志查询过滤检查用例
    def test_Logganization_Query_filter(self):
        driver = self.driver
        # 打开日志界面，查看一眼
        driver = self.OpenOperationLog(driver)
        time.sleep(1)
        # 点击"近一个月"按钮，检查操作日期
        driver.find_element_by_xpath(Operation_Log.last1month_xpath).click()
        # timestr2 = data.delay_time(months=-1)
        timestr2 = data.delay_time(days=-100)
        time.sleep(1)
        i = 2
        while (i):
            timestr1 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i - 1, 5)).text
            if (i == 11):
                try:
                    driver.find_element_by_xpath(Operation_Log.nextpage_xpath).click()
                    time.sleep(1)
                except:
                    break
                i = 1
            try:
                self.driver.implicitly_wait(1)
                timestr3 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i, 5)).text
                self.driver.implicitly_wait(30)
            except:
                self.driver.implicitly_wait(30)
                break
            print(timestr2, timestr1)
            if (timestr1 < timestr2):
                if (i == 1):
                    omode1 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(10, 2)).text
                    ocontent1 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(10, 6)).text
                else:
                    omode1 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i - 1, 2)).text
                    ocontent1 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i - 1, 6)).text
                raise AssertionError('\n操作模块和操作内容：{} {} 的操作时间\"{}\"超过了一个月！'.format(omode1, ocontent1, timestr1))
            i = i + 1

        # 点击"近三个月"按钮，检查操作日期
        driver.find_element_by_xpath(Operation_Log.last3month_xpath).click()
        # timestr2 = data.delay_time(months=-3)
        timestr2 = data.delay_time(days=-100)
        time.sleep(1)
        i = 2
        while (i):
            timestr1 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i - 1, 5)).text
            if (i == 11):
                try:
                    driver.find_element_by_xpath(Operation_Log.nextpage_xpath).click()
                    time.sleep(1)
                except:
                    break
                i = 1
            try:
                self.driver.implicitly_wait(1)
                timestr3 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i, 5)).text
                self.driver.implicitly_wait(30)
            except:
                self.driver.implicitly_wait(30)
                break
            print(timestr2, timestr1)
            if (timestr1 < timestr2):
                if (i == 1):
                    omode1 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(10, 2)).text
                    ocontent1 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(10, 6)).text
                else:
                    omode1 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i - 1, 2)).text
                    ocontent1 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i - 1, 6)).text
                raise AssertionError('\n操作模块和操作内容：{} {} 的操作时间\"{}\"超过了三个月！'.format(omode1, ocontent1, timestr1))
            i = i + 1

        driver.close()

    # 日志查询搜索框检查用例
    def test_Logganization_Query_Seek(self):
        driver = self.driver
        # 打开日志界面，查看一眼
        driver = self.OpenOperationLog(driver)
        time.sleep(1)
        time.sleep(1)
        i = 1
        all_opr_nameandcontent_name = []
        # 遍历查到的日志，把所有日志的操作人名称和操作结果放入all_opr_nameandcontent_name列表
        while (i):
            all_opr_nameandcontent_name.append(
                driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i, 4)).text)
            all_opr_nameandcontent_name.append(
                driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i, 6)).text)
            if (i == 10):
                try:
                    driver.find_element_by_xpath(Operation_Log.nextpage_xpath).click()
                    time.sleep(1)
                except:
                    break
                i = 0
            try:
                self.driver.implicitly_wait(1)
                timestr2 = driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i + 1, 6)).text
                self.driver.implicitly_wait(30)
            except:
                self.driver.implicitly_wait(30)
                break
            i = i + 1
        print(all_opr_nameandcontent_name)
        print(len(all_opr_nameandcontent_name))
        search_data = ['', '5', 'e1', 'haus']  # 搜索框要输入的字段，分别对应：1.不输入字；2.输入一个字；3.输入多个字；4.输入不存在的字，这四个用例

        # 遍历搜索数据，把搜索数据填入搜索框，进行检查
        for sdata in search_data:
            driver.find_element_by_xpath(Operation_Log.searchinput_xpath).clear()
            driver.find_element_by_xpath(Operation_Log.searchinput_xpath).send_keys(sdata)
            driver.find_element_by_xpath(Operation_Log.searchinput_s_xpath).click()

            # 遍历查到的日志，把所有日志的操作人名称和操作结果放入some_opr_nameandcontent_name列表
            i = 1
            some_opr_nameandcontent_name = []
            time.sleep(1)
            while (i):
                try:
                    self.driver.implicitly_wait(1)
                    some_opr_nameandcontent_name.append(
                        driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i, 4)).text)
                    some_opr_nameandcontent_name.append(
                        driver.find_element_by_xpath(Operation_Log.loglist_n_xpath.format(i, 6)).text)
                    self.driver.implicitly_wait(30)
                except:
                    self.driver.implicitly_wait(30)
                    break
                if (i == 10):
                    try:
                        time.sleep(1)
                        driver.find_element_by_xpath(Operation_Log.nextpage_xpath).click()
                        time.sleep(1)
                    except:
                        break
                    i = 0
                i = i + 1
            # 遍历所有日志结果，预计应该查到的数据，填入hope_opr_nameandcontent_name列表
            hope_opr_nameandcontent_name = []
            i = 0
            while (i < len(all_opr_nameandcontent_name)):
                if (re.search(sdata, all_opr_nameandcontent_name[i])):
                    hope_opr_nameandcontent_name.append(all_opr_nameandcontent_name[i])
                    hope_opr_nameandcontent_name.append(all_opr_nameandcontent_name[i + 1])
                i = i + 2

            # 比较some_organization_name和hope_organization_name，如有误，则测试不通过
            print(some_opr_nameandcontent_name)
            print(hope_opr_nameandcontent_name)
            if (some_opr_nameandcontent_name != hope_opr_nameandcontent_name):
                raise AssertionError(
                    '\n搜索功能不正确！\n应该搜索出的组织：{}；\n实际搜索出的组织：{}。'.format(hope_opr_nameandcontent_name,
                                                              hope_opr_nameandcontent_name))
        driver.close()

    @staticmethod
    def OpenOperationLog(driver):  # 打开日志界面，记录第一条信息的要素
        time.sleep(1)
        # 点击菜单栏系统管理
        try:
            driver.implicitly_wait(1)
            driver.find_element_by_xpath(Operation_Log.menubar_operationlog_xpath).click()
            time.sleep(1)
        except:
            driver.find_element_by_xpath(Operation_Log.menubar_systemmanagement_xpath).click()
            time.sleep(1)
            # 点击菜单栏操作日志
            driver.find_element_by_xpath(Operation_Log.menubar_operationlog_xpath).click()
            time.sleep(1)
        finally:
            driver.implicitly_wait(30)

        # 记录第一条信息的要素
        Operation_Log.ormodestr = driver.find_element_by_xpath(Operation_Log.loglist_1_xpath.format(2)).text  # 操作模块
        Operation_Log.orresultstr = driver.find_element_by_xpath(Operation_Log.loglist_1_xpath.format(3)).text  # 操作结果
        Operation_Log.ortimestr = driver.find_element_by_xpath(Operation_Log.loglist_1_xpath.format(5)).text  # 操作时间
        Operation_Log.orcontentstr = driver.find_element_by_xpath(Operation_Log.loglist_1_xpath.format(6)).text  # 操作内容

        return driver

    '''
    @staticmethod
    def OrganizationAdd(driver, writedata=0):
        name = data.get_some_name()
        time.sleep(1)
        # 点击新增组织按钮，弹出新增框
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/section/div/div/div[1]/div[1]/button").click()

        return driver
    '''

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
