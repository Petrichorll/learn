# -*- coding: utf-8 -*-


import re

fpath = "C:\\Users\\19144\\Desktop\微博\\442434.txt"
f = open("C:\\Users\\19144\\Desktop\微博\\44243.txt", 'r')
h = open(fpath, "a")
hstr = ''

for sstr in f.readlines():
    if (re.findall(',',sstr)):
        h.writelines(sstr)


