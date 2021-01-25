from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get("https://www.baidu.com")

browser.maximize_window()  # 浏览器窗口最大化
time.sleep(5)
browser.set_window_rect(480, 800)  # 设置浏览器宽480、高800显示
time.sleep(5)

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()

time.sleep(5)
browser.back()  # 浏览器后退按钮"<-"
time.sleep(5)
browser.forward()  # 浏览器前进按钮"->"

time.sleep(5)

time.sleep(60)

browser.quit()
