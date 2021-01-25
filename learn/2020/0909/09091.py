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
                    tmp[key] = ("."+ext, content[-1])
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
        if not os.path.exists(self.savepath+"mhttext/"):
            os.mkdir(self.savepath+"mhttext/")
        with open(self.savepath+"mhttext/"+name, "w") as f:
            f.write(content)

    def saveimages(self, name, content):
        if not os.path.exists(self.savepath+"mhtimages/"):
            os.mkdir(self.savepath+"mhtimages/")
        name = name.replace(":","-")
        with open(self.savepath+"mhtimages/"+name, "wb") as f:
            f.write(content)
    def outcontent(self):
        text = []
        # 获取html，即文本
        self.getHtml()
        soup = BeautifulSoup(self.html, 'lxml')
        divs = soup.find_all('td')
        txtname = ''
        tcontent = ''
        # 获取时间和图片
        self.imglist = {}
        for div in divs:
            t = div.text
            tnn = self.tn.match(t.strip())
            if tnn:
                if txtname:
                    self.savetxt(txtname, tcontent)
                    tcontent = ''
                txtname = tnn.group(1)+".txt"
            tc = self.txtformat.findall(t)
            if tc:
                tcontent += tc[0][0]+"\n"+"".join(tc[0][1].split()) + "\n"
            if div.img:
                self.imglist[div.img["src"].split(".")[0][1:-1]] = tc[0][0]
                count = 1
                for sibling in div.img.next_siblings:
                    self.imglist[sibling["src"].split(".")[0][1:-1]] = tc[0][0]+"_"+str(count)
                    count += 1
        if txtname:
            self.savetxt(txtname, tcontent)
        self.getImages()
        notexist = set(self.imglist)-set(self.images)
        for k, v in self.imglist.items():
            if k in notexist:
                continue
            content = base64.b64decode(self.images[k][1])
            self.saveimages(v+self.images[k][0], content)



if __name__ == "__main__":
    filepath = "MHT3.mht"
    rmht = ReadMht(path=filepath)
    rmht.outcontent()
