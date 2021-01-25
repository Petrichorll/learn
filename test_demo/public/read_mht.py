# -*- coding: utf-8 -*-
import os
import base64
import re
import lxml
from bs4 import BeautifulSoup
import sys
import uuid


class ReadMht(object):
    def __init__(self, path):
        self.path = path
        self.content = []
        self.boundary = None
        self.html = None
        self.images = None
        self.savepath = os.path.abspath("") + "/"
        self.tn = re.compile(r'日期: (\d{4}-[01][\d]-[0-3][\d])')
        # self.txtformat = re.compile(r"(.*\d*\)\d{2}:\d{2}:\d{2})(.*)")
        self.txtformat = re.compile(r"(.*\d*\d{2}:\d{2}:\d{2})(.*)")
        self.formatmht()

    def getHtml(self):
        for content in self.content:
            for ct in content:
                if "Content-Type: text/html" in ct:
                    self.html = content[-1]
                    self.content.remove(content)
                    break

    def getImages(self):
        tmp = {}
        for content in self.content:
            ext = ''
            dat = ''
            for ct in content:
                if "Content-Type:image" in ct:
                    ext = ct.strip().rsplit("/")[-1]
                    continue
                if "Content-Location" in ct:
                    dat = re.match(r'Content-Location:{(.*)}.dat', ct.strip())
                    key = dat.group(1)
                    tmp[key] = ("." + ext, content[-1])
                    self.images = tmp
                    continue

    def formatmht(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                content = []
                for line in lines:
                    if "------=" in line:
                        if len(content) != 0:
                            tmp = []
                            strc = ''
                            for ct in content:
                                if ct.strip().startswith("Content"):
                                    tmp.append(ct)
                                else:
                                    strc += ct
                            tmp.append(strc)
                            self.content.append(tmp)
                            content = []
                            continue
                    content.append(line.strip())
        except Exception as e:
            pass

    def savetxt(self, name, content):
        print(name)
        if not os.path.exists(self.savepath + "mhttext/"):
            os.mkdir(self.savepath + "mhttext/")
        with open(self.savepath + "mhttext/" + name, "w") as f:
            f.write(content)

    def saveimages(self, name, content):
        if not os.path.exists(self.savepath + "mhtimages/"):
            os.mkdir(self.savepath + "mhtimages/")
        name = name.replace(":", "-")
        with open(self.savepath + "mhtimages/" + name, "wb") as f:
            f.write(content)

    def outcontent(self, ifmy=0):
        text = []
        # 获取html，即文本
        self.getHtml()
        soup = BeautifulSoup(self.html, 'lxml')
        divs = soup.find_all('td')
        txtname = ''
        tcontent = ''
        txtname_list = []
        imagename_list = []

        # 获取时间和图片
        self.imglist = {}
        for div in divs:
            t = div.text
            tnn = self.tn.match(t.strip())
            if tnn:
                if txtname:
                    if (ifmy == 0):
                        self.savetxt(txtname, tcontent)
                    else:
                        txtname_list.append(txtname)
                    tcontent = ''
                txtname = tnn.group(1) + ".txt"
            tc = self.txtformat.findall(t)
            if tc:
                tcontent += tc[0][0] + "\n" + "".join(tc[0][1].split()) + "\n"
            if div.img:
                self.imglist[div.img["src"].split(".")[0][1:-1]] = tc[0][0]
                count = 1
                for sibling in div.img.next_siblings:
                    self.imglist[sibling["src"].split(".")[0][1:-1]] = tc[0][0] + "_" + str(count)
                    count += 1
        if txtname:
            if (ifmy == 0):
                self.savetxt(txtname, tcontent)
            else:
                txtname_list.append(txtname)
        self.getImages()
        notexist = set(self.imglist) - set(self.images)
        for k, v in self.imglist.items():
            if k in notexist:
                continue
            content = base64.b64decode(self.images[k][1])
            if (ifmy == 0):
                self.saveimages(v + self.images[k][0], content)
            else:
                imagename_list.append(v + self.images[k][0])

        return txtname_list, imagename_list

    def my_outcontent(self):
        txtname_list = []
        imagename_list = []
        txtname_list, imagename_list_f = self.outcontent(1)

        for name in imagename_list_f:
            name = name.replace(":", "-")
            imagename_list.append(name)
        # print(txtname_list, imagename_list)
        # print(len(txtname_list), len(imagename_list))
        txtname_count = len(txtname_list)
        imagename_count = len(imagename_list)
        return txtname_count, imagename_count


def readmht(filepath):
    if not os.path.exists(filepath):
        return None,None
    rmht = ReadMht(path=filepath)

    txtname_count, imagename_count = rmht.my_outcontent()
    # print(txtname_count, imagename_count)
    return txtname_count, imagename_count


if __name__ == "__main__":
    filepath = "《最强蜗牛》iOS官方15.mht"
    print(readmht(filepath))

