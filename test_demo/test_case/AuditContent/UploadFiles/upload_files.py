# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re, random
import sys

sys.path.append(r"C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\public")

import login, website_tips, read_mht, data, workxls


class Upload_Files(unittest.TestCase):
    audit_content_xpath = "//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul[1]/div[1]/li/div/span"  # 菜单栏-一级菜单-审核内容按钮的xpath
    upload_files_xpath = "//*[@id='app']/div/div[1]/div[2]/div[1]/div/ul[1]/div[1]/li/ul/div[1]/a/li/span"  # 菜单栏-二级菜单-上传文件按钮的xpath
    upload_file_xpath = "/html/body/div/div/div[2]/section/section/div/div/div[1]/div/div/p[1]/button/span/ul/div[1]/label/input"  # 上传文件页面，上传文件的xpath
    # "/html/body/div[2]/div/div[2]/section/section/div/div/div[1]/div/div/p[1]/button/span/ul/div[1]/label/input"
    #    "//*[@id="app"]/div/div[2]/section/section/div/div/div[1]/div/div/p[1]/button/span/ul/div[1]/label/input"
    # upload_file_xpath按钮在页面中是隐藏的
    upload_xpath = "/html/body/div[1]/div/div[2]/section/section/div/div[1]/div/div/p[1]/button/span"  # 上传按钮的xpath，实际没作用，鼠标悬停查看效果
    files_path = "C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\data\\PendingDocuments\\test1\\"
    files_path2 = "C:\\Users\\19144\\PycharmProjects\\学习\\test_demo\\data\\PendingDocuments\\test2\\"
    tips_xpath = "/html/body/div[1]/div/div[2]/section/section/div/div[1]/div/div/p[2]"  # 上传文件页面内提示信息的xpath
    page_sec_name_xpath = "/html/body/div[1]/div/div[2]/section/div/span/span[2]/span[1]/span"  # 页面二级名称的xpath

    def setUp(self):
        self.driver = login.Login_CAS.login()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    # 测试上传文件
    def test_Upload_Files(self):
        driver = self.driver
        # 打开上传页面
        driver = Upload_Files.OpenUploadFiles(driver)
        # 鼠标悬停"上传"按钮，查看效果
        above = driver.find_element_by_xpath(Upload_Files.upload_xpath)  # 移动光标至"上传"按钮
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(2)  # 预留时间查看效果
        # 检查提示信息文本是否正确
        tips_str = driver.find_element_by_xpath(Upload_Files.tips_xpath).text
        if (tips_str != "图片支持格式：png，bmp，jpeg，gif；文本支持格式：txt；视频支持格式：mp4文件大小不可超过500M"):
            raise AssertionError("\n上传文件页面，提示文本不正确！")
        time.sleep(1)

        # # 上传单一图片
        # driver.find_element_by_xpath(Upload_Files.upload_file_xpath).send_keys(Upload_Files.files_path + "pic (1).jpg")
        # driver = website_tips.waitupload(driver)  # 等待上传，成功后打开工单池页面
        # time.sleep(1)
        # pagename = driver.find_element_by_xpath(Upload_Files.page_sec_name_xpath).text
        # if(pagename!="工单池"):
        #     raise AssertionError("\n跳转页面不正确")
        # driver = Upload_Files.OpenUploadFiles(driver)# 重新打开上传页面
        # time.sleep(1)

        # 上传大于10M的图片
        file_name = "中国地图.jpg"
        driver.find_element_by_xpath(Upload_Files.upload_file_xpath).send_keys(Upload_Files.files_path + file_name)
        time.sleep(1)
        websitetips = website_tips.get_websitetips(driver)
        if (websitetips != "文件名：{}大小超过10M".format(file_name)):
            raise AssertionError("\n上传不支持的文件后，提示信息不正确！")
        website_tips.close_websitetips(driver)
        time.sleep(1)

        # 上传系统不支持的格式的图片
        file_name = "favicon.ico"
        driver.find_element_by_xpath(Upload_Files.upload_file_xpath).send_keys(Upload_Files.files_path + file_name)
        time.sleep(1)
        websitetips = website_tips.get_websitetips(driver)
        if (websitetips != "文件名：{}格式无效".format(file_name)):
            raise AssertionError("\n上传不支持的文件后，提示信息不正确！")
        website_tips.close_websitetips(driver)
        time.sleep(1)

        # # 上传单一视频
        # driver.find_element_by_xpath(Upload_Files.upload_file_xpath).send_keys(
        #     Upload_Files.files_path + "2020-10-22 10-00-28.mp4")
        # driver = website_tips.waitupload(driver)  # 等待上传，成功后打开工单池页面
        # time.sleep(1)
        # pagename = driver.find_element_by_xpath(Upload_Files.page_sec_name_xpath).text
        # if(pagename!="工单池"):
        #     raise AssertionError("\n跳转页面不正确")

        # driver = Upload_Files.OpenUploadFiles(driver)# 重新打开上传页面
        # time.sleep(1)

        # 上传系统大小超过500M的视频
        file_name = "2020-10-14 09-55-45.mp4"
        driver.find_element_by_xpath(Upload_Files.upload_file_xpath).send_keys(Upload_Files.files_path + file_name)
        time.sleep(1)
        websitetips = website_tips.get_websitetips(driver)
        if (websitetips != "文件名：{}大小超过500M".format(file_name)):
            raise AssertionError("\n上传不支持的文件后，提示信息不正确！")
        website_tips.close_websitetips(driver)
        time.sleep(1)

        # 上传系统不支持格式的视频
        file_name = "2020-10-28 18-21-07.mkv"
        driver.find_element_by_xpath(Upload_Files.upload_file_xpath).send_keys(Upload_Files.files_path + file_name)
        time.sleep(1)
        print(file_name)
        websitetips = website_tips.get_websitetips(driver)
        print(websitetips)
        if (websitetips != "文件名：{}格式无效".format(file_name)):
            raise AssertionError("\n上传不支持的文件后，提示信息不正确！")
        website_tips.close_websitetips(driver)
        time.sleep(1)

        time.sleep(10000)

        driver.close()

    # 测试上传mht文件

    def test_Upload_Mht_Files(self):
        driver = self.driver
        # # 打开上传页面
        # driver = Upload_Files.OpenUploadFiles(driver)
        # # 鼠标悬停"上传"按钮，查看效果
        # above = driver.find_element_by_xpath(Upload_Files.upload_xpath)  # 移动光标至"上传"按钮
        # ActionChains(driver).move_to_element(above).perform()
        # time.sleep(2)  # 预留时间查看效果
        #
        file_name = "《最强蜗牛》iOS官方15.mht"
        # driver.find_element_by_xpath(Upload_Files.upload_file_xpath).send_keys(Upload_Files.files_path + file_name)
        # time.sleep(1)

        txtname_count, imagename_count = read_mht.readmht(Upload_Files.files_path + file_name)
        print(txtname_count, imagename_count)

        driver.close()

    @staticmethod
    def OpenUploadFiles(driver):  # 打开上传文件页面
        time.sleep(1)
        # 点击菜单栏系统管理
        try:
            driver.implicitly_wait(1)
            driver.find_element_by_xpath(Upload_Files.upload_files_xpath).click()
            time.sleep(1)
        except:
            driver.find_element_by_xpath(Upload_Files.audit_content_xpath).click()
            time.sleep(1)
            # 点击菜单栏操作日志
            driver.find_element_by_xpath(Upload_Files.upload_files_xpath).click()
            time.sleep(1)
        finally:
            driver.implicitly_wait(30)

        return driver

    @staticmethod
    def UploadFile(driver, writedata=0):  # 上传文件
        # 打开上传页面
        driver = Upload_Files.OpenUploadFiles(driver)
        if writedata:
            filename = data.get_file_name(Upload_Files.files_path2)
            driver.find_element_by_xpath(Upload_Files.upload_file_xpath).send_keys(Upload_Files.files_path2 + filename)
        else:
            driver.find_element_by_xpath(Upload_Files.upload_file_xpath).send_keys(
                Upload_Files.files_path2 + "pic3.jpg")
        driver = website_tips.waitupload(driver)  # 等待上传，成功后打开工单池页面
        time.sleep(3)  # 2021-01-14,测试发现跳转工单池界面有点慢，等待时间从1秒改为3秒
        if writedata:  # 记录上传文件名和文件类型
            picturelist = ['png', 'bmp', 'jpeg', 'gif', 'jpg']
            videolist = ['mp4']
            textlist = ['txt']
            suffix = re.split('\.', filename)[1]
            if (suffix in picturelist):
                filetype = '图片'
            elif (suffix in videolist):
                filetype = '视频'
            elif (suffix in textlist):
                filetype = '文本'
            else:
                filetype = '未知'
            timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            workxls.writedata('workorderdata.xls', filename, filetype, timestr)
        # else: # 11月19日，看似无用部分，先注释掉，后续可能有用
        #     driver = Upload_Files.OpenUploadFiles(driver)  # 重新打开上传页面
        time.sleep(1)

        return driver

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
