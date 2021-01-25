# -*- coding: utf-8 -*-
# 用户登录，获取用户ID和CAStoken

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, random
import sys, re

sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")
import login, data, workxls
from selenium.webdriver.common.action_chains import ActionChains


# 用户新增
class User_Add(unittest.TestCase):
    user_add_confirm_button_xpath = "//*[@id='app']/div/div[2]/section/section/div/div/div[3]/div/div/div[3]/div/button[1]/span"  # 确定按钮的xpath

    def setUp(self):
        self.driver = login.Login_CAS.login_yaliceshi(0)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 用户新增用例
    def test_User_Add(self):
        driver = self.driver
        time.sleep(2)
        rpb = driver.get_cookies()
        # rstr = "{'name': 'CASTOKEN', 'value': 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJibE5XY2szSTd3aEtiZXNRaFNrb0ZTZ2Fpb01xSXc3bDdDOVJrZE5rbTJNIn0.eyJleHAiOjE2MDc0NTk4NjAsImlhdCI6MTYwNzQyMzg2MCwianRpIjoiM2QwOTE3NGUtZDRkNy00MmUyLTk3MmMtMjhlZmVlNTFhOTU5IiwiaXNzIjoiaHR0cDovLzE5Mi4xNjguMC4xMTM6ODA4MC9hdXRoL3JlYWxtcy9jYXMiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiYjBlNzZiYTQtZGI3NS00MTJkLTgzMTMtYzliMzU2YzUxOTJmIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYnJva2VyIiwic2Vzc2lvbl9zdGF0ZSI6ImE2MTIwYmZjLTBkMTMtNDZiYy05YWU2LWE5MDZkMDNlNWNkZSIsImFjciI6IjEiLCJyZXNvdXJjZV9hY2Nlc3MiOnsiYnJva2VyIjp7InJvbGVzIjpbIi9hcGkvdjEvb3JkZXJzL3N1YnRhZy9lZGl0IiwiL2FwaS92MS9maWxlL3VwbG9hZCIsIi9hcGkvdjEvb3JkZXJzL3VwbG9hZHJlY29yZC9kZWxldGUiLCIvYXBpL3YxL29yZGVycy9teW9yZGVyL2F1ZGl0IiwiL2FwaS92MS9vcmRlcnMvdXBsb2FkcmVjb3JkL2xpc3QiLCIvYXBpL3YxL29yZGVycy90YWcvbGlzdCIsIi9hcGkvdjEvb3JkZXJzL215b3JkZXIvbGlzdCIsIi9hcGkvdjEvb3JkZXJzL2JvdHRvbWxpYnJhcnkvZGVsZXRlIiwiL2FwaS92MS9vcmRlcnMvc3VidGFnL2RlbGV0ZSIsIi9hcGkvdjEvdXNlcnMvbG9nL2xpc3QiLCIvYXBpL3YxL29yZGVycy9teW9yZGVyL2Fzc2lnbm9yZGVyIiwiL2FwaS92MS9vcmRlcnMvc3VidGFnL2xpc3QiLCIvYXBpL3YxL29yZGVycy9vcmRlcmluZm8vcmVjZWl2ZSIsIi9hcGkvdjEvb3JkZXJzL29yZGVycXVlcnkvbGlzdCIsIi9hcGkvdjEvb3JkZXJzL3VwbG9hZHJlY29yZC9pbmZvIiwiL2FwaS92MS9vcmRlcnMvdGFnL2luZm8iLCIvYXBpL3YxL29yZGVycy90YWcvZGVsZXRlIiwiL2FwaS92MS9vcmRlcnMvc3VidGFnL2NyZWF0ZSIsIi9hcGkvdjEvb3JkZXJzL215b3JkZXIvaW5mbyIsIi9hcGkvdjEvb3JkZXJzL29yZGVycXVlcnkvcmVjZWl2ZSIsIi9hcGkvdjEvb3JkZXJzL29yZGVycXVlcnkvaW5mbyIsIi9hcGkvdjEvZmlsZS92aWRlbyIsIi9hcGkvdjEvb3JkZXJzL3VwbG9hZHZvcmRlci9jcmVhdGUiLCIvYXBpL3YxL29yZGVycy9zdHJhdGVneS91cGRhdGUiLCIvYXBpL3YxL2ZpbGUvZ2V0ZmlsZSIsIi9hcGkvdjEvb3JkZXJzL3RhZy9jcmVhdGUiLCIvYXBpL3YxL29yZGVycy9taHR1cGxvYWR2b3JkZXIvY3JlYXRlIiwiL2FwaS92MS9vcmRlcnMvc3RyYXRlZ3kvaW5mbyIsIi9hcGkvdjEvb3JkZXJzL3N1YnRhZy9pbmZvIiwiL2FwaS92MS9vcmRlcnMvb3JkZXIvbGlzdCIsIi9hcGkvdjEvb3JkZXJzL3Jlc3VsdC9kZXRhaWxzIiwiL2FwaS92MS9vcmRlcnMvb3JkZXIvcmVjZWl2ZSIsIi9hcGkvdjEvb3JkZXJzL215b3JkZXIvYXNzaWdudXNlcmxpc3QiLCIvYXBpL3YxL29yZGVycy9zdWJ0YWcvY2hlY2siLCIvYXBpL3YxL29yZGVycy9hbGx0YWcvbGlzdCIsIi9hcGkvdjEvb3JkZXJzL2JvdHRvbWxpYnJhcnkvbGlzdCIsIi9hcGkvdjEvZmlsZS9leHRyYWN0IiwiL2FwaS92MS9vcmRlcnMvYWlyZXN1bHQvZGV0YWlscyIsIi9hcGkvdjEvb3JkZXJzL29yZGVyL2RlbGV0ZSIsIi9hcGkvdjEvb3JkZXJzL3RhZy9lZGl0IiwiL2FwaS92MS9vcmRlcnMvYm90dG9tbGlicmFyeS9yZW5hbWUiLCIvYXBpL3YxL29yZGVycy9yZXN1bHQvbGlzdCIsIi9hcGkvdjEvb3JkZXJzL2FpcmVzdWx0L2xpc3QiLCIvYXBpL3YxL2ZpbGUvbWh0L3VwbG9hZCJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJiMzEyQHFxLmNvbSIsImVtYWlsIjoiYjMxMkBxcS5jb20ifQ.G1WstmE5ZFNy0gRcL4HUlzu5mZ09oEWxkEvq8tIl90e45RS75kCpCt8u5OiGPfipIpHIYKdAJQYBlxyX9phmXYLOTGzhj-yuv3ClJcjVRBOlOzDMnod-YEB9pDMy8JrKN-ZGs4n6n8khJJIf6Gz3w884cuJpG5R0GsGl0SET9qn5bplK6jK28e_pcd-z4zT4zsP2LbNv8R3wiSOAJgr9L-l5hy0muJc4R41Qp_CRYgLA1lbxsfMJZk1mErZylxeGDAuYWOakJDufuk3PhPVnDmAldsnYBVoBzn0eMssAT4UU96Q9Rm_385TE5T2BiET8ErV_I0JU5m8tdsGz-Cvvqg', 'path': '/', 'domain': '192.168.0.180', 'secure': False, 'httpOnly': False, 'sameSite': 'None'}"
        print(rpb)
        print(rpb[0])
        a = re.findall("'value': '.+', 'path':", str(rpb[0]))
        b = re.split("'value': '", a[0])
        castoken = re.split("', 'path':", b[1])
        castoken = "Bearer " + castoken
        a = re.findall("'value': '.+', 'path':", str(rpb[2]))
        b = re.split("'value': '", a[0])
        userID = re.split("', 'path':", b[1])

        print(castoken)
        print(userID)
        time.sleep(1000)
        driver.close()

    @staticmethod
    def Checkconfirmb(driver):  # 检查确定按钮
        pass

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
