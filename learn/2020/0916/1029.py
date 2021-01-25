# -*- coding: utf-8 -*-

import re, requests

str2 = "https://play-tx-ugcpub.douyucdn2.cn/live/high_15363392120201029132337-upload-c221/playlist.m3u8?tlink=5f9aaa87&tplay=5f9b3727&exper=0&nlimit=5&us=ab7003ae17ec9f15dc4a3dc800081501&sign=6c0145b3a1b92d805d6ee4f3c1b8869a&u=0&d=ab7003ae17ec9f15dc4a3dc800081501&ct=web&vid=16882405&pt=2&cdn=tx"
str2 = "https://play-tx-ugcpub.douyucdn2.cn/live/high_15363392120201029132337-upload-c221/playlist.m3u8?tlink=5f9abc91&tplay=5f9b4931&exper=0&nlimit=5&us=ab7003ae17ec9f15dc4a3dc800081501&sign=b2f2ec0459b17691a11efeb9cc4b66b4&u=0&d=ab7003ae17ec9f15dc4a3dc800081501&ct=web&vid=16882405&pt=2&cdn=tx"
str7 = "C:\\Users\\19144\\Desktop\\"

rebs = requests.get(str2)
kk = rebs.content.decode()
pp = re.findall("tran.+ts", kk)
ww = re.findall("transcode_\d+", kk)

jj = re.split("playlist\.m3u8", str2)

for str4 in pp:
    str3 = jj[0] + str4 + jj[1]
    print(str3)
    str8 = str7 + ww[0] + r"\\\\" + str4
    reb = requests.get(str3)
    with open(str8, 'wb') as f:
        f.write(reb.content)

