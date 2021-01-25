#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests, re


class youdao_trs():
    def __init__(self, str):
        self.url = "http://m.youdao.com/translate"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Mobile Safari/537.36 Edg/84.0.522.63"}
        self.data = {"inputtext": str, "type": "AUTO"}

    def fun(self):
        reb = requests.post(self.url, headers=self.headers, data=self.data)
        rstr = reb.content.decode()
        # rstr = "<ul id=\"translateResult\"><li>hhh</li>"
        regex = re.compile('<li>.*</li>')
        ret = regex.findall(rstr)
        rstr = ret[len(ret) - 1]
        rstr = re.sub("<li>", "", rstr)
        rstr = re.sub("</li>", "", rstr)
        return rstr


if __name__ == "__main__":
    h = youdao_trs("星期天")
    ret = h.fun()
    print(ret)
    # rstr = r"<ul id=\"translateResult\"><li>hhh</li>"
    # regex = re.compile('<ul id="translateResult"><li>.*</li>')
    # ret = regex.search(rstr)
    # print(ret[0])
