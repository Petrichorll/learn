# coding=utf-8
import unittest
# 把 test_case 目录添加到 path 下，这里用的相对路径
import sys
sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")
# 这里需要导入测试文件
from test_case import change_password,organization_add,organization_edit,organization_delete,organization_query
from public import login

import HTMLTestRunner

testunit = unittest.TestSuite()
# 将测试用例加入到测试容器(套件)中
# testunit.addTest(unittest.makeSuite(organization_query.Organization_Query))
testunit.addTest(unittest.makeSuite(organization_query.Organization_Query))
# testunit.addTest(unittest.makeSuite(login.Login_CAS))
# testunit.addTest(unittest.makeSuite(change_password.Change_Password))
# testunit.addTest(unittest.makeSuite(organization_add.Organization_Add))
# testunit.addTest(unittest.makeSuite(organization_edit.Organization_Edit))
# testunit.addTest(unittest.makeSuite(organization_delete.Organization_Delete))
# testunit.addTest(unittest.makeSuite(baidu.Baidu))


# 定义个报告存放路径。
filename = r'C:\Users\19144\PycharmProjects\学习\test_demo\data\report\result.html'

fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'CAS测试报告', description=u'用例执行情况：')
# 执行测试用例
runner.run(testunit)
