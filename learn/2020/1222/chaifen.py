# -*- coding: utf-8 -*-

import re

url = "C:\\Users\\19144\\Desktop\\xs\\xz\\booklist.csv"

f = open("C:\\Users\\19144\\Desktop\\xs\\xz\\booklist_女.csv", "w")
f.writelines("书名,字数,简介\n")
f.close()

f = open("C:\\Users\\19144\\Desktop\\xs\\xz\\booklist_男.csv", "w")
f.writelines("书名,字数,简介\n")
f.close()
strtmp = ""
h = open(url, "r")
for sstr in h.readlines():
    if (sstr == strtmp):
        continue
    if (re.findall("书名,字数,简介", sstr)):
        continue
    if (re.findall("她", sstr) or re.findall("媳", sstr) or re.findall("妻", sstr)):
        f = open("C:\\Users\\19144\\Desktop\\xs\\xz\\booklist_女.csv", "a")
        f.writelines(sstr)
        f.close()
    else:
        f = open("C:\\Users\\19144\\Desktop\\xs\\xz\\booklist_男.csv", "a")
        f.writelines(sstr)
        f.close()
    strtmp = sstr
