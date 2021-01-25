# -*- coding: utf-8 -*-


import re

h = []
f = open(r"C:\Users\19144\Desktop\333.txt", "r", encoding="utf-8")
for sstr in f.readlines():
    hh = re.findall("{.+?}\.dat", sstr)
    if (hh):
        i = 0
        while (i < len(hh)):
            s = hh[i]
            ss = re.sub("{", "", re.sub("}.dat", "", s))
            h.append(ss)
            i = i + 1
print(h)
print(len(h))

f=set(h)

print(f)
print(len(f))

