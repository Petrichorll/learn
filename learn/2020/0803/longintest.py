# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("https://qiye.163.com/login/?from=ym")

# time.sleep(5)

driver.find_element_by_id("accname").clear()
driver.find_element_by_id("accname").send_keys("username")
# time.sleep(5)
size = driver.find_element_by_id("accname").size
# print(size)
driver.find_element_by_id("accname").clear()
driver.find_element_by_id("accname").send_keys("liulei@deepait.com")
# time.sleep(5)
driver.find_element_by_id("accpwd").clear()
driver.find_element_by_id("accpwd").send_keys("password")
# time.sleep(5)
driver.find_element_by_id("accpwd").clear()
driver.find_element_by_id("accpwd").send_keys("234werSDF")
time.sleep(5)
driver.find_element_by_class_name("loginbtn").click()
time.sleep(5)
driver.find_element_by_id("folder_1").click()

right = driver.find_element_by_class_name("f-txt-overflow")
ActionChains(driver).context_click(right).perform()

time.sleep(5)

time.sleep(60)
# 通过 submit() 来提交操作
# driver.find_element_by_id("dl_an_submit").submit()
driver.quit()
