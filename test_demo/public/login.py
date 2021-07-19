from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time, os
import data

url = data.get_url()


# up_list = data.get_un_pw()
# user_name = up_list[0]
# user_pwd = up_list[1]


class Login_CAS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = url
        self.verificationErrors = []
        self.accept_next_alert = True

    # CAS登录用例
    def test_CAS_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        up_list = data.get_un_pw()
        user_name = up_list[0]
        user_pwd = up_list[1]
        driver.find_element_by_class_name("el-link--inner").click()
        # time.sleep(60)
        driver.find_element_by_name("account").clear()
        driver.find_element_by_name("account").send_keys(user_name)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(user_pwd)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/form/button").click()
        time.sleep(1)
        driver.close()

    # CAS退出用例
    def test_CAS_quit(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_class_name("el-link--inner").click()
        driver.find_element_by_name("account").clear()
        driver.find_element_by_name("account").send_keys(user_name)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(user_pwd)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/form/button").click()
        time.sleep(1)
        # 点击下拉框
        driver.find_element_by_class_name("el-icon-caret-bottom").click()
        time.sleep(1)
        # 再点击下拉框下的选项-退出
        driver.find_element_by_xpath("/html/body/ul/li").click()
        time.sleep(3)
        driver.close()

    # # CAS退出用例
    # def test_CAS_quit(self):
    #     driver = self.login()
    #     # 点击下拉框
    #     driver.find_element_by_class_name("el-icon-caret-bottom").click()
    #     time.sleep(1)
    #     # 再点击下拉框下的选项-退出
    #     driver.find_element_by_xpath("/html/body/ul/li").click()
    #     time.sleep(3)
    #     driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    @staticmethod
    def login():
        i = 1  # 如果i=0，表示旧版。i=1，表示中移定制版
        if (i == 0):
            driver = webdriver.Firefox()
            driver.get(url)
            driver.maximize_window()
            up_list = data.get_un_pw()
            user_name = up_list[0]
            user_pwd = up_list[1]
            driver.find_element_by_class_name("el-link--inner").click()
            # time.sleep(60)
            driver.find_element_by_name("account").clear()
            driver.find_element_by_name("account").send_keys(user_name)
            driver.find_element_by_name("password").clear()
            driver.find_element_by_name("password").send_keys(user_pwd)
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div/div/form/button").click()
            time.sleep(2)
            # driver.refresh()  # 刷新一下页面，8月18号执行时，页面没有自动刷新，所以添加了这一句，其它脚本可能也需要用上
        elif (i == 1):
            driver = webdriver.Firefox()
            driver.get(url)
            driver.maximize_window()
            up_list = data.get_un_pw()
            user_name = up_list[0]
            user_pwd = up_list[1]
            driver.find_element_by_xpath("/html/body/div/div/form/div[3]/div/div/input").clear()
            driver.find_element_by_xpath("/html/body/div/div/form/div[3]/div/div/input").send_keys(user_name)
            driver.find_element_by_xpath("/html/body/div/div/form/div[4]/div/div/input").clear()
            driver.find_element_by_xpath("/html/body/div/div/form/div[4]/div/div/input").send_keys(user_pwd)
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div/div/form/button").click()
            time.sleep(1)
        else:
            driver = webdriver.Firefox()
        return driver

    @staticmethod
    def login_yaliceshi(i):
        driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        up_list = data.get_un_pw_jameter()
        user_name = up_list[i]
        user_pwd = "qw111111"
        # time.sleep(60)
        driver.find_element_by_name("account").clear()
        driver.find_element_by_name("account").send_keys(user_name)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(user_pwd)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/form/button").click()
        time.sleep(1)
        return driver


if __name__ == "__main__":
    l = Login_CAS()
    l.test_CAS_quit()
