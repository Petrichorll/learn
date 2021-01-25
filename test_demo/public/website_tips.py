# -*- coding: utf-8 -*-
import time

website_tips_xpath = "//div[@class='el-notification right']/div/div[1]/p"  # 右上角网站提示的xpath
website_tips_close_xpath = "//div[@class='el-notification right']/div/div[2]"  # 关闭右上角网站提示的xpath
upload_wait_xpath = "/html/body/div[1]/div/div[2]/section/section/div/div/div[2]/div/div[2]/div/p"  # 上传时等待页面

# 获取网站右上角提示信息的文本
def get_websitetips(driver):
    try:
        driver.implicitly_wait(1)
        ret = driver.find_element_by_xpath(website_tips_xpath).text
        driver.implicitly_wait(30)
    except:
        driver.implicitly_wait(30)
        ret = ""
    return ret


# 关闭网站右上角提示信息的文本
def close_websitetips(driver):
    try:
        driver.implicitly_wait(1)
        driver.find_element_by_xpath(website_tips_close_xpath).click()
        driver.implicitly_wait(30)
    except:
        driver.implicitly_wait(30)
    return driver

def waitupload(driver):
    while (True):
        try:
            driver.implicitly_wait(1)
            tstr = driver.find_element_by_xpath(upload_wait_xpath).text
        except:
            driver.implicitly_wait(30)
            break
        finally:
            driver.implicitly_wait(30)
        time.sleep(1)

    return driver


if __name__ == "__main__":
    pass
